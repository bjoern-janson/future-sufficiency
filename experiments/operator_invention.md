# Operator Invention — Experiment 006

## Purpose

Experiment 005 established representation-language repair by choosing among a supplied menu of language extensions.

This experiment removes that semantic extension menu.

The claim is:

> A learner can synthesize a new reusable representation operator from low-level primitives, promote it into its online representation grammar when the expected future value exceeds invention cost, and reuse it on held-out tasks.

The target chain is:

    residual defect
    -> exhaustive failure in G0
    -> primitive program synthesis
    -> operator promotion
    -> persistent reuse
    -> transfer

No Glimmer integration is included.

## What "operator invention" means here

The primitive computational substrate is still fixed. Ex nihilo computation is not a meaningful empirical target.

The primitive description language contains only:

    x
    y
    NOT
    AND
    OR
    composition by syntax-tree construction

There is no supplied `XOR`, `XOR3`, `majority`, `NAND`, or named extension menu.

The initial online representation grammar `G0` is restricted to primitive programs of at most three syntax-tree nodes:

    x
    y
    NOT(x)
    NOT(y)
    AND(x,y)
    OR(x,y)

A self-extending learner may pay an invention cost to synthesize a deeper primitive program, bind it to a new reusable macro slot, and thereafter treat that macro as an operator in its representation language.

Thus the experiment tests:

    invention relative to G0

not:

    invention outside the fixed primitive meta-language.

## Task family

Each task selects two argument positions from a 16-bit raw observation.

The training family uses a future-relevant binary relation:

    z* = a XOR b

but the learner is never given the name `XOR`, its truth table, or a candidate XOR operator.

The evaluator only supplies probe labels.

The base grammar is exhaustively enumerable and has exact ceiling:

    max_{e in G0} Accuracy(e, XOR) = 0.75

The primitive synthesizer searches all semantically distinct binary programs expressible with at most eight primitive syntax-tree nodes.

That search contains a perfect program:

    AND(NOT(AND(x,y)), OR(x,y))

whose truth table is evaluator-equivalent to XOR.

The learner discovers the program from labels; the semantic name is never supplied.

## 006a — Invent one missing operator

The learner receives probe-labeled examples from many small pair tasks.

It:

1. exhaustively scores `G0`;
2. observes persistent residual error;
3. synthesizes deeper primitive programs;
4. identifies the best program body;
5. may bind that body to the reserved macro slot.

A positive result requires:

    best(G0) < 1
    and
    best(synthesized primitive programs) = 1

with the selected body absent from `G0`.

## 006b — Invention under cost

Let:

    a0 = best empirical accuracy in G0
    a1 = best empirical accuracy after primitive synthesis
    H  = future decision horizon
    c  = one-time invention cost

Define:

    VOI_invent = H * max(0, a1 - a0)

The self-extending learner binds the synthesized operator iff:

    VOI_invent > c

Use:

    H = 100
    c_low = 10
    c_high = 35

Predictions:

    parity + c_low  -> invent
    parity + c_high -> do not invent

A base-sufficient control uses:

    z* = a OR b

Since `OR(x,y)` already belongs to `G0`:

    VOI_invent = 0

and the learner should not invent even at low cost.

## 006c — Persistent reuse and transfer

After invention, freeze the learned macro and evaluate it without further operator search on:

- raw bit configurations disjoint from the probe-labeled configurations;
- argument-position pairs disjoint from the training task pairs.

The invented operator should transfer across those new task surfaces.

As an evaluator-only reusability diagnostic, apply the learned binary macro recursively:

    m(m(a,b),c)

to ternary parity.

If the learned macro has captured the reusable relation, recursive reuse should solve:

    a XOR b XOR c

while the fixed `G0` ternary ceiling is:

    0.5

This diagnostic demonstrates that promoting the synthesized body changes what the representation language can compactly express. It does not claim that the learner autonomously chose the ternary composition task.

## 006d — No single task identifies what to invent

Training is distributed across 60 distinct pair tasks.

Each task provides only two of the four possible local binary input patterns.

Therefore no individual task uniquely identifies a binary operator.

With 16 possible binary truth functions, two observed rows leave at least four functions perfectly consistent with any single task.

The operator is identified only by pooling residual structure across the task family.

The held-out set uses 30 disjoint argument-position pairs.

Thus:

    train task pairs ∩ test task pairs = empty

and:

    train raw configurations ∩ test raw configurations = empty

This prevents a single memorized target instance from defining the invented operator.

## Fixed-language control

The fixed-language condition receives exactly the same:

- probe labels;
- raw inputs;
- primitive candidate-synthesis computation;
- candidate-scoring budget;
- binary representation-state capacity;
- reserved eight-node macro storage slot.

It is allowed to analyze every synthesized program body, but it cannot bind a new operator into `G0`.

This intentionally isolates the causal difference:

    ability to mutate the representation grammar

rather than:

    more search
    more labels
    more memory
    or more storage.

## Primary criteria

A positive result requires all of the following:

1. **Certified base-language insufficiency**
   - `G0` is exhaustively evaluated;
   - its exact pair-parity ceiling is 0.75.

2. **Operator construction without a semantic menu**
   - the selected body is composed only from `NOT`, `AND`, `OR`, and argument atoms;
   - no named parity operator is supplied.

3. **Value-sensitive invention**
   - low-cost parity causes macro promotion;
   - high-cost parity does not;
   - the base-sufficient OR task does not.

4. **Held-out pair transfer**
   - the invented operator transfers perfectly or near-perfectly to disjoint argument-position pairs and raw configurations.

5. **Matched-budget advantage**
   - the self-extending condition beats the fixed-language control with the same probe and candidate-evaluation budgets.

6. **Reusable language change**
   - recursive application of the learned macro solves ternary parity;
   - fixed `G0` cannot exceed 0.5 on ternary parity.

7. **Cross-task invention**
   - no single training task uniquely identifies the operator;
   - pooled evidence across tasks is required.

## Interpretation boundary

A positive result establishes a narrow form of representation-operator invention:

    distributed residual evidence
    -> synthesize primitive program
    -> create reusable macro operator
    -> selectively modify G0
    -> transfer to unseen task surfaces

It does not establish unrestricted representation-language invention.

The primitive meta-language and the macro-creation mechanism are still supplied in advance. The system invents a new operator *inside that computational substrate*.

The next stronger wall would be whether the system can revise the primitive/meta-language itself when the required operator cannot be expressed by the supplied program-construction substrate.

**Scientific rule:** empirical obligation > further abstraction.
