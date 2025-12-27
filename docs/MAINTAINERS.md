✦ QSOL MAINTAINERS GUIDE ✦
Roles, Responsibilities, and Canonical Workflow for Stewarding the Invariant Core
Version: 1.0
Status: Canonical
Governs: qsol‑invariants and all dependent QSOL standards

1. Purpose
Maintainers of the QSOL Invariant Evolution Core are responsible for preserving the mathematical, architectural, and philosophical integrity of the QSOL canon.
This guide defines the responsibilities, expectations, and workflows required to ensure:

deterministic behavior

invariant preservation

PHI‑bounded evolution

audit‑grade reproducibility

long‑term stability

alignment with the QSOL Engineering Doctrine

Maintainers are stewards of the canon, not owners of the code.

2. Maintainer Responsibilities
2.1 Uphold the Canon
Maintainers must ensure that all contributions preserve:

the Absolute Limits Contract

the PHI‑bounded Evolution Law

deterministic convergence (Δ = 0)

invariant‑preserving state transitions

the canonical projection Π for public views

the SESSION_VALIDITY specification (for ZK components)

Any change that weakens or bypasses these rules must be rejected.

2.2 Protect the Doctrine
All decisions must align with the QSOL Engineering Doctrine, including:

replaceability over permanence

explicit versioning

minimal public surface

privacy by default

tests as contract

audit‑grade artifacts

deterministic, side‑effect‑free behavior

The doctrine is the highest authority in the repository.

2.3 Maintain Repository Stability
Maintainers must:

keep the core minimal

avoid unnecessary abstraction

enforce explicit, readable, deterministic code

maintain consistent naming and structure

ensure all public APIs remain stable and predictable

Stability is a primary responsibility.

2.4 Steward the Community
Maintainers must:

respond to issues professionally

guide contributors toward canonical solutions

provide clear, constructive feedback

enforce the Code of Conduct

ensure discussions remain technical and respectful

Community stewardship is part of canonical stewardship.

3. Canonical Workflow for Changes
3.1 Issue Discussion
Before approving any conceptual change to:

invariants

evolution rules

PHI‑boundedness

convergence semantics

SESSION_VALIDITY

public API

canonical metadata

the change must be discussed in an issue.

Conceptual changes require consensus and doctrinal justification.

3.2 Pull Request Requirements
A PR must:

reference the relevant issue

include tests for all new behavior

maintain ≥ 90% coverage

preserve determinism

avoid hidden state or side effects

include clear reasoning grounded in the Doctrine

update documentation where appropriate

PRs that modify invariants must also update:

spec_id

relevant specs

relevant tests

3.3 Review Process
Maintainers must verify:

deterministic behavior

invariant preservation

PHI‑bounded transitions

no randomness or nondeterminism

no leakage of internal state

alignment with the Doctrine and specs

clarity and readability of code

completeness of tests

If any canonical requirement is violated, the PR must be revised or rejected.

3.4 Approval
A PR may be approved only when:

all invariants are preserved

the change strengthens clarity or rigor

tests pass and coverage is maintained

documentation is updated

the change is fully aligned with the Doctrine

Approval is a canonical act, not a convenience.

4. Versioning and Releases
4.1 Semantic Versioning (Stability‑First)
PATCH — internal fixes, no API changes

MINOR — new deterministic features, no breaking changes

MAJOR — changes to invariants, evolution rules, or public API

4.2 Spec Versioning
Changes to:

SESSION_VALIDITY

projection Π

invariant definitions

evolution semantics

must increment the spec_id.

4.3 Release Notes
Each release must include:

summary of changes

spec changes (if any)

migration notes

doctrinal rationale

Releases must be auditable and self‑describing.

5. ZK Subsystem Stewardship
Maintainers must ensure:

backend interfaces remain stable

proofs remain self‑describing

metadata (spec_id, backend_id, hash_algorithm) is preserved

transcript commitments remain canonical

privacy‑preserving projection Π is enforced

witness extraction remains deterministic

Any change to the ZK subsystem requires heightened scrutiny.

6. Enforcement
Maintainers may:

request revisions

reject PRs

revert non‑canonical changes

restrict participation for repeated violations

All enforcement decisions must be:

professional

documented

aligned with the Doctrine and Code of Conduct

7. Scope
This guide applies to:

all maintainers

all reviewers

all canonical decision‑making processes

all QSOL invariant‑related repositories

8. License
By serving as a maintainer, you agree that all contributions and decisions fall under the Apache License 2.0, consistent with the rest of the QSOL platform.
