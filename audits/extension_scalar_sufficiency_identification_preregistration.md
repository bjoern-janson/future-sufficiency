# Extension Scalar Sufficiency / Decision-Substrate Identification — Preregistration

## Status

This document freezes the next scientific gate after actual-candidate preference application.

Parent checkpoint:

```text
97c0b092932b2931a74af47a7761a6aa93272c23
```

Actual-candidate preference-application preregistration:

```text
f64dd1d3e222b9ca13903facc8fd1e727adb2fd7
```

Actual-candidate preference-application execution:

```text
97c0b092932b2931a74af47a7761a6aa93272c23
```

Exact actual-candidate preference-application executable blob:

```text
b568d90be09bcfa23b4a67ebbdeb90be64bce02f
```

Exact actual-candidate preference-application result blob:

```text
7efc07e54de9b7e4719caee632daecab32e56f1f
```

Exact actual-candidate preference-application note blob:

```text
26c5bebb205e320df8bb8c40f60a393ccf542455
```

Preference/governance-interface identification execution:

```text
7c5bffe31b7cfae163248eadec869eb4800a059a
```

Exact preference-identification executable blob:

```text
b47c0884dcb7769a2ca9b934e8a9b64dad218399
```

Exact preference-identification result blob:

```text
4fab22d2a7be25b001b679fe92e67187098ce696
```

The only new object frozen here is:

\[
\boxed{
(R_{\rm pref}^{\rm cal},\mathcal Q_{\rm adm})
\longrightarrow
D_{\rm scalar}
}
\]

where `R_pref^cal` is an independently constructed typed preference-calibration relation, `Q_adm` is a preregistered finite family of scalar-plus-decoder substrates, and `D_scalar` is a typed sufficiency/contraction diagnosis.

This artifact does **not** scalarize the actual 12-candidate preference graph.

It does not define an actual `Q_extension`.

It does not select a governance contract.

It does not rank, adopt, authorize, bind, or execute any extension.

---

# 1. Scientific question

The preceding branch has established, in audited finite regimes:

\[
\boxed{
\mathcal V
\rightarrow
\mathcal R_{\rm compare}
\rightarrow
G_{\rm pref}
\rightarrow
R_{\rm pref}^{\rm actual}
}
\]

with `R_pref` remaining typed, contract-relative, capable of lawful equivalence, and capable of `NO_WARRANTED_PREFERENCE` without forcing completion.

The present question is not:

> Can arbitrary real numbers plus an arbitrary decoder encode a finite graph?

That question is trivial and scientifically irrelevant because the decoder can smuggle the graph back in.

The present question is:

\[
\boxed{
\textbf{
Can a preregistered restricted scalar decision substrate preserve every typed preference distinction required by a declared decision relation, introduce no unauthorized ordering, and reduce total semantic specification burden relative to the native typed pair relation?
}
}
\]

The governing separation is:

\[
\boxed{
\text{scalar representation}
\neq
\text{scalar completion}
\neq
\text{scalar contraction}.
}
\]

A representation reproduces the target typed relation exactly.

A completion invents preference where the target relation withholds it.

A contraction is a faithful representation whose complete representation/decoder/auxiliary burden is strictly smaller than the native typed-relation burden under the common preregistered ledger.

---

# 2. Actual 12-candidate preference graph is a strict holdout

The actual preference graph produced at `97c0b09` motivated this gate but may not calibrate it.

During scalar-sufficiency identification the child execution must **not read, decode, search, fit to, or inspect application records from**:

```text
audits/extension_candidate_preference_application_results.json
```

The exact blob `7efc07e54de9b7e4719caee632daecab32e56f1f` is an upstream provenance anchor only.

The child may verify that this blob exists and that the preceding gate reported `Q_extension_defined = false`, but it may not use any candidate ID, actual pair, actual four-contract vector, status count, abstention count, or relation topology to choose:

```text
score range
decoder family
threshold count
band policy
burden formula
fixture family
success criterion
```

Thus:

\[
\boxed{
R_{\rm pref}^{\rm actual}
\not\rightarrow
\mathcal Q_{\rm adm}.
}
\]

The first scalar-stage read of the actual 12-candidate graph is reserved for a later separately preregistered **actual scalar application** gate, if this identification gate earns an admissible scalar contraction family worth applying.

---

# 3. Typed preference target

Every calibration relation is defined over a finite anonymous candidate set `S` and the exact output alphabet:

```text
PREFER_I
PREFER_J
EQUIVALENT
NO_WARRANTED_PREFERENCE
```

For every unordered canonical pair `(i,j)`, exactly one token is present.

Pair swap is typed:

```text
PREFER_I                 <-> PREFER_J
PREFER_J                 <-> PREFER_I
EQUIVALENT                 -> EQUIVALENT
NO_WARRANTED_PREFERENCE    -> NO_WARRANTED_PREFERENCE
```

`NO_WARRANTED_PREFERENCE` is not a missing edge.

It is not `EQUIVALENT`.

It is not a numerical zero.

It is not an invitation to choose an arbitrary direction.

Therefore:

\[
\boxed{
\texttt{NO\_WARRANTED\_PREFERENCE}
\neq
\texttt{EQUIVALENT}.
}
\]

---

# 4. Scalar representation condition

For a supplied governance condition `G_cal`, a scalar substrate is always typed as:

\[
\boxed{
Q^G=(q_G,g_G,a_G)
}
\]

where:

- `q_G : S -> Z` is the candidate-level scalar assignment inside the frozen finite score domain;
- `g_G` is a decoder from two scalar values to the four-token preference alphabet;
- `a_G` is the explicitly counted auxiliary structure permitted by the scalar family.

The exact representation requirement is:

\[
\boxed{
\forall i\neq j:\quad
R_{\rm pref}^{G}(i,j)
=
g_G(q_G(i),q_G(j);a_G).
}
\]

Equivalently:

\[
\boxed{
R_{\rm pref}^{G}
=
g_G\circ(q_G\times q_G).
}
\]

A family is not credited for reproducing only directional pairs.

It must reproduce `PREFER_I`, `PREFER_J`, `EQUIVALENT`, and `NO_WARRANTED_PREFERENCE` exactly wherever those states occur.

---

# 5. Two independent preservation diagnostics

Exact factorization is primary. Two diagnostic failure classes must also be reported.

## 5.1 Authorized-decision loss

A target relation is lost whenever the decoded output differs from the target.

Important subcases include:

```text
PREFER_I/J -> EQUIVALENT
PREFER_I/J -> NO_WARRANTED_PREFERENCE
EQUIVALENT -> NO_WARRANTED_PREFERENCE
NO_WARRANTED_PREFERENCE -> EQUIVALENT
```

The last two matter because equivalence and abstention are distinct authorized states.

## 5.2 Scalar authority injection

A scalar substrate injects decision authority whenever it produces a directional preference that the target relation did not authorize, or produces the opposite direction.

At minimum:

```text
NO_WARRANTED_PREFERENCE -> PREFER_I/J
EQUIVALENT              -> PREFER_I/J
PREFER_I                 -> PREFER_J
PREFER_J                 -> PREFER_I
```

must be counted as injection failures.

The gate therefore operationalizes:

\[
\boxed{
\textbf{no authorized decision distinction lost}
\quad+\quad
\textbf{no unauthorized decision distinction introduced}.
}
\]

---

# 6. Governance-relative typing is mandatory

The scalar object is not governance-free.

The primary type is:

\[
\boxed{Q_{\rm extension}^{G}}
\]

not an unqualified `Q_extension`.

Calibration governance conditions are synthetic anonymous labels such as:

```text
G_CAL_A
G_CAL_B
```

They are not any of the four actual governance contracts from the preceding application gate.

A scalar representation under `G_CAL_A` may differ from one under `G_CAL_B` because the authoritative governance input differs.

A governance-free shared scalar is tested only as a broken control on a synthetic reversal fixture.

No success in this gate licenses collapsing governance provenance.

---

# 7. Frozen finite score domain

To prevent hidden information from being stored in arbitrary real precision, candidate scores are exact bounded integers.

For an `n`-candidate calibration fixture:

\[
\boxed{
q(s)\in\{0,1,\ldots,n+1\}.
}
\]

Translation is normalized by requiring:

```text
min_s q(s) = 0
```

before canonical serialization.

No candidate-specific floating-point epsilon, irrational encoding, large integer codebook, arbitrary precision decimal, hash-derived score, candidate-ID encoding, or pair-index encoding is admissible.

Existence within each scalar family must be established by complete finite search or an exactly equivalent exhaustive constraint procedure over the preregistered bounded family.

A heuristic failure to find a representation is not `NOT_REPRESENTABLE`.

---

# 8. Admissible scalar/decoder families

The primary admissible family is deliberately small and nested in semantic power.

## D0 — ordinary ordered scalar

Candidate object:

```text
q(s) in {0,...,n+1}
```

Decoder:

```text
q_i > q_j  -> PREFER_I
q_i < q_j  -> PREFER_J
q_i = q_j  -> EQUIVALENT
```

`NO_WARRANTED_PREFERENCE` is unreachable.

This is the ordinary scalar-order baseline.

## D1 — scalar + one global abstention radius

Candidate object:

```text
q(s) in {0,...,n+1}
tau in {0,...,n+1}
```

Decoder for `d = q_i - q_j`:

```text
d = 0                 -> EQUIVALENT
0 < |d| <= tau        -> NO_WARRANTED_PREFERENCE
d > tau               -> PREFER_I
d < -tau              -> PREFER_J
```

`tau = 0` reduces to ordinary ordered-scalar semantics.

The abstention rule is global. It cannot vary by pair or candidate identity.

## D2 — scalar + restricted two-cut typed decoder

Candidate object:

```text
q(s) in {0,...,n+1}
0 <= tau_1 <= tau_2 <= n+1
```

Nonzero magnitude bands:

```text
B1: 0 < |d| <= tau_1
B2: tau_1 < |d| <= tau_2
B3: |d| > tau_2
```

Each band receives exactly one globally supplied policy:

```text
DIRECTION
NO_WARRANTED_PREFERENCE
```

There are therefore exactly eight possible band-policy triples.

Zero difference is always:

```text
EQUIVALENT
```

For a band labeled `DIRECTION`, sign alone determines orientation:

```text
d > 0 -> PREFER_I
d < 0 -> PREFER_J
```

No band may use candidate identity, provenance, pair identity, governance display name, or an exception list.

D2 is the richest admissible scalar family in this gate.

## D3 — native typed relation baseline

D3 is **not a scalar family**. It is the frozen baseline representation:

```text
one typed relation token per canonical unordered pair
```

It is guaranteed faithful by construction and supplies `B_Rpref` for contraction accounting.

No result in this gate may call D3 a scalarization.

---

# 9. Unrestricted lookup is a representability control, not an admissible contraction family

Define broken/control substrate:

```text
W_LOOKUP
```

with an arbitrary pair-specific mapping:

```text
(candidate_i, candidate_j) -> target preference token
```

This control is expected to represent every finite calibration relation.

It is included to demonstrate why unrestricted `g(q_i,q_j)` is scientifically vacuous.

`W_LOOKUP` may never receive `FAITHFUL_CONTRACTION` because its pair-specific table carries at least the native pair-relation burden plus decoder overhead.

Thus the expected diagnostic is:

\[
\boxed{
\texttt{REPRESENTABLE\_NO\_CONTRACTION}.
}
\]

If the execution ever labels `W_LOOKUP` a contraction, the burden accounting has failed.

---

# 10. Burden architecture

The anti-scaffold question is frozen as:

\[
\boxed{\textbf{Where did the decision complexity go?}}
\]

Common inherited items are excluded symmetrically from both substrates:

```text
candidate registry
canonical pair enumeration rule
four-token output vocabulary
pair-swap semantics
governance-condition identity
```

Only representation-specific obligations are counted.

## 10.1 Native typed relation burden

For an `n`-candidate calibration graph:

\[
\boxed{
B_{R_{\rm pref}}=\binom n2.
}
\]

Each canonical unordered pair contributes one independently stored typed relation obligation.

No transitive closure or compression rule is assumed for the native baseline.

## 10.2 Scalar burden

For every scalar family:

\[
\boxed{
B_{\rm scalar}=B_q+B_g+B_{\rm auxiliary}.
}
\]

### D0

```text
B_q            = n candidate score assignments
B_g            = 3 decoder branch obligations
B_auxiliary    = 0
TOTAL          = n + 3
```

### D1

```text
B_q            = n candidate score assignments
B_g            = 4 decoder branch obligations
B_auxiliary    = 1 global threshold obligation
TOTAL          = n + 5
```

### D2

```text
B_q            = n candidate score assignments
B_g            = 5 decoder obligations
                  (zero/equality + three band policies + sign-orientation rule)
B_auxiliary    = 2 global cutpoint obligations
TOTAL          = n + 7
```

### W_LOOKUP

```text
B_q            = 0
B_g            = 1 pair-lookup decoder obligation
B_auxiliary    = C(n,2) pair-specific relation entries
TOTAL          = C(n,2) + 1
```

Pair-specific hidden exception tables, candidate-ID codebooks, opaque hashes, or uncounted decoder state are forbidden.

Any such structure, if introduced by a broken control, must be counted in `B_auxiliary`.

---

# 11. Contraction criterion

Faithful representation is necessary but not sufficient.

A scalar family receives `FAITHFUL_CONTRACTION` only if both:

\[
\boxed{
\forall i\neq j:\quad
R_{\rm pref}(i,j)=g(q_i,q_j)
}
\]

and:

\[
\boxed{
B_{\rm scalar}<B_{R_{\rm pref}}.
}
\]

Equality is not contraction.

A representation with:

```text
B_scalar = B_Rpref
```

or:

```text
B_scalar > B_Rpref
```

must be classified as `REPRESENTABLE_NO_CONTRACTION`.

This gate does not use byte count, source-code line count, compressed-file size, or visible token count as substitutes for semantic obligation burden.

---

# 12. Frozen outcome vocabulary

For every calibration fixture and every tested scalar family, output exactly one:

```text
FAITHFUL_CONTRACTION
REPRESENTABLE_NO_CONTRACTION
NOT_REPRESENTABLE
```

Definitions:

### `FAITHFUL_CONTRACTION`

```text
exact typed relation recovered
zero authority-injection mismatches
B_scalar < B_Rpref
```

### `REPRESENTABLE_NO_CONTRACTION`

```text
exact typed relation recovered
zero authority-injection mismatches
B_scalar >= B_Rpref
```

### `NOT_REPRESENTABLE`

```text
no member of the complete preregistered finite scalar family reproduces the target relation exactly
```

A fixture-level descriptive summary may additionally say:

```text
NO_SUPPORTED_CONTRACTION
```

iff none of D0, D1, or D2 receives `FAITHFUL_CONTRACTION` on that fixture.

`NO_SUPPORTED_CONTRACTION` means only **no contraction in the tested admissible scalar families**.

It does not establish global minimality of the native relation.

---

# 13. Independent calibration domain

The scalar-sufficiency calibration uses only anonymous synthetic candidates.

No actual candidate ID from the 12-candidate extension set may appear in a calibration fixture.

Primary anonymous node alphabet:

```text
a b c d e f
```

All relations are defined directly in the four-token preference language.

No `DeltaV`, burden, geometry, collateral, reopenability, scope, Hudson/Rubi, synthesized candidate, control candidate, or actual governance-contract outcome is used to generate these fixtures.

---

# 14. Calibration fixture A — strict total order

Six anonymous candidates:

```text
a > b > c > d > e > f
```

Every unordered pair is directional according to that order.

No `EQUIVALENT` and no `NO_WARRANTED_PREFERENCE` edges occur.

Purpose:

- positive control for ordinary scalar ordering;
- establish that the gate does not reject scalarization merely because it is scalar;
- verify strict directional factorization and pair-swap semantics.

Preregistered expectation:

```text
D0 must be representable and must satisfy the contraction inequality.
```

D1/D2 may also represent it; this does not make them preferable or minimal.

---

# 15. Calibration fixture B — total preorder with genuine equivalence

Six anonymous candidates with ordered equivalence classes:

```text
{a,b} > {c} > {d,e} > {f}
```

Within each displayed class:

```text
EQUIVALENT
```

Across classes:

```text
PREFER higher class
```

Purpose:

- verify that equality of scalar values can faithfully represent genuine candidate-level equivalence;
- distinguish lawful equality from abstention.

Preregistered expectation:

```text
D0 must be representable and must satisfy the contraction inequality.
```

---

# 16. Calibration fixture C — one-threshold abstention relation

Six anonymous candidates.

The target graph is generated independently from the following frozen witness solely to define the synthetic target:

```text
q*:
  a=0
  b=1
  c=2
  d=5
  e=6
  f=7

tau*=1
```

Target relation:

```text
same score                    -> EQUIVALENT
nonzero distance <= 1         -> NO_WARRANTED_PREFERENCE
distance > 1                  -> direction by score sign
```

Purpose:

- falsify ordinary scalar completion;
- provide a positive control where one global abstention mechanism is genuinely sufficient.

Preregistered expectations:

```text
D0 -> NOT_REPRESENTABLE
D1 -> exact representability required; burden test then determines contraction status
```

Because `n=6`, the frozen burden ledger predicts `B_D1 = 11 < 15 = B_Rpref`; therefore an exact D1 representation must be diagnosed `FAITHFUL_CONTRACTION`.

---

# 17. Calibration fixture D — non-monotone two-band abstention relation

Six anonymous candidates.

Frozen synthetic witness:

```text
q*:
  a=0
  b=1
  c=2
  d=4
  e=5
  f=6

tau_1*=1
tau_2*=3

band policies:
  B1 -> DIRECTION
  B2 -> NO_WARRANTED_PREFERENCE
  B3 -> DIRECTION
```

Zero difference remains `EQUIVALENT`.

Purpose:

- produce a typed partial decision relation that cannot be represented by the monotone one-threshold D1 decoder;
- provide a positive control for restricted typed decoder D2.

Preregistered expectations:

```text
D0 -> NOT_REPRESENTABLE
D1 -> NOT_REPRESENTABLE
D2 -> exact representability required
```

For `n=6`:

```text
B_D2    = 13
B_Rpref = 15
```

so an exact D2 representation must be diagnosed `FAITHFUL_CONTRACTION`.

---

# 18. Calibration fixture E — directional cycle

Six anonymous candidates include the frozen cycle:

```text
a PREFER_I b
b PREFER_I c
c PREFER_I a
```

Every pair involving `d`, `e`, or `f` is `NO_WARRANTED_PREFERENCE`, except no self-relations are represented.

Purpose:

- test a relation incompatible with any one-dimensional scalar whose directional output follows score sign;
- ensure the audit can return `NOT_REPRESENTABLE` rather than forcing a completion.

Preregistered expectation:

```text
D0 -> NOT_REPRESENTABLE
D1 -> NOT_REPRESENTABLE
D2 -> NOT_REPRESENTABLE
```

`W_LOOKUP` must remain representable but non-contracting.

---

# 19. Calibration fixture F — nontransitive scalar equality demand

Four anonymous candidates with:

```text
a EQUIVALENT b
b EQUIVALENT c
a PREFER_I c
```

All pairs involving `d` are `NO_WARRANTED_PREFERENCE`.

Purpose:

- test the algebraic constraint imposed by scalar equality;
- distinguish pairwise typed equivalence from an assumed scalar equality relation.

Preregistered expectation:

```text
D0 -> NOT_REPRESENTABLE
D1 -> NOT_REPRESENTABLE
D2 -> NOT_REPRESENTABLE
```

because all three frozen scalar decoders emit `EQUIVALENT` only at exact scalar equality, which is transitive.

---

# 20. Calibration fixture G — governance-relative reversal

This fixture uses the same six anonymous candidates under two synthetic governance conditions:

```text
G_CAL_A
G_CAL_B
```

Under `G_CAL_A`:

```text
a > b > c > d > e > f
```

Under `G_CAL_B`:

```text
f > e > d > c > b > a
```

Both relations are ordinary total orders individually.

Purpose:

- verify that scalar representations are typed by governance condition;
- falsify a governance-free shared scalar pretending that one `q(s)` determines preference independent of `G`.

Primary contract-relative rule:

```text
q_G_CAL_A and q_G_CAL_B may differ.
```

Broken control:

```text
W_SHARED_GOVERNANCE_FREE
```

requires one identical candidate score vector and one identical ordinary decoder across both conditions.

Preregistered expectations:

```text
contract-relative D0: representable separately under each G_CAL condition
W_SHARED_GOVERNANCE_FREE: NOT_REPRESENTABLE
```

Failure of the shared scalar is not authority injection; it is a typing failure caused by erasing an authoritative governance input.

---

# 21. Calibration fixture H — nuisance relabeling

Every primary fixture is evaluated under 64 anonymous encodings.

Permutations include:

```text
candidate handles
governance display aliases
fixture display aliases
serialization order
opaque non-authoritative nonce
implementation tag
```

The semantic relation, canonical candidate-role orientation, scalar-family definition, and burden schema remain unchanged.

Required:

```text
D_scalar classification unchanged 64/64
minimal burden unchanged 64/64
existence/nonexistence of exact representation unchanged 64/64
```

A scalar construction that depends on candidate spelling, provenance-like labels, hash order, or opaque nonce fails nuisance invariance.

---

# 22. Exact search and witness requirements

For D0-D2, the child must exhaust the complete frozen bounded integer family or use an exactly equivalent complete constraint procedure.

For every successful representation, serialize at minimum:

```text
fixture_id
governance_condition_id
scalar_family_id
canonical candidate order
canonical q vector
decoder parameters
full decoded pair relation
target pair relation
exact_match = true
B_q
B_g
B_auxiliary
B_scalar
B_Rpref
D_scalar
```

For `NOT_REPRESENTABLE`, serialize:

```text
complete_family_exhausted = true
score_domain
threshold/cutpoint domain
band-policy domain
number of canonical scalar candidates evaluated or exact equivalent proof certificate
```

No heuristic-only absence claim is allowed.

---

# 23. Canonical witness selection

If multiple scalar witnesses exist, output selection is descriptive only and must not affect representability.

Choose canonically by:

1. minimum `B_scalar` within the fixed family schema;
2. lexicographically smallest normalized `q` vector in canonical anonymous candidate order;
3. lexicographically smallest decoder-parameter tuple.

Because the family burden formulas are fixed by schema, step 1 generally ties within a family.

Canonical witness selection is not candidate preference and does not rank governance contracts.

---

# 24. Broken controls / forbidden shortcuts

The execution must explicitly falsify or reject the following.

## W1 — `NWP -> EQUIVALENT`

Treat every `NO_WARRANTED_PREFERENCE` edge as scalar equality.

Failure type:

```text
typed decision collapse
```

## W2 — `NWP -> arbitrary direction`

Resolve abstention using candidate order, candidate ID, or lexical handle.

Failure type:

```text
scalar authority injection
```

## W3 — hidden pair-specific threshold/exception table

Allow per-pair decoder thresholds or exception clauses while counting only the visible scalar.

Failure type:

```text
anti-scaffold burden violation
```

## W4 — unrestricted pair lookup called a contraction

Use `W_LOOKUP` and omit its pair table from `B_auxiliary`.

Failure type:

```text
false contraction
```

## W5 — actual 12-candidate graph tunes scalar family

Read actual preference outcomes before fixing scalar/decoder semantics.

Failure type:

```text
holdout leakage
```

## W6 — governance-free shared scalar

Erase `G` on the reversal fixture.

Failure type:

```text
governance typing collapse
```

## W7 — nuisance encoded in score

Use candidate handle, provenance-like label, nonce, serialization position, or implementation tag to assign `q`.

Failure type:

```text
authority injection
```

## W8 — decoder burden omitted

Report only the number of candidate scalar values while excluding thresholds, cutpoints, branch semantics, band policies, or exception clauses.

Failure type:

```text
anti-scaffold accounting failure
```

## W9 — total ordering assumed as success requirement

Treat a faithful typed relation containing abstention as defective merely because it is not complete.

Failure type:

```text
unlicensed decision-completion objective
```

## W10 — scalar preference becomes authorization

Use a faithful scalar result to authorize, adopt, bind, or execute a candidate.

Failure type:

```text
downstream authority leakage
```

---

# 25. No relation-pattern tuning after calibration begins

The following are immutable after this preregistration:

```text
D0 decoder
D1 decoder
D2 decoder
bounded integer score domain
burden formulas
calibration fixture definitions
outcome vocabulary
contraction inequality
nuisance family
broken controls
```

If a primary fixture is surprising, the child reports the surprise.

It may not add another threshold, widen integer precision, insert a pair exception, change `NWP` semantics, or drop a fixture during execution.

Any richer scalar family requires a new preregistration.

---

# 26. Identification success criteria

The scalar-sufficiency identification gate passes only if all of the following hold:

1. the actual 12-candidate preference graph is not read as calibration data;
2. every calibration fixture uses anonymous synthetic candidates only;
3. all D0-D2 family definitions match this preregistration exactly;
4. score precision remains the frozen bounded integer domain;
5. every representability claim is exhaustive within the corresponding finite family;
6. every successful witness reproduces every canonical unordered pair exactly;
7. `EQUIVALENT` and `NO_WARRANTED_PREFERENCE` remain distinct;
8. no target `NWP` is silently completed to direction;
9. pair-swap semantics are exact;
10. nuisance invariance holds under all 64 encodings;
11. D0 represents fixtures A and B;
12. D0 fails fixture C;
13. D1 faithfully represents fixture C;
14. D0 and D1 fail fixture D;
15. D2 faithfully represents fixture D;
16. D0-D2 all fail the directional-cycle fixture E;
17. D0-D2 all fail the nontransitive-equivalence fixture F;
18. contract-relative D0 represents each side of governance-reversal fixture G separately;
19. governance-free shared-scalar control fails fixture G;
20. `W_LOOKUP` is representable where expected but never labeled a contraction;
21. every `FAITHFUL_CONTRACTION` satisfies the strict burden inequality;
22. every faithful representation with non-smaller burden is `REPRESENTABLE_NO_CONTRACTION`;
23. no candidate ranking, utility, reward, actual `Q_extension`, adoption, authorization, binding, or execution is introduced.

A partial pass does not license actual scalar application.

---

# 27. Expected burden controls

For six-candidate fixtures:

```text
B_Rpref = C(6,2) = 15
B_D0    = 6 + 3 = 9
B_D1    = 6 + 5 = 11
B_D2    = 6 + 7 = 13
B_LOOKUP= 15 + 1 = 16
```

Therefore, when exact representability holds:

```text
D0/D1/D2 can qualify as contraction on six-candidate fixtures
W_LOOKUP cannot
```

For four-candidate fixture F:

```text
B_Rpref = C(4,2) = 6
B_D0    = 7
B_D1    = 9
B_D2    = 11
B_LOOKUP= 7
```

Thus even if a four-candidate scalar family were faithful, it would not automatically qualify as a contraction under this burden ledger.

This is intentional: representability and contraction are different scientific objects.

---

# 28. Scope of the burden result

The burden ledger is a finite semantic-obligation accounting device.

It does **not** establish:

```text
Kolmogorov complexity
minimum description length in all languages
computational runtime minimality
memory minimality in all implementations
normative simplicity
universal scalar impossibility
```

A later minimality program may compare alternative burden schemas or richer representation languages.

This gate asks only whether the frozen scalar families contract the frozen typed-relation representation under the declared ledger.

---

# 29. No global minimality claim

If all D0-D2 families fail to contract a fixture, the allowed statement is:

> No tested admissible scalar family provides a lower-burden faithful representation of this typed preference relation in the audited calibration regime.

Forbidden statement:

> The native typed preference relation is globally minimal.

Global membership in a necessary set `N` would require a broader separately preregistered minimality program over a sufficiently rich substrate family.

Thus:

\[
\boxed{
\texttt{NO\_SUPPORTED\_CONTRACTION}
\not\Rightarrow
R_{\rm pref}\in N_{\rm universal}.
}
\]

---

# 30. No governance-family comparison

The synthetic governance labels in fixture G are typing conditions only.

The execution must not infer:

```text
G_CAL_A better than G_CAL_B
one governance condition more scalarizable
scalarizability as normative evidence
lower scalar burden as governance quality
```

Likewise, the four actual supplied governance contracts from the preceding branch remain completely outside calibration.

---

# 31. No reward interpretation

A scalar witness in this gate is a **decision representation**, not a reward.

The child must not rename a scalar witness:

```text
reward
utility
value function
objective
fitness
```

unless a later separately preregistered gate defines and licenses that semantic role.

The present chain remains:

\[
\boxed{
R_{\rm pref}^{G}
\rightarrow
\text{candidate scalar representation?}
}
\]

not:

\[
\boxed{
R_{\rm pref}^{G}
\rightarrow
\text{reward authority}.
}
\]

---

# 32. Anti-downstream flags

The child execution must hard-assert:

```text
scalar_sufficiency_identification_performed = true
actual_candidate_scalar_application_performed = false
actual_Q_extension_defined = false
governance_contract_selected = false
candidate_score_for_actual_candidates_defined = false
candidate_ranking_performed = false
utility_defined = false
reward_defined = false
NO_WARRANTED_ADOPTION_defined = false
adoption_performed = false
authorization_performed = false
binding_performed = false
execution_performed = false
```

The calibration scalar witnesses are synthetic fixture representations only.

---

# 33. Required execution artifacts

A later authorized execution must add exactly three scientific artifacts:

```text
audits/extension_scalar_sufficiency_identification_audit.py
audits/extension_scalar_sufficiency_identification_results.json
audits/extension_scalar_sufficiency_identification_audit.md
```

No dependency-ledger update may occur in the same execution commit.

The correct provenance wording should be:

\[
\boxed{\textbf{
fresh scalar-sufficiency / decision-substrate identification result with frozen upstream preference lineage and hard regression assertions.
}}
\]

The upstream actual-candidate preference graph remains a provenance anchor and future application holdout, not calibration evidence.

---

# 34. Required result serialization

The result JSON must include at minimum:

```text
preregistration_commit
parent_checkpoint
upstream_blob_anchors
actual_graph_holdout_integrity
calibration_fixture_registry
anonymous_encoding_registry
scalar_family_registry
score_domain
burden_schema
family_x_fixture_diagnoses
successful_scalar_witnesses
nonrepresentability_exhaustion_certificates
pair_swap_results
nuisance_invariance_results
broken_control_results
anti_downstream_flags
```

For every family/fixture pair:

```text
exact_relation_match
loss_mismatch_count
authority_injection_count
B_q
B_g
B_auxiliary
B_scalar
B_Rpref
D_scalar
```

No actual candidate score may appear.

---

# 35. Strongest permitted claim after a successful execution

If and only if every success criterion passes, the strongest permitted claim is:

\[
\boxed{
\textbf{
In the audited finite scalar-sufficiency calibration regimes, the sufficiency and contraction status of preregistered bounded scalar-plus-decoder decision substrates is identifiable relative to the typed preference relation and the frozen semantic-obligation ledger: exact decision distinctions are preserved where representable, unauthorized scalar completion is detected, unrestricted lookup is separated from genuine contraction, and governance-relative scalar typing and nuisance invariance are preserved.
}
}
\]

The result may additionally report which tested scalar families earn `FAITHFUL_CONTRACTION`, `REPRESENTABLE_NO_CONTRACTION`, or `NOT_REPRESENTABLE` on each synthetic fixture.

It may not claim:

```text
that scalarization is universally necessary
that scalarization is universally impossible
that the native typed relation is globally minimal
that any actual governance contract admits a scalar contraction
that any actual candidate has a scalar value
that any scalar is a reward
that any candidate should be adopted or authorized
```

---

# 36. Frozen next sequence

The branch is now conceptually:

\[
\boxed{
\begin{aligned}
\mathcal M_{\rm ext}\text{ identification}&\checkmark\\
s\mapsto\mathcal V_{\rm ext}(s)&\checkmark\\
\mathcal R_{\rm compare}\text{ identification}&\checkmark\\
\text{actual native comparison graph}&\checkmark\\
G_{\rm pref}\rightarrow R_{\rm pref}\text{ identification}&\checkmark\\
\text{actual-candidate preference application}&\checkmark\\
\boxed{(R_{\rm pref}^{\rm cal},\mathcal Q_{\rm adm})\rightarrow D_{\rm scalar}}
&\text{ [preregistered here]}\\
\text{scalar-sufficiency identification execution}
&\leftarrow\textbf{next}\\
\text{actual scalar application}
&\text{ undefined}\\
Q_{\rm extension}^{G}\text{ for actual candidates}
&\text{ undefined}\\
Auth&\text{ undefined}\\
Bind&\text{ undefined}.
\end{aligned}
}
\]

No execution of the scalar gate is authorized by this document itself.

The only legitimate next repository mutation after this preregistration is a clean execution of this frozen scalar-sufficiency identification gate.