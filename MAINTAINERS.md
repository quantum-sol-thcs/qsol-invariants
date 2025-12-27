QSOL Maintainers Guide
Roles, Responsibilities, and Canonical Workflow for Stewarding the Invariant Core
Version: 1.0
Status: Canonical

1. Purpose
Maintainers of the QSOL Invariant Evolution Core are responsible for preserving:

the Absolute Limits Contract

the PHI‑bounded Evolution Law

the deterministic evolution semantics

the canonical structure of the repository

the integrity of the QSOL Engineering Doctrine

This guide defines the responsibilities, expectations, and workflows required to maintain the invariant canon without drift.

2. Maintainer Responsibilities
Maintainers must:

2.1 Uphold the Canon
Enforce the Absolute Limits Contract

Ensure all evolution operators remain deterministic

Reject any change that introduces randomness or hidden state

Preserve PHI‑boundedness in all transforms

Maintain strict adherence to the SESSION_VALIDITY specification

2.2 Protect the Doctrine
All decisions must align with the QSOL Engineering Doctrine, including:

replaceability over permanence

explicit versioning

minimal public surface

privacy by default

tests as contract

audit‑grade artifacts

2.3 Maintain Repository Stability
Keep the core minimal

Avoid unnecessary abstraction

Ensure all code is explicit, readable, and deterministic

Maintain consistent naming and structure

2.4 Steward the Community
Respond to issues professionally

Guide contributors toward canonical solutions

Provide clear, constructive feedback

Enforce the Code of Conduct

3. Canonical Workflow for Changes
3.1 Issue Discussion
Before approving any conceptual change to:

invariants

evolution rules

PHI‑boundedness

convergence semantics

SESSION_VALIDITY

public API

the change must be discussed in an issue.

3.2 Pull Request Requirements
A PR must:

reference the relevant issue

include tests for all new behavior

maintain 90%+ coverage

include clear reasoning grounded in the Doctrine

avoid introducing unnecessary complexity

3.3 Review Process
Maintainers must:

verify deterministic behavior

check for invariant violations

ensure no hidden state or side effects

confirm alignment with the spec and doctrine

require revisions when needed

3.4 Approval
A PR may be approved only when:

all invariants are preserved

the change strengthens clarity or rigor

tests pass and coverage is maintained

the change is fully documented

4. Versioning and Releases
4.1 Semantic Versioning
The repository follows a stability‑first variant of semantic versioning:

PATCH — internal fixes, no API changes

MINOR — new deterministic features, no breaking changes

MAJOR — changes to invariants, evolution rules, or public API

4.2 Spec Versioning
Changes to:

SESSION_VALIDITY

projection Π

invariant definitions

must increment the spec_id.

4.3 Release Notes
Each release must include:

summary of changes

spec changes (if any)

migration notes

rationale grounded in the Doctrine

5. ZK Subsystem Stewardship
Maintainers must ensure:

backend interfaces remain stable

proofs remain self‑describing

metadata (spec_id, backend_id, hash_algorithm) is preserved

transcript commitments remain canonical

privacy‑preserving projection Π is enforced

Any change to the ZK subsystem must be reviewed with exceptional care.

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
By serving as a maintainer, you agree that all contributions and decisions fall under the Apache License 2.0, consistent with the rest of the project.
