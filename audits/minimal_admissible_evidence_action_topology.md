# Minimal Admissible Evidence-Action Topology Audit

Status: post-`3f81e679` epistemic minimality audit of the frozen future-sufficiency architecture.

This is **not Experiment 009**, does not extend the capability ladder, and initially contains **no adaptive learner**.

## Question

What is the weakest admissible evidence-action topology under which the warranted meta-action

    {DISCRIMINATE, REOPEN, STOP}

is identifiable?

The audit separates:

    can know
    -> does know
    -> can act
    -> is authorized to act

and tests only the first term.

No hypothesis learner, repair constructor, model-selection policy, or persistence mechanism is evaluated.

## Governing distinction

The audit treats these as different scientific objects:

    G_epistemic != G_repair

`G_epistemic` asks whether the evidence-action interface exposes enough information for the required distinction to be identifiable.

`G_repair` asks whether a mechanism can exploit that distinction once it is available.

A failure of the first must not be reported as an inference or intelligence failure.

## Identifiability criterion

For worlds `W_A` and `W_B`, let

    W_A ~_{E,A} W_B

mean that the two worlds have the same evidence signature under the currently available admissible evidence/action topology.

The topology is sufficient for the declared repair contract when:

    W_A ~_{E,A} W_B
    ->
    a*(W_A) = a*(W_B)

for every pair of worlds in the finite audit universe.

An epistemic quotient defect occurs when:

    W_A ~_{E,A} W_B
    and
    a*(W_A) != a*(W_B).

Such a pair is an impossibility witness for any policy restricted to that topology.

## Finite world universe

The evaluator defines five worlds:

| World | Required action | Residual | Exact H0 alternative | Deterministic residual | Positive reopen value |
|---|---:|---:|---:|---:|---:|
| `D_resolvable` | D | 1 | 1 | 1 | 1 |
| `R_unrepresentable` | R | 1 | 0 | 1 | 1 |
| `S_zero_value` | S | 1 | 0 | 1 | 0 |
| `S_irreducible` | S | 1 | 0 | 0 | 1 |
| `S_adequate` | S | 0 | 0 | 1 | 1 |

The four binary distinctions are chosen so that each separates `R_unrepresentable` from exactly one different-action witness world while holding the other three distinctions fixed.

This makes single-component necessity directly testable by equivalence collapse rather than by learner performance.

## Candidate admissible topology

The feasible evidence-action contract admits four components:

1. `local_residual`
   - passive observation;
   - exposes whether a residual is present.

2. `alternative_fit_probe`
   - active authorized challenge;
   - exposes whether an exact alternative already exists inside the current language.

3. `consistency_probe`
   - active authorized challenge;
   - exposes whether repeated residual evidence is deterministic rather than contradictory under the declared contract.

4. `future_value_probe`
   - active authorized challenge;
   - exposes whether reopening has positive validated future value.

The active challenge contract requires:

    component cost <= 2
    component risk <= 1
    reversible = True
    authorized = True

Passive evidence is admitted directly.

The partial order for this first audit is set inclusion over admissible components.

## Pure minimality intervention

For each admissible component `e_i`:

    remove(e_i)
    -> recompute evidence equivalence classes
    -> test whether different required actions collapse into one class

No adaptive behavior is involved.

A component earns necessity in this finite contract only if its removal creates an explicit witness pair:

    same remaining evidence signature
    + different required meta-actions.

## Preregistered witness pairs

### Remove `local_residual`

Expected collapse:

    R_unrepresentable ~ S_adequate

while:

    R != S.

The other three observable distinctions are identical for this pair.

### Remove `alternative_fit_probe`

Expected collapse:

    D_resolvable ~ R_unrepresentable

while:

    D != R.

This tests whether within-language resolvability must be observable before `DISCRIMINATE` can be distinguished from `REOPEN`.

### Remove `consistency_probe`

Expected collapse:

    R_unrepresentable ~ S_irreducible

while:

    R != S.

This tests whether deterministic unrepresentability can be distinguished from irreducible contradiction.

### Remove `future_value_probe`

Expected collapse:

    R_unrepresentable ~ S_zero_value

while:

    R != S.

This tests whether positive reopen value must be identifiable before reopening can be warranted.

## Admissibility control

Identifiability must be defined relative to what the loop is actually permitted to do.

The audit therefore includes four deliberately inadmissible oracle components. Each reveals the required action directly, and each is sufficient **if illegally admitted**, but each violates exactly one feasibility constraint:

- `unauthorized_oracle` — not authorized;
- `too_costly_oracle` — cost exceeds the contract;
- `risky_oracle` — risk exceeds the contract;
- `irreversible_oracle` — challenge is irreversible.

This control attacks the degenerate theoretical move:

    imagine an omnipotent intervention
    -> declare the distinction identifiable.

The correct object is identifiability under the admissible evidence-action regime.

## Exhaustive local result

The standard-library implementation exhaustively enumerates all subsets of the four admissible components.

The full topology is sufficient.

There is exactly one inclusion-minimal sufficient topology:

    {
      local_residual,
      alternative_fit_probe,
      consistency_probe,
      future_value_probe
    }

Each single-component ablation makes the topology insufficient with the preregistered witness:

    -local_residual
        -> R_unrepresentable == S_adequate on remaining evidence
        -> required actions R vs S

    -alternative_fit_probe
        -> D_resolvable == R_unrepresentable on remaining evidence
        -> required actions D vs R

    -consistency_probe
        -> R_unrepresentable == S_irreducible on remaining evidence
        -> required actions R vs S

    -future_value_probe
        -> R_unrepresentable == S_zero_value on remaining evidence
        -> required actions R vs S

All four inadmissible oracle shortcuts are individually sufficient if their violated feasibility constraint is ignored.

No GitHub Actions CI claim is made; this is a local deterministic execution result.

## What this audit can earn

The narrow result is:

> In this finite deterministic repair contract, the four-component admissible evidence-action topology is inclusion-minimal for identifying the evaluator-defined D/R/S response classes. Removing any one admissible component creates an explicit observational equivalence class containing worlds that require different actions.

Equivalently:

    availability failure
    -> identifiability failure

can be demonstrated without training or evaluating an agent.

This is a minimality certificate for epistemic access under the declared finite contract.

## What it does not earn

It does **not** establish:

- that these four literal evidence components are universally necessary;
- that the same topology recurs across task families;
- general active causal identifiability;
- optimal challenge selection;
- learner recovery of the available distinctions;
- hypothesis-language repair;
- repair authorization or execution;
- substrate-independent corrigibility;
- autonomous authority expansion.

The evaluator still supplies:

- the finite world set;
- the required D/R/S action labels;
- the semantics of each evidence component;
- the deterministic observation contract;
- the admissibility thresholds for cost, risk, reversibility, and authority.

These remain explicit scaffold.

## Interpretation rule

The result must be classified as an epistemic minimality result, not a repair-capability result.

Use the ordering:

    availability
    -> identifiability
    -> inference
    -> repair authorization
    -> execution

Only the first two are addressed here.

If an ablation produces:

    same admissible evidence
    + different required action,

then the resulting failure is an interface / identifiability boundary. Do not attribute it to weak inference.

## Reproducibility

From the repository root:

```bash
python audits/minimal_admissible_evidence_action_topology.py
```

The implementation uses only the Python standard library and is exhaustive and deterministic.

**Scientific rule:** identifiability first, repair second.
