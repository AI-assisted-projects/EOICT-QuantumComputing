# Review of the QC project (M1)

Work in progress; sections are filled in task by task. (💡 accepted suggestion S10)

## 1. qclab/states.py and qclab/runner.py

Checked with `tests/test_states_runner.py` (run: `.venv-container/bin/python -m pytest tests`).

### Confirmed correct
- `statevector_of`: H, X, Bell (`[1/√2,0,0,1/√2]`), GHZ-3 and a random-ish 3-qubit circuit are right and normalised; final measurements are ignored.
- Qubit order is Qiskit little-endian: `x(0)` gives index 1, `x(1)` gives index 2; `CXGate` matrix has control = qubit 0 (swaps indices 1 and 3), matching the note in the git log.
- `matrix_of`: H, X, CX correct; measurements stripped for circuits.
- `matrix_to_latex`: produces a `bmatrix`, negative entries rendered correctly for H.
- `simulate`: counts sum to `shots`; `x(0)` on 2 qubits gives `"01"` (rightmost char = classical bit 0); Bell gives only `00`/`11`, GHZ only `000`/`111`.

### Findings (no code changed)
1. **No seed option in `simulate`** (low): results vary between runs (checked: 50/50, 52/48, 62/38 for H). Fine for teaching, but makes exact-count self-checks flaky; tests here use tolerances. Suggest an optional `seed=None` argument passed to `AerSimulator.run(seed_simulator=...)`; backwards compatible.
2. **`simulate` on a circuit without measurements** raises a raw `QiskitError: No counts for experiment "0"` (low). A beginner-friendly message ("add measurements") would help. Suggest wrapping it.
3. **`_counts_from_pub_result` takes only the first register** (low, IBM path only): circuits with several classical registers would lose the others. Not relevant to the course circuits.
4. **`statevector_of` with mid-circuit measurement** is not supported (`remove_final_measurements` only strips final ones) — acceptable, document if an exercise ever needs it.
5. `_pick_backend` swallows all exceptions from `least_busy` with a bare `except Exception` (cosmetic). Not exercised: the IBM path was deliberately not run (no token use).

Remaining tasks (check.py/viz.py, notebooks, README/pyproject, final summary) are still open.

Note: `pytest` is not in `pyproject.toml` (installed only in `.venv-container`). Adding it as an optional dev dependency needs the owner's approval (new dependency) — proposed, not done.
