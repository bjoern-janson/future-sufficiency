# Representation-Language Repair — Experiment 005

## Purpose

Experiment 004 showed that a learner can synthesize and persist a compositional distinction inside a fixed expression grammar.

This experiment tests the next stronger claim:

> A learner can detect when exhaustive search inside its current representation language leaves persistent residual error, estimate the value of a bounded language expansion, and expand only when the expected future gain exceeds the expansion cost.

The target chain is:

    residual error
    -> certify base-language limit
    -> evaluate extension menu
    -> expand language
    -> construct representation
    -> transfer

## Base language

The initial grammar is finite and searched exhaustively:

    G0 = {
        atom(b_i),
        xor2(b_i, b_j),
        and2(b_i, b_j),
        or2(b_i, b_j)
    }

Because every expression in `G0` is enumerated, residual error after search cannot be attributed to an incomplete optimizer over `G0`.

## Tasks

Two evaluator-defined task families are used.

### Base-sufficient

    z* = b_3 XOR b_9

This target is expressible in `G0`.

### Base-insufficient

    z* = b_3 XOR b_9 XOR b_12

Under the fixed depth/arity budget of `G0`, this target is not expressible.

The evaluator verifies this over the complete raw truth table:

    max_{e in Expr(G0)} Accuracy(e, z*) = 0.5

for the base-insufficient task.

## Extension menu

The learner is not told which extension is useful. It evaluates four available one-step language extensions:

    E = {
        add_xor3,
        add_majority3,
        add_not,
        add_nand2
    }

Only one extension contains an exact representation for the base-insufficient target:

    add_xor3

The learner sees probe-labeled raw examples and scores every candidate expression made available by each extension.

## Expansion decision

Let:

    a0 = best empirical accuracy under G0
    a1 = best empirical accuracy under the best one-step extension
    H  = fixed future decision horizon
    c  = grammar-expansion cost

The meta-level value estimate is:

    VOI_expand = H * max(0, a1 - a0)

The learner expands iff:

    VOI_expand > c

This makes expansion a value-sensitive action rather than an unconditional fallback after failure.

## Cost control

Use two expansion costs:

    c_low  = 10
    c_high = 60

with:

    H = 100

For the base-insufficient task, the exact gross improvement from 0.5 to 1.0 corresponds to 50 expected correct decisions over the horizon.

Therefore the qualitative prediction is:

    c_low < VOI_expand  -> expand
    c_high > VOI_expand -> do not expand

For the base-sufficient task:

    VOI_expand = 0

so the learner should not expand at either cost.

## Fixed-grammar control

The fixed-grammar control receives:

- the same probe-labeled examples;
- the same raw inputs;
- the same binary representation-state capacity;
- the same candidate-scoring call budget.

It cannot activate any extension.

After exhaustive `G0` search, any remaining candidate-scoring budget is spent rescoring base-language expressions. This matches the number of scoring operations without granting new representational operators.

## Primary criteria

A positive result requires:

1. **Search/language separation**
   - `G0` is exhaustively enumerated;
   - the evaluator confirms the base-insufficient target is not representable within `G0`.

2. **Selective grammar repair**
   - on the base-insufficient task at low cost, the learner selects `add_xor3`;
   - on the same task at high cost, it does not expand;
   - on the base-sufficient task, it does not expand.

3. **Persistent construction**
   - after expansion, the learner persists a ternary XOR representation.

4. **Held-out transfer**
   - the repaired representation transfers to raw configurations disjoint from probe-labeled configurations.

5. **Fixed-grammar advantage**
   - repaired transfer exceeds the matched-budget fixed-grammar control on the base-insufficient task.

6. **Budget matching**
   - probe-label count is equal;
   - candidate-scoring call count is equal;
   - both final policies use a binary representation state.

## Interpretation boundary

A positive result would establish a narrow form of **representation-language repair**:

    exhaustive failure inside G0
    -> evidence that G0 is too weak
    -> value-sensitive extension choice
    -> G0 -> G1
    -> new representation
    -> held-out transfer

It would not establish unrestricted language invention.

The extension menu is supplied in advance. The learner chooses among possible language changes; it does not invent a new operator outside the meta-language.

The next stronger wall would be whether the system can create a new representation operator when no supplied extension can express the required distinction.

No Glimmer integration is included here.

**Scientific rule:** empirical obligation > further abstraction.
