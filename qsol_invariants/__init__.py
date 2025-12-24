"""
qsol_invariants

Canonical QSOL invariant contract and evolution core.

This package exposes the public API for:
- AbsoluteLimits (invariant contract)
- QuantumState (state container)
- evolve, evolve_until, evolve_trace (PHI-bounded evolution operators)
- analyze_trace (stability analysis)
- SimulationSession (high-level orchestration)
"""

from .absolute_limits import AbsoluteLimits, ABSOLUTE_LIMITS
from .quantum_state import QuantumState
from .evolution import evolve, evolve_until, evolve_trace
from .stability import analyze_trace, StabilityReport
from .session import SimulationSession

__all__ = [
    "AbsoluteLimits",
    "ABSOLUTE_LIMITS",
    "QuantumState",
    "evolve",
    "evolve_until",
    "evolve_trace",
    "analyze_trace",
    "StabilityReport",
    "SimulationSession",
]

