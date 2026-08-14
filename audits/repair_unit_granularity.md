# Repair-Unit Granularity Audit

This audit attacks the hidden assumption that the learner already knows what size a repair unit should have.

It is **not Experiment 009**.

## Central question

The previous minimal-substrate audit removed semantic descriptors, but the candidate repair scope was still fixed at four states.

This audit asks:

> Can a learner infer both which structural states belong to a repair and how many states should count as one repair unit, using relational history plus repair consequences?

The target distinction is:

    discover repair membership
    !=
    discover repair granularity

## Opaque relational substrate

There are sixteen structural states, exposed only as arbitrary opaque IDs.

The evaluator defines a finite relation over those states. The latent world contains relation-closed components whose cardinalities include:

    2, 3, 4, 5

plus a distractor component.

The learner is never given component labels or latent coordinates.

Every audit run permutes the state IDs before observation.

## Unknown repair cardinality

The granularity-discovering condition searches every candidate scope with cardinality:

    1 <= |R| <= 6

for a total of:

    14,892 candidate scopes.

The true repair scopes have cardinalities:

    |R*| in {2, 3, 4, 5}.

Thus the correct size is never supplied.

The candidate objective is lexicographic:

1. satisfy observed repair consequences;
2. minimize relational boundary violations;
3. choose the smallest scope satisfying 1 and 2.

This encodes a relation-closure / minimality prior, but not a fixed repair size.

## Matched equal-error cases

Every true case begins with the same baseline accuracy:

    0.875

and therefore the same baseline error:

    E = 0.125.

A successful repair raises held-out accuracy to:

    1.0.

For each target repair unit the learner receives exactly four consequence observations:

- one positive repair consequence from inside the hidden unit;
- three non-positive consequences outside it.

The number of consequence observations does not reveal the true unit size.

The required responses are therefore:

    E = 0.125 -> discover |R*| = 2
    E = 0.125 -> discover |R*| = 3
    E = 0.125 -> discover |R*| = 4
    E = 0.125 -> discover |R*| = 5

Error magnitude cannot determine repair granularity.

## Fixed-granularity counterfactual

The fixed baseline receives exactly the same:

- opaque IDs;
- relational history;
- consequence observations;
- full candidate-scope search;
- candidate evaluations;
- memory;
- storage.

It may inspect the same discovered scope, but it is authorized to persist a repair only when:

    |R| = 4.

This deliberately isolates the causal difference:

    mutable repair granularity

rather than additional information or search.

## Cross-encoding invariance

Run all four true scope sizes under 64 arbitrary state-ID permutations.

A positive result requires:

    discovered_R(pi(world)) = pi(R*)

for every tested encoding.

## Information ablations

Repeat a subset of encodings under:

1. **outcomes only** — no relational history;
2. **history only** — no repair consequences;
3. **shuffled history** — same amount of relational data, independently misaligned with the consequences;
4. **opaque IDs only** — neither relation nor consequence evidence.

The full substrate should dominate these ablations in exact scope recovery.

## Killer null

Keep baseline error at:

    E = 0.125

but set observed future repair gain to zero.

The learner may still infer a coherent structural scope, but:

    VOI_repair = 0

so no mutation should be persisted.

Required behavior:

    coherent scope
    and
    no positive repair value
    ->
    no repair.

## Mechanical resource audit

The granularity-discovering and fixed-|R|=4 branches execute the same candidate-scope search.

The implementation measures:

    candidate scopes
    relation checks
    consequence checks
    history events
    memory cells
    storage slots

and requires the per-trial meter snapshots to match exactly.

## Primary criteria

A positive result requires all of the following:

1. exact scope recovery across true cardinalities 2, 3, 4, and 5;
2. exact recovery under all tested opaque-ID permutations;
3. the fixed-size-4 baseline succeeds only on the size-4 condition;
4. full-substrate held-out transfer exceeds the fixed baseline on the non-4 conditions;
5. outcomes-only, history-only, shuffled-history, and ID-only ablations lose exact recovery;
6. all true cases begin with identical baseline error 0.125;
7. the zero-VOI null does not trigger repair;
8. measured mutable/fixed resource meters match exactly;
9. goal semantics and authority remain immutable.

## Interpretation boundary

Passing this audit would support a narrow form of **repair-granularity discovery**:

    relational history
    +
    repair consequences
    ->
    infer repair membership
    +
    infer repair cardinality
    ->
    persistent transfer.

It would weaken the scaffold:

    designer fixes what size a repair unit must be.

It would **not** establish unconstrained discovery of what kind of object a repair unit should be.

The learner is still given:

- a finite sixteen-state universe;
- a relation-bearing substrate;
- the hypothesis that repairs are subsets of states;
- a bounded candidate cardinality range `1..6`;
- a relation-closure/minimality inductive bias.

The surviving question would therefore become:

    repair-unit granularity discovery
    vs.
    designer-supplied notion that a repair is a relation-closed state subset.

**Scientific rule:** empirical obligation > further abstraction.
