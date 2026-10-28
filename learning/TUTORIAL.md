# A gate and a finite quantum phase reference

A quantum controller must do more than supply energy. When a gate creates a superposition of different system energies, the controller must preserve the relative phase between the alternatives. If the controller records which energy transfer occurred in distinguishable final states, discarding it weakens the system's coherence.

This tutorial follows that mechanism in one complete qubit example, then connects it to the two directions of the resource theorem. The [30-milestone map](MILESTONES.md) supplies the full conceptual route, and the [Watrous bridge](ANCHOR_BRIDGE.md) supplies the selected textbook foundations and convention translations. The exact general statements remain in the [scientific model](../science/model.md).

## 1. The gate to be implemented

Consider a qubit with orthonormal energy states $`|0\rangle`$ and $`|1\rangle`$, of energies zero and one in fixed units. Its Hamiltonian and desired Hadamard gate are

```math
H=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\qquad
U=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
```

The gate takes $`|0\rangle`$ to $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$ and $`|1\rangle`$ to $`|-\rangle=(|0\rangle-|1\rangle)/\sqrt2`$. It must act correctly on an arbitrary superposition of those inputs and preserve any entanglement with an external reference. A successful calculation for $`|0\rangle`$ alone will illustrate the mechanism; a separate uniform bound will establish the channel guarantee.

The battery starts independently of the unknown input. A joint unitary $`V`$ is allowed only when it commutes with the total Hamiltonian $`H+H_B`$. This restriction requires every system energy gain to have a compensating battery energy loss. The framework and accuracy conventions are developed in [M01–M06](MILESTONES.md#m01).

## 2. A unitary on the entire finite system

Choose an integer packet length $`L\ge1`$. Give the battery the finite ladder of energies $`k=0,1,\ldots,L+3`$, so its full dimension is $`L+4`$. A joint basis state $`|j,k\rangle`$ specifies the system state $`j`$ and battery energy $`k`$.

For each total energy $`q=1,\ldots,L+3`$, the states $`|0,q\rangle`$ and $`|1,q-1\rangle`$ form a complete two-dimensional sector. Apply the Hadamard matrix inside each such sector:

```math
\begin{aligned}
V|0,q\rangle
&=\frac{|0,q\rangle+|1,q-1\rangle}{\sqrt2},\\
V|1,q-1\rangle
&=\frac{|0,q\rangle-|1,q-1\rangle}{\sqrt2}.
\end{aligned}
```

The lowest sector contains only $`|0,0\rangle`$, and the highest contains only $`|1,L+3\rangle`$. Let $`V`$ act as the identity on these two states. The sectors partition the full joint basis, and each carries a unitary. The resulting $`V`$ is therefore a genuine finite unitary and conserves energy exactly.

Prepare the battery in the interior sine packet

```math
|b_L\rangle
=\sqrt{\frac{2}{L+1}}
\sum_{n=1}^{L}\sin\frac{\pi n}{L+1}\,|n+1\rangle.
```

Its occupied levels are $`2,\ldots,L+1`$. For either system basis input, every occupied joint state lies in a complete sector. The unused edge levels provide a margin that makes the desired shifts compatible with a finite space. The general construction makes the same distinction between populated support and full battery dimension; see [M24–M25](MILESTONES.md#m24) and [the boundary proof](../science/battery_construction.md#3-a-global-unitary-including-the-boundary).

## 3. Shifted packets determine the system's coherence

For the input $`|0\rangle`$, the joint output has the form

```math
V(|0\rangle\otimes|b_L\rangle)
=\frac1{\sqrt2}
\left(|0\rangle\otimes|b_L\rangle
+|1\rangle\otimes|b_L^-\rangle\right),
```

where $`|b_L^-\rangle`$ is the packet shifted down by one battery level. Both packets remain inside the finite ladder. This shifted-state notation describes the output of the blockwise unitary above; it does not assume that translation is a unitary on a finite ladder.

The overlap of the two packets is

```math
g_1=\langle b_L|b_L^-\rangle
=\cos\frac{\pi}{L+1}.
```

Tracing out the battery gives

```math
\rho_{\mathrm{out}}
=\frac12\begin{pmatrix}1&g_1\\g_1&1\end{pmatrix}.
```

The diagonal entries are the probabilities of the two system energies. The off-diagonal entries carry their coherence. They contain the battery overlap because the two energy-transfer alternatives leave different battery packets. As that overlap approaches one, the battery carries less information about which alternative occurred, and the reduced system approaches the desired pure state $`|+\rangle`$.

The project's squared fidelity with this pure target is

```math
F(\rho_{\mathrm{out}},|+\rangle\langle+|)
=\langle+|\rho_{\mathrm{out}}|+\rangle
=\frac{1+g_1}{2}.
```

The infidelity for this particular input is therefore

```math
1-F
=\sin^2\frac{\pi}{2(L+1)}
=O(L^{-2}).
```

Watrous's unsquared fidelity is the nonnegative square root of this $`F`$. Keeping that distinction prevents a factor or square-root error when translating the [state-distance results](ANCHOR_BRIDGE.md#accuracy-conventions).

## 4. A small packet with all resources visible

At $`L=2`$, the normalized packet is simply

```math
|b_2\rangle=\frac{|2\rangle+|3\rangle}{\sqrt2}.
```

Its downward shift occupies levels one and two. Only level two is shared, giving overlap $`g_1=1/2`$. The resources and the selected-input accuracy are then:

| Quantity | Value | Meaning |
|---|---|---|
| Initial entropic energy coherence | 1 bit | The pure packet occupies two distinct energies with equal probabilities. |
| Full battery dimension | 6 | All levels zero through five belong to the finite implementation. |
| Initial mean battery energy | $`5/2`$ | The average of the occupied energies two and three. |
| Squared fidelity for input $`\lvert0\rangle`$ | $`3/4`$ | The probability of the ideal-output projector $`\lvert+\rangle\langle+\rvert`$. |
| Watrous root fidelity for that input | $`\sqrt3/2`$ | The square root of the project's fidelity. |

One bit of coherence describes this initial state. It does not say that a use consumes one bit. Also, the four unoccupied battery levels still count toward the implementation's total dimension. These distinctions are part of the resource model, as explained in [M07](MILESTONES.md#m07) and [M12](MILESTONES.md#m12).

The packet is deliberately small enough to inspect directly. Its selected-input fidelity is not the exact worst-case fidelity of the channel, nor is this a claim that six levels are the smallest possible controller for a specified tolerance.

## 5. From one input to a uniform gate guarantee

For an arbitrary input, several shifted packets appear at once. The general construction bounds their differences uniformly at the level of the implementing isometry. Tensoring with any reference preserves that operator-norm estimate. Comparing with the ideal purified output and then tracing out the battery gives a bound on worst-case squared-fidelity infidelity.

The half-diamond bound needs a second argument. The reduced channel contains real packet overlaps $`g_v`$. Their coefficient errors obey

```math
1-g_v=\frac12\|(T^v-I)b_L\|^2=O(L^{-2})
```

for every fixed required shift $`v`$. Here $`T^v`$ is a mathematical translation of the zero-extended packet used to evaluate overlaps. The physical operation remains the finite sector unitary. The coefficient estimates then control the channel with any reference attached.

For this fixed Hadamard example, the explicit constants in [the construction](../science/battery_construction.md) are

```math
A_{\mathrm{iso}}=\pi\sqrt2,
\qquad B_{\mathrm{ch}}=4\pi^2.
```

Consequently, both errors satisfy the conservative uniform bound

```math
\epsilon_F(\mathcal E_L,\mathcal U),\;
\delta(\mathcal E_L,\mathcal U)
\le\min\left\{1,\frac{2\pi^2}{(L+1)^2}\right\}.
```

This bound is trivial at $`L=2`$; the exact single-input calculation above gives different, more limited information. For sufficiently large $`L`$, the uniform bound certifies the inverse-square accuracy scaling. The distinct proofs for the two metrics are the subjects of [M26](MILESTONES.md#m26) and [M27](MILESTONES.md#m27).

## 6. Why several active frequencies enlarge the controller

The qubit gate uses energy changes zero and $`\pm1`$. They all belong to one integer frequency group, so its active rank is $`r_U=1`$.

For a fully supported qutrit Fourier gate on energies $`(0,1,2)`$, the active gaps still use only that one independent frequency. On energies $`(0,1,\sqrt2)`$, they require two rationally independent frequencies. The construction uses a packet along each active integer coordinate, with total battery energies given by a positive combination of those coordinates.

For a fixed gate and spectrum, a packet of width $`L`$ in each of $`r_U`$ coordinates has coherence at most $`r_U\log_2L`$ and a full padded dimension proportional to $`L^{r_U}`$. Both channel errors remain of order $`L^{-2}`$. Thus taking $`L`$ proportional to $`\varepsilon^{-1/2}`$ yields achievable leading coefficients $`r_U/2`$ for coherence and logarithmic dimension.

An untouched spectator level contributes no new active transition. A gate that mixes only the first two levels of $`(0,1,\sqrt2)`$ can therefore use a one-frequency battery while meeting the same accuracy guarantee for arbitrary input coherences with the spectator. The [worked examples](../science/examples.md) and [M13–M18](MILESTONES.md#m13) make these distinctions precise.

## 7. Why another battery cannot improve the leading coefficient

The packet construction is an upper bound: it exhibits one family of admissible controllers. The lower bound must cover every finite battery state and Hamiltonian, including mixed and degenerate alternatives.

Exact conservation supplies the connection. If the battery's time origin changes, the same interaction approximates the correspondingly conjugated target gate with the same error,

```math
\beta_t=e^{-itH_B}\beta e^{itH_B},
\qquad
U_t=e^{-itH}Ue^{itH}.
```

A finite collection of these time labels becomes a collection of battery programs. The information recoverable from those programs is at most the battery's entropic coherence. This is a mixed-state statement, obtained by combining the finite-ensemble relative-entropy identity with the Holevo bound.

The gate orbit has $`r_U`$ locally distinguishable phase coordinates. A precise geometric packing, together with known recycling and parallel-estimation results, makes many of its labels decodable from one battery program. Fano's inequality then forces enough information to have been present initially. All programs use actual time translates; the proof does not require independently adjustable phase rotations of the competitor battery.

The [converse](../science/coherence_converse.md) carries out this argument with explicit error budgets. For fixed positive rank and sufficiently small $`\varepsilon`$, it gives

```math
C(\beta,H_B)
\ge\frac{r_U}{2}\log_2(1/\varepsilon)
-\frac{3r_U}{2}\log_2\log_2(1/\varepsilon)
-O_{H,U}(1).
```

Since $`C\le\log_2\dim B`$ for every finite battery, this also constrains the total dimension. The known programming, asymmetry, recycling, and estimation ingredients are explicitly credited in the [source bridge](ANCHOR_BRIDGE.md#beyond-the-anchor) and [related work](../references/RELATED_WORK.md). Follow [M19–M23](MILESTONES.md#m19) for this branch of the proof.

## 8. The combined conclusion and its physical limits

The lower bound and construction have the same leading coefficient. For either accuracy metric, their combination gives

```math
C_{\min}^{(e)}(\varepsilon)
=\frac{r_U}{2}\log_2(1/\varepsilon)
+O_{H,U}(\log\log(1/\varepsilon)),
\qquad
D_{\min}^{(e)}(\varepsilon)
=\varepsilon^{-r_U/2+o(1)}.
```

These are separate resource optimizations, as defined in the [model](../science/model.md#4-exact-statement-of-the-resource-law). The dimension statement fixes a leading exponent and retains a polylogarithmic gap in its explicit bounds. If $`r_U=0`$, the gate commutes with the Hamiltonian and can be implemented exactly with a one-dimensional, zero-coherence battery.

The exact Hamiltonian and gate remain fixed before taking the small-error limit. Rational approximants or vanishing gate angles can change the crossover constants, so this asymptotic rank is not a uniform finite-accuracy sensitivity claim. The finite construction also achieves mean energy $`O_{H,U}(\varepsilon^{-1/2})`$; that achieved scaling does not establish an energy optimum or a bound on preparation and interaction time.

The [last three milestones](MILESTONES.md#m28) connect the theorem to these examples, resource distinctions, and its contribution relative to prior work. The [verification suite](../verification/README.md) builds finite global unitaries and compares their channels with an independent overlap formula. Its calculations make the construction inspectable, while the converse and general construction establish the resource law.
