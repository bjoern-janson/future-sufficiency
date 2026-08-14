"""H1_V2_R1 minimal implementation repair after SpecComplete failure.

This module preserves the implementation constructed at
`ddfbeea03d657de909fbd2f9a1d47232f56f1642` and changes exactly one
implementation-semantic detail identified by the conformance audit at
`06d20b30597eb246c1616d6b51a032d518eb7d8d`:

    hexadecimal identity masking must apply only to standalone tokens.

It does not alter the frozen preregistration, scientific state universe,
reconstruction target, authority regime, packet boundary, reconstruction
protocol, collision protocol, result ontology, or claim authority. Importing
this module performs no scientific execution.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

BASE_IMPLEMENTATION_COMMIT = "ddfbeea03d657de909fbd2f9a1d47232f56f1642"
FAILED_CONFORMANCE_COMMIT = "06d20b30597eb246c1616d6b51a032d518eb7d8d"
REPAIR_SCOPE = "L2_STANDALONE_HEXADECIMAL_TOKEN_BOUNDARY_ONLY"

_base_path = Path(__file__).with_name("h1_v2_framework_legibility_implementation.py")
_spec = importlib.util.spec_from_file_location("h1_v2_framework_legibility_base", _base_path)
if _spec is None or _spec.loader is None:
    raise RuntimeError("unable to load frozen H1 implementation base")
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

# Frozen preregistration rule: mask standalone hexadecimal tokens of length
# 7 through 64. The failed implementation excluded adjacency only to other
# hex characters, which could mask a hex-looking substring embedded in a word.
# Alphanumeric/underscore adjacency therefore blocks masking.
_base._HEX_RE = re.compile(
    r"(?<![0-9A-Za-z_])[0-9A-Fa-f]{7,64}(?![0-9A-Za-z_])"
)

# Re-export the repaired realization. Function objects retain the base
# module's globals, including the repaired _HEX_RE above.
for _name in dir(_base):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_base, _name)

IMPLEMENTATION_STATE = dict(_base.IMPLEMENTATION_STATE)
IMPLEMENTATION_STATE["H1_V2_IMPLEMENTATION_REPAIRED"] = True
IMPLEMENTATION_STATE["H1_V2_SPECCOMPLETE"] = False
IMPLEMENTATION_STATE["H1_V2_EXECUTION_AUTHORIZED"] = False

REPAIR_PROVENANCE = {
    "base_implementation_commit": BASE_IMPLEMENTATION_COMMIT,
    "failed_conformance_commit": FAILED_CONFORMANCE_COMMIT,
    "repair_scope": REPAIR_SCOPE,
    "scientific_design_revision": False,
    "reconstruction_evidence_seen": False,
    "collision_evidence_seen": False,
}

# No __main__ entry point. The repaired realization must pass the same
# SpecComplete / independent-confluence gate before execution authorization.
