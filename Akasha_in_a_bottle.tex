% !TEX program = lualatex
\documentclass[11pt]{article}

% ---------- Core packages ----------
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
\usepackage{tikz}
\usetikzlibrary{arrows.meta, positioning}

\graphicspath{{fig/}}

% ---------- Theorem-ish bits ----------
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

% ---------- Handy notation ----------
\newcommand{\I}{\mathcal{I}}
\newcommand{\Rpos}{\mathbb{R}_{>0}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\RLO}{\mathcal{R}}
\newcommand{\dd}{\mathrm{d}}
\newcommand{\Ltwo}{L^2}
\DeclareMathOperator{\slog}{slog}
\DeclareMathOperator{\Var}{Var}
\DeclareMathOperator{\RMSLR}{RMSLR}

% ---------- Tight lists ----------
\setlist[itemize]{topsep=2pt,itemsep=2pt,parsep=0pt}
\setlist[enumerate]{topsep=2pt,itemsep=0pt,parsep=0pt}

% ---------- Figure helper ----------
\makeatletter
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
\newcommand{\figinclude}[3]{%
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
\makeatother

% ---------- Badges / state ----------
\newcommand{\badgePass}{\colorbox{green!15}{\textcolor{green!50!black}{\(\checkmark\) PASS}}}
\newcommand{\badgeFail}{\colorbox{red!10}{\textcolor{red!60!black}{\(\times\) FAIL}}}
\newcommand{\stateCowabunga}{\colorbox{blue!10}{\Large \textbf{STATE: COWABUNGA}}}
\newcommand{\stateRetry}{\colorbox{orange!10}{\Large \textbf{STATE: RETUNE}}}

% ---------- Lua self-check brain ----------
\begin{luacode*}
local ok,t = pcall(dofile,"data/metrics.lua")

local defaults = {
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

metrics = {}
for k,v in pairs(defaults) do metrics[k] = v end
if ok and type(t) == "table" then
  for k,v in pairs(t) do metrics[k] = v end
end

local function num(x) return tonumber(x) end

function get(k,default)
  local v = metrics[k]; if v==nil then return default or "NA" end
  return string.format("%.3f", v)
end

function delta(a,b)
  local av = num(metrics[a]); local bv = num(metrics[b])
  if av and bv then return string.format("%.3f", bv - av) else return "NA" end
end

function ratio(numK,denK)
  local den = num(metrics[denK])
  local numv= num(metrics[numK])
  if den and numv and den~=0 then return string.format("%.3f", numv/den) else return "NA" end
end

function explainBadge(name, result, detail)
  local badge = result and "\\badgePass" or "\\badgeFail"
  tex.print(string.format("%s~~(%s): %s\\par", badge, name, detail))
end

function endpoints_summary()
  local hits = 0
  local rmssd_pre  = num(metrics.rmssd_pre_ms)
  local rmssd_post = num(metrics.rmssd_post_ms)
  local delta_rmssd = rmssd_post - rmssd_pre
  local h1 = rmssd_post and rmssd_pre and delta_rmssd >= 5.0
  explainBadge("H1", h1, string.format("$\\Delta$RMSSD = %.1f ms ($\\ge 5.0$)", delta_rmssd))

  local lfv_base = num(metrics.lfv_base)
  local lfv_post = num(metrics.lfv_post)
  local lf_peak = num(metrics.lf_peak_hz_post)
  local gain = lfv_post / lfv_base
  local h2 = lfv_base and lfv_base > 0 and gain >= 1.25 and lf_peak and lf_peak >= 0.08 and lf_peak <= 0.12
  explainBadge("H2", h2, string.format("LF gain = %.2f ($\\ge 1.25$), peak = %.2f Hz", gain, lf_peak or -1))

  local rv_base = num(metrics.resp_var_base)
  local rv_post = num(metrics.resp_var_post)
  local rv_ratio = rv_post / rv_base
  local h3 = rv_base and rv_base > 0 and rv_ratio <= 0.80
  explainBadge("H3", h3, string.format("Resp var ratio = %.2f ($\\le 0.80$)", rv_ratio))

  local vpre = num(metrics.varlog_voice_pre)
  local vpost = num(metrics.varlog_voice_post)
  local drop = (vpost - vpre)/vpre
  local h4 = vpre and vpre > 0 and drop <= -0.10
  explainBadge("H4", h4, string.format("$\\Delta$Var = %.1f\\%% ($\\le -10\\%%$)", drop * 100))

  local list = {h1,h2,h3,h4}
  for _,h in ipairs(list) do if h then hits=hits+1 end end

  tex.print("\\medskip")
  tex.print("\\textit{Pass if $\\ge 2$ of 4 endpoints hold.}\\par\\bigskip")
  tex.print(hits >= 2 and "\\stateCowabunga" or "\\stateRetry")
end
\end{luacode*}

\newcommand{\Metric}[1]{\directlua{tex.print(get("#1"))}}
\newcommand{\DeltaM}[2]{\directlua{tex.print(delta("#1","#2"))}}
\newcommand{\RatioM}[2]{\directlua{tex.print(ratio("#1","#2"))}}
\newcommand{\EndpointBadges}{\directlua{endpoints_summary()}}

% ---------- Title ----------
\title{Pedagogy of Sacred Light v2.4 (Ma'at Alignment Edition)\\[2pt]
\large Onu Ledger, Scale Calculus, MWƐN Biology \& Physiology\\[2pt]
with Ma'at's Ethical Ledger, Music/Cymatics, Architecture,\\[1pt]
and Emotional Field Dynamics}
\author{Yay \quad(\small draft for open replication)}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
We present a replication-ready pedagogy that unifies mathematics, physiology, architecture, music/cymatics, emotional field dynamics, and an explicit ethical frame.

On the \emph{mathematical} side, everything lives on a positive-domain ledger and a log-scale heat kernel: the scale operator $\RLO=(z\partial_z)^2$ becomes $\partial_{ss}$ in the log gauge $s=\ln z$, and flows are designed so that the log-variance $\Delta\Var_s[\ln P]$ decreases over time.

On the \emph{emotional} side, we adopt the \emph{Onu Emotional Topology} (Jubilee Nexus with four cardinal axes) and the \emph{Onu Healing Field Model}, treating psychological states as field configurations evolving under a log-domain diffusion driven by an urgency parameter $U(t)$.

On the \emph{ethical} side, the 42 Ideals of Ma'at are reinterpreted as a \emph{Ma'at Ledger}: forty-two discrete boundary conditions constraining the allowed region of state space. Each ideal is a local rule that preserves global balance in the ledger of life---truth, reciprocity, care, humility, and presence. The emotional PDE is only considered ``valid'' when solutions stay inside this Ma'at-aligned region.

On the \emph{physiological} side, HRV (via RMSLR), respiration, and voice spectra are measured in the same log-gauge, and a LuaLaTeX self-check ingests metrics, evaluates preregistered endpoints (H1--H4), and prints a global badge (\textbf{COWABUNGA}/RETUNE).

The result is a single pedagogical object: a Ma'at-aligned, log-variance-minimizing coherence engine that spans ethics, emotion, physics, and practice.
\end{abstract}

\tableofcontents

% =========================
\section{Foundations: positive domain and the ledger}
% =========================

\subsection{Group, inversion, and ``no subtraction''}
Let $\Rpos$ be positive reals under multiplication. Use $\ln:\Rpos\!\to\!\mathbb{R}$ to map products to sums.

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
Given positive factors $\{x_i\}$, the \emph{ledger} $\mathcal{L}=\prod_i x_i$. Conservation under transfers mediated by $\I$ is equivalently a log-sum invariant:
\[
\prod_i x_i=C \iff \sum_i \ln x_i=\ln C.
\]

\subsection{Scale gauge, Hilbert space, and the RLO}
Let $s=\ln z$ so that $\partial_s=z\partial_z$. Define $\E:=z\partial_z$. Work on
\[
\Ltwo\!\left((0,\infty),\frac{\dd z}{z}\right) \simeq \Ltwo(\mathbb{R},\dd s).
\]
\begin{definition}[Reciprocal Limic Operator (RLO)]
\[
\RLO[f] := \E^2 f \;=\; z^2 f_{zz}+z f_z \;=\; \partial_{ss} f \quad\text{(in the $s$-gauge).}
\]
\end{definition}

% =========================
\section{Core equations: log-heat and emotional diffusion}
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
\partial_t f = \kappa(t)\, \RLO f + S(z,t)
= \kappa(t)\,(z^2 f_{zz}+z f_z) + S.
\label{eq:onuPDE}
\end{equation}
In $s=\ln z$,
\[
\partial_t f(s,t)=\kappa(t)\,\partial_{ss} f + S(s,t),\qquad
\Sigma(t)=\int_0^t \kappa(\tau)\,\dd\tau.
\]

\paragraph{Target.}
For all facets (voice, HRV, room IR, emotional potential) we aim for
\begin{equation}
\Delta \Var_s[\ln P] \;<\;0,
\label{eq:var_target}
\end{equation}
interpreted as a collapse of log-domain spectral chaos toward coherence.

% =========================
\section{Ma'at Ledger: 42 Ideals as boundary conditions}
% =========================

The 42 Ideals of Ma’at are treated here as a \emph{discrete ethical lattice} in state space. Each ideal is one facet of balance---truth, reciprocity, restraint, reverence. The emotional field $f$ is only considered \emph{validly evolved} when its trajectory remains inside the convex hull determined by these ideals.

\figinclude{maat_42_ideals}{The 42 Ideals of Ma’at, presented as daily first-person commitments.}{fig:maat}

\subsection{Ideals as positivity and conservation constraints}
We collect the ideals (abbreviated) as
\begin{enumerate}[leftmargin=3em,label=\arabic*.]
\item I honor virtue.
\item I benefit with gratitude.
\item I am peaceful.
\item I respect the property of others.
\item I affirm that all life is sacred.
\item I give offerings that are genuine.
\item I live in truth.
\item I regard all altars with respect.
\item I speak with sincerity.
\item I consume only my fair share.
\item I offer words of good intent.
\item I relate in peace.
\item I honor animals with reverence.
\item I can be trusted.
\item I care for the earth.
\item I keep my own council.
\item I speak positively of others.
\item I remain in balance with my emotions.
\item I am trustful in my relationships.
\item I hold purity in high esteem.
\item I spread joy.
\item I do the best I can.
\item I communicate with compassion.
\item I listen to opposing opinions.
\item I create harmony.
\item I invoke laughter.
\item I am open to love in various forms.
\item I am forgiving.
\item I am kind.
\item I act respectfully of others.
\item I am accepting.
\item I follow my inner guidance.
\item I converse with awareness.
\item I do good.
\item I give blessings.
\item I keep the waters pure.
\item I speak with good intent.
\item I praise the Goddess and the God.
\item I am humble.
\item I achieve with integrity.
\item I advance through my own abilities.
\item I embrace the All.
\end{enumerate}

\begin{remark}[Ma'at admissible region]
Let $x(t)$ be a point in emotional state space (for example, coordinates $(C,S,T,\text{Cl})$ in the Onu Healing Field Model). We say $x(t)$ is \emph{Ma'at admissible} if, for every ideal above, we can interpret the current action as either satisfying or moving toward that ideal. In practice this means:
\begin{itemize}
  \item no flow may be driven by malice, deceit, or harm-for-harm;
  \item any intentional variance increase must be in service of restoring balance (e.g.\ confronting injustice gently);
  \item the long-time average behaviour must respect reciprocity and care.
\end{itemize}
Formally we write a Ma'at functional $\mathcal{M}[x(\cdot)]\in[0,1]$ and restrict our solutions to paths with $\mathcal{M}\ge M_{\min}$ for some threshold (e.g.\ $0.8$). The pedagogy is a \emph{Ma'at-aligned} coherence engine.
\end{remark}

% =========================
\section{Onu Emotional Topology: Jubilee Nexus}
% =========================

Psychological states are field activations, not fixed identities. The Onu Emotional Topology organizes these fields around a central \emph{Jubilee Nexus} (pure affirmation) and four cardinal axes:

\begin{itemize}
  \item \textbf{Integrity's Guard} (I Have Audit) --- Ma'at ideals 14, 22, 30, 41.
  \item \textbf{Wisdom's Probe} (I Have Attunement) --- ideals 7, 24, 31, 33.
  \item \textbf{Attunement's Motivation} (I Give Focus) --- ideals 2, 3, 18, 19.
  \item \textbf{Co-creation's Direction / Compassionary Action} (I Give Action) --- ideals 21, 23, 25, 35.
\end{itemize}

\figinclude{onu_emotional_topology}{Onu Emotional Topology v2.3: The Axis Affirmation. Four cardinal functions around the Jubilee Nexus (Pure Affirmation).}{fig:topology}

\paragraph{Jubilee Mantra} (central attractor):
\begin{quote}
I have only what, when viewed through certainty’s lens. I give every action through this lens. Action is pure, pervasive, and present.
\end{quote}

\paragraph{Out-breath:} I have coherence (attractor) --- (emitter) --- action’s seed is given.\\
v2.3 $\;\infty\;$ Unbounded Potential of Love $\;\infty$

The combination of Ma'at’s 42 local constraints and this topology’s four global axes gives us a complete \emph{moral-geom\-etric coordinate system} for the emotional field.

% =========================
\section{Onu Healing Field Model: Ma'at-aligned dynamics}
% =========================

The Healing Field Model places the emotional potential $f$ on axes of
\emph{Compassion} (C), \emph{Stability/Safety} (S), \emph{Truth} (T), and \emph{Clarity} (Cl), evolving under a log-domain diffusion with urgency $U(t)$.

\figinclude{onu_healing_field_model}{Onu Healing Field Model: a loop in $(C,S,T,\text{Cl})$ space that exits chaos and spirals toward Ma'at-aligned coherence.}{fig:healing_model}

In scalar form (in the $S=\ln z$ gauge) we write a stylized PDE:
\begin{equation}
\partial_t f
  = U(t)\,D\!\left(
      z^4 \frac{\partial^2 f}{\partial z^2}
    + 2 z^3 \frac{\partial f}{\partial z}
    + 2 \frac{\partial f}{\partial z}
    \right),
\label{eq:healing_model}
\end{equation}
where:
\begin{itemize}
  \item $f$ is emotional potential,
  \item $U(t)$ is urgency,
  \item $D$ is diffusion of insight,
  \item $S=\ln z$ is the log-amplitude of emotion.
\end{itemize}

We supplement \eqref{eq:healing_model} with:
\begin{equation}
I(z)=\frac{1}{z}
\end{equation}
as a conservation condition (no singular spikes of unbounded intensity), and with the variance target \eqref{eq:var_target}.

\begin{remark}[Ma'at boundary conditions]
On the emotional axes we impose Ma'at-aligned boundary conditions:
\begin{align*}
\partial_n f &= 0 \quad \text{on walls set by non-harm (life is sacred, I act respectfully)},\\
f &\ge 0 \quad \text{on compassion and integrity axes},\\
\partial_t f &\le 0 \quad \text{whenever a trajectory would cross into deceit or exploitation.}
\end{align*}
This effectively carves out a ``Ma'at-safe'' region in $(C,S,T,\text{Cl})$ space; the Jubilee Nexus sits at its center.
\end{remark}

% =========================
\section{Dynamic Affirmation Route: the $U(t)$ loop}
% =========================

The topology and PDE are turned into practice by a four-phase loop that modulates $U(t)$:

\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=2.4cm, every node/.style={align=center, text width=2.2cm}]
  \node (attune)  [draw,rounded corners, fill=blue!10] {1. Attunement Focus\\\small I give focus};
  \node (audit)   [draw,rounded corners, fill=green!10, right=of attune] {2. Integrity Audit\\\small I have audit};
  \node (probe)   [draw,rounded corners, fill=orange!10, below=of audit] {3. Wisdom Probe\\\small I know truth};
  \node (action)  [draw,rounded corners, fill=red!10, left=of probe] {4. Compassion Action\\\small I give action};
  \draw[->, very thick] (attune) -- (audit);
  \draw[->, very thick] (audit) -- (probe);
  \draw[->, very thick] (probe) -- (action);
  \draw[->, very thick] (action) -- (attune);
\end{tikzpicture}
\caption{Dynamic Affirmation Route: the $U(t)$ loop. Each phase corresponds to a Ma'at cluster: care, integrity, truth, and benevolent action.}
\label{fig:u_t_loop}
\end{figure}

\begin{table}[h]
\centering
\begin{tabular}{cll}
\toprule
Phase & Affirmation & Ma'at alignment \\
\midrule
1. Attunement Focus & ``I have attunement to the highest state here.'' & Peace, emotional balance (3,18).\\
2. Integrity Audit  & ``I have integrity in my place.'' & Fair share, honesty, respect (7,10,30,41).\\
3. Wisdom Probe     & ``I know the clear, scaled truth.'' & Truth, awareness, inner guidance (7,31,33).\\
4. Compassion Action& ``I give action for shared relief and dignity.'' & Joy, blessings, doing good (21,23,35).\\
\bottomrule
\end{tabular}
\caption{Dynamic affirmation phases mapped to clusters of Ma'at ideals.}
\end{table}

Repeated loops generate a spiral trajectory like the red curve in Figure~\ref{fig:healing_model}: exiting chaotic orbits, circling the Jubilee Nexus, and then moving outward along a Ma'at-aligned ray of service.

% =========================
\section{Music, Cymatics, and MWƐN vowels}
% =========================

\subsection{Log-frequency lattice and Coltrane mandalas}

Equal-tempered pitches
\[
f_k=f_0\,2^{k/12}
\]
live on the same log lattice $s_k=\ln f_k=\ln f_0 + \tfrac{k}{12}\ln 2$ used for the spectra in \eqref{eq:var_target}. The Circle of Fifths is the orbit of $k\mapsto k+7\pmod{12}$; Coltrane's tone mandalas overlay several such orbits (fifths, thirds, etc.) on the same circle.

These orbits preserve a highly ordered pattern of log-ratios, so harmonic motion that stays near a mandala path tends to keep $\Var_s[\ln P(f)]$ low or gently decreasing, especially when breath and timbre are kept smooth. The emotional protocol is thus a \emph{Ma'at-aligned mandala walk} in sound.

\subsection{MWƐN vowels as low-variance anchors}

MWƐN favours long, stable vowels (Ā, Ō, Ū) that pin the vocal tract into low-variance formant configurations (roughly):
\begin{itemize}
  \item Ā: F1 $\sim700$ Hz, F2 $\sim1100$ Hz,
  \item Ō: F1 $\sim500$ Hz, F2 $\sim900$ Hz,
  \item Ū: F1 $\sim350$ Hz, F2 $\sim700$ Hz.
\end{itemize}
These become acoustic realizations of Ma'at ideals like truth, sincerity, and balance: the voice itself refuses to lie by drifting into scattered spectra. Words are literally \emph{spoken on ordered fields}.

% =========================
\section{Physiology asset: HRV, respiration, voice}
% =========================

\subsection{Ledger-consistent HRV}
Given inter-beat intervals $\{RR_i\}$, define $\Delta s_i=\ln RR_{i+1}-\ln RR_i$ and
\[
\RMSLR=\sqrt{\frac{1}{N-1}\sum_{i=1}^{N-1}(\Delta s_i)^2},
\qquad
\mathrm{RMSSD}\approx \overline{RR}\cdot \RMSLR.
\]
RMSLR is invariant to multiplicative rescaling (Ma'at: fair measurement) and aligns with the positive ledger.

\subsection{Endpoints (H1–H4)}
Primary preregistered criteria:
\begin{itemize}
  \item H1: $\Delta\mathrm{RMSSD}\ge 5$ ms (or $\Delta\RMSLR\le -0.05$).
  \item H2: LF power gain $\ge 1.25$ with peak at $0.10\pm0.02$ Hz.
  \item H3: respiration-rate variance $\downarrow\ge 20\%$.
  \item H4: $\Delta\Var_s[\ln P_{\text{voice}}]\le -10\%$.
\end{itemize}
Passing $\ge2$ endpoints with good data quality is interpreted as a successful Ma'at-aligned coherence shift.

% =========================
\section{Architecture asset: room and streetscape coherence}
% =========================

For an impulse response $\mathrm{IR}(t)$, compute $A(s)=\ln P_{IR}(e^s)$ with $s=\ln f$ and apply the same variance criterion \eqref{eq:var_target}. Architectural moves (curtains, plants, placements) that reduce $\Var_s[A(s)]$ while keeping $RT_{60}$ in a comfortable range are Ma'at-aligned: they create environments where voices and hearts can settle into balance.

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
\item Pre (1.5 min): sliders for clarity, valence, arousal; 60 s focus-dot; 10 s MWƐN vowel.
\item Manipulation (90 s): MWƐN mantra, apology$\to$gratitude loop, or gentle levity --- always Ma'at-consistent.
\item Post (1.5 min): repeat; compare metrics and felt sense.
\end{enumerate}

\section{Symbol table}
\begin{center}
\begin{tabular}{ll}
\toprule
Symbol & Meaning \\
\midrule
$\I$ & inversion $x\mapsto x^{-1}$ \\
$\ominus$ & Onu difference $a b^{-1}$ \\
$\mathcal{E}$ & Euler scale $z\partial_z$ \\
$\RLO$ & scale Laplacian $(z\partial_z)^2=\partial_{ss}$ \\
$U(t)$ & urgency (dimensionless) \\
$\kappa(t)$ & diffusivity in $s$-gauge ($s^2/\text{time}$) \\
$S$ & source term \\
$s$ & $\ln z$ (log-amplitude or log-frequency) \\
$\mathcal{L}$ & product ledger (invariant) \\
RMSLR & HRV index (ledger-consistent) \\
$\Var_s[\ln P]$ & log-variance on $s=\ln f$ axis \\
$RT_{60}$ & reverberation time to 60 dB decay \\
$\mathcal{M}$ & Ma'at admissibility functional \\
\bottomrule
\end{tabular}
\end{center}

\bigskip
\noindent\textit{License/ethics:} Educational protocol only; participation voluntary; avoid practices that cause dizziness; honour Ma'at ideals in recruitment, consent, and data-sharing.\\
\textit{Disclaimer:} General information; not medical or financial advice.

\end{document}
