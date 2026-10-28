# Learning map: coherence for finite quantum control

This map organizes the scientific understanding needed to follow the [resource theorem](../science/model.md#4-exact-statement-of-the-resource-law): for a fixed Hamiltonian and gate, the rational rank of the active energy transitions fixes the leading coherence requirement and the leading exponent of the minimum battery dimension.

There are exactly **30 milestones**, with stable IDs **M01 through M30**. The first **12** build the background from quantum states and physical operations to the complete resource model. The remaining **18** follow the argument from the gate's active frequencies through the information converse and finite construction to their common conclusion. This allocation gives the several prerequisite areas enough room while placing most of the map on the project's mechanism, contribution, and limits.

The selected educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [anchor bridge](ANCHOR_BRIDGE.md) identifies the relevant sections, translates conventions, and supplies the connections that the book does not develop. Source pointers below distinguish those foundations, the project's own derivations, and specialized research theorems. The canonical statements and detailed calculations remain in [science/](../science/model.md); the map identifies their conceptual structure.

## Route through the story

| Phase | Milestones | Scientific role |
|---|---|---|
| Background/preliminaries | [M01](#m01) to [M06](#m06) | States, operations, energy conservation, and accuracy on every input |
| Background/preliminaries | [M07](#m07) to [M12](#m12) | Information, frequency coordinates, and the complete optimization problem |
| Narrative/innovation | [M13](#m13) to [M18](#m18) | The active gate orbit and the number of distinguishable phase choices |
| Narrative/innovation | [M19](#m19) to [M23](#m23) | Why every finite mixed battery must contain enough coherence |
| Narrative/innovation | [M24](#m24) to [M27](#m27) | A finite conserving battery that attains both accuracy scalings |
| Narrative/innovation | [M28](#m28) to [M30](#m30) | The matching law, its examples, and its physical meaning |

Dependencies below name earlier understanding targets. Each phase ends by assembling its components into a global account. All logarithms used for entropy and resource bounds are base two.

## Background/preliminaries

<a id="m01"></a>

### M01. Quantum states and an external reference

**Phase:** Background/preliminaries.

**Central question:** What must a gate preserve when its input may be part of a larger quantum system?

**Understanding target:** Distinguish pure states, mixed states, reduced states, and purifications. Explain how a mixed system state can arise from a pure state entangled with a reference, and why the unknown system-reference input can be correlated internally while remaining independent of the battery.

**Dependencies and story role:** This is the starting point. It identifies the physical objects that later accuracy guarantees must cover.

**Conceptual connection:** The allowed input has the form $`\rho_{SA}\otimes\beta_B`$. Following the reference through the argument gives operational meaning to a gate that works on every input.

**Source pointers:** [Watrous, Sections 2.1.2 and 2.1.3, through the states bridge](ANCHOR_BRIDGE.md#states-and-channels); [model, Section 1](../science/model.md#1-system-gate-and-implementation).

<a id="m02"></a>

### M02. Channels, dilations, and Choi states

**Phase:** Background/preliminaries.

**Central question:** How can a joint unitary produce a noisy operation on the system alone?

**Understanding target:** Relate a channel to a unitary or isometric dilation, a partial trace, and a Kraus representation. Interpret the Choi operator as the channel's action on one half of a maximally entangled input. Distinguish Watrous's unnormalized Choi operator from the normalized Choi state used here.

**Dependencies and story role:** Uses [M01](#m01). It moves from descriptions of states to equivalent descriptions of their physical transformations.

**Conceptual connection:** The actual channel is obtained by tracing out the battery, while the target unitary has a pure normalized Choi state. These descriptions support both the converse and the construction.

**Source pointers:** [Watrous, Sections 2.2.1 and 2.2.2, Eq. (2.65) and Corollary 2.27](ANCHOR_BRIDGE.md#states-and-channels); [notation bridge](ANCHOR_BRIDGE.md#notation); [model, Section 1](../science/model.md#1-system-gate-and-implementation).

<a id="m03"></a>

### M03. Energy eigenspaces and exact conservation

**Phase:** Background/preliminaries.

**Central question:** How can a gate change the system's energy while the complete operation conserves energy?

**Understanding target:** Interpret a Hamiltonian through its energies and spectral projections. Distinguish an energy eigenspace from a particular choice of basis within it. Explain that $`[V,H+H_B]=0`$ preserves total-energy sectors while allowing compensating transfers between system and battery.

**Dependencies and story role:** Uses [M01](#m01) and [M02](#m02). It adds the physical restriction that turns ordinary channel implementation into a resource question.

**Conceptual connection:** The blocks $`\Pi_EU\Pi_F`$ identify which energy changes a gate uses. Degeneracy and total-energy sectors will later matter for both the definition of rank and global unitarity.

**Source pointers:** [Bridge from channels to conservation](ANCHOR_BRIDGE.md#conservation-and-active-frequencies); [model, Section 1](../science/model.md#1-system-gate-and-implementation); [examples, Section 4](../science/examples.md#4-degeneracy-is-treated-by-spectral-blocks).

<a id="m04"></a>

### M04. Energy dephasing and a phase reference

**Phase:** Background/preliminaries.

**Central question:** Which parts of a battery state change when its time origin changes?

**Understanding target:** Explain energy dephasing as removal of matrix blocks between distinct battery energies. Recognize that coherence within a degenerate eigenspace survives this operation and does not change under time translation. Relate invariance under time translation to the absence of a usable energy phase reference.

**Dependencies and story role:** Uses [M01](#m01) and [M03](#m03). It identifies the physical property that the resource model will quantify.

**Conceptual connection:** A time-translated battery can encode a time-origin label only through coherence between different energies. This prepares the physical meaning of asymmetry before [M07](#m07) assigns it an entropy.

**Source pointers:** [Conservation and active-frequency bridge](ANCHOR_BRIDGE.md#conservation-and-active-frequencies); [model, energy dephasing in Section 2](../science/model.md#2-coherence-and-accuracy); [interpretation, phase information](../science/interpretation.md#conservation-exposes-the-information-stored-by-the-battery).

<a id="m05"></a>

### M05. Fidelity and distinguishability of states

**Phase:** Background/preliminaries.

**Central question:** What does it mean for an actual quantum output to be close to an ideal one?

**Understanding target:** Explain trace distance as a bound on measurement probability differences and fidelity as overlap after suitable purification. Translate Watrous's root fidelity $`F_{\mathrm W}`$ into this repository's squared fidelity $`F=F_{\mathrm W}^2`$. Recognize the special simplifications when the ideal output is pure.

**Dependencies and story role:** Uses [M01](#m01) and [M02](#m02). It supplies state-level accuracy concepts before channel-level optimization.

**Conceptual connection:** A test onto an ideal pure state converts infidelity into a probability difference. Purification and fidelity monotonicity later turn an isometry estimate into a guarantee after the battery is discarded.

**Source pointers:** [Watrous, Definition 3.11, Theorem 3.22 in Section 3.2.2, and Theorem 3.33 in Section 3.2.3](ANCHOR_BRIDGE.md#accuracy-conventions); [model, Section 2](../science/model.md#2-coherence-and-accuracy).

<a id="m06"></a>

### M06. Accuracy of a channel on every input

**Phase:** Background/preliminaries.

**Central question:** How does a guarantee for a few states differ from a guarantee for an unknown input entangled with a reference?

**Understanding target:** Explain why channel comparison must allow a reference. Distinguish the full diamond norm from the half-diamond error $`\delta`$, and distinguish both from the worst-case squared-fidelity infidelity $`\epsilon_F`$. Interpret $`\epsilon_F\le\delta\le\sqrt{\epsilon_F}`$ without identifying the metrics.

**Dependencies and story role:** Uses [M02](#m02) and [M05](#m05). It completes the accuracy language required by the resource optimization.

**Conceptual connection:** A bound $`\epsilon_F=O(L^{-2})`$ alone gives only $`\delta=O(L^{-1})`$ through the generic inequality. Establishing the same resource exponent for both tolerances will require a separate channel estimate.

**Source pointers:** [Watrous, Sections 3.3.2 and 3.3.3, Definition 3.43 and Theorems 3.46 and 3.51](ANCHOR_BRIDGE.md#accuracy-conventions); [model, accuracy conventions](../science/model.md#2-coherence-and-accuracy).

<a id="m07"></a>

### M07. Entropy, relative entropy, and coherence cost

**Phase:** Background/preliminaries.

**Central question:** How can the battery's phase-reference resource be measured in bits?

**Understanding target:** Interpret entropy, relative entropy, and nonnegativity of relative entropy. Connect energy dephasing to the identity $`C(\beta,H_B)=D(\beta\Vert\Delta_{H_B}\beta)=S(\Delta_{H_B}\beta)-S(\beta)`$. Explain why this counts coherence between distinct energies and satisfies $`0\le C\le\log_2\dim B`$ for arbitrary finite mixed states.

**Dependencies and story role:** Uses [M01](#m01) and [M04](#m04). It assigns a quantitative resource to the physical phase information already identified.

**Conceptual connection:** The resource is an initial stock of coherence. Its upper bound by the logarithm of dimension will later convert an information converse into a controller-size lower bound.

**Source pointers:** [Watrous, Section 5.2.1, Definitions 5.17 and 5.18, and Proposition 5.22 in Section 5.2.2](ANCHOR_BRIDGE.md#entropy-and-information); [model, coherence definition](../science/model.md#2-coherence-and-accuracy); [Gour, Marvian, and Spekkens](../references/RELATED_WORK.md#gour2009).

<a id="m08"></a>

### M08. From distinguishable messages to an information requirement

**Phase:** Background/preliminaries.

**Central question:** What does successful recovery of a label imply about the information contained in the states that encode it?

**Understanding target:** Distinguish an ensemble label, a measurement outcome, mutual information, and Holevo information. Explain why label-independent processing cannot increase accessible information. Interpret the general finite-message Fano bound as a relation between decoding error, message count, and retained information.

**Dependencies and story role:** Uses [M05](#m05) and [M07](#m07). It connects an operational discrimination experiment to an entropy lower bound.

**Conceptual connection:** The converse will encode a finite set of time labels in one battery. Holevo bounds information from above; Fano bounds it from below once those labels can be decoded.

**Source pointers:** [Watrous, Sections 5.1.1 and 5.1.2, Theorem 5.35 in Section 5.2.3, and Theorem 5.49 in Section 5.3.3; local general-message Fano bridge](ANCHOR_BRIDGE.md#entropy-and-information); [converse, orbit information](../science/coherence_converse.md#2-orbit-information-is-bounded-by-entropic-coherence) and [finite-error decoding bound](../science/coherence_converse.md#5-finite-error-converse). Watrous's Lemma 5.54 is a binary Fano statement; the bridge supplies the form used here.

<a id="m09"></a>

### M09. Covariance as a family of gate programs

**Phase:** Background/preliminaries.

**Central question:** Why does changing the battery's time origin change which gate the same interaction approximately implements?

**Understanding target:** Relate additive conservation to covariance under simultaneous time translation. Explain how one fixed interaction maps $`\beta_t`$ to the conjugated target $`U_t=e^{-itH}Ue^{itH}`$, with the same accuracy. Identify the program state as the carrier of the unknown label.

**Dependencies and story role:** Uses [M02](#m02), [M03](#m03), [M04](#m04), and [M06](#m06). It joins the physical conservation rule to the information language of [M08](#m08).

**Conceptual connection:** The lower bound will study a family of time-translated programs even though the original task asks for one fixed target gate. The family is forced by conservation.

**Source pointers:** [Bridge from conservation to programming](ANCHOR_BRIDGE.md#conservation-and-active-frequencies); [converse, Lemma 1](../science/coherence_converse.md#1-covariance-generates-an-orbit-of-programs); [Marvian and Spekkens](../references/RELATED_WORK.md#marvian2012).

<a id="m10"></a>

### M10. Independent frequencies and integer coordinates

**Phase:** Background/preliminaries.

**Central question:** When do several energy gaps require one phase coordinate, and when do they require several?

**Understanding target:** Distinguish integer span, rational span, and rational independence of a finite set of real frequencies. Explain how a basis of the generated integer group gives exact integer coordinates. Recognize why a rank based on exact rational relations cannot be inferred from rounded numerical energies.

**Dependencies and story role:** Uses [M03](#m03) and [M09](#m09). It supplies the mathematical language for counting the independent phases exposed by conservation.

**Conceptual connection:** The same coordinates will describe the gate's phase orbit and the battery's allowed energy shifts. Rational rank measures independent frequency information, rather than the number of system levels.

**Source pointers:** [Locally supplied frequency-lattice bridge](ANCHOR_BRIDGE.md#conservation-and-active-frequencies); [transition group and coordinates, Sections 1 and 2](../science/transition_rank.md#1-the-active-transition-group); [qutrit comparison](../science/examples.md#2-two-three-level-spectra-give-different-controller-exponents).

<a id="m11"></a>

### M11. Metrics, separated sets, and decoding

**Phase:** Background/preliminaries.

**Central question:** How does the geometry of a family of gates determine how many different labels can be resolved?

**Understanding target:** Interpret a metric packing as a finite collection of mutually separated points. Explain the local grid count in several coordinates and why an estimate closer than half the separation identifies its nearest point uniquely. Keep the geometric separation problem distinct from the experiment that achieves an estimation accuracy.

**Dependencies and story role:** Uses [M05](#m05), [M08](#m08), and [M10](#m10). It connects continuous phase coordinates to a finite-message information argument.

**Conceptual connection:** Choi-state trace distance supplies the triangle inequality needed for decoding. The narrative must still prove that the gate family has a positive metric in every active direction.

**Source pointers:** [Watrous's state-distance foundations](ANCHOR_BRIDGE.md#accuracy-conventions) and [local geometric bridge](ANCHOR_BRIDGE.md#beyond-the-anchor); [transition rank, local metric](../science/transition_rank.md#5-a-positive-local-choi-metric) and [packing](../science/transition_rank.md#6-finite-packings-using-actual-times); [converse, finite packing decoder](../science/coherence_converse.md#4-a-finite-packing-can-be-decoded-from-one-battery).

<a id="m12"></a>

### M12. The complete fixed-gate resource problem

**Phase:** Background/preliminaries.

**Central question:** What is being minimized, over which implementations, and under which physical and accuracy assumptions?

**Understanding target:** Assemble the system, target, battery, conserving interaction, independent initial input, coherence measure, and two accuracy conventions into one model. Distinguish the coherence optimum from the dimension optimum, allowing different minimizers. State that $`H,U,d`$ remain fixed as the tolerance decreases and that all finite mixed batteries and spectra are eligible.

**Dependencies and story role:** Integrates [M01](#m01) through [M11](#m11). It closes the background phase by turning its separate objects into a precise global question.

**Conceptual connection:** A lower bound must cover every allowed implementation, while an upper bound needs one explicit family. No original battery-return, time, locality, or preparation-efficiency constraint is part of these optimizations.

**Source pointers:** [Anchor bridge and notation](ANCHOR_BRIDGE.md#notation); [model, Sections 1 through 4](../science/model.md); [model scope](../science/model.md#6-reading-and-scope).

## Narrative/innovation

<a id="m13"></a>

### M13. The rank of the transitions the gate actually uses

**Phase:** Narrative/innovation.

**Central question:** Which part of the Hamiltonian's spectrum controls this gate's coherence requirement?

**Understanding target:** Form the active set from the nonzero blocks $`\Pi_EU\Pi_F`$ and define its rational rank $`r_U`$. Explain why inactive levels can raise the rank of the full spectrum without raising $`r_U`$, and why the block definition is independent of basis choices within degeneracies.

**Dependencies and story role:** Uses [M03](#m03), [M10](#m10), and [M12](#m12). It identifies the project-specific invariant from which both proof branches start.

**Conceptual connection:** Selecting only active transitions replaces a spectrum-wide count by a gate-specific count of usable phase coordinates.

**Source pointers:** [Frequency bridge](ANCHOR_BRIDGE.md#conservation-and-active-frequencies); [transition rank, Section 1](../science/transition_rank.md#1-the-active-transition-group); [spectator example](../science/examples.md#3-an-inactive-level-does-not-create-a-new-requirement).

<a id="m14"></a>

### M14. Active components, coordinates, and the zero-rank case

**Phase:** Narrative/innovation.

**Central question:** How can the active gaps describe every relevant energy difference without introducing unnecessary frequencies?

**Understanding target:** Explain the invariant components of the energy-support graph and the representation $`E=E_c+s_E\cdot\omega`$ within each component. Understand why component offsets cancel in gate conjugation. Establish that rank zero is exactly $`[H,U]=0`$ and permits a one-dimensional battery with zero coherence.

**Dependencies and story role:** Uses [M10](#m10) and [M13](#m13). It turns the active rank into concrete coordinates and resolves the exact, resource-free endpoint before treating positive rank.

**Conceptual connection:** These coordinates will serve both the torus description and finite energy-block construction. Component decomposition restricts the gate, without restricting unknown inputs to a single component.

**Source pointers:** [Frequency bridge](ANCHOR_BRIDGE.md#conservation-and-active-frequencies); [transition rank, Proposition 1 and Section 2](../science/transition_rank.md#2-integer-coordinates-on-each-active-component); [construction, Section 1](../science/battery_construction.md#1-integer-coordinates-for-the-transitions).

<a id="m15"></a>

### M15. A dense orbit generated by actual time translations

**Phase:** Narrative/innovation.

**Central question:** How can one real time parameter generate a gate family with several independent local phase coordinates?

**Understanding target:** Explain why rational independence makes $`t\omega`$ dense in an $`r_U`$-dimensional torus as actual nonnegative times vary. Relate the vanishing averages of nonconstant Fourier characters to that density. Distinguish the orbit's closure from a bound on the time required to approach a point.

**Dependencies and story role:** Uses [M09](#m09), [M10](#m10), and [M14](#m14). It connects the available one-parameter family of physical programs to the geometry needed by the converse.

**Conceptual connection:** The proof can choose a finite collection of actual battery time translations. It does not assume independently adjustable battery phases or a bound on the battery's frequency rank.

**Source pointers:** [Locally supplied orbit argument](ANCHOR_BRIDGE.md#beyond-the-anchor); [transition rank, Lemma 2](../science/transition_rank.md#3-closure-of-the-actual-time-orbit); [interpretation of time labels](../science/interpretation.md#one-laboratory-time-can-encode-several-phase-coordinates).

<a id="m16"></a>

### M16. Global phase and the physical gate orbit

**Phase:** Narrative/innovation.

**Central question:** Does identifying unitary matrices that differ only by global phase reduce the number of active coordinates?

**Understanding target:** Distinguish a matrix orbit from its unitary-channel orbit. Explain why active integer vectors give a trivial matrix stabilizer and why a channel stabilizer can have only finitely many elements, at most $`d`$. Understand why a finite identification leaves the local dimension unchanged.

**Dependencies and story role:** Uses [M02](#m02), [M13](#m13), [M14](#m14), and [M15](#m15). It ensures the orbit count concerns physically distinct channels.

**Conceptual connection:** For a qubit bit flip, a half-period changes the matrix sign without changing the channel. This reduces a global period but leaves the one-dimensional local phase sensitivity intact.

**Source pointers:** [Channel conventions and local orbit bridge](ANCHOR_BRIDGE.md#beyond-the-anchor); [transition rank, Proposition 3](../science/transition_rank.md#4-global-phase-leaves-the-orbit-dimension-unchanged); [bit-flip example](../science/examples.md#5-a-finite-projective-stabilizer-leaves-the-rank-intact).

<a id="m17"></a>

### M17. A positive Choi metric in every active direction

**Phase:** Narrative/innovation.

**Central question:** Why does each active frequency produce a locally distinguishable change in the gate?

**Understanding target:** Interpret the normalized Choi overlap as a weighted sum of the active phases. Explain how unitarity gives zero mean for the active integer vectors and how their spanning property makes the covariance $`\Sigma`$ positive definite. Relate this to the local expansion $`d_{\mathrm{Ch}}^2=\phi^{\mathsf T}\Sigma\phi+O(\|\phi\|^4)`$.

**Dependencies and story role:** Uses [M02](#m02), [M05](#m05), [M11](#m11), [M13](#m13), and [M16](#m16). It replaces parameter counting by a quantitative statement about distinguishability.

**Conceptual connection:** Positivity provides fixed local comparison constants between coordinate distance and Choi distance, including degenerate spectral blocks.

**Source pointers:** [Normalized Choi and fidelity conventions](ANCHOR_BRIDGE.md#notation); [local additions beyond the anchor](ANCHOR_BRIDGE.md#beyond-the-anchor); [transition rank, Section 5](../science/transition_rank.md#5-a-positive-local-choi-metric).

<a id="m18"></a>

### M18. A finite packing made from actual gates

**Phase:** Narrative/innovation.

**Central question:** How can local phase geometry supply many separated programs without inventing a larger control action on the battery?

**Understanding target:** Combine a small coordinate grid, the positive local metric, and actual-time density to obtain separated gates $`U_{t_j}`$. Explain why approximating each grid point closely enough preserves separation and yields $`M\ge c_{\mathrm{pack}}\eta^{-r_U}`$ at Choi separation $`\eta`$.

**Dependencies and story role:** Uses [M11](#m11), [M15](#m15), and [M17](#m17). It completes the geometric part of the converse with a finite ensemble ready for an information experiment.

**Conceptual connection:** Only the fixed system gate orbit is packed. The corresponding battery states are actual time translates of whatever finite mixed battery the competitor supplies.

**Source pointers:** [Local geometric bridge](ANCHOR_BRIDGE.md#beyond-the-anchor); [transition rank, Theorem 4](../science/transition_rank.md#6-finite-packings-using-actual-times); [converse, Section 4](../science/coherence_converse.md#4-a-finite-packing-can-be-decoded-from-one-battery).

<a id="m19"></a>

### M19. The orbit-information bound for an arbitrary mixed battery

**Phase:** Narrative/innovation.

**Central question:** Why can no ensemble of battery time translates reveal more information than the battery's entropic coherence?

**Understanding target:** Explain the finite-ensemble identity $`C=\chi+D(\bar\beta\Vert\Delta_{H_B}\beta)`$ and use nonnegativity to obtain $`\chi\le C`$. Understand why mixedness, energy degeneracy, and a nonuniform selection of actual times do not invalidate the argument.

**Dependencies and story role:** Uses [M07](#m07), [M08](#m08), [M09](#m09), and [M18](#m18). It puts a universal information ceiling on every allowed battery.

**Conceptual connection:** Any fixed decoder with label-independent auxiliary states remains subject to this ceiling. The argument requires no entropy-continuity estimate on a growing output space.

**Source pointers:** [Watrous's relative entropy, data processing, and Holevo foundations](ANCHOR_BRIDGE.md#entropy-and-information); [converse, Lemma 2](../science/coherence_converse.md#2-orbit-information-is-bounded-by-entropic-coherence); [Gour, Marvian, and Spekkens attribution](../references/RELATED_WORK.md#gour2009).

<a id="m20"></a>

### M20. Recycling one approximate gate program

**Phase:** Narrative/innovation.

**Central question:** How can a single accurate battery program support the many gate calls needed by the decoding experiment?

**Understanding target:** Given $`\epsilon_F\le\varepsilon`$, state the imported paired-recycling guarantee for alternating $`V`$ and $`V^\dagger`$: full diamond error at most $`8m\sqrt{\varepsilon}`$ relative to $`(U\otimes U^\dagger)^{\otimes m}`$ with the battery returned in the comparison state. After discarding the even registers and battery, interpret the output trace-distance bound $`4m\sqrt{\varepsilon}`$.

**Dependencies and story role:** Uses [M02](#m02), [M06](#m06), [M09](#m09), and [M19](#m19). It supplies the first specialized research ingredient in the decoder.

**Conceptual connection:** The original implementation need not return its mixed battery. The fixed paired circuit is a lower-bound experiment, not an assumption of unlimited independent reuse.

**Source pointers:** [Research ingredients beyond Watrous](ANCHOR_BRIDGE.md#beyond-the-anchor); [converse, Lemma 3](../science/coherence_converse.md#lemma-3-paired-recycling); [Castellano et al., Theorem 9, Eq. (60), version 2](../references/RELATED_WORK.md#castellano2026); [Chiribella, Yang, and Renner](../references/RELATED_WORK.md#chiribella2021).

<a id="m21"></a>

### M21. Universal estimation and the Choi-risk conversion

**Phase:** Narrative/innovation.

**Central question:** What estimation precision can the emulated parallel gate calls achieve, uniformly over the encoded gate?

**Understanding target:** State the imported fixed-probe, fixed-measurement estimator with expected squared Choi distance at most $`K_d/m^2`$ for $`m\ge2d(d-1)`$, where $`K_d`$ depends only on system dimension. Explain how the source's measure-and-operate half-diamond bound implies this risk bound by testing the pure ideal Choi state.

**Dependencies and story role:** Uses [M02](#m02), [M05](#m05), [M06](#m06), and [M20](#m20). It supplies the quantitative resolving power that turns the geometric packing into readable messages.

**Conceptual connection:** Uniformity keeps the experiment independent of the unknown label. Choosing a special-unitary representative changes no channel or Choi distance, so global phase creates no estimation loophole.

**Source pointers:** [Accuracy conventions](ANCHOR_BRIDGE.md#accuracy-conventions) and [research-level estimation bridge](ANCHOR_BRIDGE.md#beyond-the-anchor); [converse, Lemma 4](../science/coherence_converse.md#lemma-4-parallel-unitary-estimation); [Yang, Renner, and Chiribella, Theorem 2 and Appendix B](../references/RELATED_WORK.md#yang2020).

<a id="m22"></a>

### M22. Combining packing, estimation, recycling, and Fano

**Phase:** Narrative/innovation.

**Central question:** How do the geometric and operational errors combine into a finite-error coherence bound?

**Understanding target:** Explain nearest-point decoding at separation $`a/m`$. Identify the two contributions to $`q=4K_d/a^2+4m\sqrt{\varepsilon}`$: ideal estimation error and imperfect recycling. Use Holevo and Fano to interpret the bound $`C\ge(1-q)[r_U\log(m/a)+\log c_{\mathrm{pack}}]-h_2(q)`$ under the stated packing, estimator, and $`q\le1/2`$ conditions.

**Dependencies and story role:** Uses [M08](#m08), [M18](#m18), [M19](#m19), [M20](#m20), and [M21](#m21). It assembles the separate converse ingredients into one finite-parameter statement.

**Conceptual connection:** More available messages increase the required coherence, while both estimation uncertainty and recycling error reduce the information that can be certified.

**Source pointers:** [Local general-message Fano bridge](ANCHOR_BRIDGE.md#entropy-and-information); [converse, Section 4 and Theorem 5](../science/coherence_converse.md#5-finite-error-converse).

<a id="m23"></a>

### M23. The logarithmic converse and the dimension lower bound

**Phase:** Narrative/innovation.

**Central question:** How does the finite-message argument produce one half of a logarithm per active frequency?

**Understanding target:** Explain the parameter balance $`m\sim\varepsilon^{-1/2}/\log(1/\varepsilon)`$ and $`a\sim\sqrt{\log(1/\varepsilon)}`$. Track the leading coefficient $`r_U/2`$ and the proved negative correction $`(3r_U/2)\log\log(1/\varepsilon)`$. Transfer the result to battery dimension through $`C\le\log d_B`$ and to half-diamond accuracy through $`\epsilon_F\le\delta`$.

**Dependencies and story role:** Uses [M06](#m06), [M07](#m07), and [M22](#m22). It completes the lower-bound branch for all finite mixed competitors.

**Conceptual connection:** The converse fixes a leading coefficient and exponent, while retaining logarithmic corrections. Achievability and any matching conclusion still require an explicit conserving implementation.

**Source pointers:** [Information and accuracy conventions](ANCHOR_BRIDGE.md#notation); [converse, Corollary 6](../science/coherence_converse.md#6-the-leading-logarithmic-requirement); [half-diamond transfer and zero rank](../science/coherence_converse.md#7-half-diamond-accuracy-and-the-zero-rank-case).

<a id="m24"></a>

### M24. A positive finite sine lattice and its resources

**Phase:** Narrative/innovation.

**Central question:** What battery can carry the independent phase references while keeping its dimension and coherence controlled?

**Understanding target:** Build a finite box in the active integer coordinates with positive basis frequencies and a product sine packet of width $`L`$. Explain why rational independence makes total battery energies nondegenerate. Relate packet entropy, the complete box dimension, and mean energy to $`r_UH(p_L)`$, $`(L+2K+2)^{r_U}`$, and a quantity linear in $`L`$, respectively.

**Dependencies and story role:** Uses [M03](#m03), [M07](#m07), [M10](#m10), [M12](#m12), and [M14](#m14). It starts the constructive branch from the same active coordinates as the converse.

**Conceptual connection:** The populated packet and the full padded Hilbert space have different sizes. The entropy is that of total energy, with the fixed margin $`K`$ chosen from all coordinate differences within each active component.

**Source pointers:** [Frequency and entropy conventions](ANCHOR_BRIDGE.md#notation); [construction, Sections 1 and 2](../science/battery_construction.md#2-battery-hamiltonian-and-reference-state); [coherent-shift antecedent](../references/RELATED_WORK.md#aberg2014).

<a id="m25"></a>

### M25. Completing the conserving unitary at every boundary

**Phase:** Narrative/innovation.

**Central question:** How can a finite battery implement the desired shifts without requiring an infinite translation operator?

**Understanding target:** Organize the entire joint basis into refined blocks labeled by an active component and total integer coordinate. Apply the target gate on complete blocks and identity on incomplete blocks. Explain why an all-pair margin makes every block reached from the initial packet complete, and why coincident physical energies of different refined blocks cause no obstruction.

**Dependencies and story role:** Uses [M02](#m02), [M03](#m03), [M14](#m14), and [M24](#m24). It turns the proposed packet and shifts into a global finite unitary.

**Conceptual connection:** Exact conservation and unitarity hold on the whole Hilbert space. The input may remain coherent across components or entangled with a reference.

**Source pointers:** [Dilation foundations](ANCHOR_BRIDGE.md#states-and-channels) and [local construction bridge](ANCHOR_BRIDGE.md#beyond-the-anchor); [construction, Section 3](../science/battery_construction.md#3-a-global-unitary-including-the-boundary); [finite block verification](../verification/README.md#exact-energy-representation).

<a id="m26"></a>

### M26. From a smooth packet to reference-assisted infidelity

**Phase:** Narrative/innovation.

**Central question:** Why does a packet whose vector changes by order $`L^{-1}`$ give gate infidelity of order $`L^{-2}`$?

**Understanding target:** Relate the one-step sine overlap to a norm estimate for every fixed integer shift. Follow this estimate through the implementing isometry, tensoring with an arbitrary reference, and comparison with the ideal product isometry. Explain how squared overlap and tracing out the battery give $`\epsilon_F\le A_{\mathrm{iso}}^2/(L+1)^2`$ when this is below the trivial bound.

**Dependencies and story role:** Uses [M01](#m01), [M05](#m05), [M06](#m06), [M24](#m24), and [M25](#m25). It proves the first of the two constructive accuracy statements.

**Conceptual connection:** Watrous's root-fidelity convention must be squared consistently here. The reference guarantee follows from a uniform operator-norm estimate, rather than from sampling system inputs.

**Source pointers:** [Fidelity translation and purification](ANCHOR_BRIDGE.md#accuracy-conventions); [construction, translation estimates](../science/battery_construction.md#4-translation-estimates-for-the-packet) and [reference-assisted infidelity](../science/battery_construction.md#5-reference-assisted-infidelity).

<a id="m27"></a>

### M27. The real-overlap kernel and the diamond bound

**Phase:** Narrative/innovation.

**Central question:** Why does the stronger channel criterion also have quadratic inverse-width error?

**Understanding target:** Derive the role of the real translation overlaps in the reduced channel. Explain why $`1-g_v=\|(T^v-I)b_L\|^2/2`$ makes each relevant coefficient error of order $`L^{-2}`$. Combine these coefficients with the unit diamond norm of elementary matrix maps to obtain full diamond error at most $`B_{\mathrm{ch}}/(L+1)^2`$, and half that bound for $`\delta`$.

**Dependencies and story role:** Uses [M02](#m02), [M06](#m06), [M25](#m25), and [M26](#m26). It completes the constructive accuracy argument for the second optimization.

**Conceptual connection:** The real-kernel calculation supplies information lost by a generic isometry-to-diamond conversion. It is the step that makes both metrics share the same achievable exponent.

**Source pointers:** [Watrous's completely bounded trace norm and convention bridge](ANCHOR_BRIDGE.md#accuracy-conventions); [construction, Section 6](../science/battery_construction.md#6-diamond-distance-from-the-reduced-channel); [interpretation of the numerical bounds](../verification/README.md#fidelity-and-diamond-quantities).

<a id="m28"></a>

### M28. Matching the lower and upper resource laws

**Phase:** Narrative/innovation.

**Central question:** What exactly becomes optimal when the converse and the finite construction meet?

**Understanding target:** Choose the packet width for each accuracy metric and combine [M23](#m23) with [M24](#m24) through [M27](#m27). Explain why both $`C_{\min}^{(e)}(\varepsilon)/\log_2(1/\varepsilon)`$ and $`\log_2D_{\min}^{(e)}(\varepsilon)/\log_2(1/\varepsilon)`$ tend to $`r_U/2`$. Retain the polylogarithmic dimension gap and the exact zero-rank endpoint.

**Dependencies and story role:** Integrates [M12](#m12), [M14](#m14), [M23](#m23), and [M24](#m24) through [M27](#m27). It joins the two proof branches into the principal theorem.

**Conceptual connection:** A particular pure lattice battery matches the leading lower bound for arbitrary finite mixed competitors. This does not establish a constant-factor dimension optimum or an optimal mean-energy law.

**Source pointers:** [Bridge to the project theorem](ANCHOR_BRIDGE.md#beyond-the-anchor); [model, exact resource law](../science/model.md#4-exact-statement-of-the-resource-law); [construction, resource consequences](../science/battery_construction.md#7-resource-consequences-and-limits).

<a id="m29"></a>

### M29. Examples, spectators, and the order of limits

**Phase:** Narrative/innovation.

**Central question:** How do concrete spectra and gates reveal both the theorem's content and its limits?

**Understanding target:** Compare a fully supported qutrit gate on commensurate and rationally independent spectra, and compare both with a gate that leaves an irrational-energy spectator inactive. Explain how degeneracy, small gate angles, and rational approximants affect the rank or fixed-object constants. Distinguish a fixed-spectrum asymptotic law from a joint limit in which the gate or spectrum also changes.

**Dependencies and story role:** Uses [M13](#m13), [M14](#m14), [M16](#m16), [M24](#m24), and [M28](#m28). It turns the global theorem into interpretable contrasts.

**Conceptual connection:** A discontinuous exact rank does not by itself imply a uniform finite-accuracy experimental discontinuity. The finite verification illustrates specified constructions while the analytic proof establishes the general optimum.

**Source pointers:** [Exact-spectrum bridge](ANCHOR_BRIDGE.md#conservation-and-active-frequencies); [worked examples](../science/examples.md); [verification scope and recorded results](../verification/README.md).

<a id="m30"></a>

### M30. Physical synthesis, contribution, and attribution

**Phase:** Narrative/innovation.

**Central question:** What does the complete argument teach about the physical resources of a quantum controller?

**Understanding target:** Explain the chain from conservation to phase information, from phase information to a coherence lower bound, and from smooth finite packets to matching accuracy. Distinguish initial coherence, dimension, mean energy, and repeated-use depletion. Identify the known asymmetry, programming, recycling, estimation, and finite-reference ingredients, and locate the contribution in the matching active-rank leading law for arbitrary finite mixed competitors.

**Dependencies and story role:** Integrates [M12](#m12), [M18](#m18) through [M23](#m23), and [M24](#m24) through [M29](#m29). It closes the narrative with the result's global meaning, scope, and relationship to earlier work.

**Conceptual connection:** The theorem concerns exact conservation and fixed finite systems with unrestricted finite controller architecture. It separates an initial information requirement from energy optimality, bounded-time control, preparation efficiency, and a claim of resource consumption on every use.

**Source pointers:** [What goes beyond the educational anchor](ANCHOR_BRIDGE.md#beyond-the-anchor); [physical interpretation](../science/interpretation.md); [attribution map](../references/RELATED_WORK.md#what-is-inherited-and-what-is-established-here); [earlier finite reference systems](../references/RELATED_WORK.md#popescu2018); [model scope](../science/model.md#6-reading-and-scope).
