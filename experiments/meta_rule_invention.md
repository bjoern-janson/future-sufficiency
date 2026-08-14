# Meta-Rule Invention — Experiment 008

## Purpose

Experiment 007 established representation-generator repair by activating a supplied semantic construction rule: allow variable fan-out.

Experiment 008 removes that supplied repair identity.

The claim is:

> A learner can synthesize a new structural rule for its own representation generator from lower-level meta-primitives, bind that rule when its expected future value exceeds repair cost, and reuse the repaired generator across unrelated target relations.

The target chain is:

    persistent residual
    -> certify M0 insufficiency
    -> synthesize construction rule
    -> bind M0 -> M1
    -> synthesize new semantic programs
    -> reuse M1 across new relation families

No Glimmer integration is included.

## The distinction under test

Experiment 006 synthesized semantic operators.

Experiment 007 changed the representation generator using a supplied rule.

Experiment 008 tests a higher-level object:

    semantic operator
    !=
    construction rule for generating semantic operators

The learner is not given an extension named:

    fan-out
    reuse input
    duplicate variable
    increase occurrence cap

Instead it receives a small structural description language for deciding whether another occurrence of an input is admissible during syntax-tree construction.

## Base generator M0

Semantic programs are still composed from:

    input variables
    NOT
    AND
    OR

with a nine-node syntax-tree budget.

The initial generator is read-once:

    each input variable may occur at most once

This is represented by a structural admissibility program over the current occurrence count of one input.

The occurrence count is encoded using two structural state bits:

    lo = count mod 2
    hi = floor(count / 2) mod 2

The supplied base rule is:

    not(or(lo, hi))

It allows another occurrence only when the current count is zero.

Therefore:

    M0 => occurrence cap = 1

The semantic program space induced by M0 is exhaustively enumerable.

## Meta-language

The repair mechanism is not given a menu of semantic construction rules.

It may synthesize a Boolean program over:

    lo
    hi
    NOT
    AND
    OR
    composition by syntax-tree construction

with at most five meta-program nodes.

There are 14 semantically distinct Boolean programs in this bounded meta-language.

Only rules that permit an initial occurrence are admissible repair candidates.

The learner evaluates those synthesized structural rules by asking what semantic program space each rule induces and how well the best induced representation fits probe-labeled evidence.

No candidate is named by its semantic effect.

## Primary target: majority

The primary relation is:

    majority3(a, b, c)

The evaluator certifies:

    max_{e in M0} Accuracy(e, majority3) = 0.875

A synthesized structural rule:

    not(hi)

permits an occurrence when the current count is zero or one and blocks the third occurrence.

Its induced generator therefore allows each input to occur at most twice.

Under the same semantic primitives and the same nine-node program budget:

    max_{e in M1} Accuracy(e, majority3) = 1.0

The learner is not given the phrase "allow two occurrences" or the identity of `not(hi)`.

It discovers the structural rule by exhaustive meta-program evaluation.

## Repair decision

Let:

    a0 = best empirical accuracy under M0
    a1 = best empirical accuracy under the best synthesized meta-rule
    H  = future decision horizon
    c  = one-time meta-repair cost

Define:

    VOI_meta = H * max(0, a1 - a0)

Bind the synthesized construction rule iff:

    VOI_meta > c

Use:

    H = 100
    c_low = 5
    c_high = 20

For balanced majority evidence:

    a0 = 0.875
    a1 = 1.0
    VOI_meta = 12.5

Predictions:

    majority + low cost  -> repair M0
    majority + high cost -> preserve M0

## Already-sufficient control

Use:

    OR2(a, b)

Since read-once M0 already represents this relation exactly:

    a0 = 1.0

there is no empirical value to changing the generator.

Prediction:

    sufficient + low cost -> preserve M0

This distinguishes selective repair from gratuitous generator expansion.

## Fixed-meta-language control

The fixed control receives the same:

- probe labels;
- semantic primitives;
- synthesized meta-program candidates;
- candidate-rule evaluation;
- semantic search computations;
- representation-state capacity.

It is allowed to discover that a different structural rule would improve the primary task.

It cannot bind that rule into the persistent representation generator.

The causal contrast is therefore:

    ability to modify the construction rule

not:

    more labels
    more search
    more semantic operators
    more memory

## Generator-memory transfer

The strongest test is not majority performance.

After low-cost majority repair, freeze the synthesized construction rule.

Do not perform another meta-repair.

Then present two new relation families.

### Transfer 1: binary XOR

The evaluator certifies:

    max_{e in M0} Accuracy(e, XOR2) = 0.75

while the repaired generator can synthesize:

    Accuracy_M1(XOR2) = 1.0

### Transfer 2: multiplexer

Use:

    MUX3(selector, left, right)
        =
    left if selector else right

The evaluator certifies:

    max_{e in M0} Accuracy(e, MUX3) = 0.875

while:

    Accuracy_M1(MUX3) = 1.0

No new meta-rule search is performed for XOR or MUX.

Only ordinary semantic program synthesis is run under the already-repaired generator.

Thus the persistent object is:

    a construction rule

rather than:

    the majority solution

or:

    a remembered semantic operator

## Primary criteria

A positive result requires all of the following.

1. **Certified M0 insufficiency**
   - the read-once semantic language is exhaustively evaluated;
   - exact majority ceiling is 0.875.

2. **Rule synthesis rather than rule selection**
   - no semantic `fan-out` or `reuse` extension is supplied;
   - the selected rule is constructed from `lo`, `hi`, `NOT`, `AND`, and `OR`.

3. **Selective meta-repair**
   - low-cost majority binds a non-M0 rule;
   - high-cost majority preserves M0;
   - already-sufficient OR preserves M0.

4. **Persistent generator change**
   - the synthesized rule remains active after the majority task.

5. **Cross-relation reuse**
   - the repaired generator synthesizes perfect XOR without another meta-repair;
   - it also synthesizes perfect MUX without another meta-repair.

6. **Fixed-generator contrast**
   - fixed M0 remains at its exact ceilings on the transfer relations.

7. **Governance boundary**
   - goal/reward semantics are immutable;
   - authority does not expand.

## Interpretation boundary

A positive result establishes a narrow form of **meta-rule invention**:

    residual evidence
    -> synthesize structural admissibility program
    -> change representation-generation rule
    -> persist repaired generator
    -> enable new semantic constructions on unrelated relations

It does not establish unrestricted self-modification.

The meta-rule description language itself is still supplied in advance:

    {lo, hi, NOT, AND, OR, composition}

The next stronger wall would be whether persistent failure can cause the system to invent or alter the meta-rule description language itself rather than search inside a fixed one.

The experiment also keeps a hard architectural boundary:

    meta-capability expansion
    !=
    goal expansion

and:

    capability expansion
    !=
    authority expansion

**Scientific rule:** empirical obligation > further abstraction.
