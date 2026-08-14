# Decision-Substrate Language Identification — Round v1 Characterization Audit

## Status

Round `DSLI_R1` characterization was executed only after the specification-completeness gate emitted:

```text
CHARACTERIZATION_AUTHORIZED
```

Frozen parents:

```text
construction   6482667d3b48c2e0c47bfea2fb44da92187b0511
SpecComplete   0f2e2e9cf38258b583dc3d7f9bbbf2cd047fcf53
```

The characterization execution ran under the frozen runtime:

```text
CPython 3.12.11
standard library only
exact integer/discrete semantics
no floating point
```

Execution was performed on the ephemeral branch:

```text
agent/dsli-r1-characterization-runner
head 3cfe5d3de857822195448793a6c04578af3232ce
workflow run 31827317141
job 94854380803
```

The workflow artifact digest is:

```text
sha256:ae55af90e140241520cfe1690e581a5855aa56688e9868fd08ce14f30f16a52f
```

The complete raw characterization result produced by the frozen runtime has SHA-256:

```text
5b0b567a8913ef83770164d85490e5448c5b23bd7af7ff768367a0f7823686cc
```

The committed compact payload is lossless for all 156 treatment cells relative to the frozen calibration-world artifact: relation identity recovers structural descriptor `K`, `n` determines `B_R`, and `[status_code,B_star]` reconstructs `Rep`, `Rep^A`, minimum burden, and `Sigma_outcome`.

---

## 1. Primary treatment result

The frozen world contains 26 anonymous calibration relations and six treatment languages:

```text
26 x 6 = 156 treatment cells
```

Across those 156 cells:

```text
NOT_REPRESENTABLE                        102
REPRESENTABLE_AUTHORITY_INVALID           0
ADMISSIBLE_REPRESENTATION_NO_CONTRACTION  8
FAITHFUL_CONTRACTION                      46
```

Per-language outcomes:

| Language | Representable | Faithful contraction | Admissible / no contraction | Not representable |
|---|---:|---:|---:|---:|
| `L_ORD1` | 2/26 | 2 | 0 | 24 |
| `L_RADIUS1` | 10/26 | 10 | 0 | 16 |
| `L_BANDS1` | 11/26 | 11 | 0 | 15 |
| `L_INTERSECT2` | 13/26 | 5 | 8 | 13 |
| `L_POSET` | 14/26 | 14 | 0 | 12 |
| `L_SPARSE_LINEAR` | 4/26 | 4 | 0 | 22 |

These counts characterize this finite frozen calibration support. They do not rank the languages and do not establish universal structural-class closure.

`L_INTERSECT2` is the treatment in which the representability/contraction separation is most visible: 13 relations are admissibly representable, but 8 of those fail the frozen burden inequality and therefore remain `ADMISSIBLE_REPRESENTATION_NO_CONTRACTION`.

---

## 2. Four-state ontology controls

The treatment languages contain only declared, licensed witness state, so no treatment cell can become authority-invalid after exact legal representation is established.

The frozen controls populate the remaining diagnostic states exactly as intended:

```text
W_DIRECT_LOOKUP
  26/26 admissibly representable
  B_star = B_R + 1
  -> ADMISSIBLE_REPRESENTATION_NO_CONTRACTION

W_IDENTITY_ORACLE
  26/26 extensionally representable
  Rep^A = false
  authority violation = UNLICENSED_CANDIDATE_IDENTITY
  -> REPRESENTABLE_AUTHORITY_INVALID
```

Thus all four ontology states are empirically instantiated across treatments plus controls without collapsing authority failure into burden failure.

---

## 3. Matched structural discriminants

### Direction topology

For both `n=6` and `n=7`, changing the matched all-resolved relation from a total order to a cyclic tournament changes the terminal state for:

```text
L_ORD1
L_RADIUS1
L_BANDS1
L_INTERSECT2
L_POSET
```

from exact representation (`FC` or `ARNC`) to `NOT_REPRESENTABLE`.

`L_SPARSE_LINEAR` is `NOT_REPRESENTABLE` on both members because the complete tournament relation exceeds its frozen `|E| <= n-1` direct-edge budget.

This supports a directional-cyclicity boundary for the five order/partial-order-derived languages on the frozen matched cases. It does not imply that cyclicity is intrinsically unrepresentable outside the frozen language family.

### Equivalence lawfulness

For both `n=6` and `n=7`, the lawful two-block equivalence relation is representable by:

```text
L_RADIUS1
L_BANDS1
L_INTERSECT2
L_POSET
L_SPARSE_LINEAR
```

while the token-count-matched nontransitive-equivalence relation is `NOT_REPRESENTABLE` for all five.

`L_ORD1` is `NOT_REPRESENTABLE` on both because the matched relations contain NWP independently of the equivalence manipulation.

This localizes the observed failure to the frozen languages' lawful-equivalence requirement rather than to the number of `EQUIVALENT` tokens alone.

### Transitivity

For both candidate counts, the matched transitive partial-order case is representable by `L_INTERSECT2` and `L_POSET`, while the acyclic nontransitive relation is not.

`L_SPARSE_LINEAR` separates this mechanism from explicit relational storage: at `n=7`, both six-edge relations are faithfully represented because the frozen direct-edge budget is `n-1=6` and no transitive completion is imposed. At `n=6`, both exceed the `n-1=5` budget and are not represented.

The result therefore distinguishes a transitivity requirement from a bounded direct-relation requirement within the frozen family.

### Abstention topology

For both `n=6` and `n=7`, the monotone-local abstention relation is faithfully represented by `L_RADIUS1`, `L_INTERSECT2`, and `L_POSET`, while the matched cross-cut relation is not.

`L_BANDS1` is more specific: it changes `FC -> NR` at `n=6`, but remains `FC -> FC` at `n=7`. The result establishes representability of this particular `n=7` cross-cut case, not closure over a general cross-cut class.

### Cardinality stress

At `n=6`, changing only the resolved/NWP token counts within the frozen one-dimensional monotone structural class changes no terminal state in any language.

At `n=7`, the only terminal-state change is in `L_INTERSECT2`:

```text
sparser relation -> NOT_REPRESENTABLE
denser relation  -> FAITHFUL_CONTRACTION
```

This is direct finite evidence that greater relation cardinality does not monotonically imply greater substrate difficulty. In this frozen contrast, relation geometry and factorability dominate raw resolved-edge count.

### Connectivity

The connected and disconnected cyclic sparse relations have identical terminal states for every treatment language at both candidate counts: all are `NOT_REPRESENTABLE`.

Therefore this round does not identify connectivity as an outcome-changing boundary on these matched cases. This is a null discriminant, not evidence that connectivity is universally irrelevant.

### Product geometry

The product-order relation and its token-count-matched single-axis comparison have identical terminal states across all six languages:

```text
L_INTERSECT2   ARNC / ARNC
L_POSET        FC   / FC
all others     NR   / NR
```

This preregistered block is multi-axis rather than a one-factor discriminant, so no single manipulated structural coordinate receives causal attribution from the null terminal-state difference.

---

## 4. Burden is an independent boundary

The round directly confirms that:

```text
representable != contracting
```

because `L_INTERSECT2` produces eight admissible exact representations whose certified minimum burden is not below native relation burden.

The candidate-count scaling is visible in analogous total-order cases:

```text
n=6:  B_INTERSECT2 = 17, B_R = 15 -> ARNC
n=7:  B_INTERSECT2 = 19, B_R = 21 -> FC
```

This is a burden-threshold effect under the frozen formulas; it is not a claim that increasing candidate count generally improves representability or contraction.

---

## 5. Nuisance and pair-swap invariance

The characterization retained the already-certified anonymous witness-space equivariance and mechanically checked every frozen nuisance candidate permutation for exact bijective relation transport:

```text
26 cases x 64 nuisance encodings = 1664 relation-transport checks
mismatches = 0
```

All canonical pair orientations were also swapped and renormalized:

```text
pair-swap checks = 462
mismatches       = 0
```

Aliases, nonces, implementation tags, and record order never enter treatment semantics.

---

## 6. Downstream authority boundary

Characterization changed none of the frozen round objects.

```text
language_family_modified        false
calibration_world_modified      false
adaptive_sampling_performed     false
new_calibration_case_added      false
actual_target_read              false
application_set_selected        false
governance_selected             false
candidate_ranking_performed     false
actual_Q_extension_defined      false
authorization_performed         false
binding_performed               false
execution_performed             false
```

No language is selected merely because it represents more calibration cases or contracts more often. Calibration characterizes the fixed treatment family; it does not choose a normative or application-stage winner.

---

## 7. Strongest permitted claim

The strongest claim supported by this execution is:

> On the frozen 26-relation anonymous calibration world, the six preregistered decision-substrate languages exhibit distinct, exactly certified unrestricted/admissible closure and contraction boundaries. Matched contrasts expose local sensitivity to directional cyclicity, lawful equivalence, transitivity, and abstention topology; raw relation cardinality is not a monotone proxy for representational difficulty; and exact representability remains distinct from semantic contraction. These are finite round-v1 characterization results relative to the frozen language family and admissibility regime, not universal representation theorems.

---

## 8. Stop condition

Stop after committing this characterization.

Do not in this commit:

```text
modify any language
modify the calibration world
add a calibration relation
select an application language
freeze an application set
apply languages to the actual 12-candidate relations
use actual mismatch neighborhoods for redesign
select governance
rank candidates
define Q_extension
adopt
authorize
bind
execute
```

The next stage, if pursued, is an explicit post-characterization decision about the application-set freeze or a separately versioned development round. Characterization evidence may motivate `v=2`, but cannot validate modifications it motivates.
