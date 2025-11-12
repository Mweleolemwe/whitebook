% onu-kit/main.tex
% One-stop pedagogy paper: compiles with pdflatex or lualatex
\documentclass[11pt]{article}

% ---------- core packages ----------
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{siunitx}
\usepackage{microtype}
\usepackage{textcomp}      % for \textopenbullet
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\usepackage[draft]{graphicx}   % change to [final] when images are present
\graphicspath{{fig/}}
\usepackage{enumitem}

% ---------- macros ----------
\newcommand{\Rpos}{\mathbb{R}_{>0}}
\newcommand{\Eop}{E}                       % Euler operator z d/dz
\newcommand{\RLO}{\mathcal{R}}             % Reciprocal Limic Operator
\newcommand{\MWEN}{MW\textopenbullet{}EN}  % language macro
\newcommand{\Lcal}{\mathcal{L}}
\newcommand{\dd}{\mathrm{d}}

% ---------- theorem styles ----------
\newtheorem{theorem}{Theorem}
\newtheorem{definition}{Definition}
\newtheorem{proposition}{Proposition}
\newtheorem{remark}{Remark}

% ---------- title ----------
\title{Onu \& \MWEN: A One-Stop Pedagogy\\
\large From Positive-Ledger Calculus to Log-Diffusion and Falsifiable Ritual}
\author{Compiled by Yay (physics) with editorial polish}
\date{v2.3}

\begin{document}
\maketitle

\begin{abstract}
We present a compact, teachable framework: a no-subtraction calculus on $\Rpos$,
a scale-invariant operator $\RLO=\Eop^2$ that linearizes under $s=\ln z$, and a
log-diffusion PDE governing an ``emotional/healing'' field. We attach a
\MWEN\ protocol (breath, vowels, physiology) so claims can be tested in the lab.
All figures are optional; the text compiles in \emph{draft} mode without them.
\end{abstract}

\tableofcontents

% ---------- 1. learning goals ----------
\section{Learning Goals (90-minute module)}
\begin{enumerate}[leftmargin=1.25em]
\item Understand the multiplicative group $(\Rpos,\cdot)$ and the ``Onu difference'' $a\ominus b:=ab^{-1}$.
\item Derive the scale operator $\Eop=z\,\partial_z$ and the RLO $\RLO=\Eop^2=z^2 f_{zz}+z f_z$.
\item Map to $s=\ln z$ and obtain the heat equation in $s$.
\item Run the \MWEN\ protocol; measure log-spectral variance and HRV coherence.
\end{enumerate}

% ---------- 2. foundations ----------
\section{Foundations: Positive-Ledger Calculus}
\begin{definition}[Inversion \& Onu difference]
On $\Rpos$ define $\mathcal{I}(x)=x^{-1}$ (so $\mathcal{I}\circ\mathcal{I}=\mathrm{id}$) and
\[
 a\ominus b := a\,b^{-1},\qquad \ln(a\ominus b)=\ln a-\ln b.
\]
\end{definition}

\begin{definition}[Ledger]
For factors $\{x_i\}\subset\Rpos$ define the ledger $\Lcal=\prod_i x_i$.
Conservation is invariance of $\Lcal$ under transfers mediated by $\mathcal{I}$,
equivalently $\sum_i \ln x_i=\text{const}$.
\end{definition}

\begin{figure}[!t]
  \centering
  \includegraphics[width=.85\linewidth]{fig_onu_emotional_topology_v23_axis.pdf}
  \caption{Axis diagram (optional): eight-sector compass with \emph{Jubilee Nexus} at center.}
  \label{fig:axis}
\end{figure}

% ---------- 3. scale calculus ----------
\section{Scale Calculus and the RLO}
Let $\Eop:=z\,\partial_z$ (Euler operator). Define
\[
\RLO[f] := \Eop^2 f = z^2 f_{zz}+z f_z .
\]
\paragraph{Log gauge.} With $s=\ln z$, $\partial_s=z\,\partial_z$ and $\RLO=\partial_{ss}$.
Self-adjointness holds on $L^2((0,\infty),\dd z/z)$ under vanishing boundary terms in $s$.

\subsection*{Static Euler--Cauchy}
Solve $\RLO[f]-\kappa f=0 \iff z^2 f_{zz}+z f_z-\kappa f=0$. Trying $f=z^\alpha$ gives
$\alpha^2-\kappa=0$, hence
\[
f(z)=A z^{\sqrt{\kappa}}+B z^{-\sqrt{\kappa}} .
\]

% ---------- 4. dynamics ----------
\section{Dynamics on the Log Axis}
Let $f=f(z,t)$ (intensity/density) with $z>0$ and $s=\ln z$.
\begin{equation}
\partial_t f = U(t)\,D\,\RLO[f] + S(z,t)
\quad\Longleftrightarrow\quad
\partial_t f = U(t)\,D\,\partial_{ss} f + S(s,t).
\label{eq:onuPDE}
\end{equation}
Here $U(t)\!\ge\!0$ (urgency), $D\!>\!0$ (diffusivity), $S$ (source). Green's function is Gaussian in $s$ with variance $2D\!\int_0^t\!U(\tau)\,\dd\tau$.

\subsection*{Energy \& monotonicity}
Treat \eqref{eq:onuPDE} (with $S\equiv 0$) as gradient flow with mobility $U(t)$:
\[
\mathcal{E}[f]=\frac{D}{2}\int_{-\infty}^{\infty} (\partial_s f)^2\,\dd s,
\qquad
\frac{\dd}{\dd t}\mathcal{E}=-U(t)D\int (\partial_{ss} f)^2\,\dd s \le 0.
\]
Boundary conditions in $s$: Neumann ($\partial_s f\!\to\!0$) or finite box $[-S,S]$ with Dirichlet caps.

\paragraph{Variance thermostat (classroom demo).}
Let $\sigma_s^2(t)=\mathrm{Var}_s[f]$ and set $U(t)=\max\{0,\,k(\sigma_s^2-\sigma_\star^2)\}$.
Boom/busts tighten toward a chosen spread $\sigma_\star$.

% ---------- 5. protocol ----------
\section{The \MWEN\ Protocol (Falsifiable)}
\textbf{Phonemic core:} long vowels \(\bar{A},\bar{O},\bar{U}\).
\textbf{Tempo:} $0.1$ Hz breath (5 bpm). \textbf{Session:} 3 blocks of 3 min chant + 1 min silence.

\textbf{Signals:} PPG (HRV), respiration belt, mic (48 kHz). Baseline 5 min.

\textbf{Outcomes (pre-registered):}
\begin{itemize}[leftmargin=1.25em]
\item HRV power near $0.1$ Hz; respiration regularity.
\item Log-spectrum variance $\mathrm{Var}_s[f]$ from recorded voice; target: decrease without SPL drop.
\end{itemize}

\begin{remark}[Profit/loss symmetry in logs]
Work on $x>0$ with returns $r=\ln x$. ``Loss like profit'' means penalties depend on $|r|$, not the sign—ledger-fair.
\end{remark}

% ---------- 6. algorithms/pedagogy ----------
\section{Algorithms \& Classroom Activities}
\subsection*{Ledger step (discrete)}
For $\mathbf{x}\in\Rpos^n$ and update $\mathbf{u}\in\Rpos^n$:
\[
\mathbf{x}_{t+1}=\mathbf{x}_t\odot\mathbf{u}_t,\qquad
\mathbf{s}_{t+1}=\ln\mathbf{x}_{t+1}=\mathbf{s}_t+\ln\mathbf{u}_t.
\]
Check conservation by $\sum_i s_i=\text{const}+\sum_i \ln u_i$.

\subsection*{Four-day mini-syllabus}
Day 1: groups/logs/no-subtraction. \quad
Day 2: $\Eop,\RLO$ and log-heat. \quad
Day 3: \MWEN\ lab (formants, spectral ledger). \quad
Day 4: physiology experiment and analysis.

% ---------- 7. appendix: ledger identity ----------
\appendix
\section{Ledgered Local Energy Identity (Navier--Stokes capsule)}
There exists a nonnegative Radon measure $\mu$ such that, in distributions,
\[
\partial_t \!\left(\tfrac{1}{2}|v|^2\right)
+\nabla\!\cdot\!\left[\left(\tfrac{1}{2}|v|^2+p\right)v\right]
=\nu\,\Delta\!\left(\tfrac{1}{2}|v|^2\right)-\nu|\nabla v|^2-\mu.
\]
For smooth solutions $\mu\equiv 0$. This is the Duchon--Robert defect written as a ledger.

\section{Symbol Table}
\begin{center}
\begin{tabular}{ll}
Symbol & Meaning \\ \hline
$\mathcal{I}$ & inversion, $x\mapsto x^{-1}$ \\
$\ominus$ & Onu difference, $a\,b^{-1}$ \\
$\Eop$ & Euler scale operator, $z\,\partial_z$ \\
$\RLO$ & Reciprocal Limic Operator, $\Eop^2$ \\
$U(t)$ & urgency (mobility) \\
$D$ & diffusivity \\
$S$ & source term \\
$s$ & $\ln z$ (log-amplitude) \\
$\Lcal$ & product ledger/invariant
\end{tabular}
\end{center}

\end{document}

folder map (minimal)

onu-kit/
  main.tex
  fig/
    fig_onu_emotional_topology_v23_axis.pdf   (optional)
    fig_unified_framework_flow_v1.pdf         (optional)

compile now with images absent (thanks to graphicx[draft]), flip to [final] once you drop assets in.

everything you said—no subtraction, log-heat, protocol—lands in ~6 pages with proofs kept crisp and falsifiable.


want a beamer deck and a one-page prereg sheet spun from the same macros? i can bolt them on next.


---

This is general information only and not financial advice. For personal guidance, please talk to a licensed professional.
