# Minimal Repair Substrate Audit

This audit asks what information is actually necessary for discovering a repair dimension after the repair-axis discovery audit.

It is **not Experiment 009**.

## Central question

The surviving scaffold is:

    supplied structural descriptor vocabulary
    -> composed repair predicate

This audit removes meaningful descriptor features entirely.

The question becomes:

> What minimal representational substrate is sufficient for a learner to discover a reusable repair concept when structural states are opaque and the useful abstraction must be reconstructed from relations among observations and repair outcomes?

The target distinction is:

    compose supplied descriptors
    !=
    discover what should count as a descriptor

## Opaque structural states

There are sixteen latent structural states.

The learner receives only arbitrary opaque state IDs. State IDs carry no coordinate, feature, or repair-axis semantics.

The evaluator defines a latent relational system over those states. For reproducibility the finite world is a 4x4 rook relation, but row/column coordinates are evaluator-only and never exposed.

Two states are relational neighbors when they share one latent coordinate.

The learner does **not** receive those coordinates or a named `same-row`, `same-column`, `reuse`, `depth`, or operator-family feature.

Instead it observes an opaque transition history containing the relational edges.

## Hidden repair classes

The latent system contains eight four-state repair classes: four row classes and four column classes.

Again, `row` and `column` are evaluator-only descriptions. To the learner they are merely subsets that may or may not be recoverable from relational evidence.

For each audit trial:

1. choose one latent four-state repair class;
2. hold out one member;
3. provide positive repair outcomes for the other three members;
4. require the learner to infer whether the held-out opaque state belongs to the same reusable repair concept.

A correct persistent repair raises held-out task accuracy from:

    0.875 -> 1.0

No additional probe is allowed for the held-out member.

## Generic abstraction search

The learner is not given repair-axis predicates.

It considers all four-state subsets of the sixteen opaque states:

    C(16, 4) = 1820

Every candidate has identical cardinality.

Candidates are scored using only two evidence channels:

- **repair outcomes**: how many observed positive-repair states the candidate contains;
- **relational coherence**: how strongly the candidate members are connected in the transition history.

Thus the learner can succeed only by combining:

    outcome evidence
    +
    relational evidence

No supplied state descriptor tells it which members belong together.

## Cross-encoding invariance

For each latent repair class, arbitrarily permute the sixteen opaque state IDs:

    s -> pi(s)

and permute the transition history consistently.

The discovered repair scope must transform equivariantly:

    R(pi(s)) = pi(R(s))

Behavioral success must therefore depend on the latent relation rather than literal state IDs.

The executable tests:

    32 encodings
    x 8 latent repair classes
    x 4 possible held-out members
    = 1024 trials

## Information ablations

The same hidden classes are evaluated under five information conditions.

### Full substrate

    opaque IDs + transition history + repair outcomes

Prediction:

    exact repair-class recovery = 1.0

### Outcomes only

The learner knows which three opaque states showed positive repair value but receives no relational evidence.

Many four-state completions remain indistinguishable.

Prediction:

    exact recovery << 1.0

### History only

The learner sees the relational system but receives no repair outcomes identifying which latent class is currently relevant.

Prediction:

    relation structure alone is insufficient to select the task-relevant repair class

### Shuffled history + outcomes

The learner receives the same amount of transition data and performs the same search, but the transition relation is independently permuted relative to the repair outcomes.

This preserves:

    data volume
    candidate count
    execution count
    memory
    storage

while destroying the causal alignment between history and repair value.

Prediction:

    recovery collapses toward the outcomes-only condition

### Opaque IDs only

Neither relational history nor repair outcomes are available.

Prediction:

    no systematic repair-class recovery

## Killer null

Retain substantial residual task error:

    E = 0.125

but set observed repair gain to zero.

The repair mechanism may still search candidate abstractions, but estimated repair value is:

    VOI_repair = 0

and therefore no repair may be bound.

Required behavior:

    E > 0
    and
    VOI_repair = 0
    ->
    no mutation

## Mechanical matched-history control

The true-history and shuffled-history branches run the same exhaustive 1820-scope search.

The executable measures per trial:

- candidate scopes;
- pairwise relation checks;
- repair-outcome checks;
- transition-history events;
- memory cells;
- persistent scope-storage slots.

The meter snapshots must match exactly.

## Primary criteria

A positive result requires all of the following.

1. **Descriptor removal**
   - zero named structural descriptor features are exposed;
   - zero named repair axes are exposed.

2. **Cross-encoding invariance**
   - full-substrate repair succeeds under every tested opaque-state permutation.

3. **Relational necessity**
   - outcomes alone do not recover the latent repair class;
   - independently shuffled relational history does not recover it.

4. **Outcome necessity**
   - relational history without repair outcomes does not identify which class should be repaired.

5. **Persistent transfer**
   - the fourth, unprobed member of the latent class receives the repair under the full substrate.

6. **Matched counterfactual information volume**
   - true-history and shuffled-history meters match exactly.

7. **Value-sensitive null**
   - positive residual error with zero repair value produces no mutation.

8. **Governance preservation**
   - goal/reward semantics remain immutable;
   - authority does not expand.

## Interpretation boundary

Passing this audit would support the narrow claim:

    relational history + repair outcomes
    -> derive reusable structural abstraction
    -> persistent held-out repair

without a supplied descriptor basis.

It would show, in this finite arena, that literal descriptor identity is not necessary and that neither outcome labels nor relational structure alone is sufficient.

It would **not** establish unrestricted discovery of arbitrary representational substrates.

Important remaining scaffolds include:

- the learner is given a relation-bearing transition history;
- the candidate repair scope size is fixed at four;
- the hypothesis class is all four-state subsets;
- relational coherence is an available generic inductive bias;
- the latent world is finite and exactly searchable.

The surviving question would therefore become:

    general repair discovery
    vs.
    repair discovery given a designer-chosen relational substrate and hypothesis class

That boundary should remain explicit.

**Scientific rule:** empirical obligation > further abstraction.
