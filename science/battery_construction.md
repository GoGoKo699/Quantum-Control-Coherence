# A finite battery for arbitrary active energy gaps

Fix a finite-dimensional system Hamiltonian $`H=\sum_E E\Pi_E`$ and a target unitary $`U`$. The implementation is a unitary $`V`$ on the system and a battery, with $`[V,H+H_B]=0`$. Its induced channel is

```math
\mathcal E_\beta(\rho)=\operatorname{Tr}_B V(\rho\otimes\beta)V^\dagger.
```

This construction supplies a finite battery with nonnegative energies. It implements every fixed $`H,U`$ with both worst-case reference-assisted infidelity and diamond distance of order $`L^{-2}`$, using $`O_{H,U}(L^{r_U})`$ battery levels and mean energy $`O_{H,U}(L)`$. Constants may depend on the fixed gate and spectrum. All logarithms are base two.

The conserving shift construction follows the reference-frame approach developed in [Åberg (2014)](../references/RELATED_WORK.md#aberg2014) and the finite battery methods of [Chiribella, Yang, and Renner (2021)](../references/RELATED_WORK.md#chiribella2021). Finite reference systems for arbitrary finite spectra already exist by [Popescu et al. (2018)](../references/RELATED_WORK.md#popescu2018). The construction here realizes the matching entropy and dimension exponents on the gate's active transition lattice, including boundaries and degenerate system energies. The arbitrary-spectrum resource question is discussed by [Castellano et al. (2026)](../references/RELATED_WORK.md#castellano2026).

## Statement

Define the active transition group and its rank by

```math
\Gamma_U=\operatorname{span}_{\mathbb Z}
\{E-F:\Pi_EU\Pi_F\ne0\},
\qquad r=r_U=\operatorname{rank}_{\mathbb Z}\Gamma_U.
```

There are fixed, finite nonnegative constants $`A_{\mathrm{iso}},B_{\mathrm{ch}}`$ and an integer $`K\ge0`$ such that, for each integer $`L\ge1`$, a finite pure battery and a conserving unitary satisfy

```math
\begin{aligned}
\epsilon_F(\mathcal E_L,\mathcal U)
&\le \min\left\{1,\frac{A_{\mathrm{iso}}^2}{(L+1)^2}\right\},\\
\frac12\|\mathcal E_L-\mathcal U\|_\diamond
&\le \min\left\{1,\frac{B_{\mathrm{ch}}}{2(L+1)^2}\right\},\\
C(\beta_L,H_B)&\le r\log L,\\
d_B&=(L+2K+2)^r.
\end{aligned}
```

Here $`\epsilon_F`$ uses **squared** Uhlmann fidelity and allows an arbitrary reference. The coherence is $`C(\beta,H_B)=D(\beta\Vert\Delta_{H_B}\beta)`$. The constants are given explicitly below. For $`r=0`$, the battery can instead be one dimensional, with zero energy and coherence and exact implementation for every error tolerance.

## 1. Integer coordinates for the transitions

The group $`\Gamma_U`$ is a finitely generated torsion-free abelian subgroup of the real numbers. Choose a $`\mathbb Z`$-basis $`\omega_1,\ldots,\omega_r`$. Its entries are rationally independent. Change individual basis signs, if necessary, so that each $`\omega_a>0`$.

Form the undirected graph whose vertices are distinct system energies and whose edges connect $`E,F`$ whenever either $`\Pi_EU\Pi_F`$ or $`\Pi_FU\Pi_E`$ is nonzero. Every connected component $`c`$ determines a subspace preserved by $`U`$. Choose one energy $`E_c`$ in each component. A path in the graph shows that every energy in that component has a unique representation

```math
E=E_c+s_E\cdot\omega,\qquad s_E\in\mathbb Z^r.
```

Choose any orthonormal basis inside each energy eigenspace. For a basis index $`i`$, write $`s_i=s_{E_i}`$. This construction does not depend on a choice of basis inside a degenerate eigenspace. In particular, nonzero matrix elements of $`U`$ connect indices in the same component.

For $`r>0`$, set

```math
K=\max_c\ \max_{i,j\in c}\|s_i-s_j\|_\infty,
\qquad v_{ij}=s_j-s_i.
```

The maximum includes all pairs in a component, not only pairs for which $`U_{ij}\ne0`$. This is what makes the subsequent energy blocks complete.

If $`r=0`$, every active transition has zero energy. Hence $`[U,H]=0`$, and $`V=U`$ with a trivial battery proves the statement. The rest of the proof assumes $`r>0`$.

## 2. Battery Hamiltonian and reference state

Let the battery basis be indexed by the finite box

```math
\Omega_L=\{0,1,\ldots,L+2K+1\}^r,
\qquad H_B|k\rangle=(k\cdot\omega)|k\rangle.
```

The Hamiltonian is nonnegative and nondegenerate. Nondegeneracy follows from rational independence: two lattice points with equal energy must be identical.

Use the product sine packet

```math
|b_L\rangle=
\bigotimes_{a=1}^{r}
\left[
\sqrt{\frac{2}{L+1}}
\sum_{n=1}^{L}
\sin\frac{\pi n}{L+1}\,|K+n\rangle
\right],
\qquad \beta_L=|b_L\rangle\langle b_L|.
```

Its support is the interior box $`\{K+1,\ldots,K+L\}^r`$. If

```math
p_L(n)=\frac{2}{L+1}\sin^2\frac{\pi n}{L+1},
```

then its coherence, dimension, and mean energy are

```math
\begin{aligned}
C(\beta_L,H_B)&=rH(p_L)\le r\log L,\\
d_B&=(L+2K+2)^r,\\
\operatorname{Tr}(\beta_LH_B)
&=\left(K+\frac{L+1}{2}\right)\sum_{a=1}^{r}\omega_a.
\end{aligned}
```

The mean follows from the reflection symmetry $`p_L(n)=p_L(L+1-n)`$. These are exact finite-size expressions. The entropy is the entropy of the **total battery energy**, not a sum imposed by local dephasing. It equals the product distribution entropy here because the total energies are nondegenerate.

## 3. A global unitary, including the boundary

For a component $`c`$ and integer vector $`q`$, define

```math
\mathcal K_{c,q}
=\operatorname{span}\{
|i,q-s_i\rangle:
i\in c,\ q-s_i\in\Omega_L
\}.
```

These subspaces partition the entire system-battery basis: each $`|i,k\rangle`$ belongs to exactly the subspace with its component $`c`$ and $`q=k+s_i`$. Every vector in $`\mathcal K_{c,q}`$ has total energy

```math
E_i+(q-s_i)\cdot\omega=E_c+q\cdot\omega.
```

Different pairs $`(c,q)`$ can have the same physical total energy. This does not cause a problem: they are orthogonal subspaces of that energy eigenspace, and a direct sum of unitaries on them still conserves energy.

Call a block complete if it contains one battery-compatible basis vector for every system index in $`c`$. On every complete block, apply the unitary $`U|_c`$ in the basis indexed by $`i\in c`$:

```math
V|j,k\rangle
=\sum_{i\in c}U_{ij}|i,k+s_j-s_i\rangle.
```

On every incomplete block, let $`V`$ act as the identity. This defines a unitary on the whole finite Hilbert space. Each block has constant total energy, so $`[V,H+H_B]=0`$ exactly.

Every block reached from the initial battery support is complete. Indeed, if $`k_a\in\{K+1,\ldots,K+L\}`$, then for any $`i,j\in c`$,

```math
1\le k_a+(s_j-s_i)_a\le L+2K.
```

Thus all required shifted battery points lie in $`\Omega_L`$. The shift formula holds for every input state in the implementation, including system states entangled with a reference or in superpositions of different components. No finite-dimensional translation operator is assumed to be globally unitary. Only the blockwise operator $`V`$ is used physically.

## 4. Translation estimates for the packet

For the following estimates only, extend $`|b_L\rangle`$ by zero into $`\ell^2(\mathbb Z^r)`$, where bilateral lattice translations $`T^v`$ are well defined. All translations used by the physical implementation remain inside the padded finite box.

The one-coordinate overlap is

```math
\langle b_L|T^{e_a}|b_L\rangle
=\cos\frac{\pi}{L+1}.
```

Consequently

```math
\|(T^{e_a}-I)b_L\|
=\sqrt{2-2\cos\frac{\pi}{L+1}}
\le\frac{\pi}{L+1}.
```

Telescoping a translation, including negative coordinate steps, gives for every integer vector $`v`$

```math
\|(T^v-I)b_L\|
\le\frac{\pi\|v\|_1}{L+1}.
```

The amplitudes are real. Therefore the overlap kernel

```math
g_v=\langle b_L|T^v|b_L\rangle
```

is real, satisfies $`g_v=g_{-v}`$, and obeys

```math
0\le1-g_v
=\frac12\|(T^v-I)b_L\|^2
\le\frac{\pi^2\|v\|_1^2}{2(L+1)^2}.
```

## 5. Reference-assisted infidelity

Let $`W_L=V(I\otimes|b_L\rangle)`$ be the actual isometry from the system to system and battery, and let $`W_0=U\otimes|b_L\rangle`$. On the relevant input space,

```math
W_L-W_0
=\sum_{ij}U_{ij}|i\rangle\langle j|
\otimes(T^{v_{ij}}-I)|b_L\rangle.
```

Define

```math
A_{\mathrm{iso}}=\pi\sum_{ij}|U_{ij}|\|v_{ij}\|_1.
```

The triangle inequality gives

```math
\|W_L-W_0\|_\infty\le\eta_L,
\qquad \eta_L=\frac{A_{\mathrm{iso}}}{L+1}.
```

This operator norm is unchanged by tensoring with an arbitrary reference. For a pure input on system and reference, write $`|\Psi\rangle`$ and $`|\Phi\rangle`$ for the actual and ideal purified outputs. Their norm difference is at most $`\eta_L`$, so

```math
\operatorname{Re}\langle\Phi|\Psi\rangle
\ge1-\frac{\eta_L^2}{2}.
```

For $`\eta_L\le1`$, the squared overlap is at least $`1-\eta_L^2`$. For $`\eta_L>1`$, the corresponding infidelity bound is trivial. Tracing out the battery cannot decrease fidelity. Purifying a mixed input and then tracing out its extra reference proves the same statement for mixed inputs. Thus

```math
\epsilon_F(\mathcal E_L,\mathcal U)
\le\min\{1,\eta_L^2\}.
```

The squared-fidelity convention matters: the overlap argument produces the $`L^{-2}`$ infidelity without converting through diamond distance.

## 6. Diamond distance from the reduced channel

Tracing out the battery yields the exact coefficient formula

```math
\mathcal E_L(\rho)
=\sum_{ij,k\ell}
U_{ij}U^*_{k\ell}\rho_{j\ell}
g_{v_{ij}-v_{k\ell}}|i\rangle\langle k|.
```

The ideal channel has the same formula with every overlap replaced by one. Each elementary map $`X\mapsto|i\rangle\langle j|X|\ell\rangle\langle k|`$ has diamond norm one. Therefore

```math
\begin{aligned}
\|\mathcal E_L-\mathcal U\|_\diamond
&\le Q_L\\
&:=\sum_{ij,k\ell}|U_{ij}U_{k\ell}|
\left|1-g_{v_{ij}-v_{k\ell}}\right|\\
&\le\frac{B_{\mathrm{ch}}}{(L+1)^2},
\end{aligned}
```

where

```math
B_{\mathrm{ch}}=\frac{\pi^2}{2}
\sum_{ij,k\ell}|U_{ij}U_{k\ell}|
\|v_{ij}-v_{k\ell}\|_1^2.
```

This proof uses the real overlap kernel. The preceding isometry norm estimate by itself would only give an $`O(L^{-1})`$ diamond estimate. The half-diamond error is bounded by $`B_{\mathrm{ch}}/[2(L+1)^2]`$.

## 7. Resource consequences and limits

For worst-case infidelity at most $`\varepsilon`$, choose

```math
L_F=\max\left\{1,
\left\lceil A_{\mathrm{iso}}/\sqrt\varepsilon\right\rceil-1\right\}.
```

For half-diamond error at most the same numerical tolerance $`\varepsilon`$, choose

```math
L_\delta=\max\left\{1,
\left\lceil\sqrt{B_{\mathrm{ch}}/(2\varepsilon)}\right\rceil-1\right\}.
```

For either error metric $`e\in\{\epsilon_F,\delta\}`$, use the corresponding length $`L_e`$. This gives

```math
\begin{aligned}
C(\beta_{L_e},H_B)&\le\frac r2\log(1/\varepsilon)+O_{H,U}(1),\\
\log d_B&\le\frac r2\log(1/\varepsilon)+O_{H,U}(1),\\
\operatorname{Tr}(\beta_{L_e}H_B)&=O_{H,U}(\varepsilon^{-1/2}).
\end{aligned}
```

Combining these upper bounds with the entropy converse fixes the **leading exponent** of the minimum finite battery dimension:

```math
D_{\min}^{(e)}(\varepsilon)=\varepsilon^{-r/2+o(1)}.
```

The converse carries logarithmic corrections. It does not establish a matching constant-factor statement $`D_{\min}^{(e)}=\Theta(\varepsilon^{-r/2})`$. The energy upper bound is an achievable scaling, not a separate optimal-energy theorem.

The construction assumes exact conservation and a fixed exact spectrum. Rational approximants can require very large integer coordinates, padding, and constants. These formulas do not assert a uniform discontinuity at finite experimental accuracy, bounded preparation time, robustness to detuning, or a simultaneous large-system limit.

## Verification

The [verification suite](../verification/README.md) builds the full finite block unitary, including identity boundary blocks, and derives its Kraus channel. A separate implementation computes the overlap-kernel channel. It compares these objects for qubit, qutrit, spectator, degenerate, and disconnected-component examples, checks conservation with exact integer energy coordinates, and evaluates the finite bounds and resource formulas. These finite checks exercise the construction; the analytic arguments above establish its general validity.
