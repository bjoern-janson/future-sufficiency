# Extension Scalar Sufficiency / Decision-Substrate Identification Audit — Results

## Provenance

Preregistered before execution at:

```text
d3319438a6c8784d6057ed72033f0dc82631c527
```

Parent checkpoint:

```text
97c0b092932b2931a74af47a7761a6aa93272c23
```

Correct provenance:

\[
\boxed{\textbf{fresh scalar-sufficiency / decision-substrate identification result with frozen upstream preference lineage and hard regression assertions.}}
\]

The exact actual-candidate preference artifacts remain provenance anchors and future application holdout material. Their Git blob identities were verified separately through the GitHub connector; the scalar calibration did not decode or inspect actual candidate application records. The committed executable performs exact hash-only anchor verification when run inside the repository.

No actual candidate scalar, actual `Q_extension`, governance-contract selection, ranking, adoption, authorization, binding, or execution is introduced.

---

## 1. Frozen endpoint

The audit executes only:

\[
\boxed{(R_{\rm pref}^{\rm cal},\mathcal Q_{\rm adm})\rightarrow D_{\rm scalar}}
\]

on independently constructed anonymous typed preference relations.

The tested admissible scalar families remain exactly:

```text
D0  ordered bounded scalar
D1  bounded scalar + one global abstention radius
D2  bounded scalar + restricted two-cut typed decoder
```

`D3` remains the native typed-relation baseline, not a scalar family. `W_LOOKUP` remains a representability control and is never eligible for contraction.

---

## 2. Primary diagnoses

| fixture | D0 | D1 | D2 | W_LOOKUP |
|---|---|---|---|---|
| A strict total order | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `REPRESENTABLE_NO_CONTRACTION` |
| B total preorder + equivalence | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `REPRESENTABLE_NO_CONTRACTION` |
| C one-threshold abstention | `NOT_REPRESENTABLE` | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `REPRESENTABLE_NO_CONTRACTION` |
| D non-monotone abstention bands | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `FAITHFUL_CONTRACTION` | `REPRESENTABLE_NO_CONTRACTION` |
| E directional cycle | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `REPRESENTABLE_NO_CONTRACTION` |
| F nontransitive equivalence | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `REPRESENTABLE_NO_CONTRACTION` |
| G_CAL_A | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `REPRESENTABLE_NO_CONTRACTION` |
| G_CAL_B | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` | `REPRESENTABLE_NO_CONTRACTION` |

Across the 24 D0-D2 fixture cases:

```text
FAITHFUL_CONTRACTION  15
NOT_REPRESENTABLE       9
```

`W_LOOKUP` is exactly 8/8 `REPRESENTABLE_NO_CONTRACTION`.

The fixture-level `NO_SUPPORTED_CONTRACTION` cases are exactly:

```text
E  directional cycle
F  nontransitive equivalence
```

This means only that none of the preregistered D0-D2 families contracts those audited relations.

---

## 3. The ladder localizes the missing structure

### Fixture C — abstention expressivity

D0 fails because ordinary ordered scalar comparison cannot emit a distinct `NO_WARRANTED_PREFERENCE` state.

D1 finds the canonical witness:

```text
q   = [0,1,2,4,5,6]
tau = 1
```

with exact recovery and:

```text
B_D1    = 11
B_Rpref = 15
```

so D1 earns `FAITHFUL_CONTRACTION`.

D2 also represents C, but no family ranking follows.

### Fixture D — decoder expressivity

D0 and D1 are both `NOT_REPRESENTABLE`. D2 finds:

```text
q     = [0,1,2,4,5,6]
tau_1 = 1
tau_2 = 3
B1    = DIRECTION
B2    = NO_WARRANTED_PREFERENCE
B3    = DIRECTION
```

with:

```text
B_D2    = 13
B_Rpref = 15
```

and therefore earns `FAITHFUL_CONTRACTION`.

Thus failure of D1 on D is not evidence that scalarity alone is impossible; the frozen one-threshold decoder is insufficient for the non-monotone typed bands.

### Fixture E — order impossibility

All D0-D2 families are `NOT_REPRESENTABLE`. Their directional outputs follow scalar sign, so the frozen cycle

```text
a > b
b > c
c > a
```

cannot be realized.

### Fixture F — scalar-equality impossibility

All D0-D2 families are `NOT_REPRESENTABLE`. They emit `EQUIVALENT` only at exact scalar equality, which is transitive, while the target requires:

```text
a = b
b = c
a > c
```

The audit does not force a completion.

---

## 4. Representation is not contraction

For six-candidate fixtures the frozen ledger is:

```text
B_Rpref  = 15
B_D0     =  9
B_D1     = 11
B_D2     = 13
B_LOOKUP = 16
```

Therefore exact D0-D2 representations can qualify as contractions under the declared ledger, while unrestricted pair lookup cannot.

\[
\boxed{\text{representation compactness}\neq\text{substrate compression}}
\]

The lookup control represents every finite target but carries the pair table in `B_auxiliary`; its apparent candidate-level compactness is not credited as a contraction.

---

## 5. Exact finite-search certificates

All `NOT_REPRESENTABLE` claims arise from exhaustive bounded search or an exactly equivalent exhaustive constraint procedure.

For six-node fixtures:

```text
D0 normalized q vectors                  144495
D1 q/tau states                         1155960
D2 explicit q/cutpoint/policy states   41614560
D2 exact-equivalent q/cutpoint states   5201820
```

For D2, every q/cutpoint state induces exact required global band policies. A mixed `DIRECTION`/`NWP` requirement in a band proves all eight policy triples fail for that state.

For four-node fixture F:

```text
D0       671
D1      4026
D2    112728 explicit states
```

The lossless machine payload retains successful scalar witnesses, target and decoded pair relations, and nonrepresentability certificates.

---

## 6. Governance-relative typing

Both synthetic governance-reversal relations are ordinary total orders individually and admit separate D0 contractions:

```text
G_CAL_A  q = [5,4,3,2,1,0]
G_CAL_B  q = [0,1,2,3,4,5]
```

The governance-free shared-scalar control exhausts all 144495 normalized score vectors and is `NOT_REPRESENTABLE`.

So the same anonymous candidate set may require different scalar representations under different authoritative governance conditions. Scalarizability does not erase governance provenance, and no governance condition is ranked.

---

## 7. Nuisance invariance and pair symmetry

All primary fixture/family classifications and burden values are invariant under 64 anonymous encodings. Successful scalar witnesses transport exactly under candidate-handle permutations. For nonrepresentable cases, candidate relabeling is a bijection on the bounded scalar family and therefore preserves nonrepresentability.

Pair-swap typing passed:

```text
7104 / 7104
```

No candidate spelling, display alias, serialization order, nonce, or implementation tag supplies scalar authority.

---

## 8. Broken controls

All preregistered shortcut classes are detected or structurally rejected:

```text
W1  NWP -> EQUIVALENT                 typed decision collapse
W2  NWP -> arbitrary direction        scalar authority injection
W3  hidden pair exception table       anti-scaffold burden violation
W4  lookup called contraction         rejected 8/8
W5  actual graph tuning               absent
W6  governance-free shared scalar     NOT_REPRESENTABLE; 144495 exhausted
W7  nuisance encoded in q             rejected by nuisance invariance
W8  decoder burden omitted            rejected by full ledger
W9  total order required for success  falsified by C:D1 and D:D2
W10 scalar preference -> authorization absent
```

The audit counts 1536 encoded `NWP -> EQUIVALENT` collapse mismatches and 1536 encoded `NWP -> direction` authority injections across the frozen abstention controls.

---

## 9. Anti-downstream status

```text
scalar_sufficiency_identification_performed  true
actual_candidate_scalar_application          false
actual_Q_extension_defined                   false
governance_contract_selected                 false
actual_candidate_score_defined               false
candidate_ranking_performed                  false
utility_defined                              false
reward_defined                               false
NO_WARRANTED_ADOPTION_defined                false
adoption_performed                           false
authorization_performed                      false
binding_performed                            false
execution_performed                          false
```

---

## 10. Earned claim

\[
\boxed{\textbf{In the audited finite scalar-sufficiency calibration regimes, the sufficiency and contraction status of preregistered bounded scalar-plus-decoder decision substrates is identifiable relative to the typed preference relation and the frozen semantic-obligation ledger: exact decision distinctions are preserved where representable, unauthorized scalar completion is detected, unrestricted lookup is separated from genuine contraction, and governance-relative scalar typing and nuisance invariance are preserved.}}
\]

The result does not establish universal scalar necessity, universal scalar impossibility, global minimality of the native typed relation, scalarizability of any actual governance contract, any actual candidate scalar value, reward semantics, adoption, or authorization.

The actual preference graph remains untouched for a separately preregistered actual scalar-application gate.