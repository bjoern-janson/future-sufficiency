"""Active Evidence Acquisition Audit.

Inference-to-agency successor to the frozen epistemic baselines f4f2f33 and 3166f5b.
The evidence/action topology and D/R/S inference language are unchanged. The only
new mechanism is decision-directed selection of which already-admissible anonymous
challenge channel to query next under partial evidence.

The audit terminates at a D/R/S prediction. It contains no repair construction,
repair authorization, binding, persistence, or self-modification.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from math import log2

from epistemic_recovery_audit import (
    ACTIONS,
    ADMISSIBLE,
    BINARY_UNIVERSE,
    CANDIDATE_COUNT,
    INDEX,
    TARGET,
    TEACHING_SIGNATURES,
    choose_learner_semantic,
    make_encoding,
    predict_semantic,
)

NO_PROBE = "NO_PROBE"
ENCODINGS = 64
BASELINE_IDENTIFIABILITY = "f4f2f33f6d25d5c35b9bc2c5452c78a6c570fdb4"
BASELINE_INFERENCE = "3166f5bdaa5d14f2d606f5a1dfc84b0d68af9ff9"
DECISION_CORRECT_VALUE = 10.0
ACTIVE_PROBE_COST = 1.0

assert len(ADMISSIBLE) == 4
assert ADMISSIBLE[0].mode == "passive"
assert all(c.mode == "active" for c in ADMISSIBLE[1:])
assert tuple(c.cost for c in ADMISSIBLE) == (0.0, 1.0, 1.0, 1.0)
assert tuple(c.name for c in ADMISSIBLE) == (
    "local_residual",
    "alternative_fit_probe",
    "consistency_probe",
    "future_value_probe",
)


def compatible_completions(partial):
    """All encoded 4-bit worlds consistent with a partial anonymous observation."""
    return tuple(
        x for x in BINARY_UNIVERSE
        if all(value is None or x[j] == value for j, value in enumerate(partial))
    )


def action_counts(semantic, completions):
    return Counter(predict_semantic(semantic, x) for x in completions)


def bayes_action_accuracy(semantic, partial):
    completions = compatible_completions(partial)
    counts = action_counts(semantic, completions)
    return max(counts.values()) / len(completions)


def decision_value(semantic, partial, probe_column):
    """Expected gain in Bayes D/R/S accuracy from querying one anonymous channel."""
    completions = compatible_completions(partial)
    before = bayes_action_accuracy(semantic, partial)
    correct_after = 0
    for token in (0, 1):
        group = tuple(x for x in completions if x[probe_column] == token)
        if not group:
            continue
        correct_after += max(action_counts(semantic, group).values())
    after = correct_after / len(completions)
    return after - before, after


def outcome_entropy(partial, probe_column):
    """Shannon entropy of a probe outcome under uniform compatible completions."""
    completions = compatible_completions(partial)
    counts = Counter(x[probe_column] for x in completions)
    total = len(completions)
    h = 0.0
    for count in counts.values():
        p = count / total
        h -= p * log2(p)
    return h


def optimal_policy_value(semantic, partial, available_columns):
    """Dynamic-programming value of sequential information acquisition.

    Utility is evaluator-side decision correctness value minus inherited equal
    probe cost. This is experiment-selection value only; it grants no repair authority.
    """

    @lru_cache(None)
    def solve(partial_state, available_state):
        current = bayes_action_accuracy(semantic, partial_state)
        values = {NO_PROBE: DECISION_CORRECT_VALUE * current}
        completions = compatible_completions(partial_state)

        for column in available_state:
            expected = -ACTIVE_PROBE_COST
            for token in (0, 1):
                group = tuple(x for x in completions if x[column] == token)
                if not group:
                    continue
                probability = len(group) / len(completions)
                next_partial = list(partial_state)
                next_partial[column] = token
                next_available = tuple(c for c in available_state if c != column)
                expected += probability * solve(tuple(next_partial), next_available)[0]
            values[column] = expected

        best = max(values.values())
        optimal = tuple(
            key for key, value in values.items()
            if abs(value - best) < 1e-12
        )
        return best, optimal, values

    return solve(tuple(partial), tuple(sorted(available_columns)))


def evaluator_optimal_set(semantic, partial, available_columns):
    _, optimal, values = optimal_policy_value(semantic, partial, available_columns)
    return optimal, values


def learner_select_probe(learned_semantic, partial, available_columns):
    """Select the anonymous challenge maximizing learned sequential decision value."""
    _, optimal, values = optimal_policy_value(
        learned_semantic, partial, available_columns
    )
    if NO_PROBE in optimal:
        return NO_PROBE, optimal, values
    return min(optimal), optimal, values


def entropy_baseline(partial, available_columns):
    """Max-outcome-entropy baseline; ties by smallest anonymous column."""
    if not available_columns:
        return NO_PROBE
    entropies = {c: outcome_entropy(partial, c) for c in available_columns}
    best = max(entropies.values())
    return min(c for c, h in entropies.items() if h == best)


def final_action(semantic, partial):
    completions = compatible_completions(partial)
    counts = action_counts(semantic, completions)
    best_count = max(counts.values())
    return min(a for a, count in counts.items() if count == best_count)


def true_encoded_semantic(encode):
    """Evaluator D/R/S function represented in the run's anonymous encoding."""
    by_encoded = {}
    for canonical, label in zip(BINARY_UNIVERSE, TARGET):
        by_encoded[encode(canonical)] = label
    return tuple(by_encoded[x] for x in BINARY_UNIVERSE)


def train_inference_semantic(encode, masked_canonical=None):
    encoded = tuple(encode(x) for x in TEACHING_SIGNATURES)
    if masked_canonical is not None:
        # Locate the observed column corresponding to the ablated canonical channel.
        canonical_columns, _, _ = current_encoding_metadata
        observed = canonical_columns.index(masked_canonical)
        encoded = tuple(
            tuple(0 if j == observed else value for j, value in enumerate(obs))
            for obs in encoded
        )
    labels = tuple(TARGET[INDEX[x]] for x in TEACHING_SIGNATURES)
    learned, train_acc = choose_learner_semantic(encoded, labels)
    return learned, train_acc


# Set during each encoded run so the masked learner uses exactly the same channel map.
current_encoding_metadata = None


def mask_world(encoded_world, removed_observed):
    if removed_observed is None:
        return encoded_world
    return tuple(
        0 if j == removed_observed else value
        for j, value in enumerate(encoded_world)
    )


def run_episode(
    learned_semantic,
    evaluator_semantic,
    encoded_world,
    passive_column,
    active_columns,
):
    partial = [None] * 4
    partial[passive_column] = encoded_world[passive_column]
    available = set(active_columns)

    steps = []
    entropy_choices = []
    while True:
        evaluator_optimal, evaluator_values = evaluator_optimal_set(
            evaluator_semantic, tuple(partial), tuple(sorted(available))
        )
        selected, learner_optimal, learner_values = learner_select_probe(
            learned_semantic, tuple(partial), tuple(sorted(available))
        )

        entropy_choice = entropy_baseline(tuple(partial), tuple(sorted(available)))
        entropy_choices.append(entropy_choice)

        steps.append(
            {
                "selected": selected,
                "evaluator_optimal": evaluator_optimal,
                "learner_internal_optimal": learner_optimal,
                "evaluator_values": evaluator_values,
                "learner_values": learner_values,
                "entropy_choice": entropy_choice,
                "partial_before": tuple(partial),
                "available_before": tuple(sorted(available)),
            }
        )

        if selected == NO_PROBE:
            break

        assert selected in available
        partial[selected] = encoded_world[selected]
        available.remove(selected)
        assert len(steps) <= 4

    predicted = final_action(learned_semantic, tuple(partial))
    evaluator_terminal = final_action(evaluator_semantic, tuple(partial))
    return {
        "steps": tuple(steps),
        "probe_count": sum(step["selected"] != NO_PROBE for step in steps),
        "predicted_action": predicted,
        "evaluator_terminal_action": evaluator_terminal,
        "terminal_partial": tuple(partial),
        "terminal_bayes_accuracy_evaluator": bayes_action_accuracy(
            evaluator_semantic, tuple(partial)
        ),
    }


def initial_information_vs_decision_control(
    evaluator_semantic, passive_column, active_columns, encoded_world
):
    """All probes have one bit entropy, but only one maximizes sequential decision value."""
    partial = [None] * 4
    partial[passive_column] = encoded_world[passive_column]
    entropies = {c: outcome_entropy(tuple(partial), c) for c in active_columns}
    _, optimal, values = optimal_policy_value(
        evaluator_semantic, tuple(partial), active_columns
    )
    probe_values = {c: values[c] for c in active_columns}
    return entropies, optimal, probe_values


def bayes_ceiling_from_visible_columns(evaluator_semantic, visible_columns):
    groups = defaultdict(Counter)
    for x in BINARY_UNIVERSE:
        sig = tuple(x[j] for j in visible_columns)
        groups[sig][predict_semantic(evaluator_semantic, x)] += 1
    return sum(max(c.values()) for c in groups.values()) / len(BINARY_UNIVERSE)


def audit():
    global current_encoding_metadata

    primary_correct = 0
    primary_total = 0
    active_correct = 0
    active_total = 0
    stop_correct = 0
    stop_total = 0
    final_correct = 0
    final_total = 0
    entropy_overall_correct = 0
    entropy_overall_total = 0
    entropy_first_step_correct = 0
    entropy_first_step_total = 0
    info_decision_controls = 0
    probe_counts = []

    ablation_rows = {c.name: [] for c in ADMISSIBLE}

    for seed in range(ENCODINGS):
        canonical_columns, polarity_flips, encode = make_encoding(seed)
        current_encoding_metadata = (canonical_columns, polarity_flips, encode)
        passive_column = canonical_columns.index(0)
        active_columns = tuple(sorted(canonical_columns.index(i) for i in (1, 2, 3)))

        learned, train_acc = train_inference_semantic(encode)
        assert train_acc == 1.0
        evaluator_semantic = true_encoded_semantic(encode)
        assert learned == evaluator_semantic

        # Decision value vs raw information: choose any residual-positive world.
        positive_world = encode((1, 0, 1, 1))
        entropies, initial_optimal, values = initial_information_vs_decision_control(
            evaluator_semantic, passive_column, active_columns, positive_world
        )
        assert set(entropies.values()) == {1.0}
        assert NO_PROBE not in initial_optimal
        assert len(initial_optimal) == 1
        best_value = max(values.values())
        assert list(values.values()).count(best_value) == 1
        first_partial = [None] * 4
        first_partial[passive_column] = positive_world[passive_column]
        first_entropy_choice = entropy_baseline(
            tuple(first_partial), tuple(sorted(active_columns))
        )
        entropy_first_step_total += 1
        entropy_first_step_correct += first_entropy_choice in initial_optimal
        info_decision_controls += 1

        for canonical_world, truth in zip(BINARY_UNIVERSE, TARGET):
            encoded_world = encode(canonical_world)
            episode = run_episode(
                learned,
                evaluator_semantic,
                encoded_world,
                passive_column,
                active_columns,
            )

            for step_index, step in enumerate(episode["steps"]):
                selected = step["selected"]
                optimal = step["evaluator_optimal"]
                correct = selected in optimal
                primary_correct += correct
                primary_total += 1

                if optimal == (NO_PROBE,):
                    stop_correct += correct
                    stop_total += 1
                else:
                    active_correct += correct
                    active_total += 1

                    # Entropy-only baseline is assessed only when a challenge is warranted.
                    entropy_overall_total += 1
                    entropy_overall_correct += step["entropy_choice"] in optimal

            final_correct += episode["predicted_action"] == truth
            final_total += 1
            assert episode["evaluator_terminal_action"] == truth
            assert episode["terminal_bayes_accuracy_evaluator"] == 1.0
            probe_counts.append(episode["probe_count"])

        # Leakage / impossibility controls: retrain under each matched-width masked channel.
        for canonical_index, component in enumerate(ADMISSIBLE):
            removed_observed = canonical_columns.index(canonical_index)
            masked_train = tuple(
                mask_world(encode(x), removed_observed)
                for x in TEACHING_SIGNATURES
            )
            train_labels = tuple(TARGET[INDEX[x]] for x in TEACHING_SIGNATURES)
            masked_learner, _ = choose_learner_semantic(masked_train, train_labels)

            # Evaluator semantic projected through the masked observation quotient.
            masked_obs_all = tuple(
                mask_world(encode(x), removed_observed) for x in BINARY_UNIVERSE
            )
            ceiling_groups = defaultdict(Counter)
            for obs, label in zip(masked_obs_all, TARGET):
                ceiling_groups[obs][label] += 1
            ceiling = sum(max(c.values()) for c in ceiling_groups.values()) / 16
            learner_acc = sum(
                predict_semantic(masked_learner, obs) == label
                for obs, label in zip(masked_obs_all, TARGET)
            ) / 16
            assert learner_acc <= ceiling + 1e-12
            ablation_rows[component.name].append((learner_acc, ceiling))

    expected_ceilings = {
        "local_residual": 11 / 16,
        "alternative_fit_probe": 12 / 16,
        "consistency_probe": 15 / 16,
        "future_value_probe": 15 / 16,
    }
    ablation_summary = {}
    for name, rows in ablation_rows.items():
        ceilings = {c for _, c in rows}
        assert ceilings == {expected_ceilings[name]}
        assert all(a <= c + 1e-12 for a, c in rows)
        ablation_summary[name] = {
            "bayes_ceiling": next(iter(ceilings)),
            "max_learner_accuracy": max(a for a, _ in rows),
            "ceiling_respected_all_encodings": True,
        }

    return {
        "baselines": {
            "identifiability": BASELINE_IDENTIFIABILITY,
            "inference": BASELINE_INFERENCE,
        },
        "contract": {
            "epistemic_topology_changed": False,
            "passive_component": ADMISSIBLE[0].name,
            "active_components": tuple(c.name for c in ADMISSIBLE[1:]),
            "challenge_identities_semantically_visible": False,
            "probe_authority_changed": False,
            "repair_construction": False,
            "repair_authorization": False,
            "binding": False,
            "persistence": False,
            "terminal_output": "D/R/S only",
        },
        "primary": {
            "probe_or_stop_selection_accuracy": primary_correct / primary_total,
            "warranted_probe_selection_accuracy": active_correct / active_total,
            "no_probe_when_identifiable_accuracy": stop_correct / stop_total,
            "decision_points": primary_total,
            "active_decision_points": active_total,
            "stop_decision_points": stop_total,
        },
        "secondary": {
            "terminal_DRS_accuracy": final_correct / final_total,
            "world_episodes": final_total,
            "mean_probe_count": sum(probe_counts) / len(probe_counts),
            "max_probe_count": max(probe_counts),
        },
        "information_vs_decision_value": {
            "controls_passed": info_decision_controls,
            "all_initial_active_probe_entropies_equal_one_bit": True,
            "unique_decision_optimal_probe_at_residual_positive_start": True,
            "entropy_only_first_step_accuracy": (
                entropy_first_step_correct / entropy_first_step_total
            ),
            "entropy_only_selection_accuracy_when_probe_warranted": (
                entropy_overall_correct / entropy_overall_total
            ),
        },
        "ablated_information_controls": ablation_summary,
        "matched_inference_resources": {
            "anonymous_channels": 4,
            "candidate_semantics": CANDIDATE_COUNT,
            "teaching_examples": len(TEACHING_SIGNATURES),
            "world_universe": len(BINARY_UNIVERSE),
        },
        "boundary": {
            "finite_binary_world_family": True,
            "uniform_completion_prior_supplied": True,
            "sequential_decision_value_planner_supplied": True,
            "decision_correct_value": DECISION_CORRECT_VALUE,
            "inherited_active_probe_cost": ACTIVE_PROBE_COST,
            "learned_DRS_semantic_supplied_by_previous_inference_stage": True,
            "probe_outcomes_binary_and deterministic": True,
            "general_experiment_selection_claim": False,
            "challenge_authorization_claim": False,
            "repair_claim": False,
        },
    }


def print_report(result):
    print("Active Evidence Acquisition Audit")
    print("identifiability baseline:", result["baselines"]["identifiability"][:7])
    print("inference baseline:", result["baselines"]["inference"][:7])
    print("probe/stop selection:", result["primary"]["probe_or_stop_selection_accuracy"])
    print("warranted probe selection:", result["primary"]["warranted_probe_selection_accuracy"])
    print("no-probe termination:", result["primary"]["no_probe_when_identifiable_accuracy"])
    print("terminal D/R/S:", result["secondary"]["terminal_DRS_accuracy"])
    print("mean probes:", result["secondary"]["mean_probe_count"])
    print("entropy-only first step:", result["information_vs_decision_value"]["entropy_only_first_step_accuracy"])
    print("entropy-only overall:", result["information_vs_decision_value"]["entropy_only_selection_accuracy_when_probe_warranted"])
    print("ablated ceilings:")
    for name, row in result["ablated_information_controls"].items():
        print(" ", name, "max learner=", row["max_learner_accuracy"], "ceiling=", row["bayes_ceiling"])
    print("repair authorization:", result["contract"]["repair_authorization"])


if __name__ == "__main__":
    print_report(audit())
