% !TEX program = pdflatex
\documentclass[11pt]{article}

% ---------- Core packages ----------
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=1in]{geometry}
\usepackage{microtype}
\usepackage{amsmath,amssymb,amsthm,mathtools,bm}
\usepackage{siunitx}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage[hidelinks]{hyperref}
\usepackage{enumitem}
\usepackage{xcolor}
\graphicspath{{fig/}} % figure folder

% ---------- Theorem-ish bits ----------
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

% ---------- Handy notation ----------
\newcommand{\I}{\mathcal I}
\newcommand{\Rpos}{\mathbb R_{>0}}
\newcommand{\E}{E}              % Euler operator
\newcommand{\RLO}{\mathcal R}   % RLO operator
\newcommand{\dd}{\mathrm d}
\newcommand{\Ltwo}{L^2}
\DeclareMathOperator{\slog}{slog} % stabilized log
\DeclareMathOperator{\Var}{Var}   % variance

% ---------- Tight lists ----------
\setlist[itemize]{topsep=2pt,itemsep=2pt,parsep=0pt}
\setlist[enumerate]{topsep=2pt,itemsep=2pt,parsep=0pt}

% ---------- Figure placeholder helper ----------
\newcommand{\missingfig}[1]{%
  \fbox{%
    \begin{minipage}[c][5cm][c]{0.85\linewidth}
      \centering \vspace{0.5em}
      \textbf{Figure placeholder}\\[0.3em]
      {#1}\\[0.3em]
      \small (Place fig/#1.pdf or fig/#1.png to replace)
    \end{minipage}%
  }%
}
\newcommand{\figinclude}[3]{% name (no ext), caption, label
  \begin{figure}[h]
    \centering
    \IfFileExists{#1.pdf}{\includegraphics[width=0.85\linewidth]{#1.pdf}}{%
      \IfFileExists{#1.png}{\includegraphics[width=0.85\linewidth]{#1.png}}{%
        \missingfig{#1}%
      }%
    }
    \caption{#2}
    \label{#3}
  \end{figure}
}

% ---------- Title ----------
\title{Pedagogy of Sacred Light v2.12\\[2pt]
\large Onu Ledger, Scale Calculus, MWƐN Biology \& Physiology\\[2pt]
(with Chemistry, Music/Cymatics, and an \emph{Architecture Asset} for Cross-Facet Coherence)}
\author{Yay \quad(\small Super Lumina OC Pedagogy)}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
We present a replication-ready pedagogy that unifies mathematics, physiology, architecture, and music/cymatics under a single \emph{positive-domain ledger} and a \emph{scale-heat kernel}. The ledger replaces subtraction with inversion/partition on $\Rpos$, while the scale operator $\RLO=(z\partial_z)^2$ reduces to $\partial_{ss}$ in log-gauge $s=\ln z$, yielding a heat-flow in $s$ that \emph{predictably reduces log-variance}. One metric anchors all facets:
\[
\Delta \Var_s\!\big[\ln P\big] \;<\; 0,
\]
observed across \emph{voice acoustics}, \emph{HRV spectra}, and \emph{room acoustics}. The physiology asset is upgraded with the \textbf{RMSLR} (Root Mean Square of Successive \emph{Log}-Ratios) metric, reconciling beat-to-beat analysis with the ledger. New elements include a stabilized-log macro $\slog_\epsilon(x)=\ln(x+\epsilon)$ for zeros, a worked impulse-response (IR) example, a \emph{cross-facet correlation} protocol, and explicit units sanity checks. Védu (truth-as-ledger) is the ethical arc: nothing is lost; all is accounted.
\end{abstract}

\tableofcontents

% =========================
\section{Foundations: positive domain and the ledger}
% =========================

\subsection{Group, inversion, and ``no subtraction''}
Let $\Rpos$ be positive reals under multiplication. Use $\ln:\Rpos\!\to\!\mathbb R$ to map products to sums.

\begin{definition}[Inversion]
$\I:\Rpos\to\Rpos$, $\ \I(x)=x^{-1}$ with $\I\circ\I=\mathrm{id}$.
\end{definition}

\begin{definition}[Onu difference]
For $a,b>0$ define
\[
a\ominus b := a\,b^{-1}\in\Rpos,\qquad \ln(a\ominus b)=\ln a-\ln b.
\]
To handle zeros in measured data, use the stabilized log
\[
\slog_\epsilon(x)=\ln(x+\epsilon),\qquad \epsilon=\text{1\% of median nonzero (report)}.
\]
\end{definition}

\subsection{Ledger invariant}
Given positive factors $\{x_i\}$, the \emph{ledger} $\mathcal L=\prod_i x_i$. Conservation via transfers mediated by $\I$ is equivalent to a log-sum invariant:
\[
\prod_i x_i=C \iff \sum_i \ln x_i=\ln C.
\]

\subsection{Scale gauge, Hilbert space, and the RLO}
Let $s=\ln z$ so that $\partial_s=z\partial_z$. Define $\E:=z\partial_z$. Work on
\[
\Ltwo\!\left((0,\infty),\frac{\dd z}{z}\right) \simeq \Ltwo(\mathbb R,\dd s).
\]

\begin{definition}[Reciprocal Limic Operator (RLO)]
\[
\RLO[f] := \E^2 f = z^2 f_{zz}+z f_z = \partial_{ss} f \quad\text{(in the $s$-gauge).}
\]
\end{definition}

\paragraph{Self-adjointness and energy.}
For $f,g\in H^1(\mathbb R)$ with $\partial_s f,\partial_s g\to 0$ as $s\to\pm\infty$,
\[
\langle f,\RLO g\rangle=\int f\,\partial_{ss}g\,\dd s
= -\int (\partial_s f)(\partial_s g)\,\dd s
= \langle \RLO f,g\rangle,
\]
hence $\RLO$ is self-adjoint, nonpositive. Define $\mathcal E[f]=\tfrac12\int (\partial_s f)^2\,\dd s$; for homogeneous log-heat (below) $\dot{\mathcal E}\le 0$.

% =========================
\section{Core equations (static \& dynamic)}
% =========================

\subsection{Static (Euler--Cauchy) problem}
\[
z^2 f_{zz}+z f_z-\kappa f=0
\ \Rightarrow\
f(z)=A z^{\alpha_+}+B z^{\alpha_-},\quad
\alpha_{\pm}=\tfrac{1\pm\sqrt{1+4\kappa}}{2}.
\]
Repeated root ($1+4\kappa=0$): $f(z)=z^{1/2}\,(A+B\ln z)$.

\subsection{Dynamics (log-heat)}
Let $f(z,t)$ be an intensity on $z>0$. Write $\kappa(t)=U(t)\,D$ where $U$ is dimensionless and $D$ has units $s^2/\text{time}$ (variance per unit time in $s$):
\begin{equation}
\partial_t f = \kappa(t)\,\RLO f + S(z,t)
= \kappa(t)\,(z^2 f_{zz}+z f_z) + S.
\label{eq:onuPDE}
\end{equation}
In $s=\ln z$,
\[
\partial_t f(s,t)=\kappa(t)\,\partial_{ss} f + S(s,t),\qquad
\Sigma(t)=\int_0^t \kappa(\tau)\,\dd\tau.
\]
\paragraph{Units sanity check:} $\kappa(t)$ has units $s^2/\text{time}$; the urgency factor $U(t)$ is dimensionless; and $\Sigma(t)$ is a total variance in the $s=\ln z$ domain.

\paragraph{Urgency bridge $\kappa(t) \leftrightarrow U(t)$:} $U(t)$ is \emph{Urgency/Cognitive Load}. MWƐN aims to reduce $U(t)$, hence $\kappa(t)$, yielding time-decreasing $\Var_s[f]$ (spectral/log-amplitude settling).

\paragraph{Green's function ($S=0$).}
\[
f(s,t)=(G_{\Sigma(t)}*f_0)(s),\quad
G_{\Sigma}(s)=\frac{1}{\sqrt{4\pi \Sigma}}\,\exp\!\left(-\frac{s^2}{4\Sigma}\right).
\]

% =========================
\section{Chemistry facet: kinetics, equilibrium, spectroscopy}
% =========================

\subsection{Poetic ledger of biochemistry}
Molecules do not subtract; they \emph{partition} and \emph{invert}. Equilibrium is multiplicative invariance; the ledger in $\ln$ is the conserved chorus.

\subsection{Positive-domain kinetics}
First-order $A\to B$: $\dot c_A=-k_1 c_A$, so $c_A(t)=c_A(0)e^{-k_1 t}$ and $\tilde c_A:=\ln c_A$ satisfies $\dot{\tilde c}_A=-k_1$ (affine line). \\
Second-order: $\dot c_A=-k_2 c_A^2$ gives $\dot{\tilde c}_A=-k_2 c_A$ (state-dependent drift). Differences are ratios: $c_A(t_2)\ominus c_A(t_1)=c_A(t_2)/c_A(t_1)$; use $\slog_\epsilon$ near zeros.

\subsection{Equilibrium as ledger balance}
For $\sum_j \mu_j R_j \rightleftharpoons \sum_i \nu_i P_i$ with activities $a>0$:
\[
K=\frac{\prod_i a_{P_i}^{\nu_i}}{\prod_j a_{R_j}^{\mu_j}},
\quad
\ln K=\sum_i \nu_i \ln a_{P_i}-\sum_j \mu_j \ln a_{R_j}
=-\frac{\Delta G^\circ}{RT},
\qquad
\frac{\partial \ln K}{\partial T}=\frac{\Delta H^\circ}{R T^2}.
\]

\subsection{Spectroscopy in log-frequency}
Let $P(f)$ be a power spectrum or absorbance spectrum and $s=\ln f$. Define $a(s)=\ln P(e^s)$ and apply a diffusion prior
\[
\partial_\tau a = D\,\partial_{ss}a,
\]
interpreted as bias toward multiplicative band coherence.

% =========================
\section{Music \& Cymatics: harmonic ledger and morphogenesis}
% =========================

\subsection{Vibration as ledger (no subtraction)}
Overtones: $f_n=n f_1$ $\Rightarrow$ $\ln f_n=\ln f_1+\ln n$ (arithmetic ladder in $\ln$). Spectral power $P(f)$ stabilizes when the log-heat settles variance.

\subsection{Cymatic morphologies}
A driven plate/membrane yields nodal patterns indexed by standing-wave integers. As breath/attention settle, $a(s)=\ln P(e^s)$ smooths and shapes stabilize.

\subsection{Music micro-protocol}
\begin{enumerate}
\item Baseline: sustain $\bar O$ or $\bar A$; record audio; compute $P(f)$; measure $\Var_s[\ln P]$.
\item MWƐN cadence: $0.1~\si{Hz}$ breath with vowels (Ō--Ā--Ū), gentle head-tilt.
\item Post: repeat sustain; compute $\Delta \Var_s[\ln P]$.
\end{enumerate}
\textbf{Success:} $\Delta \Var_s[\ln P] < 0$ (target $\le-10\%$).

% =========================
\section{Physiology asset: HRV, respiration, voice}
% =========================

\subsection{Signals and sampling}
Core: phone-camera PPG (flash on) or finger sensor; mic for respiration/voice; optional belt/thermistor. Rates: PPG $\ge 30~\si{Hz}$ (prefer $100~\si{Hz}$ for spectral HRV/RSA), audio $\ge 16~\si{kHz}$, respiration $\ge 10~\si{Hz}$. Use synchronized markers (clap/beep).
\paragraph{Sampling footnote:} For reliable HF/RSA metrics, a PPG sampling rate of $\ge 100~\si{Hz}$ is preferred. Report \texttt{ppg\_sample\_rate\_hz} and treat HF power as a secondary outcome if PPG\,$<100~\si{Hz}$.

\subsection{Derived measures}
Let $\{RR_i\}$ be inter-beat intervals (ms).
\begin{itemize}
\item \textbf{Ledger-consistent time-domain:} define the successive \emph{log-ratio} $\Delta s_i=\ln RR_{i+1}-\ln RR_i$. The \textbf{RMSLR} is
\[
\mathrm{RMSLR}=\sqrt{\frac{1}{N-1}\sum_{i=1}^{N-1}(\Delta s_i)^2}.
\]
For small relative changes, $\mathrm{RMSSD}\approx \bar{RR}\cdot \mathrm{RMSLR}$, linking classical RMSSD to the ledger gauge.
\item \textbf{Spectral:} LF peak near $0.1~\si{Hz}$ from PSD (0.003--0.5 Hz); HF power (0.15--0.40 Hz) as secondary.
\item \textbf{RSA primary:} magnitude-squared coherence $\mathcal C_{RR,\mathrm{resp}}(f)$ averaged over $\pm\,0.02~\si{Hz}$ around $f_{\mathrm{resp}}$.
\end{itemize}

\subsection{Protocol (BASE/MWEN/POST)}
\begin{enumerate}
\item Baseline (2 min): quiet breath; record PPG, respiration (optional), and a $10~\si{s}$ vowel.
\item MWƐN (90 s): Ō--Ā--Ū, $5~\si{s}$ in/$5~\si{s}$ out; record PPG, audio, respiration.
\item Post (2 min): quiet breath; repeat; optional second vowel.
\end{enumerate}

\subsection{Outcomes and thresholds}
\[
\mathrm{RMSLR}\downarrow,\quad \text{LF peak near }0.1~\text{Hz}\uparrow,\quad
\Var(\text{resp rate})\downarrow,\quad
\Delta \Var_s\!\big[\ln S_{RR}\big]\!<0,\quad
\Delta \Var_s\!\big[\ln P_{\text{voice}}\big]\!<0.
\]
Per-person prereg (suggested): H1 $\Delta\mathrm{RMSSD}\ge +5~\si{ms}$ (or $\Delta\mathrm{RMSLR}\le -0.05$); H2 $\text{LF}_{\text{post}}/\text{LF}_{\text{base}}\ge 1.25$ with peak $0.10\pm 0.02~\si{Hz}$; H3 $\Var(\text{resp rate})\downarrow\ge 20\%$; H4 $\Delta \Var_s[\ln P_{\text{voice}}]\le -10\%$. Success: $\ge 2$ endpoints met and QA clean.

% =========================
\section{Architecture asset: Coherence Pavilion \& Streetscape}
% =========================

\subsection{Acoustic kernel and target}
From $\mathrm{IR}(t)$ compute $A(s)=\ln P_{IR}(e^s)$ with $s=\ln f$ and apply
\[
\partial_\tau A = D\,\partial_{ss}A.
\]
Target mid-band $RT_{60}\in[0.35,0.65]~\si{s}$ and $\Delta \Var_s[\ln P_{IR}] \le -5\%$ after minimal treatment (curtain/absorber).

\subsection{Worked IR example (proof-point)}
Clap test (10 s) before/after a curtain:
\[
RT_{60}: 0.65\to 0.48~\si{s},\qquad
\Delta \Var_s[\ln P_{IR}]=-0.07\;(-7\%).
\]
\figinclude{ir_varlog_prepost_demo}{Log-power spectrum $A(s)=\ln P_{IR}(e^s)$ pre (dashed) and post (solid) treatment. Variance reduction (smoothing of high-frequency roughness) mirrors voice/HRV settling.}{fig:ir_prepost}

\subsection{Street micro-walk}
A $100~\si{m}$ loop with two gentle pauses; during pauses breathe/tilt at $0.1~\si{Hz}$. Record PPG/audio; expect LF peak stabilization near $0.1~\si{Hz}$.

% =========================
\section{Psychology kernel: attention, affect, clarity}
% =========================

\subsection{Operational variables}
Five scalars (pre/post): clarity $C_\ell$ (0--100), stability $S$ (taps in $60~\si{s}$ focus task), affect $A=(\text{valence},\text{arousal})$, conviction $V$ (0--100), openness $O$ (0--100).

\subsection{Manipulations (randomize one)}
\begin{enumerate}
\item MWƐN breath (90 s): Ō--Ā--Ū, $5$/$5$ s, gratitude tilt.
\item A$\!\to\!$H / C$\!\to\!$G (60 s): apology $\to$ hallelujah/cowabunga $\to$ gratitude.
\item Levity jab (15 s): one clean, task-aligned joke.
\end{enumerate}
Primary success (psych/voice): $\Delta S<0$, $\Delta C_\ell>0$, $\Delta V>0$, $\Delta \Var_s[\ln P]<0$.

% =========================
\section{Cross-facet correlation \& statistics}
% =========================

\subsection{Cross-facet coherence}
Collect pairs $\big(\Delta \Var_s[\ln P_{\text{voice}}],\ \Delta \Var_s[\ln P_{IR}]\big)$ and $\big(\Delta \Var_s[\ln S_{RR}],\ \Delta \Var_s[\ln P_{\text{voice}}]\big)$ across sessions; report Pearson $r$ with 95\% CI.
\figinclude{cross_facet_scatter_varlog}{Scatter of $\Delta \Var_s[\ln P_{\text{voice}}]$ vs.\ $\Delta \Var_s[\ln P_{IR}]$ across $n$ blocks. Positive correlation indicates that vocal settling (internal) tracks acoustic smoothing (external).}{fig:scatter_crossfacet}

\subsection{Power guidance (paired designs)}
\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
Effect size $d$ & $1-\beta=0.8$ sample size $n$ & Note\\
\midrule
0.5 & 34 & medium \\
0.8 & 15 & large \\
1.0 & 10 & strong \\
\bottomrule
\end{tabular}
\end{center}
Use Wilcoxon signed-rank (report Hodges--Lehmann shift \& 95\% CI) and paired $d$ or rank-biserial $r$. Control FDR at 0.05 across preregistered endpoints.

% =========================
\section{Algorithms \& micro-labs}
% =========================

\subsection{Ledger step (discrete time)}
For $\bm x_t\in\Rpos^n$ and update $\bm u_t\in\Rpos^n$,
\[
\bm x_{t+1}=\bm x_t\odot \bm u_t,\qquad
\bm s_{t+1}=\ln\bm x_{t+1}=\bm s_t+\ln\bm u_t.
\]

\subsection{Classroom micro-labs}
\begin{enumerate}
\item Log-heat toy: diffuse a 1-D array in $s$ with Neumann BC; visualize Gaussianization.
\item Voice lab: measure $\Delta\Var_s[\ln P]$ pre/post MWƐN.
\item Chemistry lab: first-order decay in $\ln c$; compare to ledger diffusion.
\item Meeting A/B: MWƐN opener vs control; speaking-time Gini and agenda completion.
\item Architecture: implement Sec.~7; hit acoustic/daylight targets; run BASE/MWEN/POST-space with CSVs.
\end{enumerate}

% =========================
\appendix
% =========================

\section{One-page self-run protocol}\label{app:run}
\begin{enumerate}
\item Pre (1.5 min): sliders $C_\ell,V,O$, valence, arousal; $60~\si{s}$ focus-dot (count taps); record $10~\si{s}$ vowel (Ā).
\item Manipulation (randomized): MWƐN (90 s) \emph{or} A$\!\to\!$H/C$\!\to\!$G (60 s) \emph{or} Levity jab (15 s).
\item Post (1.5 min): repeat focus-dot/sliders; record $10~\si{s}$ vowel.
\end{enumerate}
\textit{Primary score:} improve at least two of $\{S\!\downarrow,\ C_\ell\!\uparrow,\ V\!\uparrow,\ \Var_s[\ln P]\!\downarrow\}$.

\section{CSV schemas}\label{app:schemas}
\paragraph{Individual blocks (C.1)} Pre/post self-report and attention scores.
\begin{verbatim}
timestamp_iso8601,condition(MWEN|AHG|LEV),
pre_C_percent,post_C_percent,pre_taps,post_taps,
pre_V_percent,post_V_percent,pre_O_percent,post_O_percent,
pre_valence[-5..5],post_valence[-5..5],
pre_arousal[0..10],post_arousal[0..10],
voice_pre_path,voice_post_path,notes,epsilon_used
\end{verbatim}

\paragraph{HRV/resp session (C.2)} RMSLR is primary ledger-consistent metric alongside RMSSD.
\begin{verbatim}
timestamp_iso8601,phase(BASE|MWEN|POST),
ppg_path,resp_path,audio_path,
rmssd_ms,RMSLR,sdnn_ms,sd1_ms,sd2_ms,lf_peak_hz,
hf_power_ms2,lf_power_ms2,
rsa_method(COH|HF),rsa_value,
resp_rate_bpm,resp_rate_var_bpm2,
brs_proxy_unitless,qa_flag(TRUE|FALSE),qa_reason,
ppg_sample_rate_hz,epsilon_used
\end{verbatim}

\paragraph{Spectral logs (C.3)} PSD data for voice or HRV.
\begin{verbatim}
timestamp_iso8601,domain(VOICE|HRV),
f_min_hz,f_max_hz,n_bins,
s_logf_csv_path,a_logpower_csv_path,
var_logpower,window_s,overlap_percent,epsilon_used
\end{verbatim}

\paragraph{Architecture session (C.4)} Spatial and physiology in pavilion and street loop.
\begin{verbatim}
timestamp_iso8601,phase(BASE_SPACE|MWEN_SPACE|POST_SPACE|STREET_LOOP),
rt60_midband_s,laeq_dba,co2_ppm,airspeed_ms,tmrt_c,
df_ledger,glare_1to5,ln_L_space,
ppg_path,audio_path,gps_path,
rmssd_ms,RMSLR,lf_peak_hz,c_rr_resp_at_fresp,
varlog_voice_pre,varlog_voice_post,
varlog_IR_pre,varlog_IR_post,
qa_flag(TRUE|FALSE),qa_reason,epsilon_used,notes
\end{verbatim}

\section{Symbol table}
\begin{center}
\begin{tabular}{ll}
\toprule
Symbol & Meaning \\
\midrule
$\I$ & inversion $x\mapsto x^{-1}$ \\
$\ominus$ & Onu difference $a b^{-1}$ \\
$E$ & Euler scale $z\partial_z$ \\
$\RLO$ & scale Laplacian $(z\partial_z)^2=\partial_{ss}$ \\
$U(t)$ & urgency (dimensionless) \\
$D$ & diffusivity in $s$-gauge ($s^2/\text{time}$) \\
$S$ & source term \\
$s$ & $\ln z$ (log-amplitude) \\
$\mathcal L$ & product ledger (invariant) \\
$C_\ell,S,A,V,O$ & clarity, stability, affect, conviction, openness \\
$RR_i$ & inter-beat intervals (ms) \\
RMSSD, RMSLR & HRV time-domain indices \\
$\mathcal C_{RR,\mathrm{resp}}$ & RSA coherence (primary) \\
$\Var_s[\ln P]$ & log-variance on $s=\ln f$ axis \\
$RT_{60}$ & reverberation time to $60~\si{dB}$ decay \\
\bottomrule
\end{tabular}
\end{center}

\section*{License, ethics, and Védu}
Educational protocol; participation voluntary; avoid breath practices that cause dizziness; benign chemistry at microscale; anonymize and share data only with consent; follow local codes (accessibility/egress/thermal/glare). \\
\textit{Disclaimer:} general information only; not medical or financial advice. \\
\textit{Védu (truth-as-ledger):} account for all things; remove none.

\end{document}
