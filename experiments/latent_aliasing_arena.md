# Latent-Aliasing Arena — Experiment 002

## Purpose

The first arena was a positive control: a visible regime cue made closure defect behaviorally recoverable. This version removes that shortcut.

The learner never observes `Gamma_I`, a regime label, or a current context marker that directly identifies whether probing has value.

A necessary information-theoretic constraint is retained: if aligned and divergent cases were literally identical in all pre-probe information, no policy could selectively probe between them. Therefore `Gamma_I` is **latent but inferable from experienced history**, while the hidden state needed for the terminal decision remains unavailable without the targeted probe.

## Hidden regimes

Each block is one of three latent regimes:

- **aligned** — `x_a` and `x_b` have the same optimal terminal action;
- **divergent** — `x_a` and `x_b` require different terminal actions;
- **misleading** — a superficial nuisance cue matches the divergent regime, but the futures are aligned.

At the probe decision itself, the current observation is identical across regimes. The learner may condition only on its observed history and the known probe cost.

## History

Before the probe decision, the learner experiences two forced `LEFT` trials, one from each hidden state in random order.

The nuisance cue is:

    aligned:     0
    divergent:   1
    misleading:  1

The reward history is:

    aligned:     (1, 1)
    divergent:   (1, 0) or (0, 1)
    misleading:  (1, 1)

Thus the nuisance cue alone is insufficient: `divergent` and `misleading` share it. The useful signal is the experienced future inconsistency under the aliased representation.

## Probe decision

The learner chooses:

    no probe
    generic probe
    targeted probe

The generic and targeted probes have equal cost and each reveal one bit.

- **generic** reveals a decision-irrelevant nuisance bit;
- **targeted** reveals whether the target state is `x_a` or `x_b`.

The learner is never given the true regime, `Gamma_I`, or true VOI.

## Cost sweep

Use probe costs:

    0.1, 0.3, 0.6

In the divergent regime the targeted probe has gross decision value `0.5`, so the optimal qualitative threshold is:

    cost < 0.5  -> probe
    cost > 0.5  -> do not probe

In aligned and misleading regimes the targeted probe has no gross decision value and should not be purchased at any positive cost.

## Primary behavioral criteria

On held-out block sequences:

    P(targeted | divergent, cost < 0.5) high
    P(targeted | divergent, cost > 0.5) low
    P(targeted | misleading) low
    P(targeted | aligned) low

The coarser evaluator-only diagnostic remains:

    P(targeted | Gamma_I = 1) > P(targeted | Gamma_I = 0)

but this is not supplied to the learner.

A shuffled-`Gamma_I` control should erase that association.

## Interpretation boundary

A positive result here means a small learner can infer **information demand from reward history** rather than from an explicit defect cue, and can scale acquisition with information cost.

It still does not establish representation repair or self-model adequacy. Those require a later test in which the acquired distinction persists as a changed internal representation and alters policy on new futures.

No Glimmer integration is included in this experiment.
