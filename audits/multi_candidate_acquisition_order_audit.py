"""Multi-Candidate Acquisition-Order Discriminant Audit.

Preregistered at c3816400ef6ffd61d02b3a5fceec2712de064357.

Primary question:
    candidate-vs-COMMIT -> multi-candidate acquisition ordering

The audit holds refinement geometry, sequential-refinement role, and termination role
fixed. It compares sign-only, sign+Pareto, compensated ordinal, max-only tournament,
and explicit cardinal-q representations. No target ranking or winner table is supplied.
"""

from collections import Counter, defaultdict
from itertools import product, permutations
from math import log2
import json
import random

from valuation_role_discriminant_audit import audit as valuation_role_audit


PREREGISTRATION_COMMIT = "c3816400ef6ffd61d02b3a5fceec2712de064357"
VALUATION_ANCHOR_COMMIT = "c97a5cfde0dba0052f63ab5636f574cd4c4d1f2e"
STOP_REGRESSION_COMMIT = "46943821f9dec0ed188410c5c22fcad0f21b5786"
ENCODINGS = 64
EPS = 1e-12

T, G1, G2, G3, N = range(5)
WORLDS = tuple(product((0, 1), repeat=5))
PANEL_NAMES = tuple(f"P{i}" for i in range(1, 9))

PANELS = {
    "P1": (("H", "H", 0.100), ("M", "M", 0.100), ("L", "L", 0.100)),
    "P2": (("M_a", "M", 0.050), ("M_b", "M", 0.100), ("M_c", "M", 0.200)),
    "P3": (("H", "H", 0.300), ("M", "M", 0.100), ("L", "L", 0.020)),
    "P4": (("H", "H", 0.450), ("M", "M", 0.080), ("L", "L", 0.010)),
    "P5": (("H", "H", 0.480), ("M", "M", 0.200), ("L", "L", 0.010)),
    "P6": (("H", "H", 0.300), ("M", "M", 0.050), ("L", "L", 0.010)),
    "P7": (("H", "H", 0.500), ("M", "M", 0.250), ("L", "L", 0.125)),
    "P8": (("H", "H", 0.550), ("M", "M", 0.100), ("L", "L", 0.200)),
}

EXPECTED = {
    "P1": frozenset(("H",)),
    "P2": frozenset(("M_a",)),
    "P3": frozenset(("H",)),
    "P4": frozenset(("M",)),
    "P5": frozenset(("L",)),
    "P6": frozenset(("H", "M")),
    "P7": frozenset(("COMMIT",)),
    "P8": frozenset(("M",)),
}

EXPECTED_RELEVANCE = {"H": 0.5, "M": 0.25, "L": 0.125}


def warranted_action(world):
    return world[T]


def gate_index(world):
    return (world[G1] << 2) | (world[G2] << 1) | world[G3]


def entropy(values):
    counts = Counter(values)
    total = len(values)
    return -sum((n / total) * log2(n / total) for n in counts.values())


def bayes_accuracy(worlds):
    counts = Counter(warranted_action(world) for world in worlds)
    return max(counts.values()) / len(worlds)


BASE_ACCURACY = bayes_accuracy(WORLDS)
assert abs(BASE_ACCURACY - 0.5) < EPS


def gate_permutation(seed):
    rng = random.Random((seed + 1) * 1000003 + 97)
    states = list(range(8))
    rng.shuffle(states)
    return tuple(states)


def evidence_outputs(kind, seed, flip):
    """Anonymous one-bit evidence realization with fixed relevance by family."""
    gates = gate_permutation(seed)
    if kind == "H":
        noise_states = set()
    elif kind == "M":
        noise_states = set(gates[:2])
    elif kind == "L":
        noise_states = set(gates[:3])
    else:
        raise ValueError(kind)

    return tuple(
        world[T] ^ int(gate_index(world) in noise_states) ^ flip
        for world in WORLDS
    )


def evidence_stats(kind, seed, flip):
    outputs = evidence_outputs(kind, seed, flip)
    groups = defaultdict(list)
    for world, output in zip(WORLDS, outputs):
        groups[output].append(world)

    post_correct = 0
    for worlds in groups.values():
        counts = Counter(warranted_action(world) for world in worlds)
        post_correct += max(counts.values())

    post_accuracy = post_correct / len(WORLDS)
    return {
        "information_bits": entropy(outputs),
        "post_evidence_bayes_accuracy": post_accuracy,
        "correction_relevance": post_accuracy - BASE_ACCURACY,
    }


def encoded_state(panel_name, seed):
    """Create one anonymous presentation of a frozen panel state."""
    specs = PANELS[panel_name]
    rng = random.Random(
        (seed + 1) * 1000003 + sum(map(ord, panel_name)) * 1009
    )
    order = list(range(3))
    rng.shuffle(order)

    rows = []
    for opaque_position, spec_index in enumerate(order):
        canonical_name, kind, kappa = specs[spec_index]
        flip = rng.randrange(2)
        stats = evidence_stats(kind, seed, flip)
        rows.append({
            "opaque_id": f"e{opaque_position}",
            "canonical_name": canonical_name,
            "evidence_family": kind,
            "information_bits": stats["information_bits"],
            "post_evidence_bayes_accuracy": stats["post_evidence_bayes_accuracy"],
            "correction_relevance": stats["correction_relevance"],
            "kappa": kappa,
        })
    return tuple(rows)


def canonical_target(panel_name, rows):
    expected = EXPECTED[panel_name]
    if "COMMIT" in expected:
        return frozenset(("COMMIT",))
    return frozenset(
        row["opaque_id"]
        for row in rows
        if row["canonical_name"] in expected
    )


def positive(row):
    return row["correction_relevance"] > row["kappa"] + EPS


def compensated_compare(left, right):
    """Compare q_left vs q_right without materializing either q value."""
    lhs = left["correction_relevance"] + right["kappa"]
    rhs = right["correction_relevance"] + left["kappa"]
    if lhs > rhs + EPS:
        return 1
    if rhs > lhs + EPS:
        return -1
    return 0


def pareto_dominates(left, right):
    return (
        left["correction_relevance"] >= right["correction_relevance"] - EPS
        and left["kappa"] <= right["kappa"] + EPS
        and (
            left["correction_relevance"] > right["correction_relevance"] + EPS
            or left["kappa"] < right["kappa"] - EPS
        )
    )


def sign_only_action_set(rows):
    positives = frozenset(row["opaque_id"] for row in rows if positive(row))
    return positives if positives else frozenset(("COMMIT",))


def sign_pareto_action_set(rows):
    positives = tuple(row for row in rows if positive(row))
    if not positives:
        return frozenset(("COMMIT",))

    undominated = []
    for candidate in positives:
        if not any(
            pareto_dominates(other, candidate)
            for other in positives
            if other is not candidate
        ):
            undominated.append(candidate["opaque_id"])
    return frozenset(undominated)


def derived_ordinal_action_set(rows):
    """Use the derived pairwise relation, never numeric q values."""
    positives = tuple(row for row in rows if positive(row))
    if not positives:
        return frozenset(("COMMIT",))

    relation = {}
    for i, left in enumerate(positives):
        for j in range(i + 1, len(positives)):
            right = positives[j]
            comparison = compensated_compare(left, right)
            relation[(left["opaque_id"], right["opaque_id"])] = comparison
            relation[(right["opaque_id"], left["opaque_id"])] = -comparison

    maximal = []
    for candidate in positives:
        if not any(
            relation.get((other["opaque_id"], candidate["opaque_id"]), 0) > 0
            for other in positives
            if other is not candidate
        ):
            maximal.append(candidate["opaque_id"])
    return frozenset(maximal)


def max_only_tournament_action_set(rows):
    """Retain only the current co-maximal class; never store a total ranking."""
    champion = rows[0]
    co_champions = [champion]

    for candidate in rows[1:]:
        comparison = compensated_compare(candidate, champion)
        if comparison > 0:
            champion = candidate
            co_champions = [candidate]
        elif comparison == 0:
            co_champions.append(candidate)

    if not positive(champion):
        return frozenset(("COMMIT",))
    return frozenset(row["opaque_id"] for row in co_champions)


def cardinal_action_set(rows):
    q_values = tuple(
        row["correction_relevance"] - row["kappa"]
        for row in rows
    )
    best = max((0.0,) + q_values)
    if best <= EPS:
        return frozenset(("COMMIT",))
    return frozenset(
        row["opaque_id"]
        for row, q in zip(rows, q_values)
        if abs(q - best) < EPS
    )


REPRESENTATIONS = {
    "sign_only": sign_only_action_set,
    "sign_plus_pareto": sign_pareto_action_set,
    "derived_compensated_ordinal": derived_ordinal_action_set,
    "max_only_tournament": max_only_tournament_action_set,
    "cardinal_q_reference": cardinal_action_set,
}


def relevance_lexicographic_action_set(rows):
    positives = tuple(row for row in rows if positive(row))
    if not positives:
        return frozenset(("COMMIT",))
    best = max(row["correction_relevance"] for row in positives)
    return frozenset(
        row["opaque_id"]
        for row in positives
        if abs(row["correction_relevance"] - best) < EPS
    )


def burden_lexicographic_action_set(rows):
    positives = tuple(row for row in rows if positive(row))
    if not positives:
        return frozenset(("COMMIT",))
    best = min(row["kappa"] for row in positives)
    return frozenset(
        row["opaque_id"]
        for row in positives
        if abs(row["kappa"] - best) < EPS
    )


def presentation_from_permutation(panel_name, order):
    """Abstract evaluator presentation for exhaustive anonymous-orbit ceilings."""
    rows = []
    for opaque_position, spec_index in enumerate(order):
        canonical_name, kind, kappa = PANELS[panel_name][spec_index]
        rows.append({
            "opaque_id": opaque_position,
            "canonical_name": canonical_name,
            "correction_relevance": EXPECTED_RELEVANCE[kind],
            "kappa": kappa,
        })
    target = canonical_target(panel_name, rows)
    return tuple(rows), target


def sign_signature(rows):
    return tuple(int(positive(row)) for row in rows)


def pareto_signature(rows):
    relation = tuple(
        int(pareto_dominates(rows[i], rows[j]))
        for i in range(3)
        for j in range(3)
        if i != j
    )
    return sign_signature(rows), relation


def restricted_representation_ceiling(signature_fn):
    """Best deterministic single-action accuracy given only a restricted signature."""
    collisions = defaultdict(list)
    for panel_name in PANEL_NAMES:
        for order in permutations(range(3)):
            rows, target = presentation_from_permutation(panel_name, order)
            collisions[signature_fn(rows)].append(target)

    actions = (0, 1, 2, "COMMIT")
    correct = 0
    total = 0
    collision_summary = []

    for signature, targets in collisions.items():
        scores = {
            action: sum(action in target for target in targets)
            for action in actions
        }
        best = max(scores.values())
        correct += best
        total += len(targets)
        collision_summary.append({
            "signature": repr(signature),
            "presentations": len(targets),
            "best_correct": best,
        })

    return {
        "correct": correct,
        "total": total,
        "accuracy": correct / total,
        "collision_classes": len(collisions),
        "collision_summary": tuple(collision_summary),
    }


def canonical_panel_stats():
    result = {}
    for panel_name in PANEL_NAMES:
        rows = []
        for canonical_name, kind, kappa in PANELS[panel_name]:
            stats = evidence_stats(kind, 0, 0)
            relevance = stats["correction_relevance"]
            rows.append({
                "candidate": canonical_name,
                "information_bits": stats["information_bits"],
                "post_evidence_bayes_accuracy": stats["post_evidence_bayes_accuracy"],
                "correction_relevance": relevance,
                "kappa": kappa,
                "reference_q": relevance - kappa,
            })
        result[panel_name] = {
            "candidates": tuple(rows),
            "expected_optimal_action_set": tuple(sorted(EXPECTED[panel_name])),
        }
    return result


def specification_ledger():
    return {
        "sign_only": {
            "supplied_target_decisions": 0,
            "supplied_rank_entries": 0,
            "persistent_cardinal_q_values": 0,
            "derived_pairwise_comparisons": 0,
            "stores_total_ranking": False,
        },
        "sign_plus_pareto": {
            "supplied_target_decisions": 0,
            "supplied_rank_entries": 0,
            "persistent_cardinal_q_values": 0,
            "derived_pairwise_comparisons": "Pareto only",
            "stores_total_ranking": False,
        },
        "derived_compensated_ordinal": {
            "supplied_target_decisions": 0,
            "supplied_rank_entries": 0,
            "persistent_cardinal_q_values": 0,
            "derived_pairwise_comparisons": "all required candidate pairs on demand",
            "stores_total_ranking": False,
            "materializes_compensated_relation": True,
        },
        "max_only_tournament": {
            "supplied_target_decisions": 0,
            "supplied_rank_entries": 0,
            "persistent_cardinal_q_values": 0,
            "derived_pairwise_comparisons": "2 candidate comparisons per 3-way state",
            "stores_total_ranking": False,
            "persistent_state": "current co-maximal class only",
        },
        "cardinal_q_reference": {
            "supplied_target_decisions": 0,
            "supplied_rank_entries": 0,
            "persistent_cardinal_q_values": 3,
            "derived_pairwise_comparisons": 0,
            "stores_total_ranking": False,
        },
        "order_or_winner_table": {
            "supplied_target_decisions": "direct or equivalent",
            "supplied_rank_entries": "direct",
            "persistent_cardinal_q_values": 0,
            "derived_pairwise_comparisons": 0,
            "oracle_displacement": True,
        },
    }


def run_upstream_regression():
    regression = valuation_role_audit()
    assert regression["encodings"] == 64
    assert regression["valuation_decisions_checked"] == 320
    assert regression["baseline_vs_scale_free_mismatches"] == 0

    stop = regression["stop_regression"]
    assert stop["encodings"] == 64
    assert stop["visited_decision_points"] == 3584
    assert stop["derived_termination_decisions"] == 1536
    assert stop["trace_mismatches"] == 0

    return {
        "valuation_anchor_commit": VALUATION_ANCHOR_COMMIT,
        "valuation_encodings": regression["encodings"],
        "valuation_decisions_checked": regression["valuation_decisions_checked"],
        "baseline_vs_kappa_mismatches": regression[
            "baseline_vs_scale_free_mismatches"
        ],
        "stop_source_commit": STOP_REGRESSION_COMMIT,
        "stop_encodings": stop["encodings"],
        "visited_decision_points": stop["visited_decision_points"],
        "derived_termination_decisions": stop["derived_termination_decisions"],
        "trace_mismatches": stop["trace_mismatches"],
    }


def audit_core():
    match_counts = {name: 0 for name in REPRESENTATIONS}
    mismatch_examples = {name: [] for name in REPRESENTATIONS}
    encoded_states_checked = 0
    identity_mismatches = {
        "derived_compensated_ordinal": 0,
        "max_only_tournament": 0,
        "cardinal_q_reference": 0,
    }

    for seed in range(ENCODINGS):
        for panel_name in PANEL_NAMES:
            rows = encoded_state(panel_name, seed)
            target = canonical_target(panel_name, rows)
            encoded_states_checked += 1

            for name, chooser in REPRESENTATIONS.items():
                predicted = chooser(rows)
                if predicted == target:
                    match_counts[name] += 1
                elif len(mismatch_examples[name]) < 8:
                    mismatch_examples[name].append({
                        "seed": seed,
                        "panel": panel_name,
                        "target": tuple(sorted(map(str, target))),
                        "predicted": tuple(sorted(map(str, predicted))),
                    })

            for name in identity_mismatches:
                if REPRESENTATIONS[name](rows) != target:
                    identity_mismatches[name] += 1

            for row in rows:
                expected_relevance = EXPECTED_RELEVANCE[row["evidence_family"]]
                assert abs(row["information_bits"] - 1.0) < EPS
                assert abs(
                    row["correction_relevance"] - expected_relevance
                ) < EPS

    sign_ceiling = restricted_representation_ceiling(sign_signature)
    pareto_ceiling = restricted_representation_ceiling(pareto_signature)
    assert sign_ceiling["correct"] == 26
    assert sign_ceiling["total"] == 48
    assert abs(sign_ceiling["accuracy"] - 13 / 24) < EPS
    assert pareto_ceiling["correct"] == 34
    assert pareto_ceiling["total"] == 48
    assert abs(pareto_ceiling["accuracy"] - 17 / 24) < EPS

    exhaustive_identity = {
        "derived_compensated_ordinal": 0,
        "max_only_tournament": 0,
        "cardinal_q_reference": 0,
    }
    exhaustive_presentations = 0
    for panel_name in PANEL_NAMES:
        for order in permutations(range(3)):
            rows, target = presentation_from_permutation(panel_name, order)
            exhaustive_presentations += 1
            for name in exhaustive_identity:
                if REPRESENTATIONS[name](rows) != target:
                    exhaustive_identity[name] += 1

    assert exhaustive_presentations == 48
    assert all(value == 0 for value in exhaustive_identity.values())

    canonical_wrong = {}
    for control_name, chooser in (
        ("correction_relevance_lexicographic", relevance_lexicographic_action_set),
        ("burden_lexicographic", burden_lexicographic_action_set),
    ):
        wrong = []
        for panel_name in PANEL_NAMES:
            rows = encoded_state(panel_name, 0)
            if chooser(rows) != canonical_target(panel_name, rows):
                wrong.append(panel_name)
        canonical_wrong[control_name] = tuple(wrong)

    assert "P4" in canonical_wrong["correction_relevance_lexicographic"]
    assert "P5" in canonical_wrong["correction_relevance_lexicographic"]
    assert "P3" in canonical_wrong["burden_lexicographic"]

    assert match_counts["sign_only"] == 128
    assert match_counts["sign_plus_pareto"] == 256
    assert match_counts["derived_compensated_ordinal"] == 512
    assert match_counts["max_only_tournament"] == 512
    assert match_counts["cardinal_q_reference"] == 512

    return {
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "encodings": ENCODINGS,
        "panel_states": PANEL_NAMES,
        "encoded_states_checked": encoded_states_checked,
        "canonical_panel_stats": canonical_panel_stats(),
        "representation_action_set_agreement": {
            name: {
                "exact_matches": match_counts[name],
                "total": encoded_states_checked,
                "accuracy": match_counts[name] / encoded_states_checked,
                "mismatch_examples": tuple(mismatch_examples[name]),
            }
            for name in REPRESENTATIONS
        },
        "restricted_representation_ceilings": {
            "sign_only": sign_ceiling,
            "sign_plus_pareto": pareto_ceiling,
        },
        "candidate_identity_invariance": {
            "anonymous_encoding_mismatches": identity_mismatches,
            "exhaustive_permutation_presentations": exhaustive_presentations,
            "exhaustive_permutation_mismatches": exhaustive_identity,
        },
        "negative_controls": canonical_wrong,
        "tournament_contract": {
            "retains_co_maximal_ties": True,
            "stores_total_ranking": False,
            "candidate_pairwise_comparisons_per_state": 2,
            "commit_comparison_after_tournament": True,
        },
        "specification_ledger": specification_ledger(),
    }


def audit():
    result = audit_core()
    result["upstream_regression"] = run_upstream_regression()
    return result


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
