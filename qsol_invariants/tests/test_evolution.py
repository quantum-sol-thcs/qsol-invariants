from qsol_invariants import (
    QuantumState,
    evolve,
    evolve_until,
    evolve_trace,
)


def identity(x):
    return x


def increment(x):
    return x + 0.05


def test_single_evolve():
    s = QuantumState(0.5)
    next_state, delta = evolve(s, increment)
    assert next_state.value == 0.55
    assert delta == 0.05


def test_evolve_until_converges():
    s = QuantumState(0.5)
    final, steps = evolve_until(s, target=0.5, fn=identity)
    assert final.value == 0.5
    assert steps == 0


def test_evolve_trace():
    s = QuantumState(0.0)
    trace = evolve_trace(s, target=0.2, fn=increment)
    assert len(trace) > 0
    assert trace[-1].next_state.value <= 1.0

