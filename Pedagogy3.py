\documentclass{article}
\usepackage{amsmath, amssymb, amsthm}

\newtheorem{theorem}{Theorem}

\begin{document}

\section*{Exposé: Ledger Regularity and the True Accounting of Energy in Navier–Stokes Theory}

\begin{theorem}[Ledgered Local Energy Identity---Leray–Hopf class]
Let $v$ be any Leray–Hopf weak solution to the incompressible Navier–Stokes equations with pressure $p$ on a smooth domain. Then there exists a nonnegative Radon measure $\mu$ (``ledger'' or ``defect'' measure) such that, as measures, the following identity holds:
\[
\partial_t \Big(\frac{1}{2}|v|^2\Big)
+ \nabla\cdot\Big[\Big(\frac{1}{2}|v|^2 + p\Big)v\Big]
= \nu \Delta\Big(\frac{1}{2}|v|^2\Big) - \nu|\nabla v|^2 - \mu .
\tag{1}
\]
The measure $\mu$ rigorously accounts for any local ``energy deficit'' or ``invisible dissipation'' that arises in weak solutions, ensuring a precise energy balance. For smooth solutions, $\mu \equiv 0$.
\end{theorem}

\end{document}
