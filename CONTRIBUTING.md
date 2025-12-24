# Contributing to qsol-invariants

Thank you for your interest in contributing to the QSOL Invariant Evolution Core.
This repository defines the canonical invariant contract for all QSol.llc systems.
Because this module serves as a public standard, contributions must maintain
mathematical clarity, determinism, and alignment with the Absolute Limits Contract.

## ✦ Contribution Guidelines

### 1. Preserve the Invariants
All contributions must respect the following non‑negotiable rules:

- State values must remain within `[0, 1]`
- Convergence is defined strictly as `Δ = 0`
- Evolution steps must remain PHI‑bounded
- No hidden state or side effects
- Deterministic, reproducible behavior only

### 2. Keep the Core Minimal
This repository is intentionally small and stable.  
New features should only be added if they strengthen:

- clarity  
- determinism  
- auditability  
- mathematical rigor  

### 3. Code Style
- Use clear, explicit Python  
- Avoid unnecessary abstraction  
- Prefer readability over cleverness  
- Document invariants where relevant  

### 4. Submitting Changes
1. Fork the repository  
2. Create a feature branch  
3. Ensure tests (if present) pass  
4. Submit a pull request with a clear explanation  

### 5. Discussion
If you want to propose a conceptual change to the invariants or evolution rules,
open an issue first so it can be discussed before implementation.

## ✦ License

By contributing, you agree that your contributions will be licensed under the
Apache License 2.0, consistent with the rest of the project.
