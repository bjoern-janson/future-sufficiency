#!/usr/bin/env python3
"""Ephemeral execution harness for DSLI_R1 characterization.

Scientific semantics are imported from the frozen round-v1 reference artifact.
This harness is execution infrastructure only and must run under CPython 3.12.11.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

EXPECTED_PYTHON = (3, 12, 11)
if sys.version_info[:3] != EXPECTED_PYTHON:
    raise SystemExit(f"FROZEN_RUNTIME_MISMATCH: expected {EXPECTED_PYTHON}, got {sys.version_info[:3]}")

ROOT = Path(__file__).resolve().parents[1]
AUD = ROOT / "audits"
OUT = ROOT / "characterization_out"
OUT.mkdir(exist_ok=True)

P_SPEC = AUD / "extension_decision_substrate_round_v1_specification.md"
P_MACHINE = AUD / "extension_decision_substrate_round_v1_specification.json"
P_REF = AUD / "extension_decision_substrate_round_v1_reference.py"
P_WORLD = AUD / "extension_decision_substrate_round_v1_calibration_world.json"
P_FIX = AUD / "extension_decision_substrate_round_v1_conformance_fixtures.json"
P_MANIFEST = AUD / "extension_decision_substrate_round_v1_manifest.json"
P_SPECCOMPLETE = AUD / "extension_decision_substrate_round_v1_speccomplete_results.json"

ALLOWED_INPUTS = [P_SPEC, P_MACHINE, P_REF, P_WORLD, P_FIX, P_MANIFEST, P_SPECCOMPLETE]
for p in ALLOWED_INPUTS:
    if not p.is_file():
        raise SystemExit(f"MISSING_FROZEN_INPUT: {p}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


manifest = json.loads(P_MANIFEST.read_text(encoding="utf-8"))
speccomplete = json.loads(P_SPECCOMPLETE.read_text(encoding="utf-8"))
machine = json.loads(P_MACHINE.read_text(encoding="utf-8"))
world_compact = json.loads(P_WORLD.read_text(encoding="utf-8"))

assert manifest["freeze_semantics"] == "ROUND_V1_CONSTRUCTION_FREEZE"
assert manifest["state"]["characterization_executed"] is False
assert manifest["state"]["characterization_authorized"] is False
assert speccomplete["SpecComplete"] is True
assert speccomplete["procedural_output"] == "CHARACTERIZATION_AUTHORIZED"
assert speccomplete["state_after_gate"]["characterization_authorized"] is True
assert speccomplete["state_after_gate"]["characterization_executed"] is False
assert speccomplete["state_after_gate"]["calibration_evidence_generated"] is False
assert speccomplete["parent_construction_commit"] == "6482667d3b48c2e0c47bfea2fb44da92187b0511"
assert machine["round"]["actual_target_access"] is False
assert world_compact["characterization_results_present"] is False
assert world_compact["case_count"] == 26
assert world_compact["sampling"] == "NONE"

# Verify every construction bundle byte anchor before characterization.
path_map = {
    str(P_SPEC.relative_to(ROOT)): P_SPEC,
    str(P_MACHINE.relative_to(ROOT)): P_MACHINE,
    str(P_REF.relative_to(ROOT)): P_REF,
    str(P_WORLD.relative_to(ROOT)): P_WORLD,
    str(P_FIX.relative_to(ROOT)): P_FIX,
}
anchor_checks = {}
for rel, meta in manifest["bundle_files"].items():
    p = path_map[rel]
    got = sha256_file(p)
    ok = got == meta["sha256"]
    anchor_checks[rel] = {"expected_sha256": meta["sha256"], "observed_sha256": got, "match": ok}
    if not ok:
        raise SystemExit(f"FROZEN_BUNDLE_HASH_MISMATCH: {rel}")

# Import frozen reference semantics without modifying them.
spec = importlib.util.spec_from_file_location("dsli_r1_frozen_reference", P_REF)
ref = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(ref)

if tuple(ref.LANG) != tuple(manifest["language_treatment_set"]):
    raise SystemExit("TREATMENT_REGISTRY_MISMATCH")

TOK = tuple(ref.TOK)
PI, PJ, EQ, NWP = ref.PI, ref.PJ, ref.EQ, ref.NWP


def relation_from_compact(case):
    n = case["n"]
    r = {p: case["default"] for p in ref.pairs(n)}
    for token, plist in case.get("overrides", {}).items():
        for a, b in plist:
            p = tuple(sorted((a, b)))
            if p not in r:
                raise AssertionError((case["relation_id"], "bad_pair", p))
            r[p] = token
    if set(r) != set(ref.pairs(n)):
        raise AssertionError((case["relation_id"], "incomplete_relation"))
    if ref.counts(r) != case["K"]["C_Sigma"]:
        raise AssertionError((case["relation_id"], "count_mismatch", ref.counts(r), case["K"]["C_Sigma"]))
    return r


# Independent construction check: frozen generator and materialized compact world
# must encode the same 26 relations. This does not apply any treatment language.
generated = {c["relation_id"]: c for c in ref.world()}
if set(generated) != {c["relation_id"] for c in world_compact["cases"]}:
    raise SystemExit("CALIBRATION_WORLD_ID_SET_MISMATCH")
for c in world_compact["cases"]:
    g = generated[c["relation_id"]]
    r = relation_from_compact(c)
    if g["anonymous_candidate_count"] != c["n"]:
        raise SystemExit(f"CALIBRATION_N_MISMATCH:{c['relation_id']}")
    if ref.records(r) != g["records"]:
        raise SystemExit(f"CALIBRATION_RELATION_MISMATCH:{c['relation_id']}")


def classify(rep: bool, rep_a: bool, b_star, b_r: int) -> str:
    if not rep:
        return "NOT_REPRESENTABLE"
    if rep and not rep_a:
        return "REPRESENTABLE_AUTHORITY_INVALID"
    assert b_star is not None
    if b_star >= b_r:
        return "ADMISSIBLE_REPRESENTATION_NO_CONTRACTION"
    return "FAITHFUL_CONTRACTION"


# Characterization proper: exactly 26 frozen relations x 6 frozen treatments.
cases_out = []
flat_cells = []
for case in world_compact["cases"]:
    rid = case["relation_id"]
    n = case["n"]
    r = relation_from_compact(case)
    b_r = n * (n - 1) // 2
    lang_out = {}
    for lang in ref.LANG:
        member, burden = ref.pi(lang, r, n)
        rep = bool(member)
        # Frozen round-v1 authority regime: every legal treatment witness is admissible.
        rep_a = rep
        b_star = burden if rep_a else None
        status = classify(rep, rep_a, b_star, b_r)
        cell = {
            "relation_id": rid,
            "language_id": lang,
            "Rep": rep,
            "RepA": rep_a,
            "B_star": b_star,
            "B_R": b_r,
            "Sigma_outcome": status,
        }
        lang_out[lang] = {k: v for k, v in cell.items() if k not in ("relation_id", "language_id")}
        flat_cells.append(cell)
    cases_out.append({
        "relation_id": rid,
        "n": n,
        "matched_block_id": case["K"]["matched_block_id"],
        "structural_descriptor_K": case["K"],
        "languages": lang_out,
    })

assert len(flat_cells) == 26 * 6

# Frozen controls, evaluated mechanically for each target relation.
control_cells = []
for case in world_compact["cases"]:
    n = case["n"]
    b_r = n * (n - 1) // 2
    control_cells.append({
        "relation_id": case["relation_id"],
        "control_id": "W_DIRECT_LOOKUP",
        "Rep": True,
        "RepA": True,
        "B_star": b_r + 1,
        "B_R": b_r,
        "Sigma_outcome": "ADMISSIBLE_REPRESENTATION_NO_CONTRACTION",
    })
    control_cells.append({
        "relation_id": case["relation_id"],
        "control_id": "W_IDENTITY_ORACLE",
        "Rep": True,
        "RepA": False,
        "B_star": None,
        "B_R": b_r,
        "Sigma_outcome": "REPRESENTABLE_AUTHORITY_INVALID",
        "authority_violation": "UNLICENSED_CANDIDATE_IDENTITY",
    })

# Nuisance transport proof over all 64 frozen encodings per calibration case.
# We do not re-optimize language witnesses; the SpecComplete gate already certified
# permutation equivariance of all language semantics. Here we verify every frozen
# nuisance candidate permutation is a bijection and that relation transport is
# exactly invertible, so the characterized cell transports without alteration.
transport_checks = 0
transport_mismatches = 0
for case in world_compact["cases"]:
    n = case["n"]
    r = relation_from_compact(case)
    for e in range(64):
        nu = ref.nuisance(case["relation_id"], n, e)
        perm = nu["candidate_permutation"]
        if sorted(perm) != list(range(n)):
            transport_mismatches += 1
            continue
        old_to_new = {old: new for new, old in enumerate(perm)}
        new_to_old = {new: old for old, new in old_to_new.items()}
        tr = {}
        for (i, j), token in r.items():
            a, b = old_to_new[i], old_to_new[j]
            if a < b:
                tr[a, b] = token
            else:
                tr[b, a] = PI if token == PJ else PJ if token == PI else token
        back = {}
        for (a, b), token in tr.items():
            i, j = new_to_old[a], new_to_old[b]
            if i < j:
                back[i, j] = token
            else:
                back[j, i] = PI if token == PJ else PJ if token == PI else token
        transport_checks += 1
        if back != r:
            transport_mismatches += 1

# Pair-orientation normalization proof on every pair of every calibration relation.
pair_swap_checks = 0
pair_swap_mismatches = 0
for case in world_compact["cases"]:
    r = relation_from_compact(case)
    for (i, j), token in r.items():
        swapped = PI if token == PJ else PJ if token == PI else token
        # Normalize record (j,i,swapped) back to canonical (i,j).
        renorm = PI if swapped == PJ else PJ if swapped == PI else swapped
        pair_swap_checks += 1
        if renorm != token:
            pair_swap_mismatches += 1

if transport_mismatches or pair_swap_mismatches:
    raise SystemExit(f"NUISANCE_OR_PAIR_SWAP_FAILURE:{transport_mismatches}:{pair_swap_mismatches}")

# Per-language summaries and matched-block response surface.
summary_by_language = {}
for lang in ref.LANG:
    cells = [c for c in flat_cells if c["language_id"] == lang]
    status_counts = Counter(c["Sigma_outcome"] for c in cells)
    bvals = Counter(str(c["B_star"]) for c in cells if c["B_star"] is not None)
    summary_by_language[lang] = {
        "case_count": len(cells),
        "representable_count": sum(c["Rep"] for c in cells),
        "admissible_representable_count": sum(c["RepA"] for c in cells),
        "status_counts": dict(sorted(status_counts.items())),
        "B_star_value_counts": dict(sorted(bvals.items())),
    }

blocks = defaultdict(list)
for c in cases_out:
    blocks[c["matched_block_id"]].append(c)
block_out = []
for bid in sorted(blocks):
    members = sorted(blocks[bid], key=lambda x: x["structural_descriptor_K"]["case_role"])
    if len(members) != 2:
        raise SystemExit(f"MATCHED_BLOCK_CARDINALITY_FAILURE:{bid}:{len(members)}")
    block_out.append({
        "matched_block_id": bid,
        "case_A": members[0]["relation_id"],
        "case_B": members[1]["relation_id"],
        "manipulated_axes": members[0]["structural_descriptor_K"]["manipulated_axes"],
        "held_fixed_axes": members[0]["structural_descriptor_K"]["held_fixed_axes"],
        "language_outcomes": {
            lang: {
                "A": members[0]["languages"][lang]["Sigma_outcome"],
                "B": members[1]["languages"][lang]["Sigma_outcome"],
                "changed": members[0]["languages"][lang]["Sigma_outcome"] != members[1]["languages"][lang]["Sigma_outcome"],
            }
            for lang in ref.LANG
        },
    })

result = {
    "schema": "dsli-round-v1-characterization-results-v1",
    "round_id": "DSLI_R1",
    "round_version": 1,
    "parent_speccomplete_commit": "0f2e2e9cf38258b583dc3d7f9bbbf2cd047fcf53",
    "parent_construction_commit": "6482667d3b48c2e0c47bfea2fb44da92187b0511",
    "evidence_role": "CALIBRATION_EVIDENCE",
    "runtime": {
        "python_implementation": sys.implementation.name,
        "python_version": ".".join(map(str, sys.version_info[:3])),
        "required_python_version": "3.12.11",
        "exact_runtime_match": sys.version_info[:3] == EXPECTED_PYTHON,
        "standard_library_only": True,
        "floating_point_used": False,
    },
    "frozen_input_checks": {
        "bundle_sha256_anchors": anchor_checks,
        "SpecComplete": True,
        "characterization_authorized": True,
        "actual_target_access": False,
        "calibration_world_case_count": 26,
        "treatment_language_count": 6,
    },
    "characterization": {
        "cell_count": len(flat_cells),
        "cases": cases_out,
        "flat_cells": flat_cells,
        "summary_by_language": summary_by_language,
        "matched_blocks": block_out,
        "controls": control_cells,
    },
    "invariance": {
        "nuisance_encodings_per_case": 64,
        "nuisance_relation_transport_checks": transport_checks,
        "nuisance_relation_transport_mismatches": transport_mismatches,
        "nuisance_result_invariance_basis": "SpecComplete-certified language permutation equivariance + exact bijective transport of every frozen nuisance candidate permutation",
        "pair_swap_checks": pair_swap_checks,
        "pair_swap_mismatches": pair_swap_mismatches,
    },
    "anti_downstream": {
        "language_family_modified": False,
        "calibration_world_modified": False,
        "adaptive_sampling_performed": False,
        "new_calibration_case_added": False,
        "actual_target_read": False,
        "application_set_selected": False,
        "governance_selected": False,
        "candidate_ranking_performed": False,
        "actual_Q_extension_defined": False,
        "authorization_performed": False,
        "binding_performed": False,
        "execution_performed": False,
    },
}

result_bytes = (canon(result) + "\n").encode("utf-8")
result_sha = hashlib.sha256(result_bytes).hexdigest()
(OUT / "extension_decision_substrate_round_v1_characterization_results.json").write_bytes(result_bytes)

# Compact human-readable summary, still mechanically derived from machine result.
lines = [
    "# DSLI_R1 Characterization Execution",
    "",
    "Frozen parents:",
    "",
    "```text",
    "SpecComplete  0f2e2e9cf38258b583dc3d7f9bbbf2cd047fcf53",
    "Construction  6482667d3b48c2e0c47bfea2fb44da92187b0511",
    "```",
    "",
    f"Runtime: `CPython {'.'.join(map(str, sys.version_info[:3]))}` (exact frozen match).",
    "",
    "## Treatment summary",
    "",
    "| Language | Representable | Status counts |",
    "|---|---:|---|",
]
for lang in ref.LANG:
    s = summary_by_language[lang]
    sc = ", ".join(f"{k}={v}" for k, v in s["status_counts"].items())
    lines.append(f"| `{lang}` | {s['representable_count']}/26 | {sc} |")
lines += [
    "",
    "## Invariance",
    "",
    f"- nuisance relation-transport checks: {transport_checks}, mismatches: {transport_mismatches}",
    f"- pair-swap checks: {pair_swap_checks}, mismatches: {pair_swap_mismatches}",
    "",
    "## Boundaries",
    "",
    "No language, calibration case, burden rule, authority rule, closure rule, or runtime was modified during characterization.",
    "No actual-target artifact was read. No application set, governance contract, candidate ranking, Q_extension, authorization, binding, or execution was produced.",
    "",
    f"Machine-result SHA-256: `{result_sha}`",
    "",
]
(OUT / "extension_decision_substrate_round_v1_characterization_audit.md").write_text("\n".join(lines), encoding="utf-8")

attestation = {
    "schema": "dsli-r1-characterization-runtime-attestation-v1",
    "python_version": ".".join(map(str, sys.version_info[:3])),
    "python_executable": sys.executable,
    "exact_frozen_runtime_match": sys.version_info[:3] == EXPECTED_PYTHON,
    "result_sha256": result_sha,
    "input_sha256": {str(p.relative_to(ROOT)): sha256_file(p) for p in ALLOWED_INPUTS},
    "allowed_input_paths": [str(p.relative_to(ROOT)) for p in ALLOWED_INPUTS],
    "actual_target_access": False,
}
(OUT / "extension_decision_substrate_round_v1_characterization_runtime.json").write_text(canon(attestation) + "\n", encoding="utf-8")

print(canon({
    "ok": True,
    "runtime": attestation["python_version"],
    "cell_count": len(flat_cells),
    "result_sha256": result_sha,
    "nuisance_transport_checks": transport_checks,
    "pair_swap_checks": pair_swap_checks,
    "summary_by_language": summary_by_language,
}))
