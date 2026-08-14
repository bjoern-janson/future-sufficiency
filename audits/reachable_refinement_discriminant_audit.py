"""Reachable Refinement Discriminant Audit.

Purpose
-------
Test whether time-indexed contingent refinement reachability predicts correction
possibility beyond a static inventory of individually informative probes.

This audit introduces no new repair mechanism, no authorization change, and no
research-agency claim. The candidate object R_E remains a hypothesis until this
matched A/B/C contrast succeeds.

Matched design
--------------
Worlds are canonical triples (selector, left, right). The warranted terminal
correction is:

    action = left  if selector == 0
             right if selector == 1

Three deterministic binary probes reveal selector, left, and right respectively.
Across A/B/C the following are exactly matched:

    * world set and uniform prior
    * target correction partition
    * probe inventory and binary alphabets
    * exact per-probe world partitions
    * per-probe information
    * probe costs
    * initial probe availability
    * two-probe budget
    * commitment deadline tau = 2

Only the contingent refinement geometry differs after querying selector first:

    A: the correction-relevant branch probe remains available and returns by tau.
    B: the same branch probe remains available but returns after tau.
    C: one follow-up remains available on time, but it is the wrong branch probe.

C is degree-matched rewiring rather than simple evidence deletion.

Stage 1 exhaustively enumerates every deterministic contingent policy using at most
two probes, including early STOP, and certifies timely/eventual reachability before
any learner is introduced.

Stage 2 uses finite ERM over the same policy class under 64 anonymous probe
permutations/polarity flips. A four-world teaching set is preregistered; the other
four worlds are held out.
"""

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import product
from math import log2
import random


WORLDS = tuple(product((0, 1), repeat=3))
PROBES = (0, 1, 2)  # evaluator-only: selector, left, right
PROBE_NAMES = ("selector_probe", "left_probe", "right_probe")
PROBE_COST = 1.0
PROBE_BUDGET = 2
COMMITMENT_TAU = 2
ENCODINGS = 64

A = "A_timely_reachable"
B = "B_late_reachable"
C = "C_unreachable_rewired"
CONDITIONS = (A, B, C)

TEACHING_WORLDS = (
    (0, 0, 0),
    (0, 1, 0),
    (1, 1, 0),
    (1, 1, 1),
)
HELDOUT_WORLDS = tuple(w for w in WORLDS if w not in TEACHING_WORLDS)

assert len(WORLDS) == 8
assert len(TEACHING_WORLDS) == 4
assert len(HELDOUT_WORLDS) == 4
assert set(TEACHING_WORLDS).isdisjoint(HELDOUT_WORLDS)


def warranted_action(world):
    """Evaluator-defined terminal correction contract for this finite audit."""
    selector, left, right = world
    return left if selector == 0 else right


TARGET = tuple(warranted_action(w) for w in WORLDS)
assert Counter(TARGET) == Counter({0: 4, 1: 4})


def entropy(values):
    counts = Counter(values)
    total = len(values)
    return -sum(
        (count / total) * log2(count / total)
        for count in counts.values()
    )


def mutual_information(xs, ys):
    assert len(xs) == len(ys)
    total = len(xs)
    x_counts = Counter(xs)
    y_counts = Counter(ys)
    joint = Counter(zip(xs, ys))
    value = 0.0
    for (x, y), count in joint.items():
        pxy = count / total
        px = x_counts[x] / total
        py = y_counts[y] / total
        value += pxy * log2(pxy / (px * py))
    return value


def probe_partition(canonical_probe):
    return tuple(
        tuple(world for world in WORLDS if world[canonical_probe] == token)
        for token in (0, 1)
    )


def bayes_target_accuracy_from_visible(canonical_probes):
    groups = defaultdict(Counter)
    for world in WORLDS:
        signature = tuple(world[p] for p in canonical_probes)
        groups[signature][warranted_action(world)] += 1
    return sum(max(counts.values()) for counts in groups.values()) / len(WORLDS)


STATIC_SIGNATURE = {
    "world_count": len(WORLDS),
    "target_partition": tuple(
        tuple(world for world in WORLDS if warranted_action(world) == action)
        for action in (0, 1)
    ),
    "probe_count": len(PROBES),
    "probe_alphabets": tuple((0, 1) for _ in PROBES),
    "probe_costs": tuple(PROBE_COST for _ in PROBES),
    "initial_availability": PROBES,
    "probe_budget": PROBE_BUDGET,
    "commitment_tau": COMMITMENT_TAU,
    "probe_partitions": tuple(probe_partition(p) for p in PROBES),
    "probe_world_information_bits": tuple(
        entropy(tuple(world[p] for world in WORLDS))
        for p in PROBES
    ),
    "probe_target_information_bits": tuple(
        mutual_information(
            tuple(world[p] for world in WORLDS),
            TARGET,
        )
        for p in PROBES
    ),
    "probe_target_bayes_accuracy": tuple(
        bayes_target_accuracy_from_visible((p,))
        for p in PROBES
    ),
    "joint_static_inventory_target_bayes_accuracy": (
        bayes_target_accuracy_from_visible(PROBES)
    ),
}

assert STATIC_SIGNATURE["probe_world_information_bits"] == (1.0, 1.0, 1.0)
assert STATIC_SIGNATURE["probe_target_bayes_accuracy"] == (0.5, 0.75, 0.75)
assert STATIC_SIGNATURE["joint_static_inventory_target_bayes_accuracy"] == 1.0


@dataclass(frozen=True)
class Encoding:
    """Anonymous probe encoding: observed index -> canonical probe plus polarity."""

    observed_to_canonical: tuple
    polarity_flips: tuple

    @property
    def canonical_to_observed(self):
        return {
            canonical: observed
            for observed, canonical in enumerate(self.observed_to_canonical)
        }

    def encode_world(self, world):
        return tuple(
            world[canonical] ^ self.polarity_flips[observed]
            for observed, canonical in enumerate(self.observed_to_canonical)
        )


def make_encoding(seed):
    rng = random.Random(seed)
    order = list(PROBES)
    rng.shuffle(order)
    flips = tuple(rng.randrange(2) for _ in PROBES)
    return Encoding(tuple(order), flips)


@dataclass(frozen=True)
class BranchProgram:
    """Action after the first probe outcome."""

    kind: str  # "stop" or "probe"
    action: int = -1
    probe: int = -1
    leaf_actions: tuple = ()


@dataclass(frozen=True)
class Policy:
    """Every deterministic policy using at most two probes."""

    first_kind: str  # "stop" or "probe"
    initial_action: int = -1
    first_probe: int = -1
    branch_if_zero: BranchProgram = None
    branch_if_one: BranchProgram = None


def branch_programs(first_probe):
    remaining = tuple(p for p in PROBES if p != first_probe)
    programs = [
        BranchProgram("stop", action=0),
        BranchProgram("stop", action=1),
    ]
    for second in remaining:
        for leaves in product((0, 1), repeat=2):
            programs.append(
                BranchProgram(
                    "probe",
                    probe=second,
                    leaf_actions=tuple(leaves),
                )
            )
    return tuple(programs)


def enumerate_policies():
    policies = [
        Policy("stop", initial_action=0),
        Policy("stop", initial_action=1),
    ]
    for first in PROBES:
        branches = branch_programs(first)
        for branch_zero in branches:
            for branch_one in branches:
                policies.append(
                    Policy(
                        "probe",
                        first_probe=first,
                        branch_if_zero=branch_zero,
                        branch_if_one=branch_one,
                    )
                )
    return tuple(policies)


POLICIES = enumerate_policies()
assert len(POLICIES) == 302


def second_step_geometry(condition, encoding, world, first_observed):
    """Return allowed second probes and their latency.

    A/B/C differ only when selector was queried first. If a data probe is queried
    first, both remaining probes retain ordinary latency in every condition.
    """
    first_canonical = encoding.observed_to_canonical[first_observed]
    remaining = set(PROBES) - {first_observed}

    if first_canonical != 0:
        return frozenset(remaining), 1

    selector = world[0]
    correct_canonical = 1 if selector == 0 else 2
    wrong_canonical = 2 if selector == 0 else 1
    c2o = encoding.canonical_to_observed
    correct_observed = c2o[correct_canonical]
    wrong_observed = c2o[wrong_canonical]

    if condition == A:
        return frozenset({correct_observed}), 1
    if condition == B:
        return frozenset({correct_observed}), 2
    if condition == C:
        return frozenset({wrong_observed}), 1
    raise ValueError(condition)


def execute_policy(policy, condition, encoding, world):
    """Execute one policy and mark blocked/late refinements explicitly."""
    if policy.first_kind == "stop":
        prediction = policy.initial_action
        return {
            "valid": True,
            "completion_time": 0,
            "timely": True,
            "prediction": prediction,
            "correct": prediction == warranted_action(world),
        }

    encoded = encoding.encode_world(world)
    first = policy.first_probe
    first_outcome = encoded[first]
    branch = (
        policy.branch_if_zero
        if first_outcome == 0
        else policy.branch_if_one
    )

    if branch.kind == "stop":
        prediction = branch.action
        return {
            "valid": True,
            "completion_time": 1,
            "timely": True,
            "prediction": prediction,
            "correct": prediction == warranted_action(world),
        }

    second = branch.probe
    allowed, second_latency = second_step_geometry(
        condition, encoding, world, first
    )

    if second not in allowed:
        return {
            "valid": False,
            "completion_time": None,
            "timely": False,
            "prediction": None,
            "correct": False,
        }

    second_outcome = encoded[second]
    prediction = branch.leaf_actions[second_outcome]
    completion_time = 1 + second_latency

    return {
        "valid": True,
        "completion_time": completion_time,
        "timely": completion_time <= COMMITMENT_TAU,
        "prediction": prediction,
        "correct": prediction == warranted_action(world),
    }


def policy_accuracy(policy, condition, encoding, worlds, timely):
    correct = 0
    for world in worlds:
        result = execute_policy(policy, condition, encoding, world)
        if not result["valid"]:
            continue
        if timely and not result["timely"]:
            continue
        correct += result["correct"]
    return correct / len(worlds)


def structural_certificate(condition):
    """Exact evaluator-side closure over every admissible deterministic policy."""
    identity = Encoding(PROBES, (0, 0, 0))

    timely_scores = {
        policy: policy_accuracy(
            policy, condition, identity, WORLDS, timely=True
        )
        for policy in POLICIES
    }
    eventual_scores = {
        policy: policy_accuracy(
            policy, condition, identity, WORLDS, timely=False
        )
        for policy in POLICIES
    }

    max_timely = max(timely_scores.values())
    max_eventual = max(eventual_scores.values())
    timely_full = tuple(
        p for p, score in timely_scores.items()
        if abs(score - 1.0) < 1e-12
    )
    eventual_full = tuple(
        p for p, score in eventual_scores.items()
        if abs(score - 1.0) < 1e-12
    )

    return {
        "condition": condition,
        "policy_count": len(POLICIES),
        "reachable_before_commitment": bool(timely_full),
        "reachable_eventually": bool(eventual_full),
        "max_timely_accuracy": max_timely,
        "max_eventual_accuracy": max_eventual,
        "timely_full_policy_count": len(timely_full),
        "eventual_full_policy_count": len(eventual_full),
    }


def choose_erm_policy(condition, encoding, timely):
    """Finite ERM learner over the same anonymous policy language."""
    scored = tuple(
        (
            policy_accuracy(
                policy,
                condition,
                encoding,
                TEACHING_WORLDS,
                timely=timely,
            ),
            policy,
        )
        for policy in POLICIES
    )
    best_score = max(score for score, _ in scored)
    best = tuple(
        policy for score, policy in scored
        if abs(score - best_score) < 1e-12
    )

    chosen = min(
        best,
        key=lambda p: repr(p),
    )
    return chosen, best_score, len(best)


def learner_summary(condition, timely):
    rows = []
    for seed in range(ENCODINGS):
        encoding = make_encoding(seed)
        learned, train_accuracy, tie_count = choose_erm_policy(
            condition, encoding, timely=timely
        )
        heldout_accuracy = policy_accuracy(
            learned,
            condition,
            encoding,
            HELDOUT_WORLDS,
            timely=timely,
        )
        full_accuracy = policy_accuracy(
            learned,
            condition,
            encoding,
            WORLDS,
            timely=timely,
        )
        rows.append(
            {
                "seed": seed,
                "train_accuracy": train_accuracy,
                "tie_count": tie_count,
                "heldout_accuracy": heldout_accuracy,
                "full_accuracy": full_accuracy,
            }
        )

    return {
        "encodings": ENCODINGS,
        "min_train_accuracy": min(r["train_accuracy"] for r in rows),
        "max_train_accuracy": max(r["train_accuracy"] for r in rows),
        "min_heldout_accuracy": min(r["heldout_accuracy"] for r in rows),
        "max_heldout_accuracy": max(r["heldout_accuracy"] for r in rows),
        "min_full_accuracy": min(r["full_accuracy"] for r in rows),
        "max_full_accuracy": max(r["full_accuracy"] for r in rows),
        "tie_counts": tuple(sorted(set(r["tie_count"] for r in rows))),
    }


def matched_static_inventory_control():
    """A/B/C share the exact same static evidence signature."""
    signatures = {condition: STATIC_SIGNATURE for condition in CONDITIONS}
    assert len({repr(signature) for signature in signatures.values()}) == 1
    return {
        "matched": True,
        "signature": STATIC_SIGNATURE,
    }


def degree_match_control():
    """After selector-first, A/B/C each expose exactly one follow-up edge."""
    identity = Encoding(PROBES, (0, 0, 0))
    rows = []
    for condition in CONDITIONS:
        for selector in (0, 1):
            world = (selector, 0, 0)
            allowed, latency = second_step_geometry(
                condition, identity, world, first_observed=0
            )
            rows.append(
                {
                    "condition": condition,
                    "selector": selector,
                    "followup_count": len(allowed),
                    "latency": latency,
                    "followup_probe": tuple(sorted(allowed)),
                }
            )
    assert all(row["followup_count"] == 1 for row in rows)
    return {
        "one_followup_edge_after_selector_all_conditions": True,
        "rows": tuple(rows),
    }


def audit():
    static_control = matched_static_inventory_control()
    degree_control = degree_match_control()

    # Stage 1: evaluator-side structure first.
    structural = {
        condition: structural_certificate(condition)
        for condition in CONDITIONS
    }

    assert structural[A]["reachable_before_commitment"]
    assert structural[A]["reachable_eventually"]
    assert structural[A]["timely_full_policy_count"] == 1
    assert structural[A]["eventual_full_policy_count"] == 1

    assert not structural[B]["reachable_before_commitment"]
    assert structural[B]["reachable_eventually"]
    assert structural[B]["timely_full_policy_count"] == 0
    assert structural[B]["eventual_full_policy_count"] == 1

    assert not structural[C]["reachable_before_commitment"]
    assert not structural[C]["reachable_eventually"]
    assert structural[C]["timely_full_policy_count"] == 0
    assert structural[C]["eventual_full_policy_count"] == 0

    assert structural[A]["max_timely_accuracy"] == 1.0
    assert structural[A]["max_eventual_accuracy"] == 1.0
    assert structural[B]["max_timely_accuracy"] == 0.75
    assert structural[B]["max_eventual_accuracy"] == 1.0
    assert structural[C]["max_timely_accuracy"] == 0.75
    assert structural[C]["max_eventual_accuracy"] == 0.75

    # Stage 2: learner only after the structural certificate is fixed.
    learner = {}
    for condition in CONDITIONS:
        learner[condition] = {
            "timely_objective": learner_summary(condition, timely=True),
            "eventual_diagnostic": learner_summary(condition, timely=False),
        }

    expected = {
        A: (1.0, 1.0),
        B: (0.75, 1.0),
        C: (0.75, 0.75),
    }
    for condition, (timely_ceiling, eventual_ceiling) in expected.items():
        timely_summary = learner[condition]["timely_objective"]
        eventual_summary = learner[condition]["eventual_diagnostic"]

        assert timely_summary["min_heldout_accuracy"] == timely_ceiling
        assert timely_summary["max_heldout_accuracy"] == timely_ceiling
        assert timely_summary["min_full_accuracy"] == timely_ceiling
        assert timely_summary["max_full_accuracy"] == timely_ceiling

        assert eventual_summary["min_heldout_accuracy"] == eventual_ceiling
        assert eventual_summary["max_heldout_accuracy"] == eventual_ceiling
        assert eventual_summary["min_full_accuracy"] == eventual_ceiling
        assert eventual_summary["max_full_accuracy"] == eventual_ceiling

    return {
        "claim_status": (
            "R_E is a candidate explanatory object; this audit tests whether it "
            "predicts beyond static evidence inventory."
        ),
        "contract": {
            "new_theory_added": False,
            "only_manipulated_variable": (
                "outcome-conditional refinement accessibility/timing"
            ),
            "repair_construction": False,
            "repair_authorization": False,
            "binding": False,
            "persistence": False,
            "research_agency": False,
            "learner_enters_after_structural_certificate": True,
            "terminal_contract": "binary warranted correction only",
        },
        "static_inventory_control": static_control,
        "degree_match_control": degree_control,
        "structural_certificate": structural,
        "learner": learner,
        "earned_if_assertions_hold": (
            "In this finite deterministic audit, correction capacity depends on "
            "timely compositional reachability of admissible refinements, not merely "
            "on the static inventory of individually informative probes."
        ),
        "not_earned": (
            "general stochastic refinement dominance",
            "dynamic-programming necessity",
            "general experiment design",
            "research agency",
            "unrestricted refinement-system repair",
            "general corrigibility theorem",
        ),
    }


def print_summary(result):
    print("Reachable Refinement Discriminant Audit")
    print("=" * 41)
    print("policy_class_size:", len(POLICIES))
    print("static_inventory_matched:", result["static_inventory_control"]["matched"])
    print(
        "joint_static_inventory_target_bayes_accuracy:",
        f'{STATIC_SIGNATURE["joint_static_inventory_target_bayes_accuracy"]:.4f}',
    )
    print(
        "one_followup_edge_after_selector_all_conditions:",
        result["degree_match_control"][
            "one_followup_edge_after_selector_all_conditions"
        ],
    )
    print()

    for condition in CONDITIONS:
        row = result["structural_certificate"][condition]
        print(condition)
        print("  reachable_before_commitment:", row["reachable_before_commitment"])
        print("  reachable_eventually:", row["reachable_eventually"])
        print("  max_timely_accuracy:", f'{row["max_timely_accuracy"]:.4f}')
        print("  max_eventual_accuracy:", f'{row["max_eventual_accuracy"]:.4f}')
        print("  timely_full_policy_count:", row["timely_full_policy_count"])
        print("  eventual_full_policy_count:", row["eventual_full_policy_count"])

        timely = result["learner"][condition]["timely_objective"]
        eventual = result["learner"][condition]["eventual_diagnostic"]
        print(
            "  learner_timely_full_accuracy:",
            f'{timely["min_full_accuracy"]:.4f}',
            "to",
            f'{timely["max_full_accuracy"]:.4f}',
            "across",
            timely["encodings"],
            "encodings",
        )
        print(
            "  learner_eventual_full_accuracy:",
            f'{eventual["min_full_accuracy"]:.4f}',
            "to",
            f'{eventual["max_full_accuracy"]:.4f}',
        )
        print("  timely_erm_tie_counts:", timely["tie_counts"])
        print("  eventual_erm_tie_counts:", eventual["tie_counts"])
        print()

    print("earned_if_assertions_hold:")
    print(" ", result["earned_if_assertions_hold"])


if __name__ == "__main__":
    result = audit()
    print_summary(result)
