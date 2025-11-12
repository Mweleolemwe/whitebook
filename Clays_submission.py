\begin{theorem}[Ledgered local energy identity—Leray–Hopf ⇒ suitable]
Let $(v,p)$ be a Leray–Hopf weak solution of incompressible Navier–Stokes on a smooth domain $\Omega\subset\mathbb{R}^3$ over $(0,T)$, with viscosity $\nu>0$. Then there exists a nonnegative Radon measure $\mu$ on $\Omega\times(0,T)$ such that, in the sense of distributions,
\begin{equation}
\partial_t \Big(\tfrac12|v|^2\Big)
+ \nabla\!\cdot\!\Big[\Big(\tfrac12|v|^2+p\Big)v\Big]
= \nu\,\Delta\Big(\tfrac12|v|^2\Big) - \nu\,|\nabla v|^2 - \mu .
\label{eq:ledger}\tag{1}
\end{equation}
Equivalently, for every nonnegative $\varphi\in C_c^\infty(\Omega\times(0,T))$,
\begin{align}
\int\!\!\int \tfrac12|v|^2\,\partial_t\varphi
+ \Big(\tfrac12|v|^2+p\Big)v\!\cdot\!\nabla\varphi
+ \nu\,\tfrac12|v|^2\,\Delta\varphi
+ \nu\,|\nabla v|^2\,\varphi
+ \varphi\,\mathrm d\mu \;=\; 0 .
\label{eq:duality}\tag{2}
\end{align}
In particular, $(v,p)$ is a suitable weak solution; for smooth solutions $\mu\equiv 0$.
\end{theorem}

\begin{proof}[Proof sketch]
Let $\rho_\varepsilon$ be a spatial mollifier and set $v^\varepsilon=\rho_\varepsilon\!*v$. Testing the mollified equations with $v^\varepsilon\varphi$ yields an exact local balance with a commutator term $\mathcal C_\varepsilon[\varphi]$ from $(v\otimes v)^\varepsilon - v^\varepsilon\!\otimes v^\varepsilon$. All other terms converge as $\varepsilon\!\to\!0$; by compactness and lower semicontinuity, $\mathcal C_\varepsilon$ converges weak* to a nonnegative Radon measure $\mu$ (the Duchon–Robert defect). Passing to the limit gives \eqref{eq:duality}.
\end{proof}

\begin{remark}[Duchon–Robert coarse-grained form]
For smooth $v$, the defect density reads
\[
\mathcal D_\ell(x,t)=\frac{1}{4\ell}\int_{\mathbb R^3}
\big(|\delta_\ell v|^2\,\delta_\ell v\big)\cdot\nabla G_\ell \, \mathrm dx'
\quad\to\quad 0 \;\;\text{as }\ell\to 0,
\]
where $\delta_\ell v(x)=v(x+\ell)-v(x)$ and $G_\ell$ is a standard kernel. For weak solutions, $\mathcal D_\ell\rightharpoonup \mu\ge 0$.
\end{remark}

\paragraph{Caccioppoli with ledger (tool).}
For $\psi\in C_c^\infty(\Omega)$ and $0<t_1<t_2<T$,
\[
\int \tfrac12|v|^2\psi^2(\cdot,t_2)
+ \nu\!\int_{t_1}^{t_2}\!\!\int |\nabla v|^2\psi^2
\;\le\;
\int \tfrac12|v|^2\psi^2(\cdot,t_1)
+ \int_{t_1}^{t_2}\!\!\int \Big(|v|^2+2p\Big)v\cdot(\psi\nabla\psi)
+ \nu\!\int_{t_1}^{t_2}\!\!\int \tfrac12|v|^2\Delta(\psi^2)
- \int_{t_1}^{t_2}\!\!\int \psi^2\,\mathrm d\mu .
\]

\begin{theorem}[ε-regularity with ledger mass]
Let $Q_r(x_0,t_0)$ be a parabolic cylinder and set
\[
\mathcal E(r)=r^{-1}\!\int_{Q_r}\!\!\big(|v|^3+|p|^{3/2}\big),\qquad
\Lambda(r)=\mu\big(Q_r\big).
\]
There exists $\varepsilon_*>0$ such that
\[
\mathcal E(r_0)+\Lambda(r_0)\le \varepsilon_*
\quad\Longrightarrow\quad v \text{ is Hölder-regular in } Q_{r_0/2}(x_0,t_0).
\label{eq:ereg}\tag{3}
\]
\end{theorem}

\begin{proof}[Idea]
Run the Caffarelli–Kohn–Nirenberg blow-up/compactness scheme using the Caccioppoli inequality above; under the smallness of $\mathcal E(r_0)+\Lambda(r_0)$, every rescaled sequence has vanishing ledger mass and energy at the limit, forcing the ancient limit to be caloric (hence regular). Contradiction if the base point were singular.
\end{proof}
