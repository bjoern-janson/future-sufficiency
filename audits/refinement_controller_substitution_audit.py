"""Controller substitution over the validated reachable-refinement geometry.

Primary intervention only: DP -> reachability-pruning controller.
STOP remains primitive. Geometry, target, costs, value, budget, and tau are frozen.
"""

from collections import Counter, defaultdict
from functools import lru_cache

from reachable_refinement_discriminant_audit import (
    A, B, C, CONDITIONS, ENCODINGS, PROBES, PROBE_BUDGET, PROBE_COST,
    COMMITMENT_TAU, WORLDS, make_encoding, warranted_action,
)

BASELINE_GEOMETRY = "fadf50368d13d80ed06c5da1ff7fd0cc628b2690"
V = 10.0
STOP = "STOP"


def observe(enc, world, p):
    c = enc.observed_to_canonical[p]
    return world[c] ^ enc.polarity_flips[p]


def acc(worlds):
    c = Counter(warranted_action(w) for w in worlds)
    return max(c.values()) / len(worlds)


def action(worlds):
    c = Counter(warranted_action(w) for w in worlds)
    m = max(c.values())
    return min(a for a, n in c.items() if n == m)


def groups(enc, worlds, p):
    out = defaultdict(list)
    for w in worlds:
        out[observe(enc, w, p)].append(w)
    return {o: tuple(ws) for o, ws in out.items()}


def geometry(condition, enc, history):
    used = {p for p, _ in history}
    remaining = set(PROBES) - used
    if not history:
        return {p: 1 for p in remaining}
    if len(history) >= PROBE_BUDGET:
        return {}
    first, outcome = history[0]
    first_c = enc.observed_to_canonical[first]
    if first_c != 0:
        return {p: 1 for p in remaining}
    selector = outcome ^ enc.polarity_flips[first]
    correct = 1 if selector == 0 else 2
    wrong = 2 if selector == 0 else 1
    c2o = enc.canonical_to_observed
    if condition == A:
        return {c2o[correct]: 1}
    if condition == B:
        return {c2o[correct]: 2}
    if condition == C:
        return {c2o[wrong]: 1}
    raise ValueError(condition)


def timely(condition, enc, history, t):
    if len(history) >= PROBE_BUDGET:
        return {}
    return {p: dt for p, dt in geometry(condition, enc, history).items()
            if t + dt <= COMMITMENT_TAU}


def stop_value(worlds):
    return V * acc(worlds)


def make_dp(condition, enc):
    @lru_cache(None)
    def solve(worlds, history, t):
        worlds, history = tuple(worlds), tuple(history)
        vals = {STOP: stop_value(worlds)}
        for p, dt in timely(condition, enc, history, t).items():
            q = -PROBE_COST
            for o, ws in groups(enc, worlds, p).items():
                q += len(ws) / len(worlds) * solve(
                    ws, history + ((p, o),), t + dt
                )[0]
            vals[p] = q
        best = max(vals.values())
        opts = tuple(k for k, v in vals.items() if abs(v - best) < 1e-12)
        choice = STOP if STOP in opts else min(opts)
        return best, opts, choice
    return solve


def make_can_correct(condition, enc):
    @lru_cache(None)
    def can(worlds, history, t):
        worlds, history = tuple(worlds), tuple(history)
        if len({warranted_action(w) for w in worlds}) == 1:
            return True
        for p, dt in timely(condition, enc, history, t).items():
            if all(can(ws, history + ((p, o),), t + dt)
                   for o, ws in groups(enc, worlds, p).items()):
                return True
        return False
    return can


def one_step(condition, enc, worlds, history, t):
    vals = {STOP: stop_value(worlds)}
    for p in timely(condition, enc, history, t):
        vals[p] = -PROBE_COST + sum(
            len(ws) / len(worlds) * stop_value(ws)
            for ws in groups(enc, worlds, p).values()
        )
    return vals


def choose_best(vals):
    best = max(vals.values())
    opts = tuple(k for k, v in vals.items() if abs(v - best) < 1e-12)
    return (STOP if STOP in opts else min(opts)), opts


def make_prune(condition, enc):
    can = make_can_correct(condition, enc)
    def choose(worlds, history, t):
        preserving, rejected = [], []
        for p, dt in sorted(timely(condition, enc, history, t).items()):
            ok = all(can(ws, history + ((p, o),), t + dt)
                     for o, ws in groups(enc, worlds, p).items())
            (preserving if ok else rejected).append(p)
        if preserving:
            return min(preserving), ("reachability", tuple(preserving), tuple(rejected))
        vals = one_step(condition, enc, worlds, history, t)
        choice, opts = choose_best(vals)
        return choice, ("fallback", opts, vals)
    return choose


def make_myopic(condition, enc):
    def choose(worlds, history, t):
        vals = one_step(condition, enc, worlds, history, t)
        choice, opts = choose_best(vals)
        return choice, ("myopic", opts, vals)
    return choose


def run(condition, enc, chooser):
    correct = probes = prune_points = pruned = 0
    decisions = []
    for true_world in WORLDS:
        worlds, history, t, n = WORLDS, tuple(), 0, 0
        while True:
            choice, meta = chooser(worlds, history, t)
            decisions.append((worlds, history, t, choice))
            if meta[0] == "reachability":
                prune_points += 1
                pruned += len(meta[2])
            if choice == STOP:
                pred = action(worlds)
                break
            dt = geometry(condition, enc, history)[choice]
            o = observe(enc, true_world, choice)
            worlds = tuple(w for w in worlds if observe(enc, w, choice) == o)
            history += ((choice, o),)
            t += dt
            n += 1
            assert n <= PROBE_BUDGET and t <= COMMITMENT_TAU
        correct += pred == warranted_action(true_world)
        probes += n
    accuracy = correct / len(WORLDS)
    mean_probes = probes / len(WORLDS)
    return {
        "accuracy": accuracy,
        "mean_probes": mean_probes,
        "mean_cost": mean_probes * PROBE_COST,
        "utility": V * accuracy - mean_probes * PROBE_COST,
        "decisions": decisions,
        "prune_points": prune_points,
        "pruned": pruned,
    }


def audit():
    rows = {c: [] for c in CONDITIONS}
    total_points = mismatches = 0
    a_root = None
    for seed in range(ENCODINGS):
        enc = make_encoding(seed)
        for condition in CONDITIONS:
            dp = make_dp(condition, enc)
            def dp_choose(worlds, history, t):
                _v, opts, choice = dp(tuple(worlds), tuple(history), t)
                return choice, ("dp", opts)
            d = run(condition, enc, dp_choose)
            p = run(condition, enc, make_prune(condition, enc))
            m = run(condition, enc, make_myopic(condition, enc))
            for key in ("accuracy", "mean_probes", "mean_cost", "utility"):
                assert abs(d[key] - p[key]) < 1e-12
            for worlds, history, t, choice in p["decisions"]:
                total_points += 1
                if choice not in dp(tuple(worlds), tuple(history), t)[1]:
                    mismatches += 1
            assert mismatches == 0
            rows[condition].append((d, p, m))
            if condition == A and seed == 0:
                raw = one_step(condition, enc, WORLDS, tuple(), 0)
                a_root = {STOP: raw[STOP]}
                for p0, v0 in raw.items():
                    if p0 != STOP:
                        a_root[enc.observed_to_canonical[p0]] = v0
    expected = {
        A: (1.0, 2.0, 8.0),
        B: (0.75, 1.0, 6.5),
        C: (0.75, 1.0, 6.5),
    }
    out = {}
    for condition, triples in rows.items():
        d0, p0, m0 = triples[0]
        exp_acc, exp_n, exp_u = expected[condition]
        assert all(abs(p["accuracy"] - exp_acc) < 1e-12 and
                   abs(p["mean_probes"] - exp_n) < 1e-12 and
                   abs(p["utility"] - exp_u) < 1e-12
                   for _d, p, _m in triples)
        out[condition] = {
            "dp": (d0["accuracy"], d0["mean_probes"], d0["utility"]),
            "prune": (p0["accuracy"], p0["mean_probes"], p0["utility"]),
            "myopic": (m0["accuracy"], m0["mean_probes"], m0["utility"]),
            "prune_points": sum(p["prune_points"] for _d, p, _m in triples),
            "pruned_actions": sum(p["pruned"] for _d, p, _m in triples),
        }
    assert out[A]["myopic"] == (0.75, 1.0, 6.5)
    assert a_root == {STOP: 5.0, 0: 4.0, 1: 6.5, 2: 6.5}
    return {
        "baseline_geometry": BASELINE_GEOMETRY,
        "encodings": ENCODINGS,
        "conditions": out,
        "visited_decision_points": total_points,
        "prune_actions_outside_dp_optimal_set": mismatches,
        "A_root_one_step_values": a_root,
        "stop_primitive_changed": False,
    }


if __name__ == "__main__":
    r = audit()
    print("Refinement Controller Substitution Audit")
    print("baseline:", r["baseline_geometry"])
    for c in CONDITIONS:
        x = r["conditions"][c]
        print(c, "DP", x["dp"], "prune", x["prune"], "myopic", x["myopic"])
    print("visited decision points:", r["visited_decision_points"])
    print("prune actions outside DP-optimal set:", r["prune_actions_outside_dp_optimal_set"])
    print("A root one-step values:", r["A_root_one_step_values"])
