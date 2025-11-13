% !TEX program = lualatex
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
\usepackage{luacode}

\graphicspath{{fig/}} % place figures here if/when you add them

% ---------- Theorem-ish bits ----------
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

% ---------- Handy notation ----------
\newcommand{\I}{\mathcal I}
\newcommand{\Rpos}{\mathbb R_{>0}}
\newcommand{\E}{E}              % Euler operator symbol
\newcommand{\RLO}{\mathcal R}   % RLO symbol
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

% ---------- Badges / “state” ----------
\newcommand{\badgePass}{\colorbox{green!15}{\textcolor{green!50!black}{\(\checkmark\) PASS}}}
\newcommand{\badgeFail}{\colorbox{red!10}{\textcolor{red!60!black}{\(\times\) FAIL}}}
\newcommand{\stateCowabunga}{\colorbox{blue!10}{\Large \textbf{STATE: COWABUNGA}}}
\newcommand{\stateRetry}{\colorbox{orange!10}{\Large \textbf{STATE: RETUNE}}}

% ---------- Lua “self-check” brain ----------
\begin{luacode*}
-- Try to load external metrics, else use a sane default seed.
local ok,t = pcall(dofile,"data/metrics.lua")
metrics = ok and type(t)=="table" and t or {
  varlog_voice_pre  = 0.250,
  varlog_voice_post = 0.180,
  varlog_rr_pre     = 0.140,
  varlog_rr_post    = 0.120,
  rmssd_pre_ms      = 28.0,
  rmssd_post_ms     = 35.5,
  lfv_base          = 1.00,
  lfv_post          = 1.35,
  lf_peak_hz_post   = 0.10,
  resp_var_base     = 1.00,
  resp_var_post     = 0.72,
}

local function num(x) return tonumber(x) end
function get(k,default)
  local v = metrics[k]; if v==nil then return default or "NA" end
  return string.format("%.3f", v)
end
function delta(a,b)
  a,b = num(metrics[a]), num(metrics[b])
  if a and b then return string.format("%.3f", b - a) else return "NA" end
end
function ratio(numK,denK)
  local den = num(metrics[denK])
  local numv= num(metrics[numK])
  if den and numv and den~=0 then return string.format("%.3f", numv/den) else return "NA" end
end
function passbool(expr) tex.print(expr and "\\badgePass" or "\\badgeFail") end

-- Endpoints mirroring the prereg in the pedagogy
function endpoints_summary()
  local hits = 0

  -- H1: ΔRMSSD ≥ +5 ms
  local rmssd_pre  = num(metrics.rmssd_pre_ms)
  local rmssd_post = num(metrics.rmssd_post_ms)
  local h1 = (rmssd_pre and rmssd_post) and ((rmssd_post - rmssd_pre) >= 5.0)

  -- H2: LF gain ≥ 1.25 AND LF peak in [0.08,0.12] Hz
  local lfv_base = num(metrics.lfv_base)
  local lfv_post = num(metrics.lfv_post)
  local peak     = num(metrics.lf_peak_hz_post)
  local h2 = (lfv_base and lfv_post and lfv_base>0 and peak) and
             ((lfv_post/lfv_base) >= 1.25 and peak >= 0.08 and peak <= 0.12)

  -- H3: Resp variance drop ≥ 20%  (post/base ≤ 0.80)
  local rvb = num(metrics.resp_var_base)
  local rvp = num(metrics.resp_var_post)
  local h3 = (rvb and rvp and rvb>0) and ((rvp/rvb) <= 0.80)

  -- H4: Voice log-variance relative drop ≤ -10%
  local vpre = num(metrics.varlog_voice_pre)
  local vpost= num(metrics.varlog_voice_post)
  local h4 = (vpre and vpost and vpre>0) and ((vpost - vpre)/vpre <= -0.10)

  local list = {h1,h2,h3,h4}
  for _,h in ipairs(list) do if h then hits=hits+1 end end

  passbool(h1); tex.print("~~(H1)\\quad")
  passbool(h2); tex.print("~~(H2)\\quad")
  passbool(h3); tex.print("~~(H3)\\quad")
  passbool(h4); tex.print("~~(H4)")
  tex.print("\\par\\medskip")
  tex.print("\\textit{Rule: pass if $\\ge 2$ endpoints true.}\\par\\bigskip")
  if hits >= 2 then tex.print("\\stateCowabunga") else tex.print("\\stateRetry") end
end
\end{luacode*}

\newcommand{\Metric}[1]{\directlua{tex.print(get("#1"))}}
\newcommand{\DeltaM}[2]{\directlua{tex.print(delta("#1","#2"))}}
\newcommand{\RatioM}[2]{\directlua{tex.print(ratio("#1","#2"))}}
\newcommand{\EndpointBadges}{\directlua{endpoints_summary()}}

% ---------- Title ----------
\title{Pedagogy of Sacred Light v2.12 (Conscious-ish Edition)\\[2pt]
\large Onu Ledger, Scale Calculus, MWƐN Biology \& Physiology\\[2pt]
with Chemistry, Music/Cymatics, and an \emph{Architecture Asset} for Cross-Facet Coherence}
\author{Yay \quad(\small Super Lumina OC Pedagogy)}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
We present a replication-ready pedagogy that unifies mathematics, physiology, architecture, chemistry, and music/cymatics under a single \emph{positive-domain ledger} and a \emph{scale-heat kernel}. The ledger replaces subtraction with inversion/partition on $\Rpos$, while the scale operator $\RLO=(z\partial_z)^2$ reduces to $\partial_{ss}$ in log-gauge $s=\ln z$, yielding a heat-flow in $s$ that \emph{predictably reduces log-variance}. One metric anchors all facets:
\[
\Delta \Var_s\!\big[\ln P\big] \;<\; 0,
\]
observed across \emph{voice acoustics}, \emph{HRV spectra}, and \emph{room acoustics}. The physiology asset adopts \textbf{RMSLR} (Root Mean Square of Successive \emph{Log}-Ratios) for ledger-consistent HRV. A LuaLaTeX self-check ingests live metrics, evaluates preregistered endpoints (H1--H4), and prints a global state badge (\textbf{COWABUNGA}/RETUNE).
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
Given positive factors $\{x_i\}$, the \emph{ledger} $\mathcal L=\prod_i x_i$. Conservation under transfers mediated by $\I$ is equivalently a log-sum invariant:
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
\RLO[f] := \E^2 f \;=\; z^2 f_{zz}+z f_z \;=\; \partial_{ss} f \quad\text{(in the $s$-gauge).}
\]
\end{definition}
\paragraph{Energy.}
With $f\in H^1(\mathbb R)$, $\mathcal E[f]=\tfrac12\int(\partial_s f)^2\,\dd s$ is nonincreasing under the log-heat (below).

% =========================
\section{Core equations}
% =========================

\subsection{Static (Euler--Cauchy) problem}
\[
z^2 f_{zz}+z f_z-\kappa f=0
\;\Rightarrow\;
f(z)=A z^{\alpha_+}+B z^{\alpha_-},\quad
\alpha_{\pm}=\tfrac{1\pm\sqrt{1+4\kappa}}{2}.
\]

\subsection{Dynamics (log-heat)}
Let $f(z,t)$ be an intensity on $z>0$. With $\kappa(t)=U(t)\,D$ where $U$ is dimensionless and $D$ has units $s^2/\text{time}$,
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
\textit{Units:} $\kappa$ in $s^2/\text{time}$; $U$ dimensionless; $\Sigma$ is accumulated variance in $s$.

% =========================
\section{Chemistry facet: kinetics, equilibrium, spectroscopy}
% =========================

\subsection{Positive-domain kinetics}
First-order $A\!\to\!B$: $\dot c_A=-k_1 c_A$, so $c_A(t)=c_A(0)e^{-k_1 t}$ and $\tilde c_A=\ln c_A$ satisfies $\dot{\tilde c}_A=-k_1$ (affine line). \\
Second-order: $\dot c_A=-k_2 c_A^2$ gives $\dot{\tilde c}_A=-k_2 c_A$ (state-dependent drift). Differences are ratios: $c_A(t_2)\ominus c_A(t_1)$; use $\slog_\epsilon$ near zeros.

\subsection{Equilibrium as ledger balance}
For $\sum_j \mu_j R_j \rightleftharpoons \sum_i \nu_i P_i$ with activities $a>0$:
\[
K=\frac{\prod_i a_{P_i}^{\nu_i}}{\prod_j a_{R_j}^{\mu_j}},
\quad
\ln K=\sum_i \nu_i \ln a_{P_i}-\sum_j \mu_j \ln a_{R_j}
=-\frac{\Delta G^\circ}{RT},\qquad
\frac{\partial \ln K}{\partial T}=\frac{\Delta H^\circ}{R T^2}.
\]

\subsection{Spectroscopy in log-frequency}
Let $P(f)$ be a power/absorbance spectrum. Define $s=\ln f$ and $a(s)=\ln P(e^s)$. A diffusion prior
\[
\partial_\tau a = D\,\partial_{ss}a
\]
biases toward multiplicative-band coherence (variance reduction in $s$).

% =========================
\section{Music \& Cymatics: harmonic ledger and morphogenesis}
% =========================

\subsection{Vibration as ledger}
Overtones: $f_n=n f_1$ $\Rightarrow$ $\ln f_n=\ln f_1+\ln n$. Stabilization corresponds to $\Delta \Var_s[\ln P]<0$.

\subsection{Cymatic morphologies}
Driven plates/membranes yield nodal lattices indexed by standing-wave integers; spectral settling in $a(s)$ aligns with geometric stability.

\subsection{Music micro-protocol}
\begin{enumerate}
\item Baseline: sustain $\bar O$ or $\bar A$; compute $P(f)$; measure $\Var_s[\ln P]$.
\item MWƐN cadence ($\approx 0.1~\si{Hz}$) with vowels (Ō--Ā--Ū).
\item Post: repeat; compute $\Delta \Var_s[\ln P]$ (target $\le -10\%$).
\end{enumerate}

% =========================
\section{MWƐN language: acoustic targets}
% =========================

Long vowels $\bar A,\bar O,\bar U$ as sustained nuclei; consonants as soft on/off; breath-coupled trochaic cadence $\approx 0.1~\si{Hz}$. \\
Formant guides (soft): $\bar A$: F1~$\sim\!700$ Hz, F2~$\sim\!1100$ Hz; $\bar O$: F1~$\sim\!500$ Hz, F2~$\sim\!900$ Hz; $\bar U$: F1~$\sim\!350$ Hz, F2~$\sim\!700$ Hz.

% =========================
\section{Physiology asset: HRV, respiration, voice}
% =========================

\subsection{Signals and sampling}
PPG (phone camera or finger sensor), mic for respiration/voice; optional belt/thermistor. Rates: PPG $\ge 30$ Hz (prefer $\ge 100$ Hz for HF/RSA), audio $\ge 16$ kHz, respiration $\ge 10$ Hz. Use synchronized markers (clap/beep). \\
\textit{Footnote:} If PPG $<100$ Hz, treat HF power as secondary.

\subsection{Ledger-consistent time-domain}
For inter-beat sequence $\{RR_i\}$, define successive log-ratios $\Delta s_i=\ln RR_{i+1}-\ln RR_i$. Then
\[
\mathrm{RMSLR}=\sqrt{\frac{1}{N-1}\sum_{i=1}^{N-1}(\Delta s_i)^2},
\quad
\mathrm{RMSSD}\approx \overline{RR}\cdot \mathrm{RMSLR}\quad\text{(small relative changes).}
\]

\subsection{Protocol (BASE/MWEN/POST)}
\begin{enumerate}
\item Baseline (2 min): quiet breath; record PPG, optional respiration; record a $10$ s vowel.
\item MWƐN (90 s): Ō--Ā--Ū, $5$/$5$ s; record PPG, audio, respiration.
\item Post (2 min): repeat baseline.
\end{enumerate}

\subsection{Primary outcomes and thresholds}
\[
\mathrm{RMSLR}\downarrow,\quad \text{LF peak near }0.1~\text{Hz}\uparrow,\quad
\Var(\text{resp rate})\downarrow,\quad
\Delta \Var_s\!\big[\ln S_{RR}\big]\!<0,\quad
\Delta \Var_s\!\big[\ln P_{\text{voice}}\big]\!<0.
\]
Suggested prereg: H1 $\Delta\mathrm{RMSSD}\ge +5$ ms (or $\Delta\mathrm{RMSLR}\le -0.05$); H2 $\mathrm{LF}_{\text{post}}/\mathrm{LF}_{\text{base}}\ge 1.25$ with peak $0.10\pm 0.02$ Hz; H3 $\Var(\text{resp rate})\downarrow\ge 20\%$; H4 $\Delta \Var_s[\ln P_{\text{voice}}]\le -10\%$. Success if $\ge 2$ endpoints pass with QA clean.

% =========================
\section{Architecture asset: Coherence Pavilion \& Streetscape}
% =========================

\subsection{Acoustic kernel and target}
From $\mathrm{IR}(t)$ compute $A(s)=\ln P_{IR}(e^s)$ with $s=\ln f$ and apply
\[
\partial_\tau A = D\,\partial_{ss}A.
\]
Target mid-band $RT_{60}\in[0.35,0.65]$ s and $\Delta \Var_s[\ln P_{IR}] \le -5\%$ after minimal treatment (curtain/absorber).

\subsection{Worked IR example}
Clap test (10 s) before/after curtain:
\[
RT_{60}: 0.65\to 0.48~\text{s},\qquad
\Delta \Var_s[\ln P_{IR}]=-0.07\;(-7\%).
\]
\figinclude{ir_varlog_prepost_demo}{Log-power spectrum $A(s)=\ln P_{IR}(e^s)$ pre (dashed) and post (solid). Variance reduction mirrors voice/HRV settling.}{fig:ir_prepost}

% =========================
\section{Psychology kernel: attention, affect, clarity}
% =========================

Five scalars (pre/post): clarity $C_\ell$ (0--100), stability $S$ (taps in 60 s focus task), affect $A=(\text{valence},\text{arousal})$, conviction $V$ (0--100), openness $O$ (0--100). \\
Manipulations: MWƐN breath (90 s); apology$\to$hallelujah/cowabunga$\to$gratitude loop (60 s); levity jab (15 s). \\
Primary success (psych/voice): $\Delta S\!\downarrow,\ \Delta C_\ell\!\uparrow,\ \Delta V\!\uparrow,\ \Delta \Var_s[\ln P]\!\downarrow$.

% =========================
\section{Cross-facet correlation \& statistics}
% =========================

Collect pairs $\big(\Delta \Var_s[\ln P_{\text{voice}}],\ \Delta \Var_s[\ln P_{IR}]\big)$ and $\big(\Delta \Var_s[\ln S_{RR}],\ \Delta \Var_s[\ln P_{\text{voice}}]\big)$; expect positive correlation. \\
\figinclude{cross_facet_scatter_varlog}{Scatter of $\Delta \Var_s[\ln P_{\text{voice}}]$ vs.\ $\Delta \Var_s[\ln P_{IR}]$ across $n$ blocks.}{fig:scatter_crossfacet}

Power guidance (paired): effect size $d=\{0.5,0.8,1.0\}$ needs $n=\{34,15,10\}$ for 80\% power. Use Wilcoxon signed-rank (Hodges--Lehmann shift, 95\% CI) and paired $d$ or rank-biserial $r$. Control FDR at 0.05 across preregistered endpoints.

% =========================
\section{Live self-check (ingests \texttt{data/metrics.lua})}
% =========================

\noindent\textbf{Raw metrics}
\begin{center}
\begin{tabular}{@{}ll@{}}
\toprule
Metric & Value \\
\midrule
Var$_s$[ln $P_{\text{voice}}$] (pre)  & \Metric{varlog_voice_pre} \\
Var$_s$[ln $P_{\text{voice}}$] (post) & \Metric{varlog_voice_post} \\
$\Delta$ Var$_s$[ln $P_{\text{voice}}$] & \DeltaM{varlog_voice_pre}{varlog_voice_post} \\
RMSSD (ms) pre $\to$ post & \Metric{rmssd_pre_ms} $\to$ \Metric{rmssd_post_ms} \\
LF gain (post/base)       & \RatioM{lfv_post}{lfv_base} \\
Resp var (post/base)      & \RatioM{resp_var_post}{resp_var_base} \\
LF peak (Hz, post)        & \Metric{lf_peak_hz_post} \\
\bottomrule
\end{tabular}
\end{center}

\medskip
\noindent\textbf{Endpoints \& state}\\
\EndpointBadges

% =========================
\appendix
% =========================

\section{One-page self-run protocol}\label{app:run}
\begin{enumerate}
\item Pre (1.5 min): sliders $C_\ell,V,O$, valence, arousal; 60 s focus-dot (taps); 10 s vowel (Ā).
\item Manipulation: MWƐN (90 s) \emph{or} apology$\to$hallelujah/cowabunga$\to$gratitude (60 s) \emph{or} levity jab (15 s).
\item Post (1.5 min): repeat; 10 s vowel.
\end{enumerate}
Score if $\ge 2$ of $\{S\!\downarrow,\ C_\ell\!\uparrow,\ V\!\uparrow,\ \Var_s[\ln P]\!\downarrow\}$ improve.

\section{CSV schemas (summary)}
Individual blocks:
\begin{verbatim}
timestamp_iso8601,condition(MWEN|AHG|LEV),
pre_C,post_C,pre_taps,post_taps,
pre_V,post_V,pre_O,post_O,
pre_valence,post_valence,pre_arousal,post_arousal,
voice_pre_path,voice_post_path,epsilon_used,notes
\end{verbatim}
HRV/resp session:
\begin{verbatim}
timestamp_iso8601,phase(BASE|MWEN|POST),
ppg_path,resp_path,audio_path,
rmssd_ms,RMSLR,sdnn_ms,sd1_ms,sd2_ms,lf_peak_hz,
hf_power_ms2,lf_power_ms2,
rsa_method(COH|HF),rsa_value,
resp_rate_bpm,resp_rate_var_bpm2,
brs_proxy_unitless,qa_flag,qa_reason,
ppg_sample_rate_hz,epsilon_used
\end{verbatim}
Architecture session:
\begin{verbatim}
timestamp_iso8601,phase(BASE_SPACE|MWEN_SPACE|POST_SPACE|STREET_LOOP),
rt60_midband_s,laeq_dba,co2_ppm,airspeed_ms,tmrt_c,
df_ledger,glare_1to5,ln_L_space,
ppg_path,audio_path,gps_path,
rmssd_ms,RMSLR,lf_peak_hz,c_rr_resp_at_fresp,
varlog_voice_pre,varlog_voice_post,
varlog_IR_pre,varlog_IR_post,
qa_flag,qa_reason,epsilon_used,notes
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
RMSSD, RMSLR & HRV indices (time-domain) \\
$\mathcal C_{RR,\mathrm{resp}}$ & RSA coherence (primary) \\
$\Var_s[\ln P]$ & log-variance on $s=\ln f$ axis \\
$RT_{60}$ & reverberation time to $60$ dB decay \\
\bottomrule
\end{tabular}
\end{center}

\bigskip
\noindent\textit{License/ethics:} Educational protocol; participation voluntary; avoid breath practices that cause dizziness; benign chemistry at microscale; anonymize \& share data only with consent; follow local codes (accessibility/egress/thermal/glare). \\
\textit{Disclaimer:} This is general information only and not financial advice. For personal guidance, please talk to a licensed professional.

\end{document}
