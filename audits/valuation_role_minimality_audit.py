"""Valuation-Role Minimality Audit.

Preregistered at faba1f247359ef89d514f73a25f84ada1222a1ff.

Cut R removes explicit controller-side R_corr and derives correction comparison
from frozen evidence partitions + frozen correction contract.
Cut K removes/weakens kappa while correction consequences remain available.
"""

from collections import Counter, defaultdict
from itertools import product, permutations
import json
import random

from multi_candidate_acquisition_order_audit import (
    audit as multi_candidate_audit,
    WORLDS, PANEL_NAMES, PANELS, EXPECTED,
    gate_permutation, gate_index,
)

PREREGISTRATION_COMMIT = "faba1f247359ef89d514f73a25f84ada1222a1ff"
MULTI_CANDIDATE_COMMIT = "9a32f94afa40f99a8fa0fcd941b59f2ca1234683"
VALUATION_COMMIT = "c97a5cfde0dba0052f63ab5636f574cd4c4d1f2e"
STOP_COMMIT = "46943821f9dec0ed188410c5c22fcad0f21b5786"
ENCODINGS = 64
EPS = 1e-12
T, G1, G2, G3, N = range(5)


def frozen_target(world):
    return world[T]


def bayes_accuracy(worlds, target_fn):
    counts = Counter(target_fn(world) for world in worlds)
    return max(counts.values()) / len(worlds)


def post_accuracy(worlds, outputs, target_fn):
    groups = defaultdict(list)
    for world, output in zip(worlds, outputs):
        groups[output].append(world)
    correct = 0
    for group in groups.values():
        counts = Counter(target_fn(world) for world in group)
        correct += max(counts.values())
    return correct / len(worlds)


def evidence_outputs(kind, seed, flip):
    gates = gate_permutation(seed)
    if kind == "H":
        noise = set()
    elif kind == "M":
        noise = set(gates[:2])
    elif kind == "L":
        noise = set(gates[:3])
    else:
        raise ValueError(kind)
    return tuple(
        world[T] ^ int(gate_index(world) in noise) ^ flip
        for world in WORLDS
    )


def consequence_compare(left, right, worlds, target_fn):
    left_post = post_accuracy(worlds, left["outputs"], target_fn)
    right_post = post_accuracy(worlds, right["outputs"], target_fn)
    lhs = left_post + right["kappa"]
    rhs = right_post + left["kappa"]
    if lhs > rhs + EPS:
        return 1
    if rhs > lhs + EPS:
        return -1
    return 0


def consequence_maximal(rows, worlds, target_fn):
    """No explicit R_corr or q; retain current co-maximal class only."""
    champion = rows[0]
    co_maximal = [champion]
    for candidate in rows[1:]:
        comparison = consequence_compare(candidate, champion, worlds, target_fn)
        if comparison > 0:
            champion = candidate
            co_maximal = [candidate]
        elif comparison == 0:
            co_maximal.append(candidate)

    base = bayes_accuracy(worlds, target_fn)
    champion_post = post_accuracy(worlds, champion["outputs"], target_fn)
    if champion_post <= base + champion["kappa"] + EPS:
        return frozenset(("COMMIT",))
    return frozenset(row["opaque_id"] for row in co_maximal)


def controller_view(evaluator_rows):
    return tuple({
        "opaque_id": row["opaque_id"],
        "outputs": row["outputs"],
        "kappa": row["kappa"],
    } for row in evaluator_rows)


# ---------------- Cut R: explicit R_corr removal ----------------


def r_rows(panel_name, seed):
    rng = random.Random((seed + 1) * 1000003 + sum(map(ord, panel_name)) * 1009)
    order = list(range(3))
    rng.shuffle(order)
    rows = []
    for opaque_position, spec_index in enumerate(order):
        canonical_name, kind, kappa = PANELS[panel_name][spec_index]
        rows.append({
            "opaque_id": f"e{opaque_position}",
            "canonical_name": canonical_name,
            "outputs": evidence_outputs(kind, seed, rng.randrange(2)),
            "kappa": kappa,
        })
    return tuple(rows)


def r_target(panel_name, evaluator_rows):
    expected = EXPECTED[panel_name]
    if "COMMIT" in expected:
        return frozenset(("COMMIT",))
    return frozenset(
        row["opaque_id"] for row in evaluator_rows
        if row["canonical_name"] in expected
    )


def run_r_main():
    exact = 0
    total = 0
    for seed in range(ENCODINGS):
        for panel_name in PANEL_NAMES:
            evaluator_rows = r_rows(panel_name, seed)
            predicted = consequence_maximal(
                controller_view(evaluator_rows), WORLDS, frozen_target
            )
            target = r_target(panel_name, evaluator_rows)
            total += 1
            exact += int(predicted == target)
    assert total == 512 and exact == 512
    return {"exact_matches": exact, "total": total, "accuracy": exact / total}


MIRROR_WORLDS = tuple(product((0, 1), repeat=3))
MIRROR_NAMES = ("E0", "E1", "EN")
MIRROR_KAPPA = {"E0": 0.10, "E1": 0.10, "EN": 0.01}


def mirror_target(context):
    return lambda world: world[context]


def mirror_outputs(name, flip):
    coordinate = {"E0": 0, "E1": 1, "EN": 2}[name]
    return tuple(world[coordinate] ^ flip for world in MIRROR_WORLDS)


def mirror_rows(seed):
    rng = random.Random((seed + 1) * 998244353 + 17)
    order = list(range(3))
    rng.shuffle(order)
    rows = []
    for opaque_position, index in enumerate(order):
        name = MIRROR_NAMES[index]
        rows.append({
            "opaque_id": f"e{opaque_position}",
            "canonical_name": name,
            "outputs": mirror_outputs(name, rng.randrange(2)),
            "kappa": MIRROR_KAPPA[name],
        })
    return tuple(rows)


def run_contract_aware_mirror():
    exact = 0
    total = 0
    for seed in range(ENCODINGS):
        evaluator_rows = mirror_rows(seed)
        rows = controller_view(evaluator_rows)
        for context in (0, 1):
            desired = "E0" if context == 0 else "E1"
            target = frozenset(
                row["opaque_id"] for row in evaluator_rows
                if row["canonical_name"] == desired
            )
            predicted = consequence_maximal(rows, MIRROR_WORLDS, mirror_target(context))
            total += 1
            exact += int(predicted == target)
    assert total == 128 and exact == 128
    return {"exact_matches": exact, "total": total, "accuracy": exact / total}


def best_choice_ceiling(presentations, signature_fn):
    collisions = defaultdict(list)
    for rows, target in presentations:
        collisions[signature_fn(rows)].append(target)
    actions = (0, 1, 2, "COMMIT")
    correct = 0
    total = 0
    for targets in collisions.values():
        correct += max(sum(action in target for target in targets) for action in actions)
        total += len(targets)
    return {
        "correct": correct,
        "total": total,
        "accuracy": correct / total,
        "collision_classes": len(collisions),
    }


def mirror_contract_blind_ceiling():
    presentations = []
    for context in (0, 1):
        desired = "E0" if context == 0 else "E1"
        for order in permutations(range(3)):
            evaluator_rows = []
            for opaque_position, index in enumerate(order):
                name = MIRROR_NAMES[index]
                evaluator_rows.append({
                    "opaque_id": opaque_position,
                    "canonical_name": name,
                    "outputs": mirror_outputs(name, 0),
                    "kappa": MIRROR_KAPPA[name],
                })
            target = frozenset(
                row["opaque_id"] for row in evaluator_rows
                if row["canonical_name"] == desired
            )
            presentations.append((controller_view(evaluator_rows), target))

    result = best_choice_ceiling(
        presentations,
        lambda rows: tuple((row["outputs"], row["kappa"]) for row in rows),
    )
    assert result["correct"] == 6 and result["total"] == 12
    assert abs(result["accuracy"] - 0.5) < EPS
    return result


# ---------------- Cut K: explicit/quantitative burden removal ----------------

BURDEN_STATES = {
    "K1": {"H": 0.300, "M": 0.100, "L": 0.020},
    "K2": {"H": 0.450, "M": 0.080, "L": 0.010},
    "K3": {"H": 0.480, "M": 0.200, "L": 0.010},
    "K4": {"H": 0.550, "M": 0.300, "L": 0.150},
    "K5": {"H": 0.550, "M": 0.350, "L": 0.270},
}
BURDEN_EXPECTED = {
    "K1": frozenset(("H",)),
    "K2": frozenset(("M",)),
    "K3": frozenset(("L",)),
    "K4": frozenset(("COMMIT",)),
    "K5": frozenset(("COMMIT",)),
}
BURDEN_KINDS = ("H", "M", "L")


def burden_rows(state_name, seed):
    rng = random.Random((seed + 1) * 1000003 + sum(map(ord, state_name)) * 4243)
    order = list(range(3))
    rng.shuffle(order)
    rows = []
    for opaque_position, index in enumerate(order):
        kind = BURDEN_KINDS[index]
        rows.append({
            "opaque_id": f"e{opaque_position}",
            "canonical_name": kind,
            "outputs": evidence_outputs(kind, seed, rng.randrange(2)),
            "kappa": BURDEN_STATES[state_name][kind],
        })
    return tuple(rows)


def burden_target(state_name, evaluator_rows):
    expected = BURDEN_EXPECTED[state_name]
    if "COMMIT" in expected:
        return frozenset(("COMMIT",))
    return frozenset(
        row["opaque_id"] for row in evaluator_rows
        if row["canonical_name"] in expected
    )


def relevance_only(evaluator_rows):
    rows = controller_view(evaluator_rows)
    values = tuple(post_accuracy(WORLDS, row["outputs"], frozen_target) for row in rows)
    best = max(values)
    return frozenset(
        row["opaque_id"] for row, value in zip(rows, values)
        if abs(value - best) < EPS
    )


def run_burden_reference():
    full_exact = 0
    relevance_only_exact = 0
    wrong = defaultdict(int)
    total = 0
    for seed in range(ENCODINGS):
        for state_name in BURDEN_STATES:
            evaluator_rows = burden_rows(state_name, seed)
            target = burden_target(state_name, evaluator_rows)
            predicted = consequence_maximal(
                controller_view(evaluator_rows), WORLDS, frozen_target
            )
            no_burden = relevance_only(evaluator_rows)
            total += 1
            full_exact += int(predicted == target)
            if no_burden == target:
                relevance_only_exact += 1
            else:
                wrong[state_name] += 1

    assert total == 320 and full_exact == 320
    assert relevance_only_exact == 64
    assert dict(wrong) == {"K2": 64, "K3": 64, "K4": 64, "K5": 64}
    return {
        "full_kappa_exact_matches": full_exact,
        "total": total,
        "full_kappa_accuracy": full_exact / total,
        "relevance_only_exact_matches": relevance_only_exact,
        "relevance_only_accuracy": relevance_only_exact / total,
        "relevance_only_wrong_states": dict(wrong),
    }


def abstract_burden_presentation(state_name, order):
    rows = []
    for opaque_position, index in enumerate(order):
        kind = BURDEN_KINDS[index]
        rows.append({
            "opaque_id": opaque_position,
            "canonical_name": kind,
            "outputs": evidence_outputs(kind, 0, 0),
            "kappa": BURDEN_STATES[state_name][kind],
        })
    target = burden_target(state_name, rows)
    return tuple(rows), target


def consequence_signature(rows):
    return tuple(round(post_accuracy(WORLDS, row["outputs"], frozen_target), 12) for row in rows)


def burden_order_signature(rows):
    kappas = tuple(row["kappa"] for row in rows)
    order = tuple(
        (kappas[i] > kappas[j]) - (kappas[i] < kappas[j])
        for i in range(3) for j in range(i + 1, 3)
    )
    return consequence_signature(rows), order


def burden_difference_signature(rows):
    kappas = tuple(row["kappa"] for row in rows)
    differences = tuple(
        round(kappas[i] - kappas[j], 12)
        for i in range(3) for j in range(i + 1, 3)
    )
    return consequence_signature(rows), differences


def burden_ceiling(state_names, signature_fn):
    presentations = []
    for state_name in state_names:
        for order in permutations(range(3)):
            presentations.append(abstract_burden_presentation(state_name, order))
    return best_choice_ceiling(presentations, signature_fn)


def burden_ceilings():
    no_burden = burden_ceiling(("K1", "K2", "K3", "K4"), consequence_signature)
    order_only = burden_ceiling(("K1", "K2", "K3", "K4"), burden_order_signature)
    relative = burden_ceiling(
        ("K1", "K2", "K3", "K4", "K5"), burden_difference_signature
    )
    assert (no_burden["correct"], no_burden["total"]) == (6, 24)
    assert abs(no_burden["accuracy"] - 0.25) < EPS
    assert (order_only["correct"], order_only["total"]) == (6, 24)
    assert abs(order_only["accuracy"] - 0.25) < EPS
    assert (relative["correct"], relative["total"]) == (24, 30)
    assert abs(relative["accuracy"] - 0.8) < EPS
    return {
        "no_burden_K1_K4": no_burden,
        "burden_order_only_K1_K4": order_only,
        "pairwise_burden_differences_K1_K5": relative,
    }


def canonical_burden_targets():
    result = {}
    for state_name in BURDEN_STATES:
        rows, target = abstract_burden_presentation(state_name, (0, 1, 2))
        base = bayes_accuracy(WORLDS, frozen_target)
        result[state_name] = {
            "kappa": dict(BURDEN_STATES[state_name]),
            "target": tuple(sorted(map(str, target))),
            "reference_q": {
                row["canonical_name"]: round(
                    post_accuracy(WORLDS, row["outputs"], frozen_target)
                    - base - row["kappa"], 12
                )
                for row in rows
            },
        }
    return result


def specification_ledger():
    return {
        "current_reference": {
            "explicit_R_corr_controller_fields_per_candidate": 1,
            "explicit_kappa_fields_per_candidate": 1,
            "R_corr_external_designer_fields": 0,
            "kappa_external_numeric_fields_per_candidate": 1,
        },
        "contract_grounded_consequence_comparator": {
            "explicit_R_corr_controller_fields_per_candidate": 0,
            "explicit_kappa_fields_per_candidate": 1,
            "added_external_valuation_fields": 0,
            "B_controller_decreases": True,
            "B_external_decreases": False,
        },
        "no_burden": {
            "explicit_kappa_fields_per_candidate": 0,
            "B_external_decreases": True,
            "sufficient": False,
        },
        "burden_order_only": {
            "quantitative_kappa_fields": 0,
            "absolute_burden_anchor": False,
            "diagnostic_language_only": True,
            "sufficient": False,
        },
        "pairwise_burden_differences_only": {
            "absolute_kappa_fields": 0,
            "absolute_burden_anchor": False,
            "relative_numeric_differences": True,
            "sufficient": False,
        },
        "winner_or_rank_table": {
            "oracle_displacement": True,
            "valid_minimality_evidence": False,
        },
    }


def run_upstream_regression():
    upstream = multi_candidate_audit()
    assert upstream["encodings"] == 64
    assert upstream["encoded_states_checked"] == 512
    agreement = upstream["representation_action_set_agreement"]
    assert agreement["derived_compensated_ordinal"]["exact_matches"] == 512
    assert agreement["max_only_tournament"]["exact_matches"] == 512
    assert agreement["cardinal_q_reference"]["exact_matches"] == 512
    ceilings = upstream["restricted_representation_ceilings"]
    assert abs(ceilings["sign_only"]["accuracy"] - 13 / 24) < EPS
    assert abs(ceilings["sign_plus_pareto"]["accuracy"] - 17 / 24) < EPS
    inherited = upstream["upstream_regression"]
    assert inherited["valuation_decisions_checked"] == 320
    assert inherited["baseline_vs_kappa_mismatches"] == 0
    assert inherited["visited_decision_points"] == 3584
    assert inherited["derived_termination_decisions"] == 1536
    assert inherited["trace_mismatches"] == 0
    return {
        "multi_candidate_commit": MULTI_CANDIDATE_COMMIT,
        "multi_candidate_encoded_states": upstream["encoded_states_checked"],
        "max_only_exact_matches": agreement["max_only_tournament"]["exact_matches"],
        "sign_only_ceiling": ceilings["sign_only"]["accuracy"],
        "pareto_ceiling": ceilings["sign_plus_pareto"]["accuracy"],
        "valuation_commit": VALUATION_COMMIT,
        "valuation_decisions_checked": inherited["valuation_decisions_checked"],
        "valuation_mismatches": inherited["baseline_vs_kappa_mismatches"],
        "stop_commit": STOP_COMMIT,
        "visited_decision_points": inherited["visited_decision_points"],
        "derived_termination_decisions": inherited["derived_termination_decisions"],
        "trace_mismatches": inherited["trace_mismatches"],
    }


def audit_core():
    return {
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "encodings": ENCODINGS,
        "cut_R": {
            "no_explicit_R_corr_main_panel": run_r_main(),
            "contract_aware_mirror": run_contract_aware_mirror(),
            "contract_blind_ceiling": mirror_contract_blind_ceiling(),
        },
        "cut_K": {
            "canonical_burden_targets": canonical_burden_targets(),
            "full_kappa_reference": run_burden_reference(),
            "restricted_representation_ceilings": burden_ceilings(),
        },
        "specification_ledger": specification_ledger(),
    }


def audit():
    result = audit_core()
    result["upstream_regression"] = run_upstream_regression()
    return result


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
