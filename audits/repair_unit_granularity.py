"""Repair-unit granularity audit for recursive repair discovery.

Not Experiment 009. The learner receives opaque state IDs, relational history,
and sparse repair consequences. It must infer both repair membership and repair
scope cardinality. No repair-scope size is supplied to the discovering policy.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from random import Random

N_STATES = 16
TRUE_SCOPE_SIZES = (2, 3, 4, 5)
CANDIDATE_MIN_SIZE = 1
CANDIDATE_MAX_SIZE = 6
N_ENCODINGS = 64
N_ABLATION_ENCODINGS = 16
BASE_ACCURACY = 0.875
REPAIRED_ACCURACY = 1.0
OBSERVED_GAIN = REPAIRED_ACCURACY - BASE_ACCURACY
HORIZON = 100.0
REPAIR_COST = 5.0
ENCODING_SEED = 1508

STATES = tuple(range(N_STATES))
FULL_MASK = (1 << N_STATES) - 1

# Evaluator-only latent relation components. Four are audited repair units with
# cardinalities 2,3,4,5; the final two-state component is a distractor.
LATENT_COMPONENTS = (
    frozenset((0, 1)),
    frozenset((2, 3, 4)),
    frozenset((5, 6, 7, 8)),
    frozenset((9, 10, 11, 12, 13)),
    frozenset((14, 15)),
)
TARGET_COMPONENTS = LATENT_COMPONENTS[:4]
assert tuple(len(c) for c in TARGET_COMPONENTS) == TRUE_SCOPE_SIZES


def mask_of(states) -> int:
    out = 0
    for s in states:
        out |= 1 << s
    return out


def latent_edges():
    edges = []
    for component in LATENT_COMPONENTS:
        for a, b in combinations(sorted(component), 2):
            edges.append((a, b))
    return tuple(edges)


LATENT_EDGES = latent_edges()


def permute_world(seed: int):
    rng = Random(seed)
    labels = list(STATES)
    rng.shuffle(labels)
    encode = {latent: labels[latent] for latent in STATES}
    edges = tuple((encode[a], encode[b]) for a, b in LATENT_EDGES)
    scopes = tuple(mask_of(encode[s] for s in component) for component in TARGET_COMPONENTS)
    distractor = mask_of(encode[s] for s in LATENT_COMPONENTS[-1])
    adjacency = [0] * N_STATES
    for a, b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a
    return tuple(adjacency), scopes, distractor


@dataclass(frozen=True)
class Consequence:
    state: int
    sign: int
    gain: float


@dataclass
class Meter:
    candidate_scopes: int = 0
    relation_checks: int = 0
    consequence_checks: int = 0
    history_events: int = 0
    memory_cells: int = 0
    storage_slots: int = 0

    def snapshot(self):
        return (
            self.candidate_scopes,
            self.relation_checks,
            self.consequence_checks,
            self.history_events,
            self.memory_cells,
            self.storage_slots,
        )


CANDIDATES = tuple(
    (mask_of(combo), size, combo)
    for size in range(CANDIDATE_MIN_SIZE, CANDIDATE_MAX_SIZE + 1)
    for combo in combinations(STATES, size)
)


def boundary_count(scope_mask: int, combo: tuple[int, ...], adjacency: tuple[int, ...], meter: Meter) -> int:
    boundary = 0
    outside = FULL_MASK ^ scope_mask
    for node in combo:
        meter.relation_checks += 1
        boundary += (adjacency[node] & outside).bit_count()
    return boundary


def consequence_violations(scope_mask: int, consequences: tuple[Consequence, ...], meter: Meter) -> int:
    violations = 0
    for event in consequences:
        meter.consequence_checks += 1
        inside = bool(scope_mask & (1 << event.state))
        violations += (event.sign > 0 and not inside) or (event.sign < 0 and inside)
    return int(violations)


def discover_scope(
    adjacency: tuple[int, ...],
    consequences: tuple[Consequence, ...],
    meter: Meter,
    *,
    use_history: bool = True,
    use_consequences: bool = True,
) -> int:
    edge_count = sum(x.bit_count() for x in adjacency) // 2
    meter.history_events += edge_count if use_history else 0
    meter.memory_cells = max(
        meter.memory_cells,
        (2 * edge_count if use_history else 0) + (2 * len(consequences) if use_consequences else 0),
    )
    meter.storage_slots = CANDIDATE_MAX_SIZE

    best_key = None
    best_mask = None
    for scope_mask, size, combo in CANDIDATES:
        meter.candidate_scopes += 1
        cv = consequence_violations(scope_mask, consequences, meter) if use_consequences else 0
        be = boundary_count(scope_mask, combo, adjacency, meter) if use_history else 0
        key = (cv, be, size, scope_mask)
        if best_key is None or key < best_key:
            best_key = key
            best_mask = scope_mask
    assert best_mask is not None
    return best_mask


def min_state(scope_mask: int) -> int:
    return (scope_mask & -scope_mask).bit_length() - 1


def scope_size(scope_mask: int) -> int:
    return scope_mask.bit_count()


def select_consequences(target_scope: int, all_scopes: tuple[int, ...], distractor: int):
    positive = min_state(target_scope)
    negatives = []
    for scope in all_scopes:
        if scope != target_scope:
            negatives.append(min_state(scope))
        if len(negatives) == 2:
            break
    negatives.append(min_state(distractor))
    return (
        Consequence(positive, +1, OBSERVED_GAIN),
        *(Consequence(s, -1, 0.0) for s in negatives),
    )


def shuffled_adjacency(adjacency: tuple[int, ...], seed: int):
    rng = Random(seed)
    perm = list(STATES)
    rng.shuffle(perm)
    out = [0] * N_STATES
    for a in STATES:
        for b in range(a + 1, N_STATES):
            if adjacency[a] & (1 << b):
                aa, bb = perm[a], perm[b]
                out[aa] |= 1 << bb
                out[bb] |= 1 << aa
    return tuple(out)


def bind_if_valuable(scope_mask: int | None, consequences: tuple[Consequence, ...]):
    positive_gains = [event.gain for event in consequences if event.sign > 0]
    observed = sum(positive_gains) / len(positive_gains) if positive_gains else 0.0
    value = HORIZON * observed
    return scope_mask if scope_mask is not None and value > REPAIR_COST else None, value


def evaluate_binding(bound_scope: int | None, true_scope: int) -> float:
    if bound_scope is None:
        return BASE_ACCURACY
    fn = (true_scope & ~bound_scope).bit_count()
    fp = (bound_scope & ~true_scope).bit_count()
    union = (true_scope | bound_scope).bit_count()
    penalty = (fn + fp) / union
    return BASE_ACCURACY + OBSERVED_GAIN * max(0.0, 1.0 - penalty)


def run_primary(seed: int, target_index: int):
    adjacency, scopes, distractor = permute_world(seed)
    true_scope = scopes[target_index]
    consequences = select_consequences(true_scope, scopes, distractor)

    full_meter, fixed_meter = Meter(), Meter()
    discovered = discover_scope(adjacency, consequences, full_meter)
    fixed_discovered = discover_scope(adjacency, consequences, fixed_meter)
    assert discovered == fixed_discovered

    full_bound, full_value = bind_if_valuable(discovered, consequences)
    fixed_candidate = fixed_discovered if scope_size(fixed_discovered) == 4 else None
    fixed_bound, fixed_value = bind_if_valuable(fixed_candidate, consequences)

    return {
        "true_size": scope_size(true_scope),
        "full_exact": discovered == true_scope,
        "full_size": scope_size(discovered),
        "fixed_exact": fixed_bound == true_scope,
        "full_transfer": evaluate_binding(full_bound, true_scope),
        "fixed_transfer": evaluate_binding(fixed_bound, true_scope),
        "full_value": full_value,
        "fixed_value": fixed_value,
        "full_meter": full_meter.snapshot(),
        "fixed_meter": fixed_meter.snapshot(),
    }


def run_ablations(seed: int, target_index: int):
    adjacency, scopes, distractor = permute_world(seed)
    true_scope = scopes[target_index]
    consequences = select_consequences(true_scope, scopes, distractor)
    results = {}
    for name, history, cons, adj in (
        ("outcomes_only", False, True, adjacency),
        ("history_only", True, False, adjacency),
        ("shuffled_history", True, True, shuffled_adjacency(adjacency, seed + 100_000)),
        ("opaque_ids_only", False, False, adjacency),
    ):
        meter = Meter()
        scope = discover_scope(adj, consequences, meter, use_history=history, use_consequences=cons)
        results[name] = {
            "exact": scope == true_scope,
            "transfer": evaluate_binding(scope, true_scope),
        }
    return results


def run_null(seed: int = 99991):
    adjacency, scopes, distractor = permute_world(seed)
    true_scope = scopes[2]
    consequences = list(select_consequences(true_scope, scopes, distractor))
    consequences[0] = Consequence(consequences[0].state, +1, 0.0)
    consequences = tuple(consequences)
    meter = Meter()
    discovered = discover_scope(adjacency, consequences, meter)
    bound, value = bind_if_valuable(discovered, consequences)
    assert value == 0.0 and bound is None
    return {
        "base_error": 1.0 - BASE_ACCURACY,
        "discovered_size": scope_size(discovered),
        "estimated_repair_value": value,
        "repair_triggered": bound is not None,
        "transfer": evaluate_binding(bound, true_scope),
    }


def mean(xs):
    return sum(xs) / len(xs)


def run_audit():
    primary = []
    for encoding in range(N_ENCODINGS):
        seed = ENCODING_SEED + encoding
        for target_index in range(len(TARGET_COMPONENTS)):
            primary.append(run_primary(seed, target_index))

    assert all(r["full_exact"] for r in primary)
    assert all(r["full_size"] == r["true_size"] for r in primary)
    assert all(r["full_meter"] == r["fixed_meter"] for r in primary)

    ablations = []
    for encoding in range(N_ABLATION_ENCODINGS):
        seed = ENCODING_SEED + 10_000 + encoding
        for target_index in range(len(TARGET_COMPONENTS)):
            ablations.append(run_ablations(seed, target_index))

    by_size = {}
    for size in TRUE_SCOPE_SIZES:
        subset = [r for r in primary if r["true_size"] == size]
        by_size[size] = {
            "trials": len(subset),
            "full_exact": mean([r["full_exact"] for r in subset]),
            "fixed_exact": mean([r["fixed_exact"] for r in subset]),
            "full_transfer": mean([r["full_transfer"] for r in subset]),
            "fixed_transfer": mean([r["fixed_transfer"] for r in subset]),
        }

    def ablation_mean(name, key):
        return mean([row[name][key] for row in ablations])

    return {
        "setup": {
            "encodings": N_ENCODINGS,
            "ablation_encodings": N_ABLATION_ENCODINGS,
            "true_scope_sizes": TRUE_SCOPE_SIZES,
            "candidate_scope_size_range": (CANDIDATE_MIN_SIZE, CANDIDATE_MAX_SIZE),
            "candidate_scope_count": len(CANDIDATES),
            "base_error_each_case": 1.0 - BASE_ACCURACY,
        },
        "full_vs_fixed": {
            "trials": len(primary),
            "full_exact_scope_rate": mean([r["full_exact"] for r in primary]),
            "fixed_size4_exact_scope_rate": mean([r["fixed_exact"] for r in primary]),
            "full_mean_transfer": mean([r["full_transfer"] for r in primary]),
            "fixed_mean_transfer": mean([r["fixed_transfer"] for r in primary]),
            "meters_exactly_matched": all(r["full_meter"] == r["fixed_meter"] for r in primary),
            "meter_per_trial": primary[0]["full_meter"],
        },
        "by_true_scope_size": by_size,
        "ablations": {
            "outcomes_only_exact": ablation_mean("outcomes_only", "exact"),
            "history_only_exact": ablation_mean("history_only", "exact"),
            "shuffled_history_exact": ablation_mean("shuffled_history", "exact"),
            "opaque_ids_only_exact": ablation_mean("opaque_ids_only", "exact"),
            "outcomes_only_transfer": ablation_mean("outcomes_only", "transfer"),
            "history_only_transfer": ablation_mean("history_only", "transfer"),
            "shuffled_history_transfer": ablation_mean("shuffled_history", "transfer"),
            "opaque_ids_only_transfer": ablation_mean("opaque_ids_only", "transfer"),
        },
        "killer_null": run_null(),
        "governance": {
            "goal_rule_mutated": False,
            "authority_expanded": False,
        },
    }


if __name__ == "__main__":
    for section, values in run_audit().items():
        print(f"[{section}]")
        if section == "by_true_scope_size":
            for size, row in values.items():
                print(f"size={size}: {row}")
        else:
            for key, value in values.items():
                print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")
        print()
