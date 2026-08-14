# Post-v1 V2 Target-Selection Protocol

## Status

```text
v1_terminal_ledger
  81efea2405e3b0269c9bad3bf417d4ab73ea080b

development_inventory
  a72f5a8df8f69d33e79304a9dafd540d1d82f601

DSLI_R1_SCIENTIFIC_STATE          = CLOSED
DEVELOPMENT_EVIDENCE_INVENTORY    = FROZEN
V2_TARGET_SELECTION_PROTOCOL      = FROZEN
V2_TARGET_SELECTED                = false
V2_PREREGISTRATION_CREATED        = false
V2_EXPERIMENTAL_DESIGN_CREATED    = false
V2_DESIGN_AUTHORITY_EXERCISED     = false
```

This artifact freezes the decision rule that a later, separate development operation may use to select one target from the already-frozen post-v1 development-evidence inventory.

Its governing separation is:

\[
\boxed{
\text{selection rule}
\neq
\text{v2 experimental design}.
}
\]

The protocol does not score the candidates, name a winner, define a benchmark, freeze a target-specific measurement system, or create a v2 preregistration.

The only new authority introduced here is authority to apply the frozen target-selection rule in a later, separate operation.

---

# 1. Frozen candidate universe

The only candidates admissible to the next target-selection operation are the four records frozen in the development-evidence inventory at `a72f5a8df8f69d33e79304a9dafd540d1d82f601`:

\[
\boxed{
\begin{aligned}
H_1 &: \text{framework legibility / reconstruction sufficiency},\\
H_2 &: \Delta_T^A,\;P_{\rm keep},\;\text{repair vs. replacement},\\
H_3 &: \text{horizon-cost / future-sufficiency surface},\\
H_4 &: \text{active-identifiability intervention}.
\end{aligned}
}
\]

The candidate records `D_j` are inputs to selection, not mutable objects during selection.

The next operation may not:

```text
add a fifth candidate
remove a candidate
rewrite a motivation
change X_j
change O_j
change T_A,j
change candidate-defect semantics
change required-evidence statements
change authority limits
change dependencies
change risks
change provenance
```

If any candidate record must change before selection, the current protocol must not be applied. A separately versioned development-inventory update and, if necessary, a separately versioned selection protocol are required first.

---

# 2. Selection provenance

Target selection is a development decision, not an empirical result.

```text
selection_provenance = DEVELOPMENT_DECISION
selection_is_v1_evidence = false
selection_is_confirmatory_evidence = false
selection_validates_selected_hypothesis = false
selection_authorizes_v2_execution = false
```

Therefore:

\[
\boxed{
\texttt{SELECTED\_V2\_TARGET}
\neq
\texttt{VALIDATED\_HYPOTHESIS}.
}
\]

and:

\[
\boxed{
\texttt{SELECTED\_V2\_TARGET}
\not\Rightarrow
\texttt{V2\_EXECUTION\_AUTHORIZED}.
}
\]

Selection grants only design focus: permission for a later preregistration operation to develop one candidate into a frozen experiment.

---

# 3. Inputs allowed during selection

The next target-selection operation may use only:

```text
1. the frozen D_j records from a72f5a8d...
2. this frozen target-selection protocol
3. the immutable fact that DSLI_R1 is closed
```

No post-protocol candidate-specific empirical result, new external critique, newly generated benchmark result, pilot outcome, or newly elaborated target-specific architecture may be used to change a candidate's score in the selection operation.

If materially new development evidence appears before selection, the correct action is:

```text
STOP_SELECTION
-> version the development inventory
-> decide whether this selection protocol remains admissible
-> only then resume selection
```

This prevents evidence observed after the rule is known from being selectively imported to favor a candidate.

---

# 4. Selection architecture

Selection uses two stages:

\[
\boxed{
\text{eligibility gates}
\rightarrow
\text{lexicographic development comparison}.
}
\]

There is no weighted sum, expected-value score, informal gestalt override, or prose-level tie-break.

The rule is deliberately development-oriented rather than confirmatory: it chooses which question is most suitable to formalize next; it does not claim which hypothesis is most true, important, valuable, or likely to succeed.

---

# 5. Eligibility gates

For each candidate `H_j`, evaluate the following gates using only its frozen `D_j` record.

Every gate is Boolean.

A candidate is `ELIGIBLE` only if all gates pass.

## E1 — empirical form is reachable

Pass iff the frozen record contains enough candidate structure to support, in principle, a finite empirical question with a domain/interface/obligation form such as:

\[
(X_j,O_j,T_{A,j})
\]

and a possible observable failure or success condition.

This does not require the experiment already to be designed.

Fail if the candidate remains only a philosophical topic with no identifiable empirical object even in provisional form.

## E2 — authority-bounded outcome is expressible

Pass iff the frozen record states a local claim boundary such that a future positive or negative result could be interpreted without automatically granting mechanism, universal validity, adoption, authorization, or binding.

Fail if any plausible result would be scientifically uninterpretable without an unlicensed authority jump.

## E3 — fresh challenge/evidence is in principle obtainable

Pass iff the frozen record admits a plausible path to future evidence that is not identical to the development observation that motivated the candidate.

The path may require later design, but confirmatory evidence must be conceptually separable from motivating evidence.

Fail if the candidate can only be evaluated by re-reading or re-labeling the evidence that selected it.

## E4 — principal failure locus can be distinguished

Pass iff the frozen record contains, or explicitly requires, a way to separate the central proposed defect from at least the most immediate competing shallow failure locus.

Examples include, depending on candidate:

```text
reconstructor failure vs interface insufficiency
diagnosis vs construction failure
later usefulness vs earlier preservation obligation
changed confidence vs changed identifiability
```

Fail if the candidate's proposed result would collapse these distinctions by construction.

## E5 — no v1 reopening is required

Pass iff pursuing the candidate can begin entirely from post-v1 development provenance without changing the interpretation, result, protocol, or scientific state of DSLI_R1.

Any candidate requiring a retroactive v1 rewrite is ineligible.

The eligibility vector is:

\[
E_j=(E1_j,E2_j,E3_j,E4_j,E5_j).
\]

Only candidates satisfying:

\[
\boxed{
E_j=(1,1,1,1,1)
}
\]

enter the comparison stage.

If no candidate is eligible, selection returns:

```text
NO_ELIGIBLE_V2_TARGET
```

and stops without target selection.

---

# 6. Lexicographic development comparison

Each eligible candidate receives a four-coordinate development vector:

\[
\boxed{
C_j=(P_j,I_j,R_j,F_j)
}
\]

with each coordinate in:

```text
0 = LOW
1 = MEDIUM
2 = HIGH
```

All coordinates are defined so that larger is preferred.

The comparison is lexicographic in the exact order:

\[
\boxed{
P
\succ
I
\succ
R
\succ
F.
}
\]

That is, compare `P` first. Only candidates tied on `P` are compared on `I`; only candidates tied on `P,I` are compared on `R`; only candidates tied on `P,I,R` are compared on `F`.

No coordinate tradeoff or compensation is permitted.

---

# 7. `P` — prerequisite leverage

Question:

> If this target were resolved cleanly, how directly would it test or secure an epistemic/interface precondition used by multiple later research directions?

Score from the frozen candidate record:

```text
P = 2 HIGH
  candidate directly tests a representation, challenge channel, or epistemic precondition
  on which multiple other future research operations would depend or whose failure could
  invalidate their interpretation.

P = 1 MEDIUM
  candidate supplies broadly reusable methodological information, but later candidates
  do not materially depend on its successful resolution as a precondition.

P = 0 LOW
  candidate is primarily a local substantive target whose resolution would not test a
  shared epistemic or interface precondition for the other inventory directions.
```

This coordinate does not mean conceptual importance, novelty, or expected truth.

It is specifically about **methodological precedence**.

A candidate may score `P=2` even if it later fails empirically; what matters is whether the question itself tests a shared precondition.

---

# 8. `I` — identification cleanliness

Question:

> How directly can the candidate's central scientific contrast be connected to a bounded defect/result without requiring a large causal or mechanistic inference stack?

```text
I = 2 HIGH
  the frozen candidate record already distinguishes a direct local certificate or typed
  failure object from obvious downstream inference failures; the main empirical claim
  can remain local and diagnostic.

I = 1 MEDIUM
  the candidate can be identified with explicit controls or interventions, but at least
  one substantial causal, temporal, or challenge-independence layer must be established
  before the primary scientific claim is clean.

I = 0 LOW
  the candidate's main proposed conclusion currently depends on multiple unresolved
  causal/mechanistic assumptions whose failure loci are not yet cleanly separable.
```

This coordinate rewards **claim localization**, not expected positive results.

---

# 9. `R` — specification readiness

Question:

> How much unresolved foundational structure must be invented before a confirmatory preregistration can even be written?

```text
R = 2 HIGH
  X_j, O_j, T_A,j and the candidate defect are already structurally differentiated in
  the inventory; remaining work is principally operational freezing, sampling, and
  implementation rather than invention of the scientific object itself.

R = 1 MEDIUM
  the core question is clear, but one major scientific object or identification layer
  still requires substantial development before preregistration.

R = 0 LOW
  multiple coupled foundational objects remain undefined, such that specifying one
  materially determines the meaning of the others and the experiment cannot yet be
  preregistered without additional architecture work.
```

`R` is not a preference for easy experiments. It measures distance to a coherent frozen specification under the current development record.

---

# 10. `F` — fresh-evidence accessibility

Question:

> How cleanly can the candidate obtain new evidence whose construction is separable from the evidence that motivated target selection?

```text
F = 2 HIGH
  fresh/sealed cases, independent reconstructors, interventions, challenge instances,
  or validation support can in principle be generated under a clear anti-leakage boundary.

F = 1 MEDIUM
  fresh evidence is feasible, but depends on stronger external conditions, scarce
  interventions, longer temporal observation, or difficult independence controls.

F = 0 LOW
  the current candidate record does not yet expose a credible route to evidence that is
  independent of the development observations motivating the candidate.
```

This is an evidence-access criterion, not a cost-benefit or convenience score.

---

# 11. Exact selection rule

Let:

\[
\mathcal H_{\rm eligible}
=
\{H_j:E_j=(1,1,1,1,1)\}.
\]

For each eligible candidate, compute:

\[
C_j=(P_j,I_j,R_j,F_j).
\]

The selected target is the unique lexicographic maximum if one exists:

\[
\boxed{
H^*
=
\operatorname{lexmax}_{H_j\in\mathcal H_{\rm eligible}}
(P_j,I_j,R_j,F_j).
}
\]

If exactly one candidate has the maximal vector:

```text
V2_TARGET_SELECTED = true
selected_target = H_j
selection_provenance = DEVELOPMENT_DECISION
```

If two or more candidates have the same maximal vector:

```text
V2_TARGET_SELECTED = false
selection_outcome = NO_UNIQUE_SELECTION
```

No candidate label, inventory order, amount of prose, prior conversational enthusiasm, aesthetic preference, or informal judgment may break an exact tie.

A tie requires a new explicit development decision about how to proceed; it cannot be silently resolved inside the application of this protocol.

---

# 12. Scoring evidence and audit requirement

The later selection artifact must emit one record for every `H_j` containing:

```text
candidate_id
eligibility:
  E1
  E2
  E3
  E4
  E5
eligibility_outcome
P
I
R
F
lexicographic_vector
field-level rationale
inventory_evidence_cited
```

Every gate and coordinate rationale must point to the relevant frozen `D_j` fields.

The selection artifact may not merely emit a winner.

The full four-candidate scorecard is required so that the selection is inspectable and reopenable.

If a score cannot be justified from the frozen inventory record:

```text
SCORE_NOT_IDENTIFIED
```

must be recorded for that coordinate.

`SCORE_NOT_IDENTIFIED` is not `0` and must not be imputed.

Any candidate with `SCORE_NOT_IDENTIFIED` on a comparison coordinate cannot participate in a unique lexicographic selection under this protocol; the operation returns `SELECTION_NOT_IDENTIFIED` unless the unresolved coordinate is provably irrelevant because the candidate has already lost on an earlier lexicographic coordinate.

---

# 13. Anti-selection-leakage rules

The later selection operation is forbidden from using:

```text
candidate name or H-number as priority
amount of inventory prose
earlier informal statements that H1 is leading
new target-specific pilot results
new benchmark outcomes
new external evaluations after this protocol
anticipated publishability
anticipated positive-result probability
anticipated narrative elegance
v1 FC/NR counts as a candidate score
B_star or language winners from v1
post-hoc weighted sums
implicit Pareto rules
unfrozen cost estimates
unfrozen utility estimates
```

In particular:

\[
\boxed{
\text{earlier conversational preference for }H_1
\neq
\text{selection authority}.
}
\]

Only the frozen rule applied to the frozen inventory may select a target.

---

# 14. Separation from v2 design

Even if the next selection operation produces a unique `H^*`, that same operation may not:

```text
freeze X for H*
freeze O for H*
freeze T_A for H*
define a benchmark corpus
define a calibration world
select models/readers/interventions
freeze measurement instruments
freeze success thresholds
construct treatment families
construct repair languages
construct P_keep
define F_d(h,c)
define an active-identifiability estimand
run pilots
access confirmatory target outcomes
create v2 preregistration
authorize v2 execution
```

The state transition is therefore:

\[
\boxed{
\text{frozen inventory}
\rightarrow
\text{frozen selection protocol}
\rightarrow
\text{separate target-selection result}
\rightarrow
\text{separate v2 preregistration}.
}
\]

Selection chooses only **which question receives the next design operation**.

---

# 15. What selection can and cannot mean

A unique selection may establish:

```text
this candidate is the next development target under the frozen selection rule
```

It may not establish:

```text
this candidate is true
this candidate is empirically supported
this candidate is more important in general
this candidate has higher expected scientific value
this candidate is the only valid future direction
other candidates are rejected
other candidates are falsified
other candidates lose DEVELOPMENT_EVIDENCE status
```

Unselected candidates remain in the frozen inventory as unresolved development candidates.

Thus:

\[
\boxed{
\text{not selected now}
\neq
\text{scientifically rejected}.
}
\]

---

# 16. Protocol failure conditions

The later selection operation must stop without selecting a target if any of the following occurs:

```text
inventory anchor mismatch
candidate universe mismatch
candidate record modified
selection protocol modified during scoring
new candidate-specific evidence imported
no eligible candidate
required score not identified and not lexicographically irrelevant
exact tie for maximal lexicographic vector
```

Typed terminal outcomes are:

```text
TARGET_SELECTED
NO_ELIGIBLE_V2_TARGET
NO_UNIQUE_SELECTION
SELECTION_NOT_IDENTIFIED
SELECTION_PROTOCOL_VIOLATION
```

These outcomes are development-decision states, not empirical scientific findings.

---

# 17. Frozen selection-protocol state

This artifact binds:

```text
candidate_universe_frozen                = true
candidate_records_mutable_during_selection = false
selection_rule_frozen                    = true
selection_rule_type                      = eligibility_then_lexicographic
weighted_sum_used                        = false
informal_tiebreak_allowed                = false
post_protocol_candidate_evidence_allowed = false
selection_is_empirical_result            = false
selection_is_v2_design                   = false
v2_target_selected                       = false
v2_preregistration_created               = false
v2_execution_authorized                  = false
```

The central firewall is:

\[
\boxed{
\text{target selection}
\neq
\text{experimental design}
\neq
\text{confirmatory evidence}.
}
\]

---

# 18. Stop condition

After this protocol is committed:

```text
STOP_V2_TARGET_SELECTION_PROTOCOL
```

Do not apply the rule in the same artifact.

Do not select a target in the same artifact.

Do not design v2 in the same artifact.

The next permitted operation is exactly:

\[
\boxed{
\textbf{apply the frozen target-selection protocol to the frozen four-candidate inventory.}
}
\]

The terminal state of this operation remains:

```text
V2_TARGET_SELECTION_PROTOCOL = FROZEN
V2_TARGET_SELECTED           = false
V2_PREREGISTRATION_CREATED   = false
V2_EXECUTION_AUTHORIZED      = false

STOP_V2_TARGET_SELECTION_PROTOCOL
```
