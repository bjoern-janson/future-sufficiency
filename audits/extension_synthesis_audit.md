# Extension Synthesis Audit — Results

## Provenance

Preregistered before execution at:

```text
fa4e744f44f0e61fe3e3a7c3bea8d2101c0f59b1
```

Closure-diagnosis anchor:

```text
7e3871c  closure-insufficiency diagnosis audit
```

The extension-synthesis panel was executed freshly in-session against the preregistered semantic search. The committed executable imports the closure-diagnosis audit and recursively hard-asserts Gate 2 / Gate 1 / accessibility / valuation / navigation when run in-repo. Those older audits were **not** freshly process-replayed in this connector session.

Correct provenance:

\[
\boxed{\textbf{fresh extension-synthesis result with inherited hard regression assertions}.}
\]

No candidate was valued against another candidate, authorized, bound, or tested in a post-binding episode.

---

## 1. Frozen endpoint

The audit tests only:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\rightarrow
M_0
\rightarrow
\widehat S_{\rm candidate}
}
\]

or:

\[
\boxed{\texttt{NO\_SUPPORTED\_CANDIDATE}.}
\]

Candidate adequacy is extensional:

\[
\operatorname{CanRestore}(s)=1
\iff
\max_{e\in\mathcal C(S\oplus s)}q(e)>0.
\]

No extension name is a success criterion.

---

## 2. Exhaustive `M0` construction space

The opaque two-input Boolean basis generated:

```text
raw syntax trees, <=3 internal N nodes: 102
distinct binary truth functions:        10
```

The supplied meta-substrate ledger is:

```text
B_truth_basis          = 1
B_pool_roles           = 2
B_program_combinators  = 3
B_grammar              = 3
B_search_bounds        = 3
B_semantic_hints       = 0
B_target_hints         = 0
------------------------------------------
expanded B_M0          = 12
```

No named extension menu or target-specific synthesis template was used.

After synthesized-operator semantic deduplication, the bounded program search contains:

| Class | raw syntax programs | bounded programs | distinct semantic closure fingerprints |
|---|---:|---:|---:|
| A | 207 | 23 | 4 |
| B | 207 | 23 | 4 |
| C | 417 | 49 | 5 |
| D | 207 | 23 | 4 |

The current closures reproduce the prior empirical anchors exactly:

```text
A/B current C0:
  size     15
  checksum 809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49

C current degree<=2 closure:
  size     1023
  checksum c51cc447000204a4c32e205d4e8daab954a52b80939664bbab2968629299efb7
```

---

## 3. A/B falsification point

Both A and B begin from the same complete linear closure:

```text
current family size = 15
current max R_corr  = 0
current max q       = -0.1
D_closure           = INSUFFICIENT
```

Exhaustive semantic candidate analysis did **not** collapse the repairs.

### Class A

Exactly one inclusion-minimal adequate semantic closure fingerprint survives:

```text
family size       = 120
new partitions    = 105
max R_corr        = 0.25
max q             = 0.15
fingerprint       = 8d3a5ecddbcf823c2ffca59f2490d2950caea216816b3c8e9af58bb2dfbb5dc1
```

Four syntactically/Boolean-semantically different synthesized functions map to this same repair-relevant closure fingerprint. They are therefore one semantic candidate class, not four repair claims.

### Class B

Exactly one different inclusion-minimal adequate semantic closure fingerprint survives:

```text
family size       = 50
new partitions    = 35
max R_corr        = 0.25
max q             = 0.15
fingerprint       = c5381b17c76e113f0927e55a929bc855b74b68f4a3a676bc4534944c1330d897
```

Thus across all anonymous encodings:

\[
\boxed{
\widehat{\mathfrak S}_A\neq\widehat{\mathfrak S}_B
\quad 64/64.
}
\]

The common 1,023-partition degree-2 expansion is adequate for both, but it is a strict semantic superset of smaller adequate candidates and is removed by the preregistered minimality rule.

Therefore:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\not\Rightarrow
\text{one fixed repair}.
}
\]

---

## 4. C — reuse/depth synthesis

Class C starts from the already-expanded complete degree-`<=2` experiment family:

```text
current family size = 1023
baseline accuracy   = 0.875
current max R_corr  = 0
current max q       = -0.1
D_closure           = INSUFFICIENT
```

The target admits at most `R_corr=0.125`, so any adequate candidate must recover an almost exact next distinction.

Exhaustive `BASE x BASE` candidate construction produced:

```text
adequate semantic closure fingerprints = 0
```

By contrast, two inclusion-minimal adequate semantic candidate classes survive when the program may use:

```text
CURRENT_NONLINEAR x BASE
```

Their fingerprints are:

| family size | added partitions | max R_corr | max q | checksum |
|---:|---:|---:|---:|---|
| 1,653 | 630 | 0.125 | 0.025 | `f5fc3cdd75661c1bdccc1efe88382e1669b481136ee14de2396009abc9330ad4` |
| 2,388 | 1,365 | 0.125 | 0.025 | `644e80b2a4e568b789dad11dbb2057c71d836bc52e1e0d68fb31e3aa1f62493f` |

Every minimal adequate C candidate therefore uses nonlinear-result reuse/depth.

Across 64 anonymous encodings:

```text
reuse/depth candidate-set synthesis  64/64
BASE x BASE-only repair success       0/64
```

This supports:

\[
\boxed{
\text{missing operator semantics}
\neq
\text{insufficient compositional depth/reuse}.
}
\]

---

## 5. D — warranted null synthesis

Class D hides one randomly selected primitive coordinate in a five-bit world. `M0` may compose only functions of the other four exposed coordinates.

Observed for every hidden-coordinate choice and every generated program:

```text
current max R_corr                = 0
candidate-space max R_corr        = 0
adequate M0 candidate classes     = 0
```

Yet direct evidence about the inaccessible coordinate, if available, would have:

```text
baseline accuracy       = 0.5
exact-target R_corr     = 0.5
exact-target q          = 0.4
```

Thus correction is potentially useful, but unsupported by the admitted meta-substrate.

Across 64 anonymous encodings:

\[
\boxed{
\texttt{NO\_SUPPORTED\_CANDIDATE}=64/64,
\qquad
\text{any supported }M_0\text{ repair}=0/64.
}
\]

This is positive epistemic behavior:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\not\Rightarrow
\text{expand anyway}.
}
\]

---

## 6. Aggregate synthesis result

Across 64 anonymous encodings x 4 synthesis classes:

```text
A adequate candidate-set synthesis       64/64
B distinct adequate candidate synthesis  64/64
C reuse/depth candidate synthesis        64/64
D NO_SUPPORTED_CANDIDATE                 64/64
------------------------------------------------
coarse synthesis outcome                256/256
```

Additional frozen checks:

```text
A/B semantic candidate sets differ       64/64
C BASE x BASE-only adequate               0/64
D any M0 repair supported                 0/64
candidate bindings performed                 0
extension-valued winner selections           0
authorization decisions                      0
```

---

## 7. Wrong-extension and shortcut controls

The generated candidate universe contains geometry-preserving candidates and space-expanding candidates that fail the active correction contract.

Observed:

```text
W1 geometry-preserving candidate: inadequate
W2 A wrong expanding candidate:    present
W2 B wrong expanding candidate:    present
W3 C BASE x BASE-only candidates:  all inadequate
W4 D all M0 candidates:            inadequate
```

Restricted controls remain:

\[
\boxed{\operatorname{Ceiling}(R0)=1/4}
\]

for a diagnosis-only fixed repair axis, and:

\[
\boxed{\operatorname{Ceiling}(R1)=3/4}
\]

for the reflex `INSUFFICIENT -> always emit some extension`.

Instantiating an actual A-minimal transformation as a fixed reflex gives:

```text
A  true
B  false
C  false
D  false
```

hence exact coarse accuracy `1/4`.

The anti-scaffold classifications remain frozen:

```text
named extension menu       -> selection only
opaque repair macro        -> hidden extension specification
target-specific template   -> oracle displacement
target-blind M0            -> valid primary substrate
```

---

## 8. Earned claim

The strongest permitted claim is:

\[
\boxed{
\textbf{
In these finite audited regimes, after diagnosing that the current experiment closure is insufficient, a system can synthesize non-oracular candidate construction-substrate transformations from a supplied target-blind lower-level meta-language, while withholding repair when that meta-language contains no supported candidate.
}
}
\]

This is:

\[
\boxed{\textbf{bounded extension synthesis relative to supplied }M_0.}
\]

It is not unrestricted extension invention.

It does **not** establish:

- discovery of `M0`;
- global minimality of `M0`;
- extension valuation;
- selection of the best adequate extension;
- authorization;
- binding;
- inheritance;
- held-out correction after a self-selected change;
- unrestricted research agency;
- general self-modification.

The next causal boundary remains:

\[
\boxed{
\widehat S_{\rm candidate}
\rightarrow
Q_{\rm extension}.
}
\]
