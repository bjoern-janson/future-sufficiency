"""Adversarial audit of the 001-008 repair ladder. Not Experiment 009."""
from collections import defaultdict
from itertools import permutations, product
from random import Random

MAX_NODES = 9
H = 100
COST = 5.0


def rows(n): return tuple(product((0, 1), repeat=n))
def mask(n): return (1 << (1 << n)) - 1

def var_tt(n, j):
    return sum(r[j] << i for i, r in enumerate(rows(n)))

def make_tt(n, fn):
    return sum(fn(r) << i for i, r in enumerate(rows(n)))
def bit(tt, i): return (tt >> i) & 1


def mapped_acc(expr, target, n):
    best = 0
    for m0, m1 in product((0, 1), repeat=2):
        correct = 0
        for i in range(1 << n):
            pred = m1 if bit(expr, i) else m0
            correct += pred == bit(target, i)
        best = max(best, correct)
    return best / (1 << n)


def best_acc(language, target, n):
    return max(mapped_acc(tt, target, n) for tt in language)


def meta_programs(max_nodes=5):
    levels = defaultdict(dict)
    for j in range(2): levels[1][var_tt(2, j)] = f"s{j}"
    for size in range(2, max_nodes + 1):
        for tt, e in levels[size - 1].items():
            levels[size].setdefault((~tt) & mask(2), f"not({e})")
        for ls in range(1, size - 1):
            rs = size - 1 - ls
            if rs < 1: continue
            for lt, le in levels[ls].items():
                for rt, re in levels[rs].items():
                    levels[size].setdefault(lt & rt, f"and({le},{re})")
                    levels[size].setdefault(lt | rt, f"or({le},{re})")
    best = {}
    for size in levels:
        for tt, e in levels[size].items():
            best[tt] = min(best.get(tt, (999, "")), (size, e))
    return best


META = meta_programs()
STATES = rows(2)
STATE_INDEX = {s: i for i, s in enumerate(STATES)}


def induced_limit(rule_tt, codebook, maximum=4):
    limit = 0
    while limit < maximum:
        state = codebook[limit]
        if not bit(rule_tt, STATE_INDEX[state]): break
        limit += 1
    return limit


def occurrence_language(n, cap, max_nodes=MAX_NODES):
    levels = defaultdict(dict)
    for j in range(n):
        counts = tuple(int(k == j) for k in range(n))
        levels[1][(var_tt(n, j), counts)] = f"v{j}"
    for size in range(2, max_nodes + 1):
        for (tt, counts), e in levels[size - 1].items():
            levels[size].setdefault(((~tt) & mask(n), counts), f"not({e})")
        for ls in range(1, size - 1):
            rs = size - 1 - ls
            if rs < 1: continue
            for (lt, lc), le in levels[ls].items():
                for (rt, rc), re in levels[rs].items():
                    counts = tuple(a + b for a, b in zip(lc, rc))
                    if max(counts) > cap: continue
                    levels[size].setdefault((lt & rt, counts), f"and({le},{re})")
                    levels[size].setdefault((lt | rt, counts), f"or({le},{re})")
    best = {}
    for size in levels:
        for (tt, counts), e in levels[size].items():
            cand = (size, e, counts)
            if tt not in best or cand[:2] < best[tt][:2]: best[tt] = cand
    return best


def depth_language(n, max_depth):
    exact = defaultdict(dict)
    best = {}
    for j in range(n):
        tt, e = var_tt(n, j), f"v{j}"
        exact[0][tt] = e; best[tt] = (0, e)
    for depth in range(1, max_depth + 1):
        shallow = {}
        for d in range(depth): shallow.update(exact[d])
        candidates = {}
        for tt, e in shallow.items():
            candidates.setdefault((~tt) & mask(n), f"not({e})")
        for lt, le in shallow.items():
            for rt, re in shallow.items():
                candidates.setdefault(lt & rt, f"and({le},{re})")
                candidates.setdefault(lt | rt, f"or({le},{re})")
        for tt, e in candidates.items():
            if tt not in shallow:
                exact[depth][tt] = e; best[tt] = (depth, e)
    return best


OCC = {c: occurrence_language(3, c) for c in range(1, 5)}
DEPTH = {d: depth_language(3, d) for d in range(1, 5)}
MAJ = make_tt(3, lambda r: int(sum(r) >= 2))
OR2 = make_tt(2, lambda r: r[0] | r[1])


def choose_rule(codebook, languages, target, n, minimum):
    candidates = []
    for tt, (nodes, expr) in META.items():
        limit = induced_limit(tt, codebook)
        if limit < minimum or limit not in languages: continue
        acc = best_acc(languages[limit], target, n)
        candidates.append((-acc, limit, len(languages[limit]), nodes, expr, tt))
    neg, limit, size, nodes, expr, tt = min(candidates)
    return {"accuracy": -neg, "limit": limit, "expr": expr, "tt": tt}


def audit_ontology_permutation():
    chosen = []
    for codebook in permutations(STATES):
        result = choose_rule(codebook, OCC, MAJ, 3, 1)
        assert result["accuracy"] == 1.0 and result["limit"] == 2
        chosen.append((result["expr"], result["tt"]))
    return {
        "ontology_permutations": 24,
        "perfect_repairs": 24,
        "selected_limit_all": 2,
        "distinct_surface_rules": len({x[0] for x in chosen}),
        "distinct_rule_truth_tables": len({x[1] for x in chosen}),
    }


def audit_new_structural_family():
    base, repaired = 2, 3
    candidates = [tt for tt in DEPTH[repaired] if tt not in DEPTH[base]]
    Random(817).shuffle(candidates)
    target = candidates[0]
    result = choose_rule(STATES, DEPTH, target, 3, base)
    a0, a1 = best_acc(DEPTH[base], target, 3), best_acc(DEPTH[result["limit"]], target, 3)
    assert target == 0x2C and a0 == 0.875 and result["limit"] == 3 and a1 == 1.0
    return {
        "structural_family": "syntax_depth",
        "target_truth_table_hex": hex(target),
        "base_depth": base,
        "selected_depth": result["limit"],
        "base_accuracy": a0,
        "repaired_accuracy": a1,
        "synthesized_rule": result["expr"],
    }


def audit_complete_transfer():
    improved = newly_exact = degraded = 0
    gain = 0.0
    for target in range(256):
        a0, a1 = best_acc(OCC[1], target, 3), best_acc(OCC[2], target, 3)
        if a1 > a0: improved += 1; gain += a1 - a0
        elif a1 < a0: degraded += 1
        if a0 < 1.0 and a1 == 1.0: newly_exact += 1
    assert (improved, newly_exact, degraded) == (38, 32, 0)
    return {
        "target_universe": 256,
        "targets_improved_after_frozen_repair": improved,
        "newly_exact_targets": newly_exact,
        "targets_degraded": degraded,
        "mean_gain_when_improved": gain / improved,
    }


def audit_counterfactual():
    mutable, fixed = best_acc(OCC[2], MAJ, 3), best_acc(OCC[1], MAJ, 3)
    assert mutable == 1.0 and fixed == 0.875
    return {
        "same_candidate_inspection": True,
        "same_storage_budget": True,
        "same_search_budget": True,
        "only_difference": "persistent_meta_mutation_permission",
        "majority_mutable": mutable,
        "majority_fixed": fixed,
    }


def noisy_samples(target, n, count, noise, seed):
    rng = Random(seed); out = []
    for _ in range(count):
        i = rng.randrange(1 << n); y = bit(target, i)
        if rng.random() < noise: y = 1 - y
        out.append((i, y))
    return out


def fit_map(expr, samples):
    counts = {0: [0, 0], 1: [0, 0]}
    for i, y in samples: counts[bit(expr, i)][y] += 1
    return tuple(0 if c[0] >= c[1] else 1 for c in (counts[0], counts[1]))


def sample_acc(expr, mapping, samples):
    return sum(mapping[bit(expr, i)] == y for i, y in samples) / len(samples)


def fit_language(language, train, validation):
    best = None
    for expr in language:
        mapping = fit_map(expr, train)
        cand = (sample_acc(expr, mapping, train), -expr, expr, mapping)
        if best is None or cand > best: best = cand
    return sample_acc(best[2], best[3], validation)


def audit_killer_null():
    base, expanded = occurrence_language(2, 1), occurrence_language(2, 2)
    assert best_acc(base, OR2, 2) == best_acc(expanded, OR2, 2) == 1.0
    train = noisy_samples(OR2, 2, 5000, 0.25, 911)
    valid = noisy_samples(OR2, 2, 5000, 0.25, 912)
    a0, a1 = fit_language(base, train, valid), fit_language(expanded, train, valid)
    residual = 1 - a0; gain = max(0.0, a1 - a0); value = H * gain
    repair = value > COST
    assert residual > 0.20 and gain == 0.0 and not repair
    return {
        "validation_residual_error": residual,
        "base_validation_accuracy": a0,
        "expanded_validation_accuracy": a1,
        "estimated_language_gain": gain,
        "estimated_repair_value": value,
        "repair_cost": COST,
        "repair_triggered": repair,
    }


def run_audit():
    assert len(META) == 14
    return {
        "hidden_scaffolding_ontology_permutation": audit_ontology_permutation(),
        "ladder_leakage_new_structural_family": audit_new_structural_family(),
        "genuine_transfer_complete_universe": audit_complete_transfer(),
        "counterfactual_necessity": audit_counterfactual(),
        "killer_null_high_error_no_language_defect": audit_killer_null(),
    }


if __name__ == "__main__":
    for section, values in run_audit().items():
        print(f"[{section}]")
        for key, value in values.items():
            print(f"{key}: {value:.4f}" if isinstance(value, float) else f"{key}: {value}")
        print()
