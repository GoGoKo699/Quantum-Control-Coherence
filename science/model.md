# The minimum coherence required for quantum control

A gate that mixes different system energies needs a controller carrying a phase reference. Exact conservation applies to the system and controller together. The question here is how much coherence that controller must initially contain when the gate has to work on every input, including one entangled with another system.

The answer depends on the energy transitions used by the gate. Their rational rank fixes both the leading entropic-coherence requirement and the power with which the minimum controller dimension grows as the error decreases. The result optimizes over finite controllers with arbitrary spectra and arbitrary mixed initial states.

## 1. System, gate, and implementation

Fix a finite-dimensional system $`S`$ of dimension $`d`$, a Hamiltonian

```math
H=\sum_{E\in\mathcal E} E\Pi_E,
```

and a target unitary $`U`$. The spectral projections $`\Pi_E`$ may have any multiplicity. The set $`\mathcal E`$ contains distinct eigenvalues. Set $`\hbar=1`$ and write $`\mathcal U(X)=UXU^\dagger`$.

An implementation consists of a finite battery $`B`$, a Hamiltonian $`H_B`$, a state $`\beta`$, and a unitary $`V`$ on $`SB`$ satisfying

```math
[V,H\otimes I_B+I_S\otimes H_B]=0.
```

The induced system channel is

```math
\mathcal E_\beta(X)
=\operatorname{Tr}_B\!\left[V(X\otimes\beta)V^\dagger\right].
```

The word battery denotes the auxiliary quantum controller in this model. Its energy coherences provide a phase reference as well as allowing energy exchange. The input is a product $`\rho_{SA}\otimes\beta_B`$; the battery is independent of the unknown system state and any external reference $`A`$. No initial return condition is imposed on the battery. A scalar shift of $`H_B`$ changes neither conservation nor coherence, so the optimization can require $`H_B\ge0`$ without loss.

The implementation unitary, battery Hamiltonian, and battery state may all depend on the fixed $`H,U`$ and on the error tolerance. Their time, gate complexity, preparation complexity, and energy are unrestricted in the optimization. The finite construction below additionally has a stated mean-energy bound.

## 2. Coherence and accuracy

Let $`P_b`$ be the projections onto the distinct battery energies. Energy dephasing and entropic energy coherence are

```math
\Delta_{H_B}(\beta)=\sum_b P_b\beta P_b,
\qquad
C(\beta,H_B)
=D\!\left(\beta\middle\|\Delta_{H_B}(\beta)\right)
=S(\Delta_{H_B}(\beta))-S(\beta).
```

All logarithms, entropies, and relative entropies use base two. Coherence inside one degenerate energy eigenspace does not contribute to $`C`$. The elementary dimension bound is

```math
0\le C(\beta,H_B)\le\log_2\dim B.
```

This is an initial resource requirement. It does not assert that one application consumes this amount. Relative-entropy asymmetry and its information interpretation are established notions; see [Gour, Marvian and Spekkens](../references/RELATED_WORK.md#gour2009). The energy-conserving gate model and the nearest entropic-coherence bounds are compared in [related work](../references/RELATED_WORK.md#castellano2026).

Use squared Uhlmann fidelity,

```math
F(\rho,\sigma)=\left\|\sqrt\rho\sqrt\sigma\right\|_1^2.
```

The reference-assisted worst-case infidelity and half-diamond error are

```math
\begin{aligned}
\epsilon_F(\mathcal E,\mathcal U)
&=1-\inf_{\rho_{SA}}
F\!\left((\mathcal E\otimes\operatorname{id}_A)(\rho_{SA}),
         (\mathcal U\otimes\operatorname{id}_A)(\rho_{SA})\right),\\
\delta(\mathcal E,\mathcal U)
&=\frac12\|\mathcal E-\mathcal U\|_\diamond.
\end{aligned}
```

A reference of dimension $`d`$ suffices, and pure extended inputs suffice for both optimizations. Purification and monotonicity of fidelity justify the first assertion about inputs. For a unitary target,

```math
\epsilon_F\le\delta\le\sqrt{\epsilon_F}.
```

The first inequality follows by projecting an output onto its ideal pure state; the second follows from the fidelity–trace-distance inequality. The equality of the two resource exponents below needs a stronger constructive estimate than these inequalities alone: the constructed reduced channel has $`\delta=O(L^{-2})`$, although its implementing isometry is only $`O(L^{-1})`$ from a product isometry.

## 3. The active transition rank

An energy gap is active when the corresponding gate block is nonzero. Define

```math
\Gamma_U
=\operatorname{span}_{\mathbb Z}
\{E-F:\Pi_EU\Pi_F\ne0\},
\qquad
r_U
=\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}\Gamma_U.
```

The integer span is a finitely generated torsion-free group. It has a basis of $`r_U`$ rationally independent real frequencies. In particular,

```math
0\le r_U\le |\mathcal E|-1\le d-1,
\qquad
r_U=0\ \Longleftrightarrow\ [H,U]=0.
```

This definition is independent of the basis chosen inside a degenerate eigenspace. A spectator level can increase the rank of the full energy spectrum without changing $`r_U`$. The [transition-rank account](transition_rank.md) derives the integer coordinates and the local geometry of the gate's time orbit.

## 4. Exact statement of the resource law

For either error measure $`e\in\{\epsilon_F,\delta\}`$, define separate optimizations

```math
\begin{aligned}
C_{\min}^{(e)}(\varepsilon)
&=\inf\{C(\beta,H_B): e(\mathcal E_\beta,\mathcal U)\le\varepsilon\},\\
D_{\min}^{(e)}(\varepsilon)
&=\min\{\dim B: e(\mathcal E_\beta,\mathcal U)\le\varepsilon\}.
\end{aligned}
```

Both range over all implementations in Section 1. The coherence optimum and dimension optimum are not assumed to have the same minimizer. The finite construction makes each feasible set nonempty for every positive tolerance.

### Theorem: optimal leading coherence and dimension

Fix $`H,U`$ and write $`r=r_U>0`$. There are constants $`a,b,c>0`$ and $`\varepsilon_0\in(0,1/2)`$, depending only on these fixed objects, such that for $`0<\varepsilon<\varepsilon_0`$ and $`\ell=\log_2(1/\varepsilon)`$,

```math
\frac r2\ell-\frac{3r}{2}\log_2\ell-a
\le C_{\min}^{(e)}(\varepsilon)
\le\frac r2\ell+b,
\qquad e\in\{\epsilon_F,\delta\},
```

and

```math
2^{-a}\varepsilon^{-r/2}\ell^{-3r/2}
\le D_{\min}^{(e)}(\varepsilon)
\le c\,\varepsilon^{-r/2}.
```

Consequently,

```math
\lim_{\varepsilon\downarrow0}
\frac{C_{\min}^{(e)}(\varepsilon)}{\log_2(1/\varepsilon)}
=
\lim_{\varepsilon\downarrow0}
\frac{\log_2 D_{\min}^{(e)}(\varepsilon)}{\log_2(1/\varepsilon)}
=\frac{r_U}{2}.
```

Equivalently, $`D_{\min}^{(e)}(\varepsilon)=\varepsilon^{-r_U/2+o(1)}`$. The result fixes the leading exponent; the stated lower and upper bounds retain a polylogarithmic gap. It does not claim $`D_{\min}=\Theta(\varepsilon^{-r_U/2})`$ or an additive constant remainder for the optimal coherence.

If $`r_U=0`$, use $`V=U`$ and a one-dimensional battery. Then both errors vanish, $`C_{\min}^{(e)}=0`$, and $`D_{\min}^{(e)}=1`$.

### Constructive energy bound

The same finite family realizing the upper bounds can have

```math
\operatorname{Tr}(H_B\beta)=O_{H,U}(\varepsilon^{-1/2}),
\qquad H_B\ge0.
```

This is an achieved mean-energy scaling for that family, with fixed energy units and spectrum-dependent constants. It is not an energy optimization theorem. The dimension exponent can depend on $`r_U`$ even though this energy exponent does not.

## 5. Proof route

The [converse](coherence_converse.md) begins with conservation. Inserting a time-translated battery into the same interaction implements the correspondingly conjugated target gate. The information recoverable from any finite ensemble of those battery states is bounded by the battery's entropic coherence. Known approximate recycling supplies many uses of the encoded gate, and known unitary estimation distinguishes a packing of the target orbit. Its dimension is $`r_U`$, giving the lower bound. The cited recycling and estimation theorems are imported ingredients, with their error conventions stated in that proof.

The [construction](battery_construction.md) uses a product of sine packets on an $`r_U`$-dimensional energy lattice. A margin around the packet makes every relevant total-energy sector complete. Applying $`U`$ on each complete sector and the identity on every incomplete sector gives a genuine finite unitary that conserves total energy. Its error is quadratic in the inverse packet width, while its entropy is logarithmic in the number of lattice points.

The dimension lower bound then follows from $`C\le\log_2\dim B`$ for every implementation. The explicit battery supplies the upper bound. This establishes a matching leading law without restricting the competitor batteries to the lattice construction.

## 6. Reading and scope

The [worked examples](examples.md) compare commensurate and irrational qutrit spectra, inactive spectator levels, degeneracies, and an exactly conserving gate. The [interpretation](interpretation.md) explains the phase information stored by the controller and the role of exact conservation. The [verification account](../verification/README.md) separates direct finite checks from the analytical theorem.

All asymptotic limits keep $`H,U,d`$ fixed. Exact spectral relations determine $`r_U`$, and the constants can change substantially near a rational relation or a vanishing gate matrix element. General continuous-spectrum batteries, approximate conservation, bounded control time, and simultaneous growing-dimension limits require different analysis. None is used to establish the finite-controller theorem above.
