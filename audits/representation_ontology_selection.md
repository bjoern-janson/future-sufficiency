# Representation Ontology Selection Audit

This audit attacks the surviving scaffold after repair-unit granularity discovery:

    repair = relation-closed subset of states

It is **not Experiment 009**.

## Central question

The learner has already been required to discover repair membership and repair
cardinality. This audit asks a deeper question:

> Can future repair consequences determine what *kind of representational object*
> should carry the repair?

The target chain is:

    residual structure
    -> repair-consequence probes
    -> ontology choice
    -> object construction / binding
    -> held-out transfer

The correct ontology is never supplied as a task label.

## Common event universe

Every case uses the same finite universe of sixteen events.

Each event can be viewed through several raw structural forms:

- an event identity;
- an ordered pair `(u, v)` on a 4 x 4 grid;
- a four-bit observation sequence.

These raw forms support several possible representation ontologies. The audit
does not tell the learner which ontology is relevant to the current defect.

Every positive case has:

    base accuracy = 0.875
    base error    = 0.125

and uses exactly:

    12 repair-consequence probes
    4 held-out events

Thus residual-error magnitude and probe count do not identify the ontology.

## Candidate ontology universe

The supplied ontology vocabulary contains six heterogeneous object types:

1. **state subset**
   - cyclic contiguous subsets of event identities, lengths 2 through 5;

2. **edge relation**
   - relations over ordered pairs such as modular difference/sum, equality,
     inequality, and order;

3. **partition**
   - equivalence classes induced by every partition of four latent nodes;

4. **predicate**
   - two-literal conjunctions over the raw four-bit observation;

5. **operator**
   - graphs of all 24 permutations `v = pi(u)`;

6. **temporal motif**
   - length-2 and length-3 motifs occurring in the four-bit sequence.

After semantic deduplication, the combined universe contains:

    137 candidate repair objects

Some object semantics can be described by more than one ontology. Primary cases
are restricted to objects whose semantics are unique to one ontology family.

The selection procedure itself does not use ontology names. It scores candidate
objects only by agreement with observed repair consequences. The evaluator uses
the family identity only to determine whether the recovered object belongs to
the intended ontology.

## Deterministic primary cases

To avoid manually selecting favorable examples, the evaluator uses the same
deterministic rule for every ontology family:

1. enumerate family-unique candidate semantics;
2. enumerate four-event holdouts;
3. choose the first object/holdout pair for which the remaining twelve
   repair-consequence observations uniquely identify that object among all
   137 candidate semantics.

This yields one matched case for each ontology family.

The learner receives neither:

    true ontology
    selected object identity
    held-out membership

## Repair consequences

For each observed event the learner receives whether a local repair has positive
future value in that context.

The hidden repair object determines those consequences:

    event in hidden object      -> local repair gain = 0.125
    event outside hidden object -> local repair gain = 0

A candidate is evaluated by how accurately its membership predicts those
observed consequences.

The mutable condition may bind the best positive-value object from any ontology.

## Fixed-ontology counterfactual

The matched baseline has a frozen representational ontology:

    state subset

It receives the same:

- raw event universe;
- repair-consequence probes;
- complete 137-candidate inspection;
- candidate scoring;
- held-out counterfactual scoring;
- memory allocation;
- storage reservation.

It may diagnose that a non-subset object fits better, but it cannot persist a
repair object outside its fixed ontology.

The causal contrast is therefore:

    ontology mutation permission

rather than:

    more probes
    more search
    more memory
    more storage

## Mechanical resource audit

Both branches meter:

    probe count
    candidate evaluation count
    execution count
    memory cells
    storage slots

The meter snapshots must match exactly.

The fixed and mutable branches also perform identical evaluator-side held-out
counterfactual scoring of every candidate object. Only the bound ontology/object
determines the acted-on transfer.

## Primary criteria

A positive result requires:

1. all six cases have exactly the same base error: `0.125`;
2. the mutable condition selects the correct ontology in every case;
3. the selected object transfers perfectly to the four held-out events;
4. the fixed-subset baseline is exact only when the true ontology is a subset;
5. resource meters match exactly;
6. the correct ontology is not supplied as an input;
7. goal semantics and authority remain immutable.

## Killer null

Use the same:

    base error = 0.125
    12 probes
    4 held-out events
    137 candidate inspections

but make every observed local repair gain equal to zero.

Then:

    VOI(ontology mutation) = 0

and neither condition may bind a repair object.

Required result:

    E > 0
    and
    estimated repair value = 0
    ->
    no ontology mutation

## Interpretation boundary

Passing this audit would establish a narrow form of **representation ontology
selection**:

    future value
    -> choose object type
    -> bind object
    -> transfer

It would weaken the assumption:

    repair must be a state subset

because equal-error cases require six different representational object types.

It would **not** establish construction of an ontology absent from the supplied
ontology vocabulary.

The remaining scaffold would be:

    designer supplies the ontology-generating vocabulary
    -> learner selects and instantiates an ontology within it

The next stronger question would therefore be whether a system can construct a
new representational ontology from raw relational experience rather than choose
among supplied ontology constructors.

The governance boundary remains:

    capability expansion != authority expansion
    meta-capability expansion != goal expansion

**Scientific rule:** empirical obligation > further abstraction.
