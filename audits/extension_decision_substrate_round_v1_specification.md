# Decision-Substrate Language Identification — Round v1 Construction Specification

## Status

This artifact instantiates exactly one candidate decision-substrate identification round:

\[
\boxed{
\mathcal R^{(1)}
=
\left(
\mathfrak L_{\rm DS}^{(1)},
\mathfrak K_{\rm cal}^{(1)},
A_{\rm DS}^{(1)},
B_{\rm DS}^{(1)},
\Pi_{\rm closure}^{(1)},
\Sigma_{\rm outcome}^{(1)}
\right).
}
\]

Parent checkpoints:

```text
specification-completeness gate
  54105e9b1d12997dc91950f2e034faa9ff4c9945

round firewall
  7e4e97aa9c5fe54b449f2ad82a7b1528f448106c

decision-substrate architecture
  fe21bbe2cd48bd71011674edd16488b5a492f291

serialization erratum
  9ee1fd5f49f2dc43889894b9617ea9333077dd05
```

Round identifier:

```text
round_id      DSLI_R1
round_version 1
```

This is a **construction/specification commit**, not a characterization commit.

The frozen construction-state flags are:

```text
concrete_language_universe_instantiated = true
calibration_world_instantiated          = true
round_specification_complete            = false
characterization_authorized             = false
characterization_executed               = false
application_set_frozen                  = false
actual_target_application_preregistered = false
actual_target_application_performed     = false
actual_Q_extension_defined              = false
```

The round must next be submitted to the already-frozen `SpecComplete` gate.

---

# 1. Governing construction boundary

The binding distinction is:

\[
\boxed{
\text{instantiate}
\neq
\text{characterize}.
}
\]

This commit may define the complete treatment family, witness domains, syntax,
semantics, authority, burden, closure/minimum procedures, calibration world,
conformance fixtures, runtime envelope, and hashes.

It may not apply the treatment languages to the calibration world and may not
emit any of:

```text
NOT_REPRESENTABLE
REPRESENTABLE_AUTHORITY_INVALID
ADMISSIBLE_REPRESENTATION_NO_CONTRACTION
FAITHFUL_CONTRACTION
```

for any calibration case.

The construction dependency graph excludes all actual application targets.
No actual candidate relation, actual pair-level topology, actual mismatch
neighborhood, or actual-graph-derived parameter is an input to this round.

The design rationale is structural:

```text
one-dimensional order
one-dimensional typed abstention
finite global distance bands
intersection of two total orders
arbitrary finite partial order
bounded explicit relational state
```

No round-v1 primitive is justified by repairing a known actual-target edge.

---

# 2. Target relation type

For anonymous candidate universe:

\[
S_n=\{0,\ldots,n-1\},
\]

the target is a complete typed relation over:

\[
\mathfrak P(S_n)=\{(i,j):0\le i<j<n\}.
\]

The token set is exactly:

```text
PREFER_I
PREFER_J
EQUIVALENT
NO_WARRANTED_PREFERENCE
```

Pair swap is exact:

```text
PREFER_I                 <-> PREFER_J
PREFER_J                 <-> PREFER_I
EQUIVALENT                 -> EQUIVALENT
NO_WARRANTED_PREFERENCE    -> NO_WARRANTED_PREFERENCE
```

Native target burden remains:

\[
\boxed{
B_R=\binom n2.
}
\]

---

# 3. Frozen treatment set

The round-v1 treatment family is exactly:

\[
\boxed{
\mathfrak L_{\rm DS}^{(1)}
=
\{
L_{\rm ORD1},
L_{\rm RADIUS1},
L_{\rm BANDS1},
L_{\rm INTERSECT2},
L_{\rm POSET},
L_{\rm SPARSE\_LINEAR}
\}.
}
\]

Machine identifiers:

```text
L_ORD1
L_RADIUS1
L_BANDS1
L_INTERSECT2
L_POSET
L_SPARSE_LINEAR
```

This is a treatment set, not a candidate pool.

No member may be added, removed, widened, narrowed, or conditionally activated
from round-v1 outcomes.

---

# 4. `L_ORD1` — one-dimensional ordered substrate

Witness:

\[
h=(q_0,\ldots,q_{n-1})
\]

with:

```text
q_i integer
0 <= q_i <= n-1
min(q) = 0
```

Decoder:

\[
q_i=q_j \Rightarrow EQUIVALENT,
\]

\[
q_i>q_j \Rightarrow i\succ j,
\qquad
q_i<q_j \Rightarrow j\succ i.
\]

`NO_WARRANTED_PREFERENCE` is unreachable.

Burden:

```text
B_state      n
B_decoder    3
B_auxiliary  0
B_selector   0
B_exception  0
```

so:

\[
\boxed{B_{ORD1}=n+3.}
\]

Unrestricted closure certification is algebraic:

1. `EQUIVALENT` must induce a lawful equivalence partition.
2. Every cross-block relation must be homogeneous.
3. NWP must be absent on the quotient.
4. The complete directional quotient must be acyclic.
5. A complete acyclic quotient has a unique total order and therefore an exact
   normalized rank witness in `0..n-1`.

Negative membership is exact, not search absence.

All legal `L_ORD1` state is declared and counted, so any exact legal witness is
authority-admissible.

All exact witnesses have the same burden `n+3`; therefore the burden minimum is
fixed once exact admissible membership is certified.

---

# 5. `L_RADIUS1` — one global abstention radius

Witness:

\[
h=(q,\tau)
\]

with the same normalized `q` domain and:

```text
tau integer
0 <= tau <= n-1
```

Decoder:

\[
q_i=q_j \Rightarrow EQUIVALENT,
\]

\[
0<|q_i-q_j|\le\tau
\Rightarrow
NO\_WARRANTED\_PREFERENCE,
\]

otherwise the sign of `q_i-q_j` supplies direction.

Burden:

```text
B_state      n
B_decoder    4
B_auxiliary  1
```

hence:

\[
\boxed{B_{RADIUS1}=n+5.}
\]

Exact unrestricted closure uses complete finite enumeration after quotienting
lawful equivalence classes:

- inject the `c` equivalence classes into distinct scores in `0..n-1`;
- require minimum used score `0`;
- enumerate every `tau in 0..n-1`;
- decode every pair;
- exact equality with the target is membership;
- complete exhaustion is nonmembership.

No heuristic pruning is licensed.

Every legal exact witness is admissible.

All exact witnesses have burden `n+5`; the complete set of exact witnesses is
the minimum-witness set.

---

# 6. `L_BANDS1` — three global distance bands

Witness:

\[
h=(q,\tau_1,\tau_2,p_1,p_2,p_3)
\]

with:

```text
q_i in {0,...,n-1}
min(q)=0
0 <= tau_1 <= tau_2 <= n-1
p_k in {DIRECTION, NWP}
```

For nonzero distance `d=|q_i-q_j|`:

```text
band 1: d <= tau_1
band 2: tau_1 < d <= tau_2
band 3: d > tau_2
```

`DIRECTION` uses the sign of the score difference.
`NWP` emits `NO_WARRANTED_PREFERENCE`.
Zero distance always emits `EQUIVALENT`.

Burden:

```text
B_state      n
B_decoder    5
B_auxiliary  2
```

hence:

\[
\boxed{B_{BANDS1}=n+7.}
\]

Exact unrestricted closure enumerates:

- every normalized equivalence-class score injection;
- every `tau_1 <= tau_2`;
- every one of the `2^3` band-policy tuples.

Complete exhaustion certifies nonmembership.

Every legal exact witness is admissible.
Every exact witness has burden `n+7`.

---

# 7. Canonical equivalence-partition representation

The remaining three treatment languages use explicit equivalence blocks.

A partition is stored by **canonical star merges**.

For every block:

```text
root = smallest anonymous candidate handle in the block
store exactly root -> x for every other x in the block
```

A partition with `c` blocks therefore contains exactly:

\[
n-c
\]

merge obligations.

This is not an implementation compression trick. Each merge is explicit,
anonymous, pair-addressed semantic state and contributes one burden obligation.

Under candidate permutation, the partition is transported and then recanonicalized;
candidate-handle choice itself has no authority.

---

# 8. `L_INTERSECT2` — intersection of two total orders

Witness:

```text
merges  canonical equivalence-partition star merges
order1  permutation of canonical block roots, best to worst
order2  permutation of canonical block roots, best to worst
```

Let `c` be the number of blocks.

Decoder:

```text
same block:
  EQUIVALENT

block A before B in both total orders:
  prefer A

block B before A in both:
  prefer B

orders disagree:
  NO_WARRANTED_PREFERENCE
```

This is a two-order partial-order substrate. It is not a scalar with another
post-hoc exception rule.

Burden:

```text
partition merges        n-c
order-1 rank state      c
order-2 rank state      c
decoder obligations     5
```

thus:

\[
\boxed{
B_{INTERSECT2}=n+c+5.
}
\]

Exact closure procedure:

1. certify lawful equivalence and homogeneous quotient;
2. directional quotient must be acyclic and transitively closed;
3. enumerate every linear extension as candidate `order1`;
4. for each target-NWP pair, force `order2` to reverse `order1`;
5. for each target directional pair, force `order2` to preserve direction;
6. exact acyclicity/topological enumeration decides whether an `order2` exists;
7. retain every exact `(order1,order2)` witness.

Completeness follows because in any exact two-order intersection, `order1` is a
linear extension of every target direction and every target-incomparable pair
must be reversed by `order2`.

All legal exact witnesses are admissible.

Given the quotient block count, every exact witness has the same burden.

---

# 9. `L_POSET` — arbitrary finite partial order

Witness:

```text
merges  canonical partition star merges
cover   sorted unique directed cover edges between block roots
```

The cover graph must be:

```text
acyclic
transitively reduced
```

Decoder:

```text
same block:
  EQUIVALENT

path A -> B:
  prefer A

path B -> A:
  prefer B

no path:
  NO_WARRANTED_PREFERENCE
```

Burden:

```text
partition merges        n-c
cover edges             |E_cover|
decoder obligations     5
```

therefore:

\[
\boxed{
B_{POSET}
=
(n-c)+|E_{\rm cover}|+5.
}
\]

Exact closure certification:

1. certify lawful equivalence and homogeneous quotient;
2. quotient directions must be acyclic;
3. quotient directions must already equal their transitive closure;
4. compute the unique finite-DAG transitive reduction;
5. that reduction is the exact witness.

If the target direction relation is cyclic or not transitive, it lies outside
this language's unrestricted closure.

The partition and transitive reduction are unique under frozen semantics, so
the exact admissible witness and its burden are unique.

---

# 10. `L_SPARSE_LINEAR` — bounded explicit relational substrate

Witness:

```text
merges  canonical partition star merges
edges   sorted unique directed cross-block edges
```

Constraints:

```text
no reciprocal directed pair
|edges| <= n-1
```

All unspecified cross-block pairs default to:

```text
NO_WARRANTED_PREFERENCE
```

No transitive closure is applied.

Thus cycles are legal when they fit inside the frozen edge budget.

The bound:

\[
\boxed{|E|\le n-1}
\]

is fixed before calibration and is justified as an `O(n)` explicit relational
state family, not by any actual application edge count.

Burden:

```text
partition merges        n-c
direct directional      |E|
decoder obligations     5
```

so:

\[
\boxed{
B_{SPARSE}
=
(n-c)+|E|+5.
}
\]

Exact closure is algebraic:

1. certify lawful equivalence and homogeneous quotient;
2. collect the unique quotient directional pair set;
3. membership iff its size is at most `n-1`.

The exact witness is unique, and therefore the minimum burden is exact.

Explicit pair-addressed state is admissible because it is declared, anonymous,
transportable, and fully counted.

Hidden identity lookup remains forbidden.

---

# 11. Frozen controls

Controls are not treatment-family members.

## `W_DIRECT_LOOKUP`

Witness:

```text
one explicit target token per canonical unordered pair
```

It represents every finite complete relation.

It is admissible because all pair state is explicit and counted.

Burden:

\[
\boxed{
B_{DIRECT}=B_R+1.
}
\]

Its role is:

```text
unrestricted representability positive control
admissibility positive control
contraction negative control
```

## `W_IDENTITY_ORACLE`

This control indexes a complete relation table by forbidden semantic candidate
identities rather than anonymous transportable pair state.

It is extensionally capable of exact reproduction, but:

```text
Rep   = true
Rep^A = false
```

by construction.

Its frozen authority violation is:

```text
UNLICENSED_CANDIDATE_IDENTITY
```

Burden is not evaluated because the authority gate fails first.

---

# 12. Authority regime `A_DS^(1)`

Every decoder-visible channel has exactly one status:

```text
LICENSED_AND_COUNTED
LICENSED_COMMON_INFRASTRUCTURE
FORBIDDEN
NOT_AVAILABLE
```

Licensed common infrastructure:

```text
anonymous candidate handles
canonical unordered-pair addressing
```

Licensed and counted state includes the explicit fields declared by each
language:

```text
scalar scores
thresholds/cutpoints
band policies
partition merges
order ranks
cover edges
sparse direct edges
```

Forbidden:

```text
semantic candidate identity
candidate provenance
display aliases
candidate hashes/nonces
serialization position
implementation tags
actual-target lookup
actual-target mismatch features
```

Not available to treatment decoders:

```text
upstream measurement state
upstream comparison state
upstream preference artifacts
network state
current time
learned/adaptive state
```

Every legal treatment witness is therefore authority-admissible.
The identity-oracle control is not.

Required invariance:

```text
candidate permutation equivariance
pair-swap equivariance
serialization-order invariance
alias invariance
nonce invariance
provenance-label invariance
implementation-tag invariance
```

---

# 13. Burden regime `B_DS^(1)`

The burden codomain is the nonnegative integers.

Every witness burden decomposes as:

\[
B(h)=
B_{\rm state}
+
B_{\rm decoder}
+
B_{\rm auxiliary}
+
B_{\rm selector}
+
B_{\rm exception}.
\]

The language-specific formulas above are exhaustive.

Excluded common infrastructure is exactly:

```text
anonymous candidate registry
canonical unordered-pair enumeration
four-token vocabulary
pair-swap convention
JSON container syntax
```

The following never reduce semantic burden:

```text
file compression
byte packing
variable renaming
compiler optimization
runtime memory layout
hash-map representation
shared implementation code
```

No hidden macro or inherited semantic state is free.

---

# 14. Tripartite certification regime `Pi_closure^(1)`

For every treatment language:

\[
\boxed{
\Pi_{\mathcal L}
=
(
\Pi^{unrestricted}_{\mathcal L},
\Pi^{admissible}_{\mathcal L},
\Pi^{minimum}_{\mathcal L}
).
}
\]

These prove different propositions.

## `Pi_unrestricted`

Decides exactly:

\[
R\in Cl_{\mathcal L}
\quad\text{or}\quad
R\notin Cl_{\mathcal L}.
\]

No timeout, optimizer failure, near miss, or best mismatch may certify
nonmembership.

## `Pi_admissible`

After unrestricted membership:

\[
R\in Cl^A_{\mathcal L}
\quad\text{or}\quad
R\notin Cl^A_{\mathcal L}.
\]

For round-v1 treatment languages, all legal declared witness state is admissible,
so a legal exact witness is an admissible exact witness.

The authority-invalid control remains separate.

## `Pi_minimum`

After admissible membership, certifies:

\[
B^*_{\mathcal L}(R)
=
\min_{h\in H^A_{\mathcal L}(R)}B(h).
\]

For fixed-burden finite-enumeration languages, every exact witness is retained.
For structural languages with unique exact state, the unique canonical witness
is the minimum certificate.

No canonical witness is used as a substitute for a missing lower-bound argument.

---

# 15. Frozen scientific outcome map

The classifier is unchanged:

```text
Rep = 0
  -> NOT_REPRESENTABLE

Rep = 1 and Rep^A = 0
  -> REPRESENTABLE_AUTHORITY_INVALID

Rep^A = 1 and B_star >= B_R
  -> ADMISSIBLE_REPRESENTATION_NO_CONTRACTION

Rep^A = 1 and B_star < B_R
  -> FAITHFUL_CONTRACTION
```

This classifier is defined here but is **not applied to the calibration world in
this construction commit**.

---

# 16. Calibration world `K_cal^(1)`

Candidate counts are exactly:

```text
n = 6
n = 7
```

The round uses a finite deterministic panel:

```text
26 anonymous relations
13 matched two-case blocks
no sampling
no RNG
no adaptive stopping
```

Every relation is materialized in the committed calibration-world JSON.

Structural descriptor axes:

```text
T_dir
T_abst
T_eq
T_comp
T_conn
T_dim
N
C_Sigma
```

`C_Sigma` is the exact four-token count vector.

The intended calibration claim scope is finite support unless a later exact
proof covers a larger class.

---

# 17. Matched structural blocks

For each `n in {6,7}`, the world contains the following two-case blocks.

## `DIR_TOPOLOGY_N{n}`

Manipulated:

```text
T_dir
```

Cases:

```text
TOTAL_ORDER
CYCLIC_TOURNAMENT
```

Held fixed:

```text
T_abst
T_eq
T_comp
T_conn
T_dim
N
C_Sigma
```

The total-order anonymous ranking is chosen solely to match the canonical
`PREFER_I/PREFER_J` token count of the cyclic tournament. Candidate handles
carry no semantic meaning.

## `ABST_TOPOLOGY_N{n}`

Manipulated:

```text
T_abst
```

Cases:

```text
MONOTONE_LOCAL
CROSS_CUT
```

Both remove exactly `n-1` pairs from the same anonymous directional order.

Held fixed:

```text
T_dir
T_eq
T_comp
T_conn
T_dim
N
C_Sigma
```

## `EQ_LAWFULNESS_N{n}`

Manipulated:

```text
T_eq
```

Cases:

```text
LAWFUL_PARTITION
NONTRANSITIVE_TOKEN
```

Both contain exactly two `EQUIVALENT` pair tokens and all remaining pairs NWP.

The nontransitive control has:

```text
0 ~ 1
1 ~ 2
0 ? 2 = NWP
```

## `CONNECTIVITY_N{n}`

Manipulated:

```text
T_conn
```

Cases:

```text
one directed cycle spanning all candidates
two disjoint directed cycles
```

Resolved-edge count and canonical token count vector are matched.

## `TRANSITIVITY_N{n}`

Manipulated:

```text
T_dir
```

Cases:

```text
PARTIAL_ORDER
ACYCLIC_NONTRANSITIVE
```

Both contain exactly six directional pairs and all other pairs NWP.

The partial-order case is the transitive closure of a four-element chain plus
isolates.

The nontransitive case is an acyclic six-edge relation containing a frozen
transitivity violation.

## `CARDINALITY_STRESS_N{n}`

Manipulated:

```text
C_Sigma
```

The structural class is held fixed:

```text
ORDER_CONSISTENT_ACYCLIC
MONOTONE_LOCAL abstention
SINGLE_AXIS
ONE_DIMENSIONAL generator tag
```

The sparse member resolves only pairs with index gap at least `3`.
The dense member resolves every pair with index gap at least `2`.

This block is explicitly for distinguishing relation cardinality effects from
changes in declared geometry class.

---

# 18. Product-geometry structural contrast

At `n=6` the world additionally contains:

```text
PRODUCT_GEOMETRY_N6_A_PRODUCT
PRODUCT_GEOMETRY_N6_B_SINGLE_AXIS
```

Both have matched token counts.

The product case is the exact componentwise order on the anonymous `2 x 3`
integer grid.

The comparison case is a one-dimensional order with exactly three NWP pairs.

This is explicitly a **multi-axis structural contrast**:

```text
T_dir
T_abst
T_comp
T_dim
```

It is not licensed as a one-factor discriminant.

---

# 19. Calibration generator determinism

All 26 relation tables are committed.

The reference generator is also frozen and must regenerate byte-equivalent
canonical relation content.

There is:

```text
no sampling seed
no random choice
no outcome-dependent generation
no case rejection
no resampling
no performance weighting
```

Generator order is binding.

Duplicate relation payloads, if any, may be retained only when they belong to
distinct preregistered structural blocks and remain distinctly labeled.

---

# 20. Nuisance world

Every calibration relation has exactly:

```text
64 deterministic nuisance encodings
```

Encoding index:

```text
0..63
```

Each encoding deterministically derives from SHA-256:

```text
candidate permutation
pair-record serialization order
display aliases
opaque nonce
implementation tag
```

No RNG is used.

These nuisance fields must not change:

```text
target relation semantics
unrestricted closure result
admissible closure result
B_star
terminal state
```

Pair-swap testing is exhaustive:

```text
every canonical unordered pair
both orientations
PREFER_I <-> PREFER_J
EQUIVALENT fixed
NWP fixed
```

---

# 21. Specification-conformance fixtures

The committed conformance fixture set is labeled:

```text
SPECIFICATION_CONFORMANCE_EVIDENCE
```

It is not calibration evidence and may not be promoted to calibration evidence.

The fixture registry tests:

```text
L_ORD1 decoding and burden
L_RADIUS1 decoding and burden
L_BANDS1 decoding and burden
L_INTERSECT2 decoding and burden
L_POSET decoding and burden
L_SPARSE_LINEAR decoding and burden
W_DIRECT_LOOKUP authority-positive behavior
W_IDENTITY_ORACLE authority-negative behavior
exact positive/negative closure golden cases
```

These fixtures test interpretation of the frozen specification.

They do not estimate the treatment-family response over `K_cal^(1)`.

---

# 22. Implementation-confluence plan

`SpecComplete` must not be certified merely because the reference implementation
agrees with itself.

The frozen plan requires a second implementation that:

```text
does not import the reference implementation;
derives semantics from the committed specification artifacts;
implements the same six treatments and two controls independently.
```

Before `SpecComplete`, the two implementations must compare:

1. every committed conformance fixture;
2. exact generated calibration-world SHA-256;
3. exhaustive complete four-token target relations at `n=4`.

At `n=4`:

\[
4^{\binom42}
=
4^6
=
4096
\]

complete target relations are exhaustively available.

For every treatment language and all 4096 targets, confluence must agree on:

```text
unrestricted closure membership
admissible closure membership
B_star when defined
terminal classifier input/output
```

Minimum witnesses need only agree up to the frozen witness semantics and exact
burden when multiple equivalent encodings exist.

This exhaustive `n=4` world is **conformance evidence**, not round-v1
calibration evidence.

---

# 23. Runtime/reproducibility envelope

Reference runtime:

```text
CPython 3.12.11
Python standard library only
```

Scientific semantics use:

```text
exact integers
exact discrete graph operations
no floating point
no numerical tolerance
no network
no current-time input
no unseeded randomness
```

Canonical JSON:

```text
UTF-8
sort_keys=true
separators=(",",":")
ensure_ascii=false
```

Hash algorithm:

```text
SHA-256
```

All output-affecting iteration is explicitly sorted or otherwise frozen.

No post-freeze learned table, adaptive cache, solver hint, model state, or
generated exception table may change semantic results.

Ordinary performance caching is allowed only when semantics-preserving.

---

# 24. Actual-target exclusion

The round construction is blind by contract to all downstream actual application
relations.

The reference code has no file-loading route for actual preference artifacts.

Forbidden design inputs include:

```text
actual candidate identities
actual pair identities
actual relation token tables
actual mismatch neighborhoods
actual near-miss witnesses
actual graph-derived threshold values
actual graph-derived dimensions
actual graph-derived edge budgets
```

The only downstream actual-target fact relevant here is the prohibition itself.

No treatment-language parameter is selected from actual application geometry.

---

# 25. Construction artifacts

The round bundle contains:

```text
extension_decision_substrate_round_v1_specification.md
extension_decision_substrate_round_v1_specification.json
extension_decision_substrate_round_v1_reference.py
extension_decision_substrate_round_v1_calibration_world.json
extension_decision_substrate_round_v1_conformance_fixtures.json
extension_decision_substrate_round_v1_manifest.json
```

The manifest binds SHA-256 and Git blob identifiers for every non-manifest file
and records a composite bundle hash.

The machine-readable JSON and reference Python are authoritative complements to
this prose specification.

If the prose and machine specification disagree, the later `SpecComplete`
execution must stop rather than choose one interpretation.

---

# 26. What this construction does not establish

This commit does **not** establish:

```text
SpecComplete = true
CHARACTERIZATION_AUTHORIZED
any language's closure on any calibration relation
any language's admissible closure on any calibration relation
any B_star on any calibration relation
any terminal Sigma_outcome on any calibration relation
any language ranking
any application-set selection
any actual-target result
any governance preference
any candidate ranking/adoption
Q_extension
authorization
binding
execution
```

Construction success is not characterization success.

---

# 27. Required next transition

The only licensed next gate is:

\[
\boxed{
\text{round-v1 construction}
\rightarrow
\operatorname{SpecComplete}(\mathcal R^{(1)}).
}
\]

If:

\[
\operatorname{SpecComplete}=0,
\]

emit only:

```text
STOP_SPECIFICATION_REPAIR_REQUIRED
```

and repair the specification before any calibration outcome exists.

If:

\[
\operatorname{SpecComplete}=1,
\]

emit:

```text
CHARACTERIZATION_AUTHORIZED
```

and only then execute the treatment family over the frozen 26-case calibration
world.

---

# 28. Stop condition

Stop after committing the complete round-v1 construction bundle.

Do not in the same commit:

```text
run treatment languages against calibration cases
summarize which language represents which calibration relation
compute the calibration response surface
compute calibration B_star values
emit calibration terminal states
run actual-target application
freeze an application set
change treatment-family membership
change calibration cases
define Q_extension
rank candidates
select governance
adopt
authorize
bind
execute
```

The next artifact is the **round-v1 specification-completeness execution**.

---

# 29. Governing invariant

\[
\boxed{\textbf{
Specification determines the experiment; characterization determines the result.
}}
\]

At this checkpoint, the experiment has been instantiated but not yet licensed to
produce a result.
