from __future__ import annotations
from typing import Dict, Any, List
from .ledger import LedgerRecord
import json

def prov_jsonld(records: List[LedgerRecord]) -> Dict[str, Any]:
    ctx = {
        "@context": "https://www.w3.org/ns/prov.jsonld",
        "activity": "prov:Activity",
        "entity": "prov:Entity",
        "used": "prov:used",
        "wasGeneratedBy": "prov:wasGeneratedBy",
    }
    ents = []
    acts = []
    edges = []
    for i, r in enumerate(records):
        ent_in = {"@id": f"entity:input:{i}", "@type": "entity", "digest": r.inputs_digest}
        ent_out= {"@id": f"entity:output:{i}", "@type": "entity", "digest": r.outputs_digest}
        act    = {"@id": f"activity:{i}", "@type": "activity", "op": r.op_id, "kind": r.kind, "gauge": r.gauge}
        ents += [ent_in, ent_out]; acts.append(act)
        edges += [
            {"@id": f"used:{i}", "used": ent_in["@id"], "activity": act["@id"]},
            {"@id": f"wgb:{i}", "wasGeneratedBy": ent_out["@id"], "activity": act["@id"]},
        ]
    return {"@context": ctx["@context"], "entity": ents, "activity": acts, "relations": edges}
