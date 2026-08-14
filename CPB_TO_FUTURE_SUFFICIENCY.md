# From Computational Phase Boundaries to Future Sufficiency

## A newcomer-facing guide to the research lineage

**Status:** conceptual bridge and orientation document.

This document explains the earlier `computational-phase-boundary` (CPB) project, how its central ideas connect to the current Future Sufficiency program, and which connections are established results versus later interpretations or live hypotheses.

It is **not** a claim that the current program is causally derived from CPB in every detail. The defensible claim is narrower:

> CPB treated transformations of search processes as the object of study. Future Sufficiency has increasingly moved one level inward, asking what evidence, inference, planning, authority, and repair structure is required for a search process to recognize and correct insufficiency in its own interfaces.

The result is a recursive research trajectory:

```text
searching a space
    ↓
transforming the search process
    ↓
identifying when the search process is insufficient
    ↓
acquiring evidence about that insufficiency
    ↓
repairing the machinery that acquires and uses evidence
```

---

# 1. What Computational Phase Boundaries was trying to explain

The CPB project starts from a simple observation:

> Large capability transitions are often caused not merely by more resources, but by changes in the process through which possible solutions are represented, explored, evaluated, and constructed.

The core question is therefore not only:

> How much computation is available?

It is:

> How has the geometry of search changed?

CPB models a computational state as:

$$
\Omega_t=(\mathfrak C_t,\alpha_t,g_t,n_t,U_t),
$$

where:

- $\mathfrak C_t$ is the surrounding computational context;
- $\alpha_t$ is accessibility of possible configurations;
- $g_t$ is the effective geometry of the search space;
- $n_t$ is effective searchable dimensionality;
- $U_t$ is the utility structure governing selection.

This already contains an important distinction that remains central in the current program:

$$
\boxed{
\text{a possibility can exist}
\neq
\text{a possibility is effectively accessible}
}
$$

A solution may exist mathematically while remaining practically inaccessible because the system cannot represent it, evaluate it, construct it, afford it, or reach it through the available interface.

---

# 2. Aligned information velocity

CPB's central operational quantity was **aligned information velocity**:

$$
\Lambda_E
=
\frac{
I(H_t;O_t)\,A(U_t\mid O_t,\mathfrak C_t)
}{
T_{\rm iteration}C_{\rm iteration}
}.
$$

The intended decomposition was:

- $I(H;O)$: how much observation reduces uncertainty;
- $A(U\mid O,\mathfrak C)$: whether that information is relevant to the actual decision or objective;
- $T_{\rm iteration}$: time required to obtain feedback;
- $C_{\rm iteration}$: cost required to obtain feedback.

This is important because CPB did **not** equate information with usefulness.

An observation can contain substantial information while being irrelevant to the decision that matters.

That old distinction now reappears much more sharply in Future Sufficiency:

$$
\boxed{
\text{information gain}
\neq
\text{decision relevance}
}
$$

and:

$$
\boxed{
\text{decision-relevant information}
\neq
\text{information worth acquiring at its cost}
}
$$

This is one of the clearest conceptual bridges between CPB and the current decomposition of experiment selection.

---

# 3. Structural transformation: changing search rather than searching harder

CPB distinguishes ordinary resource scaling from a structural transformation of search.

A structural event is represented as:

$$
\chi:(g,n,U)\rightarrow(g',n',U').
$$

The intended idea is that a major transition changes one or more of:

- operational distances between candidate solutions;
- which dimensions can be searched;
- what can be evaluated;
- which abstractions are available;
- how much specification burden remains on the human or external operator.

Examples used in CPB include:

- assembly programming $\rightarrow$ compilers;
- manual derivatives $\rightarrow$ automatic differentiation;
- exhaustive minimax $\rightarrow$ alpha-beta pruning.

The recurring mechanism was summarized as:

$$
\boxed{
\text{complexity carried by the agent}
\rightarrow
\text{complexity absorbed by the interface}
}
$$

The system becomes more capable not simply because it executes more operations, but because the path from intent to useful experiment or solution becomes shorter.

---

# 4. Basin mining versus basin opening

One of CPB's most useful later distinctions emerged under adversarial pressure.

The original framework struggled in regimes where large increases in compute or other resources produced major capability gains without a clean preceding structural signal.

That forced a separation between:

## Basin mining

```text
existing search geometry
+
more resources / better optimization
→
better traversal of an already accessible basin
```

and:

## Basin opening

```text
structural transformation
→
previously inaccessible region becomes reachable
→
new capability regime
```

Formally, the important distinction is:

$$
\boxed{
\text{better navigation inside a fixed search space}
\neq
\text{changing what the search space makes accessible}
}
$$

This distinction has become extremely important for the current program.

---

# 5. The recursive turn: from search transformation to corrigible search transformation

CPB asks:

$$
\boxed{
\text{How does the search process change?}
}
$$

Future Sufficiency asks a more internal question:

$$
\boxed{
\text{What must remain available for a search process to detect and repair insufficiency in its own search machinery?}
}
$$

That creates a layered progression.

## Layer 0 — object search

The system searches over states, solutions, models, designs, or actions.

## Layer 1 — search-process transformation

The system gains a better representation, interface, algorithm, abstraction, or tool that changes the geometry of search.

This is the primary object of CPB.

## Layer 2 — corrigible search-process transformation

The system must determine:

- whether its current representation or evidence interface is insufficient;
- whether the relevant defect is identifiable;
- what additional evidence would discriminate competing possibilities;
- whether acquiring that evidence is worthwhile;
- whether a proposed repair is warranted;
- when to stop revising.

This is increasingly the object of Future Sufficiency.

## Layer 3 — methodological recursion

The research program itself now follows the same pattern:

```text
current dependency model
    ↓
experiment / ablation
    ↓
evidence
    ↓
localize failure
    ↓
revise dependency model
    ↓
choose next discriminating intervention
```

So the research method is being used to study a system that is itself being asked to perform structurally similar corrective operations.

This is **methodological recursion**.

It should not yet be confused with a demonstrated causal claim that every construct in Future Sufficiency was inherited from CPB.

---

# 6. The current Future Sufficiency decomposition

The current program no longer treats “the agent failed” as one undifferentiated outcome.

It separates:

$$
\boxed{
\text{availability}
\rightarrow
\text{identifiability}
\rightarrow
\text{inference}
\rightarrow
\text{active evidence acquisition}
\rightarrow
\text{authorization}
\rightarrow
\text{execution}
}
$$

These are different causal stages.

A failure at one stage must not automatically be blamed on another.

For example:

- if the distinguishing evidence path does not exist, that is an **access failure**;
- if two worlds remain observationally equivalent despite requiring different responses, that is an **identifiability failure**;
- if the distinction is identifiable but the learner fails to recover it, that is an **inference failure**;
- if the correct action is known but not permitted, that is an **authorization boundary**;
- if an authorized correction is not correctly instantiated, that is an **execution failure**.

The foundational guardrail is:

$$
\boxed{
\text{unobserved}
\neq
\text{misused}
}
$$

and more strongly:

$$
\boxed{
O(W_A)=O(W_B)
\land
a_A^\star\neq a_B^\star
\Rightarrow
\text{no policy over }O\text{ can always succeed}
}
$$

That is an epistemic impossibility boundary, not a weak-agent result.

---

# 7. The three current epistemic reference points

The current epistemic branch has three especially useful reference commits.

## `f4f2f33` — epistemic-topology baseline

This audit established a finite minimal admissible evidence-action topology for an evaluator-defined D/R/S decision problem **before introducing learner competence**.

The result was about what must be available for the distinction to be identifiable in principle.

It established:

$$
\boxed{
\text{epistemic sufficiency}
}
$$

not learner intelligence.

## `3166f5b` — epistemic recovery

This audit froze the sufficient topology and introduced only inference.

The learner recovered the full evaluator-defined semantic decision function from anonymized evidence, while ablated interfaces remained bounded by their information-theoretic ceilings.

It established a clean distinction between:

$$
\boxed{
\text{epistemic sufficiency}
\neq
\text{epistemic competence}
}
$$

## `fee56ed` — active evidence acquisition

This audit then asked whether the system could choose which already-admissible anonymous challenge to query under partial evidence.

The important result was not merely successful probe selection.

A one-step value-of-information policy failed because some probes had no immediate decision value yet were necessary to make a later probe useful.

That established:

$$
\boxed{
\operatorname{VOI}_1(a)=0
\not\Rightarrow
\operatorname{VOI}_{1:2}(a)=0
}
$$

and therefore:

$$
\boxed{
\text{active epistemic competence}
\text{ can require planning over information topology}
}
$$

The current narrow claim remains:

> active epistemic competence under a supplied sequential planning contract.

It is not yet a research-agency claim.

---

# 8. Re-reading CPB through the current experiment-selection problem

The current experiment-planning substrate is represented provisionally as:

$$
P_{\rm ep}
=
\{A_{\rm probe},C,V,\Pi,\mathrm{STOP}\}.
$$

But CPB suggests that this should not be treated as a flat list of implementation details.

A more useful functional decomposition is:

$$
\boxed{
\text{access}
\rightarrow
\text{decision relevance}
\rightarrow
\text{valuation}
\rightarrow
\text{pruning/sequencing}
\rightarrow
\text{termination}
}
$$

A tentative mapping is:

| Current implementation | Candidate functional role |
|---|---|
| $A_{\rm probe}$ | experiment accessibility |
| $V$ | decision relevance of information |
| $C$ | acquisition valuation / cost sensitivity |
| $\Pi$ | decision-preserving search control |
| `STOP` | termination discipline |

The key methodological rule is:

$$
\boxed{
\text{present in a successful implementation}
\not\Rightarrow
\text{causally necessary}
}
$$

The next phase therefore asks which of these are genuine dependencies and which are replaceable scaffolding.

---

# 9. Dynamic programming may be implementation, not substrate

`fee56ed` currently uses finite sequential dynamic programming.

But CPB's alpha-beta example suggests a more abstract role.

Alpha-beta pruning improves search by identifying branches that cannot change the final decision and avoiding unnecessary exploration.

That suggests the relevant role of $\Pi$ may be:

$$
\boxed{
\text{preserve every epistemic branch capable of changing the warranted decision; prune the rest}
}
$$

rather than:

$$
\boxed{
\text{use dynamic programming specifically}
}
$$

This motivates a role-preserving substitution test:

$$
do(\Pi_{\rm DP}\leftarrow\Pi_{\rm prune}).
$$

If behavior survives under matched conditions, then dynamic programming itself is not necessary for the declared task/contract.

That would not imply that sequential search control is unnecessary.

It would distinguish:

$$
\boxed{
\text{implementation necessity}
\neq
\text{functional-role necessity}
}
$$

---

# 10. `STOP` may be derived rather than primitive

The same logic applies to termination.

The current active-epistemic system includes `STOP` as a first-class epistemic action.

But termination may be derivable from the remaining decision structure.

For example:

$$
\boxed{
\max_{a\in A_{\rm remaining}}
\left[V_{\rm discrim}(a)-C(a)\right]
\le 0
\Rightarrow
\text{terminate}
}
$$

or from a stronger dominance condition:

$$
\boxed{
\text{no remaining branch can alter the warranted terminal decision}
\Rightarrow
\text{terminate}
}
$$

If such a rule reproduces the same behavior, then an explicit `STOP` primitive may be unnecessary even if **termination discipline itself remains necessary**.

Again:

$$
\boxed{
\text{explicit stop vocabulary}
\neq
\text{termination discipline}
}
$$

---

# 11. CPB's strongest warning for future probe-generation work: where did the complexity go?

Eventually the program will attack the supplied probe menu itself.

The tempting move would be:

```text
remove fixed probe menu
→
provide experiment grammar
→
let system generate probes
```

But this can produce a false result.

If the designer simply encodes the same useful experiment structure in a richer grammar, the scaffold has moved rather than disappeared.

CPB's old “complexity absorption” criterion gives the right safeguard:

$$
\boxed{
\text{Where did the experiment-specification complexity go?}
}
$$

A useful accounting object is something like:

$$
B_{\rm spec}
=
L(\text{designer-supplied information required for successful experiment generation}).
$$

This need not be literal Kolmogorov complexity. It can be operationalized finitely.

The scientific question is whether external specification burden actually decreases while useful experiment coverage remains.

What would count as progress is closer to:

$$
\boxed{
B_{\rm external}\downarrow
\land
\text{decision-relevant experiment accessibility preserved or increased}
}
$$

not merely:

$$
\boxed{
\text{explicit menu removed}
}
$$

---

# 12. Epistemic basin mining versus epistemic basin opening

This is the strongest conceptual bridge from CPB to the current research-agency frontier.

## Epistemic basin mining

The system is given an experiment space and becomes better at navigating it:

$$
\boxed{
A_{t+1}=A_t,
\qquad
\pi_t:A_t\rightarrow\text{better choice}
}
$$

This is approximately what `fee56ed` demonstrates.

It selects well within an already supplied admissible experiment set.

## Epistemic basin opening

The system changes what experiments are effectively accessible:

$$
\boxed{
\alpha_E(a\mid h,t+1)
>
\alpha_E(a\mid h,t)
}
$$

for a useful experiment that was previously unavailable, unrepresentable, unconstructible, or unevaluable.

The important criterion is not surface novelty.

It is:

$$
\boxed{
\text{a previously inaccessible decision-relevant intervention becomes constructible and evaluable by the system}
}
$$

That gives a much sharper research-agency boundary:

$$
\boxed{
\text{select among supplied experiments}
\neq
\text{transform the geometry of the experiment space}
}
$$

or, in CPB language:

$$
\boxed{
\text{epistemic basin mining}
\neq
\text{epistemic basin opening}
}
$$

---

# 13. The current minimality program

The project is now progressively identifying minimal substrate at different causal stages.

## Evidence topology

$$
\mathfrak E_{\min}
$$

asks:

> What must reality make accessible before the required distinction is identifiable?

## Experiment-selection substrate

$$
\mathfrak P_{\rm ep,min}
$$

asks:

> What minimal structure is required to discover relevance, value experiments, sequence them, and terminate acquisition correctly?

## Repair substrate

$$
\mathfrak R_{\min}
$$

asks:

> Once a warranted distinction is identified, what machinery is required to construct and persist the correction?

The governing rule is:

$$
\boxed{
\text{one supplied assumption}
\rightarrow
\text{one intervention}
\rightarrow
\text{one preregistered localized failure signature}
\rightarrow
\text{one update to the dependency graph}
}
$$

The goal is not to build a progressively stronger agent.

It is to determine which pieces of the successful system are actually necessary.

---

# 14. What the cross-repo connection does — and does not — establish

The connection between CPB and Future Sufficiency is strong at the level of research structure.

CPB contributes:

- search geometry as an object;
- accessibility rather than mathematical existence alone;
- information gain separated from utility alignment;
- iteration cost as part of search efficiency;
- structural transformation rather than raw scaling;
- complexity absorption into interfaces;
- basin opening versus basin mining.

Future Sufficiency decomposes these broad ideas into more explicit causal stages:

- evidence access;
- identifiability;
- inference;
- active evidence acquisition;
- authorization;
- repair;
- persistence;
- reopenability;
- termination.

A defensible summary is therefore:

$$
\boxed{
\text{CPB studies transformations of search geometry}
}
$$

while:

$$
\boxed{
\text{Future Sufficiency studies the conditions under which transformations of search geometry can be detected, justified, and corrected without losing future corrective capacity}
}
$$

What is **not yet established** is a strict causal lineage claim that the later framework depends on specific earlier CPB constructs.

That would require a separate lineage analysis across commit history, concept emergence, abandoned branches, and direct inheritance.

For now the safer relation is:

$$
\boxed{
\text{CPB}
\rightsquigarrow
\text{search transformation as object}
\rightsquigarrow
\text{corrigible search transformation as current research frontier}
}
$$

where $\rightsquigarrow$ denotes conceptual/historical continuity rather than an experimentally established causal arrow.

---

# 15. Current frontier

The current frontier is **not** “build a better planner.”

It is:

$$
\boxed{
\textbf{What minimal structure is required for an agent to discover, value, sequence, and terminate its own experiments?}
}
$$

The provisional experiment-planning substrate is:

$$
P_{\rm ep}
=
\{A_{\rm probe},C,V,\Pi,\mathrm{STOP}\},
$$

but each element is now treated as a hypothesis under attack.

Near-term tests should ask whether:

- $\Pi_{\rm DP}$ can be replaced by a weaker decision-preserving pruning mechanism;
- `STOP` can be derived from dominance/exhaustion rather than supplied as a primitive;
- experiment relevance can be learned rather than encoded in a fixed probe menu;
- cost and value semantics can be inferred rather than supplied;
- removal of explicit experiment menus genuinely reduces external specification burden rather than relocating it into hidden grammar.

Only after this substrate is decomposed should the program ask whether the system can **construct a genuinely new experiment space**.

That is the prospective transition from:

$$
\boxed{
\text{active epistemic competence}
}
$$

to:

$$
\boxed{
\text{research agency}
}
$$

and the criterion should be structural:

> Did the system merely get better at choosing from a supplied experiment space, or did it change which decision-relevant experiments were accessible at all?

---

# 16. One-paragraph summary

`computational-phase-boundary` proposed that major computational transitions occur when systems change the mechanisms through which possibilities are searched, evaluated, and made accessible. Future Sufficiency has pushed that question inward. It separates whether corrective evidence exists, whether the necessary distinction is identifiable, whether a learner can recover it, whether the system can actively acquire missing evidence, whether a change is authorized, and whether a repair can be executed and preserved. The strongest cross-repo bridge is CPB's distinction between **basin mining** and **basin opening**: the current active-epistemic system can navigate a supplied experiment space, while the eventual research-agency boundary concerns changing what experiments are accessible in the first place. The current scientific program is therefore not to build a stronger agent, but to identify the minimal causal substrate required at each stage and to track where designer-supplied complexity goes when that scaffold is removed.

---

## Source repositories

- Computational Phase Boundaries: `https://github.com/bjoern-janson/computational-phase-boundary`
- Future Sufficiency: `https://github.com/bjoern-janson/future-sufficiency`
