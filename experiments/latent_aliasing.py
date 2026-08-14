"""Latent-defect Future-Sufficiency Arena.

The learner never observes the hidden regime or closure defect. At the probe
decision, the current observation is identical across regimes. The learner may
condition only on its own observed history and the known probe cost.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from random import Random
from typing import Iterable


class Regime(str, Enum):
    ALIGNED = "aligned"
    DIVERGENT = "divergent"
    MISLEADING = "misleading"


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
class WarmupEvent:
    nuisance_cue: int
    reward: float


@dataclass(frozen=True)
class DecisionState:
    history: tuple[WarmupEvent, ...]
    probe_cost: float


@dataclass(frozen=True)
class PostProbeState:
    history: tuple[WarmupEvent, ...]
    probe_cost: float
    hidden: HiddenState | None = None
    nuisance_bit: int | None = None


@dataclass(frozen=True)
class Block:
    regime: Regime
    warmup_order: tuple[HiddenState, HiddenState]
    target_hidden: HiddenState
    target_nuisance: int
    probe_cost: float


@dataclass(frozen=True)
class EvalRecord:
    gamma: int
    regime: Regime
    probe_cost: float
    probe: Probe
    net_return: float


class LatentAliasingArena:
    """Three-regime deterministic arena with latent future discrepancy."""

    COSTS = (0.1, 0.3, 0.6)

    @staticmethod
    def reward(regime: Regime, hidden: HiddenState, action: Action) -> float:
        if regime in (Regime.ALIGNED, Regime.MISLEADING):
            return 1.0 if action is Action.LEFT else 0.0
        if hidden is HiddenState.A:
            return 1.0 if action is Action.LEFT else 0.0
        return 1.0 if action is Action.RIGHT else 0.0

    @staticmethod
    def gamma(regime: Regime) -> int:
        """Evaluator-only binary defect label."""
        return int(regime is Regime.DIVERGENT)

    def warmup(self, block: Block) -> tuple[WarmupEvent, ...]:
        """Observed history before probing; no regime label is exposed.

        The nuisance cue is intentionally superficial: it is 1 in both the
        divergent and misleading regimes. Only experienced reward disagreement
        separates those two regimes.
        """
        cue = 0 if block.regime is Regime.ALIGNED else 1
        return tuple(
            WarmupEvent(cue, self.reward(block.regime, hidden, Action.LEFT))
            for hidden in block.warmup_order
        )

    def decision_state(self, block: Block) -> DecisionState:
        return DecisionState(self.warmup(block), block.probe_cost)

    def probe(self, block: Block, probe: Probe) -> PostProbeState:
        history = self.warmup(block)
        if probe is Probe.NONE:
            return PostProbeState(history, block.probe_cost)
        if probe is Probe.GENERIC:
            return PostProbeState(
                history,
                block.probe_cost,
                nuisance_bit=block.target_nuisance,
            )
        if probe is Probe.TARGETED:
            return PostProbeState(
                history,
                block.probe_cost,
                hidden=block.target_hidden,
            )
        raise ValueError(probe)

    @staticmethod
    def probe_cost(block: Block, probe: Probe) -> float:
        return 0.0 if probe is Probe.NONE else block.probe_cost

    def true_voi(self, regime: Regime, probe_cost: float, probe: Probe) -> float:
        """Evaluator-only exact VOI relative to no probe under a uniform hidden state."""
        no_probe = 1.0 if regime is not Regime.DIVERGENT else 0.5
        if probe is Probe.NONE:
            return 0.0
        if probe is Probe.GENERIC:
            return -probe_cost
        targeted = 1.0 - probe_cost
        return targeted - no_probe


class HistoryTabularLearner:
    """Epsilon-greedy learner over observable histories; Gamma is never an input."""

    def __init__(self, seed: int = 0, epsilon: float = 0.1) -> None:
        self.rng = Random(seed)
        self.epsilon = epsilon
        self.probe_value: dict[tuple[DecisionState, Probe], float] = defaultdict(float)
        self.probe_count: dict[tuple[DecisionState, Probe], int] = defaultdict(int)
        self.action_value: dict[tuple[PostProbeState, Action], float] = defaultdict(float)
        self.action_count: dict[tuple[PostProbeState, Action], int] = defaultdict(int)

    def _choose(self, values: dict, state, choices: tuple, explore: bool):
        if explore and self.rng.random() < self.epsilon:
            return self.rng.choice(choices)
        scored = [(values[(state, choice)], choice) for choice in choices]
        best_value = max(value for value, _ in scored)
        best = [choice for value, choice in scored if value == best_value]
        return self.rng.choice(best) if explore else best[0]

    def choose_probe(self, state: DecisionState, explore: bool = True) -> Probe:
        return self._choose(self.probe_value, state, tuple(Probe), explore)

    def choose_action(self, state: PostProbeState, explore: bool = True) -> Action:
        return self._choose(self.action_value, state, tuple(Action), explore)

    @staticmethod
    def _update(values: dict, counts: dict, key: tuple, target: float) -> None:
        counts[key] += 1
        n = counts[key]
        values[key] += (target - values[key]) / n

    def learn(
        self,
        decision_state: DecisionState,
        probe: Probe,
        post_probe_state: PostProbeState,
        action: Action,
        terminal_reward: float,
        net_return: float,
    ) -> None:
        self._update(
            self.action_value,
            self.action_count,
            (post_probe_state, action),
            terminal_reward,
        )
        self._update(
            self.probe_value,
            self.probe_count,
            (decision_state, probe),
            net_return,
        )


def sample_block(rng: Random, costs: tuple[float, ...]) -> Block:
    order = [HiddenState.A, HiddenState.B]
    rng.shuffle(order)
    return Block(
        regime=rng.choice(tuple(Regime)),
        warmup_order=(order[0], order[1]),
        target_hidden=rng.choice(tuple(HiddenState)),
        target_nuisance=rng.choice((0, 1)),
        probe_cost=rng.choice(costs),
    )


def train(
    learner: HistoryTabularLearner,
    arena: LatentAliasingArena,
    blocks: int,
    seed: int,
) -> None:
    rng = Random(seed)
    for _ in range(blocks):
        block = sample_block(rng, arena.COSTS)
        decision = arena.decision_state(block)
        probe = learner.choose_probe(decision, explore=True)
        post = arena.probe(block, probe)
        action = learner.choose_action(post, explore=True)
        reward = arena.reward(block.regime, block.target_hidden, action)
        net_return = reward - arena.probe_cost(block, probe)
        learner.learn(decision, probe, post, action, reward, net_return)


def held_out_blocks(count: int, seed: int, costs: tuple[float, ...]) -> list[Block]:
    rng = Random(seed)
    return [sample_block(rng, costs) for _ in range(count)]


def evaluate(
    learner: HistoryTabularLearner,
    arena: LatentAliasingArena,
    blocks: Iterable[Block],
) -> list[EvalRecord]:
    records: list[EvalRecord] = []
    for block in blocks:
        decision = arena.decision_state(block)
        probe = learner.choose_probe(decision, explore=False)
        post = arena.probe(block, probe)
        action = learner.choose_action(post, explore=False)
        reward = arena.reward(block.regime, block.target_hidden, action)
        records.append(
            EvalRecord(
                gamma=arena.gamma(block.regime),
                regime=block.regime,
                probe_cost=block.probe_cost,
                probe=probe,
                net_return=reward - arena.probe_cost(block, probe),
            )
        )
    return records


def rate(records: Iterable[EvalRecord], predicate) -> float:
    selected = [r.probe is Probe.TARGETED for r in records if predicate(r)]
    if not selected:
        raise ValueError("empty evaluation slice")
    return sum(selected) / len(selected)


def shuffled_gamma_gap(records: list[EvalRecord], seed: int, permutations: int = 200) -> float:
    rng = Random(seed)
    labels = [r.gamma for r in records]
    choices = [r.probe is Probe.TARGETED for r in records]
    gaps: list[float] = []
    for _ in range(permutations):
        shuffled = labels[:]
        rng.shuffle(shuffled)
        one = [c for c, g in zip(choices, shuffled) if g == 1]
        zero = [c for c, g in zip(choices, shuffled) if g == 0]
        gaps.append(sum(one) / len(one) - sum(zero) / len(zero))
    return sum(gaps) / len(gaps)


def run_experiment() -> dict[str, float]:
    arena = LatentAliasingArena()
    learner = HistoryTabularLearner(seed=7, epsilon=0.1)
    train(learner, arena, blocks=80_000, seed=11)
    held_out = held_out_blocks(12_000, seed=29, costs=arena.COSTS)
    records = evaluate(learner, arena, held_out)

    p_gamma_1 = rate(records, lambda r: r.gamma == 1)
    p_gamma_0 = rate(records, lambda r: r.gamma == 0)
    gamma_gap = p_gamma_1 - p_gamma_0

    p_div_low = rate(
        records,
        lambda r: r.regime is Regime.DIVERGENT and r.probe_cost < 0.5,
    )
    p_div_high = rate(
        records,
        lambda r: r.regime is Regime.DIVERGENT and r.probe_cost > 0.5,
    )
    p_misleading = rate(records, lambda r: r.regime is Regime.MISLEADING)
    p_aligned = rate(records, lambda r: r.regime is Regime.ALIGNED)
    shuffle_gap = shuffled_gamma_gap(records, seed=41)

    results = {
        "p_target_gamma_1": p_gamma_1,
        "p_target_gamma_0": p_gamma_0,
        "targeted_probe_gap": gamma_gap,
        "p_target_divergent_cost_lt_voi": p_div_low,
        "p_target_divergent_cost_gt_voi": p_div_high,
        "p_target_misleading": p_misleading,
        "p_target_aligned": p_aligned,
        "shuffled_gamma_gap": shuffle_gap,
    }

    assert gamma_gap > 0.25
    assert p_div_low > 0.8
    assert p_div_high < 0.2
    assert p_misleading < 0.2
    assert p_aligned < 0.2
    assert abs(shuffle_gap) < 0.05
    return results


if __name__ == "__main__":
    for name, value in run_experiment().items():
        print(f"{name}: {value:.4f}")
