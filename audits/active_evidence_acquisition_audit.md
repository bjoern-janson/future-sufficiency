# Active Evidence Acquisition Audit

Status: inference-to-agency successor to the frozen epistemic baselines `f4f2f33` and `3166f5b`.

This is **not Experiment 009** and does not extend the capability ladder.

It introduces only one new stage:

    inferred decision structure
    -> choose which already-admissible challenge to run
    -> receive new evidence
    -> update D/R/S inference

There is no repair construction, repair authorization, binding, persistence, or self-modification.

## Question

Given:

1. an evidence-action topology already shown sufficient for identifiability (`f4f2f33`); and
2. a learner already shown able to recover the D/R/S decision function from sufficient evidence (`3166f5b`),

can the loop choose the admissible anonymous challenge that most efficiently resolves its current decision ambiguity?

The target distinction is:

    active identifiability
    !=
    active epistemic competence

The audit asks whether a distinguishing path that exists in the interface can actually be selected.

## Frozen upstream topology

The evidence/action topology is unchanged:

    local_residual          passive
    alternative_fit_probe   active
    consistency_probe       active
    future_value_probe      active

The three active probes remain exactly the admissible challenge paths inherited from `f4f2f33`.

The audit does not add a new sensor, probe, oracle, challenge permission, or action type.

Challenge identities are semantically hidden. Across the same 64 fixed-seed channel encodings used by the epistemic-recovery audit:

- the four columns are permuted;
- each binary polarity is independently flipped.

The policy sees anonymous columns and anonymous binary tokens, not names such as `alternative_fit_probe`.

## Frozen inference stage

The audit reuses the inference mechanism from `3166f5b`:

- finite ordered decision lists over four anonymous binary channels;
- 16,827 semantically distinct candidate functions;
- the same five labeled teaching examples;
- exact recovery of the encoded evaluator D/R/S semantic function.

No larger learner is introduced.

The active stage receives the recovered semantic function and a partial evidence state. It does not receive evaluator-side channel meanings.

## Active episode

For each of the complete 16 binary evaluator worlds:

1. only the passive `local_residual` observation is initially revealed;
2. the other three anonymous channels are available as admissible active challenges;
3. the policy may select one challenge at a time;
4. the selected challenge reveals that world's token on the chosen anonymous channel;
5. the policy may select another challenge or `NO_PROBE`;
6. once it stops, it outputs only a terminal D/R/S prediction.

No D/R/S prediction is executed as a repair action.

Thus:

    challenge selection
    !=
    repair action

and:

    challenge selection
    !=
    repair authorization.

## Sequential decision value

A one-step greedy value rule is insufficient in this audit.

For example, after learning that residual is present and that no exact in-space alternative exists, either the consistency or future-value probe may have zero *immediate* classification gain while still being necessary as the first step of a two-probe path to distinguish `R` from `S`.

Therefore the evaluator and learner use a finite dynamic program over the remaining admissible challenge paths.

For a partial observation state `e`, define the current uniform completion set over the still-unknown binary channels. The terminal value of stopping is:

    10 * Bayes-optimal D/R/S accuracy under e

and each active challenge has the inherited cost:

    1

The recursive challenge value is:

    -1
    + expected optimal continuation value after the binary probe outcome.

The selected challenge maximizes this sequential decision value. Ties form the evaluator's optimal set `A*`.

The scalar `10` is evaluator scaffold for this finite audit, not a frozen theory-level utility function. Its role is to make correct D/R/S resolution worth the supplied unit challenge cost while still preferring shorter resolving sequences.

## Decision value is not raw information value

At the initial residual-positive state, each unobserved binary challenge has exactly:

    H(outcome) = 1 bit

under the supplied uniform completion distribution.

Yet the three challenges do not have equal sequential decision value.

The alternative-fit challenge is uniquely optimal because it can immediately identify `D` in half of the compatible worlds and otherwise reduces the problem to the `R/S` branch.

Thus the audit contains the explicit control:

    information gain > 0
    !=
    decision value > 0

and, more strongly at the initial state:

    equal raw information
    !=
    equal decision value.

A max-outcome-entropy baseline therefore has no semantic reason to choose the correct initial challenge. It ties all three anonymous probes and breaks ties by anonymous column index.

## Primary endpoint

At every challenge-decision point, the evaluator computes the optimal admissible set:

    A*(partial evidence)

including `NO_PROBE` when stopping is optimal.

The primary endpoint is:

    P(selected challenge in A*)

reported separately for:

- states where a probe is warranted;
- states where the correct action is `NO_PROBE`.

This makes information-acquisition termination visible rather than rewarding unconditional probing.

## Secondary endpoint

After the selected challenge sequence terminates, the learner emits only:

    D
    R
    or
    S

The secondary endpoint is terminal D/R/S accuracy over the complete 16-world family.

## Leakage / impossibility controls

The information-theoretic controls from `3166f5b` are retained.

Each frozen evidence component is masked by a constant-valued anonymous channel while keeping:

- four input columns;
- the same 16,827 inference semantics;
- the same five teaching labels;
- the same complete 16-world evaluation family.

The exact Bayes ceilings remain:

    remove local_residual          -> 11/16 = 0.6875
    remove alternative_fit_probe   -> 12/16 = 0.7500
    remove consistency_probe       -> 15/16 = 0.9375
    remove future_value_probe      -> 15/16 = 0.9375

No masked learner may exceed the information-theoretic ceiling of its observation quotient.

The diagnostic rule remains:

    active distinction unavailable + apparent perfect recovery
        -> leakage / invalid benchmark

not:

    exceptional active intelligence.

## Local deterministic result

The implementation was locally executed against a local reconstruction of the exported frozen inference interface before publication.

Across 64 hidden channel permutations / polarity flips and all 16 evaluator worlds per encoding:

    world episodes                         = 1024
    challenge decision points              = 1920
    warranted-probe decision points        = 896
    stopping decision points               = 1024

The decision-directed policy gives:

    P(selected probe or stop in A*)        = 1.0
    P(selected probe in A* | probe needed) = 1.0
    P(NO_PROBE | stopping optimal)          = 1.0
    terminal D/R/S accuracy                = 1.0

Probe use is selective:

    mean active probes per world            = 0.875
    maximum active probes                   = 3

The raw-information baseline gives:

    first residual-positive challenge accuracy = 0.3125
    overall accuracy when a probe is warranted = 0.6071428571

At every residual-positive first step, all three active challenges carry exactly one bit of outcome entropy, while the decision-directed evaluator has a unique optimal challenge.

The masked information controls remain below or at their exact ceilings:

    local_residual
        max learner = 10/16 = 0.6250
        ceiling     = 11/16 = 0.6875

    alternative_fit_probe
        max learner = 10/16 = 0.6250
        ceiling     = 12/16 = 0.7500

    consistency_probe
        max learner = 15/16 = 0.9375
        ceiling     = 15/16 = 0.9375

    future_value_probe
        max learner = 15/16 = 0.9375
        ceiling     = 15/16 = 0.9375

No GitHub Actions CI claim is made.

## What this audit can earn

If independently reproduced, the narrow claim is:

> Within the frozen finite evidence-action topology and recovered D/R/S semantic function, a supplied sequential decision-value planner can select semantically anonymous admissible challenges so that every challenge/stop decision lies in the evaluator-optimal set, while terminating without unnecessary probing and preserving exact terminal D/R/S recovery across 64 channel encodings.

Equivalently:

    distinguishing challenge available
    +
    decision function recovered
    +
    decision-directed planner
    ->
    useful challenge selected.

This is evidence for **active epistemic competence relative to the supplied planning contract**.

It is not evidence for self-modification.

## What it does not earn

It does **not** establish:

- general scientific experiment design;
- learned research taste;
- discovery of the challenge topology;
- invention of a new challenge action;
- learning the experiment-selection objective from experience;
- optimal experiment selection under unknown priors;
- stochastic or continuous active causal discovery;
- challenge-authorization reasoning;
- repair construction;
- repair authorization;
- persistent binding;
- cross-family active epistemic recurrence;
- substrate-independent corrigibility.

The designer still supplies:

- the finite 16-world decision family;
- the frozen four-channel evidence topology;
- the D/R/S teaching labels and inference language from `3166f5b`;
- a uniform completion prior over unobserved binary channels;
- the sequential decision-value planner;
- the decision-correctness scale `10`;
- the inherited equal active-probe cost `1`;
- the admissibility of the three challenge actions.

## Interpretation rule

A useful challenge can be:

- available but not identifiable as useful;
- identifiable as useful but not selected;
- selected but not authorized;
- authorized but incorrectly executed.

This audit isolates only the second transition after the upstream epistemic stages have been frozen:

    available
    -> identifiable
    -> recoverable
    -> actively resolvable.

**Scientific rule:** information acquisition is valuable only relative to the decision distinctions it can resolve.
