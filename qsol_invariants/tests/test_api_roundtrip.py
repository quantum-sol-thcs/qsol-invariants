from qsol_invariants.zk import prove_session, verify_session_proof
from qsol_invariants.session import Session
from qsol_invariants.quantum_state import QuantumState


def test_prove_and_verify_roundtrip():
    s0 = QuantumState([0.1, 0.2])
    s1 = QuantumState([0.3, 0.4])

    session = Session(
        session_id="roundtrip",
        states=[s0, s1],
        parameters={"phi": 0.5},
    )

    proof = prove_session(session)

    assert proof.session_id == "roundtrip"
    assert proof.summary.step_count == 1
    assert proof.spec_id == "SESSION_VALIDITY_V1"
    assert proof.backend_id == "FAKE_BACKEND_V1"

    assert verify_session_proof(proof)
