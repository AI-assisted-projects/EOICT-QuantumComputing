"""Known-state checks for qclab.states and qclab.runner (Qiskit little-endian order)."""
import numpy as np
import pytest
from qiskit import QuantumCircuit
from qiskit.circuit.library import CXGate, HGate, XGate

from qclab.runner import simulate
from qclab.states import matrix_of, matrix_to_latex, statevector_of

S = 1 / np.sqrt(2)


def amps(qc):
    return np.asarray(statevector_of(qc).data)


def test_h_state():
    qc = QuantumCircuit(1); qc.h(0)
    assert np.allclose(amps(qc), [S, S])


def test_x_state():
    qc = QuantumCircuit(1); qc.x(0)
    assert np.allclose(amps(qc), [0, 1])


def test_bell_state():
    qc = QuantumCircuit(2); qc.h(0); qc.cx(0, 1)
    assert np.allclose(amps(qc), [S, 0, 0, S])


def test_ghz_state():
    qc = QuantumCircuit(3); qc.h(0); qc.cx(0, 1); qc.cx(1, 2)
    v = np.zeros(8, complex); v[0] = v[7] = S
    assert np.allclose(amps(qc), v)


def test_little_endian_order():
    # X on qubit 0 gives |001>, i.e. index 1; X on qubit 1 gives index 2.
    qc = QuantumCircuit(2); qc.x(0)
    assert np.isclose(abs(amps(qc)[1]), 1)
    qc = QuantumCircuit(2); qc.x(1)
    assert np.isclose(abs(amps(qc)[2]), 1)


def test_normalised():
    qc = QuantumCircuit(3); qc.h(range(3)); qc.t(0); qc.cx(0, 2)
    assert np.isclose(np.linalg.norm(amps(qc)), 1)


def test_measurements_ignored_in_statevector():
    qc = QuantumCircuit(2, 2); qc.h(0); qc.cx(0, 1); qc.measure([0, 1], [0, 1])
    assert np.allclose(amps(qc), [S, 0, 0, S])


def test_matrices():
    assert np.allclose(matrix_of(HGate()).data, [[S, S], [S, -S]])
    assert np.allclose(matrix_of(XGate()).data, [[0, 1], [1, 0]])
    # Qiskit CXGate: control = qubit 0 (least significant) -> swaps indices 1 and 3.
    assert np.allclose(matrix_of(CXGate()).data,
                       [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])


def test_matrix_of_circuit_strips_measurements():
    qc = QuantumCircuit(1, 1); qc.x(0); qc.measure(0, 0)
    assert np.allclose(matrix_of(qc).data, [[0, 1], [1, 0]])


def test_latex():
    s = matrix_to_latex(matrix_of(HGate()))
    assert s.startswith("\\begin{bmatrix}") and "0.707" in s
    assert "-0.707" in s


def test_simulate_deterministic_states():
    qc = QuantumCircuit(2, 2); qc.x(0); qc.measure([0, 1], [0, 1])
    # little-endian: classical bit 0 is the rightmost character
    assert simulate(qc, shots=100) == {"01": 100}


def test_simulate_bell_counts():
    qc = QuantumCircuit(2, 2); qc.h(0); qc.cx(0, 1); qc.measure([0, 1], [0, 1])
    c = simulate(qc, shots=2000)
    assert set(c) == {"00", "11"} and sum(c.values()) == 2000
    assert abs(c["00"] - 1000) < 150


def test_simulate_ghz_counts():
    qc = QuantumCircuit(3, 3); qc.h(0); qc.cx(0, 1); qc.cx(1, 2); qc.measure(range(3), range(3))
    assert set(simulate(qc, shots=500)) == {"000", "111"}


def test_simulate_shots_respected():
    qc = QuantumCircuit(1, 1); qc.h(0); qc.measure(0, 0)
    assert sum(simulate(qc, shots=37).values()) == 37


def test_simulate_without_measurement_raises():
    qc = QuantumCircuit(1); qc.h(0)
    with pytest.raises(ValueError, match="measure"):
        simulate(qc, shots=10)


def test_simulate_seed_is_reproducible():
    qc = QuantumCircuit(1); qc.h(0); qc.measure_all()
    assert simulate(qc, shots=200, seed=7) == simulate(qc, shots=200, seed=7)
