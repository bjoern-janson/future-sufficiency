"""Learn and evaluate probe selection without exposing closure defect to the learner.

Pipeline:
episodes -> tabular policy -> held-out evaluation -> probe statistics

The learner observes only arena observations, chosen probes/actions, and rewards.
Gamma_I is used only by the evaluator after behavior has been generated.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from random import Random
from typing import Iterable

from arena import (
    Action,
    Episode,
    FutureSufficiencyArena,
    HiddenState,
    Observation,
    Probe,
    Regime,
)


@dataclass(frozen=True)
class EvalRecord:
    gamma: int
    probe: Probe
    net_return: float


class TabularLearner:
    """Two-stage epsilon-greedy learner with sample-average value estimates."""

    def __init__(self, seed: int = 0, epsilon: float = 0.1) -> None:
        if not 0.0 <= epsilon <= 1.0:
            raise ValueError("epsilon must be in [0, 1]")
        self.rng = Random(seed)
        self.epsilon = epsilon
        self.probe_value: dict[tuple[Observation, Probe], float] = defaultdict(float)
        self.probe_count: dict[tuple[Observation, Probe], int] = defaultdict(int)
        self.action_value: dict[tuple[Observation, Action], float] = defaultdict(float)
        self.action_count: dict[tuple[Observation, Action], int] = defaultdict(int)

    def _choose(self, values: dict, state: Observation, choices: tuple, explore: bool):
        if explore and self.rng.random() < self.epsilon:
            return self.rng.choice(choices)

        scored = [(values[(state, choice)], choice) for choice in choices]
        best_value = max(value for value, _ in scored)
        best = [choice for value, choice in scored if value == best_value]
        return self.rng.choice(best) if explore else best[0]

    def choose_probe(self, observation: Observation, explore: bool = True) -> Probe:
        return self._choose(
            self.probe_value,
            observation,
            tuple(Probe),
            explore,
        )

    def choose_action(self, observation: Observation, explore: bool = True) -> Action:
        return self._choose(
            self.action_value,
            observation,
            tuple(Action),
            explore,
        )

    @staticmethod
    def _sample_average(
        values: dict,
        counts: dict,
        key: tuple,
        target: float,
    ) -> None:
        counts[key] += 1
        n = counts[key]
        values[key] += (target - values[key]) / n

    def update(
        self,
        initial_observation: Observation,
        probe: Probe,
        post_probe_observation: Observation,
        action: Action,
        terminal_reward: float,
        net_return: float,
    ) -> None:
        self._sample_average(
            self.action_value,
            self.action_count,
            (post_probe_observation, action),
            terminal_reward,
        )
        self._sample_average(
            self.probe_value,
            self.probe_count,
            (initial_observation, probe),
            net_return,
        )


def sample_episode(rng: Random) -> Episode:
    return Episode(
        regime=rng.choice(tuple(Regime)),
        hidden=rng.choice(tuple(HiddenState)),
        nuisance_bit=rng.choice((0, 1)),
    )


def train(
    learner: TabularLearner,
    arena: FutureSufficiencyArena,
    episodes: int,
    seed: int,
) -> None:
    rng = Random(seed)
    for _ in range(episodes):
        episode = sample_episode(rng)
        initial = arena.initial_observation(episode)
        probe = learner.choose_probe(initial, explore=True)
        probe_result = arena.probe(episode, probe)
        action = learner.choose_action(probe_result.observation, explore=True)
        terminal_reward = arena.terminal_reward(episode, action)
        net_return = terminal_reward - probe_result.cost
        learner.update(
            initial,
            probe,
            probe_result.observation,
            action,
            terminal_reward,
            net_return,
        )


def evaluate_policy(
    learner: TabularLearner,
    arena: FutureSufficiencyArena,
    episodes: Iterable[Episode],
) -> list[EvalRecord]:
    """Evaluate a frozen greedy policy.

    The learner does not receive gamma. The evaluator adds gamma only after
    the learner has already selected its probe.
    """
    records: list[EvalRecord] = []
    for episode in episodes:
        initial = arena.initial_observation(episode)
        probe = learner.choose_probe(initial, explore=False)
        probe_result = arena.probe(episode, probe)
        action = learner.choose_action(probe_result.observation, explore=False)
        net_return = arena.terminal_reward(episode, action) - probe_result.cost
        gamma = arena.closure_defect(episode.regime)
        records.append(EvalRecord(gamma, probe, net_return))
    return records


def held_out_episodes(count: int, seed: int) -> list[Episode]:
    rng = Random(seed)
    return [sample_episode(rng) for _ in range(count)]


def targeted_rate(records: Iterable[EvalRecord], gamma: int) -> float:
    selected = [r.probe is Probe.TARGETED for r in records if r.gamma == gamma]
    if not selected:
        raise ValueError(f"no records with gamma={gamma}")
    return sum(selected) / len(selected)


def forced_probe_return(
    learner: TabularLearner,
    arena: FutureSufficiencyArena,
    episodes: Iterable[Episode],
    probe: Probe,
    gamma: int,
) -> float:
    """Counterfactual held-out return under a forced information condition."""
    returns: list[float] = []
    for episode in episodes:
        if arena.closure_defect(episode.regime) != gamma:
            continue
        result = arena.probe(episode, probe)
        action = learner.choose_action(result.observation, explore=False)
        returns.append(arena.terminal_reward(episode, action) - result.cost)
    if not returns:
        raise ValueError(f"no held-out episodes with gamma={gamma}")
    return sum(returns) / len(returns)


def shuffled_gamma_gap(
    records: list[EvalRecord],
    seed: int,
    permutations: int = 200,
) -> float:
    """Mean signed targeted-probe gap after permuting gamma labels."""
    rng = Random(seed)
    labels = [record.gamma for record in records]
    targeted = [record.probe is Probe.TARGETED for record in records]
    gaps: list[float] = []

    for _ in range(permutations):
        shuffled = labels[:]
        rng.shuffle(shuffled)
        rate_1 = [choice for choice, gamma in zip(targeted, shuffled) if gamma == 1]
        rate_0 = [choice for choice, gamma in zip(targeted, shuffled) if gamma == 0]
        gaps.append(sum(rate_1) / len(rate_1) - sum(rate_0) / len(rate_0))

    return sum(gaps) / len(gaps)


def run_experiment() -> dict[str, float]:
    arena = FutureSufficiencyArena(probe_cost=0.2)
    learner = TabularLearner(seed=7, epsilon=0.1)

    train(learner, arena, episodes=20_000, seed=11)
    held_out = held_out_episodes(count=4_000, seed=29)
    records = evaluate_policy(learner, arena, held_out)

    p_target_gamma_1 = targeted_rate(records, gamma=1)
    p_target_gamma_0 = targeted_rate(records, gamma=0)
    targeted_gap = p_target_gamma_1 - p_target_gamma_0

    none_gamma_1 = forced_probe_return(
        learner, arena, held_out, Probe.NONE, gamma=1
    )
    generic_gamma_1 = forced_probe_return(
        learner, arena, held_out, Probe.GENERIC, gamma=1
    )
    targeted_gamma_1 = forced_probe_return(
        learner, arena, held_out, Probe.TARGETED, gamma=1
    )

    voi_generic = generic_gamma_1 - none_gamma_1
    voi_targeted = targeted_gamma_1 - none_gamma_1
    shuffle_gap = shuffled_gamma_gap(records, seed=41)

    results = {
        "p_target_gamma_1": p_target_gamma_1,
        "p_target_gamma_0": p_target_gamma_0,
        "targeted_probe_gap": targeted_gap,
        "voi_targeted_gamma_1": voi_targeted,
        "voi_generic_gamma_1": voi_generic,
        "shuffled_gamma_gap": shuffle_gap,
    }

    assert targeted_gap > 0.0
    assert voi_targeted > voi_generic
    assert abs(shuffle_gap) < 0.05

    return results


if __name__ == "__main__":
    results = run_experiment()
    for name, value in results.items():
        print(f"{name}: {value:.4f}")
