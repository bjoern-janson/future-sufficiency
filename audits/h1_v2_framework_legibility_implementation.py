"""H1_V2_R1 implementation construction.

Faithful realization of the preregistration frozen at
`de42e3422b55a962bd16ae9fdba87447f387daa1`.

Importing this module performs no scientific execution, queries no
reconstructor, scores no reconstruction output, and computes no primary L2
collision surface.  It materializes only the implementation objects authorized
by preregistration section 18.
"""
from __future__ import annotations

import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

ROUND_ID = "H1_V2_R1"
PREREGISTRATION_COMMIT = "de42e3422b55a962bd16ae9fdba87447f387daa1"
FILE_BOUNDARY = "\n<<<H1_FILE_BOUNDARY>>>\n"
PATH_CONTENT_DELIMITER = "\n"
NOT_IDENTIFIED = "NOT_IDENTIFIED"

IMPLEMENTATION_STATE = {
    "SELECTED_V2_TARGET": "H1",
    "H1_V2_PREREGISTRATION": "FROZEN",
    "H1_V2_IMPLEMENTATION_CONSTRUCTED": True,
    "H1_V2_SPECCOMPLETE": False,
    "H1_V2_EXECUTION_AUTHORIZED": False,
    "H1_V2_RECONSTRUCTION_EVIDENCE_SEEN": False,
    "H1_V2_COLLISION_EVIDENCE_SEEN": False,
    "BACKWARD_DESIGN_AUTHORITY": 0,
}

PRIMARY_STATES = (
    ("S01", "6482667d3b48c2e0c47bfea2fb44da92187b0511", "DSLI_R1_CONSTRUCTION"),
    ("S02", "0f2e2e9cf38258b583dc3d7f9bbbf2cd047fcf53", "DSLI_R1_SPECCOMPLETE"),
    ("S03", "ddffe4b976352b3fec4efc3300a0dcc0097ca217", "DSLI_R1_CHARACTERIZATION"),
    ("S04", "f0c594bc9ed70856ec980a06926275584db79086", "APPLICATION_SET_IDENTITY_CARRY_FORWARD"),
    ("S05", "f8a76956ecfbf4848b62659e6db23c3918311679", "ACTUAL_APPLICATION_PREREGISTRATION"),
    ("S06", "a4eac05b9387e46bebf2008b3cfb57f3e375577f", "ACTUAL_APPLICATION_EXECUTION"),
    ("S07", "81efea2405e3b0269c9bad3bf417d4ab73ea080b", "DSLI_R1_TERMINAL_LEDGER"),
    ("S08", "a72f5a8df8f69d33e79304a9dafd540d1d82f601", "DEVELOPMENT_EVIDENCE_INVENTORY"),
    ("S09", "5f1282d76894716ed329a762eca8de5bfe0dc64b", "V2_TARGET_SELECTION_PROTOCOL"),
    ("S10", "80caa03109a105fd6c70d58f7d6663d957fc20ff", "H1_TARGET_SELECTED"),
)

STATE_MANIFEST = {
    "round_id": ROUND_ID,
    "preregistration_commit": PREREGISTRATION_COMMIT,
    "primary_state_type": "AUTHENTIC_REPOSITORY_CHECKPOINT",
    "synthetic_primary_states_allowed": False,
    "primary_states": [
        {"state_id": state_id, "commit": commit, "frontier_id": frontier}
        for state_id, commit, frontier in PRIMARY_STATES
    ],
}

COORDINATES = (
    "frontier_id",
    "epistemic_status",
    "provenance_class",
    "closure_state",
    "next_authorized_operation",
    "constraint_profile",
    "checkpoint_anchor",
)
CORE_COORDINATES = COORDINATES[:-1]
COORDINATE_OUTCOMES = {
    "CORRECT",
    "INCORRECT",
    "NOT_IDENTIFIED",
    "UNPARSEABLE",
    "NOT_EVALUATED",
}

EPISTEMIC_STATUS = (
    "DESIGN_FROZEN",
    "SPECIFICATION_VALID",
    "CALIBRATION_CHARACTERIZED",
    "IDENTITY_CARRY_FORWARD_FROZEN",
    "ACTUAL_APPLICATION_PREREGISTERED",
    "POST_SPECIFICATION_APPLICATION_EVIDENCE",
    "SCIENTIFIC_STATE_CLOSED",
    "DEVELOPMENT_INVENTORY_FROZEN",
    "TARGET_SELECTION_RULE_FROZEN",
    "TARGET_SELECTED",
)
PROVENANCE_CLASS = (
    "DESIGN_ARTIFACT",
    "SPECIFICATION_CONFORMANCE",
    "CALIBRATION_EVIDENCE",
    "DESIGN_CARRY_FORWARD",
    "PREREGISTERED_DESIGN",
    "POST_SPECIFICATION_APPLICATION_EVIDENCE",
    "TERMINAL_CLASSIFICATION",
    "DEVELOPMENT_EVIDENCE",
    "DEVELOPMENT_DECISION_PROTOCOL",
    "DEVELOPMENT_DECISION",
)
CLOSURE_STATE_BY_INDEX = (
    "LIVE_DESIGN_SURFACE",
    "LIVE_DESIGN_SURFACE",
    "LIVE_DESIGN_SURFACE",
    "LIVE_DESIGN_SURFACE",
    "LIVE_DESIGN_SURFACE",
    "STOP_REQUIRED",
    "CLOSED_ARCHIVE",
    "POST_V1_DEVELOPMENT",
    "POST_V1_DEVELOPMENT",
    "POST_V1_DEVELOPMENT",
)
NEXT_OPERATION = (
    "RUN_SPECCOMPLETE",
    "RUN_CHARACTERIZATION",
    "FREEZE_APPLICATION_SET",
    "PREREGISTER_ACTUAL_APPLICATION",
    "EXECUTE_ACTUAL_APPLICATION",
    "ARCHIVE_TERMINAL_LEDGER",
    "CREATE_DEVELOPMENT_INVENTORY",
    "FREEZE_TARGET_SELECTION_RULE",
    "APPLY_TARGET_SELECTION_RULE",
    "PREREGISTER_H1_V2",
)

CONSTRAINT_PROFILES = {
    "CP01": "SpecComplete before characterization; no actual-target application; no downstream selection/authorization.",
    "CP02": "characterization only after specification validity; no actual-target application; no downstream selection/authorization.",
    "CP03": "calibration evidence cannot select/rank languages; no actual-target access in characterization; no Q_extension/authorization/binding.",
    "CP04": "application-set carry-forward is identity only; no target access; no application mechanics; no Q_extension/authorization.",
    "CP05": "conformance before target access; timeout/failure-to-find cannot imply NOT_REPRESENTABLE; NOT_DEFINED != 0 != infinity; no language winner/Q_extension/authorization.",
    "CP06": "application outputs are descriptive only; no language/governance winner; no Q_extension/authorization/v2 mutation; STOP_DSLI_R1.",
    "CP07": "DSLI_R1 immutable and closed; terminal ledger is retrospective only; terminal ledger cannot design v2.",
    "CP08": "development inventory is descriptive only; no candidate ranking or selection; v1 remains immutable.",
    "CP09": "selection rule may be frozen; protocol cannot name a winner; selection rule != v2 experimental design; v1 remains immutable.",
    "CP10": "H1 receives design focus only; H1 selection != validation; no v2 execution authorization; v1 remains immutable.",
}

GOLD_TARGETS: dict[str, dict[str, str]] = {}
for index, (state_id, commit, frontier) in enumerate(PRIMARY_STATES):
    GOLD_TARGETS[state_id] = {
        "frontier_id": frontier,
        "epistemic_status": EPISTEMIC_STATUS[index],
        "provenance_class": PROVENANCE_CLASS[index],
        "closure_state": CLOSURE_STATE_BY_INDEX[index],
        "next_authorized_operation": NEXT_OPERATION[index],
        "constraint_profile": f"CP{index + 1:02d}",
        "checkpoint_anchor": commit,
    }

GOLD_TARGET_MANIFEST = {
    "round_id": ROUND_ID,
    "coordinate_order": list(COORDINATES),
    "l2_core_coordinates": list(CORE_COORDINATES),
    "domains": {
        "frontier_id": [x[2] for x in PRIMARY_STATES],
        "epistemic_status": list(EPISTEMIC_STATUS),
        "provenance_class": list(PROVENANCE_CLASS),
        "closure_state": [
            "LIVE_DESIGN_SURFACE",
            "STOP_REQUIRED",
            "CLOSED_ARCHIVE",
            "POST_V1_DEVELOPMENT",
        ],
        "next_authorized_operation": list(NEXT_OPERATION),
        "constraint_profile": list(CONSTRAINT_PROFILES),
        "checkpoint_anchor": [x[1] for x in PRIMARY_STATES],
    },
    "constraint_profiles": CONSTRAINT_PROFILES,
    "targets": GOLD_TARGETS,
}

EXECUTION_MANIFEST_SCHEMA = {
    "round_id": {"const": ROUND_ID},
    "pre_access_manifest_frozen": {"const": True},
    "reconstructors": {
        "type": "array",
        "min_items": 3,
        "required_item_fields": [
            "provider",
            "exact_model_identifier_version",
            "access_mode",
            "system_prompt_visibility",
            "temperature_or_deterministic_setting",
            "sampling_parameters",
            "tool_availability",
            "context_limits",
            "execution_date",
        ],
    },
    "mutation_after_first_packet_exposure": {"const": False},
}

FIXTURE_GOLD = dict(GOLD_TARGETS["S01"])
FIXTURE_WRONG_FRONTIER = GOLD_TARGETS["S02"]["frontier_id"]
CONFORMANCE_FIXTURES = {
    "fixture_type": "CONFORMANCE_FIXTURE",
    "identity_masking_raw": (
        "commit 6482667d3b48c2e0c47bfea2fb44da92187b0511  \r\n"
        "workflow run 31827317141\r\n"
        "job id: 94854380803\r\n"
        "artifact 9230634718\r\n"
        "date 2026-08-14\r\n"
        "time 2026-08-14T19:25:54Z\r\n"
    ),
    "identity_masking_expected": (
        "commit <HEX_ID>\n"
        "workflow run <RUN_ID>\n"
        "job id: <RUN_ID>\n"
        "artifact <RUN_ID>\n"
        "date <TIME_ID>\n"
        "time <TIME_ID>\n"
    ),
    "semantic_preservation_raw": (
        "audits/example.md\n# Status\nCALIBRATION_EVIDENCE\nB*=28\nSTOP_DSLI_R1\n"
    ),
    "fiber_grouping": {"A": "same", "B": "same", "C": "different"},
}

_HEX_RE = re.compile(r"(?<![0-9A-Fa-f])[0-9A-Fa-f]{7,64}(?![0-9A-Fa-f])")
_RUN_ID_RE = re.compile(
    r"(?i)\b(workflow\s+run|run\s+id|job(?:\s+id)?|artifact(?:\s+id)?)"
    r"(\s*[:#]?\s*)(\d+)\b"
)
_TIME_RE = re.compile(
    r"\b\d{4}-\d{2}-\d{2}"
    r"(?:T\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:\d{2})?)?\b"
)


def _git(repo_root: Path, *args: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.stdout


def resolve_commit(repo_root: Path, commit: str) -> str:
    return _git(repo_root, "rev-parse", f"{commit}^{{commit}}").decode("ascii").strip()


def eligible_paths(repo_root: Path, commit: str) -> tuple[str, ...]:
    names = _git(repo_root, "ls-tree", "-r", "--name-only", commit).decode("utf-8").splitlines()
    eligible = []
    for path in names:
        p = PurePosixPath(path)
        if path == "README.md" or (p.parent.as_posix() == "audits" and p.suffix == ".md"):
            eligible.append(path)
    return tuple(sorted(eligible))


def read_utf8_at(repo_root: Path, commit: str, path: str) -> str:
    return _git(repo_root, "show", f"{commit}:{path}").decode("utf-8", errors="strict")


def serialize_packet_records(records: Iterable[tuple[str, str]]) -> str:
    ordered = sorted(records, key=lambda item: item[0])
    return FILE_BOUNDARY.join(
        f"{path}{PATH_CONTENT_DELIMITER}{text}" for path, text in ordered
    )


def build_framework_packet(repo_root: Path, commit: str) -> tuple[str, tuple[str, ...]]:
    paths = eligible_paths(repo_root, commit)
    records = [(path, read_utf8_at(repo_root, commit, path)) for path in paths]
    return serialize_packet_records(records), paths


def build_readme_packet(repo_root: Path, commit: str) -> str:
    return serialize_packet_records(
        [("README.md", read_utf8_at(repo_root, commit, "README.md"))]
    )


def exposure_burden(packet: str, paths: Iterable[str]) -> dict[str, int]:
    path_tuple = tuple(paths)
    return {
        "N_documents": len(path_tuple),
        "N_UTF8_bytes": len(packet.encode("utf-8")),
        "N_Unicode_codepoints": len(packet),
    }


def canonicalize_semantic_packet(packet: str) -> str:
    text = packet.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip(" \t") for line in text.split("\n"))
    text = _RUN_ID_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}<RUN_ID>", text)
    text = _TIME_RE.sub("<TIME_ID>", text)
    text = _HEX_RE.sub("<HEX_ID>", text)
    return text


def core_target(target: dict[str, str]) -> tuple[str, ...]:
    return tuple(target[key] for key in CORE_COORDINATES)


def group_exact_fibers(observations: dict[str, str]) -> tuple[tuple[str, ...], ...]:
    groups: dict[str, list[str]] = defaultdict(list)
    for state_id in sorted(observations):
        groups[observations[state_id]].append(state_id)
    return tuple(sorted((tuple(group) for group in groups.values()), key=lambda g: g[0]))


def reference_group_exact_fibers(
    observations: dict[str, str],
) -> tuple[tuple[str, ...], ...]:
    remaining = set(observations)
    groups = []
    while remaining:
        seed = min(remaining)
        same = tuple(sorted(s for s in remaining if observations[s] == observations[seed]))
        groups.append(same)
        remaining.difference_update(same)
    return tuple(sorted(groups, key=lambda g: g[0]))


def evaluate_collisions(
    observations: dict[str, str],
    targets: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    defects: list[dict[str, Any]] = []
    for fiber in group_exact_fibers(observations):
        if len(fiber) < 2:
            continue
        for i, state_a in enumerate(fiber):
            for state_b in fiber[i + 1 :]:
                differing = [
                    key
                    for key in CORE_COORDINATES
                    if targets[state_a][key] != targets[state_b][key]
                ]
                if differing:
                    defects.append(
                        {
                            "state_a": state_a,
                            "state_b": state_b,
                            "differing_core_coordinates": differing,
                        }
                    )
    return defects


def allowed_token_schema() -> dict[str, list[str]]:
    return {
        key: list(GOLD_TARGET_MANIFEST["domains"][key]) + [NOT_IDENTIFIED]
        for key in COORDINATES
    }


def fixed_reconstruction_prompt() -> str:
    return (
        "You are reconstructing the scientific state represented by the supplied framework packet.\n"
        "Use only the packet. Do not use external knowledge, browsing, memory from other cases, or inferred chronology.\n\n"
        "Return exactly one JSON object with these keys:\n"
        "frontier_id\n"
        "epistemic_status\n"
        "provenance_class\n"
        "closure_state\n"
        "next_authorized_operation\n"
        "constraint_profile\n"
        "checkpoint_anchor\n\n"
        "Use only the allowed tokens defined in the accompanying schema.\n"
        "If a coordinate cannot be identified from the packet, return the exact string NOT_IDENTIFIED for that coordinate.\n"
        "Do not guess and do not replace NOT_IDENTIFIED with a default value.\n"
    )


def parse_reconstruction_output(raw: str) -> dict[str, Any] | None:
    try:
        obj = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return None
    if not isinstance(obj, dict) or set(obj) != set(COORDINATES):
        return None
    return obj


def score_reconstruction(
    raw: str | None,
    gold: dict[str, str],
    *,
    evaluated: bool = True,
) -> dict[str, str]:
    if not evaluated:
        return {key: "NOT_EVALUATED" for key in COORDINATES}
    if raw is None:
        return {key: "UNPARSEABLE" for key in COORDINATES}
    obj = parse_reconstruction_output(raw)
    if obj is None:
        return {key: "UNPARSEABLE" for key in COORDINATES}

    schema = allowed_token_schema()
    out: dict[str, str] = {}
    for key in COORDINATES:
        value = obj[key]
        if not isinstance(value, str) or value not in schema[key]:
            out[key] = "UNPARSEABLE"
        elif value == NOT_IDENTIFIED:
            out[key] = "NOT_IDENTIFIED"
        elif value == gold[key]:
            out[key] = "CORRECT"
        else:
            out[key] = "INCORRECT"
    assert set(out.values()) <= COORDINATE_OUTCOMES
    return out


def state_level_reconstruction(coordinate_scores: dict[str, str]) -> str:
    if all(coordinate_scores[key] == "CORRECT" for key in COORDINATES):
        return "EXACT_RECONSTRUCTION"
    if all(coordinate_scores[key] == "NOT_EVALUATED" for key in COORDINATES):
        return "NOT_EVALUATED"
    return "COORDINATE_ERRORS_PRESENT"


def validate_execution_manifest(manifest: dict[str, Any]) -> bool:
    if manifest.get("round_id") != ROUND_ID:
        return False
    if manifest.get("pre_access_manifest_frozen") is not True:
        return False
    if manifest.get("mutation_after_first_packet_exposure") is not False:
        return False
    reconstructors = manifest.get("reconstructors")
    if not isinstance(reconstructors, list) or len(reconstructors) < 3:
        return False
    required = set(EXECUTION_MANIFEST_SCHEMA["reconstructors"]["required_item_fields"])
    return all(isinstance(item, dict) and required <= set(item) for item in reconstructors)


def _fixture_target(base: dict[str, str], **updates: str) -> dict[str, str]:
    out = dict(base)
    out.update(updates)
    return out


def run_conformance(repo_root: Path) -> dict[str, str]:
    """Evaluate K1-K15 without model access or primary L2 fiber computation."""
    checks: dict[str, str] = {}

    # K1 — all ten commit anchors resolve exactly.
    checks["K1"] = "PASS" if all(
        resolve_commit(repo_root, commit) == commit for _, commit, _ in PRIMARY_STATES
    ) else "FAIL"

    # K2/K3 — packet membership and UTF-8 validity.
    membership_ok = True
    utf8_ok = True
    for _, commit, _ in PRIMARY_STATES:
        try:
            paths = eligible_paths(repo_root, commit)
            raw_names = _git(repo_root, "ls-tree", "-r", "--name-only", commit).decode("utf-8").splitlines()
            expected = tuple(sorted(
                path for path in raw_names
                if path == "README.md"
                or (
                    PurePosixPath(path).parent.as_posix() == "audits"
                    and PurePosixPath(path).suffix == ".md"
                )
            ))
            membership_ok &= paths == expected
            for path in paths:
                read_utf8_at(repo_root, commit, path)
        except UnicodeDecodeError:
            utf8_ok = False
        except Exception:
            membership_ok = False
            utf8_ok = False
    checks["K2"] = "PASS" if membership_ok else "FAIL"
    checks["K3"] = "PASS" if utf8_ok else "FAIL"

    # K4/K5 — deterministic primary and README-only serialization.
    checks["K4"] = "PASS" if all(
        build_framework_packet(repo_root, commit)[0]
        == build_framework_packet(repo_root, commit)[0]
        for _, commit, _ in PRIMARY_STATES
    ) else "FAIL"
    checks["K5"] = "PASS" if all(
        build_readme_packet(repo_root, commit) == build_readme_packet(repo_root, commit)
        for _, commit, _ in PRIMARY_STATES
    ) else "FAIL"

    # K6/K7 — gold manifest identity and token domains.
    state_by_id = {
        state_id: {"commit": commit, "frontier_id": frontier}
        for state_id, commit, frontier in PRIMARY_STATES
    }
    k6 = set(GOLD_TARGETS) == set(state_by_id) and all(
        GOLD_TARGETS[state_id]["frontier_id"] == state_by_id[state_id]["frontier_id"]
        and GOLD_TARGETS[state_id]["checkpoint_anchor"] == state_by_id[state_id]["commit"]
        for state_id in state_by_id
    )
    k7 = all(
        target[key] in GOLD_TARGET_MANIFEST["domains"][key]
        for target in GOLD_TARGETS.values()
        for key in COORDINATES
    )
    checks["K6"] = "PASS" if k6 else "FAIL"
    checks["K7"] = "PASS" if k7 else "FAIL"

    # K8/K9 — declared identity masks and semantic preservation.
    checks["K8"] = "PASS" if (
        canonicalize_semantic_packet(CONFORMANCE_FIXTURES["identity_masking_raw"])
        == CONFORMANCE_FIXTURES["identity_masking_expected"]
    ) else "FAIL"
    semantic_raw = CONFORMANCE_FIXTURES["semantic_preservation_raw"]
    checks["K9"] = "PASS" if canonicalize_semantic_packet(semantic_raw) == semantic_raw else "FAIL"

    # K10 — exact fiber grouping agrees with an independently structured reference.
    fiber_fixture = CONFORMANCE_FIXTURES["fiber_grouping"]
    checks["K10"] = "PASS" if (
        group_exact_fibers(fiber_fixture) == reference_group_exact_fibers(fiber_fixture)
    ) else "FAIL"

    # K11/K12 — heterogeneous target is a defect; homogeneous target is not.
    common_obs = {"A": "same", "B": "same"}
    base = dict(FIXTURE_GOLD)
    hetero = {
        "A": base,
        "B": _fixture_target(base, frontier_id=FIXTURE_WRONG_FRONTIER),
    }
    homo = {"A": base, "B": dict(base)}
    checks["K11"] = "PASS" if len(evaluate_collisions(common_obs, hetero)) == 1 else "FAIL"
    checks["K12"] = "PASS" if len(evaluate_collisions(common_obs, homo)) == 0 else "FAIL"

    # K13 — checkpoint identity alone cannot create an L2 target distinction.
    anchor_a = PRIMARY_STATES[0][1]
    anchor_b = PRIMARY_STATES[1][1]
    id_obs = {
        "A": canonicalize_semantic_packet(f"commit {anchor_a}\nstatus SAME\n"),
        "B": canonicalize_semantic_packet(f"commit {anchor_b}\nstatus SAME\n"),
    }
    id_targets = {
        "A": base,
        "B": _fixture_target(base, checkpoint_anchor=anchor_b),
    }
    k13 = (
        id_obs["A"] == id_obs["B"]
        and core_target(id_targets["A"]) == core_target(id_targets["B"])
        and len(evaluate_collisions(id_obs, id_targets)) == 0
    )
    checks["K13"] = "PASS" if k13 else "FAIL"

    # K14 — preserve missingness / parse / incorrect distinctions.
    correct = score_reconstruction(json.dumps(base), base)
    ni_obj = dict(base)
    ni_obj["frontier_id"] = NOT_IDENTIFIED
    ni = score_reconstruction(json.dumps(ni_obj), base)
    wrong_obj = dict(base)
    wrong_obj["frontier_id"] = FIXTURE_WRONG_FRONTIER
    wrong = score_reconstruction(json.dumps(wrong_obj), base)
    bad = score_reconstruction("{not-json", base)
    ne = score_reconstruction(None, base, evaluated=False)
    k14 = (
        correct["frontier_id"] == "CORRECT"
        and ni["frontier_id"] == "NOT_IDENTIFIED"
        and wrong["frontier_id"] == "INCORRECT"
        and bad["frontier_id"] == "UNPARSEABLE"
        and ne["frontier_id"] == "NOT_EVALUATED"
    )
    checks["K14"] = "PASS" if k14 else "FAIL"

    # K15 — primary universe is exactly ten authentic checkpoints; no fixtures.
    k15 = (
        len(STATE_MANIFEST["primary_states"]) == 10
        and STATE_MANIFEST["synthetic_primary_states_allowed"] is False
        and STATE_MANIFEST["primary_state_type"] == "AUTHENTIC_REPOSITORY_CHECKPOINT"
        and CONFORMANCE_FIXTURES["fixture_type"] == "CONFORMANCE_FIXTURE"
    )
    checks["K15"] = "PASS" if k15 else "FAIL"
    return checks


def conformance_terminal_state(checks: dict[str, str]) -> str:
    required = {f"K{i}" for i in range(1, 16)}
    if set(checks) != required or any(checks[key] != "PASS" for key in required):
        return "SPECIFICATION_INVALID"
    return "CONFORMANCE_PASSED"


# No __main__ execution entry point is provided at construction time.
# The next scientific operation is a separate SpecComplete/conformance gate.
