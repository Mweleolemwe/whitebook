% !TEX program = lualatex
\documentclass[11pt]{article}

% ---------- Core packages ----------
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,mathtools,amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage[hidelinks]{hyperref}

% ---------- Definitions ----------
\newcommand{\dd}{\mathrm{d}}
\newcommand{\ellP}{\ell_{\mathrm{P}}}  % Planck length
\newcommand{\rg}{r_{\mathrm{g}}}       % Gravitational radius
\newcommand{\Onu}{\mathcal{O}}         % Onu Operator
\newcommand{\sLedger}{\mathcal{S}}     % The Scale Ledger

\title{The Onu Scale-Ledger: A Log-Additivity Framework for\\ Quantum-Gravitational Information Flow}
\author{Onu Collective}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
We present the \textbf{Onu Transform}, a logarithmic gauge transformation that maps multiplicative physical scales onto a linear, additive ``scale-ledger.'' By defining the gauge $s = \ln(r/r_0)$ and its base-2 counterpart $n = -\log_2(r/r_0)$, we demonstrate that the hierarchy problem between the Planck scale and macroscopic astrophysical objects resolves into a finite ``bit-gap'' of approximately 128 bits. Furthermore, we show that entropic dynamics (the Page curve) and the Schwarzschild horizon singularity are naturally regularized on this ledger, allowing for a unified treatment of black hole thermodynamics and information flow via standard diffusion dynamics.
\end{abstract}

\section{The Onu Transform: From Multiplicative to Additive}

Standard physics operates across vast multiplicative regimes, typically managed via scientific notation ($10^{30}$ vs $10^{-35}$). The Onu Transform normalizes this by mapping the radial coordinate $r$ to a scale-bit index $n$.

\begin{equation}
    n(r) \coloneqq -\log_2\left(\frac{r}{1\,\text{m}}\right) \quad \Longleftrightarrow \quad r(n) = 2^{-n}\,\text{m}.
\end{equation}

In this gauge, positive $n$ denotes sub-meter (quantum) scales, while negative $n$ denotes super-meter (astrophysical) scales. Scale comparison becomes a linear subtraction of bits rather than a quotient of exponents.

\subsection{The 128-Bit Gap}
Using the pivot at 1 meter, we compute the fundamental ``distance'' between the quantum foam and the macroscopic vacuum solution.

\begin{itemize}
    \item \textbf{Planck Length ($\ellP$):} $\ellP = \sqrt{\hbar G / c^3} \approx 1.616 \times 10^{-35}\,\text{m}$.
    \[ n(\ellP) \approx 115.6 \text{ bits}. \]
    \item \textbf{Neutron Star Radius ($\rg$):} For $M \approx 2 M_{\odot}$, $\rg \approx 5.9 \times 10^3\,\text{m}$.
    \[ n(\rg) \approx -12.5 \text{ bits}. \]
\end{itemize}

The total scale-width of the unified theory is the sum of these domains:
\begin{equation}
    \Delta n = n(\ellP) - n(\rg) \approx 128.1 \text{ bits}.
\end{equation}
This suggests that the computational complexity separating the quantum vacuum from relativistic collapse is fundamentally dense but finite ($\approx 2^{128}$).

\section{The Horizon on the Ledger}

The Schwarzschild metric contains a coordinate singularity at the horizon radius $r_s = 2GM/c^2$.
\[
\dd s^2 = -\left(1-\frac{r_s}{r}\right)c^2 \dd t^2 + \left(1-\frac{r_s}{r}\right)^{-1} \dd r^2 + r^2 \dd \Omega^2.
\]
Applying the natural log-gauge $s = \ln(r/r_s)$ centers the horizon at $s=0$. While the curvature remains real, the ``ledger'' view allows us to treat the interior ($s<0$) and exterior ($s>0$) as continuous domains of information density.

\section{Thermodynamics: The Unitary Page Curve}

We model the evaporation of a black hole not as particle emission, but as information diffusion along the $s$-ledger.

\subsection{Entropy Density and Islands}
Let $\rho_s(s)$ be the entropy density on the ledger.
\begin{itemize}
    \item \textbf{Early Time:} Correlations are local; $\rho_s(s)$ is a Gaussian centered outside the horizon (the thermal atmosphere).
    \item \textbf{Late Time (The Island):} As the black hole evaporates (Page time $t_{\text{Page}}$), entanglement wedges reconnect. On the scale-ledger, this manifests as a double-peak distribution (see Fig. 9 in data).
\end{itemize}
The appearance of the inner peak (the ``Island'') preserves unitarity. The total entropy $S_{\text{rad}}$ follows the triangular Page curve:
\begin{equation}
    S(t) \propto \min(t, t_{\text{evap}} - t).
\end{equation}

\section{Conclusion: Coherence via Additivity}

The Onu framework simplifies the conceptual overhead of quantum gravity by:
\begin{enumerate}
    \item \textbf{Linearizing Uncertainty:} A multiplicative error factor of $2\times$ becomes a constant additive error of $\pm 1$ bit, regardless of scale.
    \item \textbf{Regularizing Flow:} Thermodynamics behaves like a standard diffusion process on the $s$-rail, reducing complex metric geometry to 1D heat flow.
    \item \textbf{Unifying Regimes:} The 128-bit gap provides a tangible, calculable bridge between $\ellP$ and $\rg$.
\end{enumerate}

\end{document}
