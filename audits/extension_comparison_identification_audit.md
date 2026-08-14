# Extension Comparison License / Native Relation Audit — Results

## Provenance

Preregistered before execution at:

```text
844573923269a767027e6052068b57961a54381b
```

Parent candidate-measurement execution:

```text
c0db168261ebfb32106382c34c992bf00ec1aa4c
```

Measurement architecture identified at:

```text
607502a9434884ca9bb06d5ddd6ff6c17f2ef002
```

The comparison-identification calibration panel was executed freshly. The 12 actual measured extension candidates were not instantiated as comparator pairs and were not used to tune any comparison contract.

The connector execution environment did not expose repository bytes to the local Python process. Exact upstream GitHub blob IDs and required summary facts were therefore verified separately through the GitHub connector; the committed executable performs exact Git-blob byte verification when run inside the repository.

Correct provenance:

\[
\boxed{\textbf{fresh comparison-identification result with inherited hard regression assertions}.}
\]

No actual-candidate comparison, preference, Pareto filtering, `Q_extension`, adoption rule, authorization, or binding operation is introduced here.

---

## 1. Frozen endpoint

The audit tests only:

\[
\boxed{
D_k\rightarrow\Lambda_k\rightarrow R_k
}
\]

for:

\[
\mathcal R_{\rm compare}
=
\{C_{\Delta V},C_B,C_{\Delta C},C_{\rm collateral},C_{\rm reopen},C_{\rm scope}\}.
\]

Observed:

```text
anonymous encodings per applicable fixture    64
actual candidate-pair evaluations              0
actual candidate-pair relations computed       false
candidate preference defined                    false
```

The five native output tokens all occur in the calibration suite:

```text
EQUIVALENT                     448
I_GREATER                      504
J_GREATER                      200
INCOMPARABLE                   320
NO_LICENSED_COMPARISON         768
```

`I_GREATER` and `J_GREATER` are coordinate-native relation tokens only.

---

## 2. Primary comparison-identification result

Every applicable preregistered fixture passed in every anonymous encoding.

| comparator | A equality | B strict | C crossed | D missing | E unsupported | F transform | broken shortcut |
|---|---:|---:|---:|---:|---:|---:|---:|
| `C_DeltaV` | 64/64 | 64/64 | n/a | 64/64 | 64/64 | 64/64 | 64/64 |
| `C_B` | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 |
| `C_DeltaC` | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 |
| `C_collateral` | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 |
| `C_reopen` | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 |
| `C_scope` | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 | 64/64 |

Cross-cutting controls also passed on every applicable calibration record:

```text
pair-swap symmetry            exact
reflexivity where licensed    exact
provenance blindness          exact
no cross-coordinate leakage   exact
transformation invariance     exact
```

Therefore:

\[
\boxed{
\mathcal R_{\rm compare}
\text{ is identified in the audited finite comparison regimes.}
}
\]

---

## 3. `INCOMPARABLE` versus `NO_LICENSED_COMPARISON`

The audit preserves the preregistered separation:

\[
\boxed{
\texttt{INCOMPARABLE}
\neq
\texttt{NO\_LICENSED\_COMPARISON}.
}
\]

Crossed native objects with complete identification and common support yield `INCOMPARABLE`:

- structured burden ledgers;
- semantic geometry sets;
- signed collateral vectors;
- stresswise reopenability vectors;
- descriptive support sets.

By contrast, missing identification or incompatible/empty support yields `NO_LICENSED_COMPARISON`.

No execution path converts missingness into incomparability.

---

## 4. Geometry cardinality falsification

The primary crossed geometry fixture uses:

```text
i: C_plus={a,b}
j: C_plus={a,c}
```

Both have:

\[
|\mathcal C_+(i)|=|\mathcal C_+(j)|=2,
\]

but neither set contains the other.

The native comparator returns:

```text
INCOMPARABLE
```

in `64/64` encodings.

The cardinality-only shortcut collapses the two records and is rejected in `64/64` encodings.

Thus:

\[
\boxed{
|\Delta\mathcal C_i|=|\Delta\mathcal C_j|
\not\Rightarrow
\Delta\mathcal C_i\equiv\Delta\mathcal C_j.
}
\]

---

## 5. Collateral mean falsification

The crossed collateral fixture uses:

```text
i = (+1/2,-1/2,0,0)
j = (0,0,0,0)
```

Both arithmetic means are zero, but the componentwise vectors cross.

Native relation:

```text
INCOMPARABLE
```

in `64/64` encodings.

Mean-collapse falsely emits equivalence and is rejected in `64/64` encodings.

---

## 6. Reopenability frequency falsification

The crossed reopenability fixture uses two eight-stress binary vectors with equal finite-panel frequency but different stresswise support.

Native relation:

```text
INCOMPARABLE
```

in `64/64` encodings.

Frequency-only comparison falsely emits equivalence and is rejected in `64/64` encodings.

Therefore:

\[
\boxed{
R_{\rm reopen}^{\rm frequency}(i)=R_{\rm reopen}^{\rm frequency}(j)
\not\Rightarrow
Y(i)=Y(j).
}
\]

---

## 7. Burden anti-scaffold comparison

The burden comparator uses the complete set of inclusion-minimal semantic obligation ledgers, not visible syntax.

A transparent one-token alias of an unchanged semantic obligation ledger remains:

```text
EQUIVALENT
```

under the native comparator.

The visible-token shortcut changes the relation and is rejected in `64/64` encodings.

Additional preregistered envelope controls also pass:

```text
all alternative ledgers robustly above reference -> I_GREATER
crossed alternative ledgers                       -> INCOMPARABLE
```

So packaging compactness cannot impersonate semantic burden reduction.

---

## 8. Scope remains license, not value

Every unsupported/disjoint-support `E` fixture returns:

```text
NO_LICENSED_COMPARISON
```

in `64/64` encodings for every comparator.

The scope-blind shortcut emits a false relation in:

```text
384 / 384
```

coordinate-encoding cases and is therefore completely falsified.

For `C_scope`, a favorable synthetic effect hint cannot override empty common support.

---

## 9. Missing-identification wrong control

Wrong control `W1` replaces `NOT_IDENTIFIED` with a zero-like native object.

Observed:

```text
typed missingness violations      384/384
false licensed/directed relations 320/384
```

The remaining 64 cases are direct scope records: replacing missing scope by an empty set still leaves the native comparator unlicensed, but the imputation itself violates the preregistered typed missingness rule.

Therefore `W1` is falsified without pretending that every invalid imputation must numerically reverse an output.

---

## 10. Wrong-control panel

```text
W1 NOT_IDENTIFIED -> zero      falsified
W2 scalarize native objects    falsified 320/320
W3 ignore common scope         falsified 384/384
W4 relation -> preference      falsified by type boundary
```

`W4` cannot execute inside the primary architecture because no `PREFER_I`, `PREFER_J`, winner, recommendation, or other preference-bearing output type exists.

---

## 11. Upstream regression boundary

The exact committed upstream result blobs are anchored as:

```text
candidate measurement results:
  dce4b66df142cfcb2a6515a082585f36ab374071

measurement-identification results:
  b23578f44742df8e484f2b60ebc708e472f4906d
```

Required inherited facts remain:

```text
candidate_count                         12
not_identified candidate-coordinate     12
upstream candidate comparison            false
upstream Q_extension                     false
M_ext architecture identified            true
measurement aggregation defined          false
```

The comparison calibration does not inspect actual candidate-pair values.

---

## 12. Anti-preference status

```text
actual candidate-pair relations computed   false
candidate preference defined               false
Pareto filtering performed                 false
cross-coordinate aggregation defined       false
Q_extension defined                        false
NO_WARRANTED_ADOPTION defined              false
authorization performed                    false
binding performed                          false
```

No Hudson/Rubi, synthesized, or control candidate receives a pairwise native relation in this execution.

---

## 13. Earned claim

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
- that any extension is better than another;
- Pareto dominance among candidates;
- any coordinate priority or tradeoff rate;
- any extension-value function;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- Hudson/Rubi superiority or inferiority;
- authorization;
- binding;
- post-adoption consequence.

The next scientific object is therefore **application of the frozen native comparators to the actual candidate records**, which remains undefined until separately preregistered.
