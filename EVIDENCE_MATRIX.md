# Evidence Matrix — Future Sufficiency / Recursive Repair

Status: consolidated through `001`–`008` and the post-008 audit sequence.

This document is a checkpoint, not a new experiment or audit.

The governing question is no longer:

    can the next toy be made to work?

It is:

    what minimum structure must be supplied before future-sensitive repair appears?

## Interpretation rule

Each row separates four things:

1. the narrow claim actually earned;
2. the strongest positive evidence;
3. the strongest surviving scaffold / alternative explanation;
4. the next discriminant that would reduce that scaffold.

A later row does not retroactively strengthen an earlier claim beyond its controls.

## Experiments 001–008

| ID | Claim actually earned | Strongest positive evidence | Surviving scaffold / live alternative | Next discriminant |
|---|---|---|---|---|
| **001 — future-sufficiency arena** | Closure defect can predict the value of targeted information in a deterministic positive control. | `p_target_gamma_1=1`, `p_target_gamma_0=0`; targeted VOI positive while generic VOI is negative; shuffled-Γ gap ≈ 0. | The defect regime is effectively trackable from visible context; no latent diagnosis or persistent repair. | Make Γ latent and require information demand to be inferred from experience. |
| **002 — latent aliasing** | Experienced future inconsistency can induce selective information demand without exposing Γ. | Divergent + cost<VOI → target probe 1.0; divergent + cost>VOI → 0; aligned and misleading → 0; shuffled Γ gap ≈ 0. | Targeted probe mechanism is supplied; no persistent change to representation. | Convert acquired evidence into a reusable representation change. |
| **003 — repair transfer** | Probe evidence can cause a persistent representation split that removes the need for later probing. | Held-out probe rate 0; repaired transfer 1.0 vs nuisance control ≈ .507 and unrepaired ≈ .497; equal binary capacity. | The useful raw candidate feature already exists and is selected/promoted. | Construct a useful distinction compositionally rather than select a supplied feature. |
| **004 — compositional repair** | A useful distinction can be synthesized compositionally inside a fixed grammar and reused on unseen raw configurations. | Learns `xor(b3,b12)`; held-out transfer 1.0; equal-complexity shuffled-label control ≈ .486; constituent bits ≈ .514; raw overlap 0. | Grammar `{ATOM,XOR,AND,OR}` is designer-supplied. | Separate exhaustive search failure from representation-language insufficiency. |
| **005 — representation-language repair** | A learner can diagnose finite language insufficiency and selectively expand a representation language when expansion value exceeds cost. | Exhaustive `G0` ceiling .5 on insufficient task; `G0+XOR3` = 1.0; cheap insufficiency expands, expensive insufficiency does not, sufficient case does not. | One-step extension menu is supplied. | Synthesize and promote a reusable operator absent from the extension menu. |
| **006 — operator invention** | A program synthesized from low-level primitives can be promoted into a reusable operator and reused beyond the task that produced it. | Invented primitive program transfers at 1.0; fixed language ≈ .753; invention is cost-sensitive; pooled tasks identify reusable operator where individual tasks are underdetermined. | Primitive algebra and macro-promotion mechanism are supplied. | Repair the rules that generate representations rather than only add an operator. |
| **007 — primitive meta-language repair** | A persistent generator rule can be changed, and the changed generator can solve a different relation without another repair. | Read-once majority ceiling .875 → repaired 1.0; repaired generator later synthesizes XOR at 1.0 vs fixed `M0` ≈ .757; cost-sensitive and sufficient-case selective. | The semantic repair `allow fan-out` is supplied. | Synthesize the construction rule rather than activate a named rule. |
| **008 — meta-rule invention** | A rule governing admissible constructions can be synthesized inside a supplied meta-language and reused across unrelated targets. | Synthesizes `not(hi)`; majority, XOR and MUX reach 1.0 after rule persistence; base generator stays at its finite ceilings; zero-value/sufficient cases do not mutate. | Structural state bits and the rule-construction meta-language are supplied; occurrence-limit semantics remain latent in the design. | Turn the method back on itself: capability recursion vs scaffold relocation. |

## Post-008 adversarial audits

| Audit | Claim actually earned | Strongest positive evidence | Surviving scaffold / live alternative | Next discriminant |
|---|---|---|---|---|
| **Recursive Capability Audit** | The 008 repair process survives literal ontology permutation, a different structural defect family, complete finite-target transfer, a matched fixed-generator contrast, and a high-error/no-defect null. | 24/24 ontology permutations; new syntax-depth family repaired; all 256 3-bit targets evaluated with 38 improved / 32 newly exact / 0 degraded; noisy null retains ≈25% error with VOI=0 and no repair. | Both occurrence and depth cases can still be described as generic structural limit relaxation. | Create equal-error cases requiring non-equivalent repairs, including a no-repair case. |
| **Anti-Limit-Relaxation Audit** | Repair identity depends on failure structure rather than error magnitude or a generic scalar-capacity increase. | Three cases all start at error .125 but require `reuse`, `operator_family`, and `keep`; scalar occurrence/node relaxations fail the operator-family case; measured mutable/fixed resource snapshots match. | The available repair axes are still designer-supplied. | Remove named repair axes and require the useful repair dimension to be synthesized. |
| **Repair-Axis Discovery Audit** | A latent repair dimension can be synthesized from anonymous structural descriptors instead of selected from named axes. | 12/12 sampled hidden axes recovered; evaluator-only completeness 24/24; held-out transfer 1.0 vs fixed literal-axis baseline .875; null does not bind; exact resource matching. | Descriptor vocabulary and predicate-construction language are supplied. | Remove semantic descriptor basis and ask what information is actually necessary for repair discovery. |
| **Minimal Repair Substrate Audit** | A semantic descriptor basis is unnecessary: relational history plus repair consequences can induce a reusable repair abstraction over opaque state IDs. | Across 1024 trials, full substrate exact recovery and held-out transfer = 1.0; outcomes-only ≈ .077 exact, history-only .125 exact, shuffled history ≈ .078 exact; `R(π(s))=π(R(s))`; zero-VOI null does not bind. | Designer still supplies a relation-bearing substrate, a relational-coherence bias, and fixed repair-scope size 4. | Make repair cardinality unknown. |
| **Repair-Unit Granularity Audit** | The learner can infer both repair membership and repair cardinality from relations plus consequences. | True sizes 2,3,4,5 all recovered exactly across 64 encodings; fixed-`|R|=4` exact only on size-4 cases; ablations fail; null does not bind; matched resources. | Repair is still assumed to be a relation-closed subset of states. | Ask why the repair object should be a subset at all. |
| **Representation Ontology Selection Audit** | Future consequences can select what *kind* of supplied representational object should carry repair. | Six equal-error cases require subset, edge relation, partition, predicate, operator, temporal motif; ontology-selecting condition correct 6/6 with held-out pattern accuracy 1.0; fixed-subset exact only 1/6; null does not mutate. | The six ontology-generating families are enumerated by the designer. | Remove the ontology-family menu and require reusable constructor synthesis. |
| **Ontology Construction Audit** | A reusable higher-order representation constructor absent from the online ontology can be synthesized from a lower-level object algebra, persisted, and instantiated on unseen primitive objects. | Hidden constructor `x & ~(y | z)` is outside `O0`; Task A has 2 perfect compatible constructors, Task B 4, pooled A+B exactly 1; transfer uses three relation identities unseen during induction; across 32 encodings mutable transfer 1.0 vs fixed-`O0` .875; positive representational gain with zero validated future consequence does not bind. | Sort, constructor signature `(set,set,set)->set`, primitive `NOT/AND/OR` algebra, and bounded synthesis mechanism are still supplied. Competing description: increasingly expressive symbolic macro synthesis. | Cross-substrate mechanism-transfer audit: vary sort, arity, primitive algebra and composition semantics while preserving only the abstract reusable-repair problem. |

## Supplied-structure ledger

This ledger tracks which designer assumptions have been removed and which remain live.

| Supplied structure | Status | First serious removal / attack |
|---|---|---|
| Visible defect/regime cue | **Removed** | 002 — defect value inferred from history rather than Γ exposure. |
| Useful feature identity | **Removed** | 004 — composition synthesized from raw dimensions. |
| Fixed representation grammar sufficiency | **Removed** | 005 — finite language insufficiency diagnosed. |
| Named operator extension | **Removed** | 006 — operator synthesized and promoted. |
| Named generator repair rule | **Removed** | 008 — construction rule synthesized. |
| Literal structural ontology | **Substantially weakened** | Recursive-capability ontology permutations and cross-encoding audits. |
| Scalar limit as repair form | **Substantially weakened** | Anti-limit-relaxation audit. |
| Named repair axis | **Removed** | Repair-axis discovery audit. |
| Semantic descriptor basis | **Removed** | Minimal repair substrate audit. |
| Fixed repair cardinality | **Removed** | Repair-unit granularity audit. |
| Fixed repair object ontology | **Removed** | Representation ontology selection audit. |
| Enumerated ontology-family menu | **Removed** | Ontology construction audit. |
| Relation-bearing experience substrate | **Still supplied** | Live scaffold. |
| Low-level object algebra | **Still supplied** | Live scaffold. |
| Constructor input/output sort | **Still supplied** | Live scaffold. |
| Constructor arity/signature | **Still supplied** | Live scaffold. |
| Program-synthesis mechanism and finite bounds | **Still supplied** | Live scaffold. |
| High verifiability / mechanically checkable feedback | **Still supplied** | Major external-validity boundary. |
| Correctness/repair-value proxy itself | **Still supplied** | Major alignment / AI-R&D boundary. |

## Current strongest defensible claim

The strongest statement supported by the current sequence is:

> In finite, highly verifiable environments, future consequences can drive value-gated persistent repair across progressively less designer-specified representational levels, culminating in synthesis and reuse of a higher-order constructor on unseen primitive objects.

Equivalently:

    future discrepancy
    -> consequence-bearing evidence
    -> representation / generator / ontology repair
    -> persistent capability
    -> held-out transfer

with the important authority constraint:

    discoverable improvement != warranted persistent modification

because positive representational gain with zero validated future value does not acquire binding authority.

## Claims not yet earned

The current evidence does **not** establish:

- general recursive capability;
- unbounded self-modification;
- unrestricted mathematical type or ontology invention;
- transfer of the repair strategy across substantially different computational substrates;
- robust research taste or judgment in weakly verifiable settings;
- reliable detection that a locally verifiable optimization loop is pursuing a future-insufficient proxy;
- authority to modify goals or governing constraints.

The governance boundary remains:

    capability expansion != authority expansion
    meta-capability expansion != goal expansion

## Minimal-substrate objective

`S_min` is **not** a universal substrate. Minimality is relative to a task family and a preregistered repair contract:

    S_min(T, P)

where:

- `T` is the task distribution / task family under study;
- `P` is the preregistered set of future-sufficiency properties that the repair process must retain.

The empirical object is therefore an intervention on supplied structure:

    S --remove s_i--> S^{-i} --> Delta R_i

where `Delta R_i` is not merely a performance change. It is a localized change in one or more repair functions, such as:

- discovery;
- authorization;
- persistent binding;
- held-out transfer;
- reopenability;
- termination discipline.

The resulting object is a dependency map:

    G_repair = Dep(R | T, P)

A supplied assumption `s_i` is **not necessary** for the chosen `(T, P)` contract when:

    R(S \ {s_i}) still satisfies P on T.

A supplied assumption `s_i` is **necessary** when its removal produces a preregistered, localized failure signature for at least one property in `P`.

Minimality should be understood with respect to a declared partial order over substrates, not as a claim that there is one globally smallest representation system.

## Minimality certificate

The strongest eventual result is not another capability demo but a minimality certificate:

    S_min(T, P)
    +
    for every s_i in S_min,
    removal(s_i) produces a non-zero localized repair failure.

A valid certificate should contain, for every retained assumption:

1. the exact intervention removing or weakening it;
2. the preregistered repair property expected to fail;
3. the observed failure signature;
4. matched controls showing the failure is not due to incidental loss of compute, probes, memory or storage;
5. the narrow necessity claim earned by that result;
6. whether the assumption is empirically necessary or constitutive of the problem definition.

This turns the project trajectory into:

    capability accumulation
    -> dependency identification
    -> minimal substrate certificate.

The stopping rule is reached when each remaining supplied assumption is either:

- empirically necessary for the declared `(T, P)` repair contract; or
- constitutive of the problem definition, such that removing it makes the target property undefined rather than falsified.

## Immediate empirical obligation

The next phase is **dependency identification**, not another rung.

Use the operating rule:

    one supplied assumption
    -> one intervention
    -> one preregistered failure signature
    -> minimal revision of the substrate hypothesis.

The first high-value discriminant remains mechanism transfer across substrates, but it should now be treated as one dependency intervention rather than as a new capability level.

Hold fixed only the abstract requirement:

    discover a reusable transformation whose value is shared across tasks

while varying at least:

    sort
    arity
    primitive algebra
    composition semantics

A positive result would weaken the necessity of the current symbolic substrate and support mechanism transfer rather than merely program synthesis inside one carefully designed formalism. A negative result should be localized to the shallowest substrate dependency that explains the failure.

An orthogonal downstream bridge to AI-R&D remains:

    can future-sufficiency detect when a highly verifiable improvement loop is optimizing a future-insufficient proxy?

That should remain separate from substrate-generalization tests so that failures remain diagnostically interpretable.

**Scientific rule:** empirical obligation > further abstraction.
