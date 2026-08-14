"""Valuation-Role Discriminant Audit.

Preregistered at dec7d9efe868437ebda136a082ce0e829c8eb9de.

Primary intervention:
    (V, C) -> kappa = C / V

The audit separates raw information, correction relevance, and acquisition worth.
The valuation-panel geometry is fixed across controller interventions. The previous
STOP-substitution audit is rerun as a regression certificate so this audit cannot
silently alter the already-earned sequential-refinement or termination roles.
"""

from collections import Counter, defaultdict
from itertools import product
from math import log2
import json
import random

from stop_substitution_audit import audit as stop_audit


PREREGISTRATION_COMMIT = "dec7d9efe868437ebda136a082ce0e829c8eb9de"
STOP_REGRESSION_COMMIT = "46943821f9dec0ed188410c5c22fcad0f21b5786"
ENCODINGS = 64
V = 10.0
EPS = 1e-12

S, X, Y, N1, N2, N3, N4 = range(7)
WORLDS = tuple(product((0, 1), repeat=7))

CASE_SPECS = {
    "A": {"coords": (X, N1, N2), "cost": 1.0, "expected_action": 1},
    "B": {"coords": (N1, N2, N3), "cost": 1.0, "expected_action": 0},
    "C": {"coords": (X,), "cost": 1.0, "expected_action": 1},
    "D": {"coords": (X, N1, N2), "cost": 3.0, "expected_action": 0},
    "B+": {"coords": (N1, N2, N3, N4), "cost": 1.0, "expected_action": 0},
}
CASE_NAMES = tuple(CASE_SPECS)


def warranted_action(world):
    return world[X] if world[S] == 0 else world[Y]


def entropy(values):
    counts = Counter(values)
    total = len(values)
    return -sum((count / total) * log2(count / total) for count in counts.values())


def bayes_accuracy(worlds):
    counts = Counter(warranted_action(world) for world in worlds)
    return max(counts.values()) / len(worlds)


BASE_ACCURACY = bayes_accuracy(WORLDS)
assert abs(BASE_ACCURACY - 0.5) < EPS


def encoded_outputs(case_name, seed):
    """Anonymous output encoding preserving the evidence partition."""
    spec = CASE_SPECS[case_name]
    coords = spec["coords"]
    rng = random.Random((seed + 1) * 1000003 + sum(map(ord, case_name)))

    order = list(range(len(coords)))
    rng.shuffle(order)
    order = tuple(order)
    flips = tuple(rng.randrange(2) for _ in coords)

    outputs = []
    for world in WORLDS:
        raw = tuple(world[coord] for coord in coords)
        permuted = tuple(raw[i] for i in order)
        outputs.append(tuple(v ^ f for v, f in zip(permuted, flips)))
    return tuple(outputs)


def evidence_stats(case_name, seed):
    spec = CASE_SPECS[case_name]
    outputs = encoded_outputs(case_name, seed)
    info = entropy(outputs)

    groups = defaultdict(list)
    for world, output in zip(WORLDS, outputs):
        groups[output].append(world)

    post_correct = 0
    for worlds in groups.values():
        counts = Counter(warranted_action(world) for world in worlds)
        post_correct += max(counts.values())

    post_accuracy = post_correct / len(WORLDS)
    relevance = post_accuracy - BASE_ACCURACY
    cost = spec["cost"]
    margin = V * relevance - cost
    kappa = cost / V

    return {
        "information_bits": info,
        "post_evidence_bayes_accuracy": post_accuracy,
        "correction_relevance": relevance,
        "cost": cost,
        "vc_margin": margin,
        "kappa": kappa,
        "baseline_action": int(margin > EPS),
        "scale_free_action": int(relevance > kappa + EPS),
        "expected_action": spec["expected_action"],
    }


def classification_ceiling(rows, signature_fn):
    """Best deterministic acquisition classification from a restricted signature."""
    groups = defaultdict(list)
    for case_name, row in rows.items():
        groups[signature_fn(row)].append(CASE_SPECS[case_name]["expected_action"])
    correct = sum(max(Counter(targets).values()) for targets in groups.values())
    return correct / len(CASE_NAMES)


def feature_ceilings(rows):
    rounded = lambda x: round(x, 12)
    return {
        "I": classification_ceiling(rows, lambda r: (rounded(r["information_bits"]),)),
        "R_corr": classification_ceiling(rows, lambda r: (rounded(r["correction_relevance"]),)),
        "I_C": classification_ceiling(
            rows, lambda r: (rounded(r["information_bits"]), rounded(r["cost"]))
        ),
        "I_R_corr": classification_ceiling(
            rows,
            lambda r: (rounded(r["information_bits"]), rounded(r["correction_relevance"])),
        ),
        "I_over_C": classification_ceiling(
            rows, lambda r: rounded(r["information_bits"] / r["cost"])
        ),
        "R_corr_C": classification_ceiling(
            rows,
            lambda r: (rounded(r["correction_relevance"]), rounded(r["cost"])),
        ),
    }


def specification_ledger():
    """Finite supplied-field accounting; not an MDL/Kolmogorov claim."""
    return {
        "baseline_V_C": {
            "global_numeric_fields": 1,
            "per_case_numeric_fields": len(CASE_NAMES),
            "direct_target_decision_fields": 0,
            "numeric_slots": 1 + len(CASE_NAMES),
            "stores_target_decisions": False,
            "interpretation": (
                "one global correctness-value scalar plus one absolute cost field "
                "per valuation case"
            ),
        },
        "scale_free_kappa": {
            "global_numeric_fields": 0,
            "per_case_numeric_fields": len(CASE_NAMES),
            "direct_target_decision_fields": 0,
            "numeric_slots": len(CASE_NAMES),
            "stores_target_decisions": False,
            "interpretation": (
                "one normalized acquisition threshold per valuation case; removes "
                "absolute value scale, not acquisition-worth ordering"
            ),
        },
        "order_table": {
            "global_numeric_fields": 0,
            "per_case_numeric_fields": 0,
            "direct_target_decision_fields": len(CASE_NAMES),
            "numeric_slots": 0,
            "stores_target_decisions": True,
            "oracle_displacement": True,
            "interpretation": (
                "directly stores acquisition decisions; behavioral equivalence does "
                "not count as substrate reduction"
            ),
        },
    }


def run_stop_regression():
    regression = stop_audit()
    assert regression["encodings"] == 64
    assert regression["visited_decision_points"] == 3584
    assert regression["derived_termination_decisions"] == 1536
    assert regression["trace_mismatches"] == 0
    return {
        "source_commit": STOP_REGRESSION_COMMIT,
        "encodings": regression["encodings"],
        "visited_decision_points": regression["visited_decision_points"],
        "primitive_stop_decisions": regression["primitive_stop_decisions"],
        "derived_termination_decisions": regression["derived_termination_decisions"],
        "trace_mismatches": regression["trace_mismatches"],
    }


def audit():
    expected_signature = tuple(CASE_SPECS[name]["expected_action"] for name in CASE_NAMES)
    baseline_mismatches = 0
    scale_free_mismatches = 0
    baseline_vs_scale_free_mismatches = 0
    valuation_decisions_checked = 0
    canonical_rows = None

    for seed in range(ENCODINGS):
        rows = {name: evidence_stats(name, seed) for name in CASE_NAMES}
        if canonical_rows is None:
            canonical_rows = rows

        baseline_signature = tuple(rows[name]["baseline_action"] for name in CASE_NAMES)
        scale_free_signature = tuple(rows[name]["scale_free_action"] for name in CASE_NAMES)

        baseline_mismatches += sum(a != b for a, b in zip(baseline_signature, expected_signature))
        scale_free_mismatches += sum(a != b for a, b in zip(scale_free_signature, expected_signature))
        baseline_vs_scale_free_mismatches += sum(
            a != b for a, b in zip(baseline_signature, scale_free_signature)
        )
        valuation_decisions_checked += len(CASE_NAMES)

    assert baseline_mismatches == 0
    assert scale_free_mismatches == 0
    assert baseline_vs_scale_free_mismatches == 0

    expected_stats = {
        "A": (3.0, 0.25, 1.0, 1.5, 0.1),
        "B": (3.0, 0.0, 1.0, -1.0, 0.1),
        "C": (1.0, 0.25, 1.0, 1.5, 0.1),
        "D": (3.0, 0.25, 3.0, -0.5, 0.3),
        "B+": (4.0, 0.0, 1.0, -1.0, 0.1),
    }
    for name, expected in expected_stats.items():
        row = canonical_rows[name]
        actual = (
            row["information_bits"],
            row["correction_relevance"],
            row["cost"],
            row["vc_margin"],
            row["kappa"],
        )
        assert all(abs(a - b) < EPS for a, b in zip(actual, expected))

    information_only_signature = tuple(
        int(canonical_rows[name]["information_bits"] > EPS) for name in CASE_NAMES
    )
    relevance_only_signature = tuple(
        int(canonical_rows[name]["correction_relevance"] > EPS) for name in CASE_NAMES
    )
    assert information_only_signature == (1, 1, 1, 1, 1)
    assert relevance_only_signature == (1, 0, 1, 1, 0)

    ceilings = feature_ceilings(canonical_rows)
    assert ceilings == {
        "I": 0.8,
        "R_corr": 0.8,
        "I_C": 0.8,
        "I_R_corr": 0.8,
        "I_over_C": 0.6,
        "R_corr_C": 1.0,
    }

    regression = run_stop_regression()

    return {
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "encodings": ENCODINGS,
        "valuation_cases": CASE_NAMES,
        "expected_signature": expected_signature,
        "baseline_signature": expected_signature,
        "scale_free_signature": expected_signature,
        "baseline_mismatches": baseline_mismatches,
        "scale_free_mismatches": scale_free_mismatches,
        "baseline_vs_scale_free_mismatches": baseline_vs_scale_free_mismatches,
        "valuation_decisions_checked": valuation_decisions_checked,
        "canonical_case_stats": canonical_rows,
        "negative_controls": {
            "information_only_signature": information_only_signature,
            "information_only_wrong_cases": ("B", "D", "B+"),
            "correction_relevance_only_signature": relevance_only_signature,
            "correction_relevance_only_wrong_cases": ("D",),
        },
        "feature_classification_ceilings": ceilings,
        "specification_ledger": specification_ledger(),
        "stop_regression": regression,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
