"""Representation ontology selection audit.

Not Experiment 009. The learner receives a common finite event universe and
repair-consequence probes. Candidate repair objects come from heterogeneous
ontology families, but no task is labeled with the correct ontology. The audit
tests whether future value selects the object type as well as the object.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product

N_ITEMS = 16
N_HOLDOUT = 4
N_PROBES = N_ITEMS - N_HOLDOUT
BASE_ACCURACY = 0.875
REPAIR_GAIN = 0.125
HORIZON = 100.0
REPAIR_COST = 5.0
STORAGE_SLOTS = 16

ITEMS = tuple(range(N_ITEMS))
PAIRS = tuple((i // 4, i % 4) for i in ITEMS)
BITS = tuple(tuple((i >> k) & 1 for k in range(3, -1, -1)) for i in ITEMS)


@dataclass(frozen=True)
class Candidate:
    mask: frozenset[int]
    families: tuple[str, ...]
    description: str

    def predicts(self, item: int) -> int:
        return int(item in self.mask)


@dataclass
class Meter:
    probes: int = 0
    candidate_evaluations: int = 0
    executions: int = 0
    memory_cells: int = 0
    storage_slots: int = 0

    def snapshot(self) -> tuple[int, int, int, int, int]:
        return (
            self.probes,
            self.candidate_evaluations,
            self.executions,
            self.memory_cells,
            self.storage_slots,
        )


def set_partitions(seq):
    if not seq:
        yield ()
        return
    first = seq[0]
    for part in set_partitions(seq[1:]):
        yield ((first,),) + part
        for j in range(len(part)):
            blocks = [tuple(block) for block in part]
            blocks[j] = tuple(sorted((first,) + blocks[j]))
            yield tuple(blocks)


def family_objects() -> dict[str, dict[str, frozenset[int]]]:
    families: dict[str, dict[str, frozenset[int]]] = {}

    subset: dict[str, frozenset[int]] = {}
    for length in range(2, 6):
        for start in range(N_ITEMS):
            scope = frozenset((start + offset) % N_ITEMS for offset in range(length))
            subset[f"interval(start={start},len={length})"] = scope
    families["state_subset"] = subset

    relation: dict[str, frozenset[int]] = {}
    for d in range(4):
        relation[f"delta_mod4={d}"] = frozenset(
            i for i, (u, v) in enumerate(PAIRS) if (v - u) % 4 == d
        )
        relation[f"sum_mod4={d}"] = frozenset(
            i for i, (u, v) in enumerate(PAIRS) if (u + v) % 4 == d
        )
    relation["neq"] = frozenset(i for i, (u, v) in enumerate(PAIRS) if u != v)
    relation["lt"] = frozenset(i for i, (u, v) in enumerate(PAIRS) if u < v)
    relation["gt"] = frozenset(i for i, (u, v) in enumerate(PAIRS) if u > v)
    relation["eq"] = frozenset(i for i, (u, v) in enumerate(PAIRS) if u == v)
    families["edge_relation"] = relation

    canonical_partitions = set()
    for raw in set_partitions((0, 1, 2, 3)):
        blocks = tuple(sorted(tuple(sorted(block)) for block in raw))
        canonical_partitions.add(blocks)
    partition: dict[str, frozenset[int]] = {}
    for blocks in sorted(canonical_partitions):
        scope = frozenset(
            i
            for i, (u, v) in enumerate(PAIRS)
            if any(u in block and v in block for block in blocks)
        )
        partition[f"blocks={blocks}"] = scope
    families["partition"] = partition

    predicate: dict[str, frozenset[int]] = {}
    literals = tuple((bit_index, bit_value) for bit_index in range(4) for bit_value in (0, 1))
    for left, right in combinations(literals, 2):
        if left[0] == right[0]:
            continue
        scope = frozenset(
            i
            for i, values in enumerate(BITS)
            if values[left[0]] == left[1] and values[right[0]] == right[1]
        )
        predicate[f"b{left[0]}={left[1]}&b{right[0]}={right[1]}"] = scope
    families["predicate"] = predicate

    operator: dict[str, frozenset[int]] = {}
    for perm in permutations(range(4)):
        scope = frozenset(i for i, (u, v) in enumerate(PAIRS) if v == perm[u])
        operator[f"perm={perm}"] = scope
    families["operator"] = operator

    temporal: dict[str, frozenset[int]] = {}
    for length in (2, 3):
        for motif in product((0, 1), repeat=length):
            scope = frozenset(
                i
                for i, values in enumerate(BITS)
                if any(
                    tuple(values[start : start + length]) == motif
                    for start in range(5 - length)
                )
            )
            temporal[f"contains={motif}"] = scope
    families["temporal_motif"] = temporal

    return families


FAMILY_OBJECTS = family_objects()


def semantic_candidates() -> tuple[Candidate, ...]:
    by_mask: dict[frozenset[int], list[tuple[str, str]]] = {}
    for family, objects in FAMILY_OBJECTS.items():
        for description, scope in objects.items():
            by_mask.setdefault(scope, []).append((family, description))

    result = []
    for scope, entries in by_mask.items():
        entries = sorted(entries)
        families = tuple(sorted({family for family, _ in entries}))
        description = " | ".join(f"{family}:{desc}" for family, desc in entries)
        result.append(Candidate(scope, families, description))
    return tuple(sorted(result, key=lambda c: (len(c.mask), tuple(sorted(c.mask)), c.families, c.description)))


CANDIDATES = semantic_candidates()
assert len(CANDIDATES) == 137


def unique_family_candidates(family: str) -> tuple[Candidate, ...]:
    return tuple(c for c in CANDIDATES if c.families == (family,))


def choose_hidden_case(family: str) -> tuple[Candidate, tuple[int, ...]]:
    """Choose first family-unique object with a holdout leaving unique identification."""
    for hidden in unique_family_candidates(family):
        for holdout in combinations(ITEMS, N_HOLDOUT):
            holdout_set = frozenset(holdout)
            if not (hidden.mask & holdout_set):
                continue
            if not (hidden.mask - holdout_set):
                continue
            observed = tuple(item for item in ITEMS if item not in holdout_set)
            labels = {item: hidden.predicts(item) for item in observed}
            matches = [
                candidate
                for candidate in CANDIDATES
                if all(candidate.predicts(item) == labels[item] for item in observed)
            ]
            if len(matches) == 1 and matches[0].mask == hidden.mask:
                return hidden, tuple(holdout)
    raise RuntimeError(f"no identifiable hidden case for {family}")


ONTOLOGY_FAMILIES = tuple(FAMILY_OBJECTS)
HIDDEN_CASES = {family: choose_hidden_case(family) for family in ONTOLOGY_FAMILIES}


def score_candidate(candidate: Candidate, observed_items: tuple[int, ...], true_mask: frozenset[int], meter: Meter) -> float:
    meter.candidate_evaluations += 1
    correct = 0
    for item in observed_items:
        meter.executions += 1
        correct += candidate.predicts(item) == int(item in true_mask)
    return correct / len(observed_items)


def inspect_all(observed_items: tuple[int, ...], true_mask: frozenset[int], meter: Meter):
    scored = []
    for candidate in CANDIDATES:
        accuracy = score_candidate(candidate, observed_items, true_mask, meter)
        scored.append((accuracy, candidate))
    return scored


def choose_best(scored, allowed_family: str | None):
    eligible = []
    for accuracy, candidate in scored:
        if allowed_family is not None and allowed_family not in candidate.families:
            continue
        eligible.append((accuracy, -len(candidate.mask), tuple(-i for i in sorted(candidate.mask)), candidate.description, candidate))
    if not eligible:
        return None, 0.0
    best = max(eligible, key=lambda x: x[:4])
    return best[4], best[0]


def repair_value(candidate: Candidate | None, observed_items: tuple[int, ...], true_mask: frozenset[int]) -> float:
    if candidate is None:
        return 0.0
    gains = [
        REPAIR_GAIN if item in true_mask else 0.0
        for item in observed_items
        if item in candidate.mask
    ]
    if not gains:
        return 0.0
    return HORIZON * (sum(gains) / len(gains))


def heldout_pattern_accuracy(candidate: Candidate | None, holdout: tuple[int, ...], true_mask: frozenset[int], meter: Meter) -> float:
    # Both branches perform the same evaluator-side counterfactual scoring.
    for counterfactual in CANDIDATES:
        meter.candidate_evaluations += 1
        for item in holdout:
            meter.executions += 1
            _ = counterfactual.predicts(item) == int(item in true_mask)

    correct = 0
    for item in holdout:
        prediction = 0 if candidate is None else candidate.predicts(item)
        correct += prediction == int(item in true_mask)
    return correct / len(holdout)


def future_score(pattern_accuracy: float, positive_value_exists: bool) -> float:
    if not positive_value_exists:
        return BASE_ACCURACY
    return BASE_ACCURACY + REPAIR_GAIN * pattern_accuracy


def run_case(family: str):
    hidden, holdout = HIDDEN_CASES[family]
    observed = tuple(item for item in ITEMS if item not in holdout)

    mutable_meter = Meter(
        probes=len(observed),
        memory_cells=len(observed) * 2,
        storage_slots=STORAGE_SLOTS,
    )
    fixed_meter = Meter(
        probes=len(observed),
        memory_cells=len(observed) * 2,
        storage_slots=STORAGE_SLOTS,
    )

    mutable_scored = inspect_all(observed, hidden.mask, mutable_meter)
    fixed_scored = inspect_all(observed, hidden.mask, fixed_meter)
    assert [(a, c.mask) for a, c in mutable_scored] == [(a, c.mask) for a, c in fixed_scored]

    discovered, discovered_fit = choose_best(mutable_scored, allowed_family=None)
    fixed, fixed_fit = choose_best(fixed_scored, allowed_family="state_subset")
    assert discovered is not None
    assert discovered_fit == 1.0
    assert discovered.mask == hidden.mask
    assert discovered.families == (family,)

    discovered_value = repair_value(discovered, observed, hidden.mask)
    fixed_value = repair_value(fixed, observed, hidden.mask)
    discovered_bound = discovered if discovered_value > REPAIR_COST else None
    fixed_bound = fixed if fixed_value > REPAIR_COST else None

    mutable_transfer = heldout_pattern_accuracy(discovered_bound, holdout, hidden.mask, mutable_meter)
    fixed_transfer = heldout_pattern_accuracy(fixed_bound, holdout, hidden.mask, fixed_meter)

    assert mutable_meter.snapshot() == fixed_meter.snapshot()
    assert mutable_transfer == 1.0

    return {
        "true_ontology": family,
        "selected_ontology": discovered.families[0],
        "selected_object": discovered.description,
        "fixed_selected_object": None if fixed is None else fixed.description,
        "base_error": 1.0 - BASE_ACCURACY,
        "probe_count": len(observed),
        "holdout_count": len(holdout),
        "discovered_training_fit": discovered_fit,
        "fixed_training_fit": fixed_fit,
        "discovered_repair_value": discovered_value,
        "fixed_repair_value": fixed_value,
        "discovered_bound": discovered_bound is not None,
        "fixed_bound": fixed_bound is not None,
        "discovered_heldout_pattern_accuracy": mutable_transfer,
        "fixed_heldout_pattern_accuracy": fixed_transfer,
        "discovered_future_score": future_score(mutable_transfer, True),
        "fixed_future_score": future_score(fixed_transfer, True),
        "matched_meter": mutable_meter.snapshot(),
    }


def run_null():
    observed = tuple(ITEMS[:N_PROBES])
    holdout = tuple(ITEMS[N_PROBES:])
    true_mask = frozenset()

    mutable_meter = Meter(
        probes=len(observed),
        memory_cells=len(observed) * 2,
        storage_slots=STORAGE_SLOTS,
    )
    fixed_meter = Meter(
        probes=len(observed),
        memory_cells=len(observed) * 2,
        storage_slots=STORAGE_SLOTS,
    )
    mutable_scored = inspect_all(observed, true_mask, mutable_meter)
    fixed_scored = inspect_all(observed, true_mask, fixed_meter)

    discovered, _ = choose_best(mutable_scored, allowed_family=None)
    fixed, _ = choose_best(fixed_scored, allowed_family="state_subset")
    discovered_value = repair_value(discovered, observed, true_mask)
    fixed_value = repair_value(fixed, observed, true_mask)
    discovered_bound = discovered if discovered_value > REPAIR_COST else None
    fixed_bound = fixed if fixed_value > REPAIR_COST else None

    mutable_transfer = heldout_pattern_accuracy(discovered_bound, holdout, true_mask, mutable_meter)
    fixed_transfer = heldout_pattern_accuracy(fixed_bound, holdout, true_mask, fixed_meter)

    assert mutable_meter.snapshot() == fixed_meter.snapshot()
    assert discovered_value == fixed_value == 0.0
    assert discovered_bound is None and fixed_bound is None
    assert mutable_transfer == fixed_transfer == 1.0

    return {
        "base_error": 1.0 - BASE_ACCURACY,
        "estimated_repair_value_discovering": discovered_value,
        "estimated_repair_value_fixed": fixed_value,
        "ontology_mutated_discovering": False,
        "ontology_mutated_fixed": False,
        "heldout_task_accuracy_discovering": BASE_ACCURACY,
        "heldout_task_accuracy_fixed": BASE_ACCURACY,
        "matched_meter": mutable_meter.snapshot(),
    }


def run_audit():
    cases = {family: run_case(family) for family in ONTOLOGY_FAMILIES}
    assert all(case["base_error"] == 0.125 for case in cases.values())
    assert all(case["selected_ontology"] == family for family, case in cases.items())
    assert all(case["discovered_heldout_pattern_accuracy"] == 1.0 for case in cases.values())

    fixed_mean = sum(case["fixed_heldout_pattern_accuracy"] for case in cases.values()) / len(cases)
    fixed_exact_families = sum(
        case["fixed_heldout_pattern_accuracy"] == 1.0
        and case["fixed_training_fit"] == 1.0
        for case in cases.values()
    )
    meters = {case["matched_meter"] for case in cases.values()}
    assert len(meters) == 1

    null = run_null()
    return {
        "candidate_universe": {
            "ontology_families": ONTOLOGY_FAMILIES,
            "semantic_candidates": len(CANDIDATES),
            "fixed_ontology": "state_subset",
            "named_correct_ontology_input": False,
        },
        "equal_error_cases": cases,
        "summary": {
            "ontology_cases": len(cases),
            "discovering_correct_ontology_rate": sum(
                case["selected_ontology"] == family for family, case in cases.items()
            ) / len(cases),
            "discovering_mean_heldout_pattern_accuracy": sum(
                case["discovered_heldout_pattern_accuracy"] for case in cases.values()
            ) / len(cases),
            "fixed_mean_heldout_pattern_accuracy": fixed_mean,
            "fixed_exact_case_count": fixed_exact_families,
            "matched_meter_per_case": next(iter(meters)),
        },
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
