"""Repair-axis discovery audit for the 001-008 future-sufficiency ladder.

This is not Experiment 009. It tests whether a system can synthesize a missing
repair dimension from anonymous structural descriptors rather than choose among
designer-labeled axes. A fixed-axis baseline is restricted to single descriptor
literals. Probe, candidate, execution, memory, and storage budgets are measured.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from random import Random

N_INPUTS = 3
N_DESC_BITS = 4
MAX_BASE_NODES = 9
MAX_AXIS_NODES = 5
REPEATS = 8
HORIZON = 100.0
BIND_COST = 1.0
SCOPE_COST = 2.0
SAMPLED_AXES = 12
SAMPLE_SEED = 1408


def rows(n: int):
    return tuple(product((0, 1), repeat=n))


def tt_from_fn(n: int, fn) -> int:
    return sum(int(fn(r)) << i for i, r in enumerate(rows(n)))


def bit(tt: int, i: int) -> int:
    return (tt >> i) & 1


def mask(n: int) -> int:
    return (1 << (1 << n)) - 1


@dataclass(frozen=True)
class Program:
    tt: int
    expr: str
    size: int
    counts: tuple[int, ...]


def build_base_language() -> dict[int, Program]:
    """Enumerate a finite read-once NOT/AND/OR language over three inputs."""
    levels: dict[int, dict[tuple[int, tuple[int, ...]], Program]] = defaultdict(dict)
    for j in range(N_INPUTS):
        tt = tt_from_fn(N_INPUTS, lambda r, j=j: r[j])
        counts = tuple(int(k == j) for k in range(N_INPUTS))
        levels[1][(tt, counts)] = Program(tt, f"v{j}", 1, counts)

    full = mask(N_INPUTS)
    for size in range(2, MAX_BASE_NODES + 1):
        for (tt, counts), p in levels[size - 1].items():
            q = Program((~tt) & full, f"not({p.expr})", size, counts)
            levels[size].setdefault((q.tt, counts), q)
        for left_size in range(1, size - 1):
            right_size = size - 1 - left_size
            if right_size < 1:
                continue
            for (_lt, left_counts), left in levels[left_size].items():
                for (_rt, right_counts), right in levels[right_size].items():
                    counts = tuple(a + b for a, b in zip(left_counts, right_counts))
                    if max(counts) > 1:
                        continue
                    for name, tt in (
                        ("and", left.tt & right.tt),
                        ("or", left.tt | right.tt),
                    ):
                        p = Program(tt, f"{name}({left.expr},{right.expr})", size, counts)
                        levels[size].setdefault((tt, counts), p)

    best: dict[int, Program] = {}
    for size in range(1, MAX_BASE_NODES + 1):
        for (tt, _counts), p in levels[size].items():
            old = best.get(tt)
            if old is None or (p.size, p.expr) < (old.size, old.expr):
                best[tt] = p
    return best


BASE = build_base_language()


def mapped_exact_acc(expr_tt: int, target_tt: int) -> float:
    best = 0
    for m0, m1 in product((0, 1), repeat=2):
        correct = 0
        for i in range(1 << N_INPUTS):
            pred = m1 if bit(expr_tt, i) else m0
            correct += pred == bit(target_tt, i)
        best = max(best, correct)
    return best / (1 << N_INPUTS)


def base_ceiling(target_tt: int) -> float:
    return max(mapped_exact_acc(p.tt, target_tt) for p in BASE.values())


def choose_optional_targets() -> list[int]:
    """Choose 16 non-complement-equivalent targets with base ceiling exactly .875."""
    chosen: list[int] = []
    seen_pairs: set[int] = set()
    full = mask(N_INPUTS)
    for target in range(1 << (1 << N_INPUTS)):
        if base_ceiling(target) != 0.875:
            continue
        canonical = min(target, target ^ full)
        if canonical in seen_pairs:
            continue
        seen_pairs.add(canonical)
        chosen.append(target)
        if len(chosen) == (1 << N_DESC_BITS):
            return chosen
    raise RuntimeError("not enough optional targets")


OPTIONAL_TARGETS = choose_optional_targets()
DESC_STATES = rows(N_DESC_BITS)
DESC_INDEX = {state: i for i, state in enumerate(DESC_STATES)}
DESC_TO_TARGET = {state: OPTIONAL_TARGETS[i] for i, state in enumerate(DESC_STATES)}


@dataclass(frozen=True)
class AxisProgram:
    tt: int
    expr: str
    size: int

    def accepts(self, state: tuple[int, ...]) -> bool:
        return bool(bit(self.tt, DESC_INDEX[state]))

    @property
    def scope(self) -> int:
        return sum(bit(self.tt, i) for i in range(1 << N_DESC_BITS))


def synth_axis_programs(max_nodes: int = MAX_AXIS_NODES) -> dict[int, AxisProgram]:
    """Synthesize structural predicates over anonymous descriptor bits."""
    levels: dict[int, dict[int, AxisProgram]] = defaultdict(dict)
    for j in range(N_DESC_BITS):
        tt = tt_from_fn(N_DESC_BITS, lambda r, j=j: r[j])
        levels[1][tt] = AxisProgram(tt, f"s{j}", 1)

    full = mask(N_DESC_BITS)
    for size in range(2, max_nodes + 1):
        for tt, p in levels[size - 1].items():
            q = AxisProgram((~tt) & full, f"not({p.expr})", size)
            levels[size].setdefault(q.tt, q)
        for left_size in range(1, size - 1):
            right_size = size - 1 - left_size
            if right_size < 1:
                continue
            for left_tt, left in levels[left_size].items():
                for right_tt, right in levels[right_size].items():
                    for name, tt in (
                        ("and", left_tt & right_tt),
                        ("or", left_tt | right_tt),
                    ):
                        q = AxisProgram(tt, f"{name}({left.expr},{right.expr})", size)
                        levels[size].setdefault(tt, q)

    best: dict[int, AxisProgram] = {}
    for size in range(1, max_nodes + 1):
        for tt, p in levels[size].items():
            old = best.get(tt)
            if old is None or (p.size, p.expr) < (old.size, old.expr):
                best[tt] = p
    return best


AXES = synth_axis_programs()

# Designer-supplied fixed axes are only one-bit literals. The discovery condition
# may synthesize any predicate in AXES. Both reserve the same five-node rule slot.
LITERAL_TTS: set[int] = set()
for j in range(N_DESC_BITS):
    positive = tt_from_fn(N_DESC_BITS, lambda r, j=j: r[j])
    LITERAL_TTS.add(positive)
    LITERAL_TTS.add(positive ^ mask(N_DESC_BITS))

# Hidden axis universe: every minimal two-literal conjunction with exactly four
# admitted structural states. No semantic axis labels are exposed to the learner.
HIDDEN_AXIS_UNIVERSE = tuple(
    sorted(
        (
            p for p in AXES.values()
            if p.scope == 4 and p.tt not in LITERAL_TTS and p.size <= 4
        ),
        key=lambda p: (p.size, p.expr, p.tt),
    )
)
assert len(HIDDEN_AXIS_UNIVERSE) == 24

_rng = Random(SAMPLE_SEED)
SAMPLED_HIDDEN_AXES = tuple(_rng.sample(list(HIDDEN_AXIS_UNIVERSE), SAMPLED_AXES))


@dataclass(frozen=True)
class Example:
    target_tt: int
    row_index: int
    label: int
    surface_id: int


@dataclass
class Meter:
    probes: int = 0
    axis_candidates: int = 0
    semantic_candidates: int = 0
    executions: int = 0
    memory_cells: int = 0
    storage_slots: int = 0

    def snapshot(self):
        return (
            self.probes,
            self.axis_candidates,
            self.semantic_candidates,
            self.executions,
            self.memory_cells,
            self.storage_slots,
        )


def make_task_examples(target_tt: int, *, heldout: bool, noisy: bool = False) -> list[Example]:
    result: list[Example] = []
    offset = 100_000 if heldout else 0
    for row_index in range(1 << N_INPUTS):
        true_label = bit(target_tt, row_index)
        for rep in range(REPEATS):
            label = true_label
            if noisy and rep == (1 if heldout else 0):
                label = 1 - label
            result.append(
                Example(
                    target_tt=target_tt,
                    row_index=row_index,
                    label=label,
                    surface_id=offset + target_tt * 100 + row_index * REPEATS + rep,
                )
            )
    return result


def optional_program(target_tt: int) -> Program:
    return Program(target_tt, f"optional_{target_tt:02x}", 1, (1, 1, 1))


def induced_language(axis: AxisProgram | None) -> dict[int, Program]:
    language = dict(BASE)
    if axis is None:
        return language
    for state, target in DESC_TO_TARGET.items():
        if axis.accepts(state):
            language.setdefault(target, optional_program(target))
    return language


def mapped_sample_accuracy(program: Program, examples: list[Example], meter: Meter) -> float:
    meter.semantic_candidates += 1
    # Four possible deterministic mappings from representation bit to label.
    meter.executions += len(examples) * 4
    counts = {0: [0, 0], 1: [0, 0]}
    for example in examples:
        counts[bit(program.tt, example.row_index)][example.label] += 1
    return (
        max(counts[0]) + max(counts[1])
    ) / len(examples)


def best_accuracy(language: dict[int, Program], examples: list[Example], meter: Meter) -> float:
    return max(mapped_sample_accuracy(p, examples, meter) for p in language.values())


def axis_objective(axis: AxisProgram, training_sets: list[list[Example]], meter: Meter):
    meter.axis_candidates += 1
    repaired = induced_language(axis)
    gains = []
    for examples in training_sets:
        base_acc = best_accuracy(BASE, examples, meter)
        repaired_acc = best_accuracy(repaired, examples, meter)
        gains.append(max(0.0, repaired_acc - base_acc))
    gross = HORIZON * (sum(gains) / len(gains))
    cost = BIND_COST + SCOPE_COST * axis.scope
    return gross - cost, gross


def candidate_schedule(*, fixed_only: bool) -> list[AxisProgram]:
    all_candidates = sorted(AXES.values(), key=lambda p: (p.size, p.expr, p.tt))
    if not fixed_only:
        return all_candidates
    literals = [p for p in all_candidates if p.tt in LITERAL_TTS]
    # Burn the same candidate slots by deterministic literal rescoring.
    return [literals[i % len(literals)] for i in range(len(all_candidates))]


def discover_axis(training_targets: list[int], meter: Meter, *, fixed_only: bool):
    training_sets = [make_task_examples(tt, heldout=False) for tt in training_targets]
    meter.probes += sum(len(examples) for examples in training_sets)
    meter.memory_cells = max(meter.memory_cells, sum(len(examples) for examples in training_sets) * 2)
    meter.storage_slots = MAX_AXIS_NODES

    best = None
    seen: set[int] = set()
    for axis in candidate_schedule(fixed_only=fixed_only):
        net, gross = axis_objective(axis, training_sets, meter)
        if axis.tt in seen:
            continue
        seen.add(axis.tt)
        candidate = (net, -axis.size, -axis.scope, axis.expr, axis, gross)
        if best is None or candidate[:4] > best[:4]:
            best = candidate

    if best is None or best[0] <= 0:
        return None, 0.0
    return best[4], best[5]


def matched_heldout(
    discovered: AxisProgram,
    bound_discovery: AxisProgram | None,
    bound_fixed: AxisProgram | None,
    target_tt: int,
    discovery_meter: Meter,
    fixed_meter: Meter,
):
    """Score identical counterfactual languages in both branches, then act on binding."""
    examples = make_task_examples(target_tt, heldout=True)
    scores_discovery = {}
    scores_fixed = {}
    for name, axis in (("keep", None), ("discovered", discovered)):
        scores_discovery[name] = best_accuracy(induced_language(axis), examples, discovery_meter)
        scores_fixed[name] = best_accuracy(induced_language(axis), examples, fixed_meter)
    assert scores_discovery == scores_fixed
    d_key = "discovered" if bound_discovery is not None else "keep"
    f_key = "discovered" if bound_fixed is not None and bound_fixed.tt == discovered.tt else "keep"
    return scores_discovery[d_key], scores_fixed[f_key]


def run_axis(axis: AxisProgram):
    positive_states = [state for state in DESC_STATES if axis.accepts(state)]
    assert len(positive_states) == 4
    training_states = positive_states[:3]
    heldout_state = positive_states[3]
    training_targets = [DESC_TO_TARGET[state] for state in training_states]
    heldout_target = DESC_TO_TARGET[heldout_state]

    discovery_meter, fixed_meter = Meter(), Meter()
    discovered, gross = discover_axis(training_targets, discovery_meter, fixed_only=False)
    fixed, fixed_gross = discover_axis(training_targets, fixed_meter, fixed_only=True)
    assert discovery_meter.snapshot() == fixed_meter.snapshot()
    assert discovered is not None and discovered.tt == axis.tt
    assert fixed is None and fixed_gross == 0.0

    discovery_acc, fixed_acc = matched_heldout(
        discovered,
        discovered,
        fixed,
        heldout_target,
        discovery_meter,
        fixed_meter,
    )
    assert discovery_meter.snapshot() == fixed_meter.snapshot()
    assert discovery_acc == 1.0 and fixed_acc == 0.875

    return {
        "evaluator_axis": axis.expr,
        "discovered_axis": discovered.expr,
        "training_tasks": 3,
        "heldout_tasks": 1,
        "base_error_each": 0.125,
        "gross_repair_value": gross,
        "axis_discovering_transfer": discovery_acc,
        "fixed_axis_transfer": fixed_acc,
        "budget_snapshot_each": discovery_meter.snapshot(),
    }


def recoverability_check(axis: AxisProgram) -> bool:
    positive_states = [state for state in DESC_STATES if axis.accepts(state)]
    training_targets = [DESC_TO_TARGET[state] for state in positive_states[:3]]
    meter = Meter()
    discovered, _gross = discover_axis(training_targets, meter, fixed_only=False)
    return discovered is not None and discovered.tt == axis.tt


def run_null():
    """Same .125 residual, but no representational defect and no positive repair value."""
    target = tt_from_fn(N_INPUTS, lambda r: r[0] or r[1] or r[2])
    training = make_task_examples(target, heldout=False, noisy=True)

    def diagnose(meter: Meter, fixed_only: bool):
        meter.probes += len(training)
        meter.memory_cells = len(training) * 2
        meter.storage_slots = MAX_AXIS_NODES
        best = None
        seen: set[int] = set()
        for axis in candidate_schedule(fixed_only=fixed_only):
            meter.axis_candidates += 1
            base_acc = best_accuracy(BASE, training, meter)
            repaired_acc = best_accuracy(induced_language(axis), training, meter)
            gross = HORIZON * max(0.0, repaired_acc - base_acc)
            net = gross - (BIND_COST + SCOPE_COST * axis.scope)
            if axis.tt in seen:
                continue
            seen.add(axis.tt)
            candidate = (net, -axis.size, -axis.scope, axis.expr, axis)
            if best is None or candidate[:4] > best[:4]:
                best = candidate
        return best[4] if best is not None and best[0] > 0 else None

    discovery_meter, fixed_meter = Meter(), Meter()
    discovered = diagnose(discovery_meter, False)
    fixed = diagnose(fixed_meter, True)
    assert discovery_meter.snapshot() == fixed_meter.snapshot()
    assert discovered is None and fixed is None

    heldout = make_task_examples(target, heldout=True, noisy=True)
    # Match held-out compute by scoring base twice in both branches.
    d1 = best_accuracy(BASE, heldout, discovery_meter)
    d2 = best_accuracy(BASE, heldout, discovery_meter)
    f1 = best_accuracy(BASE, heldout, fixed_meter)
    f2 = best_accuracy(BASE, heldout, fixed_meter)
    assert d1 == d2 == f1 == f2 == 0.875
    assert discovery_meter.snapshot() == fixed_meter.snapshot()

    return {
        "heldout_residual_error": 0.125,
        "axis_discovering_repair": "none",
        "fixed_axis_repair": "none",
        "axis_discovering_transfer": d1,
        "fixed_axis_transfer": f1,
        "budget_snapshot_each": discovery_meter.snapshot(),
    }


def run_audit():
    assert len(BASE) == 94
    assert len(OPTIONAL_TARGETS) == 16
    assert all(base_ceiling(target) == 0.875 for target in OPTIONAL_TARGETS)
    assert len(AXES) == 90
    assert len(LITERAL_TTS) == 8
    assert len(HIDDEN_AXIS_UNIVERSE) == 24

    sampled_results = [run_axis(axis) for axis in SAMPLED_HIDDEN_AXES]
    complete_recoverability = sum(recoverability_check(axis) for axis in HIDDEN_AXIS_UNIVERSE)
    assert complete_recoverability == len(HIDDEN_AXIS_UNIVERSE)
    null = run_null()

    return {
        "meta": {
            "base_language_semantics": len(BASE),
            "axis_language_semantics": len(AXES),
            "fixed_axis_unique_literals": len(LITERAL_TTS),
            "hidden_axis_universe": len(HIDDEN_AXIS_UNIVERSE),
            "sampled_hidden_axes": len(SAMPLED_HIDDEN_AXES),
            "complete_axis_recoverability": complete_recoverability,
        },
        "sampled_axes": sampled_results,
        "killer_null": null,
    }


if __name__ == "__main__":
    report = run_audit()
    print("[meta]")
    for key, value in report["meta"].items():
        print(f"{key}: {value}")
    for index, result in enumerate(report["sampled_axes"], 1):
        print(f"\n[sampled_axis_{index}]")
        for key, value in result.items():
            print(f"{key}: {value}")
    print("\n[killer_null]")
    for key, value in report["killer_null"].items():
        print(f"{key}: {value}")
