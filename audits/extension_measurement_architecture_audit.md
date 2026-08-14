# Extension Measurement Architecture Identification Audit — Results

## Provenance

Preregistered before execution at:

```text
338981353778dd4efd6c5e0b0106a2d0828710c9
```

Extension-synthesis anchor:

```text
9a50f07  extension synthesis relative to supplied M0
```

The six measurement-identification calibration families were executed freshly against the preregistered instruments. The committed executable imports the extension-synthesis audit and hard-asserts the synthesis anchors when run in-repo; that upstream chain was not freshly process-replayed in this connector session.

Correct provenance:

\[
\boxed{\textbf{fresh measurement-identification result with inherited hard regression assertions}.}
\]

No synthesized candidate, Rubi-style comparator, or preferred extension was used to define or tune any measurement coordinate. No candidate comparison, `Q_extension`, adoption rule, authorization rule, or binding operation is introduced here.

---

## 1. Frozen endpoint

The audit tests only whether:

\[
\boxed{
\mathcal M_{\rm ext}
=
\{M_{\Delta V},M_B,M_{\Delta C},M_{\rm collateral},M_{\rm reopen},M_{\rm scope}\}
}
\]

is identified in the finite calibration regimes under the preregistered contracts:

\[
M_k=(O_k,do_k,m_k,\mathcal T_k,F_k,L_k).
\]

The governing rule remains:

\[
\boxed{\textbf{measure first}\rightarrow\textbf{compare second}\rightarrow\textbf{aggregate last}.}
\]

---

## 2. Aggregate identification result

For every finite calibration family, 64 anonymous encodings were used. Each coordinate had to recover its calibration controls, remain invariant under its licensed transformation class, trigger its own `F_k` on a deliberately broken instrument, and preserve its independent evidence lineage.

| Coordinate | calibration | invariance | `F_k` triggered | lineage |
|---|---:|---:|---:|---:|
| `M_DeltaV` | 64/64 | 64/64 | 64/64 | 64/64 |
| `M_B` | 64/64 | 64/64 | 64/64 | 64/64 |
| `M_DeltaC` | 64/64 | 64/64 | 64/64 | 64/64 |
| `M_collateral` | 64/64 | 64/64 | 64/64 | 64/64 |
| `M_reopen` | 64/64 | 64/64 | 64/64 | 64/64 |
| `M_scope` | 64/64 | 64/64 | 64/64 | 64/64 |

Therefore:

\[
\boxed{\mathcal M_{\rm ext}\text{ is identified in the audited finite calibration regimes.}}
\]

This licenses later measurement of candidate transformations under these coordinates. It does not license candidate ranking or aggregation.

---

## 3. `M_DeltaV` — corrective consequence

The semantic no-op control recovered:

\[
\boxed{\Delta V_{\rm corr}=0}
\]

exactly on 64/64 encodings. A controlled construction intervention recovered the known held-out paired effect:

\[
\boxed{\Delta V_{\rm corr}=0.25}
\]

on 64/64 encodings. Under positive affine transformations `V'=aV+b`, `a>0`, the measured effect obeyed `DeltaV'=a DeltaV` on 64/64 encodings.

The deliberately broken instrument added a syntax-dependent bonus to a semantic no-op, producing a false nonzero effect. `F_DeltaV` rejected it on 64/64 encodings.

Thus the instrument distinguishes extension-attributable consequence from candidate identity or syntax.

---

## 4. `M_B` — expanded specification burden

The calibration transformation was represented four ways.

```text
explicit representation:
  expanded total = 3

transparent alias:
  visible count  = 1
  expanded total = 3

opaque macro:
  expanded total = 3
  hidden obligations charged = 2

target-specific mapping:
  expanded total = 6
  target-specific bindings charged = 4
```

Hence:

\[
\boxed{B_{\rm visible}\downarrow\not\Rightarrow B_{\rm extension}\downarrow.}
\]

The deliberately broken visible-token counter falsely treated the alias as lower burden and was rejected by `F_B` on 64/64 encodings.

---

## 5. `M_DeltaC` — construction-space geometry

The semantic closure instrument recovered three exact controls.

Syntax-only / no-geometry:

\[
\boxed{|\mathcal C_+|=0,\qquad |\mathcal C_-|=0.}
\]

Known basin opening:

\[
\boxed{|\mathcal C_+|=105,\qquad |\mathcal C_-|=0,}
\]

with candidate closure size `120` and checksum:

```text
8d3a5ecddbcf823c2ffca59f2490d2950caea216816b3c8e9af58bb2dfbb5dc1
```

Known removal:

\[
\boxed{|\mathcal C_+|=0,\qquad |\mathcal C_-|=8.}
\]

All semantic deltas were invariant under the licensed anonymous isomorphisms on 64/64 encodings. A deliberately broken raw-syntax counter treated complements as new experiments even though semantic partition deduplication eliminates them; `F_DeltaC` rejected that instrument on 64/64 encodings.

---

## 6. `M_collateral` — vector-valued collateral consequence

The frozen three-contract panel recovered:

\[
\boxed{R_{\rm collateral}(\text{no-op})=(0,0,0)}
\]

and the localized controlled intervention recovered:

\[
\boxed{R_{\rm collateral}=(0,0,0.5).}
\]

Only the intended contract component changed. Independent positive-affine transformations of each contract scale preserved the componentwise causal effects, and contract-index permutation preserved the labeled vector on 64/64 encodings.

A deliberately broken scalar mean was rejected because the native object is the labeled vector, not an aggregate scalar.

---

## 7. `M_reopen` — future corrective reachability

The critical calibration pair was matched on immediate corrective consequence:

\[
\boxed{\Delta V_{\rm corr}^{\rm preserve}=\Delta V_{\rm corr}^{\rm block}=0.25.}
\]

But the exact held-out future repair graphs differ:

```text
path-preserving transformation: R_reopen = 1.0
path-blocking transformation:   R_reopen = 0.5
```

with exhaustive finite path certificates and no evaluator-added evidence or authority.

Thus on all 64 encodings:

\[
\boxed{\Delta V_{\rm corr}\text{ matched}\not\Rightarrow R_{\rm reopen}\text{ matched}.}
\]

A deliberately broken immediate-performance proxy assigned the same signal to both transformations and was rejected by `F_reopen` on 64/64 encodings.

---

## 8. `M_scope` — support as a validity constraint

The calibration matrix contained one shared-valid regime, five coordinate-specific `FAIL` regimes, and five coordinate-specific `NOT-TESTED` regimes.

For every coordinate, the shared-valid regime entered support, its coordinate-specific `FAIL` regime was excluded, and its coordinate-specific `NOT-TESTED` regime was excluded. The conservative common support intersection contained only the shared-valid regime. Regime relabeling left membership invariant on 64/64 encodings.

A deliberately broken rule allowing favorable effect magnitude to override `FAIL` or `NOT-TESTED` was rejected by `F_scope` on 64/64 encodings.

Therefore:

\[
\boxed{\text{effect magnitude}\not\Rightarrow\text{measurement license}.}
\]

---

## 9. Cross-coordinate separation

All five preregistered anti-proxy crossings passed on all 64 anonymous encodings.

- X1: a transformation added 105 semantic partitions while the frozen target was already exactly resolved, so `DeltaV_corr=0`.
- X2: a one-token transparent alias and a three-token explicit representation had identical expanded burden.
- X3: immediate consequence was matched at `0.25`, while reopenability separated `1.0` from `0.5`.
- X4: a controlled structural replacement produced active `DeltaV_corr=+0.5` while simultaneously producing collateral `r=-0.5` on a frozen non-target contract.
- X5: a strong effect did not admit a regime whose coordinate-specific identification status was `FAIL`.

```text
X1 64/64
X2 64/64
X3 64/64
X4 64/64
X5 64/64
```

These are measurement discriminants, not extension rankings.

---

## 10. Evidence lineage

Each coordinate retained an independent lineage object carrying its own calibration source, intervention/evaluator or accounting structure, licensed transformations, and validation status.

The audit does not infer:

\[
\boxed{L_i\Rightarrow L_j.}
\]

Collateral components remain separately labeled, and scope membership is derived from the explicit PASS/FAIL/NOT-TESTED matrix.

---

## 11. Anti-leakage / anti-aggregation status

```text
candidate comparison performed       false
Q_extension defined                  false
Rubi comparator used                 false
adoption semantics present           false
authorization performed              false
binding performed                    false
```

No synthesized A/B/C candidate identity participated in choosing or tuning the measurement controls.

The coordinate system therefore preserves the preregistered provenance direction:

\[
\boxed{\mathcal M_{\rm ext}\text{ frozen}\rightarrow\text{future candidate measurement}.}
\]

---

## 12. Earned claim

The strongest permitted claim is:

\[
\boxed{\textbf{In the audited finite regimes, the six extension-measurement objects are independently operationalized and identified under their preregistered intervention contrasts, invariance classes, failure signatures, and evidence lineages.}}
\]

This result licenses the next empirical question:

\[
\boxed{\text{measure candidate transformations under }\mathcal M_{\rm ext}.}
\]

It does not establish an aggregate `Q_extension`, a candidate ranking, any coordinate weight, Rubi superiority or inferiority, `NO_WARRANTED_ADOPTION`, authorization, binding, persistence, or post-adoption consequence.

The sequence remains:

\[
\boxed{\mathcal M_{\rm ext}\text{ identification}\checkmark\rightarrow\mathcal V_{\rm ext}(s)\rightarrow Q_{\rm extension}\rightarrow Auth\rightarrow Bind.}
\]
