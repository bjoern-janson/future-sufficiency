"""Compositional representation-construction experiment.

A learner starts with a one-state representation over raw binary observations.
Targeted probes reveal the hidden state for the current episode. From those
labels, the learner synthesizes a binary expression from a small operator
grammar and promotes it into persistent state.

Gamma_I, the true source bits, and the correct expression are evaluator-only.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum, IntEnum
from random import Random
from typing import Iterable


N_BITS = 16
TRUE_SOURCE = (3, 12)


class HiddenState(IntEnum):
    A = 0
    B = 1


class Action(str, Enum):
    LEFT = "left"
    RIGHT = "right"


class Probe(str, Enum):
    NONE = "none"
    TARGETED = "targeted"


class Op(str, Enum):
    ATOM = "atom"
    XOR = "xor"
    AND = "and"
    OR = "or"


@dataclass(frozen=True)
class Expression:
    op: Op
    i: int
    j: int | None = None

    def evaluate(self, bits: tuple[int, ...]) -> int:
        left = bits[self.i]
        if self.op is Op.ATOM:
            return left
        if self.j is None:
            raise ValueError("binary expression requires j")
        right = bits[self.j]
        if self.op is Op.XOR:
            return left ^ right
        if self.op is Op.AND:
            return left & right
        if self.op is Op.OR:
            return left | right
        raise ValueError(self.op)

    def complexity(self) -> int:
        return 0 if self.op is Op.ATOM else 1

    def __str__(self) -> str:
        if self.op is Op.ATOM:
            return f"b{self.i}"
        return f"{self.op.value}(b{self.i},b{self.j})"


@dataclass(frozen=True)
class RawObservation:
    bits: tuple[int, ...]
    sample_id: int


@dataclass(frozen=True)
class Episode:
    raw: RawObservation
    hidden: HiddenState


@dataclass
class Representation:
    expression: Expression | None = None

    def encode(self, raw: RawObservation) -> tuple[str] | tuple[str, int]:
        if self.expression is None:
            return ("aliased",)
        return ("split", self.expression.evaluate(raw.bits))


@dataclass(frozen=True)
class ActionState:
    representation_state: tuple
    revealed_hidden: HiddenState | None = None


def hidden_from_bits(bits: tuple[int, ...]) -> HiddenState:
    i, j = TRUE_SOURCE
    return HiddenState(bits[i] ^ bits[j])


def terminal_reward(hidden: HiddenState, action: Action) -> float:
    if hidden is HiddenState.A:
        return 1.0 if action is Action.LEFT else 0.0
    return 1.0 if action is Action.RIGHT else 0.0


def expression_grammar() -> tuple[Expression, ...]:
    expressions: list[Expression] = [
        Expression(Op.ATOM, i) for i in range(N_BITS)
    ]
    for i in range(N_BITS):
        for j in range(i + 1, N_BITS):
            for op in (Op.XOR, Op.AND, Op.OR):
                expressions.append(Expression(op, i, j))
    return tuple(expressions)


GRAMMAR = expression_grammar()
XOR_GRAMMAR = tuple(expression for expression in GRAMMAR if expression.op is Op.XOR)


def make_unique_episodes(
    count: int,
    *,
    seed: int,
    excluded_bits: set[tuple[int, ...]] | None = None,
    sample_offset: int = 0,
) -> list[Episode]:
    rng = Random(seed)
    used = set(excluded_bits or set())
    episodes: list[Episode] = []

    while len(episodes) < count:
        packed = rng.randrange(1 << N_BITS)
        bits = tuple((packed >> i) & 1 for i in range(N_BITS))
        if bits in used:
            continue
        used.add(bits)
        raw = RawObservation(bits=bits, sample_id=sample_offset + len(episodes))
        episodes.append(Episode(raw=raw, hidden=hidden_from_bits(bits)))

    return episodes


def best_binary_accuracy(
    expression: Expression,
    labels: Iterable[tuple[RawObservation, HiddenState]],
) -> float:
    labels = list(labels)
    correct = 0
    for value in (0, 1):
        hidden_labels = [
            hidden
            for raw, hidden in labels
            if expression.evaluate(raw.bits) == value
        ]
        if not hidden_labels:
            continue
        count_a = hidden_labels.count(HiddenState.A)
        count_b = hidden_labels.count(HiddenState.B)
        correct += max(count_a, count_b)
    return correct / len(labels)


class ConstructiveRepairLearner:
    """Tabular probe/action learner plus grammar-bounded expression synthesis."""

    def __init__(
        self,
        *,
        seed: int = 0,
        epsilon: float = 0.1,
        probe_cost: float = 0.2,
        min_probe_labels: int = 128,
        repair_accuracy: float = 0.95,
        repair_margin: float = 0.10,
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
        self.repair_expression: Expression | None = None
        self.repair_episode: int | None = None
        self.runner_up_accuracy: float | None = None

    def _choose(self, values: dict, state, choices: tuple, *, explore: bool):
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

    def _maybe_construct(self, episode_index: int) -> bool:
        if self.representation.expression is not None:
            return False
        if len(self.probe_labels) < self.min_probe_labels:
            return False

        scored = sorted(
            (
                (best_binary_accuracy(expression, self.probe_labels), str(expression), expression)
                for expression in GRAMMAR
            ),
            key=lambda item: (-item[0], item[1]),
        )
        best_accuracy, _, best_expression = scored[0]
        runner_up_accuracy = scored[1][0]

        if (
            best_accuracy >= self.repair_accuracy
            and best_accuracy - runner_up_accuracy >= self.repair_margin
        ):
            self.representation.expression = best_expression
            self.repair_expression = best_expression
            self.repair_episode = episode_index
            self.runner_up_accuracy = runner_up_accuracy
            return True
        return False

    def train_step(self, episode: Episode, episode_index: int) -> Probe:
        representation_state = self.representation.encode(episode.raw)
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
            (representation_state, probe),
            net_return,
        )

        if probe is Probe.TARGETED:
            self.probe_labels.append((episode.raw, episode.hidden))
        self._maybe_construct(episode_index)
        return probe

    def reuse_action(self, raw: RawObservation) -> Action:
        return self.choose_action(
            raw,
            Probe.NONE,
            None,
            explore=False,
        )


class FixedExpressionPolicy:
    """Matched tabular action learner for a fixed binary representation."""

    def __init__(
        self,
        expression: Expression | None,
        *,
        seed: int,
        epsilon: float = 0.1,
    ) -> None:
        self.representation = Representation(expression)
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


def synthesize_shuffled_xor_control(
    labels: list[tuple[RawObservation, HiddenState]],
    *,
    seed: int,
) -> Expression:
    """Synthesize an equal-complexity control after destroying label relation."""
    rng = Random(seed)
    raws = [raw for raw, _ in labels]
    hidden = [label for _, label in labels]
    rng.shuffle(hidden)
    shuffled = list(zip(raws, hidden))

    scored = sorted(
        (
            (best_binary_accuracy(expression, shuffled), str(expression), expression)
            for expression in XOR_GRAMMAR
        ),
        key=lambda item: (-item[0], item[1]),
    )
    return scored[0][2]


def representation_capacity(
    representation: Representation,
    episodes: Iterable[Episode],
) -> int:
    return len({representation.encode(episode.raw) for episode in episodes})


def held_out_probe_rate(
    learner: ConstructiveRepairLearner,
    episodes: Iterable[Episode],
) -> float:
    episodes = list(episodes)
    targeted = sum(
        learner.choose_probe(episode.raw, explore=False) is Probe.TARGETED
        for episode in episodes
    )
    return targeted / len(episodes)


def reuse_accuracy(
    learner: ConstructiveRepairLearner,
    episodes: Iterable[Episode],
) -> float:
    episodes = list(episodes)
    correct = sum(
        terminal_reward(episode.hidden, learner.reuse_action(episode.raw))
        for episode in episodes
    )
    return correct / len(episodes)


def expression_accuracy(
    expression: Expression,
    episodes: Iterable[Episode],
) -> float:
    labels = [(episode.raw, episode.hidden) for episode in episodes]
    return best_binary_accuracy(expression, labels)


def run_experiment() -> dict[str, float | str]:
    train_episodes = make_unique_episodes(
        12_000,
        seed=11,
        sample_offset=0,
    )
    train_bits = {episode.raw.bits for episode in train_episodes}
    test_episodes = make_unique_episodes(
        4_000,
        seed=29,
        excluded_bits=train_bits,
        sample_offset=100_000,
    )

    assert train_bits.isdisjoint({episode.raw.bits for episode in test_episodes})

    learner = ConstructiveRepairLearner(seed=7)
    pre_repair_probes: list[Probe] = []
    post_repair_probes: list[Probe] = []

    for index, episode in enumerate(train_episodes):
        was_repaired = learner.representation.expression is not None
        probe = learner.train_step(episode, index)
        if was_repaired:
            post_repair_probes.append(probe)
        else:
            pre_repair_probes.append(probe)

    if learner.repair_expression is None:
        raise AssertionError("representation was not repaired")

    shuffled_expression = synthesize_shuffled_xor_control(
        learner.probe_labels,
        seed=41,
    )
    nuisance_control = FixedExpressionPolicy(shuffled_expression, seed=17)
    unrepaired_control = FixedExpressionPolicy(None, seed=19)

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

    pre_probe_rate = (
        sum(probe is Probe.TARGETED for probe in pre_repair_probes)
        / len(pre_repair_probes)
    )
    post_probe_rate = (
        sum(probe is Probe.TARGETED for probe in post_repair_probes)
        / len(post_repair_probes)
    )
    heldout_probe = held_out_probe_rate(learner, test_episodes)

    learned_expression_accuracy = expression_accuracy(
        learner.repair_expression,
        test_episodes,
    )
    shuffled_expression_accuracy = expression_accuracy(
        shuffled_expression,
        test_episodes,
    )

    source_i, source_j = TRUE_SOURCE
    atom_i_accuracy = expression_accuracy(
        Expression(Op.ATOM, source_i),
        test_episodes,
    )
    atom_j_accuracy = expression_accuracy(
        Expression(Op.ATOM, source_j),
        test_episodes,
    )

    assert learner.repair_expression.op is Op.XOR
    assert {learner.repair_expression.i, learner.repair_expression.j} == set(TRUE_SOURCE)
    assert learned_expression_accuracy > 0.99
    assert atom_i_accuracy < 0.55
    assert atom_j_accuracy < 0.55
    assert repaired_capacity == nuisance_capacity == 2
    assert learner.repair_expression.complexity() == shuffled_expression.complexity() == 1
    assert repaired_accuracy > nuisance_accuracy + 0.30
    assert repaired_accuracy > unrepaired_accuracy + 0.30
    assert heldout_probe == 0.0

    return {
        "constructed_expression": str(learner.repair_expression),
        "repair_episode": float(learner.repair_episode),
        "runner_up_probe_label_accuracy": float(learner.runner_up_accuracy),
        "pre_repair_targeted_probe_rate": pre_probe_rate,
        "post_repair_targeted_probe_rate": post_probe_rate,
        "heldout_targeted_probe_rate": heldout_probe,
        "constructed_expression_test_accuracy": learned_expression_accuracy,
        "source_bit_i_test_accuracy": atom_i_accuracy,
        "source_bit_j_test_accuracy": atom_j_accuracy,
        "transfer_accuracy_repaired": repaired_accuracy,
        "control_expression": str(shuffled_expression),
        "control_expression_test_accuracy": shuffled_expression_accuracy,
        "transfer_accuracy_equal_complexity_control": nuisance_accuracy,
        "transfer_accuracy_unrepaired": unrepaired_accuracy,
        "representation_capacity_repaired": float(repaired_capacity),
        "representation_capacity_control": float(nuisance_capacity),
        "expression_complexity_repaired": float(learner.repair_expression.complexity()),
        "expression_complexity_control": float(shuffled_expression.complexity()),
        "raw_configuration_overlap": 0.0,
    }


if __name__ == "__main__":
    results = run_experiment()
    for name, value in results.items():
        if isinstance(value, float):
            print(f"{name}: {value:.4f}")
        else:
            print(f"{name}: {value}")
