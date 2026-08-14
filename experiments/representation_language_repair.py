"""Representation-language repair experiment.

The base grammar is finite and exhaustively searched. An expandable learner can
evaluate a small menu of one-step grammar extensions and activate one only when
its estimated future value exceeds an explicit expansion cost.

The learner never receives the true source-bit indices or the correct operator.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from itertools import combinations, product
from random import Random
from typing import Iterable


N_BITS = 14
SUFFICIENT_SOURCE = (3, 9)
INSUFFICIENT_SOURCE = (3, 9, 12)
FUTURE_HORIZON = 100
LOW_EXPANSION_COST = 10.0
HIGH_EXPANSION_COST = 60.0


class Task(str, Enum):
    BASE_SUFFICIENT = "base_sufficient"
    BASE_INSUFFICIENT = "base_insufficient"


class Op(str, Enum):
    ATOM = "atom"
    XOR2 = "xor2"
    AND2 = "and2"
    OR2 = "or2"
    XOR3 = "xor3"
    MAJORITY3 = "majority3"
    NOT = "not"
    NAND2 = "nand2"


class Extension(str, Enum):
    ADD_XOR3 = "add_xor3"
    ADD_MAJORITY3 = "add_majority3"
    ADD_NOT = "add_not"
    ADD_NAND2 = "add_nand2"


@dataclass(frozen=True)
class Expression:
    """Fixed-slot representation program.

    All programs reserve one operator slot and three index slots. Unused slots
    contain -1, so repaired and control policies have the same program storage
    allocation even when they use different operators.
    """

    op: Op
    i: int
    j: int = -1
    k: int = -1

    def evaluate(self, bits: tuple[int, ...]) -> int:
        left = bits[self.i]

        if self.op is Op.ATOM:
            return left
        if self.op is Op.NOT:
            return 1 - left

        right = bits[self.j]
        if self.op is Op.XOR2:
            return left ^ right
        if self.op is Op.AND2:
            return left & right
        if self.op is Op.OR2:
            return left | right
        if self.op is Op.NAND2:
            return 1 - (left & right)

        third = bits[self.k]
        if self.op is Op.XOR3:
            return left ^ right ^ third
        if self.op is Op.MAJORITY3:
            return int(left + right + third >= 2)

        raise ValueError(self.op)

    def __str__(self) -> str:
        if self.op in (Op.ATOM, Op.NOT):
            return f"{self.op.value}(b{self.i})"
        if self.op in (Op.XOR2, Op.AND2, Op.OR2, Op.NAND2):
            return f"{self.op.value}(b{self.i},b{self.j})"
        return f"{self.op.value}(b{self.i},b{self.j},b{self.k})"


@dataclass(frozen=True)
class Example:
    bits: tuple[int, ...]
    hidden: int
    code: int


@dataclass(frozen=True)
class SearchResult:
    accuracy: float
    expression: Expression
    mapping: tuple[int, int]


def hidden_from_bits(bits: tuple[int, ...], task: Task) -> int:
    if task is Task.BASE_SUFFICIENT:
        i, j = SUFFICIENT_SOURCE
        return bits[i] ^ bits[j]

    i, j, k = INSUFFICIENT_SOURCE
    return bits[i] ^ bits[j] ^ bits[k]


def bits_from_code(code: int) -> tuple[int, ...]:
    return tuple((code >> index) & 1 for index in range(N_BITS))


def make_examples(
    count: int,
    *,
    seed: int,
    task: Task,
    exclude_codes: set[int] | None = None,
) -> list[Example]:
    excluded = exclude_codes or set()
    pool = [code for code in range(1 << N_BITS) if code not in excluded]
    if count > len(pool):
        raise ValueError("requested more unique examples than available")

    rng = Random(seed)
    rng.shuffle(pool)
    selected = pool[:count]

    examples = []
    for code in selected:
        bits = bits_from_code(code)
        examples.append(
            Example(bits=bits, hidden=hidden_from_bits(bits, task), code=code)
        )
    return examples


def base_expressions() -> list[Expression]:
    expressions = [Expression(Op.ATOM, i) for i in range(N_BITS)]
    for i, j in combinations(range(N_BITS), 2):
        expressions.extend(
            (
                Expression(Op.XOR2, i, j),
                Expression(Op.AND2, i, j),
                Expression(Op.OR2, i, j),
            )
        )
    return expressions


def extension_expressions(extension: Extension) -> list[Expression]:
    if extension is Extension.ADD_XOR3:
        return [
            Expression(Op.XOR3, i, j, k)
            for i, j, k in combinations(range(N_BITS), 3)
        ]

    if extension is Extension.ADD_MAJORITY3:
        return [
            Expression(Op.MAJORITY3, i, j, k)
            for i, j, k in combinations(range(N_BITS), 3)
        ]

    if extension is Extension.ADD_NOT:
        return [Expression(Op.NOT, i) for i in range(N_BITS)]

    if extension is Extension.ADD_NAND2:
        return [
            Expression(Op.NAND2, i, j)
            for i, j in combinations(range(N_BITS), 2)
        ]

    raise ValueError(extension)


BASE_EXPRESSIONS = base_expressions()
EXTENSION_EXPRESSIONS = {
    extension: extension_expressions(extension) for extension in Extension
}
FULL_SEARCH_BUDGET = len(BASE_EXPRESSIONS) + sum(
    len(expressions) for expressions in EXTENSION_EXPRESSIONS.values()
)


def score_expression(
    expression: Expression,
    examples: Iterable[Example],
) -> tuple[float, tuple[int, int]]:
    """Fit the best binary mapping from expression output to hidden state."""

    counts = {0: [0, 0], 1: [0, 0]}
    examples = list(examples)

    for example in examples:
        value = expression.evaluate(example.bits)
        counts[value][example.hidden] += 1

    mapping = []
    correct = 0
    for value in (0, 1):
        count_0, count_1 = counts[value]
        predicted = 0 if count_0 >= count_1 else 1
        mapping.append(predicted)
        correct += max(count_0, count_1)

    return correct / len(examples), (mapping[0], mapping[1])


def exhaustive_search(
    expressions: Iterable[Expression],
    examples: Iterable[Example],
) -> tuple[SearchResult, int]:
    """Search every supplied expression; ties resolve lexicographically."""

    best: SearchResult | None = None
    calls = 0
    examples = list(examples)

    for expression in expressions:
        accuracy, mapping = score_expression(expression, examples)
        calls += 1
        candidate = SearchResult(accuracy, expression, mapping)

        if best is None:
            best = candidate
            continue

        if candidate.accuracy > best.accuracy:
            best = candidate
        elif (
            candidate.accuracy == best.accuracy
            and str(candidate.expression) < str(best.expression)
        ):
            best = candidate

    if best is None:
        raise ValueError("empty expression set")

    return best, calls


def transfer_accuracy(
    result: SearchResult,
    examples: Iterable[Example],
) -> float:
    examples = list(examples)
    correct = 0
    for example in examples:
        value = result.expression.evaluate(example.bits)
        predicted = result.mapping[value]
        correct += int(predicted == example.hidden)
    return correct / len(examples)


class ExpandableGrammarLearner:
    """Exhaust G0, then make a value-sensitive one-step grammar decision."""

    def __init__(self) -> None:
        self.base_result: SearchResult | None = None
        self.extension_result: SearchResult | None = None
        self.selected_result: SearchResult | None = None
        self.selected_extension: Extension | None = None
        self.best_extension: Extension | None = None
        self.score_calls = 0
        self.estimated_gross_value = 0.0

    def fit(
        self,
        examples: Iterable[Example],
        *,
        expansion_cost: float,
        future_horizon: int = FUTURE_HORIZON,
    ) -> None:
        examples = list(examples)

        base_result, calls = exhaustive_search(BASE_EXPRESSIONS, examples)
        self.score_calls += calls
        self.base_result = base_result

        best_extension_result: SearchResult | None = None
        best_extension: Extension | None = None

        for extension in Extension:
            result, calls = exhaustive_search(
                EXTENSION_EXPRESSIONS[extension],
                examples,
            )
            self.score_calls += calls

            if best_extension_result is None:
                best_extension_result = result
                best_extension = extension
                continue

            if result.accuracy > best_extension_result.accuracy:
                best_extension_result = result
                best_extension = extension
            elif (
                result.accuracy == best_extension_result.accuracy
                and extension.value < best_extension.value
            ):
                best_extension_result = result
                best_extension = extension

        if best_extension_result is None or best_extension is None:
            raise RuntimeError("extension menu is empty")

        self.best_extension = best_extension
        self.extension_result = best_extension_result

        gain = max(
            0.0,
            best_extension_result.accuracy - base_result.accuracy,
        )
        self.estimated_gross_value = future_horizon * gain

        if self.estimated_gross_value > expansion_cost:
            self.selected_extension = best_extension
            self.selected_result = best_extension_result
        else:
            self.selected_extension = None
            self.selected_result = base_result


class FixedGrammarControl:
    """Same labels and score-call budget, but no grammar-expansion ability."""

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
        result, calls = exhaustive_search(BASE_EXPRESSIONS, examples)
        self.score_calls += calls
        self.selected_result = result

        index = 0
        while self.score_calls < score_budget:
            expression = BASE_EXPRESSIONS[index % len(BASE_EXPRESSIONS)]
            score_expression(expression, examples)
            self.score_calls += 1
            index += 1

        if self.score_calls != score_budget:
            raise AssertionError("failed to match score-call budget")


def exact_language_ceiling(
    task: Task,
    expressions: Iterable[Expression],
) -> SearchResult:
    """Evaluator-only truth-table ceiling for a finite language."""

    truth_table = []
    for bits in product((0, 1), repeat=N_BITS):
        code = sum(bit << index for index, bit in enumerate(bits))
        truth_table.append(
            Example(
                bits=bits,
                hidden=hidden_from_bits(bits, task),
                code=code,
            )
        )

    result, _ = exhaustive_search(expressions, truth_table)
    return result


def run_condition(
    task: Task,
    *,
    expansion_cost: float,
) -> dict[str, float | str]:
    probe_examples = make_examples(
        3_000,
        seed=11,
        task=task,
    )
    probe_codes = {example.code for example in probe_examples}
    held_out = make_examples(
        3_000,
        seed=29,
        task=task,
        exclude_codes=probe_codes,
    )

    expandable = ExpandableGrammarLearner()
    expandable.fit(
        probe_examples,
        expansion_cost=expansion_cost,
    )

    fixed = FixedGrammarControl()
    fixed.fit(
        probe_examples,
        score_budget=expandable.score_calls,
    )

    if expandable.selected_result is None or fixed.selected_result is None:
        raise RuntimeError("learner not fitted")

    return {
        "task": task.value,
        "expansion_cost": expansion_cost,
        "base_empirical_accuracy": expandable.base_result.accuracy,
        "best_extension_empirical_accuracy": expandable.extension_result.accuracy,
        "estimated_gross_value": expandable.estimated_gross_value,
        "best_extension": expandable.best_extension.value,
        "expanded": str(expandable.selected_extension is not None).lower(),
        "selected_extension": (
            expandable.selected_extension.value
            if expandable.selected_extension is not None
            else "none"
        ),
        "selected_expression": str(expandable.selected_result.expression),
        "transfer_accuracy_expandable": transfer_accuracy(
            expandable.selected_result,
            held_out,
        ),
        "transfer_accuracy_fixed": transfer_accuracy(
            fixed.selected_result,
            held_out,
        ),
        "score_calls_expandable": float(expandable.score_calls),
        "score_calls_fixed": float(fixed.score_calls),
        "probe_labels_expandable": float(len(probe_examples)),
        "probe_labels_fixed": float(len(probe_examples)),
        "representation_capacity_expandable": 2.0,
        "representation_capacity_fixed": 2.0,
        "program_storage_slots_expandable": 4.0,
        "program_storage_slots_fixed": 4.0,
        "raw_configuration_overlap": 0.0,
    }


def run_experiment() -> dict[str, dict[str, float | str]]:
    base_ceiling_insufficient = exact_language_ceiling(
        Task.BASE_INSUFFICIENT,
        BASE_EXPRESSIONS,
    )
    expanded_ceiling_insufficient = exact_language_ceiling(
        Task.BASE_INSUFFICIENT,
        EXTENSION_EXPRESSIONS[Extension.ADD_XOR3],
    )
    base_ceiling_sufficient = exact_language_ceiling(
        Task.BASE_SUFFICIENT,
        BASE_EXPRESSIONS,
    )

    insufficient_low = run_condition(
        Task.BASE_INSUFFICIENT,
        expansion_cost=LOW_EXPANSION_COST,
    )
    insufficient_high = run_condition(
        Task.BASE_INSUFFICIENT,
        expansion_cost=HIGH_EXPANSION_COST,
    )
    sufficient_low = run_condition(
        Task.BASE_SUFFICIENT,
        expansion_cost=LOW_EXPANSION_COST,
    )

    assert base_ceiling_insufficient.accuracy == 0.5
    assert expanded_ceiling_insufficient.accuracy == 1.0
    assert base_ceiling_sufficient.accuracy == 1.0

    assert insufficient_low["selected_extension"] == Extension.ADD_XOR3.value
    assert insufficient_low["expanded"] == "true"
    assert insufficient_low["transfer_accuracy_expandable"] > 0.99
    assert insufficient_low["transfer_accuracy_fixed"] < 0.55

    assert insufficient_high["expanded"] == "false"
    assert insufficient_high["transfer_accuracy_expandable"] < 0.55

    assert sufficient_low["expanded"] == "false"
    assert sufficient_low["transfer_accuracy_expandable"] > 0.99

    assert (
        insufficient_low["score_calls_expandable"]
        == insufficient_low["score_calls_fixed"]
        == float(FULL_SEARCH_BUDGET)
    )
    assert (
        insufficient_low["probe_labels_expandable"]
        == insufficient_low["probe_labels_fixed"]
    )
    assert (
        insufficient_low["representation_capacity_expandable"]
        == insufficient_low["representation_capacity_fixed"]
    )
    assert (
        insufficient_low["program_storage_slots_expandable"]
        == insufficient_low["program_storage_slots_fixed"]
    )

    return {
        "evaluator": {
            "base_language_ceiling_insufficient": (
                base_ceiling_insufficient.accuracy
            ),
            "xor3_extension_ceiling_insufficient": (
                expanded_ceiling_insufficient.accuracy
            ),
            "base_language_ceiling_sufficient": base_ceiling_sufficient.accuracy,
        },
        "insufficient_low_cost": insufficient_low,
        "insufficient_high_cost": insufficient_high,
        "sufficient_low_cost": sufficient_low,
    }


if __name__ == "__main__":
    results = run_experiment()
    for section, values in results.items():
        print(f"[{section}]")
        for name, value in values.items():
            if isinstance(value, float):
                print(f"{name}: {value:.4f}")
            else:
                print(f"{name}: {value}")
        print()
