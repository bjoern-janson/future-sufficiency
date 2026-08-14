# Closure-Insufficiency Diagnosis Audit — Preregistration

## Status

This document freezes the next empirical gate **before execution**.

Parent dependency checkpoint:

```text
79e8d32  Update experiment-planning dependency consolidation after Gate-2 basin opening
```

Gate-2 empirical anchor:

```text
ee1b9ac  experiment-space construction discriminant
```

No empirical result is recorded here.

The Gate-2 result is treated as parked. The present audit does **not** change the experiment-construction substrate, does not expose `S1`, and does not introduce any candidate extension.

The governing boundary is:

\[
\boxed{
\text{closure diagnosis}
\neq
\text{extension discovery}.
}
\]

The only output of this audit is:

\[
\boxed{
D_{\rm closure}
\in
\{\texttt{SUFFICIENT},\texttt{INSUFFICIENT}\}.
}
\]

---

## 1. Scientific question

The narrow question is:

\[
\boxed{
\textbf{Can a system infer from admissible post-failure evidence whether the complete current experiment closure still contains a warranted corrective continuation?}
}
\]

The decisive distinction is:

\[
\boxed{
\text{current closure failed to produce correction}
\neq
\text{current closure cannot produce correction}.
}
\]

The intended evidence conjunction for `INSUFFICIENT` is:

\[
\boxed{
U=1
\land
\mathcal C_0\text{ exhaustively characterized}
\land
\max_{e\in\mathcal C_0}Q_{\rm acquire}(e)\le 0,
}
\]

where `U=1` means the correction remains unresolved.

The diagnostic must **not** infer closure insufficiency from task failure alone.

---

## 2. Domain of the binary diagnosis

This audit keeps the diagnostic object binary, but only on episodes for which closure completeness is certified relative to the currently admitted construction substrate.

Formally, the binary object is licensed only when:

1. the current construction substrate `S0` is known;
2. its closure is recomputed to a semantic fixed point;
3. every closure member can be evaluated under the frozen correction contract and anchored acquisition burden;
4. the current correction is unresolved.

Within that certified domain:

\[
\boxed{
D_{\rm closure}
=
\begin{cases}
\texttt{SUFFICIENT}, & \max_{e\in\mathcal C_0} q(e)>0,\\[4pt]
\texttt{INSUFFICIENT}, & \max_{e\in\mathcal C_0} q(e)\le0,
\end{cases}
}
\]

with:

\[
q(e)=R_{\rm corr}(e)-\kappa.
\]

This definition is about **availability of a warranted corrective continuation**, not exact representability of the final correction target.

No claim is made for episodes where closure completeness itself cannot be established.

---

## 3. Freeze the construction substrate

Hold the admitted experiment-construction substrate fixed at the exact Gate-1 / Gate-2 baseline `S0`:

### Primitive semantics

```text
p1(X)=x1
p2(X)=x2
p3(X)=x3
p4(X)=x4
```

### Admitted operator

\[
XOR(f,g)(w)=f(w)\oplus g(w).
\]

### Closure rule

```text
repeat XOR over currently admitted experiment semantics until no new evidence partition appears
```

### Generic constraints

1. discard the constant/zero experiment;
2. deduplicate by evidence-partition equivalence modulo output-token polarity.

The complete current closure must be recomputed in execution:

\[
\boxed{
\mathcal C_0=\operatorname{Closure}(S_0),
\qquad |\mathcal C_0|=15.
}
\]

The frozen Gate-1 checksum is:

```text
809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

No `AND`, `NOT`, `S1`, degree-2 macro, target-specific experiment, or alternative construction grammar is admitted anywhere in this audit.

Thus:

\[
\boxed{
do(S_{\rm construct})=\varnothing.}
\]

---

## 4. Freeze downstream semantics

Use the same uniform four-bit world:

\[
X=(x_1,x_2,x_3,x_4)\in\{0,1\}^4.
\]

Freeze:

\[
\boxed{\kappa=0.1.}
\]

For a correction target `y`, let:

\[
R_{\rm corr}(e\mid y)
=
\operatorname{BayesAcc}(y\mid e)
-
\operatorname{BayesAcc}(y).
\]

The diagnostic receives no precomputed relevance score, no precomputed `q_max`, and no closure-sufficiency label.

It must derive consequence from:

- the anonymous evidence partition induced by each closure member;
- the frozen correction contract;
- the anchored acquisition burden.

The strict-positive acquisition convention remains:

\[
q(e)>0
\iff
\text{warranted acquisition continuation}.
\]

---

## 5. Matched target panel

The panel is deliberately matched so that coarse task difficulty cannot separate `SUFFICIENT` from `INSUFFICIENT`.

Every target used below must satisfy:

```text
Bayes baseline accuracy      = 0.625
exact-target post accuracy   = 1.000
exact-target R_corr          = 0.375
exact-target q at kappa=.1   = 0.275
exact target partition       outside C0
observed failed run          unresolved
observed failed run          terminates at COMMIT
```

Thus exact-target membership, baseline difficulty, and the existence of a hypothetical useful out-of-closure experiment are intentionally matched.

### 5.1 Closure-sufficient target family `H`

Freeze four nonlinear correction targets:

\[
\begin{aligned}
h_1(X)&=x_1\land(x_2\lor x_3),\\
h_2(X)&=x_2\land(x_3\lor x_4),\\
h_3(X)&=x_3\land(x_4\lor x_1),\\
h_4(X)&=x_4\land(x_1\lor x_2).
\end{aligned}
\]

For each `h_i`, the exact target partition is outside `C0`, but there is a unique worthwhile admitted parity refinement:

```text
h1 -> e* = partition(x1)
h2 -> e* = partition(x2)
h3 -> e* = partition(x3)
h4 -> e* = partition(x4)
```

Execution must derive, not hard-code, the preregistered consequence profile:

```text
Bayes baseline                    0.625
best admitted post accuracy       0.875
best admitted R_corr              0.250
best admitted q                   0.150
number of q-maximal admitted e*       1
all other C0 R_corr               0.000
```

Therefore:

\[
\boxed{
\max_{e\in\mathcal C_0}q(e)=0.15>0
}
\]

and the correct closure diagnosis is:

\[
\boxed{D_{\rm closure}=\texttt{SUFFICIENT}.}
\]

Note the intended semantics:

\[
\boxed{
\Pi(y)\notin\mathcal C_0
\not\Rightarrow
D_{\rm closure}=\texttt{INSUFFICIENT}.
}
\]

A closure can be sufficient for the **next warranted corrective continuation** without containing the exact final target partition.

### 5.2 Closure-insufficient target family `G`

Freeze four matched nonlinear targets:

\[
\begin{aligned}
g_1(X)&=(x_1\land x_2)\oplus(x_3\land x_4),\\
g_2(X)&=((1-x_1)\land x_2)\oplus(x_3\land x_4),\\
g_3(X)&=(x_1\land(1-x_2))\oplus(x_3\land x_4),\\
g_4(X)&=((1-x_1)\land(1-x_2))\oplus(x_3\land x_4).
\end{aligned}
\]

Execution must derive the preregistered consequence profile:

```text
Bayes baseline                    0.625
exact-target R_corr              0.375
max admitted C0 R_corr           0.000
max admitted C0 q               -0.100
```

Therefore:

\[
\boxed{
\max_{e\in\mathcal C_0}q(e)=-0.1\le0
}
\]

and the correct diagnosis is:

\[
\boxed{D_{\rm closure}=\texttt{INSUFFICIENT}.}
\]

---

## 6. Three failure worlds

For each anonymous encoding, evaluate 12 failed-run contexts:

```text
4 SEARCH_MISS contexts          using h1...h4
4 VALUATION_MISHANDLE contexts  using h1...h4
4 CLOSURE_INSUFFICIENT contexts using g1...g4
```

Across 64 encodings:

\[
\boxed{64\times12=768\text{ diagnostic episodes}.}
\]

All 768 episodes end with:

```text
correction unresolved = true
actor terminal action = COMMIT
```

The observed task failure is therefore non-diagnostic by itself.

### 6.1 World A — search misses a worthwhile admitted refinement

Use an `h_i` correction target.

The acting search policy is deliberately incomplete: it evaluates only non-primitive parity experiments and never evaluates the four primitive partitions.

For each `h_i`, the unique worthwhile admitted refinement `e*` is one of those omitted primitive partitions.

Therefore the failed actor observes no positive-margin candidate and commits, even though:

\[
\boxed{e^\star\in\mathcal C_0\quad\land\quad q(e^\star)=0.15>0.}
\]

Correct diagnosis:

\[
\boxed{\texttt{SUFFICIENT}.}
\]

This is a search/utilization failure inside a sufficient closure.

### 6.2 World B — valuation mishandles a worthwhile admitted refinement

Use the same `h_i` correction targets.

The acting policy has complete access to `C0`, but uses a deliberately corrupted actor-side acquisition burden:

\[
\kappa_{\rm actor}=0.30.
\]

For the true useful admitted refinement:

\[
R_{\rm corr}=0.25,
\qquad
q_{\rm actor}=0.25-0.30=-0.05,
\]

so the failed actor commits.

The diagnostic, however, recomputes closure capacity under the **frozen correct contract**:

\[
\kappa=0.10,
\qquad
q(e^\star)=0.15>0.
\]

Correct diagnosis:

\[
\boxed{\texttt{SUFFICIENT}.}
\]

This is a valuation failure inside a sufficient closure.

### 6.3 World C — complete closure cannot support warranted continuation

Use a `g_i` correction target.

The acting policy has complete access to `C0` and uses the correct frozen burden.

Every admitted experiment has:

\[
R_{\rm corr}=0,
\qquad
q=-0.1,
\]

so COMMIT is warranted under the current closure.

The correction nevertheless remains unresolved and the exact target experiment, if it existed, would be worthwhile.

Correct diagnosis:

\[
\boxed{\texttt{INSUFFICIENT}.}
\]

This is the genuine closure-defect case.

---

## 7. Primary diagnostic controller

The primary controller receives no failure-locus label and no extension proposal.

For each failed episode it must:

1. recompute `C0` from the anonymous `S0` substrate;
2. verify semantic fixed-point closure;
3. evaluate every `e in C0` against the anonymous correction contract;
4. derive `R_corr(e)`;
5. derive `q(e)=R_corr(e)-0.1`;
6. compute whether any current closure member has strict-positive acquisition worth;
7. emit only `SUFFICIENT` or `INSUFFICIENT`.

Preregistered rule:

\[
\boxed{
D_{\rm closure}
=
\begin{cases}
\texttt{SUFFICIENT},&\exists e\in\mathcal C_0:q(e)>0,\\
\texttt{INSUFFICIENT},&\forall e\in\mathcal C_0:q(e)\le0.
\end{cases}
}
\]

No `q_max` scalar is externally supplied; it is a derived runtime object.

### Primary target

Across 64 anonymous encodings:

```text
SEARCH_MISS:          256 / 256 SUFFICIENT
VALUATION_MISHANDLE:  256 / 256 SUFFICIENT
CLOSURE_INSUFFICIENT: 256 / 256 INSUFFICIENT
-------------------------------------------
TOTAL:                768 / 768 correct
```

If achieved, this supports **closure-insufficiency diagnosis relative to an exhaustively enumerable supplied construction substrate and frozen correction contract**.

---

## 8. Restricted-information controls

These controls distinguish genuine closure-capacity diagnosis from shallow failure heuristics.

### D0 — failure-only

Expose only:

```text
correction unresolved = true
actor terminal action = COMMIT
```

These fields are identical across all three failure worlds.

With 8 `SUFFICIENT` and 4 `INSUFFICIENT` contexts per encoding, the best deterministic binary classifier from this representation has ceiling:

\[
\boxed{\operatorname{Ceiling}(D0)=\frac{8}{12}=\frac23.}
\]

Thus:

\[
\boxed{\text{failure}\not\Rightarrow\text{closure insufficiency}.}
\]

### D1 — actor-observed candidate capacity only

Recompute normative consequence only over the candidates the failed actor actually evaluated, not over the complete closure.

Expected representation:

```text
SEARCH_MISS:          observed max q = -0.10
VALUATION_MISHANDLE:  observed full-closure normative max q = +0.15
CLOSURE_INSUFFICIENT: observed max q = -0.10
```

`SEARCH_MISS` and `CLOSURE_INSUFFICIENT` therefore collide exactly under this representation.

The best deterministic ceiling is:

\[
\boxed{\operatorname{Ceiling}(D1)=\frac23.}
\]

This tests the necessity of **independent exhaustive closure characterization** for separating search failure from closure impossibility.

### D2 — exact-target membership in `C0`

Ask only whether the exact correction-target partition is already a member of `C0`.

By preregistration, every `h_i` and every `g_i` exact target is outside `C0`.

Therefore this representation is constant across all 12 contexts and has ceiling:

\[
\boxed{\operatorname{Ceiling}(D2)=\frac23.}
\]

The naïve rule:

```text
exact target outside C0 -> INSUFFICIENT
```

would score only:

\[
\boxed{\frac{4}{12}=\frac13.}
\]

This protects the intended notion of closure sufficiency:

\[
\boxed{
\text{exact target representability}
\neq
\text{availability of a warranted corrective continuation}.
}
\]

### D3 — supplied `q_max` oracle

A controller directly supplied with the correct closure-wide `q_max` scalar could trivially implement the desired diagnosis.

That is **not** accepted as the primary result because it relocates the evaluator into the diagnostic interface.

The valid primary controller must derive the closure-wide comparison from lower-level partition consequences and burden.

---

## 9. Anti-oracle / anti-leakage rules

The diagnostic input must never contain:

- `search_miss`, `valuation_error`, `closure_error`, or equivalent failure-locus labels;
- `SUFFICIENT` / `INSUFFICIENT` hints;
- the identity of `e*`;
- a direct target-in-closure flag;
- a precomputed `R_corr` lookup table;
- a precomputed `q_max` field;
- an `AND` operator;
- `S1`;
- a menu of candidate construction extensions;
- a target-specific novel experiment;
- an extension winner label.

The correction contract itself is supplied, because without a correction contract there is no well-defined notion of correction relevance. Its public context identifier and action-token polarity must be anonymous.

---

## 10. Anonymous encoding requirements

Run at least 64 anonymous encodings.

For each encoding:

- permute the four primitive coordinate handles;
- permute world-state labels consistently;
- independently flip output tokens of every experiment partition;
- permute closure-member handles and enumeration order;
- permute correction-context identifiers;
- independently flip the binary terminal-action token labels per context;
- never expose target formulas, coordinate names, `primitive`, `composite`, `useful`, `novel`, `sufficient`, or `insufficient` to the diagnostic controller;
- evaluate experiment equality only by canonical evidence partition modulo polarity.

The acting search-control policy may internally use generation depth to omit depth-0 candidates, but this internal cause label is not passed to the diagnostic controller.

The diagnostic result must be invariant to all public renamings.

---

## 11. Matched-statistics certificate

Execution must report and assert for every target context:

```text
Bayes baseline accuracy    0.625
exact-target R_corr        0.375
exact-target q             0.275
exact target outside C0    true
failed run unresolved      true
failed actor action        COMMIT
```

This prevents the diagnosis from being attributed to trivial differences in baseline task difficulty, exact-target usefulness, or whether the task failure visibly persists.

For `H` contexts, execution must additionally derive:

```text
unique admitted worthwhile refinement count = 1
closure max R_corr                      = 0.250
closure max q                           = 0.150
```

For `G` contexts:

```text
admitted worthwhile refinement count    = 0
closure max R_corr                      = 0.000
closure max q                          = -0.100
```

---

## 12. Primary endpoints

Execution must report:

1. recomputed `C0` size and checksum;
2. fixed-point closure certificate;
3. matched task-level statistics for all `H` and `G` targets;
4. exact-target membership in `C0`;
5. full closure consequence profile per context;
6. full closure `q` profile per context;
7. number of strict-positive worthwhile closure members;
8. primary `D_closure` output;
9. diagnostic accuracy by failure world;
10. D0/D1/D2 collision-derived ceilings;
11. anonymous-encoding invariance;
12. absence of extension artifacts or target-specific construction hints;
13. upstream Gate-2 / Gate-1 hard-regression status.

A successful terminal label alone is insufficient.

---

## 13. Upstream regression boundary

The executable child audit must import and hard-assert the Gate-2 certificate from `ee1b9ac`:

```text
old C0 size                    15
old C0 checksum                809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
G20 exact target reachability  0/256
G20 COMMIT                     256/256
G21 C1 size                    1023
G21 exact target reachability  256/256
G21 exact target choice        256/256
G22 geometry unchanged         true
G22 exact target choice        0/256
G23 exact target choice        192/256
G23 ceiling exceeded           false
G24 target-specific displacement true
G25 opaque hidden specification   invalid
```

The inherited Gate-1 / accessibility / valuation / navigation assertions must remain recursively wired.

If an upstream certificate changes, reject closure-diagnosis attribution.

As in recent connector executions, the new diagnosis panel may be freshly executed while older audits remain inherited hard assertions unless a genuine repository-process replay occurs.

---

## 14. Frozen interpretation table

| Result | Interpretation |
|---|---|
| primary diagnosis = 768/768 | closure sufficiency can be diagnosed from exhaustive current-closure consequence structure in this finite regime |
| SEARCH_MISS -> SUFFICIENT | task failure did not trigger false closure reopening when current search omitted a worthwhile admitted refinement |
| VALUATION_MISHANDLE -> SUFFICIENT | task failure did not trigger false closure reopening when current valuation mishandled a worthwhile admitted refinement |
| CLOSURE_INSUFFICIENT -> INSUFFICIENT | complete closure incapacity was localized correctly |
| D0 reaches only collision ceiling | unresolved failure alone is insufficient |
| D1 reaches only collision ceiling | actor-observed search support is insufficient to distinguish search miss from closure impossibility |
| D2 reaches only collision ceiling | exact-target membership is not the correct criterion for warranted-continuation sufficiency |
| primary requires supplied `q_max` | reject as oracle displacement; lower-level derivation failed |
| any `S1` / extension proposal appears | reject audit scope; diagnosis contaminated by discovery |
| upstream regression changes | causal attribution invalid |

---

## 15. Candidate claim if the preregistered result holds

If the full diagnostic is exact across all anonymous encodings and the restricted representations obey their collision ceilings, the strongest permitted claim is:

\[
\boxed{
\textbf{In this finite audited regime, a controller can distinguish failure inside a still-sufficient experiment closure from failure caused by closure insufficiency by exhaustively deriving the current closure's correction-relevant acquisition capacity.}
}
\]

A complementary negative result is:

\[
\boxed{
\textbf{Observed failure, observed-search failure, and exact-target non-membership are each insufficient evidence for closure insufficiency.}
}
\]

This establishes closure diagnosis only relative to:

- a finite enumerable current construction substrate;
- an available correction contract;
- an anchored acquisition burden;
- exhaustive semantic evaluation of the current closure.

It does **not** establish:

- extension discovery;
- candidate operator generation;
- extension valuation;
- authorization;
- binding;
- autonomous experiment-space repair;
- unrestricted research agency;
- a general solution to closure diagnosis under open or unenumerable construction spaces.

---

## 16. Next boundary if this audit succeeds

The output of this audit stops at:

\[
\boxed{
E_{\rm failure}
\rightarrow
D_{\rm closure}.
}
\]

No construction transformation follows.

Only after this diagnosis is empirically established may the next gate ask:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\rightarrow
\widehat S_{\rm candidate}.
}
\]

That later gate is **extension discovery**, and must distinguish discovering a useful construction extension from being handed the correct extension.

The emerging sequence is therefore:

\[
\boxed{
\text{closure}
\rightarrow
\boxed{\text{closure diagnosis [preregistered]}}
\rightarrow
\text{extension discovery}
\rightarrow
\text{extension valuation}
\rightarrow
\text{authorization}
\rightarrow
\text{binding}
\rightarrow
\text{held-out correction}.
}
\]

No `P_ep` ledger update and no extension-discovery artifact is authorized until the present diagnosis result exists.
