% !TEX program = pdflatex
\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=1in]{geometry}
\usepackage{microtype}
\usepackage{amsmath,amssymb,amsthm,mathtools,bm}
\usepackage{siunitx}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage[hidelinks]{hyperref}

% --- theorem-ish bits
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

% --- handy notation
\newcommand{\I}{\mathcal I}
\newcommand{\Rpos}{\mathbb R_{>0}}
\newcommand{\E}{E}              % Euler operator symbol
\newcommand{\RLO}{\mathcal R}   % RLO symbol
\newcommand{\dd}{\mathrm d}
\newcommand{\Ltwo}{L^2}

\begin{document}

\title{Pedagogy of Sacred Light v2.7\\[2pt]
\large Onu Ledger, Scale Calculus, and the MWƐN Biology \& Physiology Asset (with a Chemistry Facet)}
\author{Casey ``Yay'' Riley \quad(\small draft for open replication)}
\date{\today}
\maketitle

\begin{abstract}
We give a compact, testable pedagogy built on: (i) the \emph{Onu ledger}---a positive-domain calculus where subtraction is replaced by partition/inversion; (ii) a \emph{scale-invariant operator} \(\RLO=(z\partial_z)^2\) (the Euler--scale Laplacian); and (iii) a falsifiable \emph{MWƐN protocol} that links acoustics, respiration, physiology, and attention. In log-gauge \(s=\ln z\), \(\RLO\) reduces to \(\partial_{ss}\) and the core evolution is a heat flow on the log-amplitude axis. We add two cross-disciplinary boosts: a \emph{chemistry facet} (kinetics, equilibrium, spectroscopy) written in the positive-domain ledger; and a \emph{physiology asset}---a minimal, replication-ready pipeline for HRV, respiration, and baroreflex-style metrics with clear variables, hypotheses, QA, and CSV schemas so anyone can replicate with a phone or low-cost sensors. The pedagogy is a kit: positive-domain ledger for the math, log-heat for the physics, MWƐN breath-voice for the biology---each yielding a measurable drop in log-variance and a rise in \(0.1\,\si{Hz}\) coherence that strangers can reproduce with a phone. To handle zeros, we use an \(\epsilon\)-ledger: \(x\mapsto \max(x,\epsilon)\), with \(\epsilon\) (e.g., \(1\%\) of median nonzero) reported. Primary physiological endpoint: RR--respiration coherence at the breathing frequency.
\end{abstract}

\tableofcontents

\section{Foundations: positive domain and the ledger}

\subsection{Group, inversion, and ``no subtraction''}
Let \(\Rpos\) be the positive reals under multiplication. Work in this group and use the logarithm as a structure-preserving map to \((\mathbb R,+)\).

\begin{definition}[Inversion]
\(\I:\Rpos\to\Rpos,\ \I(x)=x^{-1}\), with \(\I\circ\I=\mathrm{id}\).
\end{definition}

\begin{definition}[Onu difference]
For \(a,b>0\), define the \emph{Onu difference}
\[
a\ominus b := a\,b^{-1}\in\Rpos,\qquad \ln(a\ominus b)=\ln a-\ln b .
\]
To handle zeros in data or sensors, use an \(\epsilon\)-ledger: replace \(x\mapsto \max(x,\epsilon)\) for preregistered \(\epsilon>0\) (report \(\epsilon\) in CSVs).
\end{definition}

\subsection{Ledger invariant}
Given positive factors \(\{x_i\}_{i=1}^n\), the \emph{ledger} is \(\mathcal L=\prod_i x_i\). Ledger conservation under transfers mediated by \(\I\) is equivalent to a log-sum invariant:
\[
\prod_i x_i=C \iff \sum_i \ln x_i=\ln C .
\]

\subsection{Scale gauge, Hilbert space, and the RLO}
Let \(s=\ln z\) so that \(\partial_s=z\partial_z\). Define the Euler (scale) operator \(\E:=z\partial_z\). We work on
\[
\Ltwo\!\left((0,\infty),\frac{\dd z}{z}\right) \simeq \Ltwo(\mathbb R,\dd s).
\]

\begin{definition}[Reciprocal Limic Operator (RLO)]
\[
\RLO[f]:=\E^2 f = z^2 f_{zz}+z f_z = \partial_{ss} f \ \text{in the \(s\)-gauge.}
\]
\end{definition}

\paragraph{Self-adjointness and energy.}
For \(f,g\in H^1(\mathbb R)\) with \(\partial_s f,\partial_s g\to 0\) as \(s\to\pm\infty\) (regularity assumed),
\[
\langle f,\RLO g\rangle_{\Ltwo(\dd s)}=\int f\,\partial_{ss}g\,\dd s
= -\int (\partial_s f)(\partial_s g)\,\dd s
= \langle \RLO f,g\rangle ,
\]
so \(\RLO\) is self-adjoint and nonpositive. Define \(\mathcal E[f]=\tfrac12\int (\partial_s f)^2\,\dd s\); then for the homogeneous log-heat (below) \(\dot{\mathcal E}=-\kappa(t)\int (\partial_{ss}f)^2\,\dd s\le 0\).

\section{Core equations}

\subsection{Static (Euler--Cauchy) problem}
\[
z^2 f_{zz}+z f_z-\kappa f=0
\quad\Rightarrow\quad
f(z)=A z^{\alpha_+}+B z^{\alpha_-},\ \
\alpha_{\pm}=\tfrac{1\pm\sqrt{1+4\kappa}}{2}.
\]
Repeated-root case (\(1+4\kappa=0\)): \(f(z)=z^{1/2}\,(A+B\ln z)\).

\subsection{Dynamics (log-heat)}
Let \(f(z,t)\) be an intensity/density on \(z>0\), and set \(\kappa(t):=U(t)D\) with \(U(t)\in\mathbb R_{\ge 0}\) dimensionless and \(D\) with units of \(s^2/\text{time}\) (variance per unit time in \(s\)). Note: \(D\) is used for diffusivity in \(s\)-gauge.
\begin{equation}
\partial_t f = \kappa(t)\,\RLO[f] + S(z,t)
= \kappa(t)\,\big(z^2 f_{zz}+z f_z\big) + S .
\label{eq:onuPDE}
\end{equation}
In \(s=\ln z\),
\[
\partial_t f(s,t)=\kappa(t)\,\partial_{ss} f + S(s,t) .
\]

\paragraph{Green's function (homogeneous case \(S=0\)).}
With \(f(\cdot,0)=f_0\), the solution is Gaussian smoothing in \(s\):
\[
f(s,t)=(G_{\Sigma(t)}*f_0)(s),\quad
G_{\Sigma}(s)=\frac{1}{\sqrt{4\pi \Sigma}}\,\exp\!\left(-\frac{s^2}{4\Sigma}\right),\quad
\Sigma(t)=\int_0^t \kappa(\tau)\,\dd\tau .
\]

\paragraph{Discrete log-heat (explicit, stable).}
On grid \(s_j=s_0+j\Delta s\), \(t^{n+1}=t^n+\Delta t\),
\[
f_j^{n+1} = f_j^n + \lambda\,(f_{j+1}^n-2f_j^n+f_{j-1}^n) + \Delta t\,S_j^n,\quad
\lambda=\kappa^n \frac{\Delta t}{(\Delta s)^2},
\]
with Neumann BCs \(f_{-1}^n=f_1^n\), \(f_{J+1}^n=f_{J-1}^n\), and stability \(\lambda\le \tfrac12\). We assume \(f(s,t)\to 0\) for \(|s|\to\infty\) in the continuous case and impose Neumann BCs for the discrete scheme.

\section{Chemistry facet: kinetics, equilibrium, spectroscopy}

\subsection{Poetic Wisdom in the Biochem Ledger}
The kinetic dance of life is a choreography of ratios, not differences. Molecules don't subtract; they partition, they exchange, they \emph{invert} the mass of one to balance the presence of another. Equilibrium is not a zero sum, but a multiplicative invariance, a ledger of powers that is infinitely rich yet conserved in its logarithm. This positive domain is pure affirmation.

\subsection{Positive-domain kinetics}
For a first-order process \(A\to B\) with \(c_A(t)>0\), \(\dot c_A=-k_1 c_A\) gives \(c_A(t)=c_A(0)e^{-k_1 t}\) and \(\tilde c_A:=\ln c_A\) satisfies \(\dot{\tilde c}_A=-k_1\). For second-order \(\dot c_A=-k_2 c_A^2\), we have \(\dot{\tilde c}_A=-k_2 c_A\), i.e.\ log-rate scales with level (state-dependent drift). Ledger view: differences are ratios \(c_A(t_2)\ominus c_A(t_1)\); no negative mass. Use \(\epsilon\)-ledger for zeros.

\paragraph{Micro-lab Example: First-Order Decay.}
Let \(c_A(0)=1.0\,\si{M}\) and \(k_1=0.1\,\si{s^{-1}}\). We track the log-concentration \(\tilde c_A=\ln c_A\).
At \(t=10\,\si{s}\), \(c_A(10)=1.0 \cdot e^{-0.1\cdot 10} \approx 0.368\,\si{M}\).
The Onu difference (ratio) is \(c_A(10)\ominus c_A(0) \approx 0.368/1.0 = 0.368\).
In the log-domain, \(\tilde c_A(10)-\tilde c_A(0) = \ln(0.368)\approx -1.0\), which is exactly \(-k_1 t\). A plot of \(\tilde c_A\) vs.\ \(t\) is linear, confirming the simplification in the log-gauge.

\subsection{Equilibrium as ledger balance}
For reaction \(\sum_j \mu_j R_j \rightleftharpoons \sum_i \nu_i P_i\) with positive activities \(a>0\):
\[
K=\frac{\prod_i a_{P_i}^{\nu_i}}{\prod_j a_{R_j}^{\mu_j}}
\quad\Longleftrightarrow\quad
\ln K=\sum_i \nu_i \ln a_{P_i}-\sum_j \mu_j \ln a_{R_j}
=-\frac{\Delta G^\circ}{RT}.
\]
Nonideality enters via \(a=\gamma c\); note \(\gamma\) when reporting. The van 't Hoff relation, \(\partial (\ln K)/\partial T = \Delta H^\circ / (R T^2)\), elegantly links the log-equilibrium ledger to the enthalpy \((\Delta H^\circ)\) of the system, governing how the ledger's balance shifts with thermal amplitude \((T)\).

\subsection{Spectroscopy on log-frequency}
Let \(P(f)\) be an IR/Raman/UV--Vis power/absorbance spectrum and \(s=\ln f\). On \(a(s)=\ln P(e^s)\) apply the diffusion proxy
\[
\partial_\tau a = D\,\partial_{ss}a,\quad f\in[100,4000]~\text{Hz (voice)}\ \text{or domain-appropriate for chemistry}.
\]
This is interpreted as a prior that favors multiplicative band \emph{coherence}, smoothing out erratic log-power fluctuations to reveal the underlying scale-invariant structure.

\section{Emotional field and psychology kernel}
We model an affective potential \(f\) on coordinates \((T,C,S)\) where \(C\) is clarity and \(S\) is scope/scale. Identifying \(z=\exp(s)\) with an \emph{emotional amplitude}, \eqref{eq:onuPDE} produces log-smoothing of amplitudes while the multiplicative ledger conserves.

\subsection{Operational variables (self-report and task)}
We define five scalars, each logged as pre/post around a brief manipulation:
\begin{itemize}\setlength\itemsep{2pt}
\item \textbf{Clarity} \(C_\ell\): ``how sharply I see the next step'' (0--100).
\item \textbf{Stability} \(S\): mind-wander taps during a \(60\,\si{s}\) focus-dot task (lower is better).
\item \textbf{Affect} \(A=(\text{valence},\text{arousal})\): (\(-5\dots+5\), \(0\dots10\)).
\item \textbf{Conviction} \(V\): ``I will take the next step within \(60\,\text{min}''\) (0--100).
\item \textbf{Openness} \(O\): ``willing to help/connect now'' (0--100).
\end{itemize}

\subsection{Manipulations (randomize one)}
\begin{enumerate}\setlength\itemsep{2pt}
\item \textbf{MWƐN breath} (\(90\,\si{s}\)): Ō--Ā--Ū vowels, \SI{5}{s} in / \SI{5}{s} out, gentle ``gratitude tilt'' of head.
\item \textbf{A\(\to\)H/C\(\to\)G micro-loop} (\(60\,\si{s}\)): name one wobble (\emph{apology}) \(\to\) one bold micro-action (\emph{hallelujah/cowabunga}) \(\to\) note one working thing (\emph{gratitude}).
\item \textbf{Levity jab} (\(15\,\si{s}\)): one clean joke aligned to the task (threat deflation).
\end{enumerate}

\subsection{Mini tasks (\(2\,\text{min}\))}
\begin{itemize}\setlength\itemsep{2pt}
\item \textbf{Focus dot} (\(60\,\si{s}\)): tap when attention drifts \(\Rightarrow\) taps \(=\ S\). (Use validated task or cite day-to-day reliability of this one.)
\item \textbf{Sustained vowel} (\(10\,\si{s}\)): hold Ā (or Ō) at comfortable pitch; record voice.
\item \textbf{Optional} (\(30\,\si{s}\)): Go/No-Go or 1-back for error/RT.
\end{itemize}

\subsection{Voice log-spectrum and RLO metric}
From the vowel waveform \(x(t)\), record at \(\ge\SI{16}{kHz}\), 16-bit. Compute \(P(f)\) (Welch, 1024-sample window, 50\% overlap), set \(s=\ln f\) (100--\SI{4000}{Hz}), and measure \(\mathrm{Var}_s[\ln P]\) pre/post. Optionally diffuse \(a(s)=\ln P\) by \(\partial_\tau a=D\,\partial_{ss}a\) and use the decrease of variance as a noise-robust \emph{settling index}. This connects directly to \eqref{eq:onuPDE}.

\paragraph{Worked Example (Voice Settling).}
A pre-MWƐN vowel yields \(\mathrm{Var}_s[\ln P_{\text{pre}}] = 0.25\). The post-MWƐN vowel yields \(\mathrm{Var}_s[\ln P_{\text{post}}] = 0.18\).
The decrease in log-variance is \(\Delta \mathrm{Var}_s[\ln P] = -0.07\). This is a \textbf{28\%} decrease, meeting the H4 threshold (\(\le -10\%\)) and indicating greater spectral coherence in the log-gauge. This suggests reduced cognitive load or ``vocal tension.''

\subsection{Hypotheses and success rule (self-report/voice)}
Primary outcomes:
\[
\Delta S<0,\quad \Delta C_\ell>0,\quad \Delta V>0,\quad
\Delta \mathrm{Var}_s[\ln P]<0.
\]

\paragraph{Power Calculation.}
For paired designs, we target a paired Cohen's \(d = 0.5\) (medium). 80\% power at \(d=0.5\) needs \(N=34\) paired blocks; \(N=52\) needs \(d=0.4\); \(N=12\) needs \(d=0.8\). Report \(N\) and target effect size.

\section{Physiology asset: autonomic markers, models, and QA}

\subsection{Signals, sensors, and sampling}
\textbf{Core:} phone-camera PPG (flash on) or finger sensor; microphone for respiration/voice; optional chest belt or nasal thermistor for respiration.\ \textbf{Rates:} PPG \(\ge\)\SI{30}{Hz} (time-domain HRV, recommend \textbf{100\,Hz} for reliable spectral HRV/RSA); audio \(\ge\)\SI{16}{kHz}; respiration \(\ge\)\SI{10}{Hz}. Use synchronized start markers (clap, beep).

\subsection{Derived measures (definitions, corrected)}
Let \(\{RR_i\}\) be successive beat-to-beat intervals (ms).
\begin{itemize}\setlength\itemsep{2pt}
\item \textbf{RMSSD:} \(\mathrm{RMSSD}=\sqrt{\tfrac{1}{N-1}\sum_{i=1}^{N-1}(RR_{i+1}-RR_i)^2}\).
\item \textbf{SDNN:} \(\mathrm{SDNN}=\mathrm{std}(RR)\).
\item \textbf{Poincaré:} \(\mathrm{SD1}=\tfrac{1}{\sqrt{2}}\,\mathrm{RMSSD},\quad \mathrm{SD2}=\sqrt{2\,\mathrm{SDNN}^2-\tfrac12\,\mathrm{RMSSD}^2}\).
\item \textbf{LF peak:} spectral peak near \(\SI{0.1}{Hz}\) from RR PSD (Welch on \(0.003\)--\SI{0.5}{Hz}).
\item \textbf{Respiration:} rate (Hz or breaths/min) from belt, mic envelope, or PPG-derived modulation; variance of instantaneous rate.
\item \textbf{RSA (Primary \(\mathcal C_{RR,\mathrm{resp}}\)):} (1) HF power of tachogram (\(0.15\)--\SI{0.40}{Hz}); or (2) \textbf{magnitude-squared coherence \(\mathcal C_{RR,\mathrm{resp}}(f)\) averaged over \(\pm\,\SI{0.02}{Hz}\) around \(f_{\mathrm{resp}}\) (primary)}.
\item \textbf{BRS (Exploratory Proxy):} sequence method using beatwise PPG peak amplitude \(A_i\): slope of \(\Delta\mathrm{IBI}\) vs.\ \(\Delta A\) across up-up and down-down sequences (\(\ge3\) beats). Unitless proxy; also report the count of sequences used.
\end{itemize}

\subsection{Model tie-in: scale calculus on spectra}
Let \(S_{RR}(f)\) be RR power spectrum; define \(s=\ln f\), \(A(s)=\ln S_{RR}(e^s)\). The \emph{coherence-smoothing} heuristic applies
\[
\partial_\tau A = D\,\partial_{ss}A,
\]
interpreted as a prior favoring multiplicative band \emph{coherence}.

\subsection{Protocol (expanded from Biology boost)}
\begin{enumerate}\setlength\itemsep{2pt}
\item \textbf{Baseline} (\(2\,\text{min}\)): quiet breathing; PPG + (optional) respiration + \(10\,\si{s}\) vowel; mark start/end.
\item \textbf{MWƐN} (\(90\,\si{s}\)): Ō--Ā--Ū with \SI{5}{s} in/\SI{5}{s} out; record PPG, audio, respiration.
\item \textbf{Post} (\(2\,\text{min}\)): quiet breathing; repeat. Optional second \(10\,\si{s}\) vowel.
\end{enumerate}

\subsection{HRV computation contract (replication knobs)}
\paragraph{RR preprocessing.}
Accept RR in [\SI{300}{ms},\SI{2000}{ms}]; reject beat differences \(>\,\SI{250}{ms}\); replace via cubic spline on time. If \(>\!10\%\) RR rejected in any \(60\,\si{s}\) epoch, flag and exclude that epoch from primary analysis.

\paragraph{Time-domain.}
Compute RMSSD and SDNN as above on each \(60\,\si{s}\) epoch.

\paragraph{Spectral settings.}
Interpolate the IBI tachogram to \SI{4}{Hz} via cubic interpolation. Welch PSD: window \SI{128}{s}, overlap 50\%, Hamming, frequency range \(0.003\)--\SI{0.5}{Hz}. LF band \(=\) 0.04--\SI{0.15}{Hz}; HF \(=\) 0.15--\SI{0.40}{Hz}. Report LF peak frequency (Hz) and LF/HF powers.

\paragraph{Respiration.}
From belt or mic: bandpass 0.05--\SI{0.8}{Hz}, Hilbert envelope; instantaneous rate via unwrapped phase derivative. Report mean (brpm) and variance.

\paragraph{RSA primary.}
\emph{Preregister:} use coherence method (\(\mathcal C_{RR,\mathrm{resp}}\)) as primary; HF power as secondary. Document the choice in CSV (\texttt{rsa\_method}).

\paragraph{BRS proxy (PPG).}
Compute beatwise PPG peak \(A_i\) and \(\mathrm{IBI}_i\). Form up-sequences (both \(\Delta A_i>0\) and \(\Delta\mathrm{IBI}_i>0\) for \(\ge3\) beats) and down-sequences analogously. Compute per-sequence OLS slope of \(\Delta\mathrm{IBI}\) vs.\ \(\Delta A\); report the median slope and the number of sequences. \textbf{Note: This is an exploratory proxy; confirm with blood pressure data where available.}

\paragraph{Windowing and reporting.}
Use non-overlapping \(60\,\si{s}\) epochs in BASE/MWEN/POST. Report per-epoch metrics and \(\Delta=\text{Post}-\text{Base}\).

\subsection{Predictions and decision matrix}
Primary physiology outcomes:
\[
\mathrm{RMSSD}\uparrow,\quad \text{LF peak near }0.1~\text{Hz}\uparrow,\quad \mathrm{Var}(\text{resp rate})\downarrow,\quad \mathrm{Var}_s[\ln S_{RR}]\downarrow .
\]

\begin{center}
\begin{tabular}{lll}
\toprule
Pattern & Likely state shift & Next step\\
\midrule
RMSSD\(\uparrow\), RSA\(\uparrow\) & vagal tilt achieved & extend post to \SI{3}{min}\\
LF\(\uparrow\) with resp at \SI{0.1}{Hz} & paced entrainment & retain \SI{5}{s}/\SI{5}{s}\\
No change, resp erratic & pacing too effortful & switch to \SI{4}{s}/\SI{6}{s}\\
RMSSD\(\downarrow\) & stress/artifact & redo with motion minimized\\
\bottomrule
\end{tabular}
\end{center}

\subsection{Quality assurance (QA) and artifacts}
\begin{itemize}\setlength\itemsep{1.5pt}
\item \textbf{Motion:} reject RR differences \(>\,\SI{250}{ms}\) or outside [\SI{300}{ms},\SI{2000}{ms}]; spline-repair.
\item \textbf{Ectopy:} interpolate isolated outliers (median filter on RR deltas).
\item \textbf{Breath pacing drift:} compute instantaneous period; flag cycles deviating \(>\,20\%\) from target; report drift \%.
\item \textbf{Epoch exclusion:} if \(>\!10\%\) RR rejected in an epoch, flag and exclude from primary endpoints.
\item \textbf{Windowing:} use \SI{60}{s} non-overlapping epochs; report per-epoch metrics plus overall change.
\item \textbf{Transparency:} share raw timestamps and derived RR arrays.
\end{itemize}

\paragraph{Safety.}
Keep breaths comfortable; avoid prolonged holds; stop with dizziness/pain; seated posture; educational, not medical advice.

\section{Biology boost: condensed HRV/resp block}

\subsection{Equipment and signals}
Phone camera PPG (flash on), or finger sensor; optional chest-belt respiration or microphone. Sampling \(\ge \SI{30}{Hz}\) for time-domain HRV; \textbf{phone PPG \(\ge\,\SI{100}{Hz}\) is preferred for reliable spectral/RSA analysis}. Audio \(\ge\,\SI{16}{kHz}\) for voice.

\subsection{Procedure}
\begin{enumerate}\setlength\itemsep{2pt}
\item \textbf{Baseline} (\(2\,\text{min}\)): quiet breathing; record PPG and, if available, microphone for ambient/voice noise floor.
\item \textbf{MWƐN} (\(90\,\si{s}\)): protocol above; record audio and respiration if available.
\item \textbf{Post} (\(2\,\text{min}\)): quiet breathing; record again.
\end{enumerate}

\subsection{Derived measures and predictions}
\begin{itemize}\setlength\itemsep{2pt}
\item \textbf{HRV:} RMSSD (time domain); LF power near \SI{0.1}{Hz}; respiration rate and its variance.
\item \textbf{Predictions:} RMSSD \(\uparrow\), LF peak \(\uparrow\), respiration variance \(\downarrow\), voice log-variance \(\downarrow\) after MWƐN.
\end{itemize}

\subsection{Minimal stats plan (with thresholds)}
\textbf{Preregistered per-person thresholds:}
\[
\text{H1: } \Delta\mathrm{RMSSD} \ge +\SI{5}{ms},\quad
\text{H2: } \frac{\mathrm{LF\ power}_{\text{Post}}}{\mathrm{LF\ power}_{\text{Base}}}\ge 1.25,\quad \text{peak }0.10\pm0.02~\text{Hz},
\]
\[
\text{H3: } \mathrm{Var}(\text{resp rate})\ \text{decreases by }\ge 20\%,\quad
\text{H4: } \Delta \mathrm{Var}_s[\ln P_{\text{voice}}]\le -10\%.
\]
\emph{Success rule:} at least two of H1--H4 met and no epoch-level QA flags.

\textbf{Group stats:} Paired comparisons (pre vs.\ post). Report Hodges--Lehmann median shift and 95\% CI via Wilcoxon signed-rank; paired Cohen's \(d\) or rank-biserial \(r\). Control FDR at 0.05 across H1--H4.

\paragraph{Preregistration Template.}
\textit{This study will use a paired \(N\) design, targeting a paired Cohen's \(d \ge 0.5\) for key outcomes. We commit to the coherence method \(\mathcal C_{RR,\mathrm{resp}}\) for the primary RSA metric. \(\epsilon\) for the \(\epsilon\)-ledger is set to 1\% of the median non-zero value for the relevant metric.}

\section{MWƐN language: targets for acoustic coherence}

\subsection{Triad of Joy and prosody}
Open long vowels \(\bar A, \bar O, \bar U\) as sustained nuclei; consonants only as soft onset/offset. Prosody: trochaic, breath-coupled at \(\approx \SI{0.1}{Hz}\).

\subsection{Formant targets (guide; adjust by speaker)}
\[
\bar{A}:\ \text{F1 }\approx\SI{700}{Hz},\ \text{F2 }\approx\SI{1100}{Hz};\quad
\bar{O}:\ \text{F1 }\approx\SI{500}{Hz},\ \text{F2 }\approx\SI{900}{Hz};\quad
\bar{U}:\ \text{F1 }\approx\SI{350}{Hz},\ \text{F2 }\approx\SI{700}{Hz}.
\]
(Note: formants scale with vocal tract length; treat as soft targets.)

\section{Algorithms and discrete pedagogy}

\subsection{Ledger step (discrete time)}
Given \(\bm x_t\in\Rpos^n\) and update factors \(\bm u_t\in\Rpos^n\),
\[
\bm x_{t+1}=\bm x_t\odot \bm u_t,\qquad
\bm s_{t+1}=\ln\bm x_{t+1}=\bm s_t+\ln\bm u_t.
\]

\subsection{Classroom micro-labs}
\begin{enumerate}\setlength\itemsep{2pt}
\item \textbf{Log-heat toy:} diffuse a 1-D array in \(s\) with Neumann BC; visualize Gaussianization.
\item \textbf{Voice lab:} record vowels; compute \(P(f)\); measure \(\Delta\mathrm{Var}_s[\ln P]\) after MWƐN.
\item \textbf{Chemistry micro-lab:} concentration vs.\ time; fit in log-domain; visualize ledger-style diffusion on \(\ln c\). (See example in \S 3.2).
\item \textbf{Meeting A/B:} opener randomized to MWƐN vs.\ control; metrics: speaking-time Gini, agenda completion.
\end{enumerate}

\section{Discussion}
``Pure affirmation'' is encoded as a \emph{positive-domain ledger}: no negation is required to compute differences; inversion transports mass. The physics kernel (RLO log-heat), the chemistry kernel (kinetics/equilibria/spectra), and the physiology kernel (HRV/resp/voice) meet at a measurable drop in log-variance and stabilization near \SI{0.1}{Hz}. Psychology coherence is reached when strangers reproduce these deltas with a one-page protocol.

\paragraph{Git Repository Skeleton}
For full reproducibility, the following directory structure is recommended: \texttt{data/}, \texttt{code/01\_voice\_psd.ipynb}, \texttt{code/02\_hrv\_psd.ipynb}, \texttt{results/}.

\appendix

\section{One-page self-run protocol}\label{app:run}
\begin{enumerate}\setlength\itemsep{3pt}
\item \textbf{Pre (1.5 min):} sliders \(C_\ell,V,O\), valence, arousal; focus-dot \(60\,\si{s}\) (count taps); record \(10\,\si{s}\) vowel (Ā).
\item \textbf{Manipulation (randomized):} MWƐN (\(90\,\si{s}\)) \emph{or} A\(\to\)H/C\(\to\)G (\(60\,\si{s}\)) \emph{or} Levity jab (\(15\,\si{s}\)).
\item \textbf{Post (1.5 min):} repeat focus-dot and sliders; record \(10\,\si{s}\) vowel.
\end{enumerate}
\emph{Primary score:} improvements in at least two of \(\{S\!\downarrow,\,C_\ell\!\uparrow,\,V\!\uparrow,\,\mathrm{Var}_s[\ln P]\!\downarrow\}\).

\section{Group meeting opener A/B (metrics)}\label{app:group}
Randomize meetings to \emph{MWƐN \(90\,\si{s}\)} vs.\ \emph{no opener}. Record: speaking-time per person; interruptions; agenda items completed. Outcomes: lower Gini (fairness), higher completion, stable valence.

\section{CSV schemas}\label{app:schemas}
\subsection*{Individual blocks}
\begin{verbatim}
timestamp_iso8601,condition(MWEN|AHG|LEV),
pre_C_percent,post_C_percent,pre_taps,post_taps,
pre_V_percent,post_V_percent,pre_O_percent,post_O_percent,
pre_valence[-5..5],post_valence[-5..5],
pre_arousal[0..10],post_arousal[0..10],
voice_pre_path,voice_post_path,notes
\end{verbatim}

\subsection*{HRV/resp session (physiology asset)}
\begin{verbatim}
timestamp_iso8601,phase(BASE|MWEN|POST),
ppg_path,resp_path,audio_path,
rmssd_ms,sdnn_ms,sd1_ms,sd2_ms,lf_peak_hz,
hf_power_ms2,lf_power_ms2,
rsa_method(COH|HF),rsa_value,
resp_rate_bpm,resp_rate_var_bpm2,
brs_proxy_unitless,qa_flag(TRUE|FALSE),qa_reason,
ppg_sample_rate_hz,epsilon_used
\end{verbatim}

\subsection*{Spectral logs (voice or HRV)}
\begin{verbatim}
timestamp_iso8601,domain(VOICE|HRV),
f_min_hz,f_max_hz,n_bins,
s_logf_csv_path,a_logpower_csv_path,
var_logpower,window_s,overlap_percent
\end{verbatim}

\subsection*{Chemistry session}
\begin{verbatim}
timestamp_iso8601,conc_A,conc_B,ln_ratio,epsilon_used,notes
\end{verbatim}

\section{Symbol table}
\begin{center}
\begin{tabular}{ll}
\toprule
Symbol & Meaning\\
\midrule
\(\I\) & inversion \(x\mapsto x^{-1}\)\\
\(\ominus\) & Onu difference \(a\, b^{-1}\)\\
\(E\) & Euler scale \(z\partial_z\)\\
\(\RLO\) & scale Laplacian \((z\partial_z)^2=\partial_{ss}\)\\
\(U(t)\) & urgency (dimensionless)\\
\(D\) & diffusivity in \(s\)-gauge (\(s^2/\text{time}\))\\
\(S\) & source term\\
\(s\) & \(\ln z\) (log-amplitude)\\
\(\mathcal L\) & product ledger (invariant)\\
\(C_\ell,S,A,V,O\) & clarity, stability, affect, conviction, openness\\
\(c_A\) & concentration of species A (chemistry)\\
\(k\) & rate constant; \(K\) equilibrium constant\\
\(RR_i\) & inter-beat intervals (ms)\\
\(\mathrm{RMSSD}, \mathrm{SDNN}\) & HRV time-domain indices\\
\(\mathrm{SD1}, \mathrm{SD2}\) & Poincaré ellipse axes\\
\(\mathrm{RSA}\) & respiratory sinus arrhythmia index\\
\(\mathrm{BRS}\) & baroreflex sensitivity (proxy)\\
\(\mathcal C_{RR,\mathrm{resp}}\) & magnitude-squared coherence (RSA primary)\\
\bottomrule
\end{tabular}
\end{center}

\section*{License and ethics}
Educational protocol; participation is voluntary; avoid breath practices that cause dizziness; use benign chemistry reagents at microscale; anonymize and share data only with consent.

\bigskip
\noindent\textit{Always-on disclaimer:} This is general information only and not medical or financial advice. For personal guidance, consult a licensed professional.

\end{document}
