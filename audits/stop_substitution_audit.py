"""STOP substitution over the validated reachable-refinement controller.

Primary intervention only: primitive STOP action -> derived termination.
Geometry, target, costs, value, budget, tau, and pruning controller role are frozen.
"""

from refinement_controller_substitution_audit import (
    A, B, C, CONDITIONS, ENCODINGS, PROBES, PROBE_BUDGET, PROBE_COST,
    COMMITMENT_TAU, WORLDS, make_encoding, warranted_action, V, STOP,
    observe, action, groups, geometry, timely, stop_value,
    make_can_correct, make_prune, run as run_primitive,
)

BASELINE_CONTROLLER = "68f2338b5a903efdd77555dea372620655aec201"
EPS = 1e-12


def probe_values(condition, enc, worlds, history, t):
    """Frozen one-step acquisition utility, excluding any STOP action."""
    values = {}
    for p in timely(condition, enc, history, t):
        values[p] = -PROBE_COST + sum(
            len(ws) / len(worlds) * stop_value(ws)
            for ws in groups(enc, worlds, p).values()
        )
    return values


def preserving_probes(condition, enc, worlds, history, t, can_correct):
    """Probes whose every outcome branch retains exact timely correction reachability."""
    preserving = []
    for p, dt in sorted(timely(condition, enc, history, t).items()):
        ok = all(
            can_correct(ws, history + ((p, outcome),), t + dt)
            for outcome, ws in groups(enc, worlds, p).items()
        )
        if ok:
            preserving.append(p)
    return tuple(preserving)


def make_derived_termination_controller(condition, enc):
    """Controller with probes only; termination is derived, not an action.

    Continue on a reachability-preserving probe when one exists. Otherwise compare
    the best remaining probe continuation utility with the immediate commit utility
    implied by the frozen value/cost contract. Termination is the absence of a
    justified continuation.
    """
    can_correct = make_can_correct(condition, enc)

    def choose(worlds, history, t):
        preserving = preserving_probes(
            condition, enc, worlds, history, t, can_correct
        )
        if preserving:
            return min(preserving), {
                "mode": "reachability",
                "preserving": preserving,
            }

        values = probe_values(condition, enc, worlds, history, t)
        commit_utility = stop_value(worlds)

        if not values:
            return None, {
                "mode": "derived_termination",
                "reason": "no_timely_refinement",
                "commit_utility": commit_utility,
                "probe_values": values,
            }

        best_probe_value = max(values.values())
        if best_probe_value <= commit_utility + EPS:
            return None, {
                "mode": "derived_termination",
                "reason": "no_positive_continuation_value",
                "commit_utility": commit_utility,
                "probe_values": values,
            }

        optimal = tuple(
            p for p, value in values.items()
            if abs(value - best_probe_value) < EPS
        )
        return min(optimal), {
            "mode": "value_continuation",
            "optimal": optimal,
            "commit_utility": commit_utility,
            "probe_values": values,
        }

    return choose


def make_exhaustion_only_controller(condition, enc):
    """Negative control: remove STOP but omit value-derived termination.

    The controller keeps probing whenever any timely probe remains, even when the
    best remaining probe cannot improve utility over immediate commitment.
    """
    can_correct = make_can_correct(condition, enc)

    def choose(worlds, history, t):
        preserving = preserving_probes(
            condition, enc, worlds, history, t, can_correct
        )
        if preserving:
            return min(preserving), {
                "mode": "reachability",
                "preserving": preserving,
            }

        values = probe_values(condition, enc, worlds, history, t)
        if not values:
            return None, {
                "mode": "exhaustion_termination",
                "reason": "no_timely_refinement",
            }

        best = max(values.values())
        optimal = tuple(
            p for p, value in values.items()
            if abs(value - best) < EPS
        )
        return min(optimal), {
            "mode": "forced_continuation",
            "optimal": optimal,
            "probe_values": values,
        }

    return choose


def run_no_stop(condition, enc, chooser):
    """Execute a controller whose epistemic action set contains probes only.

    `None` is not a supplied epistemic action. It denotes an empty continuation set;
    the runner then commits using the same frozen terminal correction rule.
    """
    correct = probes = 0
    traces = []
    termination_reasons = []

    for true_world in WORLDS:
        worlds, history, t, n = WORLDS, tuple(), 0, 0
        trace = []

        while True:
            choice, meta = chooser(worlds, history, t)
            trace.append((worlds, history, t, choice, meta))

            if choice is None:
                pred = action(worlds)
                if meta["mode"] in (
                    "derived_termination",
                    "exhaustion_termination",
                ):
                    termination_reasons.append(meta.get("reason"))
                break

            assert choice in timely(condition, enc, history, t)
            dt = geometry(condition, enc, history)[choice]
            outcome = observe(enc, true_world, choice)
            worlds = tuple(
                w for w in worlds
                if observe(enc, w, choice) == outcome
            )
            history += ((choice, outcome),)
            t += dt
            n += 1
            assert n <= PROBE_BUDGET
            assert t <= COMMITMENT_TAU

        correct += pred == warranted_action(true_world)
        probes += n
        traces.append(tuple(trace))

    accuracy = correct / len(WORLDS)
    mean_probes = probes / len(WORLDS)
    return {
        "accuracy": accuracy,
        "mean_probes": mean_probes,
        "mean_cost": mean_probes * PROBE_COST,
        "utility": V * accuracy - mean_probes * PROBE_COST,
        "traces": tuple(traces),
        "termination_reasons": tuple(termination_reasons),
    }


def normalize_primitive_trace(trace):
    return tuple(
        (worlds, history, t, None if choice == STOP else choice)
        for worlds, history, t, choice, _meta in trace
    )


def normalize_no_stop_trace(trace):
    return tuple(
        (worlds, history, t, choice)
        for worlds, history, t, choice, _meta in trace
    )


def audit():
    rows = {condition: [] for condition in CONDITIONS}
    total_decisions = 0
    primitive_stop_decisions = 0
    derived_termination_decisions = 0
    trace_mismatches = 0
    reason_counts = {
        "no_timely_refinement": 0,
        "no_positive_continuation_value": 0,
    }

    for seed in range(ENCODINGS):
        enc = make_encoding(seed)

        for condition in CONDITIONS:
            primitive = run_primitive(
                condition, enc, make_prune(condition, enc)
            )
            derived = run_no_stop(
                condition, enc,
                make_derived_termination_controller(condition, enc),
            )
            exhaustion = run_no_stop(
                condition, enc,
                make_exhaustion_only_controller(condition, enc),
            )

            for key in ("accuracy", "mean_probes", "mean_cost", "utility"):
                assert abs(primitive[key] - derived[key]) < EPS

            assert len(primitive["traces"]) == len(derived["traces"])
            for p_trace, d_trace in zip(
                primitive["traces"], derived["traces"]
            ):
                total_decisions += len(p_trace)
                primitive_stop_decisions += sum(
                    step[3] == STOP for step in p_trace
                )
                derived_termination_decisions += sum(
                    step[3] is None for step in d_trace
                )
                if (
                    normalize_primitive_trace(p_trace)
                    != normalize_no_stop_trace(d_trace)
                ):
                    trace_mismatches += 1

            for reason in derived["termination_reasons"]:
                reason_counts[reason] += 1

            rows[condition].append((primitive, derived, exhaustion))

    expected = {
        A: {
            "primitive": (1.0, 2.0, 8.0),
            "exhaustion": (1.0, 2.0, 8.0),
        },
        B: {
            "primitive": (0.75, 1.0, 6.5),
            "exhaustion": (0.75, 2.0, 5.5),
        },
        C: {
            "primitive": (0.75, 1.0, 6.5),
            "exhaustion": (0.75, 2.0, 5.5),
        },
    }

    summary = {}
    for condition, triples in rows.items():
        p0, d0, e0 = triples[0]
        assert all(
            (
                p["accuracy"], p["mean_probes"], p["utility"]
            ) == expected[condition]["primitive"]
            and (
                d["accuracy"], d["mean_probes"], d["utility"]
            ) == expected[condition]["primitive"]
            and (
                e["accuracy"], e["mean_probes"], e["utility"]
            ) == expected[condition]["exhaustion"]
            for p, d, e in triples
        )

        summary[condition] = {
            "primitive_stop": (
                p0["accuracy"], p0["mean_probes"], p0["utility"]
            ),
            "derived_termination": (
                d0["accuracy"], d0["mean_probes"], d0["utility"]
            ),
            "exhaustion_only": (
                e0["accuracy"], e0["mean_probes"], e0["utility"]
            ),
        }

    assert trace_mismatches == 0
    assert primitive_stop_decisions == derived_termination_decisions
    assert primitive_stop_decisions == (
        ENCODINGS * len(CONDITIONS) * len(WORLDS)
    )
    assert reason_counts == {
        "no_timely_refinement": ENCODINGS * len(WORLDS),
        "no_positive_continuation_value": (
            ENCODINGS * 2 * len(WORLDS)
        ),
    }

    return {
        "baseline_controller": BASELINE_CONTROLLER,
        "encodings": ENCODINGS,
        "conditions": summary,
        "visited_decision_points": total_decisions,
        "primitive_stop_decisions": primitive_stop_decisions,
        "derived_termination_decisions": derived_termination_decisions,
        "trace_mismatches": trace_mismatches,
        "derived_termination_reasons": reason_counts,
        "stop_action_present_in_derived_controller": False,
    }


if __name__ == "__main__":
    result = audit()
    print("STOP Substitution Audit")
    print("baseline:", result["baseline_controller"])
    for condition in CONDITIONS:
        row = result["conditions"][condition]
        print(
            condition,
            "primitive", row["primitive_stop"],
            "derived", row["derived_termination"],
            "exhaustion_only", row["exhaustion_only"],
        )
    print("visited decision points:", result["visited_decision_points"])
    print("primitive STOP decisions:", result["primitive_stop_decisions"])
    print("derived termination decisions:", result["derived_termination_decisions"])
    print("trace mismatches:", result["trace_mismatches"])
    print("termination reasons:", result["derived_termination_reasons"])
