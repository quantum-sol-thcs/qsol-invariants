"""
absolute_limits.py

QSOL Absolute Limits Contract.

Defines the global, non-negotiable boundaries for all QSOL state evolution:
- Value domain: [0.0, 1.0]
- Deterministic convergence rule: delta == 0.0
- Global iteration ceiling
- PHI-bounded transform requirement (max per-step change)

This module is intentionally minimal and stable. It contains no
implementation-specific logic beyond the invariant contract itself.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AbsoluteLimits:
    """
    AbsoluteLimits defines the canonical invariant contract for all QSOL systems.

    All evolution, state transitions, and transforms must obey these constraints.
    This class is immutable and should be treated as a shared reference, not
    mutated or subclassed.
    """

    # Closed interval for all scalar state values.
    min_value: float = 0.0
    max_value: float = 1.0

    # Convergence is defined strictly as delta == 0.0.
    convergence_delta: float = 0.0

    # Hard ceiling on iteration count for any evolution process.
    max_iterations: int = 10_000

    # PHI-bounded transform requirement: maximum allowed absolute change per step.
    # This does not prescribe a specific transform, only its allowed magnitude.
    max_step_delta: float = 0.1

    def clamp_value(self, value: float) -> float:
        """
        Clamp a scalar to the allowed [min_value, max_value] domain.

        This is the only permitted way to repair an out-of-range value.
        """
        if value < self.min_value:
            return self.min_value
        if value > self.max_value:
            return self.max_value
        return value

    def is_within_domain(self, value: float) -> bool:
        """
        Check whether a scalar is within the allowed [min_value, max_value] domain.
        """
        return self.min_value <= value <= self.max_value

    def is_converged(self, delta: float) -> bool:
        """
        Check whether a given delta satisfies the convergence rule.

        By contract, convergence is defined as delta == convergence_delta.
        """
        return delta == self.convergence_delta

    def validate_step_delta(self, delta: float) -> None:
        """
        Enforce the PHI-bounded requirement on per-step change.

        Raises:
            ValueError if |delta| exceeds max_step_delta.
        """
        if abs(delta) > self.max_step_delta:
            raise ValueError(
                f"Step delta {delta} exceeds max_step_delta {self.max_step_delta} "
                "in AbsoluteLimits."
            )

    def validate_iteration_count(self, iterations: int) -> None:
        """
        Enforce the global iteration ceiling.

        Raises:
            ValueError if iterations exceed max_iterations.
        """
        if iterations > self.max_iterations:
            raise ValueError(
                f"Iteration count {iterations} exceeds max_iterations "
                f"{self.max_iterations} in AbsoluteLimits."
            )

    def describe(self) -> str:
        """
        Return a human-readable description of the current invariant contract.
        """
        return (
            "QSOL Absolute Limits Contract:\n"
            f"  - domain: [{self.min_value}, {self.max_value}]\n"
            f"  - convergence_delta: {self.convergence_delta}\n"
            f"  - max_iterations: {self.max_iterations}\n"
            f"  - max_step_delta (PHI-bound): {self.max_step_delta}"
        )


# Canonical, shared instance used by all QSOL components.
ABS
