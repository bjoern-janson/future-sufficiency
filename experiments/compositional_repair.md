# Compositional Repair — Experiment 004

## Purpose

Experiment 003 established persistent representation repair by selecting a useful feature from a pre-specified two-feature bank.

This experiment tests the next stronger claim:

> A learner can construct a future-relevant distinction compositionally from raw inputs, promote it into persistent state, and reuse it on unseen raw configurations without probing again.

The target chain is:

    detect
    -> probe
    -> construct
    -> persist
    -> transfer

## Information boundary

Each episode exposes a 16-bit raw observation:

    o = (b_0, b_1, ..., b_15)

The hidden state is determined by an evaluator-only compositional rule:

    z* = b_3 XOR b_12

Neither source bit alone identifies the hidden state:

    b_3 !-> z*
    b_12 !-> z*

The initial internal representation is fully aliased:

    M_0(o) = ("aliased",)

A targeted probe reveals the hidden state for the current episode at positive cost.

The learner is never given:

- `Gamma_I`;
- the source-bit indices;
- the correct expression;
- a precomputed `diagnostic_bit`;
- a repair label;
- the correct terminal action.

## Construction mechanism

Instead of choosing from named candidate features, the learner receives a small expression grammar over raw dimensions:

    atom(b_i)
    xor(b_i, b_j)
    and(b_i, b_j)
    or(b_i, b_j)

Probe-labeled examples are used to score synthesized expressions by how well their induced binary partition predicts the revealed latent state.

If one expression crosses the preregistered accuracy and margin thresholds, it is promoted persistently:

    M_t(o) = ("aliased",)

becomes:

    M_{t+1}(o) = ("split", e*(o))

where `e*` is the learned expression.

This is **grammar-bounded compositional construction**. It is stronger than selecting a supplied `diagnostic_bit`, but it is not open-ended representation invention because the operator grammar is still specified in advance.

## Raw-dimension pressure

The learner sees 16 raw bits. Only two participate in the true latent distinction.

The remaining dimensions create many equally cheap candidate partitions and compositions. The learner must allocate its one-bit representational split to the distinction supported by probe evidence.

## Transfer test

Training and test sets contain disjoint raw bit configurations:

    train raw configurations ∩ test raw configurations = empty

The latent composition rule is shared.

Held-out evaluation freezes the learned representation and disables probing. Success therefore requires reuse of the constructed rule, not memorization of training observations.

## Controls

Use two controls.

1. **Unrepaired control**
   - one aliased internal state;
   - no constructed expression.

2. **Equal-complexity shuffled-label control**
   - uses the same probe-labeled raw inputs;
   - shuffles the hidden labels before representation synthesis;
   - constructs a binary XOR expression with the same operator complexity as the repaired representation;
   - trains its terminal policy on the same environment.

The critical constraints are:

    capacity(repaired) = capacity(control) = 2

and:

    expression complexity(repaired)
    =
    expression complexity(control)

while the learned distinction differs.

## Primary criteria

A positive result requires:

1. **Information acquisition before repair**
   - targeted probing occurs while `M` is aliased.

2. **Compositional construction**
   - the learned expression is a composition rather than a single raw dimension;
   - neither source bit alone reaches high held-out predictive accuracy.

3. **Persistent repair**
   - the constructed expression becomes the persistent representation.

4. **Probe independence**
   - the frozen held-out policy no longer requires the targeted probe.

5. **Novel-configuration transfer**
   - repaired no-probe accuracy is high on raw configurations never seen during training.

6. **Equal-complexity advantage**
   - repaired transfer exceeds the shuffled-label control despite equal state cardinality and equal expression complexity.

The decisive comparison is:

    P(correct | constructed future-relevant split)
    >
    P(correct | equal-complexity irrelevant split)

## Interpretation boundary

A positive result would establish:

    probe-labeled experience
    -> compositional distinction construction
    -> persistent representation change
    -> no-probe transfer on unseen raw configurations
    -> improved future action

It would not establish unrestricted representation invention.

The learner still searches within a fixed grammar. The next stronger wall would be whether the system can expand or alter its own representation language when the required distinction is not expressible in the current grammar.

No Glimmer integration is included here.

**Scientific rule:** empirical obligation > further abstraction.
