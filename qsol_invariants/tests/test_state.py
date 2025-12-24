from qsol_invariants import QuantumState, ABSOLUTE_LIMITS


def test_initial_clamping():
    s = QuantumState(2.0)
    assert s.value == 1.0

    s = QuantumState(-5.0)
    assert s.value == 0.0


def test_apply_delta():
    s = QuantumState(0.5)
    s2 = s.apply_delta(0.1)
    assert s2.value == 0.6

    # PHI-bound violation
    try:
        s.apply_delta(1.0)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_convergence_check():
    s = QuantumState(0.5)
    assert not s.is_converged_to(0.7)

    # Converged means delta == 0
    s2 = QuantumState(0.5)
    assert s2.is_converged_to(0.5)

