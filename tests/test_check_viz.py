"""Tests for qclab.check and qclab.viz: correct answer, wrong answer, edge cases."""
import matplotlib

matplotlib.use("Agg")

import numpy as np
import pytest
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

from qclab.check import assert_distribution, assert_statevector
from qclab.viz import draw_circuit, plot_counts, plot_statevector

S = 1 / np.sqrt(2)


def bell(sign=1):
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    if sign < 0:
        qc.z(0)
    return qc


def test_statevector_correct():
    assert assert_statevector(bell(), {"00": S, "11": S}) is True


def test_statevector_wrong_state_and_wrong_phase():
    with pytest.raises(AssertionError):
        assert_statevector(bell(), {"01": S, "10": S})
    with pytest.raises(AssertionError):
        assert_statevector(bell(-1), {"00": S, "11": S})  # phi- vs phi+
    assert assert_statevector(bell(-1), {"00": S, "11": -S})


def test_statevector_edges():
    # unnormalised expected is accepted (normalised silently)
    assert assert_statevector(bell(), {"00": 1, "11": 1})
    # global phase ignored
    assert assert_statevector(bell(), {"00": 1j * S, "11": 1j * S})
    # all-zero expected
    with pytest.raises(ValueError):
        assert_statevector(bell(), {"00": 0})
    # measurements ignored
    qc = bell(); qc.measure_all()
    assert assert_statevector(qc, {"00": S, "11": S})
    # tiny amplitude error: fidelity is quadratic, so ~1e-4 error passes
    th = 1e-4
    qc = QuantumCircuit(1); qc.ry(2 * th, 0)
    assert assert_statevector(qc, {"0": 1})


def test_statevector_bad_bitstring_lengths():
    # documented finding: wrong-length keys are not rejected
    qc = QuantumCircuit(2); qc.x(0)
    assert assert_statevector(qc, {"1": 1})  # "1" is read as "01" (silent)
    with pytest.raises(IndexError):
        assert_statevector(qc, {"111": 1})


def test_distribution():
    assert assert_distribution({"00": 510, "11": 490}, {"00": 0.5, "11": 0.5})
    with pytest.raises(AssertionError):
        assert_distribution({"00": 700, "11": 300}, {"00": 0.5, "11": 0.5})
    with pytest.raises(AssertionError):  # unexpected outcome
        assert_distribution({"00": 450, "11": 450, "01": 100}, {"00": 0.5, "11": 0.5})
    # boundary: 0.54 accepted; exactly 0.05 is rejected by float rounding (0.55-0.5 > 0.05)
    assert assert_distribution({"0": 540, "1": 460}, {"0": 0.5, "1": 0.5})
    with pytest.raises(AssertionError):
        assert_distribution({"0": 560, "1": 440}, {"0": 0.5, "1": 0.5})


def test_distribution_edges():
    with pytest.raises(AssertionError):  # empty counts: fails cleanly, no crash
        assert_distribution({}, {"0": 1.0})
    with pytest.raises(ZeroDivisionError):  # counts with only zeros: raw crash
        assert_distribution({"0": 0}, {"0": 1.0})
    # expected probs not summing to 1 are not validated
    assert assert_distribution({"0": 1000}, {"0": 1.0})
    # multi-register keys with spaces never match plain keys
    with pytest.raises(AssertionError):
        assert_distribution({"0 0": 1000}, {"00": 1.0})


def test_viz_return_figures():
    import matplotlib.pyplot as plt
    assert draw_circuit(bell(), title="t") is not None
    assert plot_counts({"00": 5, "11": 5}) is not None
    fig = plot_statevector(bell())
    assert len(fig.axes[0].patches) == 4
    assert plot_statevector(Statevector.from_label("+")) is not None
    big = QuantumCircuit(4); big.h(range(4))
    assert plot_statevector(big) is not None
    plt.close("all")
