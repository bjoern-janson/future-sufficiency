"""Anti-limit-relaxation audit for the 001-008 future-sufficiency ladder.

This is not Experiment 009. It tests whether repair identity is diagnosed from
failure structure rather than selected by residual-error magnitude or a generic
"relax the current scalar limit" heuristic.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product

N_VARS = 3
MAX_NODES = 9
HORIZON = 100
REPAIR_COST = 5.0
REPEATS_PER_ROW = 8


def rows(n: int = N_VARS) -> tuple[tuple[int, ...], ...]:
    return tuple(product((0, 1), repeat=n))


def truth_table(fn, n: int = N_VARS) -> int:
    return sum(int(fn(r)) << i for i, r in enumerate(rows(n)))


def bit(tt: int, index: int) -> int:
    return (tt >> index) & 1


MAJORITY3 = truth_table(lambda r: sum(r) >= 2)
ALL_EQUAL3 = truth_table(lambda r: r[0] == r[1] == r[2])
OR3 = truth_table(lambda r: r[0] or r[1] or r[2])


@dataclass(frozen=True)
class Program:
    tt: int
    expr: str
    size: int
    counts: tuple[int, ...]


def build_language(*, occurrence_cap: int, max_nodes: int) -> dict[int, Program]:
    """Enumerate minimal read-once/reuse-limited NOT/AND/OR semantics."""
    levels: dict[int, dict[tuple[int, tuple[int, ...]], Program]] = {}
    levels[1] = {}
    full_mask = (1 << (1 << N_VARS)) - 1

    for j in range(N_VARS):
        tt = truth_table(lambda r, j=j: r[j])
        counts = tuple(int(k == j) for k in range(N_VARS))
        levels[1][(tt, counts)] = Program(tt, f"v{j}", 1, counts)

    for size in range(2, max_nodes + 1):
        here: dict[tuple[int, tuple[int, ...]], Program] = {}

        for (tt, counts), program in levels.get(size - 1, {}).items():
            candidate = Program((~tt) & full_mask, f"not({program.expr})", size, counts)
            here.setdefault((candidate.tt, counts), candidate)

        for left_size in range(1, size - 1):
            right_size = size - 1 - left_size
            if right_size < 1:
                continue
            for (_lt, lc), left in levels.get(left_size, {}).items():
                for (_rt, rc), right in levels.get(right_size, {}).items():
                    counts = tuple(a + b for a, b in zip(lc, rc))
                    if max(counts) > occurrence_cap:
                        continue
                    for name, tt in (
                        ("and", left.tt & right.tt),
                        ("or", left.tt | right.tt),
                    ):
                        candidate = Program(
                            tt,
                            f"{name}({left.expr},{right.expr})",
                            size,
                            counts,
                        )
                        here.setdefault((tt, counts), candidate)
        levels[size] = here

    best: dict[int, Program] = {}
    for size in range(1, max_nodes + 1):
        for (tt, _counts), program in levels.get(size, {}).items():
            old = best.get(tt)
            if old is None or (program.size, program.expr) < (old.size, old.expr):
                best[tt] = program
    return best


BASE = build_language(occurrence_cap=1, max_nodes=MAX_NODES)
REUSE = build_language(occurrence_cap=2, max_nodes=MAX_NODES)
SCALAR_CAPS = {
    cap: build_language(occurrence_cap=cap, max_nodes=MAX_NODES)
    for cap in (1, 2, 3, 4)
}
SCALAR_NODE_BUDGETS = {
    nodes: build_language(occurrence_cap=1, max_nodes=nodes)
    for nodes in (9, 11, 13, 15)
}

# Operator-family repair: the generator receives a reusable equality primitive.
EQ3_PROGRAM = Program(ALL_EQUAL3, "eq3(v0,v1,v2)", 1, (1, 1, 1))
OPERATOR_FAMILY = dict(BASE)
OPERATOR_FAMILY[ALL_EQUAL3] = EQ3_PROGRAM


@dataclass(frozen=True)
class Example:
    row_index: int
    label: int
    surface_id: int


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


def make_dataset(case: str, *, heldout: bool) -> list[Example]:
    result: list[Example] = []
    offset = 10_000 if heldout else 0
    if case == "reuse":
        target = MAJORITY3
    elif case == "operator":
        target = ALL_EQUAL3
    elif case == "null":
        target = OR3
    else:
        raise ValueError(case)

    for row_index in range(1 << N_VARS):
        true_label = bit(target, row_index)
        for rep in range(REPEATS_PER_ROW):
            label = true_label
            # Exactly one contradictory label per input row: irreducible 1/8 noise.
            if case == "null" and rep == (1 if heldout else 0):
                label = 1 - label
            result.append(
                Example(
                    row_index=row_index,
                    label=label,
                    surface_id=offset + row_index * REPEATS_PER_ROW + rep,
                )
            )
    return result


def score_program(program: Program, examples: list[Example], meter: Meter) -> float:
    meter.candidate_evaluations += 1
    correct = 0
    for example in examples:
        meter.executions += 1
        correct += bit(program.tt, example.row_index) == example.label
    return correct / len(examples)


def best_in_language(language: dict[int, Program], examples: list[Example], meter: Meter):
    best = None
    for program in language.values():
        accuracy = score_program(program, examples, meter)
        candidate = (accuracy, -program.size, program.expr, program)
        if best is None or candidate[:3] > best[:3]:
            best = candidate
    if best is None:
        raise RuntimeError("empty language")
    return best[0], best[3]


REPAIR_LANGUAGES = {
    "keep": BASE,
    "reuse": REUSE,
    "operator_family": OPERATOR_FAMILY,
}


@dataclass(frozen=True)
class Diagnosis:
    base_accuracy: float
    best_accuracy: float
    repair: str
    estimated_value: float


class RepairPolicy:
    def __init__(self, *, mutation_allowed: bool):
        self.mutation_allowed = mutation_allowed
        self.bound_repair = "keep"

    def diagnose(self, probes: list[Example], meter: Meter) -> Diagnosis:
        meter.probes += len(probes)
        # The probe set itself is stored once in both branches.
        meter.memory_cells = max(meter.memory_cells, len(probes) * 2)
        # Both branches reserve identical slots: current generator + one repair binding.
        meter.storage_slots = 2

        results = {}
        for repair, language in REPAIR_LANGUAGES.items():
            accuracy, _program = best_in_language(language, probes, meter)
            results[repair] = accuracy

        base = results["keep"]
        ranked = sorted(
            (
                -(HORIZON * max(0.0, accuracy - base) - (0.0 if repair == "keep" else REPAIR_COST)),
                repair,
                accuracy,
            )
            for repair, accuracy in results.items()
        )
        _neg_net, repair, best_accuracy = ranked[0]
        gross_value = HORIZON * max(0.0, best_accuracy - base)
        if gross_value <= REPAIR_COST:
            repair = "keep"
            best_accuracy = base
            gross_value = 0.0

        if self.mutation_allowed:
            self.bound_repair = repair
        else:
            self.bound_repair = "keep"

        return Diagnosis(base, best_accuracy, repair, gross_value)

    def evaluate(self, heldout: list[Example], meter: Meter) -> float:
        # Both mutable and fixed branches score every repair language on held-out
        # data. Only the persistent binding determines which score is acted on.
        scores = {}
        for repair, language in REPAIR_LANGUAGES.items():
            accuracy, _program = best_in_language(language, heldout, meter)
            scores[repair] = accuracy
        return scores[self.bound_repair]


def exact_ceiling(language: dict[int, Program], target: int) -> float:
    return max(
        sum(bit(program.tt, i) == bit(target, i) for i in range(1 << N_VARS))
        / (1 << N_VARS)
        for program in language.values()
    )


def scalar_relaxation_audit() -> dict[str, float]:
    result = {}
    for cap, language in SCALAR_CAPS.items():
        result[f"all_equal_cap_{cap}"] = exact_ceiling(language, ALL_EQUAL3)
    for nodes, language in SCALAR_NODE_BUDGETS.items():
        result[f"all_equal_nodes_{nodes}"] = exact_ceiling(language, ALL_EQUAL3)
    return result


def run_case(case: str):
    probes = make_dataset(case, heldout=False)
    heldout = make_dataset(case, heldout=True)

    mutable_meter = Meter()
    fixed_meter = Meter()
    mutable = RepairPolicy(mutation_allowed=True)
    fixed = RepairPolicy(mutation_allowed=False)

    mutable_diagnosis = mutable.diagnose(probes, mutable_meter)
    fixed_diagnosis = fixed.diagnose(probes, fixed_meter)

    mutable_accuracy = mutable.evaluate(heldout, mutable_meter)
    fixed_accuracy = fixed.evaluate(heldout, fixed_meter)

    assert mutable_meter.snapshot() == fixed_meter.snapshot()
    assert mutable_diagnosis == fixed_diagnosis

    return {
        "base_probe_error": 1.0 - mutable_diagnosis.base_accuracy,
        "diagnosed_repair": mutable_diagnosis.repair,
        "estimated_repair_value": mutable_diagnosis.estimated_value,
        "mutable_heldout_accuracy": mutable_accuracy,
        "fixed_heldout_accuracy": fixed_accuracy,
        "probe_count_each": mutable_meter.probes,
        "candidate_count_each": mutable_meter.candidate_evaluations,
        "execution_count_each": mutable_meter.executions,
        "memory_cells_each": mutable_meter.memory_cells,
        "storage_slots_each": mutable_meter.storage_slots,
    }


def run_audit():
    # Exact matched base error for the three cases.
    assert exact_ceiling(BASE, MAJORITY3) == 0.875
    assert exact_ceiling(BASE, ALL_EQUAL3) == 0.875
    assert exact_ceiling(REUSE, MAJORITY3) == 1.0
    assert exact_ceiling(REUSE, ALL_EQUAL3) == 0.875
    assert exact_ceiling(OPERATOR_FAMILY, ALL_EQUAL3) == 1.0
    assert exact_ceiling(OPERATOR_FAMILY, MAJORITY3) == 0.875

    scalar = scalar_relaxation_audit()
    assert all(value == 0.875 for value in scalar.values())

    reuse = run_case("reuse")
    operator = run_case("operator")
    null = run_case("null")

    assert reuse["base_probe_error"] == operator["base_probe_error"] == null["base_probe_error"] == 0.125
    assert reuse["diagnosed_repair"] == "reuse"
    assert operator["diagnosed_repair"] == "operator_family"
    assert null["diagnosed_repair"] == "keep"
    assert reuse["mutable_heldout_accuracy"] == 1.0
    assert operator["mutable_heldout_accuracy"] == 1.0
    assert null["mutable_heldout_accuracy"] == 0.875
    assert reuse["fixed_heldout_accuracy"] == operator["fixed_heldout_accuracy"] == null["fixed_heldout_accuracy"] == 0.875

    # Mechanical budget equality across mutable/fixed branches and task cases.
    budget_keys = (
        "probe_count_each",
        "candidate_count_each",
        "execution_count_each",
        "memory_cells_each",
        "storage_slots_each",
    )
    for key in budget_keys:
        assert reuse[key] == operator[key] == null[key]

    return {
        "matched_error_triage": {
            "reuse_case_error": reuse["base_probe_error"],
            "operator_case_error": operator["base_probe_error"],
            "null_case_error": null["base_probe_error"],
            "reuse_case_repair": reuse["diagnosed_repair"],
            "operator_case_repair": operator["diagnosed_repair"],
            "null_case_repair": null["diagnosed_repair"],
        },
        "heldout_consequence": {
            "reuse_mutable": reuse["mutable_heldout_accuracy"],
            "reuse_fixed": reuse["fixed_heldout_accuracy"],
            "operator_mutable": operator["mutable_heldout_accuracy"],
            "operator_fixed": operator["fixed_heldout_accuracy"],
            "null_mutable": null["mutable_heldout_accuracy"],
            "null_fixed": null["fixed_heldout_accuracy"],
        },
        "anti_scalar_relaxation": scalar,
        "mechanical_budget_audit": {
            key: reuse[key] for key in budget_keys
        },
        "governance": {
            "goal_rule_mutated": False,
            "authority_expanded": False,
        },
    }


if __name__ == "__main__":
    for section, values in run_audit().items():
        print(f"[{section}]")
        for key, value in values.items():
            if isinstance(value, float):
                print(f"{key}: {value:.4f}")
            else:
                print(f"{key}: {value}")
        print()
