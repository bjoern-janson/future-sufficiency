# Extension Comparison License / Native Relation — Preregistration

## Status

This document freezes the next empirical gate **before any comparison is performed over the preregistered extension candidates and before any extension-value or preference function is defined**.

Parent checkpoint:

```text
c0db168261ebfb32106382c34c992bf00ec1aa4c
```

Candidate-measurement preregistration:

```text
6850a2f421d4477c45f679dcf03909f914788bbc
```

Candidate-measurement execution:

```text
c0db168261ebfb32106382c34c992bf00ec1aa4c
```

Measurement-identification execution:

```text
607502a9434884ca9bb06d5ddd6ff6c17f2ef002
```

The only object frozen here is the comparison-license / native-relation architecture:

\[
\boxed{
\mathcal R_{\rm compare}
=
\{C_{\Delta V},C_B,C_{\Delta C},C_{\rm collateral},C_{\rm reopen},C_{\rm scope}\}.
}
\]

Each comparison contract is typed as:

\[
\boxed{
C_k=
(D_k,\Lambda_k,R_k,\mathcal T_k^{\rm cmp},F_k^{\rm cmp},L_k^{\rm cmp}).
}
\]

The only permitted evaluation chain is:

\[
\boxed{
D_k
\rightarrow
\Lambda_k
\rightarrow
R_k.
}
\]

No candidate preference relation exists in this artifact.

No `Q_extension` exists in this artifact.

No candidate is preferred, ranked, Pareto-filtered, selected, adopted, authorized, or bound.

---

# 1. Scientific boundary

The preceding branch established, in finite audited regimes:

\[
\boxed{
\mathcal M_{\rm ext}\text{ identification}\checkmark
\rightarrow
s\rightarrow\mathcal V_{\rm ext}(s)\checkmark.
}
\]

The present question is narrower:

> Given typed measurement records, can the system determine whether a native coordinate relation is licensed and, only when licensed, evaluate that relation without collapsing it into a cross-coordinate preference?

The governing distinction is:

\[
\boxed{
\text{measurement}
\neq
\text{comparison license}
\neq
\text{native relation}
\neq
\text{candidate preference}.
}
\]

The strongest claim permitted after a successful execution is:

\[
\boxed{
\textbf{
The native pairwise relations supported by the identified extension measurements are themselves empirically identifiable in the audited finite calibration regimes, with comparison license, native partial-order structure, incomparability, and missing-identification boundaries preserved.
}
}
\]

Nothing in this gate licenses a global candidate ordering.

---

# 2. Upstream candidate records are anchors, not calibration targets

The 12 measured candidate records at `c0db168` are **not** used to choose, tune, simplify, or validate the definitions of `Lambda_k`, `R_k`, or the admissible comparison transformations in this preregistration.

The comparison-identification execution must use the calibration records frozen below.

It must **not** emit pairwise relations between any of the 12 actual measured candidates.

In particular, this gate must not answer any of the following:

```text
SYN_A_120 vs SYN_B_50
SYN_C1_1653 vs SYN_C2_2388
SYN_* vs EXT_CT_*
any synthesized/control/external pairwise ordering
```

The existing Hudson/Rubi `NOT_IDENTIFIED` cells remain an upstream regression fact demonstrating why license discipline matters, but they are not evidence for tuning the comparator.

After this architecture is independently identified, a later artifact may preregister application of the frozen comparators to actual candidate records.

---

# 3. Canonical comparator contract

For coordinate `k`, define:

\[
C_k=(D_k,\Lambda_k,R_k,\mathcal T_k^{\rm cmp},F_k^{\rm cmp},L_k^{\rm cmp}).
\]

## 3.1 `D_k` — admissible native record pair

`D_k` contains exactly the two typed coordinate records being considered, including:

```text
candidate handle i
candidate handle j
coordinate identity k
Z_k(i), Z_k(j)
native values or nulls
coordinate-specific lineage
support-regime records
comparison-frame identifiers
measurement-panel / semantic-frame identifiers where applicable
```

No cross-coordinate field may enter `D_k`.

Candidate provenance class may be retained for lineage but may not alter the relation.

## 3.2 `Lambda_k` — license predicate

\[
\boxed{
\Lambda_k(i,j)\in\{\texttt{LICENSED},\texttt{NOT\_LICENSED}\}.
}
\]

A relation is licensed only if all required conditions for coordinate `k` hold.

At minimum:

1. both coordinate statuses are `IDENTIFIED`;
2. both native values have the frozen native type;
3. the comparison frames are compatible under `T_k^cmp`;
4. the two records have nonempty common `PASS` support on the regime(s) required by the relation;
5. neither record relies on a `FAIL` or `NOT_TESTED` regime for the proposed comparison;
6. all coordinate-specific lineage needed to interpret the relation is present;
7. no missing value is imputed;
8. no unlicensed bridge between incompatible panels, baselines, stress families, semantic universes, or burden schemas is introduced.

If any required condition fails:

```text
license  = NOT_LICENSED
relation = NO_LICENSED_COMPARISON
```

and evaluation stops.

## 3.3 `R_k` — native relation

`R_k` is evaluated **only if** `Lambda_k = LICENSED`.

The frozen relation vocabulary is:

\[
\boxed{
\{\
\texttt{I\_GREATER},
\texttt{J\_GREATER},
\texttt{EQUIVALENT},
\texttt{INCOMPARABLE},
\texttt{NO\_LICENSED\_COMPARISON}
\}.
}
\]

`NO_LICENSED_COMPARISON` is emitted iff the relation is not licensed.

The other four outputs require a licensed comparison.

`INCOMPARABLE` therefore means:

\[
\boxed{
\Lambda_k=\texttt{LICENSED}
\quad\land\quad
\text{the native partial relation yields no direction or equivalence}.
}
\]

It must never be used as a substitute for missing identification or unsupported scope.

---

# 4. Orientation is coordinate-specific, never generic “better”

The tokens `I_GREATER` and `J_GREATER` are syntactic outputs whose semantic orientation is frozen separately for each coordinate.

| coordinate | meaning of `I_GREATER` |
|---|---|
| `DeltaV_corr` | candidate `i` has the numerically larger identified extension-attributable corrective consequence on the frozen common contrast frame |
| `B_extension` | every admissible minimal burden ledger for `i` is componentwise greater than or equal to every admissible minimal burden ledger for `j`, with at least one strict burden component |
| `DeltaC` | the ordered semantic geometry delta of `i` componentwise set-contains that of `j`, with at least one strict containment |
| `R_collateral` | `i` has componentwise greater-or-equal signed collateral consequence on the same frozen labeled contract vector, with at least one strict component |
| `R_reopen` | the stresswise reachable-correction indicator vector of `i` componentwise contains that of `j` on the same frozen stress family, with at least one strict stress |
| `Scope` | the `PASS` support set of `i` strictly contains the `PASS` support set of `j`; this is descriptive only and has no preference authority |

Thus:

\[
\boxed{
R_k(i,j)=\texttt{I\_GREATER}
\not\Rightarrow
i\succ j.
}
\]

Likewise:

\[
\boxed{
R_k(i,j)=\texttt{EQUIVALENT}
\not\Rightarrow
\mathcal V_{\rm ext}(i)=\mathcal V_{\rm ext}(j).
}
\]

Coordinate relation is not candidate preference.

---

# 5. `C_DeltaV` — corrective-consequence comparison

## 5.1 `D_DeltaV`

Native values are the already-defined scalar held-out corrective-consequence effects, together with their causal contrast frame, outcome scale, panel identifier, estimator lineage, and support regimes.

## 5.2 `Lambda_DeltaV`

Comparison is licensed only if:

- both statuses are `IDENTIFIED`;
- both effects refer to the same consequence object or to contrast frames connected by a preregistered admissible transformation;
- both use the same frozen held-out contract panel or an explicitly licensed label-preserving permutation of that panel;
- both effects are on difference-preserving outcome scales;
- required common support is nonempty and `PASS` for both.

Different unbridged causal contrast frames produce `NO_LICENSED_COMPARISON` even if both records contain numbers.

## 5.3 `R_DeltaV`

For licensed scalar effects `v_i,v_j`:

```text
v_i > v_j  -> I_GREATER
v_i < v_j  -> J_GREATER
v_i = v_j  -> EQUIVALENT
```

`INCOMPARABLE` is not a reachable output for this exact scalar finite-calibration relation.

No tolerance is used in the finite exact calibration panel.

## 5.4 `T_DeltaV^cmp`

Admissible transformations are:

- common positive scaling of effect values induced by a positive-affine transformation of the underlying consequence scale;
- common contract-label permutation preserving contract identity and pairing;
- anonymous candidate-handle renaming;
- enumeration-order permutation.

All must preserve the relation.

## 5.5 `F_DeltaV^cmp`

The comparator is invalid if it:

- compares a `NOT_IDENTIFIED` value after replacing it by zero or another number;
- compares across an unbridged causal/common-scope frame;
- changes direction under an admissible positive scaling;
- uses candidate provenance to break equality.

---

# 6. `C_B` — structured burden comparison

## 6.1 `D_B`

The native burden object is the **complete nonempty set of inclusion-minimal semantic obligation ledgers** retained by `M_B`.

Each ledger is a vector over the frozen categories:

```text
explicit
inherited
hidden
target_specific
search
external
```

Visible syntax length is metadata only.

## 6.2 `Lambda_B`

Comparison is licensed only if:

- both statuses are `IDENTIFIED`;
- both use the same semantic-obligation unit and category schema;
- hidden/inherited/target-specific obligations have been expanded under the identified burden instrument;
- complete minimal-ledger envelopes are present;
- required common support is `PASS`.

## 6.3 `R_B`

Let `L_i` and `L_j` be the complete sets of inclusion-minimal burden ledgers.

Define robust componentwise greater burden:

\[
L_i\succeq_B L_j
\iff
\forall a\in L_i\;\forall b\in L_j:\;a_c\ge b_c\;\forall c.
\]

Then:

```text
L_i == L_j                                          -> EQUIVALENT
L_i >=_B L_j and at least one strict component     -> I_GREATER
L_j >=_B L_i and at least one strict component     -> J_GREATER
otherwise                                           -> INCOMPARABLE
```

Equality is equality of the complete semantic minimal-ledger sets after licensed obligation-handle renaming, not equality of visible token counts or only expanded totals.

This relation intentionally withholds direction when alternative minimal implementations cross.

## 6.4 `T_B^cmp`

Admissible transformations are:

- obligation-handle renaming;
- ledger ordering permutation;
- candidate-handle renaming;
- transparent aliasing that expands to the same semantic obligations;
- serialization-order permutation.

## 6.5 `F_B^cmp`

The comparator is invalid if visible-token or macro length changes the relation while the expanded semantic obligation sets are unchanged.

---

# 7. `C_DeltaC` — semantic geometry comparison

## 7.1 `D_DeltaC`

The native geometry object remains:

\[
\Delta\mathcal C(s)=(\mathcal C_+(s),\mathcal C_-(s)).
\]

Both sets must be present as semantic partition objects or lossless checksum-anchored references to those objects.

Cardinality is descriptive only.

## 7.2 `Lambda_DeltaC`

Comparison is licensed only if:

- both statuses are `IDENTIFIED`;
- both deltas are expressed in the same semantic universe and equivalence relation;
- the baseline frame is the same, or a preregistered bijective baseline transport exists;
- semantic set membership can be compared without syntax-level substitution;
- required common support is `PASS`.

Different parent/baseline frames without an identified transport produce `NO_LICENSED_COMPARISON` even if cardinalities are available.

## 7.3 `R_DeltaC`

For licensed deltas `G_i=(C+_i,C-_i)` and `G_j=(C+_j,C-_j)`:

```text
C+_i == C+_j and C-_i == C-_j                         -> EQUIVALENT
C+_i superseteq C+_j and C-_i superseteq C-_j,
  with at least one strict containment                -> I_GREATER
C+_j superseteq C+_i and C-_j superseteq C-_i,
  with at least one strict containment                -> J_GREATER
otherwise                                               -> INCOMPARABLE
```

`I_GREATER` means a set-theoretically greater semantic delta, not a better extension.

## 7.4 `T_DeltaC^cmp`

Admissible transformations are:

- bijective world-state relabeling applied to both records;
- semantic partition-handle renaming;
- polarity-equivalent representation changes already licensed by `M_DeltaC`;
- candidate and enumeration-order permutations.

Set inclusion/equality must be invariant.

## 7.5 `F_DeltaC^cmp`

The comparator is invalid if cardinality-only comparison turns crossed semantic sets into equality or direction.

---

# 8. `C_collateral` — collateral vector comparison

## 8.1 `D_collateral`

The native object is the complete labeled signed collateral vector:

\[
R_{\rm collateral}(s)=(r_1,\ldots,r_m)
\]

with component-level status, lineage, contract identity, and support.

## 8.2 `Lambda_collateral`

Comparison is licensed only if:

- both candidate-level statuses are `IDENTIFIED` for the required vector;
- every compared component is identified for both candidates;
- the same labeled contract family is used, up to a licensed common permutation;
- each component uses a compatible signed consequence scale;
- required common support is `PASS` componentwise.

## 8.3 `R_collateral`

For licensed vectors `r_i,r_j` on the same labeled components:

```text
all components equal                                  -> EQUIVALENT
r_i[c] >= r_j[c] for all c, at least one strict       -> I_GREATER
r_j[c] >= r_i[c] for all c, at least one strict       -> J_GREATER
otherwise                                               -> INCOMPARABLE
```

No mean, weighted mean, sign count, max loss, or other scalar collapse is part of this relation.

## 8.4 `T_collateral^cmp`

Admissible transformations are:

- common component-label permutation with labels carried through;
- independent positive-affine transformations of each underlying component consequence scale applied to both candidates on that component, which preserve signed pairwise direction;
- candidate-handle renaming;
- serialization-order permutation.

## 8.5 `F_collateral^cmp`

The comparator is invalid if a scalar mean or other aggregate converts a crossed vector into `EQUIVALENT`, `I_GREATER`, or `J_GREATER`.

---

# 9. `C_reopen` — reopenability comparison

## 9.1 `D_reopen`

The native object is the complete labeled binary stress vector plus its descriptive finite-panel frequency:

\[
Y(s)=(Y_1,\ldots,Y_m),
\qquad
R_{\rm reopen}(s)=m^{-1}\sum_jY_j.
\]

The stress vector, not frequency alone, defines the native relation.

## 9.2 `Lambda_reopen`

Comparison is licensed only if:

- both statuses are `IDENTIFIED`;
- the complete stress vectors are available;
- stress-family checksum, deadline, update harness, challenge/refinement apparatus, and certificate semantics are compatible;
- required common support is `PASS`;
- no stress-family bridge is invented after seeing frequencies.

Different stress-family checksums without a preregistered bijection produce `NO_LICENSED_COMPARISON`.

## 9.3 `R_reopen`

For licensed binary vectors `Y_i,Y_j`:

```text
vectors exactly equal                                 -> EQUIVALENT
Y_i[j] >= Y_j[j] for all j, at least one strict       -> I_GREATER
Y_j[j] >= Y_i[j] for all j, at least one strict       -> J_GREATER
otherwise                                               -> INCOMPARABLE
```

Equal finite-panel frequency with different stresswise success patterns is **not** equivalence.

## 9.4 `T_reopen^cmp`

Admissible transformations are:

- common stress-identifier permutation preserving the stress mapping;
- graph/node relabeling already licensed by `M_reopen`;
- candidate-handle renaming;
- enumeration-order permutation.

## 9.5 `F_reopen^cmp`

The comparator is invalid if:

- frequency-only comparison calls different stress vectors equivalent;
- incompatible stress families are compared because their frequencies share a numerical scale;
- immediate corrective performance substitutes for reopenability.

---

# 10. `C_scope` — support relation and license constraint

`Scope` has **no preference authority**.

Its primary operational role is to gate `Lambda_k` for the other coordinates.

## 10.1 `D_scope`

The native scope object is the labeled regime-status map with statuses:

```text
PASS
FAIL
NOT_TESTED
```

For descriptive relation output, define the support set:

\[
S(s)=\{r:\operatorname{status}(s,r)=\texttt{PASS}\}.
\]

## 10.2 `Lambda_scope`

A direct descriptive support-set comparison is licensed only if both scope records use the same regime universe or a preregistered bijective regime relabeling.

For coordinate `k`, the comparison license uses:

\[
S_{ij,k}=S_{i,k}\cap S_{j,k}.
\]

The required common support must be nonempty and must satisfy the coordinate-specific frame requirements.

`FAIL` and `NOT_TESTED` never enter common support.

## 10.3 `R_scope`

When a direct support-set relation is licensed:

```text
S_i == S_j                                      -> EQUIVALENT
S_i strict superset S_j                         -> I_GREATER
S_j strict superset S_i                         -> J_GREATER
otherwise                                       -> INCOMPARABLE
```

These outputs describe evidential support topology only.

They cannot be interpreted as extension quality and cannot enter a later score without a separately preregistered downstream rule.

If the coordinate-specific common support required for a proposed comparison is empty, the proposed coordinate relation is `NO_LICENSED_COMPARISON` regardless of effect magnitude.

## 10.4 `T_scope^cmp`

Admissible transformations are:

- common regime-identifier permutation;
- serialization-order permutation;
- candidate-handle renaming.

PASS/FAIL/NOT_TESTED semantics must remain unchanged.

## 10.5 `F_scope^cmp`

The comparator is invalid if favorable effect magnitude overrides `FAIL`, `NOT_TESTED`, an empty support intersection, or an incompatible comparison frame.

---

# 11. Absolute separation of two null-like outcomes

The execution must hard-assert:

\[
\boxed{
\texttt{INCOMPARABLE}
\neq
\texttt{NO\_LICENSED\_COMPARISON}.
}
\]

`INCOMPARABLE` means:

```text
both records identified
comparison frame licensed
common support sufficient
native relation evaluated
no direction/equivalence follows
```

`NO_LICENSED_COMPARISON` means one or more of:

```text
NOT_IDENTIFIED input
incompatible native type
unsupported or empty common scope
unbridged causal contrast frame
unbridged burden schema
unbridged semantic geometry frame
unbridged collateral contract family
unbridged reopenability stress family
missing required lineage
```

No execution path may convert `NO_LICENSED_COMPARISON` into `INCOMPARABLE` merely to avoid missingness.

---

# 12. Frozen finite calibration panel

The comparison-identification execution uses synthetic typed calibration records only.

No actual extension candidate pair may be used to calibrate the comparator.

Use exactly 64 anonymous encodings for every applicable calibration case.

The same semantic calibration case must survive candidate-handle swapping, label permutation, and serialization-order changes.

All finite calibration values are exact; no statistical tolerance or uncertainty rule is introduced in this gate.

The six mandatory calibration classes are:

\[
\boxed{
\begin{array}{ll}
A:&\text{native equality}\rightarrow\texttt{EQUIVALENT}\\
B:&\text{strict native difference}\rightarrow\text{correct native direction}\\
C:&\text{crossed native relation}\rightarrow\texttt{INCOMPARABLE}\\
D:&\texttt{NOT\_IDENTIFIED}\rightarrow\texttt{NO\_LICENSED\_COMPARISON}\\
E:&\text{unsupported/incompatible scope}\rightarrow\texttt{NO\_LICENSED\_COMPARISON}\\
F:&\text{licensed transformation}\rightarrow\text{relation preserved}.
\end{array}}
\]

Class `C` is not applicable to the exact scalar total order `C_DeltaV`; it is mandatory for `C_B`, `C_DeltaC`, `C_collateral`, `C_reopen`, and direct descriptive `C_scope` calibration.

---

# 13. Exact calibration fixtures

The child executable must construct the following anonymous fixtures before random relabeling.

## 13.1 `C_DeltaV`

Common frame:

```text
panel_id: DV_CAL_PANEL
contrast_frame: DV_CAL_CONTRAST
support: {r0, r1}
```

Fixtures:

```text
A: i=1/4, j=1/4                                  -> EQUIVALENT
B: i=3/8, j=1/8                                  -> I_GREATER
D: i=1/4 IDENTIFIED, j=NOT_IDENTIFIED            -> NO_LICENSED_COMPARISON
E: i support={r0}, j support={r1}                 -> NO_LICENSED_COMPARISON
F: apply v' = a*v with a in {1/2,2,3}; relation  -> preserved
```

Pair-swapping `B` must emit `J_GREATER`.

## 13.2 `C_B`

Ledger category order in the implementation may be permuted, but semantics remain the six frozen categories.

Fixtures use one-ledger envelopes unless explicitly stated:

```text
A:
  i={(1,1,0,0,0,0)}
  j={(1,1,0,0,0,0)}                              -> EQUIVALENT

B:
  i={(2,1,0,0,0,0)}
  j={(1,1,0,0,0,0)}                              -> I_GREATER

C:
  i={(2,0,0,0,0,0)}
  j={(0,2,0,0,0,0)}                              -> INCOMPARABLE

D:
  j=NOT_IDENTIFIED                                -> NO_LICENSED_COMPARISON

E:
  incompatible burden schema / no bridge          -> NO_LICENSED_COMPARISON

F:
  replace visible representation with a one-token
  transparent alias expanding to identical semantic obligations
                                                   -> relation preserved
```

Additional envelope control:

```text
i={(2,1,0,0,0,0),(1,2,0,0,0,0)}
j={(1,1,0,0,0,0)}
```

must emit `I_GREATER` because every retained minimal ledger of `i` componentwise contains `j` and each is strict somewhere.

A crossed alternative-envelope fixture must emit `INCOMPARABLE`.

## 13.3 `C_DeltaC`

Use an anonymous semantic universe with elements `{a,b,c,d}` and a common baseline frame.

```text
A:
  i=({a,b},{})
  j=({a,b},{})                                    -> EQUIVALENT

B:
  i=({a,b},{})
  j=({a},{})                                      -> I_GREATER

C:
  i=({a,b},{})
  j=({a,c},{})                                    -> INCOMPARABLE

D:
  j=NOT_IDENTIFIED                                -> NO_LICENSED_COMPARISON

E:
  same cardinalities but different unbridged baseline frame
                                                   -> NO_LICENSED_COMPARISON

F:
  apply a common bijection over {a,b,c,d}          -> relation preserved
```

The `C` fixture is the primary cardinality-only falsifier: both `C_plus` sets have cardinality 2 but are not equivalent and neither contains the other.

## 13.4 `C_collateral`

Use four labeled collateral components `{c1,c2,c3,c4}`.

```text
A:
  i=(0,0,0,0)
  j=(0,0,0,0)                                    -> EQUIVALENT

B:
  i=(1/4,0,0,0)
  j=(0,0,0,0)                                    -> I_GREATER

C:
  i=(1/2,-1/2,0,0)
  j=(0,0,0,0)                                    -> INCOMPARABLE

D:
  j=NOT_IDENTIFIED                                -> NO_LICENSED_COMPARISON

E:
  incompatible labeled contract family            -> NO_LICENSED_COMPARISON

F:
  common component permutation plus independent
  positive affine outcome rescaling per component -> relation preserved
```

The `C` fixture has equal arithmetic mean and is the primary mean-collapse falsifier.

## 13.5 `C_reopen`

Use eight labeled stresses `{rho1,...,rho8}`.

```text
A:
  i=(1,0,1,0,1,0,1,0)
  j=(1,0,1,0,1,0,1,0)                           -> EQUIVALENT

B:
  i=(1,1,1,0,1,0,1,0)
  j=(1,0,1,0,1,0,1,0)                           -> I_GREATER

C:
  i=(1,0,1,0,1,0,1,0)
  j=(0,1,1,0,1,0,1,0)                           -> INCOMPARABLE

D:
  j=NOT_IDENTIFIED                                -> NO_LICENSED_COMPARISON

E:
  equal numerical frequencies but incompatible
  stress-family checksum                          -> NO_LICENSED_COMPARISON

F:
  common stress-label permutation                 -> relation preserved
```

The `C` fixture has equal finite-panel frequency and is the primary frequency-only falsifier.

## 13.6 `C_scope`

Use regime universe `{r1,r2,r3,r4}`.

```text
A:
  S_i={r1,r2}
  S_j={r1,r2}                                     -> EQUIVALENT

B:
  S_i={r1,r2,r3}
  S_j={r1,r2}                                     -> I_GREATER

C:
  S_i={r1,r2}
  S_j={r1,r3}                                     -> INCOMPARABLE

D:
  j scope record missing / NOT_IDENTIFIED         -> NO_LICENSED_COMPARISON

E:
  coordinate-specific required supports are
  disjoint: S_i={r1}, S_j={r2}                    -> NO_LICENSED_COMPARISON

F:
  common regime-label permutation                 -> relation preserved
```

A favorable synthetic effect magnitude may be attached to the `E` fixture but must not change `NO_LICENSED_COMPARISON`.

---

# 14. Broken comparator controls

Each native comparator has one preregistered forbidden shortcut.

The child executable must implement the shortcut only as a negative control and show that it disagrees with the frozen native contract on the targeted calibration fixture.

| comparator | forbidden shortcut | required failure |
|---|---|---|
| `DeltaV` | skip causal/common-scope license and numerically compare missing/out-of-scope values | emits a relation where native result is `NO_LICENSED_COMPARISON` |
| `B` | compare visible syntax/token count only | alias fixture changes direction/equality despite identical semantic burden |
| `DeltaC` | compare `|C_plus|,|C_minus|` only | crossed equal-cardinality fixture is falsely called equivalent or directed |
| `collateral` | compare arithmetic means | crossed equal-mean fixture is falsely called equivalent |
| `reopen` | compare only finite-panel frequency | crossed equal-frequency stress vectors are falsely called equivalent |
| `Scope` | allow favorable effect magnitude to override failed/empty support | unsupported fixture is falsely licensed |

For every coordinate:

\[
\boxed{
F_k^{\rm cmp}=1
}
\]

iff the deliberately broken comparator violates the frozen relation/license contract on its targeted control.

A successful audit requires every broken control to be detected in every anonymous encoding.

---

# 15. Cross-cutting algebraic controls

For every applicable comparator and every anonymous encoding, assert:

## 15.1 Pair-swap symmetry

```text
I_GREATER  <-> J_GREATER
EQUIVALENT -> EQUIVALENT
INCOMPARABLE -> INCOMPARABLE
NO_LICENSED_COMPARISON -> NO_LICENSED_COMPARISON
```

when candidate handles `i` and `j` are swapped.

## 15.2 Reflexive relation

For any fully licensed native record `x`:

```text
R_k(x,x) = EQUIVALENT
```

This does not apply to an unlicensed or missing record; such a record remains `NO_LICENSED_COMPARISON`.

## 15.3 Transformation invariance

Every transformation in `T_k^cmp` must preserve the native relation token after relabeling the witness back to the canonical semantic frame.

## 15.4 Provenance blindness

Changing only provenance class or candidate handle while preserving the complete native record must not change `Lambda_k` or `R_k`.

## 15.5 No cross-coordinate leakage

Changing a non-`k` coordinate while holding the complete `D_k` record fixed must not change `Lambda_k` or `R_k`.

---

# 16. Anonymous encoding protocol

Use exactly 64 encodings per applicable calibration fixture.

Use deterministic seed namespace:

```text
comparison-identification-v1 / encoding 0..63
```

Randomize as applicable:

- candidate handles;
- pair presentation order;
- semantic-universe handles;
- obligation handles;
- contract labels;
- stress labels;
- regime labels;
- enumeration order;
- serialization order;
- public binary labels where the upstream measurement object admits them.

No randomization may alter the semantic relation or license status.

No seed may depend on a comparator output.

---

# 17. Comparator evidence lineage `L_k^cmp`

Every emitted calibration relation must carry lineage containing at least:

```text
comparison_contract_id
calibration_fixture_id
input_status_i
input_status_j
input_native_type
input_measurement_lineage_class
comparison_frame_id
support_intersection
license_conditions_checked
license_result
native_relation_witness
admissible_transform_applied if any
output_relation
broken_control flag
anonymous_encoding_id
```

`L_k^cmp` must preserve the distinction between:

```text
relation identified
relation incomparable
comparison unlicensed
```

No lineage from one coordinate may license a relation on another coordinate.

---

# 18. Calibration success criteria

The gate passes only if all of the following hold.

For each of the six comparator contracts:

1. all applicable `A` equality cases return `EQUIVALENT` in `64/64` encodings;
2. all `B` strict cases return the correct native direction in `64/64` encodings;
3. all applicable `C` crossed cases return `INCOMPARABLE` in `64/64` encodings;
4. all `D` missing-identification cases return `NO_LICENSED_COMPARISON` in `64/64` encodings;
5. all `E` unsupported/incompatible-scope cases return `NO_LICENSED_COMPARISON` in `64/64` encodings;
6. all `F` admissible-transformation cases preserve the original relation in `64/64` encodings;
7. the coordinate-specific broken comparator triggers its `F_k^cmp` invalidity signature in `64/64` encodings;
8. pair-swap symmetry holds in `64/64` encodings;
9. reflexivity holds wherever license is valid;
10. provenance blindness holds;
11. no cross-coordinate leakage occurs;
12. no actual candidate pair is evaluated.

The suite as a whole must demonstrate all five output tokens at least once where mathematically applicable.

A partial pass does not license application to candidate records.

---

# 19. Upstream hard-regression requirements

The child executable must import or checksum-verify the candidate-measurement and measurement-identification results.

At minimum assert the upstream facts:

```text
candidate_count = 12
post_measurement_pruning = 0
post_measurement_addition = 0
candidate_comparison_performed = false
Q_extension_defined = false
authorization_performed = false
binding_performed = false
not_identified_candidate_coordinate_cells = 12

M_ext architecture identified = true
measurement aggregation defined = false
```

The executable may use the committed upstream result as a hard-regression source if deeper historical process replay is unavailable, but the scientific provenance must say so.

Correct result wording unless the full upstream chain is freshly replayed:

\[
\boxed{
\textbf{fresh comparison-identification result with inherited hard regression assertions}.
}
\]

---

# 20. Anti-preference / anti-aggregation contract

The execution and result note must not compute, emit, or imply:

- `s_i > s_j` as an overall candidate ordering;
- `s_i \succ s_j`;
- pairwise candidate preference matrices;
- Pareto dominance or Pareto frontiers across extension candidates;
- cross-coordinate dominance counts;
- weighted sums;
- normalized common scales;
- lexicographic preference rules;
- coordinate priority rules;
- tradeoff rates;
- utility functions;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- adoption thresholds;
- authorization status;
- binding status;
- a best synthesized candidate;
- a best external candidate;
- Hudson/Rubi superiority or inferiority.

The output tokens `I_GREATER` and `J_GREATER` are coordinate-native relation tokens only.

They are forbidden from being reserialized as `better`, `winner`, `preferred`, `recommended`, or equivalent language.

The execution must include hard flags:

```text
actual_candidate_pair_relations_computed = false
candidate_preference_defined = false
Pareto_filtering_performed = false
cross_coordinate_aggregation_defined = false
Q_extension_defined = false
NO_WARRANTED_ADOPTION_defined = false
authorization_performed = false
binding_performed = false
```

---

# 21. Wrong-control ceilings / discriminants

The audit must report the following restricted wrong controls separately from the primary comparator architecture.

## W1 — `NOT_IDENTIFIED -> 0`

Treat every missing scalar/vector component as numerical zero and compare anyway.

Required falsification: fails class `D` and/or native-type requirements.

## W2 — scalarize every native object

Use:

```text
burden total only
geometry cardinality only
collateral mean
reopenability frequency only
scope cardinality only
```

Required falsification: at minimum the frozen crossed `C` fixtures for geometry, collateral, and reopenability must defeat this shortcut.

## W3 — scope-blind comparator

Ignore support intersection and compare any two populated numbers/sets/vectors.

Required falsification: class `E` must defeat it.

## W4 — one-coordinate-to-preference leak

Map any `I_GREATER` token to `PREFER_I` and any `J_GREATER` token to `PREFER_J`.

This control is invalid by construction because preference is outside the gate. The child executable must assert that no such output type exists in the primary architecture.

---

# 22. Failure interpretation

| Observation | Interpretation |
|---|---|
| missing value numerically compared | license failure / imputation leakage |
| crossed native relation forced into direction | partial-order collapse |
| unsupported scope produces a relation | scope-license failure |
| geometry relation changes under semantic relabeling | comparator invariance failure |
| visible alias changes burden relation | anti-scaffold comparison failure |
| equal collateral means erase component crossing | unauthorized scalarization |
| equal reopenability frequencies erase stress crossing | native-type collapse |
| actual Hudson or synthesized pair receives a preference | downstream preference leakage |
| actual candidate pair is evaluated during calibration | post-measurement comparator tuning risk; preregistration violation |
| all calibration relations/license boundaries survive controls | comparison-identification gate may pass |

---

# 23. Claim boundary if execution succeeds

The strongest permitted claim is exactly:

\[
\boxed{
\textbf{
The native pairwise relations supported by the identified extension measurements are themselves empirically identifiable in these finite calibration regimes, with comparison license, native partial-order structure, incomparability, transformation invariance, and missing-identification boundaries preserved.
}
}
\]

A pass does **not** establish:

- any pairwise relation between the 12 actual extension candidates;
- that one extension candidate is better than another;
- Pareto dominance among candidates;
- any coordinate priority;
- any cross-coordinate tradeoff rate;
- any extension-value function;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- Hudson/Rubi superiority or inferiority;
- authorization;
- binding;
- persistence;
- post-adoption consequence;
- general self-modification;
- research agency.

---

# 24. Frozen next sequence

The empirical sequence is now:

\[
\boxed{
\mathcal M_{\rm ext}\text{ identification}\checkmark
\rightarrow
s\rightarrow\mathcal V_{\rm ext}(s)\checkmark
\rightarrow
\boxed{\mathcal R_{\rm compare}\text{ identification [preregistered]}}
\rightarrow
\text{comparison-identification execution}
\rightarrow
\text{actual-candidate comparison application [undefined]}
\rightarrow
Q_{\rm extension}\text{ [undefined]}
\rightarrow
Auth\text{ [undefined]}
\rightarrow
Bind\text{ [undefined]}.
}
\]

The only authorized next repository action is execution of this comparison-identification preregistration.

No dependency-ledger update, actual-candidate comparison artifact, Pareto artifact, `Q_extension` artifact, adoption artifact, authorization artifact, or binding artifact is authorized before that execution result exists.
