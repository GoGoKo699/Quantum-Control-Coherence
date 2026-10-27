# Finite verification of the battery construction

The script in this directory exercises the [finite battery construction](../science/battery_construction.md) by two independent calculations. It first constructs the full energy-conserving system-battery unitary, including every boundary basis state, and derives its Kraus channel. It separately computes the reduced channel from the sine-packet overlap kernel. Their agreement checks the finite implementation, padding, shift signs, complex conjugations, and treatment of disconnected and degenerate energy sectors.

The analytical proof establishes the general bounds and asymptotic resource law. These finite calculations do not prove that theorem, optimize over battery designs, or establish an exact worst-case error by sampling.

## Run

The recorded run used Python **3.12.14** and NumPy **2.3.5**. NumPy is the only dependency; its version is pinned in [requirements.txt](requirements.txt). The script uses the standard library for exact rational elimination, integer sector labels, JSON output, and command-line arguments.

From the repository root, in a Python environment of your choice:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify_construction.py
```

The default output is [results.json](results.json). To preserve it while producing another run:

```bash
python verification/verify_construction.py --output /tmp/coherence-verification.json
```

An assertion failure exits unsuccessfully. The output file is replaced only after all checks pass. The seed is fixed at `20261027`. No network access or optional optimization package is needed to run the checks once NumPy is installed.

## Models

The system energy scale is fixed by the displayed spectra. $`F_d`$ denotes the normalized discrete Fourier unitary with a positive phase convention; $`H_2`$ denotes the qubit Hadamard gate.

| Model | System energies | Target gate | Active rank | Purpose |
|---|---|---|---:|---|
| `qubit_hadamard` | $`0,1`$ | $`H_2`$ | 1 | Basic coherent rotation and boundary padding |
| `qubit_pauli_x` | $`0,1`$ | $`X`$ | 1 | A half-period shift changes the matrix sign while leaving the channel unchanged |
| `qutrit_fourier_commensurate` | $`0,1,2`$ | $`F_3`$ | 1 | Multi-step integer transitions; $`K=2`$ |
| `qutrit_fourier_irrational` | $`0,1,\sqrt2`$ | $`F_3`$ | 2 | Two independent phase coordinates; $`K=1`$ |
| `qutrit_spectator` | $`0,1,\sqrt2`$ | $`H_2\oplus1`$ | 1 | Inactive spectral rank does not enlarge the battery lattice |
| `degenerate_fourier` | $`0,0,1,1`$ | $`F_4`$ | 1 | Degenerate system eigenspaces and complex gate entries |
| `resonant_components` | $`0,1,2,3`$ | Two separate qubit rotations | 1 | Different refined blocks can share the same total energy |
| `energy_preserving_degenerate` | $`0,0,1`$ | $`H_2\oplus e^{0.37i}`$ | 0 | A nontrivial exactly conserving gate needs a trivial battery |

Each model is tested with $`L=2,4,7`$, giving **24 explicitly assembled finite global unitaries**. The rank-zero construction is independent of $`L`$ and is included in the same loop to check that it remains trivial.

### Exact energy representation

The irrational examples explicitly declare the formal, rationally independent energy basis $`(1,\sqrt2)`$. System energies and battery generators are integer vectors in that basis. Other examples use the basis $`(1)`$. The active rank is computed over exact `Fraction` arithmetic from those integer vectors. It is never inferred from floating-point values of energies.

Conservation is checked by comparing exact total-energy vectors for every nonzero element of the constructed unitary. The floating-point Hamiltonian commutator is only a secondary diagnostic. The declared rational independence of $`1,\sqrt2`$ is a mathematical property of the specified model; no numerical procedure is used to infer it.

The script constructs the orthogonal refined blocks indexed by the invariant component and integer total coordinate. It applies the corresponding target block on every complete refined block and identity on every incomplete block. It then assembles these into one finite matrix. The `resonant_components` case explicitly confirms that several refined blocks can occupy the same physical energy sector.

## Checks and their interpretation

For each finite instance the script verifies:

1. The target gate is unitary, its support respects the declared components, and its nonzero transitions have the declared exact integer coordinates and rank.
2. The full system-battery matrix is unitary and has no matrix elements between unequal exact total-energy labels. All boundary states are included.
3. The padded sine packet is normalized, its battery energies are nonnegative and exactly nondegenerate, and every required shifted support point lies inside the finite box.
4. Applying the global unitary to the initial battery yields the shift isometry. Its Kraus channel agrees with the independent overlap-kernel formula, preserves trace, and has a positive normalized Choi matrix up to roundoff.
5. The direct isometry error agrees with the independent overlap expression and obeys the analytical finite bound. Reference-assisted fidelities for a fixed collection of pure and mixed system reductions lie within that bound. One mixed reduction is also evaluated by explicitly constructing a pure system-reference state.
6. The coefficient sum $`Q_L`$ obeys the finite diamond upper bound from the proof. The normalized Choi trace distance lies below that upper bound, with the correct factor of two for half diamond distance.
7. Entropic energy coherence, total battery dimension, and mean battery energy agree with the exact product-packet formulas. The zero-rank cases have zero coherence and energy, dimension one, and an exact channel.

The numerical tolerance is `2e-10`; it accommodates ordinary floating-point linear algebra. Exact conservation violations are integer counts and must equal zero. Numerical zero matrix entries in the specified target gates are identified using a separate support threshold of `1e-13`; this does not perform a rank inference from nearly commensurate energies.

### Fidelity and diamond quantities

For a system density matrix $`\rho`$, the script evaluates the fidelity for a pure reference-assisted probe with that system reduction:

```math
F_\rho=\sum_b
\left|\mathrm{Tr}\left(\rho U^\dagger K_b\right)\right|^2,
```

where $`K_b`$ are the directly constructed Kraus operators. A mixed $`\rho`$ therefore tests an entangled pure input, not merely a mixed unreferenced input. The reported maximum infidelity over the finite probe set is a **lower bound** on the true worst-case infidelity. The universal upper bound comes from the analytical isometry estimate, not from that maximum.

For diamond distance, the reported coefficient sum is

```math
Q_L=\sum_{ij,k\ell}|U_{ij}U_{k\ell}|
\left|1-g_{v_{ij}-v_{k\ell}}\right|.
```

The proof gives

```math
\|\mathcal E_L-\mathcal U\|_\diamond
\le Q_L\le\frac{B_{\mathrm{ch}}}{(L+1)^2}.
```

The reported normalized Choi half-trace-distance is a **lower witness** for half diamond distance. The script does not compute the exact diamond norm. Upper-bound values can exceed the trivial full-diamond bound of two for small packets; the data preserves the raw coefficient and analytical formulas so their checks remain transparent.

## Resource scaling data

The output also contains evaluations at $`L=8,16,32,64,128,256`$. These use the overlap kernel and exact resource formulas, without allocating the full unitary at those larger sizes:

```math
\begin{aligned}
C(\beta_L,H_B)&=rH(p_L),\\
d_B&=(L+2K+2)^r,\\
\langle H_B\rangle
&=\left(K+\frac{L+1}{2}\right)\sum_a\omega_a.
\end{aligned}
```

The reported last-interval slopes illustrate the approach to logarithmic coherence coefficient $`r`$, dimension exponent $`r`$, mean-energy exponent one, and error exponent minus two as functions of packet length. They are observations of this family, not fitted proofs or claims about the exact optimal controller. The theorem converts $`L=O(\varepsilon^{-1/2})`$ into a leading dimension exponent $`r/2`$ in inverse error; its converse retains a polylogarithmic gap.

## Recorded result

The committed data records all 24 finite instances passing, with:

| Quantity | Recorded value |
|---|---:|
| Exact integer conservation violations | 0 |
| Maximum channel/kernel entry discrepancy | $`2.22\times10^{-16}`$ |
| Maximum global unitarity entry defect | $`4.44\times10^{-16}`$ |
| Maximum explicit-reference fidelity discrepancy | $`2.44\times10^{-15}`$ |

Small last-digit changes are possible across NumPy builds or linear algebra libraries. The output includes the Python and NumPy versions, all model coordinates, per-instance values, the seed, and a statement of the numerical scope.
