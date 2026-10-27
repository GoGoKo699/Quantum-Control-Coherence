# Coherence converse for finite mixed batteries

This section proves the lower bound on the initial entropic coherence needed to implement a fixed unitary under exact energy conservation. The argument applies to every finite battery, including mixed states and degenerate Hamiltonians. Its constants depend on the fixed system Hamiltonian and target gate.

The [model](model.md) defines the implementation channel $`\mathcal E_\beta`$, the target $`\mathcal U(\rho)=U\rho U^\dagger`$, entropic coherence $`C(\beta,H_B)`$, reference-assisted infidelity $`\epsilon_F`$, and half-diamond distance $`\delta`$. All logarithms have base two. Throughout the proof assume

```math
\epsilon_F(\mathcal E_\beta,\mathcal U)\le\varepsilon.
```

For $`r=r_U\ge1`$, we obtain

```math
C(\beta,H_B)
\ge
\frac r2\log\frac1\varepsilon
-\frac{3r}{2}\log\log\frac1\varepsilon
-O_{H,U}(1).
```

The proof has three ingredients. Covariance makes the time-translated battery states programs for the gate's time orbit. A known recycling result lets one battery emulate several parallel uses of the programmed gate. A known estimation protocol distinguishes a sufficiently large finite packing of those gates. The resulting information must fit within the battery's entropic coherence.

The symmetry-to-programming perspective is due to [Marvian and Spekkens](../references/RELATED_WORK.md#marvian2012). The information bound associated with relative entropy of asymmetry is established by [Gour, Marvian and Spekkens](../references/RELATED_WORK.md#gour2009). We give the finite-ensemble calculation explicitly and credit the two quantitative imported results where they enter.

## 1. Covariance generates an orbit of programs

Write $`\mathcal T_t(\rho)=e^{-itH}\rho e^{itH}`$, and define

```math
\beta_t=e^{-itH_B}\beta e^{itH_B},
\qquad
U_t=e^{-itH}Ue^{itH}.
```

### Lemma 1: the same implementation processes every time translate

If $`[V,H\otimes I_B+I_S\otimes H_B]=0`$, then

```math
\mathcal E_{\beta_t}
=\mathcal T_t\circ\mathcal E_\beta\circ\mathcal T_{-t}.
```

Consequently,

```math
\epsilon_F(\mathcal E_{\beta_t},\mathcal U_t)
=\epsilon_F(\mathcal E_\beta,\mathcal U)
\le\varepsilon
```

for every real $`t`$. The corresponding half-diamond distances are equal as well.

**Proof.** Inserting $`e^{-it(H+H_B)}`$ and its inverse on either side of $`V`$, commuting them through $`V`$, and tracing out $`B`$ gives the channel identity. Fidelity and diamond distance are invariant under common unitary conjugation, while precomposition by $`\mathcal T_{-t}`$ simply permutes the input states over which the worst case is taken. ∎

The processor $`V`$ is fixed. All dependence on the unknown label $`t`$ is carried by the inserted battery state.

## 2. Orbit information is bounded by entropic coherence

### Lemma 2: finite-ensemble Holevo bound

Let $`t_1,\ldots,t_M`$ be arbitrary actual times and $`p_1,\ldots,p_M`$ any probability distribution. Then

```math
\chi(\{p_j,\beta_{t_j}\})
\le C(\beta,H_B).
```

**Proof.** Put $`\sigma=\Delta_{H_B}(\beta)`$ and $`\bar\beta=\sum_jp_j\beta_{t_j}`$. Since $`\sigma`$ commutes with $`H_B`$,

```math
D(\beta_{t_j}\Vert\sigma)=C(\beta,H_B)
```

for every $`j`$. Expanding the relative entropies gives the exact identity

```math
\begin{aligned}
C(\beta,H_B)
&=\sum_jp_jD(\beta_{t_j}\Vert\sigma)\\
&=\sum_jp_jD(\beta_{t_j}\Vert\bar\beta)
  +D(\bar\beta\Vert\sigma)\\
&=\chi(\{p_j,\beta_{t_j}\})
  +D(\bar\beta\Vert\sigma).
\end{aligned}
```

The last term is nonnegative. All states are finite dimensional, and the support of every $`\beta_{t_j}`$ is contained in the support of $`\sigma`$, so these expressions are well defined. ∎

This is the orbit-information interpretation of relative entropy of asymmetry applied to a finite ensemble; see [Gour, Marvian and Spekkens, Section III](https://arxiv.org/html/0901.0943v2). In particular, the ensemble need not uniformly sample a compact group. Every program in the proof is an actual time translate of the original mixed battery.

Any experiment acting on these programs with a fixed ancillary state and label-independent operations satisfies

```math
I(J;\widehat J)
\le\chi(\{p_j,\beta_{t_j}\})
\le C(\beta,H_B).
```

The decoder used below may perform arbitrary measurements. Its ancillary state and operations contain no information about $`J`$, so this data-processing statement needs no symmetry restriction on the decoder.

## 3. Imported quantitative ingredients

### Lemma 3: paired recycling

Let $`S_1,\ldots,S_{2m}`$ be copies of the system. Define the fixed unitary

```math
W_m=
V_{S_{2m}B}^{\dagger}V_{S_{2m-1}B}
\cdots
V_{S_2B}^{\dagger}V_{S_1B},
```

where the rightmost factor acts first. Let

```math
\mathcal R_{m,\beta}(\rho)
=W_m(\rho\otimes\beta)W_m^\dagger,
\qquad
\mathcal U_m^{\mathrm{pair}}
=\bigotimes_{k=1}^m
(\mathcal U_{S_{2k-1}}\otimes\mathcal U^\dagger_{S_{2k}}),
```

with $`\mathcal U^\dagger(\rho)=U^\dagger\rho U`$. Then

```math
\left\|
\mathcal R_{m,\beta}
-
\bigl(\mathcal U_m^{\mathrm{pair}}(\,\cdot\,)\otimes\beta\bigr)
\right\|_\diamond
\le8m\sqrt{\varepsilon}.
```

This is [Castellano et al., Theorem 9, Eq. (60), version 2](https://arxiv.org/html/2509.01515v2), which attributes the recycling result to [Chiribella, Yang and Renner](../references/RELATED_WORK.md#chiribella2021). The hypothesis is the reference-assisted squared-fidelity infidelity defined in the model. The stated bound is for the **full diamond norm** and includes the final battery.

The statement allows mixed $`\beta`$ and does not require the original single-use implementation to return it. The inverse $`V^\dagger`$ also conserves total energy. For every $`\beta_t`$, the same $`W_m`$ obeys the bound with target $`(\mathcal U_t\otimes\mathcal U_t^\dagger)^{\otimes m}`$, by Lemma 1.

Preparing fixed states on the even registers and tracing them and the battery out leaves an emulation of $`m`$ parallel uses of $`\mathcal U_t`$. For every possibly entangled probe on the odd registers and a reference, its actual and ideal output states are at trace distance at most

```math
4m\sqrt{\varepsilon}.
```

### Lemma 4: parallel unitary estimation

For $`d\ge2`$, define

```math
m_0=2d(d-1),
\qquad
K_d=
2\left[
\frac{\pi(d-1)^2(3d-2)}{d}
\right]^2.
```

For every integer $`m\ge m_0`$, there is a fixed probe and measurement using $`m`$ parallel instances of an unknown unitary $`W`$ such that the estimate $`\widehat W`$ satisfies, uniformly in $`W`$,

```math
\mathbb E_W\!\left[
d_{\mathrm{Ch}}(W,\widehat W)^2
\right]\le\frac{K_d}{m^2}.
```

The required estimation protocol is given by [Yang, Renner and Chiribella, Theorem 2 and Appendix B](https://arxiv.org/html/2007.10363v3). Their Eq. (5) bounds the half-diamond error of the associated measure-and-operate channel by $`K_d/m^2`$.

To obtain the displayed risk bound, let $`p(d\widehat W\mid W)`$ be the estimator's outcome law and set

```math
\mathcal M_W=\int
p(d\widehat W\mid W)\,\widehat{\mathcal W}.
```

The normalized ideal Choi state $`|W\rangle\langle W|`$ is pure. Testing the actual Choi state with its projector yields

```math
\begin{aligned}
\mathbb E_W[d_{\mathrm{Ch}}(W,\widehat W)^2]
&=1-\langle W|
(\mathcal M_W\otimes\operatorname{id})
(|\Phi_d\rangle\langle\Phi_d|)
|W\rangle\\
&\le\frac12\|\mathcal M_W-\mathcal W\|_\diamond\\
&\le\frac{K_d}{m^2}.
\end{aligned}
```

The source works with $`\mathrm{SU}(d)`$. Choosing a special-unitary representative of $`W`$ changes neither its channel, the Choi distance, nor the estimator's outcome law. The probe and measurement are independent of the unknown gate.

## 4. A finite packing can be decoded from one battery

Use $`c_{\mathrm{pack}}`$ and $`\eta_0`$ from Theorem 4 of [Transition rank](transition_rank.md). These positive constants depend only on $`H,U`$.

Fix an integer $`m\ge m_0`$ and a real $`a>0`$ such that

```math
\frac am\le\eta_0.
```

The packing theorem supplies actual times $`t_1,\ldots,t_M`$ with

```math
d_{\mathrm{Ch}}(U_{t_j},U_{t_k})\ge\frac am
\quad(j\ne k),
\qquad
M\ge c_{\mathrm{pack}}\left(\frac ma\right)^r.
```

Choose a uniformly distributed label $`J`$ and insert $`\beta_{t_J}`$. Prepare the probe of Lemma 4 on the odd registers, fixed auxiliary inputs on the even registers, and apply the paired recycler. Measure the odd outputs and the estimator's reference, then assign the estimate to its nearest packing point. Fix any deterministic convention for ties.

In the ideal experiment, a decoding error requires

```math
d_{\mathrm{Ch}}(U_{t_J},\widehat U)\ge\frac{a}{2m}.
```

Otherwise the triangle inequality makes the true packing point strictly closer than every other point. Markov's inequality and Lemma 4 therefore give

```math
p_{\mathrm{ideal}}\le\frac{4K_d}{a^2}.
```

Lemma 3 changes the probability of any event by at most $`4m\sqrt\varepsilon`$. The actual decoding error is consequently bounded by

```math
p_{\mathrm{err}}\le q,
\qquad
q=\frac{4K_d}{a^2}+4m\sqrt\varepsilon.
```

This entire experiment is one fixed channel from the inserted battery to the classical estimate. Access to $`V^\dagger`$ and to independent probe states in this lower-bound experiment introduces no additional information about $`J`$.

## 5. Finite-error converse

### Theorem 5: a bound for every admissible pair of parameters

Assume $`r=r_U\ge1`$. For every implementation with $`\epsilon_F(\mathcal E_\beta,\mathcal U)\le\varepsilon`$, every integer $`m\ge m_0`$, and every $`a>0`$ satisfying

```math
\frac am\le\eta_0,
\qquad
q=\frac{4K_d}{a^2}+4m\sqrt\varepsilon\le\frac12,
```

one has

```math
C(\beta,H_B)
\ge
(1-q)
\left[
r\log\frac ma+\log c_{\mathrm{pack}}
\right]
-h_2(q),
```

where $`h_2`$ is binary entropy.

**Proof.** Lemma 2 and data processing imply $`C(\beta,H_B)\ge I(J;\widehat J)`$. Fano's inequality gives

```math
\begin{aligned}
I(J;\widehat J)
&\ge\log M-h_2(p_{\mathrm{err}})
-p_{\mathrm{err}}\log(M-1)\\
&\ge(1-p_{\mathrm{err}})\log M-h_2(p_{\mathrm{err}})\\
&\ge(1-q)\log M-h_2(q).
\end{aligned}
```

For the last step, $`p_{\mathrm{err}}\le q\le1/2`$ and binary entropy is increasing on that interval. Substitute the packing lower bound on $`M`$. ∎

The result is uniform over the battery Hamiltonian, its dimension and degeneracies, its mixedness, and its energy distribution. No continuity estimate for an entropy on a growing output space is used.

## 6. The leading logarithmic requirement

### Corollary 6: asymptotic lower bound

For fixed $`H,U`$ with $`r=r_U\ge1`$, there are constants $`A_{H,U}<\infty`$ and $`\varepsilon_0>0`$ such that every implementation with $`0<\varepsilon\le\varepsilon_0`$ and $`\epsilon_F\le\varepsilon`$ obeys

```math
C(\beta,H_B)
\ge
\frac r2\log\frac1\varepsilon
-\frac{3r}{2}\log\log\frac1\varepsilon
-A_{H,U}.
```

**Proof.** Set

```math
\ell=\log\frac1\varepsilon,
\qquad
m=\left\lfloor
\frac{\varepsilon^{-1/2}}{16\ell}
\right\rfloor,
\qquad
a=4\sqrt{K_d\ell}.
```

As $`\varepsilon\to0`$, one has $`m\to\infty`$ and $`a/m\to0`$. Thus the estimator and packing hypotheses hold for all sufficiently small $`\varepsilon`$. Moreover,

```math
q\le\frac1{4\ell}+\frac1{4\ell}
=\frac1{2\ell}.
```

Once the quantity inside the floor is at least two,

```math
m\ge\frac{\varepsilon^{-1/2}}{32\ell}.
```

Consequently,

```math
r\log\frac ma+\log c_{\mathrm{pack}}
\ge
\frac r2\ell-\frac{3r}{2}\log\ell
-r\left(7+\frac12\log K_d\right)
+\log c_{\mathrm{pack}}.
```

The explicit packing constants satisfy $`0<c_{\mathrm{pack}}<1`$. For sufficiently large $`\ell`$, the bracket in Theorem 5 is positive and at most $`r\ell/2`$. Multiplying it by $`q\le1/(2\ell)`$ therefore loses at most $`r/4`$. Since $`h_2(q)\le1`$, one may take

```math
A_{H,U}
=r\left(7+\frac12\log K_d\right)
-\log c_{\mathrm{pack}}
+\frac r4+1.
```

This proves the stated bound. The particular constant and logarithmic remainder are consequences of this parameter choice; the leading coefficient is the quantity matched by the construction. ∎

Taking the infimum over all allowed implementations preserves the inequality. Also, $`C(\beta,H_B)\le\log d_B`$, so the same argument yields

```math
d_B
\ge
2^{-A_{H,U}}
\varepsilon^{-r/2}
\left(\log\frac1\varepsilon\right)^{-3r/2}.
```

Together with the [finite battery construction](battery_construction.md), these are the matching leading entropy and logarithmic dimension requirements stated in the model.

## 7. Half-diamond accuracy and the zero-rank case

For a unitary target,

```math
\epsilon_F(\mathcal E,\mathcal U)
\le\delta(\mathcal E,\mathcal U)
=\frac12\|\mathcal E-\mathcal U\|_\diamond.
```

Indeed, for each pure input on system and reference, the ideal output is pure. The two-outcome test onto that ideal output gives $`1-F`$ as a probability difference, which is at most the output trace distance. Optimizing over inputs proves the inequality; mixed inputs can be purified.

Thus imposing $`\delta\le\varepsilon`$ also satisfies the hypothesis of Theorem 5 and Corollary 6, with the same numerical error budget $`\varepsilon`$. The lower bounds apply separately to each optimization

```math
C_{\min}^{(e)}(\varepsilon),
\qquad
D_{\min}^{(e)}(\varepsilon),
\qquad
e\in\{\epsilon_F,\delta\}.
```

Their upper bounds require the corresponding accuracy estimates in the construction; the two error metrics are not identified with each other.

If $`r_U=0`$, then $`[H,U]=0`$ by Proposition 1 of [Transition rank](transition_rank.md). A one-dimensional battery implements the gate exactly, so both coherence minima vanish and both dimension minima equal one. This includes $`d=1`$ and requires no estimation theorem.

## Sources of the imported machinery

- Gour, Marvian and Spekkens, *Measuring the quality of a quantum reference frame: the relative entropy of frameness*, Physical Review A **80**, 012307 (2009), especially Section III. [Primary source](https://arxiv.org/html/0901.0943v2) · [Relation to this result](../references/RELATED_WORK.md#gour2009).
- Marvian and Spekkens, *An information-theoretic account of the Wigner-Araki-Yanase theorem*, arXiv:1212.3378 (2012), Lemma 1 and the discussion of unitary transformations. [Primary source](https://arxiv.org/abs/1212.3378) · [Relation to this result](../references/RELATED_WORK.md#marvian2012).
- Chiribella, Yang and Renner, *Fundamental Energy Requirement of Reversible Quantum Operations*, Physical Review X **11**, 021014 (2021). [Primary source](https://doi.org/10.1103/PhysRevX.11.021014) · [Relation to this result](../references/RELATED_WORK.md#chiribella2021).
- Castellano, Cavina, Perarnau-Llobet, Giovannetti and Sekatski, *The entropic coherence is a necessary resource for non energy preserving gates*, arXiv:2509.01515v2 (2026 revision), Theorem 9, Eq. (60). [Primary source](https://arxiv.org/html/2509.01515v2) · [Relation to this result](../references/RELATED_WORK.md#castellano2026).
- Yang, Renner and Chiribella, *Optimal universal programming of unitary gates*, Physical Review Letters **125**, 210501 (2020), Theorem 2 and Appendix B; constants as in arXiv:2007.10363v3. [Primary source](https://arxiv.org/html/2007.10363v3) · [Relation to this result](../references/RELATED_WORK.md#yang2020).
