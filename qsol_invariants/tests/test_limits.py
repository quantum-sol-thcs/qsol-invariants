from qsol_invariants import ABSOLUTE_LIMITS


def test_clamp_value():
    assert ABSOLUTE_LIMITS.clamp_value(-1.0) == 0.0
    assert ABSOLUTE_LIMITS.clamp_value(2.0) == 1.0
    assert ABSOLUTE_LIMITS.clamp_value(0.5) == 0.5


def test_domain_check():
    assert ABSOLUTE_LIMITS.is_within_domain(0.0)
    assert ABSOLUTE_LIMITS.is_within_domain(1.0)
    assert not ABSOLUTE_LIMITS.is_within_domain(-0.1)
    assert not ABSOLUTE_LIMITS.is_within_domain(1.1)


def test_step_delta_validation():
    ABSOLUTE_LIMITS.validate_step_delta(0.05)
    ABSOLUTE_LIMITS.validate_step_delta(-0.05)

    try:
        ABSOLUTE_LIMITS.validate_step_delta(1.0)
        assert False, "Expected ValueError"
    except ValueError:
        pass

