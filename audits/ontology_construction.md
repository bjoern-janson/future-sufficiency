# Ontology Construction Audit

This audit attacks the surviving scaffold after representation-ontology selection:

    designer supplies ontology-generating families
    -> learner selects and instantiates one

It is **not Experiment 009**.

## Central question

The ontology-selection audit allowed the learner to choose among supplied families such as subsets, relations, partitions, predicates, operators, and temporal motifs.

This audit removes that family menu.

The question is:

> Can future repair consequences induce a reusable representation constructor that was not present in the learner's initial online ontology?

The target chain is:

    future discrepancy
    -> synthesize operation over primitive objects
    -> bind higher-order constructor
    -> instantiate new repair objects
    -> reuse constructor on an unseen task

The intended distinction is:

    ontology selection
    !=
    ontology construction

## Important operational boundary

In a finite toy system, calling an arbitrary new subset a "new ontology" would be too weak.

The persistent object in this audit must therefore be a **higher-order constructor**:

    C : (A, B, C) -> R

that maps three task-local primitive representation objects to a repair object.

The constructor itself is absent from the initial online ontology `O0`.

It must be synthesized from lower-level operations and then reused on new primitive objects.

This establishes construction of a reusable representation family **relative to a supplied lower-level algebra**.

It does **not** establish unrestricted mathematical type-system invention. The output sort remains set-valued, and the constructor signature `(set, set, set) -> set` is supplied.

## Raw relational substrate

There are sixteen opaque structural states and eight opaque binary relations.

Evaluator-only, the relations are generated on a 4 x 4 torus. The learner never receives coordinates or semantic relation names.

It observes only encoded relation-history events:

    (relation_id, source_id, target_id)

Every audit run independently permutes:

- state IDs;
- relation IDs.

Primitive task-local objects are reconstructed as relation fibers from this history.

Thus the constructor operates on objects recovered from relational experience rather than on meaningful designer descriptors.

## Lower-level object algebra

For a task, three primitive objects are placed in anonymous ordered slots:

    x
    y
    z

The learner has primitive membership operations:

    NOT
    AND
    OR

and syntax-tree composition.

These operations are lifted pointwise over object membership.

No ontology-family names are supplied.

### Initial online ontology O0

`O0` contains every distinct ternary constructor expressible with at most three syntax-tree nodes.

There are:

    12 O0 constructor semantics

### Construction language

The audit permits synthesis up to nine nodes using the same lower-level algebra.

After semantic deduplication there are:

    127 constructor semantics

The learner therefore receives a compositional object algebra, not an enumerated menu of ontology families.

## Deterministic hidden constructor

The evaluator does not manually select a convenient target formula.

It deterministically searches the finite audit space for the first constructor/task configuration satisfying all of the following:

1. the constructor depends on all three primitive object slots;
2. its minimum program size exceeds the O0 budget;
3. each training task has exact O0 ceiling `0.875`;
4. each training task individually is compatible with multiple full constructor semantics;
5. pooling the two training tasks uniquely identifies one full constructor;
6. the two training tasks jointly expose all eight Boolean membership patterns;
7. the transfer task also has O0 ceiling `0.875`;
8. every primitive relation used by the transfer task is absent from both training tasks.

The resulting hidden constructor is:

    and(x, not(or(y, z)))

with six syntax-tree nodes.

Its three tasks are:

    train A: anchor 0, relations (0, 1, 3)
    train B: anchor 5, relations (0, 4, 5)
    transfer: anchor 10, relations (2, 6, 7)

All three transfer relations are unseen during constructor induction.

## Cross-task identifiability

A single task must not identify the reusable constructor.

For the deterministic case:

    task A -> 2 full constructors fit perfectly
    task B -> 4 full constructors fit perfectly

but:

    task A + task B -> exactly 1 full constructor fits

Therefore:

    local repair success
    !=
    ontology-family identification

The higher-order constructor becomes identifiable only by pooling consequences across tasks.

## Equal-error structure

For all three tasks:

    best O0 accuracy = 0.875
    base error       = 0.125

The synthesized constructor reaches:

    1.0

Thus the representation gain is:

    Delta = 0.125

Use:

    H = 100
    repair cost = 5

When validated future consequence is active:

    VOI = H * Delta = 12.5 > 5

so the mutable condition may bind the new constructor.

## Fixed-O0 counterfactual

The fixed condition receives the same:

- encoded relation history;
- repair probes;
- consequence probes;
- full 127-constructor search;
- O0 search;
- counterfactual transfer scoring;
- memory allocation;
- nine-node storage reservation.

It may discover which higher-order constructor would fit.

It is forbidden only from persisting a constructor outside `O0`.

It therefore binds its best O0 constructor.

The causal contrast is:

    permission to add a synthesized constructor to the online representation ontology

not:

    more data
    more search
    more compute
    more memory
    more storage

## Cross-encoding invariance

Run 32 independent encodings.

For every encoding:

- state IDs are permuted;
- relation IDs are permuted;
- raw relation history is transformed accordingly;
- no semantic coordinates or relation labels are available.

Required result:

    exact constructor recovery = 1.0
    mutable transfer           = 1.0
    fixed-O0 transfer          = 0.875

This attacks memorization of particular state or relation IDs.

## Transfer criterion

After induction on the two training tasks:

1. freeze the synthesized constructor;
2. do not perform another constructor search for authority acquisition;
3. apply the frozen constructor to three primitive relation fibers whose relation identities were never used during training.

The decisive result is:

    constructor learned on A,B
    -> constructor frozen
    -> instantiate on unseen primitive objects in C
    -> exact transfer

The persistent object is therefore not either training repair mask.

It is the constructor schema itself.

## Mechanical resource audit

Both branches meter:

    repair probes
    value probes
    raw history events
    history checks
    constructor evaluations
    constructor executions
    memory cells
    storage slots

The snapshots must match exactly.

The current deterministic per-encoding meter is:

    repair probes:             32
    value probes:              32
    history events:           384
    history checks:          3456
    constructor evaluations:  266
    executions:              6480
    memory cells:            1216
    storage slots:              9

## Killer null

The null keeps the same:

    representational discrepancy = 0.125
    constructor search
    repair probes
    compute
    memory
    storage

but independently validates that repairing the discrepancy has no future consequence:

    validated consequence multiplier = 0

Therefore:

    estimated VOI = 0

and no new constructor may be bound.

Required result:

    E > 0
    and
    representational gain > 0
    and
    Delta future value = 0
    ->
    no ontology construction authority

This distinguishes representation discrepancy from warranted repair authority.

## Primary criteria

A positive audit requires all of the following:

1. the hidden constructor is outside `O0`;
2. both training tasks individually underdetermine the constructor;
3. pooled training uniquely identifies it;
4. all three tasks have O0 ceiling `0.875`;
5. transfer uses only primitive relation identities unseen during induction;
6. the mutable condition binds the synthesized constructor iff expected future value exceeds cost;
7. mutable transfer is `1.0`;
8. fixed-O0 transfer remains `0.875`;
9. the result survives all 32 state/relation encodings;
10. measured resource meters match exactly;
11. the zero-VOI null does not bind;
12. goal semantics and authority remain immutable.

## Interpretation boundary

Passing this audit supports the narrow statement:

    future consequences
    -> synthesize operation over primitive representation objects
    -> create reusable higher-order constructor
    -> persist constructor
    -> instantiate on unseen primitive objects

This is stronger than ontology-family selection because no menu such as:

    subset
    relation
    partition
    predicate
    operator
    temporal motif

appears in the learner's action space.

However, the remaining scaffold is explicit:

    designer supplies low-level object algebra
    +
    designer supplies higher-order constructor signature
    +
    bounded program synthesis
    ->
    learner constructs a new reusable family inside that meta-system

So a positive result is **ontology construction relative to a supplied compositional substrate**, not unrestricted invention of a new mathematical sort.

This is also the point where a competing description becomes important:

    ontology construction
    vs.
    increasingly expressive symbolic macro synthesis

That distinction should be audited before making a general recursive-capability claim.

The governance boundary remains:

    capability expansion != authority expansion
    meta-capability expansion != goal expansion

**Scientific rule:** empirical obligation > further abstraction.
