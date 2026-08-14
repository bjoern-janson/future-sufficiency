# Repair-Axis Discovery Audit

This audit attacks the strongest surviving scaffold explanation after the anti-limit-relaxation audit:

    repair-axis selection
    vs.
    repair-axis discovery

It is **not Experiment 009**.

## Claim under audit

The previous audit showed that identical residual error can require different repairs. However, the available repair axes were still designer-supplied.

This audit asks a narrower question:

> Can a learner synthesize which structural dimension of its generator should be modified when that dimension is not provided as a named repair axis?

The target chain is:

    residual structure
    -> infer missing repair dimension
    -> synthesize structural predicate
    -> bind repair
    -> transfer to a held-out task sharing the latent repair dimension

## What is hidden

Each optional representational primitive is associated with an anonymous four-bit structural descriptor:

    s = (s0, s1, s2, s3)

The learner is not told what any descriptor bit means.

A hidden repair axis is a predicate over these anonymous structural states. The primary hidden-axis universe contains all 24 minimal two-literal conjunctions that admit exactly four of the sixteen structural states.

Examples, shown only for evaluator interpretation, include predicates such as:

    s0 AND s1
    s0 AND NOT(s2)
    NOT(s1) AND s3

The learner never receives semantic axis names such as:

    reuse
    depth
    arity
    operator family

## Base representation language

The base semantic language is a finite read-once Boolean language over three inputs using:

    variable
    NOT
    AND
    OR

with a nine-node syntax-tree budget.

It contains 94 distinct semantics.

The evaluator deterministically selects sixteen optional target relations such that every one has exact base ceiling:

    Accuracy_base = 0.875

and no pair is equivalent up to output complementation.

Each optional target is assigned to one anonymous structural descriptor state.

## Generic repair language

The axis-discovering condition does not receive a list of repair dimensions.

It receives only a predicate-construction language over the anonymous descriptor bits:

    s0, s1, s2, s3
    NOT
    AND
    OR
    composition

with at most five predicate nodes.

This bounded language contains 90 distinct predicate semantics.

A synthesized predicate determines which optional primitives the repaired generator will admit.

Thus the mutable object is:

    admissible structural subset

not a named repair-axis token.

## Fixed-axis baseline

The fixed-axis condition is restricted to eight designer-supplied one-bit literals:

    s0, NOT(s0), ..., s3, NOT(s3)

It cannot persist a compositional repair dimension.

To match search effort, it spends the same number of candidate slots by deterministically rescoring its fixed literal axes.

Both conditions reserve the same five-node predicate storage slot.

## Hidden-axis task construction

Every hidden axis admits exactly four structural states.

For each audit case:

1. Three admitted states define three training target relations.
2. The fourth admitted state defines a held-out target relation.
3. Every training and held-out target has the same base error:

       0.125

4. The identity of the hidden structural predicate is never supplied to the learner.

The axis-discovering condition must infer a predicate that explains why the same type of repair has value across the three training targets and then transfer that predicate to the fourth unseen target.

## Repair value

For a synthesized predicate `r`, let:

    g(r) = mean held-in gain across the three training relations

Use:

    H = 100

and define:

    gross_value(r) = H * g(r)

Repair cost contains:

    bind_cost = 1
    scope_cost = 2 * number_of_admitted_structural_states

so:

    net_value(r)
        = gross_value(r)
        - bind_cost
        - scope_cost

This prevents the trivial repair:

    admit everything

and forces the learner to allocate representational expansion selectively.

The fixed one-bit axes admit eight states and are therefore too broad to have positive value in the hidden compositional-axis cases.

## Hidden-axis universe and sampling

The evaluator defines a universe of 24 compositional axes satisfying:

    predicate scope = 4 states
    predicate complexity <= 4 nodes
    predicate is not a one-bit literal

The primary audit samples twelve axes using a fixed seed.

In addition, an evaluator-only completeness check asks whether the same discovery procedure would recover all 24 axes.

The learner does not receive the axis identity in either analysis.

## Brutal null

The null uses an OR relation already exactly represented by the base language, but each input row contains one contradictory label in eight repetitions.

Therefore:

    held-out residual error = 0.125

while:

    value(any repair axis) <= 0

The required behavior is:

    no mutation

for both the fixed-axis and axis-discovering conditions.

This tests:

    structural residual -> repair discovery

against the degenerate policy:

    nonzero residual -> invent some repair dimension

## Mechanical resource matching

The implementation measures:

    probe count
    axis-candidate count
    semantic-candidate count
    execution count
    memory cells
    storage slots

The fixed-axis and axis-discovering branches must match exactly on these quantities for every primary case and the null.

On held-out evaluation, both branches score the same counterfactual languages; only the persisted repair binding determines which result is acted upon.

## Primary criteria

A positive result requires all of the following:

1. All sampled hidden axes are recovered without axis labels.
2. The discovered predicate transfers to the fourth, unseen target relation.
3. Axis-discovering held-out accuracy is `1.0`.
4. The matched fixed-axis baseline remains at `0.875`.
5. The evaluator-only completeness check recovers all 24 axes in the hidden-axis universe.
6. The null retains `0.125` residual error but triggers no repair.
7. Measured probe, candidate, execution, memory, and storage budgets match exactly.
8. Goal semantics and authority remain immutable.

## Interpretation boundary

Passing this audit would support:

    repair-axis discovery within a supplied structural predicate language

rather than merely:

    selection among named repair axes

It would **not** establish arbitrary repair-axis invention.

The experiment designer still supplies:

    anonymous descriptor coordinates
    the predicate-construction language
    the repair-binding mechanism

So the surviving scaffold would move to:

    designer supplies the vocabulary from which repair dimensions can be composed

rather than:

    designer enumerates the repair dimensions themselves

That is a meaningful but bounded reduction in scaffolding.

The governance boundary remains fixed:

    capability expansion != authority expansion

and:

    meta-capability expansion != goal expansion

**Scientific rule:** empirical obligation > further abstraction.
