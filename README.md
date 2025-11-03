# onu_ledger

Partition-first, non-erasure ledger toolkit (Lumina/Onu).

**What you get**
- Reversible integer-lifting codec for byte streams (perfect round‑trip).
- Multiplicative partition maps for floats (`u -> (y=u/v, g=ln v)`).
- Append-only ledger store with Merkle roots + inclusion proofs.
- PROV JSON‑LD export for standards-friendly provenance.
- **Ledger Entropy**: query-conditioned information metric (Shannon over deltas, MDL via LZMA).
- CLI: compute/commit Merkle root, export proofs, print Ledger Entropy.

```
pip install .
onu-ledger demo
```

**Ledger Entropy (formal)**
Let `D = (δ_1,...,δ_n)` be typed deltas and `Q` a finite query family.  
The *query-conditioned ledger entropy* is
\[
  \mathcal{H}_Q(D) := \min_{S\subseteq D}\ \{\mathrm{MDL}(S): \forall q\in Q,\ q(S)=q(D)\}
\]
i.e., the minimum description length of any subset of deltas that suffices to answer all queries as if the full history were present. In practice we approximate with greedy coverage and LZMA-compressed size.

