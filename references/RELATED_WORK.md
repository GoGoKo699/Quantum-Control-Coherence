# Related work and proof dependencies

This project studies the initial entropic energy coherence needed to implement one fixed finite-dimensional unitary under exact additive energy conservation. For the system Hamiltonian $`H=\sum_E E\Pi_E`$ and target $`U`$, the invariant used throughout is

```math
\Gamma_U=\mathrm{span}_{\mathbb Z}
\{E-F:\Pi_EU\Pi_F\ne0\},
\qquad
r_U=\mathrm{rank}_{\mathbb Z}\Gamma_U.
```

The result combines established information-theoretic and reference-frame methods with an explicit identification of this active transition group and a finite conserving construction. The theorem concerns arbitrary mixed finite batteries. It charges the coherence initially present, not the amount consumed in one use. The main error $`\epsilon_F`$ is worst-case reference-assisted infidelity with squared Uhlmann fidelity; half-diamond error $`\delta`$ is treated separately.

## What is inherited and what is established here

| Ingredient | Antecedent | Role in this project |
| --- | --- | --- |
| Symmetric implementation as programming of a group orbit | [Marvian and Spekkens](#marvian2012) | Applied to actual time translates of an arbitrary mixed battery. |
| Relative-entropy asymmetry bounds accessible orbit information | [Gour, Marvian, and Spekkens](#gour2009) | A finite-ensemble relative-entropy identity bounds the decoder's information by battery coherence. |
| Approximate reuse by alternating a processor and its inverse | [Chiribella, Yang, and Renner](#chiribella2021); current statement in [Castellano et al.](#castellano2026) | Supplies many approximately independent gate queries from one battery program. |
| Universal parallel unitary estimation at Heisenberg scaling | [Yang, Renner, and Chiribella](#yang2020) | Resolves a finite packing of the physical gate orbit. |
| Parameter count as a guide to programming memory | [Yang et al.](#yang2020), [He and Yang](#heyang2026) | Motivation; the converse uses a proved local metric packing of this particular orbit. |
| Coherent energy shifts and smooth finite packets | [Åberg](#aberg2014), [Chiribella et al.](#chiribella2021) | Extended to the active integer lattice, with finite boundary completion. |
| Finite reference frames under general conservation laws | [Popescu et al.](#popescu2018) | Establishes that finite arbitrary-spectrum implementations already exist. |
| Entropic coherence lower bounds for the same gate task | [Castellano et al.](#castellano2026) | Closest comparison for the optimal entropy and dimension laws. |

The project-specific conclusion is the matching leading law

```math
\lim_{\varepsilon\to0}
\frac{C_{\min}^{(e)}(\varepsilon)}{\log_2(1/\varepsilon)}
=
\lim_{\varepsilon\to0}
\frac{\log_2 D_{\min}^{(e)}(\varepsilon)}{\log_2(1/\varepsilon)}
=\frac{r_U}{2},
\qquad e\in\{\epsilon_F,\delta\},
```

with the separate optimizations defined in the [model](../science/model.md). The proof identifies the closed projective gate orbit with an $`r_U`$-dimensional torus quotient, obtains the entropy converse from finite-packing discrimination, and realizes the matching dimension exponent with a positive finite energy lattice. The componentwise construction excludes spectator transitions and keeps mean battery energy at $`O_{H,U}(\varepsilon^{-1/2})`$. These statements are proved in the science documents; they are not consequences of a parameter count asserted without a local metric argument.

<a id="castellano2026"></a>

## Castellano et al.: entropic coherence for gates

Riccardo Castellano, Vasco Cavina, Martí Perarnau-Llobet, Vittorio Giovannetti, and Pavel Sekatski, *The entropic coherence is a necessary resource for non-energy preserving gates*. [arXiv:2509.01515v2](https://arxiv.org/abs/2509.01515v2), revised 1 September 2026; [full text](https://arxiv.org/html/2509.01515v2). Bibliography key: `castellano2026entropic`.

This is the closest work in the same energy-conserving gate model. Main Eqs. (7)–(8) give leading lower coefficients $`r_2/8`$ for suitable battery families and $`r_2/4`$ under their proportionate-family condition. The qubit argument separately gives coefficient $`1/2`$ under that condition. Corollary 3 establishes diverging battery dimension and the optimal qubit dimension exponent. The final discussion asks for sharper general bounds and constructions beyond equally spaced spectra.

The comparison here is the matching arbitrary-spectrum law for arbitrary mixed finite batteries, without a proportionate-family hypothesis. Neither the qubit dimension exponent nor the necessity of unbounded dimension is claimed as new. We retain their notation $`r_2`$ when describing their results and use the independently defined $`r_U`$ for ours; no uniform numerical factor comparison is asserted between these separately defined invariants.

Their Theorem 9, Eq. (60), is the precise recycling statement used below. No iid-sum entropy theorem from their Appendix F is imported into this project's proof.

<a id="chiribella2021"></a>

## Chiribella, Yang, and Renner: recycling and energy requirements

Giulio Chiribella, Yuxiang Yang, and Renato Renner, *Fundamental Energy Requirement of Reversible Quantum Operations*, **Physical Review X 11**, 021014 (2021). [DOI](https://doi.org/10.1103/PhysRevX.11.021014); [arXiv:1908.10884v3](https://arxiv.org/abs/1908.10884v3), 28 May 2021; [PDF](https://arxiv.org/pdf/1908.10884v3). Bibliography key: `chiribella2021energy`.

Appendix A, Lemma 1 and Corollaries 1–2, supplies the approximate decoupling and alternating forward/inverse reuse argument. It permits mixed initial batteries and compares the final state with the original battery. The coherent-shift construction and sine-shaped finite battery packet in the main text and Appendix C are also antecedents of our upper bound.

For consistency with the current [entropic-coherence paper](#castellano2026), this project uses its full-diamond estimate

```math
\left\|\mathcal R_m(\,\cdot\,\otimes\beta)
-(\mathcal U\otimes\mathcal U^\dagger)^{\otimes m}(\,\cdot\,)
\otimes\beta\right\|_\diamond
\le 8m\sqrt{\epsilon_F}.
```

The original PRX Corollary 2 displays the stronger constant $`4`$; no claim here depends on that stronger constant. Reuse is an imported proof device, not a new catalytic implementation theorem. The resource in this project is total-energy dephasing asymmetry, so results for dephasing in a fixed tensor-product basis must not be substituted without checking the free operations.

<a id="yang2020"></a>

## Yang, Renner, and Chiribella: programming and estimation

Yuxiang Yang, Renato Renner, and Giulio Chiribella, *Optimal Universal Programming of Unitary Gates*, **Physical Review Letters 125**, 210501 (2020). [DOI](https://doi.org/10.1103/PhysRevLett.125.210501); [arXiv:2007.10363v3](https://arxiv.org/abs/2007.10363v3), 4 February 2021; [full text](https://arxiv.org/html/2007.10363v3). Bibliography key: `yang2020programming`.

Theorem 2 and Appendix B construct a probe for $`m`$ parallel uses of an unknown unitary and a measurement returning an estimate. Their Eq. (5), for $`m\ge2d(d-1)`$, bounds the half-diamond error of the measure-and-operate channel by $`K_d/m^2`$, with

```math
K_d=2\left[\frac{\pi(d-1)^2(3d-2)}d\right]^2.
```

Testing that channel on a normalized maximally entangled state implies the mean squared Choi-distance bound used here. The arXiv v3 constants improve the dimension dependence relative to the published version; the fixed-dimension scaling is unchanged.

The paper already connects programming, recycling, Holevo information, and Heisenberg estimation. Its Eq. (11) conjectures a half-parameter-count law for more general gate families. This project establishes a specific conserving-controller entropy optimum, not a new universal programming principle. A lower bound on program dimension alone would not imply a lower bound on coherence of arbitrary mixed programs.

<a id="heyang2026"></a>

## He and Yang: parameterized circuit programming

Entong He and Yuxiang Yang, *Resource quantification for programming low-depth quantum circuits*, **Quantum 10**, 2166 (2026). [Journal](https://quantum-journal.org/papers/q-2026-07-20-2166/); [DOI](https://doi.org/10.22331/q-2026-07-20-2166); [arXiv:2509.09642v2](https://arxiv.org/abs/2509.09642v2), 14 July 2026; [full text](https://arxiv.org/html/2509.09642v2). Bibliography key: `he2026programming`.

The work bounds the memory and circuit costs of programming shallow circuit families. Section 4.6, Proposition 28, discusses parameterized families and gives program-dimension bounds in terms of the ambient parameter-space dimension. The displayed lower and upper coefficients do not coincide in general.

Its resource is program Hilbert-space size. It does not provide the mixed-battery entropic energy-coherence converse or the exactly conserving arbitrary-spectrum construction used here. We do not import Proposition 28. Instead, the gate orbit's local Choi metric, finite projective stabilizer, and packing size are established explicitly. The known connection between dimension, distinguishability, and programming remains part of the attribution.

<a id="gour2009"></a>

## Gour, Marvian, and Spekkens: orbit information and asymmetry

Gilad Gour, Iman Marvian, and Robert W. Spekkens, *Measuring the quality of a quantum reference frame: The relative entropy of frameness*, **Physical Review A 80**, 012307 (2009). [DOI](https://doi.org/10.1103/PhysRevA.80.012307); [arXiv:0901.0943v2](https://arxiv.org/abs/0901.0943v2), 14 July 2009; [PDF](https://arxiv.org/pdf/0901.0943v2). Bibliography key: `gour2009frameness`.

The paper identifies relative-entropy frameness with the entropy increase under group twirling. Section III gives its interpretation as an upper bound on information accessible from a group-orbit encoding. This is the information-theoretic meaning of coherence used in the converse.

For a finite ensemble of actual time translates, the proof here writes Donald's identity with the invariant comparison state $`\Delta_{H_B}(\beta)`$. This directly gives $`\chi\le C(\beta,H_B)`$ for mixed batteries. It is an application of the established asymmetry-information connection. The finite-ensemble formulation avoids imposing any commensurability condition on the battery Hamiltonian or extending its real-time orbit to the system's torus.

<a id="marvian2012"></a>

## Marvian and Spekkens: symmetry and programming

Iman Marvian and Robert W. Spekkens, *An information-theoretic account of the Wigner-Araki-Yanase theorem*. [arXiv:1212.3378v1](https://arxiv.org/abs/1212.3378v1), 14 December 2012; [PDF](https://arxiv.org/pdf/1212.3378v1). Bibliography key: `marvian2012way`.

Lemma 1 expresses the duality between symmetric resource conversion and a common processor acting on an entire group-orbit encoding. The discussion extends the information-theoretic perspective beyond the original measurement setting, including unitaries.

The relation between time-translated battery programs and conjugated target gates is this established perspective applied to additive energy conservation. Our proof supplies the covariance identity explicitly, so the approximate, reference-assisted error convention can be tracked directly. The additional quantitative work is the active-orbit packing and its discrimination after recycling, followed by the matching finite-controller construction.

<a id="aberg2014"></a>

## Åberg: coherent energy shifts

Johan Åberg, *Catalytic Coherence*, **Physical Review Letters 113**, 150402 (2014). [DOI](https://doi.org/10.1103/PhysRevLett.113.150402); [arXiv:1304.1060v3](https://arxiv.org/abs/1304.1060v3), 20 October 2014; [PDF](https://arxiv.org/pdf/1304.1060v3). Bibliography key: `aberg2014catalytic`.

The energy-ladder construction implements system transitions by compensating translations of a coherent reservoir. Main Eq. (1) and Appendix B develop the conserving shift operator and explain why translation overlaps control the induced channel.

That architecture is inherited. Here it is placed on the integer lattice generated by active energy transitions, padded to define a unitary on the entire finite battery space, and combined with product sine packets. The resulting entropy and dimension exponents are matched to the mixed-state converse. The present theorem charges an initial resource inventory and makes no assertion of unlimited independent catalytic reuse.

<a id="tajima2020"></a>

## Tajima, Shiraishi, and Saito: Fisher-information coherence cost

Hiroyasu Tajima, Naoto Shiraishi, and Keiji Saito, *Coherence cost for violating conservation laws*, **Physical Review Research 2**, 043374 (2020). [DOI](https://doi.org/10.1103/PhysRevResearch.2.043374); [arXiv:1906.04076v2](https://arxiv.org/abs/1906.04076v2), 25 July 2019; [PDF](https://arxiv.org/pdf/1906.04076v2). Bibliography key: `tajima2020coherence`.

Theorems 1–2 give asymptotically matching necessary and sufficient coherence requirements when coherence is measured by quantum Fisher information. Their coefficient depends on the spectral range of $`U^\dagger H U-H`$ and their error convention.

This is an optimal-resource theorem for a different quantity. Quantum Fisher information depends on the magnitudes of energy gaps; entropic energy coherence is invariant under a nonzero common rescaling of the Hamiltonian. A Fisher-information bound does not determine the entropy or total Hilbert dimension when the battery spectrum and state are unconstrained. The current theorem complements that law by quantifying the number of independent active phase coordinates.

<a id="popescu2018"></a>

## Popescu et al.: finite reference frames for general conserved quantities

Sandu Popescu, Ana Belén Sainz, Anthony J. Short, and Andreas Winter, *Quantum reference frames and their applications to thermodynamics*, **Philosophical Transactions of the Royal Society A 376**, 20180111 (2018). [DOI](https://doi.org/10.1098/rsta.2018.0111); [arXiv:1804.03730v1](https://arxiv.org/abs/1804.03730v1), 10 April 2018; [PDF](https://arxiv.org/pdf/1804.03730v1). Bibliography key: `popescu2018reference`.

Theorem 1 constructs finite reference systems from many replicas of the controlled system. Partial swaps implement arbitrary target unitaries while preserving extensive quantities. Appendices C–D give an $`O(1/N)`$ trace-error estimate for the repeated construction.

Thus finite conserving implementations for arbitrary finite system spectra already exist. This project does not claim that existence result. Its construction instead matches an optimal entropic active-rank law and a polynomial **total** battery-dimension exponent. The general replica construction does not state that optimum or the unrestricted mixed-state entropy converse.

<a id="castellanosekatski2025"></a>

## Castellano and Sekatski: entropy of discrete sums and rank conventions

Riccardo Castellano and Pavel Sekatski, *On the entropy growth of sums of iid discrete random variables*. [arXiv:2508.05348v1](https://arxiv.org/abs/2508.05348v1), submitted 7 August 2025; [full text](https://arxiv.org/html/2508.05348v1). Bibliography key: `castellanosekatski2025entropy`.

This is the entropy-growth source used by Castellano et al. It defines an incommensurability rank through nondegenerate canonical prepartitions. The present work defines its active transition rank directly and keeps the source's $`r_2`$ notation separate from $`r_U`$ when stating comparisons.

No prepartition rank, iid-sum entropy asymptotic, or example from this source is needed for the theorem here. The active rank is defined directly from spectral blocks, and its operational role is proved by the local geometry of the gate orbit.

## Scope of the comparison

The strongest antecedents establish the information-theoretic framework, the recycling and estimation tools, conserving controller constructions, and the necessity of entropic coherence. The contribution developed here is their use in a matching, gate-specific resource characterization for arbitrary mixed finite batteries: an $`r_U/2`$ entropy coefficient and the same leading logarithmic dimension coefficient for arbitrary fixed finite spectra.

No statement is made here about continuous-spectrum batteries, approximate conservation, a uniform limit in growing system dimension, or physically efficient preparation of the optimal battery and joint unitary. Exact rational relations can affect $`r_U`$; constants in the construction depend on the fixed arithmetic embedding. These limits are part of the theorem's scope, not assumptions supplied by the cited general programming results.

Bibliographic entries are in [references.bib](references.bib).
