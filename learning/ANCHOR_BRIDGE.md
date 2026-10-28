# From Watrous to the coherence required for quantum control

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018)**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) supplies chapter manuscripts and errata. The section and theorem numbers below were checked in its standard-layout chapter PDFs. This repository links to that material and does not reproduce the book.

Watrous supplies the language of states, channels, distinguishability, and information. This project adds a physical restriction: the interaction implementing a gate must conserve the total energy of the system and its controller. The resulting question is how much energy coherence the controller must initially carry as the allowed gate error decreases.

Use the selected passages when their concepts enter the [30-milestone map](MILESTONES.md). They are not a whole-book prerequisite. The [model](../science/model.md) remains the canonical statement of the optimization and theorem; this bridge translates conventions and explains the additional steps.

<a id="reading-selections"></a>

## Selected passages

| Project question | Passage in the anchor | What to take into the project |
| --- | --- | --- |
| What is a mixed controller, and what does discarding it mean? | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.1.2–2.1.3 | Density operators, partial trace, and purification. |
| How does a joint interaction define the implemented gate? | Chapter 2, §§2.2.1–2.2.2; Corollary 2.27 | Channels and their Choi, Kraus, and isometric descriptions. |
| How does an experiment extract a classical label? | Chapter 2, §2.3.1; [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §3.1.1 | Measurement probabilities and state discrimination. |
| How close are the actual and ideal outputs? | Chapter 3, Definition 3.11; §3.2.2, Theorem 3.22; §3.2.3, Theorem 3.33 | Fidelity, its purification interpretation, and its relation to trace norm. |
| Why test the gate on entangled inputs? | Chapter 3, §§3.3.2–3.3.3; Definition 3.43 and Theorems 3.46, 3.51 | The completely bounded trace norm, sufficient reference dimension, and pure-input optimization. |
| How are uncertainty and distinguishability quantified? | [Chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), §§5.1.1–5.1.2; §5.2.1, Definitions 5.17–5.18; §5.2.2, Proposition 5.22; §5.2.3, Theorem 5.35 | Classical entropy, quantum entropy, relative entropy, nonnegativity, and data processing. |
| Why must recoverable phase information fit inside a controller resource? | Chapter 5, §5.3.3, especially Theorem 5.49 and Corollary 5.50 | The Holevo bound and the distinction between an ensemble's information and the dimension of its carrier. |

An optional illustration of an information-based converse is the **second main step** in the proof of Theorem 8.27, [Chapter 8](https://cs.uwaterloo.ca/~watrous/TQI/TQI.8.pdf), §8.1.2, Eqs. (8.141)–(8.148). It converts reliable decoding into a mutual-information requirement. The channel-capacity theorem itself is not an ingredient of this project. The direct Holevo theorem needed here is already in Chapter 5.

<a id="notation"></a>

## Notation and convention translations

| Object | Watrous convention | Convention in this project |
| --- | --- | --- |
| State vector and adjoint | A unit vector $`u`$, adjoint $`u^*`$, and pure state $`uu^*`$ | $`\lvert\psi\rangle`$, $`\langle\psi\rvert`$, and $`\lvert\psi\rangle\langle\psi\rvert`$; matrix adjoints use $`\dagger`$. |
| State space | $`\mathrm D(\mathcal X)`$ denotes density operators | $`\rho`$ and $`\beta`$ are density operators; $`D_{\min}^{(e)}`$ instead denotes a minimum battery dimension. |
| Identity map | $`1_{\mathrm L(\mathcal X)}`$ | $`\mathrm{id}`$; identity matrices are $`I`$. |
| Channel and unitary | A channel is usually $`\Phi`$ | $`U`$ is a matrix, $`\mathcal U(X)=UXU^\dagger`$ is its channel, and $`\mathcal E_\beta`$ is the implemented channel. |
| Fidelity | Definition 3.11 uses $`F_W(\rho,\sigma)=\lVert\sqrt\rho\sqrt\sigma\rVert_1`$; the subscript here distinguishes conventions | $`F=F_W^2`$. The error $`\epsilon_F`$ is worst-case **squared-fidelity infidelity**. |
| Channel norm | Definition 3.43 uses $`\lVert\!\lVert\!\lVert\Phi\rVert\!\rVert\!\rVert_1`$, the full completely bounded trace norm | This is $`\lVert\Phi\rVert_\diamond`$. The error $`\delta`$ is **half** this norm for the channel difference. |
| Choi operator | $`J(\Phi)`$ in §2.2.2 has trace $`d`$ for a channel with input dimension $`d`$ | A Choi **state** is $`J(\Phi)/d`$. The gate vector $`\lvert U\rangle`$ is normalized. |
| Entropy | $`H(\rho)`$ denotes quantum entropy | $`S(\rho)`$ denotes quantum entropy; $`H`$ without a state argument is the system Hamiltonian. Both use base-two logarithms. |
| Relative entropy | $`D(\rho\Vert\sigma)`$, with the support condition in Definition 5.18 | The same quantity. Energy coherence is the particular choice $`C(\beta,H_B)=D(\beta\Vert\Delta_{H_B}(\beta))`$. |
| Resource being optimized | The anchor supplies entropy and information quantities, rather than this controller optimization | $`C_{\min}^{(e)}`$ measures the coherence **initially present**, not coherence consumed per use. |

The symbols $`\epsilon_F`$ and $`\delta`$ label different error measures. The symbol $`\varepsilon`$ is a numerical tolerance imposed on one of them. Their separate optimizations are defined in [Model, Section 4](../science/model.md#4-exact-statement-of-the-resource-law).

<a id="states-and-channels"></a>

## From states and channels to a finite controller

Start with a system input $`\rho`$ and a controller state $`\beta`$. Apply a joint unitary $`V`$, then discard the controller:

```math
\mathcal E_\beta(\rho)
=\mathrm{Tr}_B[V(\rho\otimes\beta)V^\dagger].
```

This is a composition of a state preparation, unitary evolution, and partial trace. Chapter 2 supplies these operations and the general representation framework. The project restricts the allowed joint unitary further:

```math
[V,H\otimes I_B+I_S\otimes H_B]=0.
```

An arbitrary channel representation from Corollary 2.27 need not obey this equation. Establishing a channel representation therefore does not by itself supply an admissible controller.

The battery can be mixed. Its possible purification is a mathematical tool, not an extra controller that the implementation may secretly access. Initially the battery is independent of the input and any reference. For an entangled input $`\rho_{SA}`$, the tested output is $`(\mathcal E_\beta\otimes\mathrm{id}_A)(\rho_{SA})`$. The reference $`A`$ keeps track of correlations that a gate must preserve even though it acts only on $`S`$.

The implementation has no initial promise to return the battery. Approximate return appears later inside an imported recycling argument used to prove the lower bound. It is not part of the definition of a permissible single-use implementation. See [Model, Section 1](../science/model.md#1-system-gate-and-implementation).

<a id="accuracy-conventions"></a>

## From state distances to the two gate errors

With the notation translation above, Watrous's Theorem 3.33 becomes

```math
1-\sqrt{F(\rho,\sigma)}
\le\frac12\lVert\rho-\sigma\rVert_1
\le\sqrt{1-F(\rho,\sigma)}.
```

There is a stronger lower estimate when the ideal state is pure. Measuring its projector shows that the change in one event probability is $`1-F`$, so

```math
1-F(\rho,\lvert\psi\rangle\langle\psi\rvert)
\le\frac12\lVert\rho-\lvert\psi\rangle\langle\psi\rvert\rVert_1.
```

The ideal output of a unitary on a pure extended input is pure. Taking the appropriate worst cases gives the project's

```math
\epsilon_F(\mathcal E,\mathcal U)
\le\delta(\mathcal E,\mathcal U)
\le\sqrt{\epsilon_F(\mathcal E,\mathcal U)}.
```

These inequalities alone do not transfer an upper bound with coefficient $`r_U/2`$ from one error optimization to the other: the square root changes the precision scale. The [battery construction](../science/battery_construction.md) establishes a separate $`O(L^{-2})`$ bound for each reduced-channel error. Its proof of half-diamond accuracy uses real packet overlaps; an $`O(L^{-1})`$ bound on the implementing isometry alone would be too weak.

### Normalize the Choi state before measuring its distance

For a $`d`$-dimensional system, define

```math
\lvert\Phi_d\rangle
=\frac1{\sqrt d}\sum_{j=1}^{d}\lvert j\rangle\otimes\lvert j\rangle,
\qquad
\lvert U\rangle=(U\otimes I)\lvert\Phi_d\rangle.
```

Then $`\lvert U\rangle\langle U\rvert=J(\mathcal U)/d`$. The distance used to pack the gate orbit is

```math
d_{\mathrm{Ch}}(U,W)
=\frac12\bigl\lVert
\lvert U\rangle\langle U\rvert
-\lvert W\rangle\langle W\rvert
\bigr\rVert_1
=\sqrt{1-\frac{\lvert\mathrm{Tr}(U^\dagger W)\rvert^2}{d^2}}.
```

This uses one particular entangled input. It is not a replacement for the worst-case channel error. It provides a convenient metric on unitary channels, insensitive to global phase, for the [orbit geometry](../science/transition_rank.md) and the [estimation step](../science/coherence_converse.md#lemma-4-parallel-unitary-estimation).

<a id="entropy-and-information"></a>

## From entropy to the phase information in one battery

Chapter 5 gives the entropy and relative-entropy foundations. The physical comparison state here is obtained by removing coherence between **distinct battery energies**:

```math
\sigma=\Delta_{H_B}(\beta)=\sum_bP_b\beta P_b,
\qquad
C(\beta,H_B)=S(\sigma)-S(\beta).
```

The project supplies this choice of dephasing. It leaves all matrix elements within a degenerate energy eigenspace intact. On a composite system, dephasing in total-energy eigenspaces is generally different from dephasing each subsystem separately. A large entropy $`S(\beta)`$ is also not evidence of a large $`C`$: any state commuting with $`H_B`$ has $`C=0`$, including highly mixed states.

To see the information connection, choose a finite collection of actual times and encode a label $`j`$ in

```math
\beta_j=e^{-it_jH_B}\beta e^{it_jH_B},
\qquad
\bar\beta=\sum_jp_j\beta_j.
```

The comparison state $`\sigma`$ is unchanged by time translation. Expanding relative entropy therefore gives the locally proved identity

```math
C(\beta,H_B)
=\chi(\{p_j,\beta_j\})+D(\bar\beta\Vert\sigma),
\qquad
\chi=S(\bar\beta)-\sum_jp_jS(\beta_j).
```

The last relative entropy is nonnegative, so the ensemble carries at most $`C`$ bits of Holevo information. Watrous's Theorem 5.49 then bounds the information recovered by any fixed experiment:

```math
I(J;\widehat J)\le\chi\le C(\beta,H_B).
```

The experiment may use a fixed ancillary state and arbitrary measurements. They contain no information about the encoded label. The [converse, Lemma 2](../science/coherence_converse.md#lemma-2-finite-ensemble-holevo-bound), checks supports and derives the identity for every mixed finite battery. This use of asymmetry as orbit information has its own research antecedents, credited [below](#beyond-the-anchor).

### Supply the finite-label decoding step explicitly

For a uniform label $`J`$ among $`M\ge2`$ possibilities, let $`p`$ be the probability that an estimate $`\widehat J`$ is wrong. Introduce the classical error indicator $`Z`$, equal to one precisely when the estimate is wrong. The entropy chain rule gives

```math
\begin{aligned}
H(J\mid\widehat J)
&=H(Z\mid\widehat J)+H(J\mid Z,\widehat J)\\
&\le h_2(p)+p\log_2(M-1).
\end{aligned}
```

When $`Z=0`$, the estimate determines the label; when $`Z=1`$, at most $`M-1`$ labels remain. Here $`h_2(p)`$ is the binary entropy. Consequently,

```math
I(J;\widehat J)
\ge(1-p)\log_2 M-1.
```

This is the needed form of Fano's inequality, supplied here from classical entropy rules. Watrous's Lemma 5.54 discusses a binary special case, so it should not be cited as the full $`M`$-label statement. Combining the displayed bound with $`I\le C`$ explains why a reliably decodable collection of controller programs forces a coherence requirement.

<a id="conservation-and-active-frequencies"></a>

## From conservation to the gate's active phase coordinates

The next step is specific to the physical model. Commuting the joint time translation through the conserving interaction shows that the same processor takes $`\beta_t`$ to a channel approximating

```math
U_t=e^{-itH}Ue^{itH}.
```

Thus an implementation of one gate also determines a family of programs for its time orbit. The matrix block from energy $`F`$ to energy $`E`$ acquires the phase $`e^{-it(E-F)}`$ only when $`\Pi_EU\Pi_F\ne0`$. The active transition group and its rank are

```math
\Gamma_U=\mathrm{span}_{\mathbb Z}
\{E-F:\Pi_EU\Pi_F\ne0\},
\qquad
r_U=\dim_{\mathbb Q}\mathrm{span}_{\mathbb Q}\Gamma_U.
```

Rational independence is different from counting distinct gaps. Gaps $`1`$ and $`2`$ supply one independent frequency; gaps $`1`$ and $`\sqrt2`$ supply two. A gap belonging only to an untouched spectator does not contribute. These are exact statements about fixed spectra and fixed gates, not comparisons based on numerical rounding.

Watrous's finite-dimensional channel formalism does not by itself identify the geometry of this time orbit. The project proves that its closure has $`r_U`$ local phase coordinates, that quotienting global phase leaves this dimension unchanged, and that its Choi metric admits a packing with size proportional to $`\eta^{-r_U}`$ at sufficiently small separation $`\eta`$. The [transition-rank proof](../science/transition_rank.md) supplies the integer coordinates, the local metric argument, and the replacement of ideal torus points by actual times.

The finite-ensemble formulation matters: the battery's spectrum is arbitrary. Its time translations do not have to extend to the same torus used to describe the system gate. The entropy argument only needs the actual finite ensemble of battery states.

<a id="beyond-the-anchor"></a>

## What the project adds, and what it imports from research

The bridge from the textbook to the resource law has several distinct parts. Their status should remain visible when reading the proof.

| Step | Status and source |
| --- | --- |
| A conserved symmetry turns reference states into programs for an orbit | Established perspective due to [Marvian and Spekkens](../references/RELATED_WORK.md#marvian2012). The project's covariance identity is derived in [converse, Lemma 1](../science/coherence_converse.md#lemma-1-the-same-implementation-processes-every-time-translate). |
| Relative-entropy asymmetry bounds orbit information | Established connection due to [Gour, Marvian, and Spekkens](../references/RELATED_WORK.md#gour2009). The finite-ensemble calculation is supplied in Lemma 2. |
| One accurate processor emulates several parallel uses of the programmed gate | Imported recycling theorem of [Chiribella, Yang, and Renner](../references/RELATED_WORK.md#chiribella2021), used in the stated form from [Castellano et al., Theorem 9](../references/RELATED_WORK.md#castellano2026). It is not derived from the textbook's fidelity inequalities alone. |
| Parallel gate queries resolve nearby unitary channels at the required scale | Imported estimation protocol of [Yang, Renner, and Chiribella](../references/RELATED_WORK.md#yang2020). The passage from its channel guarantee to the Choi-distance risk is shown in converse, Lemma 4. |
| The gate-specific orbit has dimension $`r_U`$ and a usable metric packing | Proved in [transition_rank.md](../science/transition_rank.md), including degeneracies and global phase. |
| A conserving finite battery achieves the matching exponent | Proved in [battery_construction.md](../science/battery_construction.md), using established shift and sine-packet ideas. [Åberg](../references/RELATED_WORK.md#aberg2014), [Chiribella et al.](../references/RELATED_WORK.md#chiribella2021), and [Popescu et al.](../references/RELATED_WORK.md#popescu2018) supply the relevant construction antecedents. |

These primary papers are proof dependencies and attribution sources. They are not additional educational anchors or a second prerequisite reading list.

The lower bound uses approximately $`m`$ gate queries to decode a packing with about $`m^{r_U}`$ elements, with logarithmic adjustments to make the decoding error vanish. The imported recycling error grows as $`m\sqrt{\varepsilon}`$. Balancing these quantities gives the leading coherence coefficient $`r_U/2`$. The [converse](../science/coherence_converse.md) keeps the error terms and proves the stated logarithmic remainder; a parameter count alone does not establish the bound for mixed batteries.

For the upper bound, a smooth packet of length $`L`$ in each active frequency coordinate has entropy at most $`r_U\log_2L`$. Fixed shifts give both gate errors of order $`L^{-2}`$. Taking $`L`$ of order $`\varepsilon^{-1/2}`$ gives the same leading coefficient. Completing the action on boundary energy sectors is essential: a shift on a finite ladder is not automatically unitary. The construction includes the necessary margin and defines the interaction on the entire finite Hilbert space.

Finally, $`C\le\log_2\dim B`$ converts the coherence converse into a dimension lower bound, while the explicit battery supplies the matching upper exponent. The [model](../science/model.md#4-exact-statement-of-the-resource-law) states separate results for $`\epsilon_F`$ and $`\delta`$, retains the polylogarithmic gap, and fixes $`H,U,d`$ before taking the error to zero. Neither the anchor nor this bridge turns that statement into an exact finite-error minimum, an energy optimum, or a claim of unlimited catalytic reuse.

Return to the [milestone map](MILESTONES.md), the [model](../science/model.md), or the [worked examples](../science/examples.md) according to the concept being followed.
