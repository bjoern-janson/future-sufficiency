# Dependency Hypotheses — Future Sufficiency

Status: methodological dependency ledger through the Active Evidence Acquisition Audit (`fee56ed`).

This file records candidate substrate dependencies to be attacked. Entries are hypotheses, not definitional requirements.

## Frozen reference baselines

The current program has three distinct methodological reference points:

    a47e534  repair-substrate baseline
    f4f2f33  epistemic-topology baseline
    fee56ed  active-evidence baseline

They serve different purposes and should not be collapsed.

- `a47e534` marks the transition from capability accumulation toward dependency identification and minimal-substrate analysis on the repair side.
- `f4f2f33` establishes a finite minimal admissible evidence-action topology for the evaluator-defined D/R/S distinction before learner competence is tested.
- `fee56ed` establishes active epistemic competence relative to a supplied sequential planning contract while preserving the upstream evidence topology and keeping repair authority absent.

None is Experiment 009. The 001–008 capability ladder remains frozen.

## Evidence hierarchy checkpoint

The empirical sequence now separates two branches.

Repair-side progression:

    repair
    -> meta-repair
    -> repair-axis discovery
    -> representation-substrate discovery
    -> repair-unit granularity
    -> ontology selection
    -> ontology construction
    -> loop-level diagnosis (D / R / S)

Epistemic-side progression:

    availability
    -> identifiability
    -> inference
    -> active evidence acquisition

with the reference commits:

    f4f2f33  topology sufficient in principle
    3166f5b  decision partition recovered by a bounded learner
    fee56ed  useful admissible evidence action selected sequentially

The active-evidence result is narrow:

> Under the frozen finite admissible evidence topology, an already-recovered D/R/S semantic function, and a supplied sequential decision-value planner, the loop can select semantically anonymous probes that optimally resolve its current decision ambiguity and stop when further probing is not warranted.

This is active epistemic competence under a supplied planning contract, not general research agency.

## Foundational epistemic guardrail

Keep the following distinction explicit:

    unobserved != misused

and more strongly:

    O(W_A) = O(W_B)
    and
    required_action(W_A) != required_action(W_B)
    ->
    no policy over O alone can always succeed.

This is an identifiability boundary, not an inference failure.

The dependency program therefore distinguishes:

    G_epistemic != G_repair

where `G_epistemic` asks whether the relevant correction-triggering distinction is available and identifiable, and `G_repair` asks whether the system can exploit an identified distinction to construct, authorize and persist a correction.

## Current live scaffold after active evidence acquisition

The active epistemic audit still supplies:

- the finite admissible probe set;
- the four-channel finite evidence family;
- the evaluator-defined D/R/S decision contract;
- the already-recovered inference function / inference language;
- the probe cost model;
- the decision-correctness value scale;
- the prior over compatible completions;
- the sequential planning algorithm and finite horizon induced by the remaining probe set;
- probe authorization/admissibility itself;
- a finite, mechanically verifiable environment.

These assumptions must be classified as one of:

1. empirically necessary for a declared task/contract;
2. removable implementation contingency;
3. constitutive of the problem definition.

## Candidate dependency: independent challengeability

Notation:

    E_challenge
        = an external or sufficiently independent evidence path capable of
          exposing a discrepancy that the current hypothesis language cannot
          make visible from its ordinary evidence stream.

Candidate hypothesis:

> **Independent challengeability may be a necessary substrate for future-sufficient hypothesis repair.**

The motivation is an identifiability limit.

If:

    H* not in H_t

but every evidence channel available to the loop is generated, filtered, or interpreted through the same insufficient hypothesis language, then:

    "the current language is adequate"

and:

    "the current language is inadequate but the inadequacy is observationally invisible"

may be indistinguishable to the loop.

Formally, if:

    O_H(W_A) = O_H(W_B)

while:

    adequate(H_t, W_A) != adequate(H_t, W_B),

then no decision rule over `O_H` alone can reliably choose different meta-actions in the two worlds.

That is epistemic non-identifiability, not failed optimization inside the loop.

### Constitutive versus empirical status

Do not declare `E_challenge` necessary merely because successful audits supply it.

Two possibilities remain live.

Empirical necessity:

    remove/degrade challengeability
    -> target distinction remains meaningful
    -> diagnosis/reopening selectively fails.

Constitutive limit:

    remove all admissible challenge information
    -> worlds requiring different responses become observationally equivalent
    -> the target distinction itself becomes unidentifiable.

The latter is an impossibility boundary, not a failed learner.

## Candidate dependency: experiment-planning substrate

Notation:

    P_ep
        = the supplied substrate that defines which epistemic actions are
          considered, how their future decision consequences are evaluated,
          and when information acquisition should terminate.

In `fee56ed`, `P_ep` currently includes at least:

- the admissible active probe set `A_probe`;
- probe costs `C(a)`;
- the decision-value scale used to compare stopping with probing;
- a prior / weighting over compatible latent completions;
- the sequential planning recursion over remaining admissible probes;
- `STOP` as a first-class epistemic action.

Candidate hypothesis:

> **Active epistemic competence may depend on a supplied experiment-planning substrate even when the evidence topology and inference function are already adequate.**

The current result does not establish that this substrate is necessary, nor which parts of it are necessary.

The next dependency question is not:

    can a stronger planner solve the same toy?

It is:

    which parts of P_ep can be removed, learned, inferred, or replaced
    without destroying decision-directed evidence acquisition?

In particular, future tests should distinguish:

    supplied candidate experiment set
    !=
    learned experiment relevance

    supplied probe cost/value semantics
    !=
    learned experiment utility

    supplied sequential planner
    !=
    learned experiment-selection structure

    experiment worth considering
    !=
    experiment authorized to execute.

Do not add `P_ep` to a minimal causal core from the active-evidence result alone.

## Myopic planning failure

The Active Evidence Acquisition Audit exposed a structural failure of one-step value-of-information selection.

A probe can have zero immediate decision value while still being necessary to unlock a later probe with positive decision value:

    VOI_1(a) = 0
    does not imply
    VOI_1:2(a) = 0.

This means active epistemic competence in the current finite setting is not reducible to:

    choose the probe with the largest immediate information gain

or:

    choose the probe with the largest immediate decision-accuracy gain.

The relevant object is sequential structure over the evidence-action topology.

This is evidence about the inadequacy of a myopic policy class. It is **not** yet evidence that the particular dynamic-programming planner used in `fee56ed` is necessary.

## Information gain versus decision-directed information gain

The active audit also preserves:

    I(W; E_a) > 0
    does not imply
    decision_value(a) > 0.

At the key residual-positive control, the admissible probes have equal outcome entropy while only one is decision-optimal under the supplied planning contract.

Therefore:

    information gain != decision-directed information gain.

This distinction should remain a permanent control in future experiment-selection work.

## STOP as a first-class epistemic action

The active epistemic action set is conceptually:

    A_epistemic = {probe_1, ..., probe_m, STOP}.

This matters because:

    reopenability != keep probing forever.

The desired behavior is:

    probe while warranted
    -> resolve the decision-relevant ambiguity
    -> stop when marginal warranted value disappears.

Thus termination discipline is now operationalized inside the evidence-acquisition layer itself, before any repair or self-modification occurs.

This does not establish `T_stop` as universally necessary; it provides a clean place to test its necessity.

## Edge acquisition rule

Neither `E_challenge` nor `P_ep` belongs in the minimal causal core merely because it is supplied in a successful audit.

A dependency edge requires:

    intervention on supplied structure
    -> preregistered localized failure
    -> replication
    -> matched controls
    -> rule out incidental information / compute / search-volume loss
    -> classify empirical necessity vs constitutive non-identifiability.

In particular:

    supplied in a successful audit
    !=
    causally necessary.

And:

    failed under a weaker planner
    !=
    this particular stronger planner is necessary.

## Relation to the current candidate core

The current loop-level dependency hypotheses remain under attack:

    E_rel        relational evidence
    C_future     future consequence signal
    A_value      value-sensitive authorization
    M_persist    persistent state change
    Q_reopen     reopenability
    T_stop       termination discipline
    E_challenge  independent challengeability
    P_ep         experiment-planning substrate

This is not a flat ontology and not a frozen causal ordering.

A plausible but unearned distinction is:

    upstream epistemic substrate
    -> identifiable correction-relevant distinctions
    -> downstream repair machinery.

Whether `E_challenge`, `E_rel`, `C_future`, and `P_ep` are serial, parallel, substitutable, or partially reducible remains empirical.

## Current scientific question

The next high-level dependency question is:

> **Can the loop learn which experiments are worth considering, rather than receiving the admissible probe set and experiment-planning semantics in advance?**

This is the boundary between:

    active epistemic competence

and:

    research agency.

The immediate methodological objective is to attack one supplied component of `P_ep` at a time, not to add another capability rung.

High-value candidate interventions include:

- enlarge the admissible action universe with irrelevant/dominated candidate probes and require the system to infer which are decision-relevant;
- hide or vary probe consequence structure while matching raw information gain;
- vary cost/value tradeoffs without changing the evidence topology;
- compare myopic, sequential, learned and misspecified planning substrates under matched resources;
- preserve challenge authorization as a separate gate from identifying which challenge would be useful.

No such next audit is frozen by this ledger entry.

## Scientific rules

**Do not confuse absence of corrective evidence with failure to use corrective evidence.**

**Do not confuse information gain with decision-directed information gain.**

**Do not confuse identifying a useful experiment with authority to perform it.**

**Do not confuse reopenability with nontermination.**
