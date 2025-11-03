from onu_ledger import encode_lossless, decode_lossless, LedgerStore, LedgerRecord, sha256, merkle_root
import os, json, time

def test_roundtrip_and_merkle():
    raw = os.urandom(97)
    enc, lifted = encode_lossless(raw)
    dec = decode_lossless(enc)
    assert dec[:len(raw)] == raw

    from onu_ledger import ledger
    store = LedgerStore()
    rec = LedgerRecord(
        op_id="codec:v1", kind="reversible",
        inputs_digest=sha256(raw),
        outputs_digest=sha256(enc),
        delta_signature=sha256(b"x"),
        gauge={"type": "integer-lifting"},
        energy_delta=0.0, metadata={"ts": time.time()},
    )
    idx = store.append(rec)
    root = store.commit_root()
    proof = store.proof_of_inclusion(idx)
    assert proof["root"] == root
