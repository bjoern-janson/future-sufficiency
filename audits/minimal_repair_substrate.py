"""Minimal-substrate audit for recursive repair discovery.

This is not Experiment 009. Structural states are opaque IDs. The learner can
recover a repair scope only from relations reconstructed from transition history
plus observed repair outcomes. Cross-encoding permutations and information
ablations identify which substrate is sufficient/necessary in this finite toy.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from random import Random

N_STATES = 16
SCOPE_SIZE = 4
N_ENCODINGS = 32
BASE_ACCURACY = 0.875
REPAIRED_ACCURACY = 1.0
OBSERVED_GAIN = REPAIRED_ACCURACY - BASE_ACCURACY
HORIZON = 100.0
REPAIR_COST = 5.0

STATES = tuple(range(N_STATES))
SCOPE_CANDIDATES = tuple(frozenset(c) for c in combinations(STATES, SCOPE_SIZE))


def latent_coord(state: int) -> tuple[int, int]:
    return divmod(state, 4)


def latent_edges() -> frozenset[tuple[int, int]]:
    """4x4 rook relation; semantic row/column labels are evaluator-only."""
    edges = set()
    for a, b in combinations(STATES, 2):
        ra, ca = latent_coord(a)
        rb, cb = latent_coord(b)
        if ra == rb or ca == cb:
            edges.add((a, b))
    return frozenset(edges)


LATENT_EDGES = latent_edges()
LATENT_SCOPES = tuple(
    [frozenset(4 * r + c for c in range(4)) for r in range(4)]
    + [frozenset(4 * r + c for r in range(4)) for c in range(4)]
)


@dataclass
class Meter:
    candidate_scopes: int = 0
    relation_checks: int = 0
    outcome_checks: int = 0
    history_events: int = 0
    memory_cells: int = 0
    storage_slots: int = 0

    def snapshot(self) -> tuple[int, ...]:
        return (
            self.candidate_scopes,
            self.relation_checks,
            self.outcome_checks,
            self.history_events,
            self.memory_cells,
            self.storage_slots,
        )


def encode_edges(
    edges: frozenset[tuple[int, int]], encoding: tuple[int, ...]
) -> frozenset[tuple[int, int]]:
    out = set()
    for a, b in edges:
        x, y = encoding[a], encoding[b]
        out.add((x, y) if x < y else (y, x))
    return frozenset(out)


def history_from_edges(edges: frozenset[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    """Opaque transition history: each undirected relation appears in both directions."""
    directed = []
    for a, b in sorted(edges):
        directed.append((a, b))
        directed.append((b, a))
    return tuple(directed)


def reconstruct_relation(history: tuple[tuple[int, int], ...]) -> frozenset[tuple[int, int]]:
    return frozenset((a, b) if a < b else (b, a) for a, b in history if a != b)


def choose_scope(
    *,
    positive_states: frozenset[int],
    history: tuple[tuple[int, int], ...],
    use_outcomes: bool,
    use_history: bool,
    meter: Meter,
) -> frozenset[int]:
    relation = reconstruct_relation(history) if use_history else frozenset()
    coherence_cache = {}
    if use_history:
        for scope in SCOPE_CANDIDATES:
            coherence_cache[scope] = sum(
                ((a, b) if a < b else (b, a)) in relation
                for a, b in combinations(sorted(scope), 2)
            )
    meter.history_events += len(history)
    meter.memory_cells = max(meter.memory_cells, len(history) * 2 + len(positive_states))
    meter.storage_slots = SCOPE_SIZE

    best_key = None
    best_scope = None
    for scope in SCOPE_CANDIDATES:
        meter.candidate_scopes += 1
        coverage = 0
        for state in positive_states:
            meter.outcome_checks += 1
            coverage += int(use_outcomes and state in scope)

        meter.relation_checks += 6
        coherence = coherence_cache.get(scope, 0)

        # No semantic axis vocabulary: all size-4 subsets are candidates.
        # Outcomes constrain membership; relational coherence resolves the latent abstraction.
        key = (coverage, coherence, tuple(-x for x in sorted(scope)))
        if best_key is None or key > best_key:
            best_key = key
            best_scope = scope

    assert best_scope is not None
    return best_scope


def decision_value(observed_gains: tuple[float, ...]) -> float:
    if not observed_gains:
        return 0.0
    return HORIZON * max(0.0, sum(observed_gains) / len(observed_gains))


def evaluate_condition(
    *,
    true_scope: frozenset[int],
    holdout: int,
    encoding: tuple[int, ...],
    history_encoding: tuple[int, ...],
    use_outcomes: bool,
    use_history: bool,
) -> dict[str, object]:
    observed_scope = frozenset(encoding[s] for s in true_scope)
    holdout_observed = encoding[holdout]
    positives = frozenset(encoding[s] for s in true_scope if s != holdout)

    observed_edges = encode_edges(LATENT_EDGES, history_encoding)
    history = history_from_edges(observed_edges)
    meter = Meter()
    selected = choose_scope(
        positive_states=positives,
        history=history,
        use_outcomes=use_outcomes,
        use_history=use_history,
        meter=meter,
    )

    gains = tuple(OBSERVED_GAIN for _ in positives) if use_outcomes else tuple()
    value = decision_value(gains)
    bind = value > REPAIR_COST
    transfer = REPAIRED_ACCURACY if bind and holdout_observed in selected else BASE_ACCURACY
    return {
        "exact_scope": selected == observed_scope,
        "heldout_in_scope": holdout_observed in selected,
        "transfer": transfer,
        "repair_value": value,
        "repair_bound": bind,
        "meter": meter.snapshot(),
    }


def run_cross_encoding_audit() -> dict[str, object]:
    totals = {
        name: {"exact": 0, "heldout": 0, "transfer": 0.0}
        for name in (
            "full",
            "outcomes_only",
            "history_only",
            "shuffled_history",
            "opaque_ids_only",
        )
    }
    matched_meter = None
    total = 0

    for seed in range(N_ENCODINGS):
        rng = Random(20260814 + seed)
        encoding_list = list(STATES)
        rng.shuffle(encoding_list)
        encoding = tuple(encoding_list)

        shuffled_list = list(STATES)
        rng.shuffle(shuffled_list)
        shuffled_history_encoding = tuple(shuffled_list)

        for true_scope in LATENT_SCOPES:
            for holdout in sorted(true_scope):
                total += 1
                configs = {
                    "full": (encoding, True, True),
                    "outcomes_only": (encoding, True, False),
                    "history_only": (encoding, False, True),
                    "shuffled_history": (shuffled_history_encoding, True, True),
                    "opaque_ids_only": (encoding, False, False),
                }
                results = {}
                for name, (hist_enc, use_outcomes, use_history) in configs.items():
                    result = evaluate_condition(
                        true_scope=true_scope,
                        holdout=holdout,
                        encoding=encoding,
                        history_encoding=hist_enc,
                        use_outcomes=use_outcomes,
                        use_history=use_history,
                    )
                    results[name] = result
                    totals[name]["exact"] += int(result["exact_scope"])
                    totals[name]["heldout"] += int(result["heldout_in_scope"])
                    totals[name]["transfer"] += float(result["transfer"])

                # True-vs-shuffled relational histories have identical information volume
                # and execute exactly the same search path.
                assert results["full"]["meter"] == results["shuffled_history"]["meter"]
                if matched_meter is None:
                    matched_meter = results["full"]["meter"]
                else:
                    assert matched_meter == results["full"]["meter"]

    summary = {}
    for name, values in totals.items():
        summary[name] = {
            "exact_scope_recovery": values["exact"] / total,
            "heldout_scope_recovery": values["heldout"] / total,
            "mean_heldout_accuracy": values["transfer"] / total,
        }

    assert total == N_ENCODINGS * len(LATENT_SCOPES) * SCOPE_SIZE == 1024
    assert summary["full"] == {
        "exact_scope_recovery": 1.0,
        "heldout_scope_recovery": 1.0,
        "mean_heldout_accuracy": 1.0,
    }
    assert summary["outcomes_only"]["exact_scope_recovery"] < 0.10
    assert summary["history_only"]["exact_scope_recovery"] == 0.125
    assert summary["shuffled_history"]["exact_scope_recovery"] < 0.10

    return {
        "encodings": N_ENCODINGS,
        "latent_repair_classes": len(LATENT_SCOPES),
        "heldout_choices_per_class": SCOPE_SIZE,
        "trials": total,
        "conditions": summary,
        "matched_true_vs_shuffled_meter_per_trial": matched_meter,
    }


def run_null_audit() -> dict[str, object]:
    """High residual error, but observed repair gain is zero: no mutation."""
    rng = Random(717)
    encoding_list = list(STATES)
    rng.shuffle(encoding_list)
    encoding = tuple(encoding_list)
    history = history_from_edges(encode_edges(LATENT_EDGES, encoding))
    arbitrary_probes = frozenset(encoding[s] for s in (0, 1, 2))
    meter = Meter()
    selected = choose_scope(
        positive_states=arbitrary_probes,
        history=history,
        use_outcomes=True,
        use_history=True,
        meter=meter,
    )
    _ = selected
    observed_gains = (0.0, 0.0, 0.0)
    value = decision_value(observed_gains)
    bind = value > REPAIR_COST
    residual_error = 0.125
    assert residual_error > 0 and value == 0.0 and not bind
    return {
        "residual_error": residual_error,
        "estimated_repair_value": value,
        "repair_cost": REPAIR_COST,
        "repair_bound": bind,
        "heldout_accuracy": BASE_ACCURACY,
        "meter": meter.snapshot(),
    }


def run_audit() -> dict[str, object]:
    assert len(LATENT_EDGES) == 48
    assert len(LATENT_SCOPES) == 8
    assert len(SCOPE_CANDIDATES) == 1820
    cross = run_cross_encoding_audit()
    null = run_null_audit()
    return {
        "substrate": {
            "opaque_states": N_STATES,
            "transition_relations": len(LATENT_EDGES),
            "candidate_repair_scopes": len(SCOPE_CANDIDATES),
            "named_descriptor_features": 0,
            "named_repair_axes": 0,
        },
        "cross_encoding_and_ablations": cross,
        "killer_null": null,
        "governance": {
            "goal_rule_mutated": False,
            "authority_expanded": False,
        },
    }


if __name__ == "__main__":
    report = run_audit()
    for section, values in report.items():
        print(f"[{section}]")
        print(values)
        print()
