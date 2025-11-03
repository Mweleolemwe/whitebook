from __future__ import annotations
from typing import Iterable, Tuple, List
import math

# ---- Integer-lifting (Haar), bijective on bytes ----
def lift_fwd_int(a: int, b: int) -> Tuple[int, int]:
    s = a + b
    d = a - (s // 2)
    return s & 0xFF, d & 0xFF

def lift_inv_int(s: int, d: int) -> Tuple[int, int]:
    s &= 0xFF; d &= 0xFF
    a = (d + (s // 2)) & 0xFF
    b = (s - a) & 0xFF
    return a, b

def bytes_to_pairs(data: bytes) -> List[Tuple[int,int]]:
    if len(data) % 2 == 1:
        data += b"\x00"
    it = iter(data)
    return [(next(it), next(it)) for _ in range(len(data)//2)]

def pairs_to_bytes(pairs: Iterable[Tuple[int,int]]) -> bytes:
    out = bytearray()
    for a,b in pairs:
        out.append(a & 0xFF); out.append(b & 0xFF)
    return bytes(out)

def encode_lossless(data: bytes) -> Tuple[bytes, List[Tuple[int,int]]]:
    pairs = bytes_to_pairs(data)
    lifted = [lift_fwd_int(a,b) for a,b in pairs]
    enc = pairs_to_bytes(lifted)
    return enc, lifted

def decode_lossless(encoded: bytes) -> bytes:
    pairs = bytes_to_pairs(encoded)
    inv = [lift_inv_int(s,d) for s,d in pairs]
    return pairs_to_bytes(inv)

# ---- Multiplicative partition (float path) ----
def partition_multiplicative(u: Iterable[float], v: Iterable[float]):
    y, g = [], []
    for ui, vi in zip(u, v):
        if vi <= 0:
            raise ValueError("v must be > 0")
        y.append(ui/vi); g.append(math.log(vi))
    return y, g

def partition_inverse(y: Iterable[float], g: Iterable[float]):
    import math
    return [yi*math.exp(gi) for yi,gi in zip(y,g)]
