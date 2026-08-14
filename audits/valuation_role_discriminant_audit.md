# Valuation-Role Discriminant Audit — Results

## Provenance

Preregistered before execution at:

```text
dec7d9efe868437ebda136a082ce0e829c8eb9de
```

Parent dependency checkpoint:

```text
cb9afb6a84d3ceec620e9cb2e33ab6d19888ad81
```

No broader dependency ledger is updated by this result file.

The valuation panel was executed in-session against the preregistered logic. The STOP/navigation regression comes from the unchanged deterministic audit at `4694382`; the executable valuation audit imports and reasserts that certificate when run in-repo. This session does not claim a fresh repository-process execution of the old STOP audit.

---

## 1. Frozen question

The audit tests whether the separate cardinal representation

\[
(V,C)
\]

is necessary for the observed acquisition decisions, while preserving the functional separation:

\[
\boxed{
I(e)\neq R_{\rm corr}(e)\neq Q_{\rm acquire}(e).
}
\]

The valuation geometry is identical across compared controllers. Sequential refinement and termination roles are not modified.

---

## 2. Evaluator-side panel

The preregistered five-case panel produced exactly the expected quantities:

| Case | Information bits | Correction relevance | Cost | `V R_corr - C` | `kappa=C/V` | Warranted action |
|---|---:|---:|---:|---:|---:|---|
| A | 3.0 | 0.25 | 1.0 | +1.5 | 0.1 | ACQUIRE |
| B | 3.0 | 0.00 | 1.0 | -1.0 | 0.1 | COMMIT |
| C | 1.0 | 0.25 | 1.0 | +1.5 | 0.1 | ACQUIRE |
| D | 3.0 | 0.25 | 3.0 | -0.5 | 0.3 | COMMIT |
| B+ | 4.0 | 0.00 | 1.0 | -1.0 | 0.1 | COMMIT |

Thus the core signature is:

\[
\boxed{(A,B,C,D,B+)=(1,0,1,0,0).}
\]

---

## 3. Primary substitution result

The scale-free controller replaces:

\[
\boxed{(V,C)\rightarrow\kappa=C/V}
\]

and decides only by:

\[
R_{\rm corr}(e)>\kappa(e).
\]

Across all 64 anonymous encodings:

```text
valuation decisions checked:       320
baseline decision mismatches:         0
scale-free decision mismatches:       0
baseline vs scale-free mismatches:    0
```

Therefore the separate literal `V,C` representation is not necessary for this panel's observed acquisition decisions.

The earned contraction is representational:

\[
\boxed{
V,C\text{ separately represented}
\;
\notin
\text{necessary implementation for this behavior}
}
\]

while the surviving role remains:

\[
\boxed{
Q_{\rm acquire}\text{-like acquisition ordering / threshold comparison}.
}
\]

This is **not** evidence that valuation disappeared.

---

## 4. Negative controls localize the surviving role

### Information-only

The information-only rule acquires every probe:

\[
(1,1,1,1,1).
\]

It therefore incorrectly acquires:

```text
B   high-information but correction-irrelevant
B+  even-more-informative but correction-irrelevant
D   correction-relevant but too costly
```

The B/B+ failures establish the intended local contrast:

\[
\boxed{
\text{raw information gain cannot substitute for correction relevance.}
}
\]

### Correction-relevance-only

The relevance-only rule produces:

\[
(1,0,1,1,0)
\]

and fails only on D.

Thus:

\[
\boxed{
\text{correction relevance cannot substitute for acquisition worth.}
}
\]

The panel therefore realizes the preregistered decomposition:

\[
\boxed{
I
\rightarrow
R_{\rm corr}
\rightarrow
Q_{\rm acquire}
}
\]

as a finite behavioral non-substitutability result, not as a universal ontology.

---

## 5. Feature-collision certificate

The best deterministic acquisition classification accuracy from restricted signatures is:

| Available signature | Best possible accuracy |
|---|---:|
| `I` | 0.80 |
| `R_corr` | 0.80 |
| `(I,C)` | 0.80 |
| `(I,R_corr)` | 0.80 |
| `I/C` | 0.60 |
| `(R_corr,C)` | **1.00** |

The key exact collisions are therefore structural, not optimizer failures:

\[
I(A)=I(B),\;C(A)=C(B),\;\text{but opposite actions};
\]

and:

\[
I(A)=I(D),\;R_{\rm corr}(A)=R_{\rm corr}(D),\;\text{but opposite actions}.
\]

So neither information plus cost nor information plus correction relevance is sufficient for the acquisition contract on this panel.

---

## 6. Specification-burden accounting

The anti-scaffold rule remains mandatory:

\[
\boxed{\text{behavioral substitution}\neq\text{substrate reduction}.}
\]

A finite supplied-field ledger gives:

| Representation | Global numeric fields | Per-case numeric fields | Direct decision fields | Interpretation |
|---|---:|---:|---:|---|
| baseline `V,C` | 1 | 5 | 0 | global value scale plus absolute costs |
| `kappa` | 0 | 5 | 0 | normalized acquisition thresholds; removes absolute scale |
| order table | 0 | 0 | 5 | directly stores answers; oracle displacement |

The `kappa` substitution removes the separate absolute value scale, but it does not remove the per-case acquisition threshold information.

Therefore the result supports a **representation contraction**, not a complete minimal-substrate certificate.

An order table would preserve behavior but is explicitly rejected as evidence of substrate reduction because it stores the target acquisition decisions directly.

---

## 7. Frozen-role regression boundary

The executable audit imports `stop_substitution_audit.audit()` and requires the already-earned certificate:

```text
64 anonymous encodings
3584 visited decision points
1536 derived terminations
0 normalized trace mismatches
```

The source audit is unchanged from:

```text
46943821f9dec0ed188410c5c22fcad0f21b5786
```

Any future run in which those assertions fail invalidates valuation-only attribution.

---

## 8. Earned result

Within this finite deterministic valuation panel:

\[
\boxed{
\textbf{raw information, correction relevance, and acquisition worth are behaviorally non-substitutable.}
}
\]

And:

\[
\boxed{
\textbf{the separate cardinal }V,C\textbf{ representation is not necessary for the observed acquisition decisions; the normalized }\kappa=C/V\textbf{ representation preserves them.}
}
\]

The stronger conclusion is not earned:

\[
\boxed{Q_{\rm acquire,min}\;?}
\]

remains open.

Likewise, the result does not establish that cost, correction relevance, or valuation ordering itself can be removed.

---

## 9. Interpretation for the dependency program

The audit contracts the implementation from:

\[
\text{absolute }V + \text{absolute }C
\]

to:

\[
\boxed{\text{normalized acquisition threshold / ordering}.}
\]

while preserving the functional distinction:

\[
\boxed{
\text{informative}
\neq
\text{correction-relevant}
\neq
\text{worth acquiring}.
}
\]

No experiment-accessibility or experiment-space-construction claim follows from this audit.
