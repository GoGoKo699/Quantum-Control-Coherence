# Active transitions and the gate's time orbit

The rank of the active energy transitions determines the dimension of the closure of a gate's time orbit. This section proves that statement, including degenerate system energies and the quotient by global phase, and constructs the finite packings used in the [coherence converse](coherence_converse.md).

We use the fixed finite-dimensional system and target unitary of the [model](model.md). Write $`d=\dim\mathcal H_S`$ and

```math
H=\sum_{E\in\mathcal E}E\Pi_E.
```

The set $`\mathcal E`$ contains the distinct energies; each $`\Pi_E`$ can have arbitrary finite rank.

## 1. The active transition group

Define

```math
\begin{aligned}
\mathcal S_U
&=\{E-F:\Pi_EU\Pi_F\ne0\},\\
\Gamma_U
&=\operatorname{span}_{\mathbb Z}\mathcal S_U,\\
r_U
&=\operatorname{rank}_{\mathbb Z}\Gamma_U
=\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}\mathcal S_U.
\end{aligned}
```

The group $`\Gamma_U`$ is a finitely generated subgroup of the additive real numbers. It is torsion free, so it is a free abelian group of finite rank. The definition uses spectral blocks and is therefore independent of a choice of basis inside a degenerate eigenspace.

### Proposition 1: elementary rank properties

If $`s=|\mathcal E|`$, then

```math
0\le r_U\le s-1\le d-1.
```

Moreover,

```math
r_U=0\quad\Longleftrightarrow\quad[H,U]=0.
```

**Proof.** Fix any $`E_0\in\mathcal E`$. Every active gap belongs to the rational span of the $`s-1`$ differences $`E-E_0`$, giving the upper bound. Rank zero means every active gap vanishes. Equivalently, all nonzero blocks $`\Pi_EU\Pi_F`$ have $`E=F`$, which is precisely the commutation condition. ∎

When $`r_U=0`$, the gate is implemented exactly by $`V=U`$ with a one-dimensional battery. The entropy and dimension requirements are respectively zero and one. The rest of this section assumes $`r=r_U\ge1`$.

Choose a group basis $`\omega_1,\ldots,\omega_r`$ of $`\Gamma_U`$. These real numbers are rationally independent, and every active gap has a unique integer coordinate vector:

```math
E-F=\boldsymbol v_{EF}\cdot\boldsymbol\omega,
\qquad
\boldsymbol v_{EF}\in\mathbb Z^r.
```

The active vectors $`\boldsymbol v_{EF}`$ generate the whole group $`\mathbb Z^r`$. In particular, they span $`\mathbb R^r`$ as a real vector space.

## 2. Integer coordinates on each active component

Make an undirected graph whose vertices are the distinct energies. Join $`E`$ and $`F`$ if either $`\Pi_EU\Pi_F`$ or $`\Pi_FU\Pi_E`$ is nonzero. A connected component $`c`$ defines

```math
P_c=\sum_{E\in c}\Pi_E.
```

There are no matrix blocks of $`U`$ between distinct components. Consequently,

```math
U=\bigoplus_c U_c,
```

where every restriction $`U_c`$ is unitary.

Choose a root energy $`E_c`$ in each component. Following a path of active edges shows that $`E-E_c\in\Gamma_U`$ for every $`E\in c`$. Thus there are unique vectors $`\boldsymbol s_E\in\mathbb Z^r`$ such that

```math
E=E_c+\boldsymbol s_E\cdot\boldsymbol\omega,
\qquad E\in c.
```

For every active block,

```math
\boldsymbol v_{EF}=\boldsymbol s_E-\boldsymbol s_F.
```

This componentwise construction also provides the integer coordinates used by the [finite battery construction](battery_construction.md). Energies in different components can have additional rational relations; those relations do not need to be included in $`\Gamma_U`$.

## 3. Closure of the actual time orbit

Let $`\mathbb T^r=(\mathbb R/2\pi\mathbb Z)^r`$ and define

```math
D_{\boldsymbol\phi}
=\sum_Ee^{-i\boldsymbol\phi\cdot\boldsymbol s_E}\Pi_E,
\qquad
U_{\boldsymbol\phi}
=D_{\boldsymbol\phi}UD_{\boldsymbol\phi}^{\dagger}.
```

The actual time-translated gate is

```math
U_t=e^{-itH}Ue^{itH}.
```

The root-energy phase is constant on each invariant component, so it cancels in the conjugation. Therefore

```math
U_t=U_{t\boldsymbol\omega\bmod 2\pi}.
```

### Lemma 2: density of actual times

The set $`\{t\boldsymbol\omega\bmod2\pi:t\ge0\}`$ is dense in $`\mathbb T^r`$.

**Proof.** For every nonzero $`\boldsymbol n\in\mathbb Z^r`$, rational independence gives $`\boldsymbol n\cdot\boldsymbol\omega\ne0`$. Hence

```math
\frac1T\int_0^T
e^{it\boldsymbol n\cdot\boldsymbol\omega}\,dt
\longrightarrow0.
```

The corresponding average is one for the constant character. By approximation with trigonometric polynomials, the time average of every continuous function on the torus converges to its normalized Haar integral. A nonnegative continuous function supported in a nonempty open set can have positive Haar integral, so the trajectory enters every such set. ∎

It follows that the closure of $`\{U_t:t\ge0\}`$ is exactly $`\{U_{\boldsymbol\phi}:\boldsymbol\phi\in\mathbb T^r\}`$. The density statement supplies actual times for every finite approximation used below. It supplies no uniform bound on those times.

## 4. Global phase leaves the orbit dimension unchanged

### Proposition 3: matrix and channel stabilizers

The matrix orbit has trivial stabilizer on $`\mathbb T^r`$. The stabilizer of the corresponding unitary-channel orbit has at most $`d`$ elements. Thus the channel orbit is an $`r`$-dimensional compact torus quotient.

**Proof.** If $`U_{\boldsymbol\phi}=U`$, every active block satisfies

```math
e^{-i\boldsymbol\phi\cdot\boldsymbol v_{EF}}=1.
```

Since these integer vectors generate $`\mathbb Z^r`$, each coordinate of $`\boldsymbol\phi`$ is a multiple of $`2\pi`$. This is the identity point of the torus.

Two unitaries define the same channel exactly when they differ by a global phase. If

```math
U_{\boldsymbol\phi}=zU,
\qquad |z|=1,
```

then equality of determinants gives $`z^d=1`$. For each such scalar $`z`$, there is at most one torus point: two points with the same scalar would differ by an element of the trivial matrix stabilizer. The projective stabilizer is therefore a finite subgroup of size at most $`d`$. Quotienting a torus by a finite subgroup preserves its dimension. ∎

For example, a qubit bit flip has $`r_U=1`$ even though a half-period shift can multiply the matrix by minus one. The global-phase identification changes a finite period, not the number of continuous phase coordinates.

## 5. A positive local Choi metric

Let $`|\Phi_d\rangle=d^{-1/2}\sum_{j=1}^d|j,j\rangle`$ and $`|U\rangle=(U\otimes I)|\Phi_d\rangle`$. Define the distance between unitary channels by

```math
d_{\mathrm{Ch}}(U,W)
=\sqrt{1-\left|\frac{\operatorname{Tr}(U^\dagger W)}d\right|^2}.
```

This is the trace distance between their normalized pure Choi states, so it obeys the triangle inequality and ignores global phase.

For active energy blocks set

```math
p_{EF}=\frac{\|\Pi_EU\Pi_F\|_{\mathrm{HS}}^2}{d}.
```

These numbers sum to one. Unitarity gives both marginal identities

```math
\sum_Fp_{EF}=\frac{\operatorname{rank}\Pi_E}{d},
\qquad
\sum_Ep_{EF}=\frac{\operatorname{rank}\Pi_F}{d}.
```

In particular, the active integer vector has mean zero:

```math
\sum_{E,F}p_{EF}\boldsymbol v_{EF}=0.
```

Its covariance matrix is

```math
\Sigma=\sum_{E,F}p_{EF}
\boldsymbol v_{EF}\boldsymbol v_{EF}^{\mathsf T}.
```

Every active block has positive weight, and the corresponding vectors span $`\mathbb R^r`$. Thus $`\Sigma`$ is positive definite.

The orbit's Choi overlap is its characteristic function:

```math
\frac{\operatorname{Tr}(U^\dagger U_{\boldsymbol\phi})}{d}
=\sum_{E,F}p_{EF}
e^{-i\boldsymbol\phi\cdot\boldsymbol v_{EF}}.
```

Writing $`\alpha,\beta`$ for active-block labels gives the exact expression

```math
d_{\mathrm{Ch}}(U,U_{\boldsymbol\phi})^2
=\sum_{\alpha,\beta}p_\alpha p_\beta
\left[1-\cos\!\left(
\boldsymbol\phi\cdot(\boldsymbol v_\alpha-\boldsymbol v_\beta)
\right)\right].
```

Consequently,

```math
d_{\mathrm{Ch}}(U,U_{\boldsymbol\phi})^2
=\boldsymbol\phi^{\mathsf T}\Sigma\boldsymbol\phi
+O(\|\boldsymbol\phi\|_2^4).
```

For a quantitative version, put

```math
R=\max_\alpha\|\boldsymbol v_\alpha\|_2,
\qquad
\mu=\sqrt{\frac{\lambda_{\min}(\Sigma)}2}.
```

Both are positive. If $`\|\boldsymbol\phi\|_2\le1/(2R)`$, every cosine argument has magnitude at most one. The bounds $`x^2/4\le1-\cos x\le x^2/2`$ on that interval imply

```math
\mu\|\boldsymbol\phi\|_2
\le d_{\mathrm{Ch}}(U,U_{\boldsymbol\phi})
\le\sqrt{\lambda_{\max}(\Sigma)}\,\|\boldsymbol\phi\|_2.
```

Here we used

```math
\sum_{\alpha,\beta}p_\alpha p_\beta
\left[\boldsymbol\phi\cdot
(\boldsymbol v_\alpha-\boldsymbol v_\beta)\right]^2
=2\boldsymbol\phi^{\mathsf T}\Sigma\boldsymbol\phi.
```

The same estimates apply to two points of a sufficiently small coordinate patch because

```math
d_{\mathrm{Ch}}(U_{\boldsymbol\phi},U_{\boldsymbol\psi})
=d_{\mathrm{Ch}}(U,U_{\boldsymbol\psi-\boldsymbol\phi}).
```

## 6. Finite packings using actual times

### Theorem 4: quantitative packing

For fixed $`H,U`$ with $`r_U=r\ge1`$, define

```math
b=\frac1{4R\sqrt r},
\qquad
\eta_0=\frac{\mu b}{4},
\qquad
c_{\mathrm{pack}}=\left(\frac{\mu b}{2}\right)^r.
```

For every $`0<\eta\le\eta_0`$, there are finitely many actual times $`t_1,\ldots,t_M\ge0`$ satisfying

```math
\begin{aligned}
d_{\mathrm{Ch}}(U_{t_j},U_{t_k})&\ge\eta
&&\text{for }j\ne k,\\
M&\ge c_{\mathrm{pack}}\eta^{-r}.
\end{aligned}
```

The constants depend only on the fixed gate and Hamiltonian, through the chosen integer coordinates.

They also satisfy $`0<c_{\mathrm{pack}}<1`$: indeed, $`\lambda_{\min}(\Sigma)\le\operatorname{Tr}\Sigma\le R^2`$, and hence $`\mu b/2\le1/(8\sqrt{2r})<1`$.

**Proof.** In the cube $`[0,b]^r`$, place a rectangular grid with coordinate spacing $`h=2\eta/\mu`$. The assumption on $`\eta`$ ensures $`h\le b/2`$. Differences between cube points have norm at most $`b\sqrt r=1/(4R)`$, so the local metric bound applies. Two grid points are at Choi distance at least $`\mu h=2\eta`$.

The number of grid points is

```math
M=\left(\left\lfloor\frac bh\right\rfloor+1\right)^r
\ge\left(\frac{\mu b}{2\eta}\right)^r.
```

By Lemma 2 and continuity, choose an actual time for each grid point whose gate is at Choi distance less than $`\eta/4`$ from that point. The triangle inequality leaves pairwise distance greater than $`3\eta/2`$, and hence at least $`\eta`$. The cardinality is unchanged. ∎

The proof requires neither a torus action on the battery nor a bound on the battery's rational spectral rank. Only the system's gate orbit is packed. The battery programs used in the converse are the corresponding actual time translates.

## 7. Active rank and spectators

For $`H=\operatorname{diag}(0,1,\sqrt2)`$, a nontrivial rotation confined to the first two energies has $`r_U=1`$. A fully supported qutrit Fourier gate has $`r_U=2`$. With $`H=\operatorname{diag}(0,1,2)`$, that Fourier gate instead has $`r_U=1`$.

These are statements about a fixed exact spectrum and a fixed gate. Their asymptotic resource consequences follow from the converse and construction. Neither the packing constants nor the required actual times are asserted to be uniform as a rational relation or an active matrix block changes.
