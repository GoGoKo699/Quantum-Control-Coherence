#!/usr/bin/env python3
"""Independent finite checks of the energy-block battery construction.

The full finite unitary and the shift-overlap channel are constructed by
different paths. Exact integer energy labels test conservation; floating
Hamiltonian commutators are reported only as a secondary check. This program
does not optimize the diamond norm or certify an asymptotic theorem by fitting.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path
import platform
from typing import Any

import numpy as np


TOL = 2e-10
SUPPORT_TOL = 1e-13
SEED = 20261027
FINITE_LENGTHS = (2, 4, 7)
SCALING_LENGTHS = (8, 16, 32, 64, 128, 256)


@dataclass(frozen=True)
class Case:
    name: str
    # Coefficients of system energies in a formal rationally independent basis.
    charges: tuple[tuple[int, ...], ...]
    frequencies: tuple[float, ...]
    # One exact ambient charge vector for each active-lattice basis frequency.
    battery_generators: tuple[tuple[int, ...], ...]
    shifts: tuple[tuple[int, ...], ...]
    components: tuple[int, ...]
    target: np.ndarray
    projective_point: tuple[float, ...] | None = None
    basis_labels: tuple[str, ...] = ("1",)

    @property
    def d(self) -> int:
        return len(self.charges)

    @property
    def r(self) -> int:
        return len(self.battery_generators)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def max_abs(array: np.ndarray) -> float:
    return float(np.max(np.abs(array))) if array.size else 0.0


def rational_rank(rows: list[tuple[int, ...]]) -> int:
    """Gaussian elimination over Fraction; no floating rank decisions."""
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def ambient_charge(case: Case, k: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        sum(k[a] * case.battery_generators[a][b] for a in range(case.r))
        for b in range(len(case.frequencies))
    )


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def subtract(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x - y for x, y in zip(a, b))


def fourier(d: int) -> np.ndarray:
    indices = np.arange(d)
    return np.exp(2j * np.pi * np.outer(indices, indices) / d) / np.sqrt(d)


def cases() -> list[Case]:
    had = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    spectator = np.eye(3, dtype=complex)
    spectator[:2, :2] = had
    commuting = spectator.copy()
    commuting[2, 2] = np.exp(0.37j)
    resonant = np.zeros((4, 4), dtype=complex)
    resonant[:2, :2] = had
    theta = 0.41
    resonant[2:, 2:] = [[math.cos(theta), -math.sin(theta)],
                       [math.sin(theta), math.cos(theta)]]
    return [
        Case("qubit_hadamard", ((0,), (1,)), (1.0,), ((1,),),
             ((0,), (1,)), (0, 0), had),
        Case("qubit_pauli_x", ((0,), (1,)), (1.0,), ((1,),),
             ((0,), (1,)), (0, 0),
             np.array([[0, 1], [1, 0]], dtype=complex), (math.pi,)),
        Case("qutrit_fourier_commensurate", ((0,), (1,), (2,)), (1.0,),
             ((1,),), ((0,), (1,), (2,)), (0, 0, 0), fourier(3)),
        Case("qutrit_fourier_irrational", ((0, 0), (1, 0), (0, 1)),
             (1.0, math.sqrt(2)), ((1, 0), (0, 1)),
             ((0, 0), (1, 0), (0, 1)), (0, 0, 0), fourier(3),
             basis_labels=("1", "sqrt(2)")),
        Case("qutrit_spectator", ((0, 0), (1, 0), (0, 1)),
             (1.0, math.sqrt(2)), ((1, 0),),
             ((0,), (1,), (0,)), (0, 0, 1), spectator,
             basis_labels=("1", "sqrt(2)")),
        Case("degenerate_fourier", ((0,), (0,), (1,), (1,)), (1.0,),
             ((1,),), ((0,), (0,), (1,), (1,)), (0, 0, 0, 0), fourier(4)),
        Case("resonant_components", ((0,), (1,), (2,), (3,)), (1.0,),
             ((1,),), ((0,), (1,), (0,), (1,)), (0, 0, 1, 1), resonant),
        Case("energy_preserving_degenerate", ((0,), (0,), (1,)), (1.0,),
             (), ((), (), ()), (0, 0, 1), commuting),
    ]


def validate_case(case: Case) -> dict[str, Any]:
    require(case.target.shape == (case.d, case.d), case.name + ": shape")
    require(len(case.basis_labels) == len(case.frequencies), case.name + ": declared energy basis")
    require(max_abs(case.target.conj().T @ case.target - np.eye(case.d)) < TOL,
            case.name + ": target unitarity")
    require(rational_rank(list(case.battery_generators)) == case.r,
            case.name + ": independent active generators")
    offsets: dict[int, tuple[int, ...]] = {}
    for i in range(case.d):
        require(len(case.shifts[i]) == case.r, case.name + ": shift rank")
        offset = subtract(case.charges[i], ambient_charge(case, case.shifts[i]))
        component = case.components[i]
        require(component not in offsets or offsets[component] == offset,
                case.name + ": exact component energy offset")
        offsets[component] = offset
    active = []
    for i, j in product(range(case.d), repeat=2):
        if abs(case.target[i, j]) > SUPPORT_TOL:
            require(case.components[i] == case.components[j],
                    case.name + ": target component invariance")
            charge = subtract(case.charges[i], case.charges[j])
            require(charge == ambient_charge(case, subtract(case.shifts[i], case.shifts[j])),
                    case.name + ": exact active shift")
            active.append(charge)
    active_rank = rational_rank(active)
    require(active_rank == case.r, case.name + ": active rank")
    omega = [sum(g * f for g, f in zip(generator, case.frequencies))
             for generator in case.battery_generators]
    require(all(w > 0 for w in omega), case.name + ": positive frequencies")
    result: dict[str, Any] = {
        "name": case.name, "system_dimension": case.d,
        "active_rank": active_rank,
        "declared_exact_independent_energy_basis": case.basis_labels,
        "system_gap_rank": rational_rank([
            subtract(q, case.charges[0]) for q in case.charges]),
        "exact_system_charges": case.charges,
        "exact_battery_generators": case.battery_generators,
        "integer_shifts": case.shifts,
        "components": case.components,
        "battery_frequencies": omega,
    }
    if case.projective_point is not None:
        phases = np.exp(-1j * np.array(case.shifts) @ np.array(case.projective_point))
        transformed = phases[:, None] * case.target * phases.conj()[None, :]
        overlap = np.trace(case.target.conj().T @ transformed) / case.d
        require(abs(abs(overlap) - 1) < TOL, case.name + ": projective stabilizer")
        require(max_abs(transformed - case.target) > 1, case.name + ": nontrivial phase")
        result["finite_projective_stabilizer_check"] = {
            "phase_point": case.projective_point,
            "choi_infidelity": float(max(0.0, 1 - abs(overlap) ** 2)),
            "scalar_phase_real": float(overlap.real),
            "scalar_phase_imag": float(overlap.imag),
        }
    return result


def padding(case: Case) -> int:
    return max((max((abs(x) for x in subtract(case.shifts[i], case.shifts[j])), default=0)
                for i, j in product(range(case.d), repeat=2)
                if case.components[i] == case.components[j]), default=0)


def sine_amplitudes(length: int) -> np.ndarray:
    n = np.arange(1, length + 1)
    return np.sqrt(2 / (length + 1)) * np.sin(np.pi * n / (length + 1))


def overlap_1d(amplitudes: np.ndarray, shift: int) -> float:
    shift = abs(shift)
    if shift >= len(amplitudes):
        return 0.0
    if shift == 0:
        return float(np.dot(amplitudes, amplitudes))
    return float(np.dot(amplitudes[shift:], amplitudes[:-shift]))


def kernel_channel(case: Case, length: int) -> tuple[np.ndarray, dict[str, float]]:
    """Compute channel coefficients without assembling V or a battery box."""
    one = sine_amplitudes(length)
    cache: dict[tuple[int, ...], float] = {}

    def overlap(v: tuple[int, ...]) -> float:
        if v not in cache:
            cache[v] = math.prod(overlap_1d(one, step) for step in v)
        return cache[v]

    displacements = {(i, j): subtract(case.shifts[j], case.shifts[i])
                     for i, j in product(range(case.d), repeat=2)}
    channel = np.zeros((case.d,) * 4, dtype=complex)  # i,k,j,l
    q_bound = 0.0
    b_bound = 0.0
    for i, k, j, ell in product(range(case.d), repeat=4):
        coefficient = case.target[i, j] * case.target[k, ell].conjugate()
        v = subtract(displacements[i, j], displacements[k, ell])
        g = overlap(v)
        channel[i, k, j, ell] = coefficient * g
        q_bound += abs(coefficient) * abs(1 - g)
        b_bound += abs(coefficient) * sum(abs(x) for x in v) ** 2
    b_bound *= np.pi ** 2 / 2
    a_bound = np.pi * sum(abs(case.target[i, j]) * sum(abs(x) for x in v)
                          for (i, j), v in displacements.items())
    projected = np.array([[case.target[i, j] * overlap(displacements[i, j])
                           for j in range(case.d)] for i in range(case.d)])
    cross = case.target.conj().T @ projected
    difference_gram = 2 * np.eye(case.d) - cross - cross.conj().T
    isometry_error_sq = max(0.0, float(np.linalg.eigvalsh(difference_gram)[-1]))
    require(q_bound <= b_bound / (length + 1) ** 2 + TOL,
            case.name + ": finite coefficient diamond bound")
    require(isometry_error_sq <= a_bound ** 2 / (length + 1) ** 2 + TOL,
            case.name + ": finite isometry bound")
    return channel, {
        "A": float(a_bound), "B": float(b_bound),
        "coefficient_full_diamond_upper": float(q_bound),
        "analytic_full_diamond_upper": float(b_bound / (length + 1) ** 2),
        "analytic_infidelity_upper": float(min(1, a_bound ** 2 / (length + 1) ** 2)),
        "isometry_error_squared": float(isometry_error_sq),
    }


def normalized_choi(channel: np.ndarray) -> np.ndarray:
    d = channel.shape[0]
    return channel.transpose(0, 2, 1, 3).reshape(d * d, d * d) / d


def density_samples(d: int, rng: np.random.Generator) -> list[np.ndarray]:
    samples = [np.eye(d, dtype=complex) / d]
    for i in range(d):
        basis = np.eye(d, dtype=complex)[:, i]
        samples.append(np.outer(basis, basis.conj()))
    for _ in range(12):
        vector = rng.normal(size=d) + 1j * rng.normal(size=d)
        vector /= np.linalg.norm(vector)
        samples.append(np.outer(vector, vector.conj()))
        matrix = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        rho = matrix @ matrix.conj().T
        samples.append(rho / np.trace(rho))
    return samples


def fidelity_from_channel(channel: np.ndarray, target: np.ndarray,
                          rho: np.ndarray) -> float:
    # rho is the system reduction of an arbitrary pure system-reference probe.
    weight = (rho @ target.conj().T).T
    value = np.einsum("ij,kl,ikjl->", weight, weight.conj(), channel)
    require(abs(value.imag) < TOL, "real reference fidelity")
    return float(value.real)


def direct_purification_fidelity(kraus: np.ndarray, target: np.ndarray,
                                rho: np.ndarray) -> float:
    eigenvalues, eigenvectors = np.linalg.eigh(rho)
    root = (eigenvectors * np.sqrt(np.maximum(eigenvalues, 0))) @ eigenvectors.conj().T
    ideal = (target @ root).reshape(-1)
    return float(sum(abs(np.vdot(ideal, (operator @ root).reshape(-1))) ** 2
                     for operator in kraus))


def resource_values(case: Case, length: int) -> dict[str, float | int]:
    k = padding(case)
    p = sine_amplitudes(length) ** 2
    entropy = float(-np.sum(p * np.log2(p)))
    omega = [sum(g * f for g, f in zip(generator, case.frequencies))
             for generator in case.battery_generators]
    coherence = case.r * entropy
    require(coherence <= case.r * math.log2(length) + TOL, case.name + ": entropy bound")
    return {
        "L": length, "padding_K": k,
        "battery_dimension": (length + 2 * k + 2) ** case.r,
        "coherence_bits": coherence,
        "coherence_upper_bits": case.r * math.log2(length),
        "mean_energy": (k + (length + 1) / 2) * sum(omega),
    }


def check_finite_instance(case: Case, length: int, rng: np.random.Generator) -> dict[str, Any]:
    """Assemble the full block unitary, including every boundary basis state."""
    k_pad = padding(case)
    coordinates = list(product(range(length + 2 * k_pad + 2), repeat=case.r))
    lookup = {k: b for b, k in enumerate(coordinates)}
    nb = len(coordinates)
    total_dimension = case.d * nb
    one = sine_amplitudes(length)
    battery = np.array([
        math.prod(one[x - k_pad - 1] for x in k)
        if all(k_pad + 1 <= x <= k_pad + length for x in k) else 0.0
        for k in coordinates
    ])
    require(abs(np.vdot(battery, battery) - 1) < TOL, case.name + ": battery normalization")
    battery_charges = [ambient_charge(case, k) for k in coordinates]
    require(len(set(battery_charges)) == nb, case.name + ": exact battery nondegeneracy")
    battery_energies = np.array([sum(q * f for q, f in zip(charge, case.frequencies))
                                 for charge in battery_charges])
    require(float(battery_energies.min()) >= -TOL, case.name + ": nonnegative energy")

    blocks: dict[tuple[int, tuple[int, ...]], list[tuple[int, int]]] = {}
    members: dict[int, list[int]] = {}
    for i, component in enumerate(case.components):
        members.setdefault(component, []).append(i)
        for b, k in enumerate(coordinates):
            blocks.setdefault((component, add(k, case.shifts[i])), []).append((i, b))
    unitary = np.zeros((total_dimension, total_dimension), dtype=complex)
    full_blocks = 0
    boundary_blocks = 0
    physical_blocks: dict[tuple[int, ...], int] = {}
    for (component, _), basis in blocks.items():
        indices = [i * nb + b for i, b in basis]
        system_indices = [i for i, _ in basis]
        total_charges = {add(case.charges[i], battery_charges[b]) for i, b in basis}
        require(len(total_charges) == 1, case.name + ": exact constant-energy block")
        energy_label = next(iter(total_charges))
        physical_blocks[energy_label] = physical_blocks.get(energy_label, 0) + 1
        if system_indices == members[component]:
            unitary[np.ix_(indices, indices)] = case.target[np.ix_(system_indices, system_indices)]
            full_blocks += 1
        else:
            unitary[indices, indices] = 1
            boundary_blocks += 1

    unitarity_defect = max_abs(unitary.conj().T @ unitary - np.eye(total_dimension))
    require(unitarity_defect < TOL, case.name + ": global unitarity")
    all_charges = [add(case.charges[i], battery_charges[b])
                   for i in range(case.d) for b in range(nb)]
    rows, columns = np.nonzero(np.abs(unitary) > SUPPORT_TOL)
    violations = sum(all_charges[i] != all_charges[j] for i, j in zip(rows, columns))
    require(violations == 0, case.name + ": exact conservation")
    all_energies = np.array([sum(q * f for q, f in zip(charge, case.frequencies))
                             for charge in all_charges])
    commutator = max_abs(unitary * (all_energies[:, None] - all_energies[None, :]))

    initial_embedding = np.zeros((total_dimension, case.d), dtype=complex)
    for j in range(case.d):
        initial_embedding[j * nb:(j + 1) * nb, j] = battery
    actual_isometry = unitary @ initial_embedding
    kraus = actual_isometry.reshape(case.d, nb, case.d).transpose(1, 0, 2)
    direct_channel = np.einsum("bij,bkl->ikjl", kraus, kraus.conj())
    kernel, bounds = kernel_channel(case, length)
    channel_discrepancy = max_abs(direct_channel - kernel)
    require(channel_discrepancy < TOL, case.name + ": block channel equals overlap kernel")
    require(max_abs(np.einsum("bji,bjk->ik", kraus.conj(), kraus) - np.eye(case.d)) < TOL,
            case.name + ": Kraus trace preservation")

    shifted_isometry = np.zeros_like(actual_isometry)
    for i, j in product(range(case.d), repeat=2):
        if abs(case.target[i, j]) <= SUPPORT_TOL:
            continue
        displacement = subtract(case.shifts[j], case.shifts[i])
        for b, k in enumerate(coordinates):
            if battery[b] != 0:
                shifted = add(k, displacement)
                require(shifted in lookup, case.name + ": padded support contains shift")
                shifted_isometry[i * nb + lookup[shifted], j] += case.target[i, j] * battery[b]
    shift_discrepancy = max_abs(actual_isometry - shifted_isometry)
    require(shift_discrepancy < TOL, case.name + ": physical isometry equals shift formula")
    ideal_isometry = np.kron(case.target, battery[:, None])
    difference = actual_isometry - ideal_isometry
    direct_isometry_error_sq = max(0.0, float(np.linalg.eigvalsh(difference.conj().T @ difference)[-1]))
    require(abs(direct_isometry_error_sq - bounds["isometry_error_squared"]) < TOL,
            case.name + ": independent isometry error formula")

    choi = normalized_choi(direct_channel)
    eigenvalues = np.linalg.eigvalsh(choi)
    require(float(eigenvalues.min()) > -TOL, case.name + ": Choi positivity")
    require(abs(np.trace(choi) - 1) < TOL, case.name + ": Choi trace")
    target_vector = case.target.reshape(-1) / np.sqrt(case.d)
    choi_difference = choi - np.outer(target_vector, target_vector.conj())
    choi_trace_norm = float(np.sum(np.abs(np.linalg.eigvalsh(choi_difference))))
    require(choi_trace_norm <= bounds["coefficient_full_diamond_upper"] + TOL,
            case.name + ": Choi witness below coefficient diamond upper")

    samples = density_samples(case.d, rng)
    sample_infidelities = [1 - fidelity_from_channel(direct_channel, case.target, rho)
                           for rho in samples]
    require(min(sample_infidelities) > -TOL, case.name + ": nonnegative sample infidelity")
    require(max(sample_infidelities) <= min(1, direct_isometry_error_sq) + TOL,
            case.name + ": sampled reference-assisted fidelity bound")
    purification = direct_purification_fidelity(kraus, case.target, samples[-1])
    purification_discrepancy = abs(purification - fidelity_from_channel(
        direct_channel, case.target, samples[-1]))
    require(purification_discrepancy < TOL, case.name + ": explicit reference purification")

    resources = resource_values(case, length)
    support_probabilities = np.abs(battery[battery != 0]) ** 2
    direct_entropy = float(-np.sum(support_probabilities * np.log2(support_probabilities)))
    direct_mean = float(np.dot(np.abs(battery) ** 2, battery_energies))
    require(nb == resources["battery_dimension"], case.name + ": dimension formula")
    require(abs(direct_entropy - resources["coherence_bits"]) < TOL, case.name + ": total-energy entropy")
    require(abs(direct_mean - resources["mean_energy"]) < TOL, case.name + ": mean energy formula")
    if case.name == "resonant_components":
        require(any(count > 1 for count in physical_blocks.values()),
                case.name + ": coincident physical energy sectors are exercised")
    if case.r == 0:
        require(nb == 1 and direct_entropy == 0 and direct_mean == 0,
                case.name + ": zero-rank resources")
        require(max(sample_infidelities) < TOL, case.name + ": exact zero-rank channel")

    return {
        **resources, **bounds,
        "total_dimension": total_dimension,
        "complete_refined_blocks": full_blocks,
        "identity_boundary_blocks": boundary_blocks,
        "physical_total_energy_sectors": len(physical_blocks),
        "sectors_with_multiple_refined_blocks": sum(v > 1 for v in physical_blocks.values()),
        "global_unitarity_max_entry_defect": unitarity_defect,
        "exact_integer_conservation_violations": violations,
        "floating_commutator_max_entry": commutator,
        "channel_kernel_max_entry_discrepancy": channel_discrepancy,
        "isometry_shift_max_entry_discrepancy": shift_discrepancy,
        "choi_min_eigenvalue": float(eigenvalues.min()),
        "choi_half_trace_distance_lower_witness": choi_trace_norm / 2,
        "reference_probe_count": len(samples),
        "sample_max_reference_infidelity": max(0.0, float(max(sample_infidelities))),
        "explicit_purification_fidelity_discrepancy": purification_discrepancy,
        "direct_mean_energy": direct_mean,
        "direct_coherence_bits": direct_entropy,
    }


def scaling_data(case: Case) -> dict[str, Any]:
    rows = []
    for length in SCALING_LENGTHS:
        kernel, bounds = kernel_channel(case, length)
        infidelity = max(0.0, 1 - fidelity_from_channel(
            kernel, case.target, np.eye(case.d) / case.d))
        rows.append({**resource_values(case, length), **bounds,
                     "maximally_entangled_probe_infidelity": infidelity})
    previous, last = rows[-2:]
    log_ratio = math.log(last["L"] / previous["L"])

    def slope(field: str) -> float | None:
        if previous[field] <= 0 or last[field] <= 0:
            return None
        return math.log(last[field] / previous[field]) / log_ratio

    return {
        "method": "overlap kernel and exact resource formulas; no full unitary at these sizes",
        "rows": rows,
        "last_interval_observations_not_theorem_certificates": {
            "coherence_increment_per_log2_L":
                (last["coherence_bits"] - previous["coherence_bits"]) /
                math.log2(last["L"] / previous["L"]),
            "log_dimension_slope": slope("battery_dimension"),
            "log_mean_energy_slope": slope("mean_energy"),
            "log_coefficient_diamond_upper_slope": slope("coefficient_full_diamond_upper"),
            "log_choi_probe_infidelity_slope": slope("maximally_entangled_probe_infidelity"),
        },
    }


def run() -> dict[str, Any]:
    rng = np.random.default_rng(SEED)
    results = []
    for case in cases():
        metadata = validate_case(case)
        finite = [check_finite_instance(case, length, rng) for length in FINITE_LENGTHS]
        results.append({**metadata, "finite_instances": finite, "scaling": scaling_data(case)})
        print(f"PASS {case.name}: rank {case.r}, {len(finite)} explicit finite unitaries")
    all_finite = [instance for case in results for instance in case["finite_instances"]]
    return {
        "schema_version": 1,
        "status": "passed",
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "seed": SEED,
        "numerical_tolerance": TOL,
        "scope": {
            "exact": "integer energy coordinates, active rational ranks, dimensions and sector labels",
            "floating": "unitarity, channel equality, fidelity, entropy and finite bound evaluations",
            "not_computed": "exact diamond norm or a certified optimization of worst-case infidelity",
            "asymptotics": "scaling observations illustrate the analytic proof; finite checks do not prove it",
        },
        "summary": {
            "cases": len(results), "explicit_finite_unitaries": len(all_finite),
            "exact_conservation_violations": sum(x["exact_integer_conservation_violations"] for x in all_finite),
            "maximum_channel_kernel_discrepancy": max(x["channel_kernel_max_entry_discrepancy"] for x in all_finite),
            "maximum_unitarity_defect": max(x["global_unitarity_max_entry_defect"] for x in all_finite),
            "maximum_reference_purification_discrepancy": max(x["explicit_purification_fidelity_discrepancy"] for x in all_finite),
        },
        "cases": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parent / "results.json")
    args = parser.parse_args()
    results = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(results, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(args.output)
    print(json.dumps(results["summary"], indent=2))
    print(f"Results: {args.output}")


if __name__ == "__main__":
    main()
