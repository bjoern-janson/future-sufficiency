# Corrigible Adaptive Loop Principle

Status: meta-level methodological invariant frozen after `fc7d646`.

This document does **not** claim that the full invariant has already been empirically established across task families. It freezes the conceptual contract that future experiments must test rather than assume.

## Core principle

> **Future sufficiency is a property of a corrigible adaptive loop, not merely of a representation.**

Future sufficiency is not uncertainty preservation.

Instead, the candidate loop-level contract is:

    future sufficiency
    = warranted updating
    + reopenability
    + termination discipline

These terms are independently falsifiable requirements, not ingredients to be declared necessary by definition.

## Three-way requirement

### Warranted updating

The loop must change when evidence earns a revision.

Failure mode:

    evidence arrives
    -> current state is inadequate
    -> no warranted update occurs

### Reopenability

A previously accepted representation, hypothesis space, or repair must remain challengeable when new evidence exposes inadequacy.

Failure mode:

    locally successful closure
    -> challenge capacity lost
    -> later contradiction cannot reopen the model

### Termination discipline

The loop must stop revising when marginal warranted value disappears.

Failure mode:

    residual uncertainty
    -> perpetual expansion / modification
    -> no evidence-sensitive stopping condition

Therefore:

    reopenability != uncertainty maximization

and

    termination != irreversible closure.

The target is selective but corrigible closure.

## Selective and extensible hypothesis spaces

At the science level, the live hypothesis space `H_t` must be both selective and extensible.

Selective:

    if everything remains possible,
    discrimination and termination fail.

Extensible:

    if H* is not in H_t,
    efficient inference within H_t can converge on the least-wrong explanation.

The central science-level defect is therefore:

> **hypothesis-space closure without evidence that closure is warranted.**

## Object-level / science-level symmetry

The object under study performs:

    evidence
    -> representation update
    -> better future repair

The research program performs:

    experimental evidence
    -> dependency-model update
    -> better next experiment

The correspondence is:

| System level | Science level |
|---|---|
| state / world distinctions | dependency hypotheses |
| current representation | current hypothesis language |
| probe / action | experiment |
| repair | theory revision |
| persistent state change | retained dependency update |
| reopenability | hypothesis-space expansion / challenge retention |
| termination discipline | justified experimental stopping |

The symmetry does not imply that the same implementation governs both levels. It states that both are instances of a common corrigibility requirement:

    preserve enough structure for the next warranted corrective transformation to remain possible.

## Premature closure pair

Two analogous pathologies are now explicit.

Object-level premature closure:

    "this representation works"
    -> stop preserving challenge capacity
    -> future defect becomes undetectable

Science-level premature closure:

    "this explanation fits"
    -> stop retaining alternatives / challenge tests
    -> misspecification becomes invisible

Thus:

    premature object closure
    ||
    premature theory closure

are parallel failure modes.

## Closed-world / open-world empirical split

A future science-loop experiment should distinguish two regimes.

### Closed-world regime

    H* in H_0

Question:

> How efficiently does the experiment-selection policy discriminate among live hypotheses?

Primary metric family:

    within-space efficiency

Candidate comparisons include EIG-guided, random, and capability-gain-guided experiment selection, with matched experimental budgets.

### Open-world regime

    H* not in H_0

Question:

> Does the process detect model misspecification and reopen the hypothesis language rather than concentrate on the least-wrong in-space explanation?

Primary metric family:

    out-of-space detection

A process that is strong on within-space efficiency but weak on out-of-space detection is a canonical future-insufficient loop:

    highly efficient
    and
    structurally unable to recognize its own hypothesis-space insufficiency.

## Hypothesis-space expansion authority

Expansion is itself subject to evidence and cost.

The desired chain is:

    current alternatives exhausted
    + structured residual
    + expansion value exceeds cost
    -> expand hypothesis space

not:

    residual
    -> add arbitrary hypotheses.

This is the science-level analogue of the project's existing distinction:

    discoverable improvement != warranted persistent modification.

Likewise:

    conceivable explanation != warranted hypothesis-space expansion.

## Experiment-selection boundary

Expected information gain is useful only relative to the current hypothesis language.

If

    H* not in H_t,

then maximizing

    EIG(a | H_t)

can efficiently discriminate among wrong explanations.

Therefore EIG alone is not a complete future-sufficiency objective for science.

The eventual research objective may need to distinguish at least:

    within-space discrimination value
    challenge / misspecification value
    experiment cost
    future-closure damage

No exact scalar objective is frozen here. Those terms must be operationalized and empirically justified before being promoted into the formal theory.

## Candidate metrics for a future science-loop audit

Do not reduce success to posterior entropy reduction alone. Candidate outcomes include:

- dependency identification error;
- experimental cost to identification;
- false-closure rate;
- out-of-hypothesis-space detection;
- successful reopening rate;
- unnecessary reopening rate;
- correct termination rate.

These metrics remain candidates until a concrete audit preregisters them.

## Meta-level invariant

The methodological compression is:

    future sufficiency != uncertainty preservation

and instead:

    future sufficiency
    = warranted updating
    + reopenability
    + termination discipline

at the level of a corrigible adaptive loop.

The research symmetry is:

    system repairs its model
    ||
    science repairs its hypothesis space.

Both must remain capable of warranted change without collapsing into either irreversible closure or endless revision.

## Claim boundary

This principle currently earns a methodological role, not a universal empirical claim about intelligence.

The six candidate repair dependencies and the update/reopen/stop decomposition remain hypotheses under intervention. Their necessity and cross-family generality must still be earned under the rules in `EVIDENCE_MATRIX.md` and `GENERALITY_PRINCIPLE.md`.

**Scientific rule:** closure is warranted only while the loop preserves a licensed path for reality to reopen it.