"""Primitive/meta-language repair experiment (Experiment 007).

The online representation generator begins with a finite read-once construction
rule over NOT/AND/OR. The base meta-language is exhaustively characterized.
A repaired condition may pay to enable variable fan-out/reuse, then persist
that construction rule for future operator synthesis.

This tests representation-generator repair only. Goal/reward semantics and
authority are evaluator-owned and immutable.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from itertools import combinations, product
from random import Random
from typing import Iterable

N_BITS = 18
TRAIN_TASKS = 50
TEST_TASKS = 25
PROBE_PATTERNS_PER_TASK = 4
HELDOUT_EXAMPLES = 3000
FUTURE_HORIZON = 100
LOW_REPAIR_COST = 5.0
HIGH_REPAIR_COST = 20.0
MAX_FANOUT_NODES = 9


class Family(str, Enum):
    NEEDS_FANOUT = "needs_fanout"
    BASE_SUFFICIENT = "base_sufficient"
    NOVEL_XOR = "novel_xor"


class Op(str, Enum):
    VAR = "var"
    NOT = "not"
    AND = "and"
    OR = "or"


@dataclass(frozen=True)
class Program:
    op: Op
    var: int = -1
    left: Program | None = None
    right: Program | None = None

    def evaluate_local(self, values: tuple[int, int, int]) -> int:
        if self.op is Op.VAR:
            return values[self.var]
        if self.op is Op.NOT:
            assert self.left is not None
            return 1 - self.left.evaluate_local(values)
        assert self.left is not None and self.right is not None
        left = self.left.evaluate_local(values)
        right = self.right.evaluate_local(values)
        if self.op is Op.AND:
            return left & right
        if self.op is Op.OR:
            return left | right
        raise ValueError(self.op)

    def size(self) -> int:
        if self.op is Op.VAR:
            return 1
        if self.op is Op.NOT:
            assert self.left is not None
            return 1 + self.left.size()
        assert self.left is not None and self.right is not None
        return 1 + self.left.size() + self.right.size()

    def support(self) -> frozenset[int]:
        if self.op is Op.VAR:
            return frozenset((self.var,))
        if self.op is Op.NOT:
            assert self.left is not None
            return self.left.support()
        assert self.left is not None and self.right is not None
        return self.left.support() | self.right.support()

    def __str__(self) -> str:
        if self.op is Op.VAR:
            return ("x", "y", "z")[self.var]
        if self.op is Op.NOT:
            return f"not({self.left})"
        return f"{self.op.value}({self.left},{self.right})"


LOCAL_PATTERNS = tuple(product((0, 1), repeat=3))


def semantics(program: Program) -> tuple[int, ...]:
    return tuple(program.evaluate_local(values) for values in LOCAL_PATTERNS)


def preferable(program: Program, other: Program) -> bool:
    return (program.size(), str(program)) < (other.size(), str(other))


def build_read_once_programs() -> dict[tuple[int, ...], Program]:
    """Enumerate every semantically distinct read-once formula on x,y,z."""
    by_support: dict[
        frozenset[int], dict[tuple[int, ...], Program]
    ] = defaultdict(dict)

    for var in range(3):
        atom = Program(Op.VAR, var=var)
        by_support[frozenset((var,))][semantics(atom)] = atom
        negated = Program(Op.NOT, left=atom)
        by_support[frozenset((var,))][semantics(negated)] = negated

    for support_size in (2, 3):
        for support_tuple in combinations(range(3), support_size):
            support = frozenset(support_tuple)
            candidates: dict[tuple[int, ...], Program] = {}

            for left_size in range(1, support_size):
                for left_tuple in combinations(support_tuple, left_size):
                    left_support = frozenset(left_tuple)
                    right_support = support - left_support
                    if not right_support:
                        continue

                    for left in by_support[left_support].values():
                        for right in by_support[right_support].values():
                            for op in (Op.AND, Op.OR):
                                combined = Program(op, left=left, right=right)
                                for candidate in (
                                    combined,
                                    Program(Op.NOT, left=combined),
                                ):
                                    key = semantics(candidate)
                                    old = candidates.get(key)
                                    if old is None or preferable(candidate, old):
                                        candidates[key] = candidate

            by_support[support] = candidates

    programs: dict[tuple[int, ...], Program] = {}
    for support_programs in by_support.values():
        for key, program in support_programs.items():
            old = programs.get(key)
            if old is None or preferable(program, old):
                programs[key] = program
    return programs


def build_fanout_programs(
    max_nodes: int = MAX_FANOUT_NODES,
) -> dict[tuple[int, ...], Program]:
    """Enumerate minimal semantic programs when variable reuse is allowed."""
    exact_size: dict[int, dict[tuple[int, ...], Program]] = defaultdict(dict)
    best: dict[tuple[int, ...], Program] = {}

    for var in range(3):
        atom = Program(Op.VAR, var=var)
        key = semantics(atom)
        exact_size[1][key] = atom
        best[key] = atom

    for size in range(2, max_nodes + 1):
        candidates: dict[tuple[int, ...], Program] = {}

        for child in exact_size[size - 1].values():
            candidate = Program(Op.NOT, left=child)
            key = semantics(candidate)
            old = best.get(key)
            if old is None or preferable(candidate, old):
                current = candidates.get(key)
                if current is None or preferable(candidate, current):
                    candidates[key] = candidate

        for left_size in range(1, size - 1):
            right_size = size - 1 - left_size
            if right_size < 1:
                continue
            for left in exact_size[left_size].values():
                for right in exact_size[right_size].values():
                    for op in (Op.AND, Op.OR):
                        candidate = Program(op, left=left, right=right)
                        key = semantics(candidate)
                        old = best.get(key)
                        if old is None or preferable(candidate, old):
                            current = candidates.get(key)
                            if current is None or preferable(candidate, current):
                                candidates[key] = candidate

        exact_size[size] = candidates
        for key, candidate in candidates.items():
            old = best.get(key)
            if old is None or preferable(candidate, old):
                best[key] = candidate

    return best


READ_ONCE_PROGRAMS = build_read_once_programs()
FANOUT_PROGRAMS = build_fanout_programs()


@dataclass(frozen=True)
class Task:
    args: tuple[int, int, int]


@dataclass(frozen=True)
class Example:
    bits: tuple[int, ...]
    task: Task
    hidden: int
    raw_id: int


@dataclass(frozen=True)
class SearchResult:
    accuracy: float
    program: Program


def target(values: tuple[int, int, int], family: Family) -> int:
    x, y, z = values
    if family is Family.NEEDS_FANOUT:
        return int(x + y + z >= 2)
    if family is Family.BASE_SUFFICIENT:
        return (x & y) | z
    if family is Family.NOVEL_XOR:
        return x ^ y
    raise ValueError(family)


def make_task_split(seed: int = 7) -> tuple[list[Task], list[Task]]:
    triples = list(combinations(range(N_BITS), 3))
    rng = Random(seed)
    rng.shuffle(triples)
    needed = TRAIN_TASKS + TEST_TASKS
    if needed > len(triples):
        raise ValueError("not enough argument triples")
    train = [Task(tuple(t)) for t in triples[:TRAIN_TASKS]]
    test = [Task(tuple(t)) for t in triples[TRAIN_TASKS:needed]]
    return train, test


def set_local_pattern(
    bits: list[int],
    task: Task,
    values: tuple[int, int, int],
) -> None:
    for index, value in zip(task.args, values):
        bits[index] = value


def make_probe_examples(
    tasks: Iterable[Task],
    family: Family,
    *,
    seed: int,
) -> list[Example]:
    rng = Random(seed)
    examples: list[Example] = []
    raw_id = 0

    for task in tasks:
        patterns = list(LOCAL_PATTERNS)
        rng.shuffle(patterns)
        for values in patterns[:PROBE_PATTERNS_PER_TASK]:
            bits = [rng.randrange(2) for _ in range(N_BITS)]
            set_local_pattern(bits, task, values)
            examples.append(
                Example(
                    bits=tuple(bits),
                    task=task,
                    hidden=target(values, family),
                    raw_id=raw_id,
                )
            )
            raw_id += 1
    return examples


def make_heldout_examples(
    tasks: Iterable[Task],
    family: Family,
    *,
    seed: int,
    count: int = HELDOUT_EXAMPLES,
    raw_offset: int = 1_000_000,
) -> list[Example]:
    tasks = list(tasks)
    rng = Random(seed)
    examples: list[Example] = []

    for index in range(count):
        task = rng.choice(tasks)
        values = rng.choice(LOCAL_PATTERNS)
        bits = [rng.randrange(2) for _ in range(N_BITS)]
        set_local_pattern(bits, task, values)
        examples.append(
            Example(
                bits=tuple(bits),
                task=task,
                hidden=target(values, family),
                raw_id=raw_offset + index,
            )
        )
    return examples


def local_values(example: Example) -> tuple[int, int, int]:
    return tuple(example.bits[index] for index in example.task.args)  # type: ignore[return-value]


def score_program(program: Program, examples: Iterable[Example]) -> float:
    examples = list(examples)
    correct = sum(
        program.evaluate_local(local_values(example)) == example.hidden
        for example in examples
    )
    return correct / len(examples)


def exhaustive_search(
    programs: Iterable[Program],
    examples: Iterable[Example],
) -> tuple[SearchResult, int]:
    examples = list(examples)
    best: SearchResult | None = None
    calls = 0

    for program in programs:
        accuracy = score_program(program, examples)
        calls += 1
        candidate = SearchResult(accuracy, program)
        if best is None:
            best = candidate
        elif candidate.accuracy > best.accuracy:
            best = candidate
        elif (
            candidate.accuracy == best.accuracy
            and preferable(candidate.program, best.program)
        ):
            best = candidate

    if best is None:
        raise ValueError("empty program language")
    return best, calls


def exact_ceiling(
    programs: dict[tuple[int, ...], Program],
    family: Family,
) -> SearchResult:
    labels = tuple(target(values, family) for values in LOCAL_PATTERNS)
    best: SearchResult | None = None
    for semantic_key, program in programs.items():
        accuracy = sum(
            predicted == label
            for predicted, label in zip(semantic_key, labels)
        ) / len(labels)
        candidate = SearchResult(accuracy, program)
        if best is None or candidate.accuracy > best.accuracy:
            best = candidate
        elif (
            candidate.accuracy == best.accuracy
            and preferable(candidate.program, best.program)
        ):
            best = candidate
    assert best is not None
    return best


class MetaRepairLearner:
    """Repair the construction rule from read-once to fan-out-enabled."""

    def __init__(self) -> None:
        self.fanout_enabled = False
        self.base_result: SearchResult | None = None
        self.fanout_result: SearchResult | None = None
        self.selected_result: SearchResult | None = None
        self.score_calls = 0
        self.estimated_repair_value = 0.0

    def fit(
        self,
        examples: Iterable[Example],
        *,
        repair_cost: float,
        future_horizon: int = FUTURE_HORIZON,
    ) -> None:
        examples = list(examples)
        base, calls = exhaustive_search(READ_ONCE_PROGRAMS.values(), examples)
        self.score_calls += calls
        fanout, calls = exhaustive_search(FANOUT_PROGRAMS.values(), examples)
        self.score_calls += calls

        self.base_result = base
        self.fanout_result = fanout
        gain = max(0.0, fanout.accuracy - base.accuracy)
        self.estimated_repair_value = future_horizon * gain

        if self.estimated_repair_value > repair_cost:
            self.fanout_enabled = True
            self.selected_result = fanout
        else:
            self.selected_result = base

    def search_current_generator(
        self,
        examples: Iterable[Example],
    ) -> SearchResult:
        programs = (
            FANOUT_PROGRAMS.values()
            if self.fanout_enabled
            else READ_ONCE_PROGRAMS.values()
        )
        result, _ = exhaustive_search(programs, examples)
        return result


class FixedMetaLanguageControl:
    """Same labels and scoring budget, but construction rules cannot change."""

    def __init__(self) -> None:
        self.selected_result: SearchResult | None = None
        self.score_calls = 0

    def fit(
        self,
        examples: Iterable[Example],
        *,
        score_budget: int,
    ) -> None:
        examples = list(examples)
        result, calls = exhaustive_search(READ_ONCE_PROGRAMS.values(), examples)
        self.score_calls += calls
        self.selected_result = result

        programs = list(READ_ONCE_PROGRAMS.values())
        index = 0
        while self.score_calls < score_budget:
            score_program(programs[index % len(programs)], examples)
            self.score_calls += 1
            index += 1


def transfer_accuracy(
    result: SearchResult,
    examples: Iterable[Example],
) -> float:
    return score_program(result.program, examples)


def run_primary_condition(
    family: Family,
    *,
    repair_cost: float,
) -> dict[str, float | str]:
    train_tasks, test_tasks = make_task_split()
    probe = make_probe_examples(train_tasks, family, seed=17)
    heldout = make_heldout_examples(test_tasks, family, seed=31)

    learner = MetaRepairLearner()
    learner.fit(probe, repair_cost=repair_cost)

    fixed = FixedMetaLanguageControl()
    fixed.fit(probe, score_budget=learner.score_calls)

    assert learner.selected_result is not None
    assert fixed.selected_result is not None

    return {
        "family": family.value,
        "repair_cost": repair_cost,
        "base_empirical_accuracy": learner.base_result.accuracy,
        "fanout_empirical_accuracy": learner.fanout_result.accuracy,
        "estimated_repair_value": learner.estimated_repair_value,
        "repaired": str(learner.fanout_enabled).lower(),
        "selected_program": str(learner.selected_result.program),
        "selected_program_nodes": float(learner.selected_result.program.size()),
        "transfer_accuracy_repaired_condition": transfer_accuracy(
            learner.selected_result, heldout
        ),
        "transfer_accuracy_fixed_control": transfer_accuracy(
            fixed.selected_result, heldout
        ),
        "score_calls_repair": float(learner.score_calls),
        "score_calls_fixed": float(fixed.score_calls),
        "probe_labels_repair": float(len(probe)),
        "probe_labels_fixed": float(len(probe)),
        "construction_rule_after": (
            "fanout_allowed" if learner.fanout_enabled else "read_once"
        ),
        "goal_rule_mutated": "false",
        "authority_expanded": "false",
    }


def run_novel_family_transfer() -> dict[str, float | str]:
    """Test whether the repaired meta-rule helps construct a different operator."""
    train_tasks, test_tasks = make_task_split(seed=13)

    repair_probe = make_probe_examples(
        train_tasks,
        Family.NEEDS_FANOUT,
        seed=41,
    )
    repaired = MetaRepairLearner()
    repaired.fit(repair_probe, repair_cost=LOW_REPAIR_COST)
    assert repaired.fanout_enabled

    xor_probe = make_probe_examples(
        train_tasks,
        Family.NOVEL_XOR,
        seed=43,
    )
    xor_heldout = make_heldout_examples(
        test_tasks,
        Family.NOVEL_XOR,
        seed=47,
    )
    repaired_xor = repaired.search_current_generator(xor_probe)

    fixed_xor, _ = exhaustive_search(
        READ_ONCE_PROGRAMS.values(),
        xor_probe,
    )

    return {
        "repaired_generator": "fanout_allowed",
        "novel_family": Family.NOVEL_XOR.value,
        "repaired_novel_program": str(repaired_xor.program),
        "repaired_novel_transfer": transfer_accuracy(
            repaired_xor, xor_heldout
        ),
        "fixed_novel_transfer": transfer_accuracy(
            fixed_xor, xor_heldout
        ),
    }


def run_experiment() -> dict[str, dict[str, float | str]]:
    exact_majority_read_once = exact_ceiling(
        READ_ONCE_PROGRAMS, Family.NEEDS_FANOUT
    )
    exact_majority_fanout = exact_ceiling(
        FANOUT_PROGRAMS, Family.NEEDS_FANOUT
    )
    exact_sufficient_read_once = exact_ceiling(
        READ_ONCE_PROGRAMS, Family.BASE_SUFFICIENT
    )
    exact_xor_read_once = exact_ceiling(
        READ_ONCE_PROGRAMS, Family.NOVEL_XOR
    )
    exact_xor_fanout = exact_ceiling(
        FANOUT_PROGRAMS, Family.NOVEL_XOR
    )

    insufficient_low = run_primary_condition(
        Family.NEEDS_FANOUT,
        repair_cost=LOW_REPAIR_COST,
    )
    insufficient_high = run_primary_condition(
        Family.NEEDS_FANOUT,
        repair_cost=HIGH_REPAIR_COST,
    )
    sufficient_low = run_primary_condition(
        Family.BASE_SUFFICIENT,
        repair_cost=LOW_REPAIR_COST,
    )
    novel_transfer = run_novel_family_transfer()

    assert len(READ_ONCE_PROGRAMS) == 94
    assert len(FANOUT_PROGRAMS) == 127

    assert exact_majority_read_once.accuracy == 0.875
    assert exact_majority_fanout.accuracy == 1.0
    assert exact_sufficient_read_once.accuracy == 1.0
    assert exact_xor_read_once.accuracy == 0.75
    assert exact_xor_fanout.accuracy == 1.0

    assert insufficient_low["repaired"] == "true"
    assert insufficient_low["transfer_accuracy_repaired_condition"] > 0.99
    assert insufficient_low["transfer_accuracy_fixed_control"] < 0.90

    assert insufficient_high["repaired"] == "false"
    assert sufficient_low["repaired"] == "false"
    assert sufficient_low["transfer_accuracy_repaired_condition"] > 0.99

    assert (
        insufficient_low["score_calls_repair"]
        == insufficient_low["score_calls_fixed"]
    )
    assert (
        insufficient_low["probe_labels_repair"]
        == insufficient_low["probe_labels_fixed"]
    )
    assert insufficient_low["goal_rule_mutated"] == "false"
    assert insufficient_low["authority_expanded"] == "false"

    assert novel_transfer["repaired_novel_transfer"] > 0.99
    assert novel_transfer["fixed_novel_transfer"] < 0.80

    return {
        "evaluator": {
            "read_once_program_count": float(len(READ_ONCE_PROGRAMS)),
            "fanout_program_count": float(len(FANOUT_PROGRAMS)),
            "majority_read_once_ceiling": exact_majority_read_once.accuracy,
            "majority_fanout_ceiling": exact_majority_fanout.accuracy,
            "sufficient_read_once_ceiling": exact_sufficient_read_once.accuracy,
            "xor_read_once_ceiling": exact_xor_read_once.accuracy,
            "xor_fanout_ceiling": exact_xor_fanout.accuracy,
        },
        "insufficient_low_cost": insufficient_low,
        "insufficient_high_cost": insufficient_high,
        "sufficient_low_cost": sufficient_low,
        "novel_family_transfer": novel_transfer,
    }


def main() -> None:
    results = run_experiment()
    for section, values in results.items():
        print(f"[{section}]")
        for key, value in values.items():
            if isinstance(value, float):
                print(f"{key}: {value:.4f}")
            else:
                print(f"{key}: {value}")
        print()


if __name__ == "__main__":
    main()
