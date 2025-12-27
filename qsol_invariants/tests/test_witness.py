from qsol_invariants.zk.witness import session_to_witness
from qsol_invariants.session import Session
from qsol_invariants.quantum_state import QuantumState


def test_session_to_witness_basic():
    s0 = QuantumState([0.1, 0.2])
    s1 = QuantumState([0.3, 0.4])
    session = Session(
        session_id="abc",
        states=[s0, s1],
        parameters={"phi": 0.5},
    )

    w = session_to_witness(session)

    assert w.session_id == "abc"
    assert w.states == [s0, s1]
    assert w.parameters == {"phi": 0.5}
