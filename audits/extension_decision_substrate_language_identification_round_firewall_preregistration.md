# Decision-Substrate Language Identification — Round Firewall Amendment

## Status

This document is a **semantic architecture amendment** to the decision-substrate language-identification architecture frozen at:

```text
fe21bbe2cd48bd71011674edd16488b5a492f291
```

with the non-semantic serialization erratum at:

```text
9ee1fd5f49f2dc43889894b9617ea9333077dd05
```

It closes one remaining adaptive-calibration loophole **before any concrete decision-substrate language is specified**.

The governing invariant added here is:

\[
\boxed{\textbf{
Calibration characterizes a frozen language; it does not construct or repair it.
}}
\]

and its companion:

\[
\boxed{\textbf{
Evidence may motivate a new language version, but cannot validate within the same round the modifications it motivated.
}}
\]

No concrete language, grammar, primitive, dimensionality, parameter domain, calibration relation, or actual-target application is introduced here.

---

# 1. Precedence and scope of amendment

The parent architecture remains binding except where this amendment explicitly tightens its round semantics.

In particular, this amendment **supersedes only** the parent-architecture clauses in Sections 21–22 that allowed anonymous calibration evidence to revise candidate languages before a later final-language freeze.

The superseded behavior was:

```text
frozen architecture
-> language specification
-> calibration
-> within-round language revision permitted
-> final language freeze
```

The binding behavior is now:

```text
frozen architecture
-> frozen round specification
-> calibration characterization
-> no within-round language modification
```

Any calibration-motivated modification creates a **new version and a new scientific round**.

All parent definitions of unrestricted closure, admissible closure, witness-level authority, witness-specific burden, closure certification, burden minimization, four-state outcomes, nuisance invariance, pair-swap symmetry, actual-target exclusion, and anti-scaffold accounting remain unchanged.

---

# 2. Round-indexed object

A decision-substrate identification round is indexed by version `v`.

Before calibration execution, the round must freeze the complete tuple:

\[
\boxed{
\mathcal R^{(v)}
=
\left(
\mathfrak L_{\rm DS}^{(v)},
\mathfrak K_{\rm cal}^{(v)},
A_{\rm DS}^{(v)},
B_{\rm DS}^{(v)},
\Pi_{\rm closure}^{(v)},
\Sigma_{\rm outcome}^{(v)}
\right).
}
\]

The six objects retain the parent architecture meanings.

The calibration generator is not a seventh architecture object. It is a binding component of:

\[
\boxed{\mathfrak K_{\rm cal}^{(v)}}.
\]

Accordingly, the round-specific calibration object must freeze, before execution, at minimum:

```text
structural-axis value sets
relation generators
matched-discriminant construction rules
candidate-count domains
relation enumeration/sampling rules
random/deterministic seeds where applicable
calibration panel cardinality or exact generation rule
nuisance-encoding construction
control-relation generators
structural certificates retained from generators
```

Changing any of these after observing round outcomes is a round modification and therefore requires `v -> v+1`.

---

# 3. Concrete language-family freeze occurs before calibration

For round `v`:

\[
\boxed{
\mathfrak L_{\rm DS}^{(v)}
=
\{\mathcal L_1^{(v)},\ldots,\mathcal L_m^{(v)}\}
}
\]

must be frozen before any round-`v` calibration result is observed.

Every language is frozen with the complete parent-architecture schema:

\[
\boxed{
\mathcal L
=
(\Sigma_{\mathcal L},
\mathcal G_{\mathcal L},
\llbracket\cdot\rrbracket_{\mathcal L},
A_{\mathcal L},
B_{\mathcal L},
\Pi_{\mathcal L}).
}
\]

Within round `v`, calibration outcomes may not alter any of:

```text
Sigma_L
G_L
[[.]]_L
A_L
B_L
Pi_L
language membership in the frozen round family
parameter domains
primitive inventory
number or type of dimensions
exception mechanisms
selector mechanisms
closure decision procedure
burden ledger
admissibility predicate
```

Thus:

\[
\boxed{
\text{calibration}^{(v)}
\not\longrightarrow
\text{within-round language modification}.
}
\]

---

# 4. Specification-outcome firewall

Let:

\[
\mathcal Y_{\rm cal}^{(v)}
\]

denote the complete observed calibration outcomes from round `v`.

For specification purposes, the binding firewall is written:

\[
\boxed{
\mathfrak L_{\rm DS}^{(v)}
\perp
\mathcal Y_{\rm cal}^{(v)}.
}
\]

Here `perp` is **not** a probabilistic-independence claim.

It means only:

> the defining specification of the already-frozen round-`v` language family is invariant to the subsequently observed round-`v` calibration outcomes.

The permitted arrow is:

\[
\boxed{
\mathfrak L_{\rm DS}^{(v)}
\longrightarrow
\mathcal Y_{\rm cal}^{(v)}.
}
\]

The forbidden within-round arrow is:

\[
\boxed{
\mathcal Y_{\rm cal}^{(v)}
\not\longrightarrow
\mathfrak L_{\rm DS}^{(v)}.
}
\]

This firewall applies equally to the frozen calibration generator and the other round objects:

\[
\boxed{
\mathcal Y_{\rm cal}^{(v)}
\not\longrightarrow
\mathcal R^{(v)}.
}
\]

---

# 5. Identification target

The language is supplied by design.

The object identified by calibration is its response over the frozen structural calibration domain.

Define:

\[
\boxed{
\Phi_{\mathfrak L^{(v)}}(K)
=
\left\{
\operatorname{Rep}_{\mathcal L}(R),
\operatorname{Rep}^{A}_{\mathcal L}(R),
B_{\mathcal L}^{*}(R),
\Sigma_{\rm outcome}(R,\mathcal L)
\right\}_{\mathcal L\in\mathfrak L_{\rm DS}^{(v)}}
}
\]

for calibration relations `R` generated under structural descriptor `K`.

The four-state terminal status remains a derived classifier:

\[
\boxed{
\Sigma_{\rm outcome}
=
f\!\left(
\operatorname{Rep}_{\mathcal L},
\operatorname{Rep}^{A}_{\mathcal L},
B_{\mathcal L}^{*},
B_R
\right).
}
\]

Calibration therefore identifies/characterizes:

```text
unrestricted closure membership
admissible closure membership
authority-invalid exact representation when present
minimum admissible exact-witness burden when defined
terminal four-state status
matched structural boundary changes
```

Calibration does **not** identify which grammar should be invented next.

---

# 6. Characterization is not development

The two operations are frozen as distinct:

\[
\boxed{
\text{CHARACTERIZATION}
\neq
\text{DEVELOPMENT}.
}
\]

`CHARACTERIZATION` means:

```text
apply the already-frozen round objects
certify closure/admissibility/burden
record the response surface
preserve the language specification unchanged
```

`DEVELOPMENT` means:

```text
propose a new primitive
alter grammar or semantics
change dimensions or parameter ranges
change admissibility
change burden accounting
change closure procedure
change calibration generators or distributions
add/remove a language
```

Development may be scientifically motivated by evidence, but it occurs outside the characterization round that produced that evidence.

---

# 7. Revision creates a new version

If round `v` produces evidence motivating a language change, the only licensed revision path is:

\[
\boxed{
\mathfrak L^{(v)}
\rightarrow
\mathcal Y_{\rm cal}^{(v)}
\rightarrow
\text{new hypothesis}
\rightarrow
\text{new preregistration}
\rightarrow
\mathfrak L^{(v+1)}.
}
\]

The new round must receive a new immutable specification hash and a new round identifier.

There is no object called:

```text
L_v_repaired_within_round
```

for confirmatory characterization purposes.

Any change to the round tuple after calibration exposure increments the round version.

---

# 8. Evidence provenance classes

Every evidence item used by the decision-substrate language program must be assigned a round-relative provenance role from exactly these classes:

```text
DEVELOPMENT_EVIDENCE
CALIBRATION_EVIDENCE
APPLICATION_EVIDENCE
```

## `DEVELOPMENT_EVIDENCE`

Evidence used to motivate specification or revision of a language, calibration generator, burden rule, authority rule, or closure procedure.

Examples may include:

```text
prior-round calibration outcomes
prior actual-application outcomes
external theory or literature
previous benchmark failures
abstract structural hypotheses motivated by earlier results
```

Development evidence may justify a new hypothesis or new round specification.

It does not validate the modifications it motivated.

## `CALIBRATION_EVIDENCE`

Evidence generated by executing a fully frozen round on its preregistered anonymous structural calibration world.

It characterizes only the exact frozen version on which it was generated.

If a calibration datum is subsequently used to motivate `v+1`, its role relative to the **modified v+1 specification** becomes `DEVELOPMENT_EVIDENCE`.

It may not simultaneously serve as clean confirmatory calibration evidence for the modifications it motivated.

## `APPLICATION_EVIDENCE`

Evidence generated after the frozen language/application set has passed characterization and is tested on separately preregistered actual targets.

Application evidence tests the frozen application-stage object.

If later used to motivate a language revision, its role relative to that new language version becomes `DEVELOPMENT_EVIDENCE`.

---

# 9. Evidence-role non-leakage

For a modification `Delta L` motivated by evidence `E`:

\[
\boxed{
E
\xrightarrow{\text{motivates}}
\Delta\mathcal L
\quad\Rightarrow\quad
E\text{ cannot validate }\Delta\mathcal L\text{ within that same evidence role}.
}
\]

This is the binding methodological rule:

\[
\boxed{\textbf{
Evidence may motivate a revision, but cannot validate the revision it motivated within the same round.
}}
\]

A new version requires new characterization evidence if a confirmatory characterization claim is desired.

Reusing old relations is permitted only if their provenance is explicitly downgraded to development/regression evidence for the modified version; they cannot be presented as independent validation of the modification.

---

# 10. New characterization data after revision

For `v+1`, the default confirmatory path is a newly frozen anonymous calibration world:

\[
\boxed{
\mathfrak K_{\rm cal}^{(v+1)}
}
\]

specified before executing `v+1`.

It may share abstract structural axes with earlier rounds, but its confirmatory relations must not be selected adaptively to make the new language look favorable.

If any calibration relations from an earlier round are intentionally reused, the later preregistration must label them explicitly as one of:

```text
DEVELOPMENT_REUSE
REGRESSION_REUSE
```

and exclude them from claims of independent confirmation of the change they helped motivate.

A separate newly generated or otherwise unexposed calibration subset is required for a fresh confirmatory claim about the modified language.

---

# 11. Calibration-generator firewall

The calibration generator is frozen before calibration execution.

The forbidden adaptive loop is:

\[
\boxed{
\mathcal L
\rightarrow
\text{observed calibration behavior}
\rightarrow
\text{change calibration distribution/generator}
\rightarrow
\text{recharacterize the same round}.
}
\]

Within one round, observed results may not change:

```text
which structural regimes are generated
relative frequency or weighting of regimes
candidate counts
matched-pair construction
control frequencies
fixture inclusion/exclusion
sampling seed
relation enumeration boundaries
nuisance encoding count or construction
stop rules
```

A change to any such item creates `v+1` or a separately numbered new round specification.

---

# 12. Round execution order

The binding execution order is now:

\[
\boxed{
\text{round architecture inherited}
\rightarrow
\text{concrete language-family freeze}
\rightarrow
\text{calibration-world freeze}
\rightarrow
\text{characterization execution}
\rightarrow
\text{characterization result}
\rightarrow
\text{application-set freeze or external revision}.
}
\]

Inside characterization, the parent gate ordering remains:

\[
\boxed{
\text{unrestricted closure certification}
\rightarrow
\text{admissible closure certification}
\rightarrow
\text{minimum-burden certification}
\rightarrow
\text{terminal classification}.
}
\]

No result-driven modification occurs between these steps.

---

# 13. Meaning of final/application-set freeze

Under this amendment, the later freeze after characterization is **not** a language-redesign event.

It may only:

```text
record the exact characterized language-version hashes
record which already-characterized versions are eligible for actual application
preserve their calibration provenance
freeze the actual application set
```

It may not alter the syntax, semantics, admissibility, burden, closure procedure, or calibration-tested parameter domains of an eligible language.

Thus the later stage is more precisely an:

```text
APPLICATION_SET_FREEZE
```

rather than an opportunity to repair the language after calibration.

---

# 14. Revised stage sequence

The binding program sequence is now:

\[
\boxed{
\text{architecture}
\rightarrow
\text{concrete language-family freeze}
\rightarrow
\text{anonymous calibration-world freeze}
\rightarrow
\text{structural characterization}
\rightarrow
\text{application-set freeze}
\rightarrow
\text{actual application preregistration}
\rightarrow
\text{actual application execution}.
}
\]

If characterization motivates development, leave the round and start:

\[
\boxed{
\text{new hypothesis}
\rightarrow
\text{new version preregistration}
\rightarrow
\text{new calibration-world freeze}
\rightarrow
\text{new characterization round}.
}
\]

No adaptive repair occurs inside the preceding round.

---

# 15. Round-level serialization

Every later language-characterization artifact must include at minimum:

```text
round_id
round_version
parent_architecture_commit
round_specification_commit
round_specification_hash
language_family_hash
calibration_world_hash
language_specification_hashes
calibration_generator_hashes
A_DS_hash
B_DS_hash
Pi_closure_hash
Sigma_outcome_hash
evidence_provenance_registry
calibration_relations_or_generation_certificate
characterization_results
within_round_modification_performed
post_result_generator_modification_performed
application_set_freeze_performed
```

Hard requirements:

```text
within_round_modification_performed         = false
post_result_generator_modification_performed = false
```

for a valid characterization round.

Every calibration result must retain the corrected parent serialization field:

```text
anonymous_candidate_count
```

as established by the non-semantic erratum.

---

# 16. Broken controls / forbidden shortcuts added by this amendment

## F1 — calibration-driven grammar repair

Observe calibration failure and alter the language grammar within the same round.

```text
failure: WITHIN_ROUND_LANGUAGE_ADAPTATION
```

## F2 — calibration-driven parameter widening

Expand dimensions, thresholds, alphabet, precision, or parameter range after seeing calibration outcomes.

```text
failure: WITHIN_ROUND_DOMAIN_ADAPTATION
```

## F3 — favorable calibration redistribution

Change generator frequencies, regimes, candidate counts, or relation selection after observing poor performance.

```text
failure: CALIBRATION_DISTRIBUTION_ADAPTATION
```

## F4 — old calibration validates its own repair

Use a round-`v` failure to design `v+1`, then present the same exposed relation as independent confirmation of the modification.

```text
failure: DEVELOPMENT_VALIDATION_COLLAPSE
```

## F5 — version mutation without new preregistration

Change any defining round object while retaining the same round/version identity.

```text
failure: VERSION_PROVENANCE_COLLAPSE
```

## F6 — application-set freeze used as redesign

Modify a language after characterization while describing the change as merely a final freeze.

```text
failure: POST_CHARACTERIZATION_REDESIGN
```

## F7 — calibration called language discovery

Infer that the calibration process itself supplied the language grammar or primitives.

```text
failure: CHARACTERIZATION_DEVELOPMENT_COLLAPSE
```

---

# 17. Success criteria added by this amendment

A later identification round is valid only if:

1. all six round objects are frozen before calibration execution;
2. the calibration generator is frozen as part of `K_cal^(v)` before execution;
3. the concrete language family is immutable within the round;
4. the calibration world is immutable within the round;
5. calibration outcomes only characterize the frozen language family;
6. every language modification creates a new version and preregistration;
7. evidence roles are explicitly typed as development, calibration, or application evidence;
8. evidence motivating a revision is not used as independent confirmation of that revision;
9. reused old calibration data are labeled development/regression reuse for the modified version;
10. newly modified versions receive newly frozen characterization evidence for fresh confirmatory claims;
11. the post-characterization application-set freeze does not alter language definitions;
12. actual-target exclusion from language construction remains fully binding.

---

# 18. Anti-downstream flags

At this amendment checkpoint:

```text
round_firewall_architecture_frozen          = true
concrete_language_universe_instantiated     = false
calibration_world_instantiated              = false
calibration_generator_instantiated          = false
characterization_executed                   = false
within_round_language_revision_allowed      = false
within_round_generator_revision_allowed     = false
application_set_frozen                      = false
actual_target_application_preregistered     = false
actual_target_application_performed         = false
actual_Q_extension_defined                  = false
governance_contract_selected                = false
candidate_ranking_performed                 = false
candidate_adoption_selected                 = false
authorization_performed                     = false
binding_performed                           = false
execution_performed                         = false
```

No dependency-ledger update is implied.

---

# 19. Strongest permitted claim

The strongest claim licensed by this amendment alone is:

\[
\boxed{\textbf{
Decision-substrate language identification is now round-versioned so that each concrete language family and anonymous calibration world are frozen before characterization; calibration outcomes may certify the closure, admissibility, burden, and terminal-status properties of that frozen version but may not modify it within the same round. Any evidence-motivated revision creates a new preregistered version and requires separately classified characterization evidence.
}}
\]

This amendment does not establish any language's closure, admissibility, minimum burden, or actual-target performance.

---

# 20. Stop condition

Stop after freezing this firewall.

Do not in this commit:

```text
instantiate a concrete language
choose language primitives
choose a dimensionality
choose parameter ranges
instantiate calibration structural values
construct calibration relations
select calibration frequencies
execute characterization
revise a language
freeze an application set
read actual target artifacts for design
apply any language to actual targets
define Q_extension
rank candidates
select governance
adopt
authorize
bind
execute
update the dependency ledger
```

The next scientific artifact remains a **concrete language-family and calibration-world specification preregistration**, now governed by both the parent architecture and this round firewall.