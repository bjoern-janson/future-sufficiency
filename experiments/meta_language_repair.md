# Primitive / Meta-Language Repair — Experiment 007

## Purpose

Experiment 006 established a narrow form of operator invention: a learner could synthesize a reusable program from low-level primitives and promote it into its online representation grammar.

This experiment moves one level higher.

The claim is:

> Persistent residual error can justify repairing the construction rules that generate representation programs, when the expected future value of that repair exceeds its cost.

The target chain is:

    residual defect
    -> certify construction-rule insufficiency
    -> repair meta-language
    -> synthesize previously inexpressible program
    -> persist repaired generator
    -> transfer to new task families

No Glimmer integration is included.

## The three failure levels

Experiment 007 keeps three failure modes separate:

    task failure
    !=
    search failure
    !=
    construction-language failure

The base representation language is searched exhaustively.

The base construction rule is also finite and exhaustively characterized.

Therefore a residual ceiling under the base rule is evidence about the expressivity of the current generator, not merely evidence that search stopped early.

## Base meta-language M0

The primitive operators are:

    x
    y
    z
    NOT
    AND
    OR

The base construction rule is **read-once**:

> each input variable may appear at most once in a generated program.

Examples allowed by `M0`:

    x
    NOT(x)
    AND(x,y)
    OR(AND(x,y),z)

Examples forbidden by `M0`:

    OR(AND(x,y), AND(x,z))

because `x` is reused.

`M0` generates exactly 94 semantically distinct Boolean programs over three arguments under these primitives.

The experiment exhaustively enumerates those 94 semantics.

## One-step meta-repair

The available meta-level repair is:

    allow variable fan-out / reuse

After repair:

    M0 = read_once
        ->
    M1 = fanout_allowed

The primitive operator set does not change.

What changes is the rule governing how primitive programs may be constructed.

`M1` is still finite for the experiment because synthesis is bounded to programs of at most nine syntax-tree nodes.

Under that bound, `M1` generates 127 semantically distinct Boolean programs.

## Primary task family

The future-relevant relation is three-input majority:

    z* = 1[x + y + z >= 2]

The evaluator verifies over the complete local truth table:

    max_{e in Expr(M0)} Accuracy(e, z*) = 0.875

while:

    max_{e in Expr(M1)} Accuracy(e, z*) = 1.0

A perfect program under `M1` necessarily reuses at least one input.

For example, the learner may synthesize an equivalent form such as:

    AND(
        OR(AND(x,y), z),
        OR(x,y)
    )

No `MAJORITY` primitive is supplied.

## Cost-sensitive repair

Let:

    a0 = best empirical accuracy under M0
    a1 = best empirical accuracy under M1
    H  = future decision horizon
    c  = one-time construction-rule repair cost

Define:

    VOI_repair = H * max(0, a1 - a0)

Repair occurs iff:

    VOI_repair > c

Use:

    H = 100
    c_low = 5
    c_high = 20

The qualitative predictions are:

    insufficient + low cost  -> repair
    insufficient + high cost -> retain M0

## Already-sufficient control

Use:

    z* = (x AND y) OR z

This relation is exactly expressible under the read-once rule.

Therefore:

    best(M0) = 1
    VOI_repair = 0

and the learner should not repair even when repair is cheap.

This separates:

    "repair after any error signal"

from:

    "repair when the current construction rule is the binding limitation."

## Matched fixed-meta-language control

The fixed control receives the same:

- probe labels;
- raw inputs;
- number of candidate-scoring calls;
- binary representation-state capacity;
- primitive operator set.

It cannot change the read-once construction rule.

After exhausting `M0`, remaining scoring budget is spent rescoring `M0` programs so compute is matched without granting fan-out.

The causal contrast is therefore:

    mutable construction rule
    vs.
    fixed construction rule

rather than more labels, more search, or more memory.

## Held-out transfer

Training and test task surfaces use disjoint raw argument triples.

The repaired learner is evaluated on unseen triples and unseen raw observations.

A positive result requires:

    Transfer(repaired M1) > Transfer(fixed M0)

for the majority task.

## Meta-rule reuse on a new operator family

A stronger diagnostic asks whether the repaired construction rule changes future operator-generation capacity beyond the task that caused repair.

After earning `fanout_allowed` from majority evidence, freeze the repaired meta-language.

Then present a distinct task family:

    z* = x XOR y

with `z` treated as nuisance.

Under `M0`:

    max Accuracy = 0.75

Under the repaired `M1`:

    max Accuracy = 1.0

The learner must synthesize the XOR relation from the same `NOT/AND/OR` primitives.

No second meta-repair is allowed.

This tests:

    repaired construction rule
    ->
    future synthesis ability

rather than merely memorization of the majority program.

## Governance boundary

Experiment 007 deliberately restricts self-modification scope.

The mutable object is only:

    representation construction rule

The following remain evaluator-owned and immutable:

- target / reward semantics;
- probe labels;
- repair cost;
- success criterion;
- action authority.

Therefore:

    representation-language repair
    !=
    goal-language repair

and:

    capability expansion
    !=
    authority expansion

The implementation records:

    goal_rule_mutated = false
    authority_expanded = false

in every condition.

This is an architectural boundary, not an empirical claim about alignment in general.

## Primary criteria

A positive result requires all of the following:

1. **Certified construction-rule insufficiency**
   - `M0` is exhaustively characterized;
   - its exact majority ceiling is 0.875;
   - `M1` reaches 1.0.

2. **Selective meta-repair**
   - low-cost insufficient task repairs `M0 -> M1`;
   - high-cost insufficient task does not;
   - already-sufficient task does not.

3. **Held-out consequence**
   - repaired transfer exceeds the fixed-meta-language control on unseen task surfaces.

4. **Matched budget**
   - probe-label count matches;
   - candidate-scoring calls match.

5. **Persistent generator change**
   - the repaired condition retains `fanout_allowed` after the original task.

6. **Novel-family reuse**
   - the repaired generator subsequently synthesizes XOR perfectly;
   - fixed `M0` remains near its 0.75 ceiling.

7. **Governance preservation**
   - objective semantics do not mutate;
   - action authority does not expand.

## Interpretation boundary

A positive result would establish a narrow form of **representation-generator repair**:

    residual evidence
    -> certify read-once insufficiency
    -> value-sensitive construction-rule change
    -> persistent M0 -> M1
    -> improved future synthesis

It would not establish unrestricted meta-language invention.

The possible repair `allow fan-out` is supplied in advance.

The system decides whether to activate a new construction rule; it does not invent an arbitrary new primitive construction principle outside the supplied meta-level action space.

The next stronger wall would be meta-rule invention rather than meta-rule activation.

**Scientific rule:** empirical obligation > further abstraction.
