"""Minimal deterministic Future-Sufficiency Arena.

The arena isolates one phenomenon:
a representation may alias latent states whose action-conditioned futures differ.

There are no external dependencies and no learning-agent assumptions here.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import isclose


class Regime(str, Enum):
    ALIGNED = "aligned"
    DIVERGENT = "divergent"


class HiddenState(str, Enum):
    A = "x_a"
    B = "x_b"


class Action(str, Enum):
    LEFT = "left"
    RIGHT = "right"


class Probe(str, Enum):
    NONE = "none"
    GENERIC = "generic"
    TARGETED = "targeted"


@dataclass(frozen=True)
class Episode:
    regime: Regime
    hidden: HiddenState
    nuisance_bit: int

    def __post_init__(self) -> None:
        if self.nuisance_bit not in (0, 1):
            raise ValueError("nuisance_bit must be 0 or 1")


@dataclass(frozen=True)
class Observation:
    regime: Regime
    hidden: HiddenState | None = None
    nuisance_bit: int | None = None


@dataclass(frozen=True)
class ProbeResult:
    observation: Observation
    cost: float


class FutureSufficiencyArena:
    """Two-state deterministic arena with optional costly information."""

    def __init__(self, probe_cost: float = 0.2) -> None:
        if not 0.0 < probe_cost < 0.5:
            raise ValueError("probe_cost must be between 0 and 0.5")
        self.probe_cost = probe_cost

    @staticmethod
    def initial_observation(episode: Episode) -> Observation:
        """Initial representation I: hidden state and nuisance bit are aliased."""
        return Observation(regime=episode.regime)

    def probe(self, episode: Episode, kind: Probe) -> ProbeResult:
        """Return the post-probe observation and its information cost."""
        if kind is Probe.NONE:
            return ProbeResult(self.initial_observation(episode), 0.0)
        if kind is Probe.GENERIC:
            return ProbeResult(
                Observation(
                    regime=episode.regime,
                    nuisance_bit=episode.nuisance_bit,
                ),
                self.probe_cost,
            )
        if kind is Probe.TARGETED:
            return ProbeResult(
                Observation(
                    regime=episode.regime,
                    hidden=episode.hidden,
                ),
                self.probe_cost,
            )
        raise ValueError(f"unknown probe: {kind}")

    @staticmethod
    def terminal_reward(episode: Episode, action: Action) -> float:
        """Deterministic future payoff after the information decision."""
        if episode.regime is Regime.ALIGNED:
            return 1.0 if action is Action.LEFT else 0.0

        if episode.hidden is HiddenState.A:
            return 1.0 if action is Action.LEFT else 0.0
        return 1.0 if action is Action.RIGHT else 0.0

    def closure_defect(self, regime: Regime) -> int:
        """Binary operational Gamma_I for the initial representation.

        Gamma_I = 1 iff some common action has different terminal consequences
        for hidden states that I aliases.
        """
        for action in Action:
            a = Episode(regime, HiddenState.A, 0)
            b = Episode(regime, HiddenState.B, 0)
            if self.terminal_reward(a, action) != self.terminal_reward(b, action):
                return 1
        return 0


def _reference_action(observation: Observation) -> Action:
    """Optimal action given only the information contained in observation."""
    if observation.regime is Regime.ALIGNED:
        return Action.LEFT
    if observation.hidden is HiddenState.B:
        return Action.RIGHT
    return Action.LEFT


def reference_return(
    arena: FutureSufficiencyArena,
    regime: Regime,
    probe: Probe,
) -> float:
    """Exact mean net return of a reference policy over hidden/nuisance states."""
    returns: list[float] = []
    for hidden in HiddenState:
        for nuisance_bit in (0, 1):
            episode = Episode(regime, hidden, nuisance_bit)
            result = arena.probe(episode, probe)
            action = _reference_action(result.observation)
            returns.append(
                arena.terminal_reward(episode, action) - result.cost
            )
    return sum(returns) / len(returns)


def sanity_check() -> None:
    """Verify that the arena contains the intended experimental contrast."""
    arena = FutureSufficiencyArena(probe_cost=0.2)

    assert arena.closure_defect(Regime.ALIGNED) == 0
    assert arena.closure_defect(Regime.DIVERGENT) == 1

    aligned_none = reference_return(arena, Regime.ALIGNED, Probe.NONE)
    aligned_generic = reference_return(arena, Regime.ALIGNED, Probe.GENERIC)
    aligned_targeted = reference_return(arena, Regime.ALIGNED, Probe.TARGETED)

    divergent_none = reference_return(arena, Regime.DIVERGENT, Probe.NONE)
    divergent_generic = reference_return(arena, Regime.DIVERGENT, Probe.GENERIC)
    divergent_targeted = reference_return(arena, Regime.DIVERGENT, Probe.TARGETED)

    assert isclose(aligned_none, 1.0)
    assert isclose(aligned_generic, 0.8)
    assert isclose(aligned_targeted, 0.8)

    assert isclose(divergent_none, 0.5)
    assert isclose(divergent_generic, 0.3)
    assert isclose(divergent_targeted, 0.8)

    assert divergent_targeted > divergent_none > divergent_generic
    assert aligned_none > aligned_targeted
    assert aligned_none > aligned_generic


if __name__ == "__main__":
    sanity_check()
    print("Future-Sufficiency Arena sanity check passed.")
