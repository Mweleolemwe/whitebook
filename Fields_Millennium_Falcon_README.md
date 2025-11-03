# Fields’ Millennium Falcon — Ledgered Navier–Stokes Program

**Mission:** strengthen localized energy analysis for 3D NSE with a nonnegative **ledger/defect** measure \(\mu\), prove an **ε-regularity** criterion under ledger saturation, and ship a **conservative diagnostic** that prints the energy ledger to truncation order.

---

## Core Identity (Leray–Hopf)
\[
\partial_t\Big(\tfrac12|v|^2\Big)+\nabla\!\cdot\!\Big[(\tfrac12|v|^2+p)v\Big]
=\nu\,\Delta\Big(\tfrac12|v|^2\Big)-\nu\|\nabla v\|^2-\mu,\quad \mu\ge 0.
\]

**Weak form:** for \(\phi\ge0\), the term \(\int\phi\,d\mu\) sits on the **left** (nonnegative), tightening Caccioppoli.

## ε-Regularity (ledger saturation)
Let \(\mathcal E(r)\) be the scaled CKNS energy and \(\Lambda(r)=r^{-1}\mu(Q_r)\) the scaled ledger mass.
Smallness of \(\mathcal E(r_0)+\Lambda(r_0)\) implies Hölder regularity on \(Q_{\delta r_0}\).

## Evidence Engine (Conservative Diagnostic)
2D periodic vorticity–streamfunction NSE (Arakawa Jacobian + FFT Poisson):
\[
E(t)+\int_0^t \nu\|\omega\|_2^2 \,ds = E(0) + \mathcal O(\Delta t^2).
\]
- **Artifacts (permanent DOI):** https://doi.org/10.6084/m9.figshare.30520784  
  Files: `nse_ledger_scheme.py`, `ledger_timeseries.csv`, `ledger_timeseries.png`

---

## 72-Hour Sprint
- **Preprint v1 (arXiv):** abstract, identity, ε-regularity statement, reproducibility section (DOI).
- **Figures:** budget + residual and residual-vs-Δt (slope ≈ 2).
- **Comms:** seminar email, homepage one-liner, poster.

## 30/90-Day Flight Plan
- **P1:** Ledgered Local Energy (full Leray–Hopf proof; DR consistency).
- **P2:** ε-regularity with ledger; CKNS-scale criterion.
- **Adoption:** repo, CI, reproducible examples; external users regenerate plots.

## Crosswalk (Lumina ↔ PDE)
- **Partition** ↔ localized balance with transported cutoffs  
- **Ledger** ↔ nonnegative defect measure **μ**  
- **Ledger mass** **Λ(r)** ↔ **r⁻¹ μ(Q_r)**  
- **Evidence engine** ↔ conservative budget (O(Δt²) closure)

---

## Cite the replication
Conservative ledger diagnostic for periodic 2D NSE: code and artifacts (figshare, 2025).  
**DOI:** 10.6084/m9.figshare.30520784
