"""Persistent representation-repair transfer experiment.

The learner starts with an aliased representation that discards two candidate
one-bit features. A costly targeted probe reveals the hidden state for the
current episode. Probe-labeled examples are used by a generic feature selector
to promote one candidate feature into the persistent representation.

The policy never receives Gamma_I or a regime label. Transfer is evaluated on
disjoint surface histories with probing disabled.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum, IntEnum
from random import Random
from typing import Iterable


class HiddenState(IntEnum):
    A = 0
    B = 1


class Action(str, Enum):
    LEFT = "left"
    RIGHT = "right"


class Probe(str, Enum):
    NONE = "none"
    TARGETED = "targeted"


class Feature(str, Enum):
    DIAGNOSTIC = "diagnostic"
    NUISANCE = "nuisance"


@dataclass(frozen=True)
class RawObservation:
    surface_history: tuple[int, int, int]
    diagnostic_bit: int
    nuisance_bit: int


@dataclass(frozen=True)
class Episode:
    raw: RawObservation
    hidden: HiddenState

    def __post_init__(self) -> None:
        if self.raw.diagnostic_bit != int(self.hidden):
            raise ValueError("diagnostic_bit must encode the latent distinction")


@dataclass
class Representation:
    """Compressed internal state M."""

    active_feature: Feature | None = None

    def encode(self, raw: RawObservation) -> tuple[str, int] | tuple[str]:
        if self.active_feature is None:
            return ("aliased",)
        if self.active_feature is Feature.DIAGNOSTIC:
            return ("split", raw.diagnostic_bit)
        return ("split", raw.nuisance_bit)


@dataclass(frozen=True)
class ActionState:
    representation_state: tuple
    revealed_hidden: HiddenState | None = None


def terminal_reward(hidden: HiddenState, action: Action) -> float:
    if hidden is HiddenState.A:
        return 1.0 if action is Action.LEFT else 0.0
    return 1.0 if action is Action.RIGHT else 0.0


def make_episodes(
    count: int,
    seed: int,
    surface_offset: int,
) -> list[Episode]:
    """Generate episodes with unique surface histories.

    Train and test calls use disjoint offsets. The same latent distinction and
    candidate features recur across both sets.
    """
    rng = Random(seed)
    episodes: list[Episode] = []
    for index in range(count):
        hidden = rng.choice(tuple(HiddenState))
        raw = RawObservation(
            surface_history=(
                surface_offset + index,
                rng.randrange(1_000_000),
                rng.randrange(1_000_000),
            ),
            diagnostic_bit=int(hidden),
            nuisance_bit=rng.choice((0, 1)),
        )
        episodes.append(Episode(raw=raw, hidden=hidden))
    return episodes


class RepairLearner:
    """Tabular learner with persistent feature promotion.

    Probe choice is learned from reward. Representation repair is generic:
    among a fixed bank of candidate one-bit features, promote the feature whose
    values best predict hidden labels obtained through targeted probes.

    This is feature selection/promotion, not open-ended feature invention.
    """

    def __init__(
        self,
        *,
        seed: int = 0,
        epsilon: float = 0.1,
        probe_cost: float = 0.2,
        min_probe_labels: int = 32,
        repair_accuracy: float = 0.9,
        repair_margin: float = 0.2,
    ) -> None:
        self.rng = Random(seed)
        self.epsilon = epsilon
        self.probe_cost = probe_cost
        self.min_probe_labels = min_probe_labels
        self.repair_accuracy = repair_accuracy
        self.repair_margin = repair_margin

        self.representation = Representation()
        self.probe_value: dict[tuple[tuple, Probe], float] = defaultdict(float)
        self.probe_count: dict[tuple[tuple, Probe], int] = defaultdict(int)
        self.action_value: dict[tuple[ActionState, Action], float] = defaultdict(float)
        self.action_count: dict[tuple[ActionState, Action], int] = defaultdict(int)

        self.probe_labels: list[tuple[RawObservation, HiddenState]] = []
        self.repair_feature: Feature | None = None
        self.repair_episode: int | None = None

    def _choose(
        self,
        values: dict,
        state,
        choices: tuple,
        *,
        explore: bool,
    ):
        if explore and self.rng.random() < self.epsilon:
            return self.rng.choice(choices)

        scored = [(values[(state, choice)], choice) for choice in choices]
        best_value = max(value for value, _ in scored)
        best = [choice for value, choice in scored if value == best_value]
        return self.rng.choice(best) if explore else best[0]

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

    def choose_probe(self, raw: RawObservation, *, explore: bool) -> Probe:
        state = self.representation.encode(raw)
        return self._choose(
            self.probe_value,
            state,
            tuple(Probe),
            explore=explore,
        )

    def choose_action(
        self,
        raw: RawObservation,
        probe: Probe,
        revealed_hidden: HiddenState | None,
        *,
        explore: bool,
    ) -> Action:
        state = ActionState(
            self.representation.encode(raw),
            revealed_hidden if probe is Probe.TARGETED else None,
        )
        return self._choose(
            self.action_value,
            state,
            tuple(Action),
            explore=explore,
        )

    @staticmethod
    def _feature_value(feature: Feature, raw: RawObservation) -> int:
        if feature is Feature.DIAGNOSTIC:
            return raw.diagnostic_bit
        return raw.nuisance_bit

    def _feature_accuracy(self, feature: Feature) -> float:
        """Best empirical binary mapping from candidate feature to probed label."""
        correct = 0
        for value in (0, 1):
            labels = [
                hidden
                for raw, hidden in self.probe_labels
                if self._feature_value(feature, raw) == value
            ]
            if not labels:
                continue
            count_a = labels.count(HiddenState.A)
            count_b = labels.count(HiddenState.B)
            correct += max(count_a, count_b)
        return correct / len(self.probe_labels)

    def _maybe_repair(self, episode_index: int) -> bool:
        if self.representation.active_feature is not None:
            return False
        if len(self.probe_labels) < self.min_probe_labels:
            return False

        scored = sorted(
            ((self._feature_accuracy(feature), feature) for feature in Feature),
            key=lambda item: item[0],
            reverse=True,
        )
        best_accuracy, best_feature = scored[0]
        second_accuracy = scored[1][0]

        if (
            best_accuracy >= self.repair_accuracy
            and best_accuracy - second_accuracy >= self.repair_margin
        ):
            self.representation.active_feature = best_feature
            self.repair_feature = best_feature
            self.repair_episode = episode_index
            return True
        return False

    def train_step(self, episode: Episode, episode_index: int) -> Probe:
        rep_state = self.representation.encode(episode.raw)
        probe = self.choose_probe(episode.raw, explore=True)
        revealed = episode.hidden if probe is Probe.TARGETED else None
        action = self.choose_action(
            episode.raw,
            probe,
            revealed,
            explore=True,
        )
        reward = terminal_reward(episode.hidden, action)
        net_return = reward - (self.probe_cost if probe is Probe.TARGETED else 0.0)

        action_state = ActionState(
            self.representation.encode(episode.raw),
            revealed,
        )
        self._sample_average(
            self.action_value,
            self.action_count,
            (action_state, action),
            reward,
        )
        self._sample_average(
            self.probe_value,
            self.probe_count,
            (rep_state, probe),
            net_return,
        )

        if probe is Probe.TARGETED:
            self.probe_labels.append((episode.raw, episode.hidden))
        self._maybe_repair(episode_index)
        return probe

    def reuse_action(self, raw: RawObservation) -> Action:
        """Greedy no-probe action from the persistent representation."""
        return self.choose_action(
            raw,
            Probe.NONE,
            None,
            explore=False,
        )


class FixedRepresentationPolicy:
    """Matched action learner for a fixed representation."""

    def __init__(
        self,
        feature: Feature | None,
        *,
        seed: int,
        epsilon: float = 0.1,
    ) -> None:
        self.representation = Representation(feature)
        self.rng = Random(seed)
        self.epsilon = epsilon
        self.action_value: dict[tuple[tuple, Action], float] = defaultdict(float)
        self.action_count: dict[tuple[tuple, Action], int] = defaultdict(int)

    def choose_action(self, raw: RawObservation, *, explore: bool) -> Action:
        state = self.representation.encode(raw)
        if explore and self.rng.random() < self.epsilon:
            return self.rng.choice(tuple(Action))

        scored = [(self.action_value[(state, action)], action) for action in Action]
        best_value = max(value for value, _ in scored)
        best = [action for value, action in scored if value == best_value]
        return self.rng.choice(best) if explore else best[0]

    def train_step(self, episode: Episode) -> None:
        state = self.representation.encode(episode.raw)
        action = self.choose_action(episode.raw, explore=True)
        reward = terminal_reward(episode.hidden, action)
        key = (state, action)
        self.action_count[key] += 1
        n = self.action_count[key]
        self.action_value[key] += (reward - self.action_value[key]) / n

    def accuracy(self, episodes: Iterable[Episode]) -> float:
        episodes = list(episodes)
        correct = sum(
            terminal_reward(
                episode.hidden,
                self.choose_action(episode.raw, explore=False),
            )
            for episode in episodes
        )
        return correct / len(episodes)


def representation_capacity(
    representation: Representation,
    episodes: Iterable[Episode],
) -> int:
    return len({representation.encode(episode.raw) for episode in episodes})


def reuse_accuracy(
    learner: RepairLearner,
    episodes: Iterable[Episode],
) -> float:
    episodes = list(episodes)
    correct = sum(
        terminal_reward(episode.hidden, learner.reuse_action(episode.raw))
        for episode in episodes
    )
    return correct / len(episodes)


def held_out_probe_rate(
    learner: RepairLearner,
    episodes: Iterable[Episode],
) -> float:
    episodes = list(episodes)
    targeted = sum(
        learner.choose_probe(episode.raw, explore=False) is Probe.TARGETED
        for episode in episodes
    )
    return targeted / len(episodes)


def run_experiment() -> dict[str, float | str]:
    train_episodes = make_episodes(
        count=20_000,
        seed=11,
        surface_offset=0,
    )
    test_episodes = make_episodes(
        count=4_000,
        seed=29,
        surface_offset=1_000_000,
    )

    train_surfaces = {episode.raw.surface_history for episode in train_episodes}
    test_surfaces = {episode.raw.surface_history for episode in test_episodes}
    assert train_surfaces.isdisjoint(test_surfaces)

    learner = RepairLearner(seed=7)
    pre_repair_probes: list[Probe] = []
    post_repair_probes: list[Probe] = []

    for index, episode in enumerate(train_episodes):
        was_repaired = learner.representation.active_feature is not None
        probe = learner.train_step(episode, index)
        if was_repaired:
            post_repair_probes.append(probe)
        else:
            pre_repair_probes.append(probe)

    nuisance_control = FixedRepresentationPolicy(
        Feature.NUISANCE,
        seed=17,
    )
    unrepaired_control = FixedRepresentationPolicy(
        None,
        seed=19,
    )
    for episode in train_episodes:
        nuisance_control.train_step(episode)
        unrepaired_control.train_step(episode)

    repaired_accuracy = reuse_accuracy(learner, test_episodes)
    nuisance_accuracy = nuisance_control.accuracy(test_episodes)
    unrepaired_accuracy = unrepaired_control.accuracy(test_episodes)

    repaired_capacity = representation_capacity(
        learner.representation,
        test_episodes,
    )
    nuisance_capacity = representation_capacity(
        nuisance_control.representation,
        test_episodes,
    )

    paired_surface = (9_999_999, 1, 2)
    pair_a = RawObservation(paired_surface, diagnostic_bit=0, nuisance_bit=1)
    pair_b = RawObservation(paired_surface, diagnostic_bit=1, nuisance_bit=1)
    persistent_split = (
        learner.representation.encode(pair_a)
        != learner.representation.encode(pair_b)
    )
    nuisance_does_not_split_pair = (
        nuisance_control.representation.encode(pair_a)
        == nuisance_control.representation.encode(pair_b)
    )

    pre_probe_rate = (
        sum(probe is Probe.TARGETED for probe in pre_repair_probes)
        / len(pre_repair_probes)
    )
    post_probe_rate = (
        sum(probe is Probe.TARGETED for probe in post_repair_probes)
        / len(post_repair_probes)
    )
    heldout_probe = held_out_probe_rate(learner, test_episodes)

    assert learner.repair_feature is Feature.DIAGNOSTIC
    assert persistent_split
    assert nuisance_does_not_split_pair
    assert repaired_capacity == nuisance_capacity == 2
    assert repaired_accuracy > nuisance_accuracy + 0.3
    assert repaired_accuracy > unrepaired_accuracy + 0.3
    assert heldout_probe == 0.0

    return {
        "repair_feature": learner.repair_feature.value,
        "repair_episode": float(learner.repair_episode),
        "pre_repair_targeted_probe_rate": pre_probe_rate,
        "post_repair_targeted_probe_rate": post_probe_rate,
        "heldout_targeted_probe_rate": heldout_probe,
        "transfer_accuracy_repaired": repaired_accuracy,
        "transfer_accuracy_nuisance_control": nuisance_accuracy,
        "transfer_accuracy_unrepaired": unrepaired_accuracy,
        "representation_capacity_repaired": float(repaired_capacity),
        "representation_capacity_control": float(nuisance_capacity),
        "surface_history_overlap": 0.0,
    }


if __name__ == "__main__":
    results = run_experiment()
    for name, value in results.items():
        if isinstance(value, float):
            print(f"{name}: {value:.4f}")
        else:
            print(f"{name}: {value}")
