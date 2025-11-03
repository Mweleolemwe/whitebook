from onu_ledger import ledger_entropy_shannon, ledger_entropy_mdl, Query, QuerySet

def test_entropy_estimators():
    lifted = [(10, 0), (15, 1), (9, 2), (8, 0), (7, 1)]
    H = ledger_entropy_shannon(lifted)
    assert H >= 0.0
    deltas = [{"d": d} for (_,d) in lifted]
    Q = QuerySet([
        Query("count", lambda D: len(D)),
        Query("nonzero", lambda D: sum(1 for x in D if x["d"]!=0)),
    ])
    size, idx = ledger_entropy_mdl(deltas, Q)
    assert size >= 0 and isinstance(idx, list)
