"""Epistemic Recovery Audit.

Inference-only successor to the Minimal Admissible Evidence-Action Topology Audit.
The upstream evidence/action topology is inherited unchanged. The learner receives
only anonymous binary channel observations and D/R/S labels on a minimal teaching
set, then predicts D/R/S on held-out evidence combinations.

No repair construction, authorization, binding, or persistence is present.
Standard library only; deterministic apart from fixed-seed channel encodings.
"""

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from random import Random

from minimal_admissible_evidence_action_topology import (
    ADMISSIBLE,
    D,
    R,
    S,
    WORLDS as BASELINE_WORLDS,
)

ACTIONS = (D, R, S)
ENCODINGS = 64
BINARY_UNIVERSE = tuple(product((0, 1), repeat=4))
INDEX = {x: i for i, x in enumerate(BINARY_UNIVERSE)}

# The four roles are evaluator-side only. The learner never receives these names.
EXPECTED_FIELDS = (
    "residual_present",
    "exact_h0_alternative",
    "deterministic_residual",
    "positive_reopen_value",
)
assert tuple(c.field for c in ADMISSIBLE) == EXPECTED_FIELDS
assert tuple(c.mode for c in ADMISSIBLE) == ("passive", "active", "active", "active")


def required_action(bits):
    """Evaluator-supplied D/R/S contract extending the frozen five-world cases."""
    residual, exact_alt, deterministic, positive_value = bits
    if residual and exact_alt:
        return D
    if residual and (not exact_alt) and deterministic and positive_value:
        return R
    return S


TARGET = tuple(required_action(x) for x in BINARY_UNIVERSE)

# Verify that the evaluator rule exactly reproduces all five f4f2f33 worlds.
for world in BASELINE_WORLDS:
    signature = tuple(getattr(world, field) for field in EXPECTED_FIELDS)
    assert required_action(signature) == world.required_action

# A minimal teaching set for the supplied ordered-decision-list inference language.
# It contains all three action labels; the other 11/16 evidence combinations are held out.
TEACHING_SIGNATURES = (
    (0, 1, 0, 0),  # S
    (1, 0, 0, 1),  # S
    (1, 0, 1, 0),  # S
    (1, 0, 1, 1),  # R
    (1, 1, 0, 0),  # D
)
TRAIN_CANONICAL = tuple(INDEX[x] for x in TEACHING_SIGNATURES)
HELDOUT_CANONICAL = tuple(i for i in range(len(BINARY_UNIVERSE)) if i not in TRAIN_CANONICAL)
assert len(TRAIN_CANONICAL) == 5
assert len(HELDOUT_CANONICAL) == 11
assert {TARGET[i] for i in TRAIN_CANONICAL} == set(ACTIONS)


def eval_program(program, x):
    tests, default = program
    for column, value, label in tests:
        if x[column] == value:
            return label
    return default


def enumerate_semantic_hypotheses(n_features=4):
    """Enumerate unique ordered-decision-list semantics and minimum rule length."""
    min_length = {}
    example = {}
    for length in range(n_features + 1):
        for order in permutations(range(n_features), length):
            for values in product((0, 1), repeat=length):
                for labels in product(ACTIONS, repeat=length):
                    for default in ACTIONS:
                        program = (tuple(zip(order, values, labels)), default)
                        semantic = tuple(eval_program(program, x) for x in BINARY_UNIVERSE)
                        if semantic not in min_length:
                            min_length[semantic] = length
                            example[semantic] = program
    return min_length, example


SEMANTIC_MIN_LENGTH, SEMANTIC_EXAMPLE = enumerate_semantic_hypotheses()
SEMANTICS = tuple(sorted(SEMANTIC_MIN_LENGTH))
CANDIDATE_COUNT = len(SEMANTICS)
assert CANDIDATE_COUNT == 16827
assert TARGET in SEMANTIC_MIN_LENGTH
assert SEMANTIC_MIN_LENGTH[TARGET] == 4


def consistent_semantics(train_observations, train_labels):
    pairs = tuple((INDEX[x], y) for x, y in zip(train_observations, train_labels))
    return tuple(
        semantic
        for semantic in SEMANTICS
        if all(semantic[idx] == label for idx, label in pairs)
    )


def teaching_set_is_minimal():
    labels = tuple(required_action(x) for x in TEACHING_SIGNATURES)
    consistent = consistent_semantics(TEACHING_SIGNATURES, labels)
    assert consistent == (TARGET,)
    for removed in range(len(TEACHING_SIGNATURES)):
        obs = TEACHING_SIGNATURES[:removed] + TEACHING_SIGNATURES[removed + 1 :]
        lab = labels[:removed] + labels[removed + 1 :]
        assert len(consistent_semantics(obs, lab)) > 1
    return True


assert teaching_set_is_minimal()


def make_encoding(seed):
    """Hide channel role and bit polarity with a run-specific bijection."""
    rng = Random(seed)
    canonical_columns = list(range(4))
    rng.shuffle(canonical_columns)
    polarity_flips = [rng.randrange(2) for _ in range(4)]

    def encode(bits):
        return tuple(
            bits[canonical_column] ^ polarity_flips[observed_column]
            for observed_column, canonical_column in enumerate(canonical_columns)
        )

    return tuple(canonical_columns), tuple(polarity_flips), encode


def masked_observation(encoded, observed_column):
    """Matched-width information ablation: replace one channel by a constant token."""
    return tuple(0 if j == observed_column else value for j, value in enumerate(encoded))


def choose_learner_semantic(train_observations, train_labels):
    """ERM over anonymous ordered decision lists; uses no canonical channel semantics."""
    observed_indices = tuple(INDEX[x] for x in train_observations)
    best_semantic = None
    best_key = None
    best_correct = -1
    for semantic in SEMANTICS:
        correct = sum(
            semantic[idx] == label
            for idx, label in zip(observed_indices, train_labels)
        )
        key = (-correct, SEMANTIC_MIN_LENGTH[semantic], semantic)
        if best_key is None or key < best_key:
            best_key = key
            best_semantic = semantic
            best_correct = correct
    return best_semantic, best_correct / len(train_labels)


def predict_semantic(semantic, observation):
    return semantic[INDEX[observation]]


def accuracy(semantic, observations, labels):
    return sum(
        predict_semantic(semantic, obs) == label
        for obs, label in zip(observations, labels)
    ) / len(labels)


def bayes_ceiling(observations, labels):
    """Uniform-distribution Bayes-optimal accuracy allowed by the observation quotient."""
    groups = defaultdict(Counter)
    for obs, label in zip(observations, labels):
        groups[obs][label] += 1
    correct = sum(max(counts.values()) for counts in groups.values())
    return correct / len(labels)


def memorization_baseline(train_observations, train_labels, heldout_observations):
    """Exact-signature lookup with majority default; cannot infer unseen combinations."""
    lookup = dict(zip(train_observations, train_labels))
    majority = Counter(train_labels).most_common(1)[0][0]
    return tuple(lookup.get(obs, majority) for obs in heldout_observations)


def confusion(labels, predictions):
    out = {action: Counter() for action in ACTIONS}
    for truth, pred in zip(labels, predictions):
        out[truth][pred] += 1
    return {truth: dict(counts) for truth, counts in out.items()}


def run_condition(seed, removed_canonical=None):
    canonical_columns, polarity_flips, encode = make_encoding(seed)
    encoded_all = tuple(encode(x) for x in BINARY_UNIVERSE)

    removed_observed = None
    if removed_canonical is not None:
        removed_observed = canonical_columns.index(removed_canonical)
        observed_all = tuple(
            masked_observation(obs, removed_observed) for obs in encoded_all
        )
    else:
        observed_all = encoded_all

    train_obs = tuple(observed_all[i] for i in TRAIN_CANONICAL)
    train_labels = tuple(TARGET[i] for i in TRAIN_CANONICAL)
    heldout_obs = tuple(observed_all[i] for i in HELDOUT_CANONICAL)
    heldout_labels = tuple(TARGET[i] for i in HELDOUT_CANONICAL)

    learned, train_acc = choose_learner_semantic(train_obs, train_labels)
    heldout_acc = accuracy(learned, heldout_obs, heldout_labels)
    full_acc = accuracy(learned, observed_all, TARGET)
    ceiling = bayes_ceiling(observed_all, TARGET)
    assert full_acc <= ceiling + 1e-12

    heldout_pred = tuple(predict_semantic(learned, obs) for obs in heldout_obs)
    full_pred = tuple(predict_semantic(learned, obs) for obs in observed_all)

    baseline_pred = memorization_baseline(train_obs, train_labels, heldout_obs)
    baseline_acc = sum(
        pred == truth for pred, truth in zip(baseline_pred, heldout_labels)
    ) / len(heldout_labels)

    return {
        "seed": seed,
        "removed_canonical_component": (
            None if removed_canonical is None else ADMISSIBLE[removed_canonical].name
        ),
        "removed_observed_column": removed_observed,
        "channel_permutation_hidden": canonical_columns,
        "polarity_flips_hidden": polarity_flips,
        "train_accuracy": train_acc,
        "heldout_accuracy": heldout_acc,
        "full_universe_accuracy": full_acc,
        "bayes_ceiling_full_universe": ceiling,
        "heldout_confusion": confusion(heldout_labels, heldout_pred),
        "full_confusion": confusion(TARGET, full_pred),
        "memorization_baseline_heldout_accuracy": baseline_acc,
        "candidate_semantics_evaluated": CANDIDATE_COUNT,
        "training_examples": len(TRAIN_CANONICAL),
        "heldout_combinations": len(HELDOUT_CANONICAL),
        "evaluation_combinations": len(BINARY_UNIVERSE),
        "terminal_output_only": True,
    }


def audit():
    intact = []
    ablated = {c.name: [] for c in ADMISSIBLE}

    for seed in range(ENCODINGS):
        result = run_condition(seed)
        assert result["train_accuracy"] == 1.0
        assert result["heldout_accuracy"] == 1.0
        assert result["full_universe_accuracy"] == 1.0
        assert result["bayes_ceiling_full_universe"] == 1.0
        assert result["memorization_baseline_heldout_accuracy"] == 8 / 11
        intact.append(result)

        for canonical_index, component in enumerate(ADMISSIBLE):
            masked = run_condition(seed, removed_canonical=canonical_index)
            ablated[component.name].append(masked)

    expected_ceilings = {
        "local_residual": 11 / 16,
        "alternative_fit_probe": 12 / 16,
        "consistency_probe": 15 / 16,
        "future_value_probe": 15 / 16,
    }
    expected_observed = {
        "local_residual": 10 / 16,
        "alternative_fit_probe": 10 / 16,
        "consistency_probe": 15 / 16,
        "future_value_probe": 15 / 16,
    }

    ablation_summary = {}
    for component in ADMISSIBLE:
        rows = ablated[component.name]
        ceilings = {row["bayes_ceiling_full_universe"] for row in rows}
        observed = {row["full_universe_accuracy"] for row in rows}
        assert ceilings == {expected_ceilings[component.name]}
        assert observed == {expected_observed[component.name]}
        assert all(
            row["full_universe_accuracy"]
            <= row["bayes_ceiling_full_universe"] + 1e-12
            for row in rows
        )
        ablation_summary[component.name] = {
            "bayes_ceiling": next(iter(ceilings)),
            "learner_full_accuracy": next(iter(observed)),
            "ceiling_respected_all_encodings": True,
            "candidate_semantics_evaluated": CANDIDATE_COUNT,
        }

    matched_resources = {
        "anonymous_channels": 4,
        "candidate_semantics_evaluated": CANDIDATE_COUNT,
        "training_examples": len(TRAIN_CANONICAL),
        "heldout_combinations": len(HELDOUT_CANONICAL),
        "evaluation_combinations": len(BINARY_UNIVERSE),
    }
    for rows in ablated.values():
        for row in rows:
            assert row["candidate_semantics_evaluated"] == CANDIDATE_COUNT
            assert row["training_examples"] == len(TRAIN_CANONICAL)
            assert row["heldout_combinations"] == len(HELDOUT_CANONICAL)
            assert row["evaluation_combinations"] == len(BINARY_UNIVERSE)

    return {
        "baseline_commit": "f4f2f33f6d25d5c35b9bc2c5452c78a6c570fdb4",
        "contract": {
            "epistemic_topology_inherited_unchanged": True,
            "semantic_channel_names_visible_to_learner": False,
            "canonical_bit_polarity_visible_to_learner": False,
            "channel_order_visible_as_semantics": False,
            "terminal_actions": ACTIONS,
            "repair_authority": False,
            "repair_construction": False,
            "binding": False,
            "persistence": False,
        },
        "inference_language": {
            "type": "ordered decision lists over anonymous binary channels",
            "unique_semantics": CANDIDATE_COUNT,
            "target_min_rule_length": SEMANTIC_MIN_LENGTH[TARGET],
            "teaching_set_size": len(TRAIN_CANONICAL),
            "teaching_set_minimal_within_language": True,
            "heldout_combination_count": len(HELDOUT_CANONICAL),
        },
        "intact": {
            "encodings": ENCODINGS,
            "train_accuracy": 1.0,
            "heldout_accuracy": 1.0,
            "full_universe_accuracy": 1.0,
            "oracle_identifiability_ceiling": 1.0,
            "memorization_baseline_heldout_accuracy": 8 / 11,
            "all_encodings_exact": True,
        },
        "ablated_information_controls": ablation_summary,
        "matched_resources": matched_resources,
        "boundary": {
            "finite_binary_evidence_family": True,
            "decision_contract_evaluator_supplied": True,
            "ordered_decision_list_language_supplied": True,
            "five_label_teaching_set_supplied": True,
            "unique_R_signature_in_frozen_binary_contract": True,
            "heldout_R_combination_test": False,
            "general_inference_claim": False,
            "repair_or_authorization_claim": False,
        },
    }


def print_report(result):
    print("Epistemic Recovery Audit")
    print("baseline:", result["baseline_commit"][:7])
    print("intact heldout accuracy:", result["intact"]["heldout_accuracy"])
    print("memorization baseline:", result["intact"]["memorization_baseline_heldout_accuracy"])
    print("candidate semantics:", result["inference_language"]["unique_semantics"])
    print("ablated controls:")
    for name, info in result["ablated_information_controls"].items():
        print(
            " ",
            name,
            "learner=",
            info["learner_full_accuracy"],
            "ceiling=",
            info["bayes_ceiling"],
        )
    print("repair authority:", result["contract"]["repair_authority"])


if __name__ == "__main__":
    result = audit()
    print_report(result)
