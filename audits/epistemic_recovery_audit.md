# Epistemic Recovery Audit

Status: inference-only successor to the frozen epistemic baseline `f4f2f33`.

This is **not Experiment 009**, does not extend the capability ladder, and introduces **inference only**.

It does not add or modify any evidence path, challenge authority, repair mechanism, authorization rule, binding operation, or persistence mechanism.

## Question

Given an evidence-action topology already proven sufficient for identifiability in principle, can a minimal inference process recover the warranted decision partition?

The causal ordering is held fixed as:

    availability
    -> identifiability
    -> inference

and the audit terminates at:

    predicted meta-action in {D, R, S}

No predicted action is executed.

## Frozen upstream baseline

The audit inherits the four-component admissible topology from `f4f2f33` unchanged:

    local_residual
    alternative_fit_probe
    consistency_probe
    future_value_probe

The prior audit established that the intact topology is sufficient for the evaluator-defined D/R/S partition and that deleting any one component creates a quotient defect.

This audit does not re-estimate that topology and does not permit any additional evidence source.

The conceptual contrast is now:

    impossible
    !=
    identifiable but uninferred
    !=
    inferred correctly

## Evaluator-side decision family

The four evidence components retain exactly the frozen meanings:

    residual_present
    exact_h0_alternative
    deterministic_residual
    positive_reopen_value

For the inference audit, the evaluator extends the five frozen worlds to the complete 16-signature binary family so held-out evidence combinations can be tested.

The evaluator-defined action rule is:

    residual and exact alternative
        -> D

    residual and no exact alternative and deterministic residual and positive reopen value
        -> R

    otherwise
        -> S

The implementation asserts that this rule reproduces all five original `f4f2f33` worlds exactly.

This extension of the world family is evaluator scaffold; it is not claimed as a universal D/R/S law.

## Channel semantics are hidden

The learner never receives the names or meanings of the four evidence components.

Across 64 fixed-seed encodings, the evaluator independently:

- permutes the four channel columns;
- flips the binary polarity of each channel.

Thus observed column 0 does not mean `local_residual`, and observed token `1` does not mean the canonical positive value.

The learner sees only:

    anonymous binary tuple -> D/R/S training label

and must infer a decision structure over those anonymous channels.

## Supplied inference language

The learner uses a finite language of ordered decision lists over anonymous binary channels.

A rule is a sequence of tests:

    if channel_j == token: output action

with a default terminal action.

Features may appear at most once in a rule.

Across four anonymous binary channels, semantic deduplication yields:

    16,827 unique decision functions

The target rule has minimum decision-list length 4.

The learner performs empirical risk minimization over this entire semantic hypothesis space using only the labeled teaching cases. Ties are resolved by shorter rule length and then a deterministic semantic ordering.

No evaluator-side channel role is available to the inference routine.

## Minimal teaching set and held-out combinations

Five labeled evidence signatures form a teaching set:

    (0,1,0,0) -> S
    (1,0,0,1) -> S
    (1,0,1,0) -> S
    (1,0,1,1) -> R
    (1,1,0,0) -> D

The implementation exhaustively verifies that:

1. exactly one semantic function in the supplied inference language is consistent with all five labels;
2. removing any one teaching example leaves more than one consistent semantic function.

So this is a minimal teaching set relative to the declared inference language.

The remaining:

    11 / 16

binary evidence combinations are held out from learning.

The primary inference question is therefore not signature memorization but whether the learned rule generalizes to unseen combinations.

A lookup baseline that memorizes the five training signatures and predicts the training-majority action elsewhere reaches only:

    8 / 11 = 0.727272...

held-out accuracy.

## Primary endpoint

For every one of 64 hidden channel encodings, the intact topology must satisfy:

    train accuracy   = 1.0
    heldout accuracy = 1.0
    full-universe accuracy = 1.0

while the oracle identifiability ceiling remains:

    1.0

The interpretation is narrow:

    distinction available in principle
    +
    minimal learner recovers it

not:

    general intelligence

or:

    general scientific inference.

## Information-theoretic ablation controls

Each of the four topology components is ablated again, but only as a leakage / ceiling control.

To match width and inference compute, deletion is implemented as a constant-valued anonymous channel. This removes world-dependent information while retaining:

- four input columns;
- the same 16,827 semantic candidates;
- the same five training labels;
- the same 11 held-out combinations;
- the same 16-combination evaluation universe.

For a uniform distribution over the 16 evaluator signatures, the Bayes-optimal recovery ceiling permitted by each ablated observation quotient is computed directly from the induced equivalence classes.

Preregistered ceilings are:

    remove local_residual          -> 11/16 = 0.6875
    remove alternative_fit_probe   -> 12/16 = 0.7500
    remove consistency_probe       -> 15/16 = 0.9375
    remove future_value_probe      -> 15/16 = 0.9375

The learner must never exceed these ceilings.

If it does, the audit is invalid because information has leaked around the declared interface.

This yields the diagnostic matrix:

    identifiable=0, recovered=0 -> epistemic impossibility
    identifiable=1, recovered=0 -> inference failure
    identifiable=1, recovered=1 -> epistemic recovery
    identifiable=0, recovered=1 -> leakage / invalid benchmark

## No downstream authority

The audit terminates at the predicted symbol:

    D
    R
    or
    S

There is explicitly no:

- discrimination action;
- hypothesis-language expansion;
- candidate repair construction;
- repair authorization;
- persistent binding;
- held-out repair transfer.

Therefore:

    inference
    !=
    action
    !=
    authorization.

The audit cannot earn a repair or governance claim.

## Local deterministic result

The implementation was locally executed before publication.

Across all 64 hidden channel permutations / polarity encodings, the intact topology gives:

    train accuracy         = 1.0
    heldout accuracy       = 1.0
    full-universe accuracy = 1.0

The signature-memorization baseline gives:

    heldout accuracy = 8/11 ~= 0.7273

The matched-width information ablations give the following full-universe learner accuracy / Bayes ceiling:

    local_residual
        10/16 = 0.6250 / 11/16 = 0.6875

    alternative_fit_probe
        10/16 = 0.6250 / 12/16 = 0.7500

    consistency_probe
        15/16 = 0.9375 / 15/16 = 0.9375

    future_value_probe
        15/16 = 0.9375 / 15/16 = 0.9375

No ablated learner exceeds its information-theoretic ceiling.

No GitHub Actions CI claim is made; this is a local deterministic execution result.

## What this audit can earn

If independently reproduced, the narrow claim is:

> Within the frozen four-channel finite evidence topology and a supplied ordered-decision-list inference language, a learner can recover the evaluator-defined D/R/S decision partition from five semantically anonymized teaching cases and generalize exactly to eleven held-out evidence combinations across 64 channel encodings.

This localizes the positive result to inference because:

- upstream evidence access is inherited from `f4f2f33`;
- identifiability was established independently before this audit;
- channel semantics are hidden;
- held-out combinations defeat exact signature lookup;
- ablated topologies obey their Bayes ceilings;
- no downstream action or authority is present.

## What it does not earn

It does **not** establish:

- general inference capability;
- learning from naturalistic evidence;
- optimal active experiment selection;
- discovery of the evidence topology itself;
- discovery of a new challenge channel;
- open-ended hypothesis-language invention;
- repair construction;
- repair authorization;
- persistent binding;
- cross-family epistemic recurrence;
- substrate-independent corrigibility.

The designer still supplies:

- the finite binary evidence family;
- the evaluator D/R/S contract;
- the ordered-decision-list inference language;
- the five labeled teaching cases;
- the admissible evidence-action topology inherited from `f4f2f33`.

One important finite-design limitation is explicit: under the frozen binary contract there is only one `R` signature, so that signature must occur in the teaching set. Held-out combination generalization therefore tests unseen D/S signatures; `R` is still evaluated in the full-universe recovery score but is not a held-out action class.

## Reproducibility

From the repository root:

```bash
python audits/epistemic_recovery_audit.py
```

The implementation uses only the Python standard library and fixed seeds.

## Interpretation rule

A failure on the intact topology is an inference failure only because `f4f2f33` independently established that the required decision distinction is available through the frozen interface.

A failure on an ablated topology must not be called an inference failure when it is bounded by the corresponding information-theoretic ceiling.

**Scientific rule:** impossible != available but uninferred.
