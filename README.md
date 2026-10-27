# Quantum Control Coherence

How much coherence must a finite quantum controller contain to implement a gate while conserving total energy exactly?

For a fixed system Hamiltonian and target unitary, the answer is set by the **rational rank of the energy transitions used by the gate**. Each independent active frequency contributes one half of the leading logarithmic coherence requirement. The same rank fixes the leading power with which the minimum controller dimension grows as the allowed error decreases.

## Principal result

Let $`H=\sum_E E\Pi_E`$ be a fixed finite-dimensional Hamiltonian and $`U`$ a fixed target unitary. The controller, called a battery, begins in an arbitrary state $`\beta`$ independent of the unknown system input. A joint unitary $`V`$ obeys exact additive energy conservation, $`[V,H+H_B]=0`$. Define

```math
r_U=\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}
\{E-F:\Pi_EU\Pi_F\ne0\}.
```

The charged resource is the battery's initial entropic energy coherence,

```math
C(\beta,H_B)=S(\Delta_{H_B}\beta)-S(\beta),
```

where dephasing removes coherence between distinct total battery energies and entropy is measured in bits. Optimize separately over all finite battery Hamiltonians, mixed states, and conserving interactions. For either reference-assisted worst-case squared-fidelity infidelity $`e=\epsilon_F`$ or half-diamond error $`e=\delta`$, the [resource theorem](science/model.md#4-exact-statement-of-the-resource-law) gives

```math
\lim_{\varepsilon\downarrow0}
\frac{C_{\min}^{(e)}(\varepsilon)}{\log_2(1/\varepsilon)}
=
\lim_{\varepsilon\downarrow0}
\frac{\log_2 D_{\min}^{(e)}(\varepsilon)}{\log_2(1/\varepsilon)}
=\frac{r_U}{2}.
```

For positive rank and sufficiently small $`\varepsilon`$, the proved finite-error bounds are

```math
\begin{aligned}
\frac{r_U}{2}\ell-\frac{3r_U}{2}\log_2\ell-O_{H,U}(1)
&\le C_{\min}^{(e)}(\varepsilon)
\le\frac{r_U}{2}\ell+O_{H,U}(1),\\
\varepsilon^{-r_U/2}\ell^{-3r_U/2}\,2^{-O_{H,U}(1)}
&\le D_{\min}^{(e)}(\varepsilon)
\le O_{H,U}(\varepsilon^{-r_U/2}),
\qquad \ell=\log_2(1/\varepsilon).
\end{aligned}
```

Thus $`D_{\min}^{(e)}(\varepsilon)=\varepsilon^{-r_U/2+o(1)}`$. The dimension bounds retain a polylogarithmic gap. If $`r_U=0`$, the gate commutes with the Hamiltonian and a one-dimensional, zero-coherence battery implements it exactly.

The constructive family has nonnegative, finite battery energies and mean energy $`O_{H,U}(\varepsilon^{-1/2})`$. This is an achievable energy scaling, not an optimal-energy claim.

## What the rank changes

The same three-level gate can require different dimension exponents, while an unused level adds no active frequency. Here $`F_3`$ is the qutrit Fourier gate and $`H_2`$ the qubit Hadamard gate.

| System energies | Target gate | Active rank | Leading dimension law |
|---|---|---:|---|
| $`0,1`$ | $`H_2`$ | 1 | $`\varepsilon^{-1/2+o(1)}`$ |
| $`0,1,2`$ | $`F_3`$ | 1 | $`\varepsilon^{-1/2+o(1)}`$ |
| $`0,1,\sqrt2`$ | $`F_3`$ | 2 | $`\varepsilon^{-1+o(1)}`$ |
| $`0,1,\sqrt2`$ | $`H_2\oplus1`$ | 1 | $`\varepsilon^{-1/2+o(1)}`$ |
| Any finite spectrum | $`[H,U]=0`$ | 0 | Exactly 1 |

The [worked examples](science/examples.md) also cover degenerate energies, a finite global-phase stabilizer, small-angle gates, and rational approximants. Exact spectral relations determine the asymptotic rank. The constants and crossover scales need not remain uniform as those relations or the gate change.

## Read the science

Start with the [model and theorem](science/model.md), then follow the proofs or the physical interpretation according to your question.

| Question | Authoritative account |
|---|---|
| What is optimized, and under which accuracy convention? | [Model, assumptions, and resource law](science/model.md) |
| Why can one time parameter contain several active phases? | [Transition rank and the closed gate orbit](science/transition_rank.md) |
| Why must every finite mixed battery carry enough coherence? | [Orbit information, recycling, and the converse](science/coherence_converse.md) |
| How is a finite, globally unitary conserving controller built? | [Energy lattice, boundary completion, and error bounds](science/battery_construction.md) |
| What happens in concrete systems and limiting cases? | [Examples](science/examples.md) |
| What does the result say about physical resources? | [Interpretation](science/interpretation.md) |
| Which methods and endpoints come from earlier work? | [Related work and proof dependencies](references/RELATED_WORK.md), [BibTeX](references/references.bib) |

The converse uses the known connection between asymmetry and accessible orbit information, approximate processor recycling, and parallel unitary estimation. The construction uses conserving energy shifts and smooth finite packets. The contribution developed here is the matching active-rank law for arbitrary mixed finite batteries and the corresponding optimal leading dimension exponent. The [attribution map](references/RELATED_WORK.md#what-is-inherited-and-what-is-established-here) distinguishes this conclusion from those inherited ingredients and the known qubit endpoint.

## Reproduce the finite construction

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_construction.py
```

The [verification suite](verification/README.md) compares a directly assembled finite energy-block unitary with an independently evaluated overlap-kernel channel. It exercises eight models and 24 global unitaries, with exact integer energy-conservation checks. The [recorded output](verification/results.json) reports zero conservation violations, a maximum channel discrepancy of $`2.22\times10^{-16}`$, and a maximum unitarity entry defect of $`4.44\times10^{-16}`$.

The checks include spectators, degenerate energies, coincident total-energy sectors, and the rank-zero case. They test the construction and its finite bounds. The analytic proofs establish the general resource law; sampled fidelities and scaling data are not substitutes for its converse or an exact diamond-norm optimization.

## Scope

The system, gate, and exact spectrum remain fixed as the error tends to zero. The theorem charges initial coherence and total battery dimension. It does not impose a return condition, bounded interaction time, locality, efficient preparation, or a fixed battery architecture. Its mean-energy statement concerns the explicit upper-bound construction. Approximate conservation and simultaneous growing-system limits require separate analysis.

For question-based navigation and retrieval, see [llms.txt](llms.txt).

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
