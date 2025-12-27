from qsol_invariants.zk.backend import FakeBackend
from qsol_invariants.zk.summary import PublicSessionSummary
from qsol_invariants.zk.witness import SessionWitness


def test_fake_backend_prove_and_verify():
    backend = FakeBackend()

    witness = SessionWitness(
        session_id="abc",
        states=[],
        parameters={},
    )

    summary = PublicSessionSummary(
        session_id="abc",
        step_count=0,
        public_parameters={},
        final_state_public_view={},
    )

    proof_bytes = backend.prove(witness, summary)
    assert isinstance(proof_bytes, bytes)
    assert len(proof_bytes) == 32  # SHA-256 digest

    class Proof:
        proof_bytes = proof_bytes

    assert backend.verify(Proof())
