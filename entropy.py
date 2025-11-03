from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Iterable, List, Sequence, Tuple, Dict
from collections import Counter
import math, lzma, json

def shannon_entropy(symbols: Iterable[int], base: float = 2.0) -> float:
    c = Counter(symbols); n = sum(c.values())
    if n == 0: return 0.0
    return -sum((k/n)*math.log(k/n, base) for k in c.values())

def ledger_entropy_shannon(lifted: Sequence[Tuple[int,int]]) -> float:
    ds = [(d & 0xFF) for (_,d) in lifted]
    return shannon_entropy(ds, base=2.0)

# Query model
@dataclass(frozen=True)
class Query:
    name: str
    func: Callable[[Sequence[Dict[str,Any]]], Any]

@dataclass
class QuerySet:
    queries: List[Query]

    def answers(self, deltas: Sequence[Dict[str,Any]]) -> Dict[str,Any]:
        return {q.name: q.func(deltas) for q in self.queries}

def _compressed_size(obj: Any) -> int:
    blob = json.dumps(obj, sort_keys=True).encode()
    return len(lzma.compress(blob, preset=3))

def ledger_entropy_mdl(deltas: List[Dict[str,Any]], Q: QuerySet) -> Tuple[int, List[int]]:
    """Return (compressed bytes of minimal subset, chosen indices).
    Greedy coverage: choose deltas that change some query answer until all answers match full history.
    """
    target = Q.answers(deltas)
    chosen: List[int] = []
    have: List[Dict[str,Any]] = []
    last = {}
    while last != target:
        best = None
        best_gain = -1
        for i, d in enumerate(deltas):
            if i in chosen: continue
            trial = have + [d]
            if Q.answers(trial) == last:  # no change
                continue
            gain = 1  # unit gain heuristic
            if gain > best_gain:
                best_gain = gain; best = i
        if best is None:
            # queries do not depend on deltas (degenerate): encode empty
            break
        chosen.append(best)
        have.append(deltas[best])
        last = Q.answers(have)
    size = _compressed_size(have)
    return size, chosen
