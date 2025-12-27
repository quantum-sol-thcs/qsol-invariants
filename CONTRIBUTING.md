✦ Contribution Guidelines
Thank you for your interest in contributing to the QSOL Invariant Evolution Core.
This repository defines the canonical invariant contract for all QSol.llc  systems.
Because this module serves as a public standard, contributions must maintain mathematical clarity, determinism, and alignment with the Absolute Limits Contract.

1. Preserve the Invariants
All contributions must respect the following non‑negotiable rules:

State values must remain within [0, 1]

Convergence is defined strictly as Δ = 0

Evolution steps must remain PHI‑bounded

No hidden state or side effects

Deterministic, reproducible behavior only

These constraints form the foundation of the QSOL invariant canon and may not be weakened or bypassed.

2. Keep the Core Minimal
This repository is intentionally small, stable, and canonical.
New features should only be added if they strengthen:

clarity

determinism

auditability

mathematical rigor

If a change introduces complexity without strengthening the canon, it will not be accepted.

3. Code Style
To maintain consistency and auditability:

Use clear, explicit Python

Avoid unnecessary abstraction

Prefer readability over cleverness

Document invariants where relevant

Keep functions deterministic and side‑effect‑free

The goal is boring, predictable, standards‑grade code.

4. Submitting Changes
To contribute:

Fork the repository

Create a feature branch

Ensure all tests pass

Add new tests if your change introduces new behavior

Submit a pull request with a clear explanation of the change

Pull requests that modify invariant logic must reference the QSOL Engineering Doctrine and justify the change in canonical terms.

5. Discussion and Proposals
If you want to propose a conceptual change to:

the invariants

the evolution rules

the Absolute Limits Contract

the PHI‑bounded evolution law

or the SESSION_VALIDITY specification

please open an issue first so it can be discussed before implementation.

Conceptual changes must be evaluated for:

mathematical soundness

determinism

compatibility with existing proofs

long‑term stability

alignment with the doctrine

✦ License
By contributing, you agree that your contributions will be licensed under the Apache License 2.0, consistent with the rest of the project.
