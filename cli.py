from __future__ import annotations
import argparse, json, time, sys
from .ledger import LedgerStore, LedgerRecord, sha256, digest_obj
from .codec import encode_lossless, decode_lossless
from .entropy import Query, QuerySet, ledger_entropy_shannon, ledger_entropy_mdl

def demo():
    store = LedgerStore()
    raw = b"hello luminous world"
    enc, lifted = encode_lossless(raw)
    # record
    rec = LedgerRecord(
        op_id="codec:v1",
        kind="reversible",
        inputs_digest=sha256(raw),
        outputs_digest=sha256(enc),
        delta_signature=digest_obj({"lifted_len":len(lifted)}),
        gauge={"type": "integer-lifting"},
        energy_delta=0.0,
        metadata={"ts": time.time()},
    )
    store.append(rec)
    root = store.commit_root()
    # Entropy demo
    H = ledger_entropy_shannon(lifted)
    print("Merkle root:", root)
    print("Shannon ledger entropy (deltas, bits):", H)
    # MDL demo with toy queries
    deltas = [{"d": int(d)} for (_,d) in lifted]
    Q = QuerySet([
        Query("num_nonzero_d", lambda D: sum(1 for x in D if x["d"]!=0)),
        Query("parity_sum_d",  lambda D: sum(x["d"] for x in D) % 2),
    ])
    size, idxs = ledger_entropy_mdl(deltas, Q)
    print("MDL(bytes) for answering Q:", size, " chosen indices:", idxs[:8], "...")

def main(argv=None):
    parser = argparse.ArgumentParser(description="onu-ledger CLI")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("demo")
    args = parser.parse_args(argv)
    if args.cmd == "demo":
        demo()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
