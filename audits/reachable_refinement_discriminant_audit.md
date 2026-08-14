# Reachable Refinement Discriminant Audit

## Status

This audit is the empirical gate for the candidate object

\[
\mathfrak R_E(\Pi,\tau,\mathcal A),
\]

interpreted provisionally as **time-indexed reachable admissible refinement structure**.

The object is **not assumed to be a primitive**.

The audit asks only whether it predicts a difference that a static evidence inventory cannot.

No new theory is introduced here.

---

# 1. Scientific question

The previous epistemic work established that evidence availability, identifiability, inference, and active acquisition are distinct.

The current candidate refinement is stronger:

> Correction capacity may depend not only on which informative probes exist, but on whether their refinements can be composed contingently and in time.

The decisive prediction is therefore:

\[
\boxed{
\text{same static evidence}
\land
\text{different contingent refinement geometry}
\Rightarrow
\text{different correction possibility}.
}
\]

If this contrast fails under matched controls, the candidate object does not earn explanatory authority and the program should contract toward the static evidence account.

---

# 2. What is held fixed

The A/B/C conditions share exactly the same:

\[
\boxed{
\Pi_0,\;
\Pi_{\mathcal P},\;
A_{\rm probe},\;
I(W;E_{r_i}),\;
C,\;
\text{budget},\;
\tau.
}
\]

Operationally, all three conditions use:

- the same 8 worlds;
- the same uniform prior;
- the same binary terminal correction contract;
- the same three binary probe semantics;
- the same exact per-probe partitions of the world set;
- the same probe outcome alphabets;
- the same probe costs;
- the same initial availability of all three probes;
- the same two-probe budget;
- the same commitment deadline \(\tau=2\).

The **only manipulated variable** is the outcome-conditional accessibility/timing of the second refinement after the selector probe has been observed.

---

# 3. Finite world and correction contract

Each world is:

\[
W=(s,x,y)\in\{0,1\}^3,
\]

where:

- \(s\) is a selector bit;
- \(x\) is the left branch value;
- \(y\) is the right branch value.

The terminal warranted correction is:

\[
a^\star(W)
=
\begin{cases}
x,&s=0,\\
y,&s=1.
\end{cases}
\]

For this deliberately terminal finite audit, the required correction partition is exactly the binary action partition:

\[
W_A\sim_{\Pi_{\mathcal P}}W_B
\iff
a^\star(W_A)=a^\star(W_B).
\]

This audit does **not** generalize that terminal-action partition to the broader Future Sufficiency program.

---

# 4. Static evidence inventory

There are three canonical evaluator-side probes:

1. selector probe \(r_s\): reveals \(s\);
2. left probe \(r_x\): reveals \(x\);
3. right probe \(r_y\): reveals \(y\).

Every probe is deterministic and binary.

Under the uniform eight-world prior:

\[
I(W;E_{r_s})
=
I(W;E_{r_x})
=
I(W;E_{r_y})
=
1\text{ bit}.
\]

The probes differ in immediate target relevance, but that relevance is also exactly matched across A/B/C:

| Probe | \(I(a^\star;E_r)\) bits | Bayes target accuracy from probe alone |
|---|---:|---:|
| selector | 0 | 0.50 |
| left | 0.1887218755 | 0.75 |
| right | 0.1887218755 | 0.75 |

The complete static inventory is jointly sufficient:

\[
\boxed{
\operatorname{BayesAcc}
(a^\star\mid r_s,r_x,r_y)
=
1.
}
\]

So a static account that records only which evidence channels exist, their semantics, and their individual information content sees the same resources in A, B, and C.

---

# 5. Budget and commitment boundary

The system may use at most:

\[
\boxed{2\text{ probes}}
\]

and the correction must be available by:

\[
\boxed{\tau=2}.
\]

The first probe returns at time \(1\).

An ordinary second probe returns one time unit later, at time \(2\), and is therefore timely.

A delayed second refinement with latency \(2\) returns at time \(3\), after the commitment boundary.

This creates a distinction between:

\[
\boxed{
\text{timely reachable}
\neq
\text{eventually reachable}
\neq
\text{unreachable}.
}
\]

---

# 6. The only A/B/C manipulation

All three probes are initially available in every condition.

If the first query is one of the data probes \(r_x\) or \(r_y\), the other two probes retain ordinary availability and ordinary latency in **all three conditions**.

A/B/C differ only after querying the selector first.

## A — timely reachable

After \(s\) is observed:

- if \(s=0\), \(r_x\) remains available;
- if \(s=1\), \(r_y\) remains available.

The relevant follow-up returns at time \(2\).

Thus the contingent policy

```text
query selector
    |
    +-- s=0 --> query left
    |
    +-- s=1 --> query right
```

reaches the required correction partition before commitment.

---

## B — reachable too late

The same correction-relevant follow-up remains available after the selector:

- \(r_x\) when \(s=0\);
- \(r_y\) when \(s=1\).

But the follow-up has latency \(2\), so its observation arrives at time \(3\).

Thus the same refinement is:

\[
\boxed{
\text{eventually reachable}
}
\]

but:

\[
\boxed{
\text{not reachable before }\tau.
}
\]

---

## C — unreachable rewiring

C does **not** simply delete the second edge.

After the selector, exactly one follow-up remains available, just as in A and B, but it is rewired to the irrelevant branch:

- if \(s=0\), only \(r_y\) remains;
- if \(s=1\), only \(r_x\) remains.

The edge returns on time.

Therefore A/B/C are degree-matched after selector-first:

\[
\boxed{
\text{one follow-up edge per selector outcome in every condition}.
}
\]

The manipulated difference is which refinement that edge reaches, and in B when it returns.

This is a stronger control than simply removing a probe.

---

# 7. Why C cannot route around the rewiring

Because all probes are initially available, a policy can choose a data probe before the selector.

But with only two total probes, no alternative ordering can identify the multiplexed target for all eight worlds.

For example:

```text
left -> selector
```

resolves the target when \(s=0\), but leaves \(y\) unknown when \(s=1\).

Likewise:

```text
right -> selector
```

fails symmetrically.

And:

```text
left -> right
```

never observes which branch is warranted.

This is not asserted informally. The evaluator exhaustively enumerates the entire finite policy class.

---

# 8. Stage 1 — evaluator-side structural certificate

The evaluator enumerates every deterministic policy using **at most two probes**, including early stopping.

The policy class contains:

\[
\boxed{302}
\]

policies.

It includes:

- STOP immediately with either terminal action;
- any first probe;
- after each first outcome, either STOP or choose either remaining probe;
- every binary terminal action mapping after the second observation.

Thus the structural certificate is computed before any learner exists.

Define:

\[
\operatorname{Reach}^{\tau}_{\mathcal P}(\Pi_0)=1
\]

iff at least one enumerated contingent policy achieves the warranted correction for **all worlds** by the commitment deadline.

Define:

\[
\operatorname{Reach}_{\mathcal P}(\Pi_0)=1
\]

iff at least one policy achieves the warranted correction for all worlds when the deadline is ignored but the same two-probe budget and refinement accessibility are retained.

---

# 9. Stage 1 results

Local deterministic execution gives:

| Condition | Reachable by \(\tau\) | Eventually reachable | Max timely accuracy | Max eventual accuracy | Full timely policies | Full eventual policies |
|---|---:|---:|---:|---:|---:|---:|
| A — timely reachable | **yes** | **yes** | **1.0000** | **1.0000** | 1 | 1 |
| B — late reachable | **no** | **yes** | **0.7500** | **1.0000** | 0 | 1 |
| C — rewired unreachable | **no** | **no** | **0.7500** | **0.7500** | 0 | 0 |

This is the intended three-way separation:

\[
\boxed{
A:
\operatorname{Reach}_{\mathcal P}^{\tau}=1
}
\]

\[
\boxed{
B:
\operatorname{Reach}_{\mathcal P}=1,
\qquad
\operatorname{Reach}_{\mathcal P}^{\tau}=0
}
\]

\[
\boxed{
C:
\operatorname{Reach}_{\mathcal P}=0.
}
\]

---

# 10. Stage 2 — learner test

Only after the structural certificate is fixed is a learner introduced.

The learner is finite ERM over the **same 302-policy language**.

To prevent semantic probe names from carrying the result, each run anonymously transforms the evidence interface using:

- a permutation of probe identities;
- independent binary outcome-polarity flips.

The audit runs:

\[
\boxed{64}
\]

anonymous encodings.

The learner receives a preregistered four-world teaching set:

```text
(0,0,0)
(0,1,0)
(1,1,0)
(1,1,1)
```

and is evaluated on the other four held-out worlds.

No hidden canonical probe name is supplied to the policy learner.

Two objectives are reported:

1. **timely objective** — correction after \(\tau\) counts as failure;
2. **eventual diagnostic** — deadline ignored, to distinguish B from C.

---

# 11. Stage 2 results

Across all 64 anonymous encodings:

| Condition | Learner timely full accuracy | Learner eventual full accuracy |
|---|---:|---:|
| A | **1.0000** | **1.0000** |
| B | **0.7500** | **1.0000** |
| C | **0.7500** | **0.7500** |

The same values hold on the held-out worlds.

For A, the teaching set identifies one perfect policy.

For B and C under the timely objective, multiple ERM policies tie, but every tied optimum has the same held-out accuracy of \(0.75\). Therefore the result is not tie-break sensitive.

For B under the eventual diagnostic, one perfect eventual policy is recovered.

The learner therefore reaches the evaluator-side structural ceiling in every condition.

That matters diagnostically:

\[
\boxed{
\text{B/C failure is not attributed to learner weakness within this policy class}.
}
\]

---

# 12. Static-account contrast

The strongest control is now explicit.

Across A/B/C:

\[
\boxed{
\text{same worlds}
}
\]

\[
\boxed{
\text{same target partition}
}
\]

\[
\boxed{
\text{same probe inventory}
}
\]

\[
\boxed{
\text{same exact single-probe partitions}
}
\]

\[
\boxed{
\text{same single-probe information}
}
\]

\[
\boxed{
\text{same initial availability}
}
\]

\[
\boxed{
\text{same costs, budget, and commitment time}
}
\]

and the full static evidence inventory is jointly sufficient.

Yet:

\[
\boxed{
\text{correction possibility differs}.
}
\]

The difference is entirely in the contingent composition/timing of the refinements.

---

# 13. Earned result

If the executable assertions continue to hold under replication, this audit earns the following narrow claim:

\[
\boxed{
\textbf{
In this finite deterministic audit, correction capacity depends on timely compositional reachability of admissible refinements, not merely on the static inventory of individually informative probes.
}
}
\]

This is incremental predictive content over the static evidence account.

It is sufficient to justify treating:

\[
\boxed{
\mathfrak R_E(\Pi,\tau,\mathcal A)
}
\]

as a useful explanatory object **for this finite deterministic regime**.

It does not establish a universal primitive.

---

# 14. What is not earned

This audit does **not** establish:

- stochastic refinement dominance;
- a universal partition formalism;
- dynamic-programming necessity;
- STOP as primitive or derived;
- general experiment design;
- self-specified experiment spaces;
- research agency;
- repair of the refinement geometry;
- general corrigibility;
- a theorem about arbitrary POMDPs or partially observed systems.

The stochastic generalization remains open.

---

# 15. Contradiction rule

The audit preserves the existing benchmark discipline.

If the evaluator certifies:

\[
\boxed{
\operatorname{Reach}^{\tau}_{\mathcal P}=0
}
\]

but a learner/controller nevertheless obtains perfect timely correction, the first response is:

\[
\boxed{
\text{audit the construction for leakage or an unmodeled refinement path}.
}
\]

Do not reinterpret an impossibility violation as superior intelligence until the certificate itself has been invalidated.

Likewise, if A fails despite a certified reachable policy, that is initially a competence failure, not evidence that the refinement geometry is impossible.

---

# 16. Relation to the next phase

This audit tests the **geometry** before minimizing the machinery that navigates it.

If the result survives, the next dependency problem becomes:

\[
\boxed{
\mathfrak P_{\rm ep,min}\;?
}
\]

with the refinement geometry held fixed.

Only after navigation is minimized should the program ask whether the system can transform:

\[
\boxed{
\mathfrak R_E
\rightarrow
\mathfrak R_E'.
}
\]

So the empirical order remains:

\[
\boxed{
\text{validate geometry}
\rightarrow
\text{minimize navigation}
\rightarrow
\text{test geometry repair}.
}
\]

No additional abstraction is required by this audit.
