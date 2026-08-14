# Extension Candidate Measurement Audit — Results

## Provenance

Preregistered before execution at:

```text
6850a2f421d4477c45f679dcf03909f914788bbc
```

Measurement architecture identified at:

```text
607502a9434884ca9bb06d5ddd6ff6c17f2ef002
```

The candidate-measurement panel was executed freshly against the preregistered 12-record registry. The committed executable imports and hard-asserts the measurement-identification audit; in this execution environment the deeper upstream process chain was not fully replayable, so the already-committed `607502a` result was used as the fallback hard-regression source after the import reached a missing older module.

Correct provenance:

\[
\boxed{\textbf{fresh candidate-measurement result with inherited hard regression assertions}.}
\]

No candidate comparison, Pareto filtering, `Q_extension`, adoption rule, authorization rule, or binding operation is introduced here.

---

## 1. Frozen endpoint

The audit tests only:

\[
\boxed{s\longrightarrow\mathcal V_{\rm ext}(s)}
\]

for the preregistered candidate universe:

```text
SYNTHESIZED  4
EXTERNAL     4
CONTROL      4
----------------
TOTAL       12
```

Observed:

```text
expected candidates          12
observed candidates          12
post-measurement pruning      0
post-measurement addition     0
anonymous encodings          64
```

Every candidate record remains present irrespective of coordinate status.

---

## 2. Missing-identification discipline

Exactly 12 candidate-coordinate cells are `NOT_IDENTIFIED`:

```text
4 Hudson composites x {DeltaV, collateral, reopen}
```

All 12 contain:

```text
status       NOT_IDENTIFIED
native_value null
explicit failed-identification condition
```

Observed:

```text
zero imputation       false
negative relabeling   false
numeric imputation    false
candidate deletion    false
```

Therefore:

\[
\boxed{
\texttt{NOT\_IDENTIFIED}\neq0\neq\text{negative consequence}.
}
\]

and:

\[
\boxed{\texttt{NOT\_IDENTIFIED}\not\rightarrow\text{imputation}.}
\]

---

## 3. Hudson/Rubi scope result

The external wrapper was not allowed to enlarge the measurement ontology.

The existing guards resolve the composite intervention as:

```text
DeltaV      NOT_IDENTIFIED
B           IDENTIFIED
DeltaC      IDENTIFIED via frozen structural projection
collateral  NOT_IDENTIFIED
reopen      NOT_IDENTIFIED
Scope       IDENTIFIED
```

`M_DeltaV` and `M_collateral` were identified for construction-only causal contrasts; the Hudson composite changes goal/action/reward semantics. `M_reopen` at `607502a` was not identified on this composite goal/action transformation regime. Those instruments therefore remain unchanged and emit missing identification rather than a fabricated value.

The geometry coordinate is identified because the preregistered structural projection is the underlying synthesized repair and the wrapper adds no experiment-construction rule. The burden coordinate is identified because its object is the expanded semantic specification ledger and explicitly includes the eight frozen external wrapper obligations.

No Hudson/Rubi superiority or inferiority claim is made.

---

## 4. Canonical candidate records

The following table co-displays the native measurements in candidate-ID order. It is **not a ranking** and no row ordering is derived from a measured coordinate.

| candidate | provenance | `DeltaV_corr` panel mean | `B_extension` | `DeltaC` cardinalities | `R_collateral` vector | `R_reopen` |
|---|---|---:|---|---|---|---:|
| `CTRL_ALIAS_A` | CONTROL | 0.096153846154 | expanded=6, incremental=2; ledgers=4 | (+105, -0) | [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] | 1.000 |
| `CTRL_ID_DEG2` | CONTROL | 0.000000000000 | expanded=1, incremental=0; ledgers=1 | (+0, -0) | [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] | 1.000 |
| `CTRL_ID_LINEAR` | CONTROL | 0.000000000000 | expanded=1, incremental=0; ledgers=1 | (+0, -0) | [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] | 0.500 |
| `CTRL_SUPPLIED_DEG2` | CONTROL | 0.192307692308 | expanded=8, incremental=3; ledgers=1 | (+1008, -0) | [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] | 1.000 |
| `EXT_CT_A` | EXTERNAL | NOT_IDENTIFIED | expanded=14, incremental=10; ledgers=4 | (+105, -0) | NOT_IDENTIFIED | NOT_IDENTIFIED |
| `EXT_CT_B` | EXTERNAL | NOT_IDENTIFIED | expanded=14, incremental=10; ledgers=1 | (+35, -0) | NOT_IDENTIFIED | NOT_IDENTIFIED |
| `EXT_CT_C1` | EXTERNAL | NOT_IDENTIFIED | expanded=15, incremental=10; ledgers=1 | (+630, -0) | NOT_IDENTIFIED | NOT_IDENTIFIED |
| `EXT_CT_C2` | EXTERNAL | NOT_IDENTIFIED | expanded=15, incremental=9, expanded=15, incremental=10; ledgers=4 | (+1365, -0) | NOT_IDENTIFIED | NOT_IDENTIFIED |
| `SYN_A_120` | SYNTHESIZED | 0.096153846154 | expanded=6, incremental=2; ledgers=4 | (+105, -0) | [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] | 1.000 |
| `SYN_B_50` | SYNTHESIZED | 0.096153846154 | expanded=6, incremental=2; ledgers=1 | (+35, -0) | [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] | 1.000 |
| `SYN_C1_1653` | SYNTHESIZED | 0.028846153846 | expanded=7, incremental=2; ledgers=1 | (+630, -0) | [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] | 1.000 |
| `SYN_C2_2388` | SYNTHESIZED | 0.028846153846 | expanded=7, incremental=1, expanded=7, incremental=2; ledgers=4 | (+1365, -0) | [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] | 1.000 |

The JSON result retains the full native objects: all 13 per-contract `DeltaV` effects, all minimal burden obligation ledgers, complete `C_plus`/`C_minus` partition sets and checksums, all six collateral components, all eight reopenability stress outcomes, and coordinate-specific scope records.

For repository size without native-type loss, the committed JSON serializes the complete raw result as a **lossless zlib+base64 payload** with the uncompressed SHA-256 and byte count in the wrapper. The executable emits that packed form deterministically; decompression recovers the full JSON object exactly.

---

## 5. Held-out corrective panel

The frozen 13-contract panel excludes the synthesis targets. The structural candidates and controls were measured under the construction-only paired instrument with `kappa=0.1`.

Canonical panel means are present in the records exactly as measured; the per-contract effects are retained in JSON and are not converted into a cross-coordinate score.

The four external Hudson composites have no `DeltaV` number because their composite intervention is outside the identified `do_DeltaV` class.

---

## 6. Burden accounting

The burden instrument preserves the complete implementation envelopes rather than choosing a post-measurement representation.

Key controls:

```text
CTRL_ALIAS_A
  visible macro tokens = 1
  expanded total       = 6
  hidden obligations   = 2
  inherited obligations= 4

SYN_A_120
  expanded total       = 6
  explicit obligations = 2
  inherited obligations= 4
```

Thus the alias packaging does not make the A semantics disappear.

Each Hudson composite additionally carries all eight preregistered external wrapper obligations. No theorem assumption was used to promote an otherwise out-of-scope causal coordinate; those coordinates remain `NOT_IDENTIFIED`.

---

## 7. Geometry

The full semantic set-valued geometry is retained in JSON. Cardinalities are descriptive only.

```text
SYN_A_120 / CTRL_ALIAS_A / EXT_CT_A  C_plus=105,  C_minus=0
SYN_B_50 / EXT_CT_B                  C_plus=35,   C_minus=0
SYN_C1_1653 / EXT_CT_C1              C_plus=630,  C_minus=0
SYN_C2_2388 / EXT_CT_C2              C_plus=1365, C_minus=0
CTRL_ID_LINEAR                       C_plus=0,    C_minus=0
CTRL_ID_DEG2                         C_plus=0,    C_minus=0
CTRL_SUPPLIED_DEG2                   C_plus=1008, C_minus=0
```

These lines report structural facts only; no cardinality is treated as value.

---

## 8. Collateral and reopenability

For every construction-only candidate, the frozen six-component collateral panel is retained componentwise. In this panel each identified component effect is exactly zero. No mean or sign-count is substituted for the vector.

The frozen eight-stress reopenability records are retained as binary vectors plus their finite-panel frequency. The identity-linear control has frequency `0.5`; the other identified construction-only candidates have frequency `1.0` in this stress family. These are measurements under the frozen finite stress panel, not preference claims.

The Hudson composites receive neither a collateral vector nor a reopenability frequency because those composite causal regimes were not identified by the frozen instruments.

---

## 9. Anonymous invariance

For every candidate and every coordinate/status record:

```text
64/64 common anonymous encodings preserved the preregistered result/status
```

Randomization covered world labels, candidate order/handles, target identifiers, collateral identifiers, stress identifiers, public output polarity, update-bit public labels, and enumeration order as applicable.

No final record order depends on a measured value.

---

## 10. Anti-leakage status

```text
candidate comparison performed        false
ranking performed                     false
Pareto filtering performed            false
cross-coordinate aggregate defined    false
Q_extension defined                   false
NO_WARRANTED_ADOPTION defined         false
adoption semantics present            false
authorization performed               false
binding performed                     false
Hudson superiority/inferiority claim  false
```

The immutable-architecture condition held:

\[
\boxed{
\mathcal M_{\rm ext}^{\rm candidate}
=
\mathcal M_{\rm ext}^{\rm identified}.
}
\]

---

## 11. Earned claim

The strongest permitted claim is exactly:

\[
\boxed{
\textbf{
The preregistered synthesized, external, and control candidate records were measured under the previously identified extension-measurement architecture, with provenance, native coordinate types, coordinate-specific lineage, explicit identification status, and scope preserved.
}
}
\]

A pass does **not** establish a candidate ordering, Pareto relation, coordinate priority, tradeoff rate, `Q_extension`, Hudson/Rubi superiority or inferiority, `NO_WARRANTED_ADOPTION`, authorization, binding, persistence, or post-adoption consequence.

The next scientific object is therefore not yet defined in this execution artifact. The branch has produced candidate measurement records; any later comparison rule must be separately designed and preregistered.
