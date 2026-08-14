# Decision-Substrate Language Identification — Round v1 Application-Set Freeze

## Status

```text
APPLICATION_SET_FROZEN
```

This checkpoint is an identity carry-forward operation only. It does not select, rank, weight, modify, authorize, or execute any treatment language.

## Scientific lineage

```text
characterization_anchor = ddffe4b976352b3fec4efc3300a0dcc0097ca217
```

The scientific state transition is anchored to the characterization checkpoint above. Repository commits after that checkpoint do not alter this scientific anchor merely by changing Git history.

## Frozen application treatment set

The round-v1 application treatment family is exactly the round-v1 decision-substrate treatment family:

\[
\boxed{
\mathfrak L_{\rm app}^{(1)}
=
\mathfrak L_{\rm DS}^{(1)}
}
\]

with exactly these six treatment languages:

```text
L_ORD1
L_RADIUS1
L_BANDS1
L_INTERSECT2
L_POSET
L_SPARSE_LINEAR
```

Equivalently, for every language `L`:

\[
L\in\mathfrak L_{\rm app}^{(1)}
\iff
L\in\mathfrak L_{\rm DS}^{(1)}.
\]

No language is added, removed, substituted, or semantically altered by this checkpoint.

## Binding carry-forward facts

```text
carry_forward_is_identity              = true
characterization_dependent_filtering   = false
characterization_dependent_weighting   = false
language_semantics_modified            = false
application_priority_assigned          = false
cross_language_ranking_performed       = false
```

The characterization result is not an input to application-set membership:

\[
\boxed{
\Phi_{\mathfrak L^{(1)}}(K)
\not\rightarrow
\mathfrak L_{\rm app}^{(1)}
}
\]

In particular, characterization outcomes do not determine treatment inclusion, exclusion, weighting, priority, semantics, or cross-language rank.

## Scope boundary

This checkpoint contains no target access and defines no actual-application mechanics.

It does not define or perform:

```text
actual-target access
actual-application evaluation
Q_extension
cross-language winner selection
authorization
binding
execution
```

Those operations remain downstream and unreachable from this application-set freeze.

## Interpretation

This artifact freezes only the treatment set carried into the next preregistration step. It is a procedural scientific-lineage checkpoint, not application evidence and not authorization evidence.
