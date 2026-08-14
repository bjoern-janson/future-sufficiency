# Anti-Limit-Relaxation Audit

This audit attacks the strongest surviving alternative explanation after the recursive capability audit:

    recursive capability
    vs.
    limit-relaxation heuristic

It is **not Experiment 009**.

## Core falsification target

A scalar-relaxation heuristic predicts that persistent error should be handled by increasing some existing structural budget:

    k -> k + 1

The audit instead constructs three cases with identical superficial difficulty:

    same 3-bit input space
    same 64 probe examples
    same 64 held-out examples
    same base error = 0.125

but different correct responses:

    case A -> reuse repair
    case B -> operator-family repair
    case C -> no repair

Therefore error magnitude cannot identify the repair.

## Base language

The base representation language uses:

    variables
    NOT
    AND
    OR

with:

    occurrence cap = 1
    maximum syntax-tree nodes = 9

The language is exhaustively enumerated.

## Case A — reuse defect

Target:

    majority3(x, y, z)

Base ceiling:

    0.875

Allowing each variable to occur twice raises the ceiling to:

    1.0

The equality-operator repair does not improve this target.

Required diagnosis:

    reuse

## Case B — operator-family defect

Target:

    all_equal3(x, y, z)

Base ceiling:

    0.875

Scalar relaxations do not help under the audit boundaries:

    occurrence caps 1, 2, 3, 4 -> 0.875
    node budgets 9, 11, 13, 15 with read-once construction -> 0.875

A distinct operator-family expansion that adds a reusable three-input equality primitive reaches:

    1.0

Required diagnosis:

    operator_family

This case is intentionally not solvable by simply relaxing the scalar limit that fixes Case A.

## Case C — high residual error without representation defect

Target structure:

    OR3(x, y, z)

The base language already contains the exact relation.

Each input row is repeated eight times and exactly one label is contradicted, giving irreducible held-out error:

    0.125

Both repair families leave held-out accuracy unchanged at:

    0.875

Required diagnosis:

    keep

This is the hard null:

    high residual error
    and
    no representational-language defect
    ->
    no repair

## Repair decision

Both candidate repairs have the same one-time cost:

    c = 5

with future horizon:

    H = 100

For a candidate repair with held-out gain `g`:

    VOI = H * g

Repair is bound only when:

    VOI > c

The fixed branch performs the same diagnosis but is forbidden from persisting the mutation.

## Mechanical budget audit

The mutable and fixed branches execute the same code paths for:

- probe acquisition;
- candidate-language inspection;
- held-out candidate scoring;
- memory allocation;
- persistent storage reservation.

The implementation measures, rather than asserts:

    probe count
    candidate evaluation count
    execution count
    memory cells
    storage slots

The snapshots must be exactly equal between branches.

## Primary criteria

A positive result requires all of the following:

1. The three cases have exactly the same base error: `0.125`.
2. The diagnosed actions differ: `reuse`, `operator_family`, `keep`.
3. Mutable repair reaches `1.0` on Cases A and B.
4. The fixed branch remains at `0.875` on Cases A and B.
5. Neither branch improves the noisy null above `0.875`.
6. Scalar cap and node-budget relaxations fail to repair Case B.
7. Measured probe, candidate, execution, memory, and storage budgets match exactly.
8. Goal semantics and authority remain immutable.

## Interpretation boundary

Passing this audit would weaken the explanation:

    high error -> relax current scalar limit

because identical error produces three different responses, and one successful repair lies on a different structural axis.

It would **not** establish a general recursive capability.

The repair families are still designed into the audit. In particular, the equality-operator family is supplied as an available repair axis. The result would therefore support:

    structural repair diagnosis across non-equivalent repair axes

not:

    unrestricted discovery of arbitrary repair axes

A stronger future audit would randomize or synthesize the repair-axis vocabulary itself.

**Scientific rule:** empirical obligation > further abstraction.
