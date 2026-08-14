# Persistent Repair Transfer — Experiment 003

## Purpose

Experiment 002 established that a tabular learner can infer information demand from reward history without observing `Gamma_I`.

This experiment tests the next stronger claim:

> A closure-relevant distinction acquired through probing can be promoted into a persistent internal representation and reused on novel surface histories without probing again.

The target chain is:

    detect
    -> probe
    -> split
    -> reuse

## Information boundary

Each episode contains:

- a latent state: `x_a` or `x_b`;
- a visible but deliberately compressed raw record;
- two candidate one-bit features:
  - `diagnostic_bit`
  - `nuisance_bit`;
- a unique surface history.

Initially the policy uses:

    M_0(raw) = ("aliased",)

so:

    M_0(x_a) = M_0(x_b)

even though the raw record contains candidate distinctions that the current representation discards.

A costly targeted probe reveals the hidden state for the current training episode only.

The probe does **not** directly modify the policy representation.

Instead, probed examples provide labels that a generic feature selector can use to decide whether one candidate distinction should be promoted into `M`.

The learner is never given:

- `Gamma_I`;
- a "repair now" label;
- the identity of the useful feature;
- the correct terminal action.

## Repair rule

The representation has a fixed candidate feature bank:

    {diagnostic_bit, nuisance_bit}

After enough targeted probe labels, the learner compares how well each candidate feature predicts the revealed latent state.

If one candidate is sufficiently accurate and sufficiently better than the alternative, it is promoted persistently:

    M_t(raw) = ("aliased",)

becomes:

    M_{t+1}(raw) = ("split", selected_feature(raw))

A successful closure-relevant repair therefore yields:

    M_{t+1}(x_a) != M_{t+1}(x_b)

for the diagnostic distinction.

This is **feature promotion**, not open-ended representation invention. The candidate features are supplied in advance.

## Transfer test

Training and test episodes use disjoint surface histories:

    train histories ∩ test histories = ∅

The latent distinction and candidate feature semantics are shared.

Held-out transfer is evaluated with **no targeted probe required**. The question is whether the persistent repaired representation supports the correct terminal action on unseen surface histories.

## Controls

Use two controls:

1. **unrepaired control**
   - one aliased internal state;
   - no promoted feature.

2. **matched-capacity nuisance control**
   - two internal states;
   - same binary representation capacity as the repaired learner;
   - split is based on `nuisance_bit`, not the closure-relevant distinction.

The critical complexity constraint is:

    capacity(repaired) = capacity(nuisance control)

while the represented distinction differs.

## Primary criteria

A positive result requires all of the following:

1. **Probe before repair**
   - the learner uses the targeted probe while the representation is aliased.

2. **Persistent split**
   - the selected feature is the diagnostic feature;
   - the repaired representation maps matched `x_a` and `x_b` cases to different internal states.

3. **Probe independence after repair**
   - a frozen greedy policy no longer needs the targeted probe on held-out episodes.

4. **Transfer**
   - repaired no-probe policy accuracy on unseen surface histories exceeds the unrepaired control.

5. **Matched-capacity advantage**
   - repaired no-probe policy accuracy exceeds the nuisance-split control despite equal representation cardinality.

The decisive comparison is:

    P(correct reuse | repaired)
    >
    P(correct reuse | matched-capacity nuisance split)

on disjoint held-out surface histories.

## Interpretation boundary

A positive result would establish a narrow form of persistent representation repair:

    probe-labeled experience
    -> select missing distinction
    -> persistently split internal state
    -> reuse split on novel histories
    -> improve future action

It would **not** establish open-ended representation invention, self-model adequacy, or consciousness.

The repair mechanism still operates over a pre-specified candidate feature bank.

**Scientific rule:** empirical obligation > further abstraction.
