"""Minimal Admissible Evidence-Action Topology Audit.

Pure epistemic minimality audit: no adaptive learner, no hypothesis search,
no repair construction. It asks which admissible evidence/action components
are required for the warranted meta-action {D,R,S} to be identifiable.

Standard library only; deterministic and exhaustive.
"""

from dataclasses import dataclass, asdict
from itertools import combinations
from collections import defaultdict

D, R, S = "D", "R", "S"


@dataclass(frozen=True)
class World:
    name: str
    required_action: str
    residual_present: int
    exact_h0_alternative: int
    deterministic_residual: int
    positive_reopen_value: int


WORLDS = (
    World("D_resolvable", D, 1, 1, 1, 1),
    World("R_unrepresentable", R, 1, 0, 1, 1),
    World("S_zero_value", S, 1, 0, 1, 0),
    World("S_irreducible", S, 1, 0, 0, 1),
    World("S_adequate", S, 0, 0, 1, 1),
)


@dataclass(frozen=True)
class Component:
    name: str
    mode: str  # passive | active
    field: str | None
    cost: float
    risk: float
    reversible: bool
    authorized: bool
    oracle: bool = False

    def observe(self, world: World):
        if self.oracle:
            return world.required_action
        return getattr(world, self.field)


# Feasibility / authority contract for active challenge paths.
MAX_COST = 2.0
MAX_RISK = 1.0
REQUIRE_REVERSIBLE = True
REQUIRE_AUTHORITY = True

COMPONENTS = (
    Component(
        "local_residual",
        "passive",
        "residual_present",
        cost=0.0,
        risk=0.0,
        reversible=True,
        authorized=True,
    ),
    Component(
        "alternative_fit_probe",
        "active",
        "exact_h0_alternative",
        cost=1.0,
        risk=0.0,
        reversible=True,
        authorized=True,
    ),
    Component(
        "consistency_probe",
        "active",
        "deterministic_residual",
        cost=1.0,
        risk=0.5,
        reversible=True,
        authorized=True,
    ),
    Component(
        "future_value_probe",
        "active",
        "positive_reopen_value",
        cost=1.0,
        risk=0.5,
        reversible=True,
        authorized=True,
    ),
    # Four deliberately inadmissible shortcuts. Each reveals the required
    # action directly, showing why feasibility constraints must be part of
    # the evidence-action topology rather than added after identifiability.
    Component(
        "unauthorized_oracle",
        "active",
        None,
        cost=0.0,
        risk=0.0,
        reversible=True,
        authorized=False,
        oracle=True,
    ),
    Component(
        "too_costly_oracle",
        "active",
        None,
        cost=100.0,
        risk=0.0,
        reversible=True,
        authorized=True,
        oracle=True,
    ),
    Component(
        "risky_oracle",
        "active",
        None,
        cost=0.0,
        risk=10.0,
        reversible=True,
        authorized=True,
        oracle=True,
    ),
    Component(
        "irreversible_oracle",
        "active",
        None,
        cost=0.0,
        risk=0.0,
        reversible=False,
        authorized=True,
        oracle=True,
    ),
)

COMPONENT_BY_NAME = {c.name: c for c in COMPONENTS}


def admissible(component: Component) -> bool:
    if component.mode == "passive":
        return True
    if component.cost > MAX_COST:
        return False
    if component.risk > MAX_RISK:
        return False
    if REQUIRE_REVERSIBLE and not component.reversible:
        return False
    if REQUIRE_AUTHORITY and not component.authorized:
        return False
    return True


ADMISSIBLE = tuple(c for c in COMPONENTS if admissible(c))
INADMISSIBLE = tuple(c for c in COMPONENTS if not admissible(c))


def signature(world: World, topology):
    return tuple((c.name, c.observe(world)) for c in topology)


def equivalence_classes(topology):
    classes = defaultdict(list)
    for world in WORLDS:
        classes[signature(world, topology)].append(world)
    return tuple(tuple(group) for group in classes.values())


def conflicts(topology):
    out = []
    for group in equivalence_classes(topology):
        actions = {w.required_action for w in group}
        if len(actions) > 1:
            out.append(
                {
                    "worlds": tuple(w.name for w in group),
                    "actions": tuple(sorted(actions)),
                }
            )
    return tuple(out)


def sufficient(topology):
    return len(conflicts(topology)) == 0


def powerset(items):
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            yield combo


def minimal_sufficient_topologies(items):
    sufficient_sets = [combo for combo in powerset(items) if sufficient(combo)]
    mins = []
    for combo in sufficient_sets:
        names = {c.name for c in combo}
        if not any(
            {c.name for c in other} < names
            for other in sufficient_sets
        ):
            mins.append(combo)
    return tuple(mins)


def intended_witness(component_name):
    return {
        "local_residual": ("R_unrepresentable", "S_adequate"),
        "alternative_fit_probe": ("D_resolvable", "R_unrepresentable"),
        "consistency_probe": ("R_unrepresentable", "S_irreducible"),
        "future_value_probe": ("R_unrepresentable", "S_zero_value"),
    }[component_name]


def pair_is_collapsed(topology, pair):
    wa = next(w for w in WORLDS if w.name == pair[0])
    wb = next(w for w in WORLDS if w.name == pair[1])
    return signature(wa, topology) == signature(wb, topology)


def audit():
    assert len(ADMISSIBLE) == 4
    assert len(INADMISSIBLE) == 4
    assert all(not c.oracle for c in ADMISSIBLE)
    assert all(c.oracle for c in INADMISSIBLE)

    full = ADMISSIBLE
    assert sufficient(full)

    minima = minimal_sufficient_topologies(ADMISSIBLE)
    assert len(minima) == 1
    assert {c.name for c in minima[0]} == {c.name for c in ADMISSIBLE}

    ablations = {}
    for removed in ADMISSIBLE:
        remaining = tuple(c for c in ADMISSIBLE if c.name != removed.name)
        assert not sufficient(remaining)
        witness = intended_witness(removed.name)
        assert pair_is_collapsed(remaining, witness)
        wa = next(w for w in WORLDS if w.name == witness[0])
        wb = next(w for w in WORLDS if w.name == witness[1])
        assert wa.required_action != wb.required_action
        ablations[removed.name] = {
            "remaining": tuple(c.name for c in remaining),
            "witness_pair": witness,
            "witness_actions": (wa.required_action, wb.required_action),
            "conflicts": conflicts(remaining),
        }

    # Each inadmissible oracle would trivialize identifiability if the
    # corresponding feasibility constraint were silently ignored.
    shortcut_results = {}
    for shortcut in INADMISSIBLE:
        assert sufficient((shortcut,))
        shortcut_results[shortcut.name] = {
            "sufficient_if_illegally_admitted": True,
            "cost": shortcut.cost,
            "risk": shortcut.risk,
            "reversible": shortcut.reversible,
            "authorized": shortcut.authorized,
        }

    all_admissible_subsets = []
    for topology in powerset(ADMISSIBLE):
        all_admissible_subsets.append(
            {
                "components": tuple(c.name for c in topology),
                "sufficient": sufficient(topology),
                "conflicts": conflicts(topology),
            }
        )

    return {
        "contract": {
            "required_actions": (D, R, S),
            "max_component_cost": MAX_COST,
            "max_risk": MAX_RISK,
            "require_reversible": REQUIRE_REVERSIBLE,
            "require_authority": REQUIRE_AUTHORITY,
            "learner_present": False,
            "repair_construction_present": False,
        },
        "worlds": tuple(asdict(w) for w in WORLDS),
        "admissible_components": tuple(asdict(c) for c in ADMISSIBLE),
        "inadmissible_shortcuts": tuple(asdict(c) for c in INADMISSIBLE),
        "full_topology_sufficient": sufficient(full),
        "minimal_sufficient_topologies": tuple(
            tuple(c.name for c in topology) for topology in minima
        ),
        "ablation_certificate": ablations,
        "inadmissible_shortcut_control": shortcut_results,
        "all_admissible_subsets": tuple(all_admissible_subsets),
        "boundary": {
            "finite_world_set": True,
            "deterministic_observation_contract": True,
            "required_meta_actions_evaluator_supplied": True,
            "component_semantics_evaluator_supplied": True,
            "admissibility_thresholds_supplied": True,
            "general_identifiability_theorem": False,
            "learner_capability_claim": False,
        },
    }


def print_report(result):
    print("Minimal Admissible Evidence-Action Topology Audit")
    print("learner present:", result["contract"]["learner_present"])
    print("admissible:", [c["name"] for c in result["admissible_components"]])
    print("inadmissible shortcuts:", [c["name"] for c in result["inadmissible_shortcuts"]])
    print("full topology sufficient:", result["full_topology_sufficient"])
    print("minimal sufficient topologies:", result["minimal_sufficient_topologies"])
    print("ablation witnesses:")
    for name, info in result["ablation_certificate"].items():
        print(" ", name, "->", info["witness_pair"], info["witness_actions"])
    print("inadmissible shortcut control:")
    for name, info in result["inadmissible_shortcut_control"].items():
        print(" ", name, "sufficient_if_illegally_admitted=", info["sufficient_if_illegally_admitted"])


if __name__ == "__main__":
    result = audit()
    print_report(result)
