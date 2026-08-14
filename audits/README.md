# Recursive Capability Audit Suite

This directory adversarially audits the `001`–`008` future-sufficiency ladder.

It is **not Experiment 009**.

The central question is:

    capability recursion
    vs.
    scaffold relocation

Experiment 008 established only:

    meta-rule invention within a supplied meta-language

not unrestricted self-modification.

The audit asks whether the repair process survives attacks that change the task surface, structural ontology, and source of residual error.

## Audit target

The strongest ladder claim under audit is:

    persistent residual
    -> identify structural insufficiency
    -> synthesize repair rule
    -> mutate representation generator
    -> reuse repaired generator

A useful recursive-capability interpretation requires the **repair process** to transfer, not merely the specific rule `not(hi)` or the majority task.

## A1 — Hidden scaffolding / ontology permutation

Permute the encoding of the structural state used by the meta-rule.

The learner must not depend on the literal surface expression:

    not(hi)

For every permutation, it re-synthesizes a rule from anonymous structural bits and is scored only by the program space induced by that rule.

Positive criterion:

    task identity changes at the structural-code level
    and
    repair consequence persists

The evaluator does not special-case any expression name.

## A2 — Ladder leakage / different structural family

Replace variable-occurrence insufficiency with a different generator defect:

    syntax-depth insufficiency

The same rule-synthesis procedure is applied to a target selected deterministically from relations that are inexpressible at depth 2 but expressible at depth 3.

Positive criterion:

    repair mechanism transfers
    while
    useful structural rule family changes

This attacks the possibility that the ladder merely taught the benchmark to discover fan-out-like repairs.

## A3 — Genuine transfer over the complete target universe

Freeze the majority-earned repaired generator.

Do not perform further meta-repair.

Evaluate base and repaired generators against all 256 three-input Boolean target relations.

Report:

- how many targets improve;
- how many become newly exact;
- whether any target degrades;
- mean gain conditional on improvement.

This replaces a small handpicked transfer set with a complete finite target universe.

## A4 — Counterfactual necessity

The fixed-generator condition receives the same:

- candidate inspection;
- search budget;
- storage budget;
- semantic primitives.

It is forbidden only from persisting the meta-mutation.

The causal contrast is:

    persistent generator mutation permission

not additional compute or information.

Positive criterion:

    fixed ceiling < repaired transfer

under the matched audit.

## A5 — Killer null: high error without language defect

Construct a task with substantial irreducible residual error but no representation-language insufficiency.

The base generator already contains the correct structural representation; labels are independently corrupted by noise.

Therefore:

    residual error > 0

but:

    VOI(language expansion) = 0

up to held-out estimation error.

The repair process must **not** mutate merely because the task is hard.

The required behavior is:

    repair
    iff
    identified structural insufficiency
    and
    positive repair value

not:

    high error -> mutate machinery

## Reproducibility

Run from the repository root:

```bash
python audits/recursive_capability_audit.py
```

The suite uses only the Python standard library and fixed seeds.

## Interpretation

Passing this suite does not establish unbounded recursive self-improvement.

It would weaken several scaffold-relocation explanations by showing that:

- the literal structural ontology can be permuted;
- the useful repair family can change;
- the frozen repaired generator improves a non-handpicked finite target universe;
- mutation remains counterfactually necessary under matched resources;
- high residual error alone does not trigger repair.

A failure should be treated diagnostically. Do not add another abstraction layer to rescue the ladder without first identifying which audit assumption failed.

The governance boundary remains fixed:

    capability expansion != authority expansion

and:

    meta-capability expansion != goal expansion

**Scientific rule:** empirical obligation > further abstraction.
