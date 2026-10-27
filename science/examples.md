# Which energy gaps does a gate use?

The rank in the [resource theorem](model.md#4-exact-statement-of-the-resource-law) belongs to the pair $`(H,U)`$. These examples make it computable before building a controller. They also separate the number of system levels, the number of active frequencies, and the dimension of a sufficient finite battery.

In every example, energies are in fixed units and the matrices are expressed in an energy eigenbasis. The claimed minimum dimension is an asymptotic exponent as the error $`\varepsilon`$ tends to zero. The displayed finite dimensions describe the construction, not exact finite-error minima.

## 1. A qubit rotation uses one frequency

Take

```math
H=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\qquad
U_{\mathrm H}=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
```

The active gaps are $`0,1,-1`$. Their integer span is $`\mathbb Z`$, so $`r_U=1`$. A controller implementing this fixed Hadamard gate must obey

```math
C_{\min}^{(e)}(\varepsilon)
=\frac12\log_2(1/\varepsilon)
+O(\log\log(1/\varepsilon)),
\qquad
D_{\min}^{(e)}(\varepsilon)=\varepsilon^{-1/2+o(1)}.
```

For the [finite construction](battery_construction.md), choose integer charges $`s_0=0,s_1=1`$ and margin $`K=1`$. A length-$`L`$ sine packet sits on battery energies $`2,\ldots,L+1`$ inside the full ladder $`0,\ldots,L+3`$. The full battery dimension is $`L+4`$, and its mean energy is $`1+(L+1)/2`$.

In a complete total-energy sector with label $`q`$, the two states $`|0,q\rangle`$ and $`|1,q-1\rangle`$ have the same energy. The implementation applies the Hadamard matrix to this pair. It acts as the identity on an incomplete edge sector. The packet margin ensures that an arbitrary system input reaches only complete sectors.

This exponent agrees with established qubit results. The contribution of the general theorem is its extension to arbitrary fixed spectra and mixed finite competitors; see the [closest-work comparison](../references/RELATED_WORK.md#castellano2026).

## 2. Two three-level spectra give different controller exponents

Use the same fully supported Fourier gate in both cases:

```math
(F_3)_{jk}=\frac1{\sqrt3}\exp(2\pi i jk/3),
\qquad j,k\in\{0,1,2\}.
```

Since every entry is nonzero, all differences of the three energies are active.

| System spectrum | Active group | Rank | Leading minimum coherence | Minimum-dimension exponent |
|---|---|---:|---|---:|
| $`0,1,2`$ | $`\mathbb Z`$ | $`1`$ | $`\frac12\log_2(1/\varepsilon)`$ | $`1/2`$ |
| $`0,1,\sqrt2`$ | $`\mathbb Z+\sqrt2\mathbb Z`$ | $`2`$ | $`\log_2(1/\varepsilon)`$ | $`1`$ |

The coherence column gives the leading term; its controlled remainder is $`O(\log\log(1/\varepsilon))`$. The last column means $`D_{\min}=\varepsilon^{-\alpha+o(1)}`$.

For the equally spaced spectrum, take $`\omega=1`$ and charges $`s=(0,1,2)`$. The construction has $`K=2`$, dimension $`L+6`$, and mean energy $`2+(L+1)/2`$.

For the irrational spectrum, take

```math
\omega=(1,\sqrt2),
\qquad
s_0=(0,0),\quad s_1=(1,0),\quad s_2=(0,1).
```

The margin is $`K=1`$, the dimension is $`(L+4)^2`$, and the mean energy is

```math
\left(1+\frac{L+1}{2}\right)(1+\sqrt2).
```

Both reduced-channel errors are $`O(L^{-2})`$. The second controller stores two phase coordinates, giving a quadratic number of lattice states, even though its mean energy is still linear in $`L`$. This is a comparison of full finite-controller optima because the converse permits every mixed finite battery, not only these ladders and lattices.

## 3. An inactive level does not create a new requirement

Keep the irrational spectrum but replace the target:

```math
H=\operatorname{diag}(0,1,\sqrt2),
\qquad
U=U_{\mathrm H}\oplus1.
```

The gate mixes only the first two levels. Its active gaps are again $`0,1,-1`$, and $`r_U=1`$. The level of energy $`\sqrt2`$ is a separate component of the energy-support graph. It can be assigned component offset $`E_c=\sqrt2`$ and integer charge zero. A one-frequency battery therefore suffices.

The guarantee still applies to coherent superpositions involving the spectator. It is not a promise that the input stays in the two-level subspace. In the [construction proof](battery_construction.md), the same battery packet accompanies all components, so the error bound also controls cross-component coherences and entanglement with a reference.

The distinction is useful for selective gates. The rank of the whole spectrum would predict two coordinates here; the active transition group correctly predicts one.

## 4. Degeneracy is treated by spectral blocks

Let

```math
H=\operatorname{diag}(0,0,1,\sqrt2).
```

A unitary acting arbitrarily on the first two states and leaving the other levels unchanged commutes with $`H`$. It has $`r_U=0`$ and needs no battery coherence. The amplitudes inside the degenerate energy-zero space may be complex and fully mixed by the gate.

If the gate instead mixes one of those two zero-energy states with the energy-one state while leaving the other states unchanged, $`r_U=1`$. Changing the basis inside the zero-energy eigenspace changes matrix entries but cannot change whether $`\Pi_0U\Pi_1`$ is zero. The block definition therefore gives the same rank in every such basis.

Battery degeneracy also cannot supply missing phase information at zero cost. Time translation acts identically on all vectors with one battery energy. The [Holevo bound](coherence_converse.md) permits arbitrary degeneracy and counts exactly the information carried between different energies.

## 5. A finite projective stabilizer leaves the rank intact

For the qubit bit flip,

```math
H=\operatorname{diag}(0,1),\qquad
U=X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
```

the active gaps are $`1,-1`$. The conjugated gate is

```math
U_t=e^{-itH}Xe^{itH}
=\begin{pmatrix}0&e^{it}\\e^{-it}&0\end{pmatrix}.
```

Shifting $`t`$ by $`\pi`$ changes the matrix sign and hence leaves its channel unchanged. This finite identification does not reduce the local orbit dimension: $`r_U=1`$. Indeed,

```math
\frac12\operatorname{Tr}(X^\dagger U_t)=\cos t,
\qquad
d_{\mathrm{Ch}}(X,U_t)^2=\sin^2t.
```

The distance is linear in $`|t|`$ near zero. The converse needs a small local packing, so the finite global ambiguity has no effect on its exponent.

## 6. What the fixed-gate assumption does

The rank alone does not supply a uniform finite-error lower bound as a gate approaches an energy-preserving one. For

```math
U_\theta=e^{-i\theta X},\qquad H=\operatorname{diag}(0,1),
```

every fixed $`0<|\theta|<\pi/2`$ has rank one. However, implementing the identity gives

```math
\epsilon_F(\operatorname{id},\mathcal U_\theta)=\sin^2\theta,
\qquad
\delta(\operatorname{id},\mathcal U_\theta)=|\sin\theta|.
```

If the target angle is allowed to shrink with the error tolerance, a one-dimensional controller can already meet that tolerance. The theorem fixes $`\theta`$ before taking $`\varepsilon\downarrow0`$. The local packing constants record how strongly the gate responds to each phase coordinate.

Exact rational relations have a similar order-of-limits issue. For $`H=\operatorname{diag}(0,1,p/q)`$ with coprime positive integers $`p,q`$, a fully supported gate has rank one and may use lattice spacing $`1/q`$ with charges $`0,q,p`$. The required padding can grow with $`p,q`$. Taking rational approximants with increasing denominators while decreasing the error is a joint limit and is not described by a fixed-spectrum exponent alone.

## 7. Generic fixed systems

For a generic fixed nondegenerate $`d`$-level Hamiltonian, the $`d-1`$ gaps from one reference energy are rationally independent. A fully supported gate then has $`r_U=d-1`$, giving

```math
C_{\min}^{(e)}(\varepsilon)
=\frac{d-1}{2}\log_2(1/\varepsilon)
+O_{H,U}(\log\log(1/\varepsilon)),
\qquad
D_{\min}^{(e)}(\varepsilon)=\varepsilon^{-(d-1)/2+o(1)}.
```

Here generic excludes a countable union of rational-relation hyperplanes in the spectrum and zero-block conditions on the gate. The assertion concerns each such fixed pair. It does not make the constants uniform as $`d`$ increases.

The [verification suite](../verification/README.md) checks finite instances of these distinctions by constructing a global conserving unitary and comparing its reduced channel with the translation-overlap formula. Rational ranks are supplied by exact model definitions; floating-point eigenvalues are not used to decide rational independence.
