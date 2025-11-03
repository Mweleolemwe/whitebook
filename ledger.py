from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import hashlib, json, time

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def digest_obj(obj: Any) -> str:
    return sha256(json.dumps(obj, sort_keys=True, default=str).encode())

def merkle_root(hashes: List[str]) -> str:
    if not hashes:
        return sha256(b"")
    level = [bytes.fromhex(h) for h in hashes]
    while len(level) > 1:
        nxt = []
        for i in range(0, len(level), 2):
            a = level[i]
            b = level[i+1] if i+1 < len(level) else a
            nxt.append(hashlib.sha256(a + b).digest())
        level = nxt
    return level[0].hex()

@dataclass
class LedgerRecord:
    op_id: str
    kind: str
    inputs_digest: str
    outputs_digest: str
    delta_signature: str
    gauge: Dict[str, Any]
    energy_delta: float = 0.0
    metadata: Dict[str, Any] = None

class LedgerStore:
    def __init__(self) -> None:
        self._records: List[LedgerRecord] = []
        self._roots: List[str] = []

    def append(self, rec: LedgerRecord) -> int:
        self._records.append(rec)
        return len(self._records) - 1

    def commit_root(self) -> str:
        root = merkle_root([digest_obj(asdict(r)) for r in self._records])
        self._roots.append(root)
        return root

    def proof_of_inclusion(self, index: int) -> Dict[str, Any]:
        assert self._roots, "no committed root"
        return {"index": index, "root": self._roots[-1], "record": asdict(self._records[index])}

    def export_json(self) -> Dict[str, Any]:
        return {
            "records": [asdict(r) for r in self._records],
            "roots": self._roots,
        }
