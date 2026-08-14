"""Meta-rule invention experiment (Experiment 008).

The learner starts with a read-once representation generator M0. It may
synthesize a new structural admissibility rule from count-state bits using only
NOT/AND/OR. Goal semantics and authority remain immutable.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product

HORIZON = 100
LOW_COST = 5.0
HIGH_COST = 20.0
MAX_META_NODES = 5
MAX_PROGRAM_NODES = 9


def rows(n: int) -> list[tuple[int, ...]]:
    return list(product((0, 1), repeat=n))


def var_tt(n: int, i: int) -> int:
    out = 0
    for k, r in enumerate(rows(n)):
        out |= r[i] << k
    return out


def mask(n: int) -> int:
    return (1 << (1 << n)) - 1


def synth_bool_programs(nvars: int, max_nodes: int, cap: int | None = None):
    """Return minimal programs, optionally limiting each variable occurrence."""

    vs = [var_tt(nvars, i) for i in range(nvars)]
    levels: dict[int, dict[tuple[int, tuple[int, ...]], str]] = defaultdict(dict)
    for i, tt in enumerate(vs):
        counts = tuple(int(j == i) for j in range(nvars))
        levels[1][(tt, counts)] = f"v{i}"

    for size in range(2, max_nodes + 1):
        for (tt, counts), expr in levels[size - 1].items():
            levels[size].setdefault(((~tt) & mask(nvars), counts), f"not({expr})")

        for ls in range(1, size - 1):
            rs = size - 1 - ls
            if rs < 1:
                continue
            for (lt, lc), le in levels[ls].items():
                for (rt, rc), re in levels[rs].items():
                    counts = tuple(a + b for a, b in zip(lc, rc))
                    if cap is not None and max(counts) > cap:
                        continue
                    for name, tt in (("and", lt & rt), ("or", lt | rt)):
                        levels[size].setdefault((tt, counts), f"{name}({le},{re})")

    best: dict[int, tuple[int, str, tuple[int, ...]]] = {}
    for size in range(1, max_nodes + 1):
        for (tt, counts), expr in levels[size].items():
            old = best.get(tt)
            candidate = (size, expr, counts)
            if old is None or candidate[:2] < old[:2]:
                best[tt] = candidate
    return best


def meta_programs():
    """Synthesize distinct rules over occurrence-counter bits lo/hi."""

    raw = synth_bool_programs(2, MAX_META_NODES)
    return {
        tt: (size, expr)
        for tt, (size, expr, _counts) in raw.items()
    }


META = meta_programs()


def meta_eval(tt: int, count: int) -> int:
    lo, hi = count & 1, (count >> 1) & 1
    index = rows(2).index((lo, hi))
    return (tt >> index) & 1


def occurrence_cap(rule_tt: int, maximum: int = 4) -> int:
    cap = 0
    while cap < maximum and meta_eval(rule_tt, cap):
        cap += 1
    return cap


def find_rule(target_bits: tuple[int, int, int, int]) -> int:
    target = sum(bit << i for i, bit in enumerate(target_bits))
    if target not in META:
        raise RuntimeError("required meta-rule is outside bounded meta-language")
    return target


M0_RULE = find_rule((1, 0, 0, 0))


def target_tt(name: str) -> tuple[int, int]:
    if name == "majority3":
        n = 3
        fn = lambda r: int(sum(r) >= 2)
    elif name == "xor2":
        n = 2
        fn = lambda r: r[0] ^ r[1]
    elif name == "mux3":
        n = 3
        fn = lambda r: r[1] if r[0] else r[2]
    elif name == "or2":
        n = 2
        fn = lambda r: r[0] | r[1]
    else:
        raise ValueError(name)

    tt = 0
    for i, r in enumerate(rows(n)):
        tt |= fn(r) << i
    return n, tt


def mapped_accuracy(expr_tt: int, target: int, n: int) -> float:
    """Best deterministic mapping from one representation bit to target label."""

    total = 1 << n
    best = 0
    for mapping in ((0, 0), (0, 1), (1, 0), (1, 1)):
        correct = 0
        for i in range(total):
            x = (expr_tt >> i) & 1
            y = (target >> i) & 1
            correct += int(mapping[x] == y)
        best = max(best, correct)
    return best / total


def best_semantic(name: str, cap: int):
    n, target = target_tt(name)
    language = synth_bool_programs(n, MAX_PROGRAM_NODES, cap=cap)
    scored = []
    for tt, (size, expr, _counts) in language.items():
        scored.append((mapped_accuracy(tt, target, n), -size, expr, tt))
    accuracy, neg_size, expr, tt = max(scored)
    return {
        "accuracy": accuracy,
        "expr": expr,
        "tt": tt,
        "language_size": len(language),
        "nodes": -neg_size,
    }


def admissible_meta_candidates():
    result = []
    for tt, (size, expr) in META.items():
        if meta_eval(tt, 0) != 1:
            continue
        cap = occurrence_cap(tt)
        if cap >= 1:
            result.append((tt, size, expr, cap))
    return result


class MetaLearner:
    def __init__(self):
        self.rule = M0_RULE
        self.base = None
        self.best = None
        self.value = 0.0
        self.repaired = False

    def analyze(self, relation: str):
        self.base = best_semantic(relation, occurrence_cap(M0_RULE))
        candidates = []
        for tt, size, expr, cap in admissible_meta_candidates():
            semantic = best_semantic(relation, cap)
            candidates.append(
                (
                    -semantic["accuracy"],
                    cap,
                    size,
                    expr,
                    tt,
                    semantic,
                )
            )
        candidates.sort()
        _neg_acc, cap, size, expr, tt, semantic = candidates[0]
        self.best = {
            "rule_tt": tt,
            "rule_expr": expr,
            "rule_nodes": size,
            "cap": cap,
            "semantic": semantic,
        }

    def decide(self, cost: float):
        gain = max(0.0, self.best["semantic"]["accuracy"] - self.base["accuracy"])
        self.value = HORIZON * gain
        if self.value > cost and self.best["rule_tt"] != M0_RULE:
            self.rule = self.best["rule_tt"]
            self.repaired = True

    def synthesize(self, relation: str):
        return best_semantic(relation, occurrence_cap(self.rule))


def run_condition(relation: str, cost: float):
    learner = MetaLearner()
    learner.analyze(relation)
    learner.decide(cost)
    selected = learner.synthesize(relation)
    fixed = best_semantic(relation, occurrence_cap(M0_RULE))
    return learner, selected, fixed


def run_experiment():
    exact = {
        "majority_M0": best_semantic("majority3", 1)["accuracy"],
        "majority_cap2": best_semantic("majority3", 2)["accuracy"],
        "xor_M0": best_semantic("xor2", 1)["accuracy"],
        "xor_cap2": best_semantic("xor2", 2)["accuracy"],
        "mux_M0": best_semantic("mux3", 1)["accuracy"],
        "mux_cap2": best_semantic("mux3", 2)["accuracy"],
    }

    low, majority_low, majority_fixed = run_condition("majority3", LOW_COST)
    high, majority_high, _ = run_condition("majority3", HIGH_COST)
    sufficient, or_selected, _ = run_condition("or2", LOW_COST)

    xor_repaired = low.synthesize("xor2")
    xor_fixed = best_semantic("xor2", 1)
    mux_repaired = low.synthesize("mux3")
    mux_fixed = best_semantic("mux3", 1)

    assert exact == {
        "majority_M0": 0.875,
        "majority_cap2": 1.0,
        "xor_M0": 0.75,
        "xor_cap2": 1.0,
        "mux_M0": 0.875,
        "mux_cap2": 1.0,
    }
    assert low.repaired and occurrence_cap(low.rule) == 2
    assert low.best["rule_expr"] == "not(v1)"
    assert majority_low["accuracy"] == 1.0
    assert majority_fixed["accuracy"] == 0.875
    assert not high.repaired and majority_high["accuracy"] == 0.875
    assert not sufficient.repaired and or_selected["accuracy"] == 1.0
    assert xor_repaired["accuracy"] == 1.0 and xor_fixed["accuracy"] == 0.75
    assert mux_repaired["accuracy"] == 1.0 and mux_fixed["accuracy"] == 0.875

    meta_candidates = len(admissible_meta_candidates())
    primary_budget = sum(
        best_semantic("majority3", cap)["language_size"]
        for _tt, _size, _expr, cap in admissible_meta_candidates()
    )

    return {
        "evaluator": {
            "meta_program_semantics": len(META),
            "admissible_meta_rules": meta_candidates,
            "M0_rule": META[M0_RULE][1],
            "M0_occurrence_cap": occurrence_cap(M0_RULE),
            **exact,
        },
        "majority_low_cost": {
            "base_accuracy": low.base["accuracy"],
            "best_meta_accuracy": low.best["semantic"]["accuracy"],
            "synthesized_meta_rule": low.best["rule_expr"].replace("v0", "lo").replace("v1", "hi"),
            "synthesized_occurrence_cap": low.best["cap"],
            "estimated_repair_value": low.value,
            "repair_cost": LOW_COST,
            "repaired": low.repaired,
            "transfer_repaired": majority_low["accuracy"],
            "transfer_fixed_M0": majority_fixed["accuracy"],
            "meta_rule_evaluations_each": meta_candidates,
            "semantic_score_budget_each": primary_budget,
            "goal_rule_mutated": False,
            "authority_expanded": False,
        },
        "majority_high_cost": {
            "estimated_repair_value": high.value,
            "repair_cost": HIGH_COST,
            "repaired": high.repaired,
            "transfer": majority_high["accuracy"],
        },
        "already_sufficient_low_cost": {
            "base_accuracy": sufficient.base["accuracy"],
            "estimated_repair_value": sufficient.value,
            "repaired": sufficient.repaired,
            "transfer": or_selected["accuracy"],
        },
        "generator_reuse_xor": {
            "repaired_generator": xor_repaired["accuracy"],
            "fixed_M0": xor_fixed["accuracy"],
            "matched_score_budget_each": max(
                xor_repaired["language_size"], xor_fixed["language_size"]
            ),
        },
        "generator_reuse_mux": {
            "repaired_generator": mux_repaired["accuracy"],
            "fixed_M0": mux_fixed["accuracy"],
            "matched_score_budget_each": max(
                mux_repaired["language_size"], mux_fixed["language_size"]
            ),
        },
    }


if __name__ == "__main__":
    report = run_experiment()
    for section, values in report.items():
        print(f"[{section}]")
        for key, value in values.items():
            if isinstance(value, float):
                print(f"{key}: {value:.4f}")
            else:
                print(f"{key}: {value}")
        print()
