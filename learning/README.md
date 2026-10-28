# Learn Quantum Control Coherence

An accurate quantum gate must preserve relative phases while it moves a system between energy levels. A finite controller can supply the required energy and phase reference, but its quantum state changes during the operation. This project asks how large and how coherent that controller must initially be when total energy is conserved exactly.

The learning route connects that physical task to the leading resource law. It uses one educational anchor: **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the selected source; the [anchor bridge](ANCHOR_BRIDGE.md) identifies the portions used here and translates their conventions. Read those selections as they become useful alongside the project explanations.

## Where to start

| Your question | Start here | Continue with |
|---|---|---|
| What does a coherent controller actually do? | [Worked controller tutorial](TUTORIAL.md) | [Physical interpretation](../science/interpretation.md) |
| How do the prerequisite ideas fit together? | [M01–M12: background/preliminaries](MILESTONES.md#backgroundpreliminaries) | [Watrous bridge](ANCHOR_BRIDGE.md) |
| How do the proofs establish the optimal law? | [M13–M30: narrative/innovation](MILESTONES.md#narrativeinnovation) | [Model and exact theorem](../science/model.md) and its linked proofs |
| Which textbook conventions need translation? | [Source bridge](ANCHOR_BRIDGE.md) | [Accuracy and coherence definitions](../science/model.md#2-coherence-and-accuracy) |
| What can be checked with a finite calculation? | [Verification guide](../verification/README.md) | [Recorded results](../verification/results.json) |

## One connected map

The [milestone map](MILESTONES.md) contains exactly **30 understanding targets**. The first 12 build from states and channels to conservation, operational accuracy, information, and the fixed-gate resource problem. The next 18 follow the active transition orbit, information converse, finite battery construction, and their joint physical meaning.

This allocation gives the two proof directions room to develop. A necessity argument must cover every allowed mixed finite battery. An achievable construction must define a conserving unitary on the whole finite Hilbert space, including its boundaries. Their assumptions and error conventions have to agree before their bounds can be combined.

Each milestone has a central question, an understanding target, earlier dependencies, a conceptual connection, and source pointers. The map is shared conceptual structure. It does not record a reader's attempts, results, or mastery.

## Keep the conventions visible

Three translations matter throughout the route:

- The project uses **squared fidelity**. Watrous's fidelity is its nonnegative square root.
- The project's channel error $`\delta`$ is **half** the diamond norm of the channel difference.
- The project's Choi states are **normalized**. The Choi operator in the selected book convention has trace equal to the input dimension for a channel.

The [bridge](ANCHOR_BRIDGE.md) spells out these translations. It also separates textbook foundations from the specialized recycling and estimation results imported from primary research papers.

## Read the conclusion at its stated scope

The exact Hamiltonian and target gate are fixed before the allowed error decreases. The active transition rank determines the leading coefficient for initial entropic coherence and logarithmic battery dimension. A zero-rank gate already preserves system energy and needs a trivial battery.

The dimension theorem retains a polylogarithmic gap between its explicit lower and upper bounds. Mean energy proportional to inverse square-root error is achieved by the construction; its optimality is a different question. The finite numerical checks exercise the construction and its formulas. General optimality follows from the written converse and construction.

For direct specialist access, return to the [scientific reading route](../README.md#read-the-science). The [related-work account](../references/RELATED_WORK.md) explains which methods and endpoints are inherited and which matching resource characterization is established here.
