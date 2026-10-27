# Why phase information fixes the controller size

The [resource law](model.md) assigns one leading half-logarithmic coherence requirement to each independent active energy frequency. It follows from a connection between exact conservation, the information contained in a phase reference, and the precision with which a finite quantum packet can tolerate energy shifts.

## Conservation exposes the information stored by the battery

Fix an interaction that conserves total energy and approximately implements $`U`$. Changing the initial battery's time origin changes the implemented gate to

```math
U_t=e^{-itH}Ue^{itH}.
```

The same hardware therefore reads a family of gate programs from the battery's time-translated states. Every coherence between distinct battery energies can carry information about that time origin. Coherence confined to one degenerate energy eigenspace cannot.

This programming view of symmetry restrictions and the accessible-information meaning of relative-entropy asymmetry are established ideas, attributed in [related work](../references/RELATED_WORK.md#gour2009). Their quantitative use here identifies the optimal coherence needed for a fixed gate. A precise implementation can be approximately recycled into many calls to the encoded gate. A suitable joint estimation experiment then distinguishes more phase choices than independent single-call probes would. The original battery must contain enough information to support that distinction.

Only a finite ensemble of actual time translations is used in the converse. The proof does not assume that the battery can be independently rotated along the target system's several phase coordinates. Rationally independent system frequencies make its real-time trajectory dense in the corresponding torus, which supplies the finite ensemble required for each accuracy.

## One laboratory time can encode several phase coordinates

The gate's phase changes have the form $`\exp[-it(E-F)]`$ on active spectral blocks. If all active gaps are integer multiples of one frequency, their phases trace a circle. If there are $`r_U`$ rationally independent generators, the closure of that trajectory has $`r_U`$ local coordinates.

This rank is an exact property of the gate and spectrum. It counts the independent frequency information accessible through the gate, even though the time translation is parametrized by one real number. The [positive local Choi metric](transition_rank.md) makes this statement quantitative: a small phase displacement changes the gate's normalized Choi state in every active direction.

The converse may choose large time labels to approximate a fine finite packing. These are a mathematical discrimination experiment in a coherence-only resource bound. The theorem does not price elapsed time or claim a uniform time needed to explore the phase orbit.

## Why a sine lattice matches the bound

To implement a transition $`F\to E`$, a conserving controller shifts its energy by $`F-E`$. A superposition of system transitions produces a superposition of such shifted controller packets. The gate remains close to a unitary on the system when these packets overlap strongly, so that the controller retains little information about which transition occurred.

The [construction](battery_construction.md) represents every active gap as an integer vector in $`r_U`$ frequency coordinates. It puts a smooth sine packet of width $`L`$ along each coordinate. Any required shift is fixed as $`L`$ grows, and changes the packet by $`O(L^{-1})`$ in vector norm. Infidelity is consequently $`O(L^{-2})`$. The real packet overlaps also give a reduced-channel diamond error of that order.

The packet uses $`L^{r_U}`$ populated energy levels. Their entropy is at most $`r_U\log_2 L`$. Choosing $`L`$ proportional to $`\varepsilon^{-1/2}`$ gives the leading coefficient $`r_U/2`$. A fixed margin surrounding the packet lets the construction act unitarily on the entire finite system-battery Hilbert space; no infinite ladder is hidden at its boundary.

## Coherence, dimension, and energy are different resources

The coherence converse optimizes over arbitrary finite mixed battery states. It does not assume that a pure packet or an energy lattice is optimal. The construction then attains its leading coefficient. This yields

```math
C_{\min}^{(e)}(\varepsilon)
=\frac{r_U}{2}\log_2(1/\varepsilon)
+O_{H,U}(\log\log(1/\varepsilon)).
```

Since entropic coherence is bounded by the logarithm of the battery dimension, the same argument fixes the minimum-dimension exponent. The matching statement is at the level of that exponent; the proved dimension bounds retain logarithmic factors.

The construction's mean energy grows as $`O_{H,U}(\varepsilon^{-1/2})`$ for every fixed rank. Higher rank instead raises the number of distinct energy combinations within the available range. Thus a scalar mean-energy budget does not describe the controller's full coherent-information requirement. The qutrit examples show this distinction with one and two active frequencies.

Entropic coherence measures an initial stock. The same battery can retain much of its coherence after one accurate gate, and the imported recycling theorem exploits this. Repeated-use depletion, correlations between successive outputs, and the cost of refreshing the controller are separate operational questions. They are not silently counted as one-gate consumption.

## Exactness and the order of limits

The main theorem fixes the gate and exact spectrum before decreasing the error. A rational relation can lower the active rank, and a gate entry becoming exactly zero can remove an active direction. Nearby finite-error problems can still behave continuously because the constants and crossover scales depend on those fixed objects. The [small-angle and rational-approximant examples](examples.md#6-what-the-fixed-gate-assumption-does) show why the order of limits matters.

The energy-conserving interaction is otherwise unrestricted. There is no bounded interaction time, locality, or computational-efficiency requirement, and the supplied spectrum is known exactly. A controller architecture with a fixed spectral density or restricted couplings is a smaller optimization class and may have a larger cost. The present construction answers the unrestricted finite-controller existence question under exact conservation.

The closest entropic-coherence work already establishes necessity and the qubit endpoint. The present account combines a converse valid for arbitrary mixed finite batteries with an explicit construction for general active spectra, producing a complete leading resource law. The [attribution map](../references/RELATED_WORK.md) separates that conclusion from the known asymmetry, programming, recycling, estimation, and sine-packet ingredients.
