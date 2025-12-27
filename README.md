qsol‑invariants
Canonical QSOL invariant contract and evolution core
Deterministic, PHI‑bounded, audit‑ready state evolution for all QSol.llc  systems.

Overview
The QSOL Invariant Evolution Core defines the foundational mathematical rules, state constraints, and deterministic evolution operators used across all QSol.llc  systems. This repository establishes the Absolute Limits Contract and the PHI‑bounded Evolution Engine, ensuring that every QSOL simulation, transform, and state transition obeys the same universal, non‑negotiable invariants.

This module is the canonical reference implementation for invariant‑preserving state evolution across the entire QSOL platform.

✦ Features
AbsoluteLimits Contract
Defines the global, immutable boundaries for all QSOL state evolution:

Value domain: [0, 1]

Deterministic convergence rule: Δ = 0

Global iteration ceiling

PHI‑bounded transform requirement

These constraints ensure mathematical stability, reproducibility, and cross‑module consistency.

QuantumState
A normalized, PHI‑bounded, reversible state container that automatically enforces:

domain constraints

normalization

PHI‑bounded transitions

deterministic evolution semantics

Evolution Operators
evolve — canonical PHI‑bounded evolution step

evolve_until — deterministic fixed‑point convergence

evolve_trace — full audit‑ready evolution history

These operators guarantee deterministic, invariant‑preserving state transitions.

Stability Analysis
Tools for analyzing:

fixed points

monotonicity

convergence

final deltas

These functions provide mathematical insight into system behavior and invariant compliance.

SimulationSession
A unified interface for running complete, reproducible QSOL evolution sessions with:

full reporting

deterministic replay

audit‑ready trace extraction

✦ Zero‑Knowledge Subsystem (ZK)
The repository includes a fully modular, backend‑agnostic ZK subsystem implementing the SESSION_VALIDITY proof standard.

ZK Features
Canonical SESSION_VALIDITY constraint system

Deterministic witness extraction

Privacy‑preserving public projection Π

Pluggable backend interface (ZKBackend)

Self‑describing proofs (spec_id, backend_id, hash_algorithm)

Transcript commitments for archival integrity

Full test suite locking the invariant canon

See:
qsol_invariants/zk/SESSION_VALIDITY_SPEC.md

✦ Purpose
This repository serves as the mathematical and architectural foundation for the QSOL platform. Higher‑level engines, governance modules, research tools, and simulation frameworks depend on these invariants to ensure:

determinism

reproducibility

auditability

mathematical stability

cross‑module consistency

This module is stable, minimal, and intended as a public standard.

It contains:

no proprietary algorithms

no cryptographic secrets

no sensitive QSol.llc  logic

Only the universal rules that all QSOL components must obey.

✦ QSOL Engineering Doctrine
This repository adheres to the QSOL Engineering Doctrine, the governing set of principles that ensures every QSOL subsystem is:

production‑ready

forward‑thinking

deterministic

auditable

privacy‑preserving

versioned

stable across implementations and time

The doctrine establishes the architectural and philosophical rules that all QSOL components must follow, including:

Replaceability over permanence

Explicit versioning (spec_id, backend_id, hash_algorithm)

Minimal public surface

Determinism above all

Privacy by default (projection Π)

Tests as contract

CI mirrors local development

Audit‑grade artifacts

See:
QSOL_ENGINEERING_DOCTRINE.md

✦ Repository Structure

qsol_invariants/
    quantum_state.py
    evolution.py
    stability.py
    session.py
    absolute_limits.py

    zk/
        api.py
        backend.py
        witness.py
        summary.py
        transcript.py
        projection.py
        errors.py
        SESSION_VALIDITY_SPEC.md

tests/
    test_witness.py
    test_summary.py
    test_backend_fake.py
    test_api_roundtrip.py

QSOL_ENGINEERING_DOCTRINE.md
LICENSE
README.md

✦ Status
This module is stable, minimal, and canonical.
It is intended as a public standard for invariant‑preserving state evolution.

✦ License
This project is licensed under the Apache License 2.0.
See the LICENSE file for full details.
