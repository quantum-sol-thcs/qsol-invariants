"""
stability.py

QSOL stability and convergence analysis.

Provides tools to analyze evolution traces for:

- convergence status
- final delta
- monotonicity
- step counts

These functions are pure, deterministic, and side-effect free.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .absolute_limits import ABSOLUTE_LIMITS
from .evolution import EvolutionStep
from .quantum_state import QuantumState


@dataclass(frozen=True)
class StabilityReport:
    """
    Summary of stability properties for an evolution process.
    """

    converged: bool
    steps: int
    initial_value: float
    final_value: float
    final_delta: float
    monotonic_increasing: bool
    monotonic_decreasing: bool

    def describe(self) -> str:
        """
        Human-readable description of the stability outcome.
        """
        lines = [
            "QSOL Stability Report:",
            f"  - converged: {self.converged}",
            f"  - steps: {self.steps}",
            f"  - initial_value: {self.initial_value}",
            f"  - final_value: {self.final_value}",
            f"  - final_delta: {self.final_delta}",
            f"  - monotonic_increasing: {self.monotonic_increasing}",
            f"  - monotonic_decreasing: {self.monotonic_decreasing}",
        ]
        return "\n".join(lines)


def _compute_monotonicity(values: List[float]) -> tuple[bool, bool]:
    """
    Determine whether a sequence is monotonic increasing or decreasing (non-strict).
    """
    if len(values) < 2:
        return True, True

    inc = all(values[i] <= values[i + 1] for i in range(len(values) - 1))
    dec = all(values[i] >= values[i + 1] for i in range(len(values) - 1))
    return inc, dec


def analyze_trace(trace: List[EvolutionStep], target: float) -> StabilityReport:
    """
    Analyze an evolution trace and compute stability properties.

    Args:
        trace: List of EvolutionStep objects in chronological order.
        target: Scalar target value for convergence evaluation.

    Returns:
        StabilityReport with convergence and monotonicity information.
    """
    if not trace:
        # No steps executed; treat as a degenerate process.
        # We still respect the domain and convergence definition.
        dummy_state = QuantumState(ABSOLUTE_LIMITS.clamp_value(target))
        converged = dummy_state.is_converged_to(target)
        return StabilityReport(
            converged=converged,
            steps=0,
            initial_value=dummy_state.value,
            final_value=dummy_state.value,
            final_delta=0.0,
            monotonic_increasing=True,
            monotonic_decreasing=True,
        )

    initial_value = trace[0].prev_state.value
    final_value = trace[-1].next_state.value
    final_delta = final_value - initial_value

    values = [step.prev_state.value for step in trace] + [final_value]
    monotonic_increasing, monotonic_decreasing = _compute_monotonicity(values)

    final_state = trace[-1].next_state
    converged = final_state.is_converged_to(target)

    return StabilityReport(
        converged=converged,
        steps=len(trace),
        initial_value=initial_value,
        final_value=final_value,
        final_delta=final_delta,
        monotonic_increasing=monotonic_increasing,
        monotonic_decreasing=monotonic_decreasing,
    )


def analyze_direct(
    initial: QuantumState,
    final: QuantumState,
    steps: int,
    target: float,
) -> StabilityReport:
    """
    Analyze stability when you only have initial/final states and step count.

    Args:
        initial: Initial QuantumState.
        final: Final QuantumState.
        steps: Number of steps taken.
        target: Scalar target value.

    Returns:
        StabilityReport with basic convergence information.
    """
    ABSOLUTE_LIMITS.validate_iteration_count(steps)

    initial_value = initial.value
    final_value = final.value
    final_delta = final_value - initial_value

    converged = final.is_converged_to(target)

    # Without a full trace, we cannot guarantee monotonicity;
    # we mark both as False to avoid over-claiming.
    return StabilityReport(
        converged=converged,
        steps=steps,
        initial_value=initial_value,
        final_value=final_value,
        final_delta=final_delta,
        monotonic_increasing=False,
        monotonic_decreasing=False,
    )

