"""
session.py

QSOL SimulationSession.

Provides a high-level, audit-ready wrapper around the QSOL evolution process,
combining:

- initial state
- target
- transform function
- evolution trace
- stability analysis

This is the orchestration layer for running deterministic, reproducible QSOL
evolution sessions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional

from .absolute_limits import ABSOLUTE_LIMITS
from .evolution import EvolutionStep, evolve_trace
from .quantum_state import QuantumState
from .stability import StabilityReport, analyze_trace


TransformFn = Callable[[float], float]


@dataclass
class SimulationSession:
    """
    A complete QSOL evolution session.

    This class runs a deterministic, PHI-bounded evolution from an initial
    state toward a target using a user-provided transform function, and
    produces both a trace and a stability report.
    """

    initial_value: float
    target: float
    transform: TransformFn

    initial_state: QuantumState = field(init=False)
    trace: List[EvolutionStep] = field(default_factory=list, init=False)
    stability: Optional[StabilityReport] = field(default=None, init=False)
    completed: bool = field(default=False, init=False)

    def __post_init__(self) -> None:
        # Clamp initial value into the invariant domain and construct state.
        clamped = ABSOLUTE_LIMITS.clamp_value(self.initial_value)
        self.initial_state = QuantumState(clamped)

    def run(self) -> None:
        """
        Execute the evolution session, generating a full trace and stability report.

        This method is idempotent: re-running will recompute the trace and report
        from the same initial conditions.
        """
        self.trace = evolve_trace(
            initial=self.initial_state,
            target=self.target,
            fn=self.transform,
        )
        self.stability = analyze_trace(self.trace, self.target)
        self.completed = True

    def final_state(self) -> QuantumState:
        """
        Return the final QuantumState of the session.

        Raises:
            RuntimeError if the session has not been run yet.
        """
        if not self.completed or not self.trace:
            # If no steps were taken, the final state is the initial state.
            if self.completed and not self.trace:
                return self.initial_state
            raise RuntimeError("SimulationSession has not been run yet.")
        return self.trace[-1].next_state

    def report(self) -> str:
        """
        Return a human-readable report of the session outcome.

        Raises:
            RuntimeError if the session has not been run yet.
        """
        if not self.completed or self.stability is None:
            raise RuntimeError("SimulationSession has not been run yet.")
        lines = [
            "QSOL Simulation Session:",
            f"  - initial_value: {self.initial_state.value}",
            f"  - target: {self.target}",
            f"  - steps: {self.stability.steps}",
            f"  - converged: {self.stability.converged}",
            f"  - final_value: {self.stability.final_value}",
            f"  - final_delta: {self.stability.final_delta}",
            f"  - monotonic_increasing: {self.stability.monotonic_increasing}",
            f"  - monotonic_decreasing: {self.stability.monotonic_decreasing}",
        ]
        return "\n".join(lines)

