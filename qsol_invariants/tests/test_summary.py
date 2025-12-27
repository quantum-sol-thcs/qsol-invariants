from qsol_invariants.zk.summary import PublicSessionSummary
from qsol_invariants.quantum_state import QuantumState
from qsol_invariants.session import Session


def test_public_summary_defaults():
    s0 = QuantumState([0.1, 0.2])
    s1 = QuantumState([0.3, 0.4])
    session = Session(
        session_id="xyz",
        states=[s0, s1],
        parameters={"phi": 0.5},
    )

    summary = PublicSessionSummary.from_session(
        session,
        public_parameters=None,
        final_state_public_view=None,
    )

    assert summary.session_id == "xyz"
    assert summary.step_count == 1
    assert summary.public_parameters == {}
    assert "norm" in summary.final_state_public_view
    assert summary.spec_id == "SESSION_VALIDITY_V1"
