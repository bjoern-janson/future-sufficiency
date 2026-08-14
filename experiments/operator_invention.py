"""Operator-invention experiment (Experiment 006).

A learner receives probe-labeled examples from many small tasks. Its online
representation language G0 is finite and exhaustively searched. If residual
error remains, a self-extending condition may synthesize a reusable binary
operator body from low-level Boolean primitives and bind that body to a new
macro slot when expected future value exceeds invention cost.

There is no menu of named semantic extensions. The primitive program language
is fixed, so this tests operator invention relative to G0, not unrestricted
creation outside the supplied computational substrate.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from itertools import combinations, product
from random import Random
from typing import Iterable


N_BITS = 16
TRAIN_TASKS = 60
TEST_TASKS = 30
PROBE_EXAMPLES_PER_TASK = 2
HELDOUT_EXAMPLES = 3_000
FUTURE_HORIZON = 100
LOW_INVENTION_COST = 10.0
HIGH_INVENTION_COST = 35.0
MAX_OPERATOR_BODY_NODES = 8
MACRO_STORAGE_NODES = 8


class Family(str, Enum):
    PARITY = "parity"
    BASE_SUFFICIENT = "base_sufficient"


class Primitive(str, Enum):
    X = "x"
    Y = "y"
    NOT = "not"
    AND = "and"
    OR = "or"


@dataclass(frozen=True)
class Program:
    op: Primitive
    left: Program | None = None
    right: Program | None = None

    def evaluate(self, x: int, y: int) -> int:
        if self.op is Primitive.X:
            return x
        if self.op is Primitive.Y:
            return y
        if self.op is Primitive.NOT:
            if self.left is None:
                raise ValueError("NOT requires left")
            return 1 - self.left.evaluate(x, y)
        if self.left is None or self.right is None:
            raise ValueError("binary primitive requires two children")
        left = self.left.evaluate(x, y)
        right = self.right.evaluate(x, y)
        if self.op is Primitive.AND:
            return left & right
        if self.op is Primitive.OR:
            return left | right
        raise ValueError(self.op)

    def size(self) -> int:
        if self.op in (Primitive.X, Primitive.Y):
            return 1
        if self.op is Primitive.NOT:
            assert self.left is not None
            return 1 + self.left.size()
        assert self.left is not None and self.right is not None
        return 1 + self.left.size() + self.right.size()

    def __str__(self) -> str:
        if self.op in (Primitive.X, Primitive.Y):
            return self.op.value
        if self.op is Primitive.NOT:
            return f"not({self.left})"
        return f"{self.op.value}({self.left},{self.right})"


@dataclass(frozen=True)
class ProbeExample:
    bits: tuple[int, ...]
    arg_i: int
    arg_j: int
    label: int


@dataclass(frozen=True)
class SearchAnalysis:
    base_program: Program
    base_accuracy: float
    invented_program: Program
    invented_accuracy: float
    estimated_invention_value: float
    candidate_evaluations: int


@dataclass(frozen=True)
class Decision:
    active_program: Program
    invented: bool
    invention_cost: float
    analysis: SearchAnalysis


def truth_table(program: Program) -> tuple[int, int, int, int]:
    return tuple(
        program.evaluate(x, y)
        for x, y in product((0, 1), repeat=2)
    )


def enumerate_unique_programs(max_nodes: int) -> dict[tuple[int, ...], Program]:
    """Enumerate minimal primitive programs, deduplicated by binary truth table."""
    x = Program(Primitive.X)
    y = Program(Primitive.Y)
    by_size: dict[int, dict[tuple[int, ...], Program]] = {
        1: {truth_table(x): x, truth_table(y): y}
    }
    best: dict[tuple[int, ...], Program] = dict(by_size[1])

    for size in range(2, max_nodes + 1):
        current: dict[tuple[int, ...], Program] = {}

        for child in by_size.get(size - 1, {}).values():
            candidate = Program(Primitive.NOT, left=child)
            table = truth_table(candidate)
            if table not in best:
                previous = current.get(table)
                if previous is None or str(candidate) < str(previous):
                    current[table] = candidate

        for left_size in range(1, size - 1):
            right_size = size - 1 - left_size
            for left in by_size.get(left_size, {}).values():
                for right in by_size.get(right_size, {}).values():
                    for op in (Primitive.AND, Primitive.OR):
                        candidate = Program(op, left=left, right=right)
                        table = truth_table(candidate)
                        if table not in best:
                            previous = current.get(table)
                            if previous is None or str(candidate) < str(previous):
                                current[table] = candidate

        by_size[size] = current
        best.update(current)

    return best


def target(family: Family, x: int, y: int) -> int:
    if family is Family.PARITY:
        return x ^ y
    return x | y


def all_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(N_BITS), 2))


def train_pairs() -> tuple[tuple[int, int], ...]:
    return all_pairs()[:TRAIN_TASKS]


def test_pairs() -> tuple[tuple[int, int], ...]:
    return all_pairs()[80 : 80 + TEST_TASKS]


def generate_probe_examples(
    family: Family,
    *,
    seed: int,
) -> list[ProbeExample]:
    """Two distinct local input patterns per task.

    No single task can identify a unique binary truth function from only two
    observed rows of its four-row truth table.
    """
    rng = Random(seed)
    examples: list[ProbeExample] = []
    seen_raw: set[tuple[int, ...]] = set()

    for arg_i, arg_j in train_pairs():
        local_patterns: set[tuple[int, int]] = set()
        while len(local_patterns) < PROBE_EXAMPLES_PER_TASK:
            bits = tuple(rng.choice((0, 1)) for _ in range(N_BITS))
            if bits in seen_raw:
                continue
            local = (bits[arg_i], bits[arg_j])
            if local in local_patterns:
                continue
            local_patterns.add(local)
            seen_raw.add(bits)
            examples.append(
                ProbeExample(
                    bits=bits,
                    arg_i=arg_i,
                    arg_j=arg_j,
                    label=target(family, *local),
                )
            )

    return examples


def generate_heldout_examples(
    family: Family,
    *,
    seed: int,
    exclude_raw: set[tuple[int, ...]],
) -> list[ProbeExample]:
    rng = Random(seed)
    examples: list[ProbeExample] = []
    seen_raw = set(exclude_raw)
    pairs = test_pairs()

    while len(examples) < HELDOUT_EXAMPLES:
        bits = tuple(rng.choice((0, 1)) for _ in range(N_BITS))
        if bits in seen_raw:
            continue
        seen_raw.add(bits)
        arg_i, arg_j = rng.choice(pairs)
        examples.append(
            ProbeExample(
                bits=bits,
                arg_i=arg_i,
                arg_j=arg_j,
                label=target(
                    family,
                    bits[arg_i],
                    bits[arg_j],
                ),
            )
        )

    return examples


def program_accuracy(
    program: Program,
    examples: Iterable[ProbeExample],
) -> float:
    examples = list(examples)
    correct = sum(
        program.evaluate(
            example.bits[example.arg_i],
            example.bits[example.arg_j],
        )
        == example.label
        for example in examples
    )
    return correct / len(examples)


def choose_best(
    programs: Iterable[Program],
    examples: list[ProbeExample],
) -> tuple[Program, float]:
    scored = [
        (program_accuracy(program, examples), program)
        for program in programs
    ]
    scored.sort(
        key=lambda item: (
            -item[0],
            item[1].size(),
            str(item[1]),
        )
    )
    accuracy, program = scored[0]
    return program, accuracy


def analyze_language(
    examples: list[ProbeExample],
) -> SearchAnalysis:
    """Run the same exhaustive search used by both experimental conditions."""
    all_programs = enumerate_unique_programs(MAX_OPERATOR_BODY_NODES)
    base_programs = [
        program
        for program in all_programs.values()
        if program.size() <= 3
    ]
    operator_programs = list(all_programs.values())

    base_program, base_accuracy = choose_best(base_programs, examples)
    invented_program, invented_accuracy = choose_best(
        operator_programs,
        examples,
    )

    estimated_value = FUTURE_HORIZON * max(
        0.0,
        invented_accuracy - base_accuracy,
    )

    # Both conditions score every synthesized operator body over every label.
    candidate_evaluations = len(operator_programs) * len(examples)

    return SearchAnalysis(
        base_program=base_program,
        base_accuracy=base_accuracy,
        invented_program=invented_program,
        invented_accuracy=invented_accuracy,
        estimated_invention_value=estimated_value,
        candidate_evaluations=candidate_evaluations,
    )


def self_extending_decision(
    analysis: SearchAnalysis,
    *,
    invention_cost: float,
) -> Decision:
    is_new_truth_function = (
        analysis.invented_program.size() > 3
        and analysis.invented_accuracy > analysis.base_accuracy
    )
    invent = (
        is_new_truth_function
        and analysis.estimated_invention_value > invention_cost
    )
    return Decision(
        active_program=(
            analysis.invented_program
            if invent
            else analysis.base_program
        ),
        invented=invent,
        invention_cost=invention_cost,
        analysis=analysis,
    )


def fixed_language_decision(
    analysis: SearchAnalysis,
    *,
    invention_cost: float,
) -> Decision:
    """Matched-search control: analyzes candidates but cannot bind a macro."""
    return Decision(
        active_program=analysis.base_program,
        invented=False,
        invention_cost=invention_cost,
        analysis=analysis,
    )


def exact_pair_ceiling(
    family: Family,
    *,
    base_only: bool,
) -> float:
    programs = enumerate_unique_programs(MAX_OPERATOR_BODY_NODES)
    candidates = [
        program
        for program in programs.values()
        if (not base_only or program.size() <= 3)
    ]
    rows = [
        ProbeExample((x, y), 0, 1, target(family, x, y))
        for x, y in product((0, 1), repeat=2)
    ]
    return max(program_accuracy(program, rows) for program in candidates)


def single_task_min_consistent_programs(
    examples: list[ProbeExample],
) -> int:
    programs = enumerate_unique_programs(MAX_OPERATOR_BODY_NODES)
    grouped: dict[tuple[int, int], list[ProbeExample]] = {}
    for example in examples:
        grouped.setdefault(
            (example.arg_i, example.arg_j),
            [],
        ).append(example)

    counts = []
    for task_examples in grouped.values():
        counts.append(
            sum(
                program_accuracy(program, task_examples) == 1.0
                for program in programs.values()
            )
        )
    return min(counts)


def recursive_ternary_accuracy(program: Program) -> float:
    """Evaluator diagnostic: generic recursive reuse on ternary parity."""
    correct = 0
    rows = 0
    for x, y, z in product((0, 1), repeat=3):
        represented = program.evaluate(
            program.evaluate(x, y),
            z,
        )
        correct += represented == (x ^ y ^ z)
        rows += 1
    return correct / rows


def exact_fixed_ternary_ceiling() -> float:
    """G0 can inspect at most two of three arguments; enumerate that ceiling."""
    programs = [
        program
        for program in enumerate_unique_programs(
            MAX_OPERATOR_BODY_NODES
        ).values()
        if program.size() <= 3
    ]
    best = 0.0
    rows = list(product((0, 1), repeat=3))
    for arg_i, arg_j in combinations(range(3), 2):
        for program in programs:
            correct = sum(
                program.evaluate(bits[arg_i], bits[arg_j])
                == (bits[0] ^ bits[1] ^ bits[2])
                for bits in rows
            )
            best = max(best, correct / len(rows))
    return best


def run_condition(
    family: Family,
    *,
    invention_cost: float,
    self_extending: bool,
    seed: int,
) -> dict[str, float | str | bool]:
    probe_examples = generate_probe_examples(family, seed=seed)
    heldout = generate_heldout_examples(
        family,
        seed=seed + 100,
        exclude_raw={example.bits for example in probe_examples},
    )
    analysis = analyze_language(probe_examples)
    decision = (
        self_extending_decision(
            analysis,
            invention_cost=invention_cost,
        )
        if self_extending
        else fixed_language_decision(
            analysis,
            invention_cost=invention_cost,
        )
    )

    return {
        "base_empirical_accuracy": analysis.base_accuracy,
        "best_synthesized_accuracy": analysis.invented_accuracy,
        "estimated_invention_value": analysis.estimated_invention_value,
        "invention_cost": invention_cost,
        "invented": decision.invented,
        "active_program": str(decision.active_program),
        "active_program_nodes": float(decision.active_program.size()),
        "heldout_accuracy": program_accuracy(
            decision.active_program,
            heldout,
        ),
        "probe_labels": float(len(probe_examples)),
        "candidate_evaluations": float(
            analysis.candidate_evaluations
        ),
        "macro_storage_nodes": float(MACRO_STORAGE_NODES),
        "train_tasks": float(len(train_pairs())),
        "test_tasks": float(len(test_pairs())),
        "pair_overlap": float(
            len(set(train_pairs()) & set(test_pairs()))
        ),
        "raw_overlap": float(
            len(
                {example.bits for example in probe_examples}
                & {example.bits for example in heldout}
            )
        ),
        "single_task_min_consistent_programs": float(
            single_task_min_consistent_programs(probe_examples)
        ),
    }


def run_experiment() -> dict[str, float | str | bool]:
    parity_low = run_condition(
        Family.PARITY,
        invention_cost=LOW_INVENTION_COST,
        self_extending=True,
        seed=11,
    )
    parity_high = run_condition(
        Family.PARITY,
        invention_cost=HIGH_INVENTION_COST,
        self_extending=True,
        seed=11,
    )
    parity_fixed = run_condition(
        Family.PARITY,
        invention_cost=LOW_INVENTION_COST,
        self_extending=False,
        seed=11,
    )
    sufficient_low = run_condition(
        Family.BASE_SUFFICIENT,
        invention_cost=LOW_INVENTION_COST,
        self_extending=True,
        seed=11,
    )

    base_parity_ceiling = exact_pair_ceiling(
        Family.PARITY,
        base_only=True,
    )
    full_parity_ceiling = exact_pair_ceiling(
        Family.PARITY,
        base_only=False,
    )
    fixed_ternary_ceiling = exact_fixed_ternary_ceiling()

    all_programs = enumerate_unique_programs(
        MAX_OPERATOR_BODY_NODES
    )
    invented_program = analyze_language(
        generate_probe_examples(Family.PARITY, seed=11)
    ).invented_program
    ternary_reuse = recursive_ternary_accuracy(invented_program)

    assert base_parity_ceiling == 0.75
    assert full_parity_ceiling == 1.0

    assert parity_low["invented"] is True
    assert parity_low["heldout_accuracy"] == 1.0
    assert parity_low["single_task_min_consistent_programs"] > 1.0

    assert parity_high["invented"] is False
    assert sufficient_low["invented"] is False

    assert parity_fixed["heldout_accuracy"] < 0.85
    assert (
        parity_low["candidate_evaluations"]
        == parity_fixed["candidate_evaluations"]
    )
    assert parity_low["probe_labels"] == parity_fixed["probe_labels"]
    assert (
        parity_low["macro_storage_nodes"]
        == parity_fixed["macro_storage_nodes"]
    )

    assert parity_low["pair_overlap"] == 0.0
    assert parity_low["raw_overlap"] == 0.0

    assert ternary_reuse == 1.0
    assert fixed_ternary_ceiling == 0.5

    return {
        "primitive_truth_functions_found": float(len(all_programs)),
        "g0_exact_parity_ceiling": base_parity_ceiling,
        "synthesized_language_parity_ceiling": full_parity_ceiling,
        "invented_operator_body": str(invented_program),
        "invented_operator_nodes": float(invented_program.size()),
        "low_cost_invented": parity_low["invented"],
        "low_cost_estimated_value": parity_low[
            "estimated_invention_value"
        ],
        "low_cost_transfer_accuracy": parity_low["heldout_accuracy"],
        "high_cost_invented": parity_high["invented"],
        "high_cost_transfer_accuracy": parity_high["heldout_accuracy"],
        "sufficient_task_invented": sufficient_low["invented"],
        "sufficient_task_transfer_accuracy": sufficient_low[
            "heldout_accuracy"
        ],
        "fixed_language_transfer_accuracy": parity_fixed[
            "heldout_accuracy"
        ],
        "probe_labels_each": parity_low["probe_labels"],
        "candidate_evaluations_each": parity_low[
            "candidate_evaluations"
        ],
        "macro_storage_nodes_each": parity_low[
            "macro_storage_nodes"
        ],
        "train_tasks": parity_low["train_tasks"],
        "heldout_tasks": parity_low["test_tasks"],
        "single_task_min_consistent_programs": parity_low[
            "single_task_min_consistent_programs"
        ],
        "train_test_pair_overlap": parity_low["pair_overlap"],
        "raw_configuration_overlap": parity_low["raw_overlap"],
        "recursive_ternary_reuse_accuracy": ternary_reuse,
        "fixed_g0_ternary_ceiling": fixed_ternary_ceiling,
    }


if __name__ == "__main__":
    results = run_experiment()
    for name, value in results.items():
        if isinstance(value, float):
            print(f"{name}: {value:.4f}")
        else:
            print(f"{name}: {value}")
