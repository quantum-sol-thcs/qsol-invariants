"""
quantum_state.py

QSOL QuantumState container.

A normalized, PHI‑bounded, invariant‑enforcing scalar state used by all QSOL
evolution operators. This class guarantees:

- value is always clamped to [0, 1]
- all deltas are validated against AbsoluteLimits
- state transitions are deterministic and side‑effect free
"""

from __future__ import annotations

from dataclasses import dataclass, field
from .absolute_limits import ABSOLUTE_LIMITS


@dataclass
class QuantumState:
    """
    A scalar state constrained by the QSOL Absolute Limits Contract.

    The state is always kept within [0, 1] and all transitions must obey the
    PHI‑bounded max_step_delta constraint.
    """

    value: float = field(default=0.0)

    def __post_init__(self) -> None:
        # Clamp initial value to the allowed domain.
        self.value = ABSOLUTE_LIMITS.clamp_value(self.value)

    def apply_delta(self, delta: float) -> "QuantumState":
        """
        Apply a PHI‑bounded delta to the state and return a NEW QuantumState.

        This method:
        - validates |delta| <= max_step_delta
        - applies the delta
        - clamps the result to [0, 1]
        - returns a new QuantumState (no mutation)
        """
        ABSOLUTE_LIMITS.validate_step_delta(delta)

        new_value = self.value + delta
        new_value = ABSOLUTE_LIMITS.clamp_value(new_value)

        return QuantumState(new_value)

    def distance_to(self, target: float) -> float:
        """
        Compute the signed distance to a target scalar.
        """
        return target - self.value

    def is_converged_to(self, target: float) -> bool:
        """
        Check whether the state has converged to the target under the invariant
        convergence rule (delta == 0).
        """
        delta = self.distance_to(target)
        return ABSOLUTE_LIMITS.is_converged(delta)

    def copy(self) -> "QuantumState":
        """
        Return a shallow copy of the state.
        """
        return QuantumState(self.value)

    def __repr__(self) -> str:
        return f"QuantumState(value={self.value:.6f})"

