"""Hypothesis-Language Insufficiency Audit.

Tests whether a corrigible adaptive loop distinguishes:
- unresolved uncertainty inside an adequate hypothesis language -> DISCRIMINATE
- structured evidence no current hypothesis can represent, with positive reopen value -> REOPEN
- adequate / irreducible / zero-value cases -> STOP

The D/R/S meta-action is chosen before extension construction.

Standard library only; deterministic except for fixed-seed encoding permutations.
"""

from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from random import Random

D, R, S = "D", "R", "S"
N_STATE = 24
LOCAL = tuple(range(0, 8))
CHALLENGE = tuple(range(8, 16))
TRANSFER = tuple(range(16, 24))
ENCODINGS = 64

REOPEN_HORIZON = 50.0
REOPEN_COST = 5.0
BIND_HORIZON = 50.0
BIND_COST = 5.0


def bitmask(states):
    out = 0
    for state in states:
        out |= 1 << state
    return out


def predict(table, state):
    return (table >> state) & 1


# H0 is deliberately inadequate for one case but adequate for another.
# Both H0 hypotheses are identical on LOCAL, so the incumbent h0 is not
# privileged by the ordinary evidence.
H0 = {
    "h0": bitmask([]),
    "h1": bitmask((8, 9, 16, 17)),
}

# Extension candidates are unavailable to the meta-diagnosis. They are
# searched only after the meta-action has already been set to REOPEN.
EXT = {
    "g": bitmask((10, 11, 18, 19)),
    "g2": bitmask((12, 13, 20, 21)),
    "g3": bitmask((14, 15, 22, 23)),
}


def observations(table, states, reps=1):
    return tuple(
        (state, predict(table, state))
        for state in states
        for _ in range(reps)
    )


LOCAL_OBS = observations(H0["h0"], LOCAL)

# D: same incumbent challenge error as R, but h1 already in H0 is exact.
D_CHALLENGE = observations(H0["h1"], CHALLENGE, reps=2)

# R: same incumbent challenge error, but no member of H0 is exact.
R_CHALLENGE = observations(EXT["g"], CHALLENGE, reps=2)

# S adequate: incumbent itself is exact.
ADEQUATE_CHALLENGE = observations(H0["h0"], CHALLENGE, reps=2)

# S noise: same incumbent challenge error (.25), but repeated observations
# contradict each other for four states, so no deterministic hypothesis can
# remove the residual under this audit contract.
NOISE_CHALLENGE = tuple(
    obs
    for i, state in enumerate(CHALLENGE)
    for obs in (
        ((state, 0), (state, 1))
        if i < 4
        else ((state, 0), (state, 0))
    )
)


@dataclass
class Meter:
    probes: int = 0
    h0_evals: int = 0
    contradiction_checks: int = 0
    extension_evals: int = 0
    executions: int = 0
    memory_cells: int = 0
    storage_slots: int = 0

    def diagnostic_snapshot(self):
        return (
            self.probes,
            self.h0_evals,
            self.contradiction_checks,
            self.executions,
            self.memory_cells,
            self.storage_slots,
        )


def remap_table(table, permutation):
    out = 0
    for state in range(N_STATE):
        if predict(table, state):
            out |= 1 << permutation[state]
    return out


def remap_obs(obs, permutation):
    return tuple((permutation[state], label) for state, label in obs)


def accuracy(table, obs, meter=None, kind=None):
    if meter is not None:
        if kind == "h0":
            meter.h0_evals += len(obs)
        elif kind == "extension":
            meter.extension_evals += len(obs)
        meter.executions += len(obs)
    return sum(predict(table, state) == label for state, label in obs) / len(obs)


def contradictory(obs, meter):
    by_state = defaultdict(set)
    for state, label in obs:
        by_state[state].add(label)
        meter.contradiction_checks += 1
    return any(len(labels) > 1 for labels in by_state.values())


def diagnose(incumbent, h0_items, local_obs, challenge_obs, reopen_multiplier, meter):
    """Return D/R/S before any extension candidate is inspected."""
    meter.probes = len(local_obs) + len(challenge_obs)
    meter.memory_cells = 2 * meter.probes + 2 * len(h0_items)
    meter.storage_slots = len(h0_items) + len(EXT)

    local_consistent = []
    for name, table in h0_items:
        if accuracy(table, local_obs, meter, "h0") == 1.0:
            local_consistent.append((name, table))

    challenge_scores = []
    for name, table in local_consistent:
        challenge_scores.append(
            (accuracy(table, challenge_obs, meter, "h0"), name, table)
        )

    current_table = dict(h0_items)[incumbent]
    current_acc = accuracy(current_table, challenge_obs)
    best_h0_acc = max(score for score, _, _ in challenge_scores)
    has_contradiction = contradictory(challenge_obs, meter)

    exact_existing = [
        (name, table)
        for score, name, table in challenge_scores
        if score == 1.0
    ]

    language_insufficiency_detected = (
        not exact_existing and not has_contradiction
    )

    # Current language already explains the challenge with the incumbent.
    if current_acc == 1.0:
        return S, {
            "reason": "current_language_adequate",
            "current_acc": current_acc,
            "best_h0_acc": best_h0_acc,
            "language_insufficiency_detected": False,
            "voi_reopen": 0.0,
        }

    # Residual is resolvable by discriminating among hypotheses already in H0.
    if exact_existing:
        return D, {
            "reason": "resolvable_within_H0",
            "current_acc": current_acc,
            "best_h0_acc": best_h0_acc,
            "language_insufficiency_detected": False,
            "voi_reopen": 0.0,
        }

    # Contradictory repeated labels identify an irreducible residual under the
    # deterministic hypothesis contract; adding deterministic hypotheses cannot
    # repair it.
    if has_contradiction:
        return S, {
            "reason": "irreducible_under_deterministic_contract",
            "current_acc": current_acc,
            "best_h0_acc": best_h0_acc,
            "language_insufficiency_detected": False,
            "voi_reopen": 0.0,
        }

    # At this point H0 has been exhausted and the challenge is deterministic.
    # Use an optimistic value bound before constructing any extension.
    gain_upper = 1.0 - best_h0_acc
    voi_reopen = REOPEN_HORIZON * gain_upper * reopen_multiplier

    if language_insufficiency_detected and voi_reopen > REOPEN_COST:
        return R, {
            "reason": "H0_exhausted_structured_positive_reopen_value",
            "current_acc": current_acc,
            "best_h0_acc": best_h0_acc,
            "language_insufficiency_detected": True,
            "voi_reopen": voi_reopen,
        }

    return S, {
        "reason": "H0_exhausted_but_reopen_value_nonpositive",
        "current_acc": current_acc,
        "best_h0_acc": best_h0_acc,
        "language_insufficiency_detected": language_insufficiency_detected,
        "voi_reopen": voi_reopen,
    }


def search_extension(extension_items, challenge_obs, meter):
    scored = []
    for name, table in extension_items:
        scored.append(
            (
                accuracy(table, challenge_obs, meter, "extension"),
                name,
                table,
            )
        )
    return max(scored, key=lambda row: (row[0], row[1]))


def best_existing(h0_items, obs):
    scored = [(accuracy(table, obs), name, table) for name, table in h0_items]
    return max(scored, key=lambda row: (row[0], row[1]))


CASES = {
    "D_resolvable": {
        "challenge": D_CHALLENGE,
        "transfer": observations(H0["h1"], TRANSFER),
        "expected": D,
        "reopen_multiplier": 1.0,
        "bind_multiplier": 1.0,
    },
    "R_unrepresentable": {
        "challenge": R_CHALLENGE,
        "transfer": observations(EXT["g"], TRANSFER),
        "expected": R,
        "reopen_multiplier": 1.0,
        "bind_multiplier": 1.0,
    },
    "S_zero_reopen_value": {
        "challenge": R_CHALLENGE,
        "transfer": observations(EXT["g"], TRANSFER),
        "expected": S,
        "reopen_multiplier": 0.0,
        "bind_multiplier": 1.0,
    },
    "S_irreducible": {
        "challenge": NOISE_CHALLENGE,
        "transfer": observations(H0["h0"], TRANSFER),
        "expected": S,
        "reopen_multiplier": 1.0,
        "bind_multiplier": 1.0,
    },
    "S_adequate": {
        "challenge": ADEQUATE_CHALLENGE,
        "transfer": observations(H0["h0"], TRANSFER),
        "expected": S,
        "reopen_multiplier": 1.0,
        "bind_multiplier": 1.0,
    },
    # Governance control: reopening/search can be warranted while persistence
    # is not. This separates meta-action/extension discovery from authorization.
    "R_discover_no_bind": {
        "challenge": R_CHALLENGE,
        "transfer": observations(EXT["g"], TRANSFER),
        "expected": R,
        "reopen_multiplier": 1.0,
        "bind_multiplier": 0.0,
    },
}


def run_case(case_name, encoding_seed):
    case = CASES[case_name]
    rng = Random(271828 + encoding_seed)

    permutation = list(range(N_STATE))
    rng.shuffle(permutation)

    h0_items = [
        (name, remap_table(table, permutation))
        for name, table in H0.items()
    ]
    extension_items = [
        (name, remap_table(table, permutation))
        for name, table in EXT.items()
    ]
    rng.shuffle(h0_items)
    rng.shuffle(extension_items)

    local_obs = remap_obs(LOCAL_OBS, permutation)
    challenge_obs = remap_obs(case["challenge"], permutation)
    transfer_obs = remap_obs(case["transfer"], permutation)

    meter = Meter()
    action, diagnosis = diagnose(
        "h0",
        h0_items,
        local_obs,
        challenge_obs,
        case["reopen_multiplier"],
        meter,
    )

    # This is the audit's key sequencing invariant.
    assert meter.extension_evals == 0
    diagnostic_meter = meter.diagnostic_snapshot()

    selected_name = "h0"
    selected_table = dict(h0_items)["h0"]
    extension_found = None
    extension_acc = None
    authorized = False
    bound = False
    transfer_gain = 0.0
    bind_voi = 0.0
    post_bind_action = None

    if action == D:
        score, selected_name, selected_table = best_existing(h0_items, challenge_obs)
        assert score == 1.0

    elif action == R:
        extension_acc, extension_found, extension_table = search_extension(
            extension_items, challenge_obs, meter
        )
        assert extension_acc == 1.0

        best_h0_transfer, _, _ = best_existing(h0_items, transfer_obs)
        extension_transfer = accuracy(extension_table, transfer_obs)
        transfer_gain = extension_transfer - best_h0_transfer
        bind_voi = (
            BIND_HORIZON
            * max(0.0, transfer_gain)
            * case["bind_multiplier"]
        )
        authorized = bind_voi > BIND_COST
        bound = authorized

        if bound:
            selected_name = extension_found
            selected_table = extension_table

            # After a successful bind, the now-expanded language is tested for
            # termination rather than rewarded for further expansion.
            expanded = h0_items + [(extension_found, extension_table)]
            stop_meter = Meter()
            post_bind_action, _ = diagnose(
                extension_found,
                expanded,
                challenge_obs,
                transfer_obs,
                1.0,
                stop_meter,
            )

    selected_transfer_acc = accuracy(selected_table, transfer_obs)

    return {
        "case": case_name,
        "expected_action": case["expected"],
        "action": action,
        "diagnosis": diagnosis,
        "diagnostic_meter": diagnostic_meter,
        "extension_found": extension_found,
        "extension_acc": extension_acc,
        "authorized": authorized,
        "bound": bound,
        "transfer_gain": transfer_gain,
        "bind_voi": bind_voi,
        "selected_name": selected_name,
        "selected_transfer_acc": selected_transfer_acc,
        "post_bind_action": post_bind_action,
        "full_meter": asdict(meter),
    }


def error_trigger_baseline(case_name):
    """Degenerate policy: reopen whenever incumbent challenge error > 0."""
    challenge = CASES[case_name]["challenge"]
    incumbent_error = 1.0 - accuracy(H0["h0"], challenge)
    return R if incumbent_error > 0 else S


def never_reopen_baseline(case_name):
    """Closed-world policy: discriminate if H0 can fit, otherwise stop."""
    challenge = CASES[case_name]["challenge"]
    current_acc = accuracy(H0["h0"], challenge)
    if current_acc == 1.0:
        return S
    if any(accuracy(table, challenge) == 1.0 for table in H0.values()):
        return D
    return S


def audit():
    confusion = {D: Counter(), R: Counter(), S: Counter()}
    diagnostic_meter = None
    case_summaries = {}
    false_reopen = 0
    false_closure = 0
    nontermination = 0

    for seed in range(ENCODINGS):
        for case_name, case in CASES.items():
            result = run_case(case_name, seed)
            expected = case["expected"]
            observed = result["action"]
            confusion[expected][observed] += 1

            if diagnostic_meter is None:
                diagnostic_meter = result["diagnostic_meter"]
            assert result["diagnostic_meter"] == diagnostic_meter

            if expected != R and observed == R:
                false_reopen += 1
            if expected == R and observed != R:
                false_closure += 1

            if case_name == "R_unrepresentable":
                assert observed == R
                assert result["diagnosis"]["current_acc"] == 0.75
                assert result["diagnosis"]["best_h0_acc"] == 0.75
                assert result["diagnosis"]["language_insufficiency_detected"]
                assert result["diagnosis"]["voi_reopen"] == 12.5
                assert result["extension_found"] == "g"
                assert result["authorized"] and result["bound"]
                assert result["selected_transfer_acc"] == 1.0
                assert result["transfer_gain"] == 0.25
                assert result["bind_voi"] == 12.5
                assert result["post_bind_action"] == S
                nontermination += result["post_bind_action"] != S

            elif case_name == "D_resolvable":
                assert observed == D
                assert result["diagnosis"]["current_acc"] == 0.75
                assert result["diagnosis"]["best_h0_acc"] == 1.0
                assert not result["diagnosis"]["language_insufficiency_detected"]
                assert result["extension_found"] is None
                assert result["selected_name"] == "h1"
                assert result["selected_transfer_acc"] == 1.0

            elif case_name == "S_zero_reopen_value":
                assert observed == S
                assert result["diagnosis"]["current_acc"] == 0.75
                assert result["diagnosis"]["best_h0_acc"] == 0.75
                assert result["diagnosis"]["language_insufficiency_detected"]
                assert result["diagnosis"]["voi_reopen"] == 0.0
                assert result["extension_found"] is None
                assert not result["authorized"] and not result["bound"]

            elif case_name == "S_irreducible":
                assert observed == S
                assert result["diagnosis"]["current_acc"] == 0.75
                assert result["diagnosis"]["best_h0_acc"] == 0.75
                assert not result["diagnosis"]["language_insufficiency_detected"]
                assert result["extension_found"] is None

            elif case_name == "S_adequate":
                assert observed == S
                assert result["diagnosis"]["current_acc"] == 1.0
                assert result["extension_found"] is None

            elif case_name == "R_discover_no_bind":
                assert observed == R
                assert result["extension_found"] == "g"
                assert result["transfer_gain"] == 0.25
                assert result["bind_voi"] == 0.0
                assert not result["authorized"] and not result["bound"]
                assert result["selected_name"] == "h0"

            if seed == 0:
                case_summaries[case_name] = result

    total_r = ENCODINGS * sum(
        case["expected"] == R for case in CASES.values()
    )
    total_non_r = ENCODINGS * sum(
        case["expected"] != R for case in CASES.values()
    )

    error_trigger = {
        name: error_trigger_baseline(name)
        for name in CASES
    }
    never_reopen = {
        name: never_reopen_baseline(name)
        for name in CASES
    }

    return {
        "design": {
            "encodings": ENCODINGS,
            "actions": (D, R, S),
            "cases": tuple(CASES),
            "diagnosis_precedes_extension_search": True,
            "matched_diagnostic_meter": diagnostic_meter,
        },
        "matched_surface": {
            "D_current_error": 1.0 - accuracy(H0["h0"], D_CHALLENGE),
            "R_current_error": 1.0 - accuracy(H0["h0"], R_CHALLENGE),
            "S_zero_value_current_error": 1.0 - accuracy(H0["h0"], R_CHALLENGE),
            "S_irreducible_current_error": 1.0 - accuracy(H0["h0"], NOISE_CHALLENGE),
            "ordinary_local_H0_fit": 1.0,
        },
        "primary": {
            "confusion": {
                expected: dict(counts)
                for expected, counts in confusion.items()
            },
            "P_R_given_open_world_positive_challenge": 1.0 - false_closure / total_r,
            "P_R_given_non_R_contract": false_reopen / total_non_r,
            "P_R_given_zero_reopen_value": 0.0,
            "post_bind_nontermination_rate": nontermination / ENCODINGS,
        },
        "governance": {
            "discover_no_bind_case": {
                "action": case_summaries["R_discover_no_bind"]["action"],
                "extension_found": case_summaries["R_discover_no_bind"]["extension_found"],
                "authorized": case_summaries["R_discover_no_bind"]["authorized"],
                "bound": case_summaries["R_discover_no_bind"]["bound"],
                "bind_voi": case_summaries["R_discover_no_bind"]["bind_voi"],
            },
            "goal_rule_mutated": False,
            "authority_expanded": False,
        },
        "baselines": {
            "error_trigger": error_trigger,
            "never_reopen": never_reopen,
        },
        "case_examples_seed0": {
            name: {
                "expected": result["expected_action"],
                "observed": result["action"],
                "reason": result["diagnosis"]["reason"],
                "current_acc": result["diagnosis"]["current_acc"],
                "best_h0_acc": result["diagnosis"]["best_h0_acc"],
                "language_insufficiency_detected": result["diagnosis"]["language_insufficiency_detected"],
                "voi_reopen": result["diagnosis"]["voi_reopen"],
                "extension_found": result["extension_found"],
                "authorized": result["authorized"],
                "bound": result["bound"],
                "selected_transfer_acc": result["selected_transfer_acc"],
                "post_bind_action": result["post_bind_action"],
            }
            for name, result in case_summaries.items()
        },
        "boundary": {
            "finite_hypothesis_spaces": True,
            "deterministic_extension_language_supplied": True,
            "independent_challenge_channel_supplied": True,
            "reopen_value_multiplier_supplied": True,
            "general_model_misspecification_detection": False,
        },
    }


if __name__ == "__main__":
    for section, value in audit().items():
        print(f"[{section}]")
        print(value)
        print()
