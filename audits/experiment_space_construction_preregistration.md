# Experiment-Space Construction Discriminant — Preregistration

## Status

This document freezes the first Gate-2 experiment **before execution**.

Parent dependency checkpoint:

```text
5fe0a86  Update experiment-planning dependency consolidation after Gate-1 registry compression
```

Gate-1 empirical anchor:

```text
c661e58  latent-registry minimality audit
```

No Gate-2 empirical result is recorded here.

The governing boundary is:

\[
\boxed{
\text{registry compression}
\neq
\text{registry expansion}.
}
\]

Gate 1 established that the old 15-partition registry can be derived from a smaller supplied compositional substrate. Gate 2 now asks whether a useful experiment partition that is **provably outside that old closure** can become reachable only after the admitted experiment-construction substrate changes.

This audit tests **causal experiment-space expansion under a supplied target-blind substrate extension**. It does **not** test whether the system can autonomously discover, authorize, or invent the substrate extension itself.

---

## 1. Scientific question

The narrow question is:

\[
\boxed{
\textbf{Can a target-blind change in the admitted experiment-construction substrate make a useful refinement reachable that was outside the complete Gate-1 closure?}
}
\]

A successful result requires all of the following:

1. the novel target partition is absent from the **exhaustively computed old closure**;
2. the old closure cannot support the warranted acquisition decision;
3. a changed target-blind construction substrate makes the target partition reachable;
4. downstream access, valuation, navigation, stopping, correction contract, burden, and commitment rules remain frozen;
5. no target-specific experiment description, lookup, semantic label, or winner hint is supplied;
6. the new useful partition is genuinely outside the old closure rather than an unenumerated point already licensed by it.

The anti-cheat criterion is therefore:

\[
\boxed{
\Pi(e_{\rm novel})\notin
\operatorname{Closure}(S_0)
}
\]

where `S0` is the exact Gate-1 construction substrate.

---

## 2. Freeze the old Gate-1 substrate

The old admitted experiment substrate `S0` is exactly the successful R1 representation from `c661e58`:

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

### Old closure rule

```text
repeat XOR over currently admitted experiment semantics until no new evidence partition appears
```

### Old generic constraints

1. discard the constant/zero experiment;
2. deduplicate by evidence-partition equivalence, allowing output-polarity reversal.

The complete old closure is:

\[
\boxed{
\mathcal C_0
=
\operatorname{Closure}(S_0)
=
\{\Pi(m\cdot X):m\neq0000\},
\qquad
|\mathcal C_0|=15.
}
\]

The canonical Gate-1 partition-set checksum is frozen as:

```text
809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

Execution must recompute this closure from the Gate-1 substrate rather than accepting the number `15` as a target label.

---

## 3. Formal novelty definition

For a binary experiment `e`, let `Pi(e)` denote the induced partition of the 16 worlds, identifying output-token complements as the same experiment partition.

Define Gate-2 novelty relative to `S0` by:

\[
\boxed{
\operatorname{Novel}_{S_0}(e)=1
\iff
\Pi(e)\notin\mathcal C_0.
}
\]

Novelty is therefore **extensional and closure-relative**.

It is not established by:

- a new probe name;
- a new syntax tree;
- a longer expression;
- a different output polarity;
- a probe omitted from a finite enumeration but already licensed by `S0`;
- a new implementation of an old partition.

The execution must prove novelty by exhaustive membership failure against the canonical old partition closure.

---

## 4. Freeze everything downstream of experiment construction

Hold fixed across all compared construction substrates:

\[
\boxed{
A_{\rm registry},\;
\mathfrak R_E,\;
S_{\rm refine},\;
Q_{\rm acquire}^{\rm role},\;
T_{\rm stop},\;
\Pi_{\mathcal P},\;
\tau.
}
\]

In particular:

- accessibility remains the target-blind `ALL_REGISTRY` mechanism earned at `6355333`;
- the correction contract is evaluator-defined and unchanged;
- every exposed candidate receives the same anchored acquisition burden `kappa=0.1`;
- valuation remains contract-derived corrective consequence against the COMMIT-anchored burden;
- no target-specific candidate generator or semantic hint is introduced;
- candidate identities remain opaque and permuted;
- the commitment rule is unchanged.

The only causal intervention is:

\[
\boxed{
S_0\rightarrow S_1
}
\]

in the admitted experiment-construction substrate.

---

## 5. Frozen nonlinear novelty panel

Use the same uniform four-bit world:

\[
X=(x_1,x_2,x_3,x_4)\in\{0,1\}^4.
\]

Freeze four nonlinear correction targets:

\[
\begin{aligned}
n_1(X)&=x_1\land x_2,\\
n_2(X)&=(x_1\oplus x_2)\land x_3,\\
n_3(X)&=(x_1\oplus x_2)\land(x_3\oplus x_4),\\
n_4(X)&=(x_1\land x_2)\oplus(x_3\land x_4).
\end{aligned}
\]

For correction context `c_k`, the warranted terminal action is:

\[
a^\star_{c_k}(X)=n_k(X).
\]

Each exact evidence experiment `e_k(X)=n_k(X)` is a candidate novel refinement.

### Preregistered novelty obligation

For every `k in {1,2,3,4}`:

\[
\boxed{
\Pi(e_k)\notin\mathcal C_0.
}
\]

Execution must verify this by exhaustive old-closure membership testing under every anonymous encoding.

---

## 6. Frozen decision relevance

Under the uniform world distribution:

```text
n1 baseline Bayes accuracy = 0.75
n2 baseline Bayes accuracy = 0.75
n3 baseline Bayes accuracy = 0.75
n4 baseline Bayes accuracy = 0.625
```

The exact target experiment therefore produces correction-relevance gains:

```text
n1 exact R_corr = 0.25
n2 exact R_corr = 0.25
n3 exact R_corr = 0.25
n4 exact R_corr = 0.375
```

Every old Gate-1 parity experiment must satisfy:

\[
\boxed{
R_{\rm corr}(e\mid c_k)=0
\quad\forall e\in\mathcal C_0,
\quad\forall k.
}
\]

With the frozen burden:

\[
\boxed{\kappa=0.1,}
\]

this implies:

- under `S0`, every old experiment has non-positive acquisition margin and the frozen controller returns `COMMIT`;
- if the exact novel target experiment becomes reachable, it is strictly worthwhile and uniquely choice-maximal by partition.

Execution must recompute these quantities from evidence partitions and the correction contract, not hard-code target choices.

---

## 7. G20 reference — old Gate-1 closure

`G20` uses the unchanged Gate-1 substrate `S0`.

Recovered experiment space:

\[
\boxed{\mathcal C_0,\ |\mathcal C_0|=15.}
\]

Preregistered endpoints across 64 anonymous encodings × 4 nonlinear contexts:

\[
\boxed{256\text{ context-encoding evaluations}.}
\]

Expected:

```text
novel targets reachable:       0 / 256
novel target partitions found: 0 / 4 per encoding
choice of novel target:         0 / 256
COMMIT under old closure:     256 / 256
```

This is the critical impossibility baseline:

\[
\boxed{
\text{useful target exists in evaluator}
\land
\Pi(e_{\rm target})\notin\mathcal C_0
\land
\text{old construction substrate cannot expose it}.
}
\]

---

## 8. G21 primary expansion — add one generic nonlinear operator and adequate post-extension closure

Keep the four primitive semantics and XOR operator.

Add one target-blind binary experiment operator:

\[
\boxed{
AND(f,g)(w)=f(w)\land g(w).
}
\]

The operator receives no correction context, target name, target truth table, winner identity, or semantic hint.

### Expanded construction grammar

1. compute the complete old Gate-1 XOR closure `C0`;
2. admit one `AND` composition of any pair of experiments in `C0`;
3. take XOR closure over the union of the old experiments and the newly admitted nonlinear experiments;
4. discard the constant/zero experiment;
5. deduplicate by evidence-partition equivalence.

This is a bounded degree-2 expansion. It does not allow recursive `AND` of newly nonlinear results.

The resulting admitted experiment family should be exactly the nonzero degree-`<=2` Boolean polynomial partitions with zero constant term over the four supplied coordinates:

\[
\boxed{|\mathcal C_1|=1023.}
\]

Execution must derive this size extensionally rather than hard-code it.

### Primary success condition

For every anonymous encoding:

\[
\boxed{
\mathcal C_0\subsetneq\mathcal C_1
}
\]

and all four target partitions must satisfy:

\[
\boxed{
\Pi(e_k)\in\mathcal C_1\setminus\mathcal C_0.
}
\]

Across 256 context-encoding evaluations:

```text
novel target reachability: 256 / 256
novel target choice:       256 / 256
```

If this holds, the strongest permitted claim is:

\[
\boxed{
\textbf{A target-blind change in the admitted experiment-composition substrate makes previously unreachable useful experiment partitions reachable and selectable.}
}
\]

Because the admitted partition family changes extensionally, this is a local experiment-space expansion / basin-opening result relative to the frozen Gate-1 substrate.

It does **not** establish that the system discovered or authorized the `AND` extension itself.

---

## 9. Construction-specification ledger

The Gate-2 ledger tracks the supplied construction substrate explicitly.

### Old `S0`

```text
B_primitives             = 4
B_operators              = 1   # XOR
B_grammar                = 1   # XOR closure
B_semantic_labels        = 0
B_generation_constraints = 2
B_target_hints           = 0
--------------------------------
B_construction clauses   = 8
```

### Expanded `S1`

```text
B_primitives             = 4
B_operators              = 2   # XOR, AND
B_grammar                = 2   # old closure + one nonlinear layer followed by XOR closure
B_semantic_labels        = 0
B_generation_constraints = 2
B_target_hints           = 0
--------------------------------
B_construction clauses   = 10
```

Gate 2 is not a compression claim: `S1` deliberately increases admitted construction structure.

The required causal signature is:

\[
\boxed{
B_{\rm construction}\uparrow
\land
\mathcal C_0\subsetneq\mathcal C_1
\land
\text{new correction-relevant partitions become reachable}.
}
\]

The burden increase must be target-blind and smaller than directly supplying target semantics.

---

## 10. G22 negative control — add syntax that does not change partition geometry

Add a generic unary `NOT` operator to `S0`, with closure under NOT and XOR.

Because experiment semantics are scored as partitions modulo output polarity, `NOT` must not add a new evidence partition:

\[
\boxed{
\mathcal C_{NOT}=\mathcal C_0.
}
\]

Expected across 256 evaluations:

```text
novel target reachable: 0 / 256
novel target choice:    0 / 256
```

This establishes:

\[
\boxed{
\text{new syntax/operator token}
\neq
\text{experiment-space expansion}.
}
\]

If `G22` reaches a nonlinear target partition, classify the benchmark as defective.

---

## 11. G23 negative control — nonlinear operator without adequate post-extension closure

Add the same generic `AND` operator, but allow only one direct `AND` of two old `C0` experiments and **do not** XOR-compose newly nonlinear results afterward.

This admits a larger family than `C0`, but not the full `C1` expansion.

The extensional family should contain 120 partitions after deduplication.

Preregistered target recovery:

```text
n1 reachable: yes
n2 reachable: yes
n3 reachable: yes
n4 reachable: no
```

Thus:

\[
\boxed{\operatorname{TargetCoverage}(G23)=3/4.}
\]

Across 64 anonymous encodings × 4 contexts:

\[
\boxed{192/256}
\]

is the exact target-reachability and downstream-choice ceiling.

The missing `n4` target requires recombination of newly nonlinear structure:

\[
n_4=(x_1\land x_2)\oplus(x_3\land x_4).
\]

Therefore:

\[
\boxed{
\text{nonlinear operator availability}
\neq
\text{adequate expanded compositional closure}.
}
\]

`G23` exceeding `192/256` is leakage or a benchmark defect.

---

## 12. G24 anti-scaffold control — direct novel-target registry

Directly append the four target experiment semantics `n1...n4` to the old registry.

This trivially permits 256/256 behavior, but it supplies the exact target partitions and therefore relocates the evaluator into the experiment substrate.

Ledger must record at least:

```text
B_target_specific_semantics = 4
context-independent target set = supplied directly
```

This is not accepted as evidence that a generic construction substrate opened the experiment space.

It is classified as:

\[
\boxed{\text{target-specific specification displacement}.}
\]

The fact that four direct target bindings may use fewer finite clauses than the generic `S1` is irrelevant: the causal question is whether a **target-blind reusable construction rule** can open the admitted experiment space, not whether the evaluator can inject the answers compactly.

---

## 13. G25 anti-scaffold control — opaque nonlinear-family macro

Allow a superficially small command such as:

```text
ALL_DEGREE2_4
```

If it emits `C1` without a transparent lower-level definition, its visible syntax is not its specification burden.

The execution must expand the macro to the semantic obligations it encodes.

Two valid classifications exist:

1. if transparently implemented only through the `S1` primitive/operator/grammar clauses, it is an alias for `S1` and inherits the `S1` expanded burden;
2. if it directly encodes the emitted family, it is hidden specification and cannot support a construction claim.

Thus:

\[
\boxed{
\text{compact family macro}
\neq
\text{warranted experiment-space construction}.
}
\]

---

## 14. Anonymous encoding requirements

Run at least 64 anonymous encodings.

For each encoding:

- permute primitive coordinate handles;
- permute world-state labels consistently;
- independently flip binary experiment output tokens;
- permute correction-context identifiers;
- permute emitted experiment handles / registry order;
- evaluate semantic equality only by canonical evidence partition;
- never expose `AND`, `XOR`, target formulas, target names, `novel`, `relevant`, or `best` to the downstream chooser;
- construction operators may exist internally in the experiment generator, but emitted experiments must have opaque identities.

The construction result must be invariant to public naming and output polarity.

---

## 15. Primary endpoints

Execution must report:

1. recomputed old closure `C0` size and checksum;
2. exhaustive novelty proof for each `n1...n4` against `C0`;
3. old-closure maximum correction relevance for each nonlinear context;
4. exact target correction relevance and acquisition margin;
5. extensional family size for every construction condition;
6. old/new partition-set inclusion relation;
7. target partition reachability;
8. downstream choice agreement;
9. candidate-identity invariance;
10. complete visible and expanded construction-specification ledgers;
11. target-specific semantic/hint counts;
12. whether each condition changes experiment-space extensionally;
13. upstream Gate-1/accessibility hard-regression status.

Terminal choice alone is not a sufficient endpoint.

---

## 16. Upstream regression boundary

The child executable must import and hard-assert the Gate-1 registry-minimality certificate from `c661e58`:

```text
R0 explicit registry:
  15/15 partitions
  64/64 extensional equality
  960/960 downstream choices

R1 Gate-1 basis + XOR closure:
  15/15 partitions
  precision/recall 1/1
  zero extras
  64/64 extensional equality
  960/960 downstream choices
  expanded B_E* = 8

R2 primitives only:
  4/15 partitions
  256/960 choices

R3 one XOR layer:
  10/15 partitions
  640/960 choices
```

The inherited accessibility / valuation / navigation assertions must remain recursively wired.

If any upstream certificate changes, reject Gate-2 attribution.

As in recent connector runs, the new Gate-2 panel may be freshly executed while older audits remain inherited hard assertions unless a genuine repository-process replay is performed.

---

## 17. Frozen interpretation table

| Result | Interpretation |
|---|---|
| `G20` cannot reach any nonlinear target and exhaustive novelty checks pass | old Gate-1 closure genuinely excludes the targets |
| `G21` produces `C0 subsetneq C1`, reaches all four novel targets, and preserves frozen downstream choice | causal experiment-space expansion under supplied target-blind substrate extension |
| `G22` changes syntax but not partition set | no basin opening; representation-only change |
| `G23` reaches exactly 3/4 targets | operator availability alone insufficient; post-extension compositional closure matters |
| `G23 > 3/4` | leakage / benchmark defect |
| `G24` succeeds | target-specific specification displacement; invalid construction evidence |
| `G25` succeeds via hidden macro semantics | hidden specification; invalid construction evidence |
| `G21` target appears in recomputed `C0` | novelty criterion failed; reject Gate 2 |
| upstream regression changes | causal attribution invalid |

---

## 18. Candidate claim if the preregistered result holds

If `G20` proves all four targets are outside the exhaustive old closure, `G21` makes them reachable and selected under a target-blind generic extension, `G22/G23` obey their extensional ceilings, and `G24/G25` are rejected as specification displacement, the strongest permitted claim is:

\[
\boxed{
\textbf{In this finite audited regime, changing the admitted experiment-composition substrate opens a strictly larger refinement space containing useful evidence partitions that were unreachable under the complete prior closure.}
}
\]

This supports a local causal basin-opening statement relative to `S0`.

It does **not** establish:

- autonomous discovery of the `AND` operator;
- warranted selection among candidate substrate extensions;
- authorization to change experiment machinery;
- unrestricted experiment invention;
- general ontology construction;
- self-modification;
- that `AND` is uniquely necessary;
- that the expanded degree-2 family is minimal.

---

## 19. Discovery remains a separate unsolved question

A successful `G21` result would establish that a change in experiment-construction machinery **can** make a previously unreachable useful refinement reachable.

It would not establish that the system can infer from failure evidence that such a change is warranted, generate an appropriate extension, distinguish it from alternatives, and bind it without target leakage.

That later question is closer to the CCA-style adaptive transformation problem:

\[
\boxed{
\text{failure evidence}
\rightarrow
\text{diagnosis of closure insufficiency}
\rightarrow
\text{candidate substrate transformation}
\rightarrow
\text{authorization}
\rightarrow
\text{expanded refinement space}.
}
\]

This preregistration does not test that chain.

---

## 20. Research position after this preregistration

The empirical spine is now:

\[
\boxed{
\text{geometry}\checkmark
\rightarrow
\text{navigation}\checkmark
\rightarrow
\text{valuation}\checkmark
\rightarrow
\text{accessibility}\checkmark
\rightarrow
G_1:\text{ registry compression}\checkmark
\rightarrow
\boxed{G_2:\text{ experiment-space construction [preregistered]}}.
}
\]

The next repository action is implementation/execution of this Gate-2 discriminant only.

No `P_ep` ledger update and no autonomous-discovery artifact is authorized until the Gate-2 result exists.
