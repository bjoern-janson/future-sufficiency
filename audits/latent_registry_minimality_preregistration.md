# Latent-Registry Minimality Audit — Preregistration

## Status

This document freezes the next experiment-planning dependency cut **before execution**.

Parent dependency checkpoint:

```text
0af61e5  Update experiment-planning dependency consolidation after accessibility contraction
```

Empirical accessibility anchor:

```text
6355333  accessibility contraction audit
```

No empirical results are recorded here.

The accessibility phase is treated as parked. The present audit targets only the remaining externally supplied latent experiment specification:

\[
\boxed{B_{\mathcal E^\star}.}
\]

The governing distinction is:

\[
\boxed{
\text{registry compression}
\neq
\text{registry expansion}.
}
\]

This audit is **Gate 1 only**:

\[
\boxed{
\mathcal E^\star_{\rm explicit}
\rightarrow
\mathcal E^\star_{\rm derived}
}
\]

with the useful experiment family held extensionally fixed.

It is **not** Gate 2:

\[
\mathcal E_t^\star\subsetneq\mathcal E_{t+1}^\star.
\]

No experiment-space expansion, basin-opening claim, or novel experiment construction is permitted in this audit.

---

## 1. Scientific question

The narrow question is:

\[
\boxed{
\textbf{How little designer-supplied latent-registry structure is required to recover the same already-defined useful experiment family?}
}
\]

The decisive success condition is:

\[
\boxed{
B_{\mathcal E^\star}\downarrow
\quad\land\quad
\operatorname{Recover}(\mathcal E^\star_{\rm useful})=1
}
\]

while preserving:

- the same evidence partitions;
- the same experiment family extensionally;
- the same generic access rule earned at `6355333`;
- the same correction contract;
- the same valuation and termination roles;
- the same downstream choices.

A smaller syntax alone is insufficient:

\[
\boxed{
\text{compressed syntax}
\not\Rightarrow
\text{compressed specification}.
}
\]

---

## 2. Frozen downstream structure

Hold fixed across every registry representation:

\[
\boxed{
A_{\rm access},\;
\mathfrak R_E,\;
S_{\rm refine},\;
Q_{\rm acquire}^{\rm role},\;
T_{\rm stop},\;
\Pi_{\mathcal P},\;
\tau.
}
\]

In particular:

- `A_access` is the target-blind `ALL_REGISTRY` exposure rule earned by the accessibility-contraction audit;
- the correction contract is unchanged;
- every emitted experiment receives the same anchored burden as in the accessibility audit;
- downstream experiment valuation remains contract-derived corrective consequence against COMMIT-anchored quantitative burden;
- no stronger planner, target-specific selector, semantic hint, or winner lookup may be introduced.

The only intervention is the representation from which the latent registry is recovered.

---

## 3. Freeze the extensional target family

Reuse the exact 15-probe parity family from `6355333`.

Let:

\[
X=(x_1,x_2,x_3,x_4)\in\{0,1\}^4.
\]

The target latent experiment universe is:

\[
\boxed{
\mathcal E^\star
=
\{e_m:m\in\{0,1\}^4\setminus\{0000\}\},
\qquad
|\mathcal E^\star|=15,
}
\]

where:

\[
\boxed{
e_m(X)=m\cdot X\pmod 2.}
\]

The extensional target is the set of **evidence partitions**, not human-readable mask names.

Two binary experiments are treated as semantically equivalent when they induce the same partition of the 16 worlds, allowing output-token polarity reversal.

Every valid representation must therefore be scored against the same partition set:

\[
\boxed{
\Pi(\mathcal E^\star)=\{\Pi(e_m):m\neq0000\}.
}
\]

Gate 1 succeeds only if the derived representation recovers exactly this set and does not add a new useful evidence partition.

---

## 4. Registry-specification ledger

The finite supplied-structure ledger is:

\[
\boxed{
B_{\mathcal E^\star}
=
B_{\rm primitives}
+B_{\rm operators}
+B_{\rm grammar}
+B_{\rm semantic\ labels}
+B_{\rm generation\ constraints}
+B_{\rm target\ hints}.
}
\]

These are **audited structural clauses**, not universal bits, MDL, or Kolmogorov complexity.

Each execution must report both:

1. the visible clause vector;
2. the **expanded specification ledger**, where opaque macros are unfolded to the semantic obligations they encode.

This second ledger is mandatory because:

\[
\boxed{
\text{one opaque macro token}
\not\Rightarrow
\text{one unit of specification burden}.
}
\]

A valid contraction requires a lower expanded burden than the explicit-registry reference.

---

## 5. R0 reference — explicit registry

The reference directly supplies the 15 target experiment semantics.

Operationally, R0 contains one semantic binding for each latent experiment partition.

Finite ledger:

```text
B_primitives             = 0
B_operators              = 0
B_grammar                = 0
B_semantic_labels        = 15   # one explicit experiment-semantic binding per target partition
B_generation_constraints = 0
B_target_hints           = 0
--------------------------------
B_E* clauses             = 15
```

Expanded burden is also 15.

R0 must recover:

\[
\boxed{15/15}
\]

target partitions and preserve all 960 accessibility-context choices from `6355333`.

R0 is a behavioral reference, not a presumed minimum.

---

## 6. R1 primary substitution — basis + reusable XOR closure

Replace the 15 explicit experiment-semantic bindings with a smaller target-blind generative substrate.

### Supplied primitives

Supply only the four coordinate evidence primitives:

```text
p1(X) = x1
p2(X) = x2
p3(X) = x3
p4(X) = x4
```

Their public identities are opaque under anonymous encodings.

### Supplied operator

Supply one reusable binary evidence-composition operator:

\[
\boxed{
XOR(f,g)(w)=f(w)\oplus g(w).
}
\]

The operator is supplied as a generic semantic operation over binary experiment outputs. It receives no correction context and no target information.

### Supplied grammar

Supply one closure rule:

```text
repeat XOR over the currently available experiment semantics until no new partition appears
```

### Generation constraints

Supply two generic constraints:

1. discard the constant/zero partition;
2. deduplicate experiments by evidence-partition equivalence.

No mask names, parity-family labels, target masks, context-to-experiment mappings, or desired-registry table are supplied.

Finite ledger:

```text
B_primitives             = 4
B_operators              = 1
B_grammar                = 1
B_semantic_labels        = 0
B_generation_constraints = 2
B_target_hints           = 0
--------------------------------
B_E* clauses             = 8
```

The expanded burden is also preregistered as 8 because every clause is explicit and no opaque family macro is allowed.

### Preregistered target

The algebraic closure of the four coordinate primitives under XOR should recover exactly the 15 nonzero linear parity partitions:

\[
\boxed{
\operatorname{Precision}_{R1}=1,
\qquad
\operatorname{Recall}_{R1}=1.
}
\]

Equivalently:

\[
\boxed{
\Pi(\mathcal E_{R1})
=
\Pi(\mathcal E^\star).
}
\]

Across the 64 anonymous encodings × 15 correction contexts:

\[
\boxed{960/960}
\]

downstream choices should match R0.

If this holds, the strongest permitted claim is:

\[
\boxed{
\textbf{In this finite audited regime, the 15 explicit latent experiment-semantic bindings are not necessary; the same extensional experiment registry can be recovered from a smaller target-blind compositional substrate.}
}
\]

This is registry-specification contraction only.

It does **not** establish experiment invention because the primitive set, XOR operator, closure grammar, and target extensional family are all fixed before execution.

---

## 7. R2 negative control — primitives only

Remove the XOR operator and closure grammar.

Retain only the four coordinate primitives.

Ledger:

```text
B_primitives             = 4
B_operators              = 0
B_grammar                = 0
B_semantic_labels        = 0
B_generation_constraints = 0
B_target_hints           = 0
--------------------------------
B_E* clauses             = 4
```

The recovered experiment family should contain only four of the 15 target partitions:

\[
\boxed{
\operatorname{Recall}_{R2}=\frac4{15}.
}
\]

Because the 15 correction contexts are evaluated uniformly, the downstream exact-choice ceiling is:

\[
\boxed{
\frac4{15}
=
\frac{256}{960}.
}
\]

This localizes the need for some composition mechanism rather than merely the latent existence of the four coordinates.

---

## 8. R3 negative control — one XOR layer only

Supply the same four primitives and XOR operator, but forbid recursive closure.

Allow only:

- the four primitive probes;
- one XOR of two distinct primitives.

This recovers:

\[
4+\binom42=10
\]

of the 15 target partitions.

It cannot recover the four three-way parities or the one four-way parity.

Preregistered recall:

\[
\boxed{
\operatorname{Recall}_{R3}=\frac{10}{15}.
}
\]

Preregistered downstream exact-choice ceiling:

\[
\boxed{
\frac{10}{15}
=
\frac{640}{960}.
}
\]

This distinguishes:

\[
\boxed{
\text{operator availability}
\neq
\text{compositional closure sufficient to recover the registry}.
}
\]

R3 must not exceed its extensional coverage ceiling.

---

## 9. R4 anti-scaffold control — opaque family macro

Provide a superficially tiny command:

```text
ALL_PARITIES_4
```

that emits the 15 target experiments.

The visible syntax contains one token, but unless the macro is implemented through the explicit R1 primitives/operator/grammar, the macro hides the complete family definition.

Therefore the audit must expand its burden.

If `ALL_PARITIES_4` is a direct family-specific macro, its expanded ledger is preregistered as carrying at least the 15 target semantic obligations:

```text
visible clauses            = 1
expanded semantic burden  >= 15
valid registry contraction = no
```

Behavioral success from this control earns nothing.

The rule is:

\[
\boxed{
\text{registry removed from syntax}
\neq
\text{registry removed from substrate}.
}
\]

If the macro is instead transparently implemented only by the R1 lower-level substrate, it is merely an alias for R1 and receives R1's expanded burden, not one unit.

---

## 10. R5 anti-oracle control — context-to-experiment generator

Allow a context-conditioned rule that emits the experiment known to match the correction context.

Operationally:

```text
TARGET_EXPERIMENT(context) -> matching latent experiment
```

This may reproduce all 960 downstream decisions without maintaining the full registry explicitly.

But it requires one target-specific mapping per correction context and therefore carries:

```text
B_target_hints = 15
```

and fails the registry-recovery endpoint because it does not recover the same context-independent latent experiment universe as a target-blind object.

It is preregistered as:

\[
\boxed{\text{oracle displacement}.}
\]

No minimality claim follows from behavioral success.

---

## 11. Why R1 is still not experiment invention

R1 may look generative because it composes primitives.

That does **not** make it Gate 2.

The scientific object remains the same fixed extensional target family:

\[
\boxed{
\Pi(\mathcal E_{R1})
=
\Pi(\mathcal E^\star).
}
\]

No target experiment outside the preregistered family is required, rewarded, or treated as a new capability.

The supplied XOR grammar is evaluated only as a possible **compression of the old registry specification**.

Thus:

\[
\boxed{
\text{derived old experiment}
\neq
\text{new experiment-space construction}.
}
\]

The later Gate 2 requires an intervention in which a useful refinement is not recoverable under the old admitted experiment substrate and becomes recoverable only after the experiment-space machinery itself changes.

That is outside this audit.

---

## 12. Anonymous encoding requirements

Run at least 64 anonymous encodings.

For each encoding:

- permute the four primitive coordinate handles;
- permute world-state labels consistently;
- independently flip binary output tokens of primitive and generated experiments;
- permute latent experiment handles;
- permute correction-context identifiers;
- evaluate semantic equality by induced evidence partition, not by public names;
- never expose masks, parity-family labels, target masks, `relevant`, `best`, or equivalent semantic hints.

The R1 derivation must remain exact under all renamings.

---

## 13. Registry recovery endpoints

For each registry representation report:

1. recovered target partitions;
2. missing target partitions;
3. extra partitions not in the fixed target family;
4. partition-level precision;
5. partition-level recall;
6. exact extensional equality with \(\mathcal E^\star\);
7. downstream choice agreement under frozen `ALL_REGISTRY` accessibility;
8. candidate-identity invariance;
9. visible burden vector;
10. expanded burden vector;
11. target-hint count;
12. whether the representation changes the admitted experiment family.

A terminal choice score alone is insufficient.

---

## 14. Frozen semantic checksum / identity requirement

The execution must reuse the same target parity partitions as `6355333` and report a canonical semantic checksum.

The checksum is over the sorted canonical partition representations, not over human-readable probe names.

R0 and R1 must have identical target-family checksums.

If R1 changes the target-family checksum by adding or removing a useful partition, the registry-compression attribution fails.

---

## 15. Upstream regression boundary

The executable child audit must hard-assert the accessibility-contraction certificate from `6355333`:

```text
A0 explicit menu:
  target reachability 960/960
  choice agreement    960/960

A1 ALL_REGISTRY:
  target reachability 960/960
  choice agreement    960/960
  B_access            1

A2 no access:
  target reachability 0/960
  choice agreement    0/960

A3 FIRST_7_REGISTRY:
  target reachability 448/960
  choice agreement    448/960

A4 target lookup:
  behavioral agreement 960/960
  oracle displacement  true
```

The valuation/navigation hard regressions inherited by `6355333` must remain wired through the child executable.

As before, a fresh registry panel may be executed in the connector environment while older audits remain inherited hard assertions unless a true repository-process replay occurs.

---

## 16. Preregistered primary predictions

The primary predictions are:

| Representation | Target partitions recovered | Recall | Downstream exact-choice target | Interpretation |
|---|---:|---:|---:|---|
| R0 explicit registry | 15/15 | 1.0 | 960/960 | reference |
| R1 basis + XOR closure | 15/15 | 1.0 | 960/960 | candidate registry contraction |
| R2 primitives only | 4/15 | 4/15 | 256/960 | insufficient substrate |
| R3 one XOR layer | 10/15 | 10/15 | 640/960 | insufficient closure |
| R4 opaque family macro | 15/15 behaviorally | 1.0 | 960/960 possible | hidden specification; invalid contraction |
| R5 context-target generator | not a context-independent full registry | n/a | 960/960 possible | oracle displacement |

The execution must derive these coverage quantities from recovered evidence partitions, not hard-code the final scores.

---

## 17. Decision tree

### If R1 recovers 15/15, preserves 960/960, and expanded burden falls 15 -> 8

Earn only:

\[
\boxed{
\textbf{explicit latent experiment enumeration is not necessary for this fixed finite experiment family; a smaller target-blind compositional substrate recovers the same extensional registry.}
}
\]

Do **not** claim experiment invention.

### If R1 is behaviorally exact but expanded burden does not fall

Interpret as:

\[
\boxed{
\text{registry substitution}
\neq
\text{registry substrate reduction}.
}
\]

### If R1 fails extensional recovery

Do not infer that explicit enumeration is globally necessary.

Infer only that the tested basis/operator/grammar substrate is insufficient for the frozen family.

### If R2 or R3 exceeds its extensional coverage ceiling

Classify as leakage or benchmark defect.

### If R4/R5 behavioral success is used to support minimality

Reject the claim as oracle/specification displacement.

---

## 18. Candidate Gate-1 claim if the preregistered prediction holds

If R1 succeeds and controls behave as predicted, the strongest candidate claim is:

\[
\boxed{
\textbf{
In this finite audited regime, the externally supplied latent experiment registry can be compressed from 15 explicit experiment-semantic bindings to a smaller target-blind primitive/operator/closure specification while preserving the exact same experiment partitions and downstream decisions.
}
}
\]

The complementary dependency result is:

\[
\boxed{
\textbf{
primitive availability without adequate composition/closure is insufficient to recover the full useful registry.
}
}
\]

The audit does **not** establish:

- that the R1 substrate is globally minimal;
- that XOR is a universally necessary experiment operator;
- that the primitive coordinate basis is minimal;
- that the experiment family was invented;
- that a useful experiment outside the old recoverable family became available;
- that \(\mathcal E_t^\star\subsetneq\mathcal E_{t+1}^\star\);
- that \(\mathfrak R_{E,t}\to\mathfrak R_{E,t+1}\) has occurred;
- any basin-opening result.

---

## 19. Gate separation after this preregistration

The program now distinguishes:

\[
\boxed{
\begin{aligned}
G_1:&\quad
B_{\mathcal E^\star}\downarrow
\land
\mathcal E^\star\text{ unchanged extensionally},\\[3pt]
G_2:&\quad
\mathcal E_t^\star\subsetneq\mathcal E_{t+1}^\star.
\end{aligned}
}
\]

Only G2 earns the language of experiment-space construction / basin opening.

The empirical spine is therefore:

\[
\boxed{
\text{geometry}
\rightarrow
\text{navigation}
\rightarrow
\text{valuation}
\rightarrow
\text{accessibility}
\rightarrow
\boxed{\text{latent-registry minimality}}
\rightarrow
\text{experiment-space construction}.
}
\]

The next repository action after this preregistration is implementation/execution of **this Gate-1 audit only**.

No `P_ep` ledger update and no Gate-2 artifact is authorized until the registry-minimality result exists.
