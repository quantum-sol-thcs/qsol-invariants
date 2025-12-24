"""
evolution.py

QSOL PHI-bounded evolution operators.

Defines the canonical state evolution primitives:

- evolve       : single PHI-bounded step
- evolve_until : deterministic fixed-point evolution toward a target
- evolve_trace : evolution with full audit-ready trace

All evolution is:
- deterministic
- PHI-bounded per step
- constrained by AbsoluteLimits.max_iterations
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Tuple

from .absolute_limits import ABSOLUTE_LIMITS
from .quantum_state import QuantumState


TransformFn = Callable[[float], float]


@dataclass(frozen=True)
class EvolutionStep:
    """
    A single evolution step, capturing the transition for auditability.
    """

    index: int
    prev_state: QuantumState
    next_state: QuantumState
    delta: float


def evolve(state: QuantumState, fn: TransformFn) -> Tuple[QuantumState, float]:
    """
    Perform a single PHI-bounded evolution step.

    Args:
        state: Current QuantumState.
        fn: A deterministic transform function f(x) -> x', before clamping.

    Returns:
        (next_state, delta) where:
            next_state: new QuantumState after applying fn and invariant checks.
            delta:      signed change in value (next - prev).

    Raises:
        ValueError: if the implied delta violates PHI bounds.
    """
    raw_next = fn(state.value)
    delta = raw_next - state.value

    # Validate delta against PHI-bound requirement.
    ABSOLUTE_LIMITS.validate_step_delta(delta)

    # Clamp the resulting value to the allowed domain.
    clamped_next = ABSOLUTE_LIMITS.clamp_value(raw_next)
    next_state = QuantumState(clamped_next)

    return next_state, delta


def evolve_until(
    initial: QuantumState,
    target: float,
    fn: TransformFn,
) -> Tuple[QuantumState, int]:
    """
    Evolve deterministically until convergence to a target under the invariant rule.

    Convergence is defined by the AbsoluteLimits convergence_delta (delta == 0.0).

    Args:
        initial: Starting QuantumState.
        target: Target scalar value.
        fn: Deterministic transform function f(x) -> x', before clamping.

    Returns:
        (final_state, steps) where:
            final_state: converged QuantumState (or last valid state if ceiling hit).
            steps:       number of evolution steps executed.

    Raises:
        ValueError: if iteration count would exceed AbsoluteLimits.max_iterations.
    """
    state = initial.copy()
    steps = 0

    while True:
        # Enforce iteration ceiling before performing the next step.
        ABSOLUTE_LIMITS.validate_iteration_count(steps)

        # If already converged, stop.
        if state.is_converged_to(target):
            return state, steps

        next_state, delta = evolve(state, fn)

        state = next_state
        steps += 1

        # Check convergence relative to target after the step.
        if state.is_converged_to(target):
            return state, steps

        # Optional: short-circuit if the transform no longer moves toward the target.
        # This keeps deterministic behavior while avoiding infinite loops on bad fn.
        if delta == 0.0 and not state.is_converged_to(target):
            return state, steps


def evolve_trace(
    initial: QuantumState,
    target: float,
    fn: TransformFn,
) -> List[EvolutionStep]:
    """
    Evolve with a full audit-ready trace of all intermediate states.

    Args:
        initial: Starting QuantumState.
        target: Target scalar value.
        fn: Deterministic transform function f(x) -> x', before clamping.

    Returns:
        List of EvolutionStep objects, in chronological order.
    """
    trace: List[EvolutionStep] = []
    state = initial.copy()
    index = 0

    while True:
        ABSOLUTE_LIMITS.validate_iteration_count(index)

        if state.is_converged_to(target):
            break

        next_state, delta = evolve(state, fn)

        step = EvolutionStep(
            index=index,
            prev_state=state,
            next_state=next_state,
            delta=delta,
        )
        trace.append(step)

        state = next_state
        index += 1

        if state.is_converged_to(target):
            break

        if delta == 0.0 and not state.is_converged_to(target):
            break

    return trace

