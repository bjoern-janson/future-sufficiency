"""Experiment-Space Construction Discriminant.

Preregistered at fd99c09e6d65dd0e73a6909bd38fc1d8d55c6bb3.

Gate 2 tests causal experiment-space expansion under a supplied, target-blind
construction-substrate extension. It does not test autonomous discovery or
authorization of that extension.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
import hashlib
import json
import random

try:
    from latent_registry_minimality_audit import audit as gate1_audit
except ImportError:
    gate1_audit = None

PREREGISTRATION_COMMIT = "fd99c09e6d65dd0e73a6909bd38fc1d8d55c6bb3"
GATE1_COMMIT = "c661e58a97b3dbcc580bd096835aa9d2e09f0490"
ENCODINGS = 64
KAPPA = 0.1
EPS = 1e-12
FULL = (1 << 16) - 1
WORLDS = tuple(product((0, 1), repeat=4))

def bit_table(fn, order=tuple(range(16))):
    value = 0
    for out_pos, world_index in enumerate(order):
        if fn(WORLDS[world_index]):
            value |= 1 << out_pos
    return value

def coordinate(index, order=tuple(range(16))):
    return bit_table(lambda w: w[index], order)

def canon_partition(value):
    # Match Gate-1 tuple-lexicographic partition canonicalization. The first
    # world entry decides between a binary table and its complement.
    return value if (value & 1) == 0 else (value ^ FULL)

def nonconstant_partition(value):
    c = canon_partition(value)
    return c not in (0,)

def checksum(partitions):
    tuples = [tuple((x >> i) & 1 for i in range(16)) for x in partitions]
    return hashlib.sha256(
        json.dumps([list(x) for x in sorted(tuples)], separators=(",", ":")).encode()
    ).hexdigest()

def xor_span(vectors):
    """Return the complete GF(2) vector span as raw 16-bit functions."""
    basis = []
    for v in vectors:
        x = v
        for b in basis:
            x = min(x, x ^ b)
        if x:
            basis.append(x)
            basis.sort(reverse=True)
            reduced = []
            for y in basis:
                z = y
                for b in reduced:
                    z = min(z, z ^ b)
                if z:
                    reduced.append(z)
            basis = reduced
    span = {0}
    for b in basis:
        span |= {x ^ b for x in tuple(span)}
    return frozenset(span)

def old_raw_closure(order):
    primitives = tuple(coordinate(i, order) for i in range(4))
    span = xor_span(primitives)
    assert len(span) == 16
    return frozenset(x for x in span if x != 0)

def partitions(raw_functions):
    return frozenset(canon_partition(x) for x in raw_functions if nonconstant_partition(x))

def build_G20(order):
    return partitions(old_raw_closure(order))

def build_G21(order):
    old = old_raw_closure(order)
    nonlinear = {a & b for a in old for b in old}
    span = xor_span(tuple(old | nonlinear))
    return partitions(x for x in span if x != 0)

def build_G22(order):
    old = old_raw_closure(order)
    with_not = set(old) | {x ^ FULL for x in old}
    return partitions(with_not)

def build_G23(order):
    old = old_raw_closure(order)
    direct = set(old)
    direct |= {a & b for a in old for b in old}
    return partitions(direct)

def novel_targets(order):
    fns = (
        lambda w: w[0] & w[1],
        lambda w: (w[0] ^ w[1]) & w[2],
        lambda w: (w[0] ^ w[1]) & (w[2] ^ w[3]),
        lambda w: (w[0] & w[1]) ^ (w[2] & w[3]),
    )
    return tuple(canon_partition(bit_table(fn, order)) for fn in fns)

def target_raw(index, order):
    fns = (
        lambda w: w[0] & w[1],
        lambda w: (w[0] ^ w[1]) & w[2],
        lambda w: (w[0] ^ w[1]) & (w[2] ^ w[3]),
        lambda w: (w[0] & w[1]) ^ (w[2] & w[3]),
    )
    return bit_table(fns[index], order)

def build_G24(order):
    return frozenset(set(build_G20(order)) | set(novel_targets(order)))

def post_accuracy(experiment, target):
    groups = {0: [0, 0], 1: [0, 0]}
    for i in range(16):
        e = (experiment >> i) & 1
        t = (target >> i) & 1
        groups[e][t] += 1
    return sum(max(counts) for counts in groups.values()) / 16

def bayes_accuracy(target):
    ones = target.bit_count()
    return max(ones, 16 - ones) / 16

def make_encoding(seed):
    rng = random.Random((seed + 1) * 1000003 + 299)
    world_order = list(range(16))
    rng.shuffle(world_order)
    primitive_handles = [f"p{i}" for i in range(4)]
    rng.shuffle(primitive_handles)
    contexts = list(range(4))
    rng.shuffle(contexts)
    return {
        "seed": seed,
        "world_order": tuple(world_order),
        "primitive_handles": tuple(primitive_handles),
        "context_order": tuple(contexts),
    }

def present_family(family, seed, condition):
    """Opaque emitted handles with independent public output-token polarity flips.

    Construction happens on internal semantic values. Polarity randomization is
    applied only at the emitted experiment interface, so AND/XOR semantics are
    not changed by arbitrary public token names.
    """
    rng = random.Random((seed + 1) * 2654435761 + sum(map(ord, condition)) * 131)
    members = list(family)
    rng.shuffle(members)
    rows = []
    for i, partition in enumerate(members):
        emitted = partition ^ (FULL if rng.randrange(2) else 0)
        rows.append({"handle": f"e{i}", "partition": partition, "outputs": emitted})
    return tuple(rows)

def frozen_choice(rows, target):
    base = bayes_accuracy(target)
    scored = []
    for row in rows:
        r = post_accuracy(row["outputs"], target) - base
        scored.append((row["handle"], row["partition"], r - KAPPA, r))
    best = max((0.0,) + tuple(x[2] for x in scored))
    if best <= EPS:
        return frozenset(("COMMIT",)), tuple(scored)
    winners = frozenset(handle for handle, _, margin, _ in scored if abs(margin - best) < EPS)
    return winners, tuple(scored)

def target_handle(rows, target_partition):
    matches = [row["handle"] for row in rows if row["partition"] == target_partition]
    assert len(matches) <= 1
    return matches[0] if matches else None

LEDGER = {
    "G20_old_S0": {
        "visible": [4, 1, 1, 0, 2, 0], "visible_total": 8,
        "expanded": [4, 1, 1, 0, 2, 0], "expanded_total": 8,
        "target_specific_semantics": 0, "valid_gate2_evidence": False,
    },
    "G21_AND_plus_post_extension_closure": {
        "visible": [4, 2, 2, 0, 2, 0], "visible_total": 10,
        "expanded": [4, 2, 2, 0, 2, 0], "expanded_total": 10,
        "target_specific_semantics": 0, "valid_gate2_evidence": True,
    },
    "G22_NOT_no_new_geometry": {
        "visible": [4, 2, 2, 0, 2, 0], "visible_total": 10,
        "expanded": [4, 2, 2, 0, 2, 0], "expanded_total": 10,
        "target_specific_semantics": 0, "valid_gate2_evidence": False,
    },
    "G23_AND_one_layer_only": {
        "visible": [4, 2, 2, 0, 2, 0], "visible_total": 10,
        "expanded": [4, 2, 2, 0, 2, 0], "expanded_total": 10,
        "target_specific_semantics": 0, "valid_gate2_evidence": False,
    },
    "G24_direct_target_registry": {
        "visible": [4, 1, 1, 4, 2, 0], "visible_total": 12,
        "expanded": [4, 1, 1, 4, 2, 0], "expanded_total": 12,
        "target_specific_semantics": 4,
        "classification": "target-specific specification displacement",
        "valid_gate2_evidence": False,
    },
    "G25_transparent_macro_alias": {
        "visible": [0, 0, 1, 0, 0, 0], "visible_total": 1,
        "expanded": [4, 2, 2, 0, 2, 0], "expanded_total": 10,
        "target_specific_semantics": 0,
        "classification": "alias for S1; no independent minimality evidence",
        "valid_gate2_evidence": False,
    },
    "G25_opaque_direct_family_macro": {
        "visible": [0, 0, 1, 0, 0, 0], "visible_total": 1,
        "expanded_semantic_bindings": 1023,
        "expanded_total": 1023,
        "classification": "hidden specification",
        "valid_gate2_evidence": False,
    },
}

def audit_core():
    canonical_order = tuple(range(16))
    canonical_c0 = build_G20(canonical_order)
    canonical_c1 = build_G21(canonical_order)
    canonical_g23 = build_G23(canonical_order)
    canonical_targets = novel_targets(canonical_order)

    assert len(canonical_c0) == 15
    assert checksum(canonical_c0) == "809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49"
    assert len(canonical_c1) == 1023
    assert len(canonical_g23) == 120
    assert canonical_c0 < canonical_c1
    assert all(t not in canonical_c0 for t in canonical_targets)
    assert all(t in canonical_c1 for t in canonical_targets)
    assert [t in canonical_g23 for t in canonical_targets] == [True, True, True, False]

    n4_raw_canonical = target_raw(3, canonical_order)
    n4_base = bayes_accuracy(n4_raw_canonical)
    g23_n4_gains = [post_accuracy(p, n4_raw_canonical) - n4_base for p in canonical_g23]
    g23_n4_max_gain = max(g23_n4_gains)
    g23_n4_max_count = sum(abs(g - g23_n4_max_gain) < EPS for g in g23_n4_gains)
    assert abs(g23_n4_max_gain - 0.125) < EPS
    assert g23_n4_max_count == 18

    condition_builders = {
        "G20_old_S0": build_G20,
        "G21_AND_plus_post_extension_closure": build_G21,
        "G22_NOT_no_new_geometry": build_G22,
        "G23_AND_one_layer_only": build_G23,
        "G24_direct_target_registry": build_G24,
        "G25_transparent_macro_alias": build_G21,
    }
    totals = {
        name: {
            "target_reachable": 0, "exact_target_chosen": 0, "commit": 0,
            "family_sizes": set(), "space_changed": 0,
        }
        for name in condition_builders
    }
    novelty = {f"n{i}": {"outside_old_closure_encodings": 0} for i in range(1, 5)}
    decision_diag = {}
    per_encoding_g23_coverage = []
    exact_extensional = {"G20": 0, "G21": 0, "G22": 0, "G23": 0}
    total = 0

    for seed in range(ENCODINGS):
        enc = make_encoding(seed)
        order = enc["world_order"]
        c0 = build_G20(order)
        c1 = build_G21(order)
        g22 = build_G22(order)
        g23 = build_G23(order)
        targets = novel_targets(order)

        assert len(c0) == 15
        assert len(c1) == 1023
        assert len(g22) == 15
        assert len(g23) == 120
        assert c0 < c1
        exact_extensional["G20"] += int(len(c0) == 15)
        exact_extensional["G21"] += int(len(c1) == 1023 and c0 < c1)
        exact_extensional["G22"] += int(g22 == c0)
        exact_extensional["G23"] += int(len(g23) == 120)

        for i, target_p in enumerate(targets, 1):
            novelty[f"n{i}"]["outside_old_closure_encodings"] += int(target_p not in c0)
            assert target_p not in c0
            assert target_p in c1

        g23_hits = sum(t in g23 for t in targets)
        assert g23_hits == 3
        per_encoding_g23_coverage.append(g23_hits)

        families = {
            "G20_old_S0": c0,
            "G21_AND_plus_post_extension_closure": c1,
            "G22_NOT_no_new_geometry": g22,
            "G23_AND_one_layer_only": g23,
            "G24_direct_target_registry": build_G24(order),
            "G25_transparent_macro_alias": c1,
        }
        presentations = {
            name: present_family(fam, seed, name) for name, fam in families.items()
        }

        for context_index in enc["context_order"]:
            total += 1
            target = target_raw(context_index, order)
            target_p = canon_partition(target)
            base = bayes_accuracy(target)
            exact_gain = post_accuracy(target_p, target) - base
            old_gains = [post_accuracy(p, target) - base for p in c0]
            assert max(old_gains) == 0.0
            decision_diag.setdefault(f"n{context_index+1}", {
                "baseline_bayes_accuracy": base,
                "exact_target_R_corr": exact_gain,
                "exact_target_margin": exact_gain - KAPPA,
                "old_closure_max_R_corr": max(old_gains),
            })

            for name, rows in presentations.items():
                family = families[name]
                pred, scored = frozen_choice(rows, target)
                th = target_handle(rows, target_p)
                reachable = th is not None
                exact = reachable and pred == frozenset((th,))
                totals[name]["target_reachable"] += int(reachable)
                totals[name]["exact_target_chosen"] += int(exact)
                totals[name]["commit"] += int(pred == frozenset(("COMMIT",)))
                totals[name]["family_sizes"].add(len(family))
                totals[name]["space_changed"] += int(family != c0)

    assert total == 256
    assert all(v["outside_old_closure_encodings"] == 64 for v in novelty.values())

    assert totals["G20_old_S0"]["target_reachable"] == 0
    assert totals["G20_old_S0"]["exact_target_chosen"] == 0
    assert totals["G20_old_S0"]["commit"] == 256

    assert totals["G21_AND_plus_post_extension_closure"]["target_reachable"] == 256
    assert totals["G21_AND_plus_post_extension_closure"]["exact_target_chosen"] == 256

    assert totals["G22_NOT_no_new_geometry"]["target_reachable"] == 0
    assert totals["G22_NOT_no_new_geometry"]["exact_target_chosen"] == 0
    assert totals["G22_NOT_no_new_geometry"]["commit"] == 256

    assert totals["G23_AND_one_layer_only"]["target_reachable"] == 192
    assert totals["G23_AND_one_layer_only"]["exact_target_chosen"] == 192
    assert all(x == 3 for x in per_encoding_g23_coverage)

    assert totals["G24_direct_target_registry"]["target_reachable"] == 256
    assert totals["G24_direct_target_registry"]["exact_target_chosen"] == 256
    assert totals["G25_transparent_macro_alias"]["exact_target_chosen"] == 256

    assert totals["G23_AND_one_layer_only"]["commit"] == 0

    family_sizes = {
        name: sorted(vals["family_sizes"])[0] for name, vals in totals.items()
    }
    assert family_sizes == {
        "G20_old_S0": 15,
        "G21_AND_plus_post_extension_closure": 1023,
        "G22_NOT_no_new_geometry": 15,
        "G23_AND_one_layer_only": 120,
        "G24_direct_target_registry": 19,
        "G25_transparent_macro_alias": 1023,
    }

    results = {}
    for name, vals in totals.items():
        results[name] = {
            "family_size": family_sizes[name],
            "target_reachable": vals["target_reachable"],
            "target_reachability": vals["target_reachable"] / total,
            "exact_target_chosen": vals["exact_target_chosen"],
            "exact_target_choice_rate": vals["exact_target_chosen"] / total,
            "commit_decisions": vals["commit"],
            "context_encoding_evaluations": total,
            "experiment_space_changed_vs_S0": vals["space_changed"] == total,
        }

    return {
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "gate": "G2_supplied_target_blind_experiment_space_expansion",
        "encodings": ENCODINGS,
        "contexts_per_encoding": 4,
        "context_encoding_evaluations": total,
        "old_closure": {
            "size": len(canonical_c0),
            "checksum_sha256": checksum(canonical_c0),
            "exhaustively_recomputed": True,
        },
        "expanded_closure": {
            "size": len(canonical_c1),
            "checksum_sha256": checksum(canonical_c1),
            "strictly_contains_old_closure": canonical_c0 < canonical_c1,
        },
        "G23_family": {
            "size": len(canonical_g23),
            "checksum_sha256": checksum(canonical_g23),
            "target_coverage_per_encoding": 3,
            "coverage_ceiling": 3/4,
            "aggregate_target_reachability_ceiling": 192,
            "aggregate_total": 256,
            "ceiling_exceeded": False,
            "n4_exact_target_reachable": False,
            "n4_best_partial_R_corr": g23_n4_max_gain,
            "n4_best_partial_margin": g23_n4_max_gain - KAPPA,
            "n4_co_maximal_partial_partitions": g23_n4_max_count,
        },
        "novelty_proof": novelty,
        "decision_relevance": decision_diag,
        "condition_results": results,
        "construction_specification_ledger": LEDGER,
        "anti_scaffold": {
            "G24": {
                "behavioral_exact": True,
                "target_specific_semantics": 4,
                "classification": "target-specific specification displacement",
                "valid_gate2_evidence": False,
            },
            "G25_transparent_alias": {
                "behavioral_exact": True,
                "visible_total": 1,
                "expanded_total": 10,
                "classification": "alias for S1",
                "valid_independent_evidence": False,
            },
            "G25_opaque_direct_macro": {
                "visible_total": 1,
                "expanded_direct_semantic_bindings": 1023,
                "classification": "hidden specification",
                "valid_gate2_evidence": False,
            },
        },
        "primary_causal_signature": {
            "B_construction_S0": 8,
            "B_construction_S1": 10,
            "B_construction_increases": True,
            "C0_strict_subset_C1": True,
            "novel_targets_outside_C0": True,
            "novel_targets_inside_C1": True,
            "target_blind_extension": True,
            "novel_target_reachability": 256,
            "novel_target_choice": 256,
            "total": 256,
            "local_basin_opening_relative_to_S0": True,
            "autonomous_extension_discovery_tested": False,
            "extension_authorization_tested": False,
        },
        "anonymous_encoding": {
            "primitive_handle_permutation": True,
            "world_label_permutation": True,
            "context_identifier_permutation": True,
            "emitted_experiment_handle_permutation": True,
            "emitted_output_token_polarity_flips": True,
            "operator_semantics_internal_before_public_output_relabeling": True,
        },
        "exact_extensional_encoding_checks": exact_extensional,
    }

def run_upstream_regression():
    if gate1_audit is None:
        raise RuntimeError("Run in-repo so latent_registry_minimality_audit is importable.")
    u = gate1_audit()
    r = u["registry_results"]
    assert r["R0_explicit"]["recovered"] == 15
    assert r["R0_explicit"]["exact_extensional_encodings"] == 64
    assert r["R0_explicit"]["downstream_matches"] == 960
    assert r["R1_basis_xor_closure"]["recovered"] == 15
    assert r["R1_basis_xor_closure"]["precision"] == 1.0
    assert r["R1_basis_xor_closure"]["recall"] == 1.0
    assert r["R1_basis_xor_closure"]["extra_partitions"] == 0
    assert r["R1_basis_xor_closure"]["exact_extensional_encodings"] == 64
    assert r["R1_basis_xor_closure"]["downstream_matches"] == 960
    assert u["registry_specification_ledger"]["R1_basis_xor_closure"]["expanded_total"] == 8
    assert r["R2_primitives_only"]["downstream_matches"] == 256
    assert r["R3_one_xor_layer"]["downstream_matches"] == 640
    inherited = u["upstream_regression"]
    assert inherited["A1_reachability"] == 960
    assert inherited["A1_choices"] == 960
    assert inherited["A1_B_access"] == 1
    assert inherited["A3_reachability"] == 448
    assert inherited["inherited_valuation_navigation_assertions"] is True
    return {
        "gate1_commit": GATE1_COMMIT,
        "R0_exact_extensional_encodings": 64,
        "R1_exact_extensional_encodings": 64,
        "R1_downstream_matches": 960,
        "R1_expanded_B_E_star": 8,
        "R2_downstream_matches": 256,
        "R3_downstream_matches": 640,
        "accessibility_and_valuation_navigation_assertions_inherited": True,
    }

def audit():
    result = audit_core()
    result["upstream_regression"] = run_upstream_regression()
    return result

if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
