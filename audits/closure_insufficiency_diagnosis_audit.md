# Closure-Insufficiency Diagnosis Audit — Results

## Provenance

Preregistered before execution at:

```text
133ab57111d57afe2897df84e9202e73b1099b28
```

Gate-2 anchor:

```text
ee1b9ac  experiment-space construction discriminant
```

The new closure-diagnosis panel was executed freshly in-session against the preregistered logic. The committed executable imports the Gate-2 audit and recursively hard-asserts the Gate-1 / accessibility / valuation / navigation chain when run in-repo.

Correct provenance:

\[
\boxed{\textbf{fresh closure-insufficiency-diagnosis result with inherited hard regression assertions}.}
\]

No construction change, extension proposal, extension valuation, authorization, or binding is introduced.

---

## 1. Frozen diagnostic object

The audit tests only:

\[
\boxed{
E_{\rm failure}\rightarrow D_{\rm closure},
\qquad
D_{\rm closure}\in\{\texttt{SUFFICIENT},\texttt{INSUFFICIENT}\}.
}
\]

The admitted construction substrate remains exactly `S0`.

The complete current closure was recomputed from the four coordinate primitives plus XOR fixed-point closure:

```text
|C0| = 15
canonical checksum =
809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

No `S1`, `AND`, alternative grammar, candidate extension, or target-specific experiment is admitted.

---

## 2. Matched failure panel

Across every diagnostic episode:

```text
Bayes baseline accuracy    0.625
exact-target R_corr        0.375
exact-target q             0.275
exact target outside C0    yes
correction unresolved      yes
actor terminal action      COMMIT
```

Thus neither raw task failure nor exact-target absence can identify closure insufficiency.

### H family — closure sufficient

For each `h_i`, the exact nonlinear target is outside `C0`, but one admitted primitive partition has:

```text
best admitted R_corr = 0.250
best admitted q      = 0.150
q-maximal candidates = 1
all other C0 R_corr  = 0
```

Hence:

\[
\boxed{\exists e\in\mathcal C_0:q(e)>0}
\]

and the correct diagnosis is `SUFFICIENT`.

### G family — closure insufficient

For each `g_i`:

```text
max admitted C0 R_corr = 0.000
max admitted C0 q      = -0.100
```

Hence:

\[
\boxed{\forall e\in\mathcal C_0:q(e)\le0}
\]

and the correct diagnosis is `INSUFFICIENT`.

---

## 3. Primary result

Across 64 anonymous encodings × 12 failed-run contexts:

```text
SEARCH_MISS:
  correct SUFFICIENT        256 / 256
  failed actor COMMIT       256 / 256

VALUATION_MISHANDLE:
  correct SUFFICIENT        256 / 256
  failed actor COMMIT       256 / 256

CLOSURE_INSUFFICIENT:
  correct INSUFFICIENT      256 / 256
  failed actor COMMIT       256 / 256

TOTAL:
  diagnostic correctness    768 / 768
```

Therefore:

\[
\boxed{
\text{current closure failed to produce correction}
\neq
\text{current closure cannot produce correction}.
}
\]

The diagnostic succeeds by independently recomputing the complete admitted closure and evaluating closure-wide normative acquisition capacity under the frozen correction contract.

It does not infer from actor behavior.

---

## 4. Failure-locus controls

### Search miss

The failed actor omits the four primitive partitions. The unique worthwhile admitted refinement is therefore never evaluated.

Actor-observed normative capacity:

\[
\boxed{\max q=-0.1}
\]

while complete-closure normative capacity is:

\[
\boxed{\max q=+0.15.}
\]

Correct diagnosis remains `SUFFICIENT`.

### Valuation mishandling

The actor sees the complete closure but uses:

\[
\kappa_{\rm actor}=0.30
\]

rather than the frozen correct:

\[
\kappa=0.10.
\]

The useful admitted refinement has actor-side margin `-0.05`, so the actor commits, while the diagnostic recomputes the correct closure-wide margin `+0.15`.

Correct diagnosis remains `SUFFICIENT`.

### Genuine closure defect

The actor has complete access and correct valuation, but every current closure member has `q=-0.1`.

Correct diagnosis is `INSUFFICIENT`.

Thus:

\[
\boxed{
\text{search failure}
\neq
\text{valuation failure}
\neq
\text{closure insufficiency}.
}
\]

---

## 5. Restricted-information ceilings

The preregistered shortcut controls were exact.

| Representation | Best deterministic accuracy |
|---|---:|
| D0 failure-only | `512/768 = 2/3` |
| D1 actor-observed candidate capacity only | `512/768 = 2/3` |
| D2 exact-target membership in `C0` | `512/768 = 2/3` |
| naïve `target outside C0 -> INSUFFICIENT` | `256/768 = 1/3` |

D3, direct supplied `q_max`, can trivially be exact but is classified as oracle displacement and is not valid primary evidence.

The strongest diagnostic controls therefore establish:

\[
\boxed{\text{failure}\not\Rightarrow\text{closure insufficiency}}
\]

and:

\[
\boxed{
\Pi(y)\notin\mathcal C_0
\not\Rightarrow
\text{closure insufficiency}.
}
\]

Closure sufficiency is about the existence of a **next warranted corrective continuation**, not exact representation of the final target.

---

## 6. Earned claim

The strongest permitted claim is:

\[
\boxed{
\textbf{
In this finite audited regime, a system can diagnose whether the complete current experiment closure is insufficient for warranted continuation, while separating genuine closure impossibility from search and valuation failures, without being supplied the missing extension.
}
}
\]

Scope qualifications:

- `S0` is supplied and exhaustively enumerable;
- closure completeness is mechanically certifiable;
- the correction contract and acquisition burden are frozen;
- the diagnostic derives closure-wide consequence from lower-level evidence partitions;
- no extension is generated, valued, authorized, or bound.

Therefore:

\[
\boxed{
\text{closure diagnosis}
\neq
\text{extension discovery}.
}
\]

---

## 7. What remains unresolved

This audit does **not** establish:

- discovery of `S1` or any other extension;
- generation of candidate operators or grammars;
- extension valuation;
- authority to modify `S_construct`;
- binding of an extension;
- held-out verification after a self-selected construction change;
- unrestricted research agency.

The next empirical object, if pursued, is:

\[
\boxed{
D_{\rm closure}
\rightarrow
\widehat S_{\rm candidate}
}
\]

with extension discovery kept separate from valuation, authorization, and binding.