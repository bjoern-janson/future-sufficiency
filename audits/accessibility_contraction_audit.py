"""Accessibility Contraction Audit.

Preregistered at 6116603e0814f6fd7742cdb21ef312bd0cb15070.

Primary intervention:
    A_explicit -> A_reduced

The latent experiment universe E* and all downstream valuation/navigation roles are
frozen. This audit tests accessibility contraction only; it does not generate,
compose, or alter probes.
"""

from collections import Counter, defaultdict
from itertools import product
import hashlib
import json
import random

from valuation_role_minimality_audit import audit as valuation_minimality_audit

PREREGISTRATION_COMMIT = "6116603e0814f6fd7742cdb21ef312bd0cb15070"
VALUATION_MINIMALITY_COMMIT = "b7c068b79f630e12dbeeb70a610973898305cdfb"
ENCODINGS = 64
MASKS = tuple(range(1, 16))
WORLDS = tuple(product((0, 1), repeat=4))
KAPPA = 0.1
EPS = 1e-12


def parity(mask, world):
    """Four-bit parity under a fixed canonical bit ordering."""
    return sum(((mask >> (3 - i)) & 1) * world[i] for i in range(4)) % 2


def truth_table(mask):
    return tuple(parity(mask, world) for world in WORLDS)


LATENT_SEMANTICS = {mask: truth_table(mask) for mask in MASKS}
LATENT_SEMANTICS_CHECKSUM = hashlib.sha256(
    json.dumps(
        {str(mask): list(table) for mask, table in LATENT_SEMANTICS.items()},
        sort_keys=True,
    ).encode("utf-8")
).hexdigest()


def make_encoding(seed):
    """Anonymous probe handles, registry order, output polarities, and contexts."""
    rng = random.Random((seed + 1) * 1000003 + 6116603)

    mask_order = list(MASKS)
    rng.shuffle(mask_order)
    handle_to_mask = {f"e{i}": mask for i, mask in enumerate(mask_order)}
    mask_to_handle = {mask: handle for handle, mask in handle_to_mask.items()}

    registry_order = list(handle_to_mask)
    rng.shuffle(registry_order)

    flips = {handle: rng.randrange(2) for handle in handle_to_mask}

    contexts = list(MASKS)
    rng.shuffle(contexts)
    context_id_to_mask = {f"c{i}": mask for i, mask in enumerate(contexts)}

    return {
        "handle_to_mask": handle_to_mask,
        "mask_to_handle": mask_to_handle,
        "registry_order": tuple(registry_order),
        "flips": flips,
        "context_id_to_mask": context_id_to_mask,
    }


def probe_outputs(encoding, handle):
    mask = encoding["handle_to_mask"][handle]
    flip = encoding["flips"][handle]
    return tuple(parity(mask, world) ^ flip for world in WORLDS)


def target_fn(mask):
    return lambda world: parity(mask, world)


def bayes_accuracy(worlds, target):
    counts = Counter(target(world) for world in worlds)
    return max(counts.values()) / len(worlds)


def post_accuracy(worlds, outputs, target):
    groups = defaultdict(list)
    for world, output in zip(worlds, outputs):
        groups[output].append(world)

    correct = 0
    for group in groups.values():
        counts = Counter(target(world) for world in group)
        correct += max(counts.values())
    return correct / len(worlds)


def frozen_choice(encoding, context_mask, accessible_handles):
    """Frozen valuation role: corrective consequence + anchored burden -> maximal."""
    if not accessible_handles:
        return frozenset(("COMMIT",))

    target = target_fn(context_mask)
    base = bayes_accuracy(WORLDS, target)
    margins = []

    for handle in accessible_handles:
        post = post_accuracy(WORLDS, probe_outputs(encoding, handle), target)
        margins.append((handle, post - base - KAPPA))

    best = max((0.0,) + tuple(margin for _, margin in margins))
    if best <= EPS:
        return frozenset(("COMMIT",))

    return frozenset(
        handle for handle, margin in margins
        if abs(margin - best) < EPS
    )


# ---------------- Access interfaces ----------------

def access_A0_explicit(encoding, context_mask):
    del context_mask
    return tuple(encoding["handle_to_mask"].keys())


def access_A1_all_registry(encoding, context_mask):
    del context_mask
    return encoding["registry_order"]


def access_A2_none(encoding, context_mask):
    del encoding, context_mask
    return tuple()


def access_A3_first_seven(encoding, context_mask):
    del context_mask
    return encoding["registry_order"][:7]


def access_A4_target_lookup(encoding, context_mask):
    return (encoding["mask_to_handle"][context_mask],)


ACCESS = {
    "A0_explicit_menu": access_A0_explicit,
    "A1_all_registry": access_A1_all_registry,
    "A2_no_access": access_A2_none,
    "A3_first_7_registry": access_A3_first_seven,
    "A4_target_lookup_oracle": access_A4_target_lookup,
}


def access_ledger():
    return {
        "A0_explicit_menu": {
            "vector": {"B_menu": 15, "B_generator": 0, "B_grammar": 0, "B_semantic_hints": 0, "B_search_constraints": 0},
            "B_access_clauses": 15,
            "oracle_displacement": False,
        },
        "A1_all_registry": {
            "vector": {"B_menu": 0, "B_generator": 1, "B_grammar": 0, "B_semantic_hints": 0, "B_search_constraints": 0},
            "B_access_clauses": 1,
            "oracle_displacement": False,
        },
        "A2_no_access": {
            "vector": {"B_menu": 0, "B_generator": 0, "B_grammar": 0, "B_semantic_hints": 0, "B_search_constraints": 0},
            "B_access_clauses": 0,
            "oracle_displacement": False,
        },
        "A3_first_7_registry": {
            "vector": {"B_menu": 0, "B_generator": 1, "B_grammar": 0, "B_semantic_hints": 0, "B_search_constraints": 1},
            "B_access_clauses": 2,
            "oracle_displacement": False,
        },
        "A4_target_lookup_oracle": {
            "vector": {"B_menu": 0, "B_generator": 1, "B_grammar": 0, "B_semantic_hints": 15, "B_search_constraints": 0},
            "B_access_clauses": 16,
            "oracle_displacement": True,
        },
    }


def validate_latent_universe():
    assert len(MASKS) == 15
    assert len(set(LATENT_SEMANTICS.values())) == 15

    relevance_pairs = set()
    for context_mask in MASKS:
        target = target_fn(context_mask)
        base = bayes_accuracy(WORLDS, target)
        assert abs(base - 0.5) < EPS
        for probe_mask in MASKS:
            post = post_accuracy(WORLDS, LATENT_SEMANTICS[probe_mask], target)
            relevance = post - base
            relevance_pairs.add((probe_mask == context_mask, relevance))

    assert relevance_pairs == {(False, 0.0), (True, 0.5)}

    return {
        "latent_universe_size": len(MASKS),
        "world_count": len(WORLDS),
        "semantics_checksum_sha256": LATENT_SEMANTICS_CHECKSUM,
        "distinct_probe_semantics": len(set(LATENT_SEMANTICS.values())),
        "target_probe_relevance": 0.5,
        "non_target_probe_relevance": 0.0,
        "raw_information_bits_per_probe": 1.0,
        "anchored_kappa_per_probe": KAPPA,
    }


def audit_core():
    latent = validate_latent_universe()
    ledgers = access_ledger()

    totals = {name: {"target_reachable": 0, "choice_matches_A0": 0} for name in ACCESS}
    per_context_reach = {name: {str(mask): 0 for mask in MASKS} for name in ACCESS}
    per_encoding_A3 = []
    total_evaluations = 0

    for seed in range(ENCODINGS):
        encoding = make_encoding(seed)
        a3_reachable_this_encoding = 0
        assert set(encoding["handle_to_mask"].values()) == set(MASKS)
        assert len(encoding["registry_order"]) == 15

        for context_mask in encoding["context_id_to_mask"].values():
            total_evaluations += 1
            target_handle = encoding["mask_to_handle"][context_mask]
            reference = frozen_choice(encoding, context_mask, access_A0_explicit(encoding, context_mask))
            assert reference == frozenset((target_handle,))

            for name, access_fn in ACCESS.items():
                accessible = access_fn(encoding, context_mask)
                reachable = target_handle in accessible
                predicted = frozen_choice(encoding, context_mask, accessible)
                totals[name]["target_reachable"] += int(reachable)
                totals[name]["choice_matches_A0"] += int(predicted == reference)
                per_context_reach[name][str(context_mask)] += int(reachable)
                if name == "A3_first_7_registry":
                    a3_reachable_this_encoding += int(reachable)

        per_encoding_A3.append(a3_reachable_this_encoding)

    assert total_evaluations == 960
    assert totals["A0_explicit_menu"] == {"target_reachable": 960, "choice_matches_A0": 960}
    assert totals["A1_all_registry"] == {"target_reachable": 960, "choice_matches_A0": 960}
    assert totals["A2_no_access"] == {"target_reachable": 0, "choice_matches_A0": 0}
    assert totals["A3_first_7_registry"] == {"target_reachable": 448, "choice_matches_A0": 448}
    assert totals["A4_target_lookup_oracle"] == {"target_reachable": 960, "choice_matches_A0": 960}
    assert all(value == 7 for value in per_encoding_A3)
    assert ledgers["A0_explicit_menu"]["B_access_clauses"] == 15
    assert ledgers["A1_all_registry"]["B_access_clauses"] == 1
    assert ledgers["A4_target_lookup_oracle"]["oracle_displacement"] is True

    return {
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "encodings": ENCODINGS,
        "contexts_per_encoding": 15,
        "context_encoding_evaluations": total_evaluations,
        "latent_universe": latent,
        "latent_universe_identical_across_interfaces": True,
        "B_E_star_frozen": True,
        "access_results": {
            name: {
                **result,
                "target_reach_rate": result["target_reachable"] / total_evaluations,
                "choice_agreement": result["choice_matches_A0"] / total_evaluations,
            }
            for name, result in totals.items()
        },
        "A3_coverage_certificate": {
            "reachable_per_encoding": tuple(per_encoding_A3),
            "all_encodings_exactly_7_of_15": all(v == 7 for v in per_encoding_A3),
            "aggregate_reachable": totals["A3_first_7_registry"]["target_reachable"],
            "aggregate_total": total_evaluations,
            "coverage": totals["A3_first_7_registry"]["target_reachable"] / total_evaluations,
            "preregistered_ceiling": 7 / 15,
            "exceeds_ceiling": False,
        },
        "per_context_target_reachability_counts": per_context_reach,
        "access_burden_ledger": ledgers,
        "primary_contraction": {
            "A0_B_access": 15,
            "A1_B_access": 1,
            "B_access_decreases": True,
            "same_target_reachability": True,
            "same_downstream_choice": True,
            "B_E_star_changed": False,
        },
        "oracle_control": {
            "interface": "A4_target_lookup_oracle",
            "behavioral_choice_matches": 960,
            "semantic_hint_clauses": 15,
            "B_access_clauses": 16,
            "classification": "oracle displacement",
            "valid_minimality_evidence": False,
        },
    }


def run_upstream_regression():
    upstream = valuation_minimality_audit()
    cut_r = upstream["cut_R"]
    assert cut_r["no_explicit_R_corr_main_panel"]["exact_matches"] == 512
    assert cut_r["contract_aware_mirror"]["exact_matches"] == 128
    assert abs(cut_r["contract_blind_ceiling"]["accuracy"] - 0.5) < EPS

    cut_k = upstream["cut_K"]
    reference = cut_k["full_kappa_reference"]
    assert reference["full_kappa_exact_matches"] == 320
    ceilings = cut_k["restricted_representation_ceilings"]
    assert abs(ceilings["no_burden_K1_K4"]["accuracy"] - 0.25) < EPS
    assert abs(ceilings["burden_order_only_K1_K4"]["accuracy"] - 0.25) < EPS
    assert abs(ceilings["pairwise_burden_differences_K1_K5"]["accuracy"] - 0.8) < EPS

    inherited = upstream["upstream_regression"]
    assert inherited["multi_candidate_encoded_states"] == 512
    assert inherited["max_only_exact_matches"] == 512
    assert abs(inherited["sign_only_ceiling"] - 13 / 24) < EPS
    assert abs(inherited["pareto_ceiling"] - 17 / 24) < EPS
    assert inherited["valuation_decisions_checked"] == 320
    assert inherited["valuation_mismatches"] == 0
    assert inherited["visited_decision_points"] == 3584
    assert inherited["derived_termination_decisions"] == 1536
    assert inherited["trace_mismatches"] == 0

    return {
        "valuation_minimality_commit": VALUATION_MINIMALITY_COMMIT,
        "cut_R_no_explicit_R_corr_exact": 512,
        "cut_R_contract_aware_mirror_exact": 128,
        "cut_R_contract_blind_ceiling": 0.5,
        "cut_K_anchored_burden_exact": 320,
        "cut_K_no_burden_ceiling": 0.25,
        "cut_K_burden_order_ceiling": 0.25,
        "cut_K_relative_difference_ceiling": 0.8,
        "multi_candidate_encoded_states": inherited["multi_candidate_encoded_states"],
        "max_only_exact_matches": inherited["max_only_exact_matches"],
        "sign_only_ceiling": inherited["sign_only_ceiling"],
        "pareto_ceiling": inherited["pareto_ceiling"],
        "valuation_decisions_checked": inherited["valuation_decisions_checked"],
        "valuation_mismatches": inherited["valuation_mismatches"],
        "visited_decision_points": inherited["visited_decision_points"],
        "derived_termination_decisions": inherited["derived_termination_decisions"],
        "trace_mismatches": inherited["trace_mismatches"],
    }


def audit():
    result = audit_core()
    result["upstream_regression"] = run_upstream_regression()
    return result


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))