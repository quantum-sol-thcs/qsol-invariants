from qsol_invariants import SimulationSession


def increment(x):
    return x + 0.05


def test_session_run():
    session = SimulationSession(
        initial_value=0.0,
        target=0.2,
        transform=increment,
    )
    session.run()

    assert session.completed
    assert session.stability is not None
    assert session.stability.steps > 0
    assert session.final_state().value <= 1.0


def test_session_report():
    session = SimulationSession(
        initial_value=0.0,
        target=0.0,
        transform=lambda x: x,
    )
    session.run()
    report = session.report()
    assert "QSOL Simulation Session:" in report

