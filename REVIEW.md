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

## 2. qclab/check.py and qclab/viz.py

Checked with `tests/test_check_viz.py` (7 tests; whole suite: 22 passed). No code changed.

### Confirmed correct
- `assert_statevector`: accepts the right state (Bell), rejects a wrong state, and distinguishes relative phase (Φ⁻ is rejected when Φ⁺ is expected, accepted with `-S`). Global phase is ignored (correct physically). Measurements in the circuit are ignored. All-zero expected raises `ValueError`.
- `assert_distribution`: accepts right counts, rejects skewed counts and unexpected extra outcomes; error messages show measured vs expected.
- `viz`: `draw_circuit`, `plot_counts`, `plot_statevector` return figures; the statevector plot has one bar per basis state (4 for Bell), also works for `Statevector` input and for 4 qubits. Labels use the same leftmost = highest-qubit convention as Qiskit.

### Findings (no behaviour changed; changes to what checks accept need owner approval)
1. **Wrong-length bit-strings are not validated in `assert_statevector`** (medium, changes acceptance): `{"1": 1}` on 2 qubits is silently read as `"01"`; `"111"` gives a raw `IndexError`. Suggest a clear `ValueError` ("bit-strings must have N characters"). `n` is passed to `_bitstring_to_index` but unused.
2. **Expected amplitudes are silently normalised** (low, by design per comment): `{"00": 1, "11": 1}` passes for Bell. Friendly for beginners, but hides a forgotten 1/√2; consider documenting in the exercises.
3. **State tolerance is quadratic** (low): fidelity < 1-1e-6 means amplitude errors up to ~1e-3 pass. Fine for a course.
4. **`assert_distribution` boundary is float-fragile** (low): a deviation of exactly 0.05 (550/450 vs 0.5/0.5) is rejected because 0.55-0.5 = 0.05000000000000004. Harmless with real shot noise.
5. **Zero total counts** (`{"0": 0}`) gives a raw `ZeroDivisionError`; empty counts fail cleanly with the normal message. Very unlikely for students.
6. **Expected probabilities are not validated** (low): they need not sum to 1, and a key with a register space (`"0 0"`) never matches `"00"`, so such counts fail. Suggest normalising/validating and stripping spaces.
7. **Statistical power** (info): 5% tol with 1024 shots (σ≈1.6%) is ~3σ, so a correct circuit fails about 0.3% of the time on the simulator; a mildly wrong answer (e.g. 0.56/0.44) passes. Consider fixed seed in `simulate` (see section 1, finding 1) to make checks deterministic.
8. `viz.py`: `plot_counts` docstring is correct; `draw_circuit` sizes the figure by gate count (cosmetic); unused `matplotlib` import style is fine. Annotation hides probabilities below 0.05 for >8 states (intended).

## 3. Teacher notebook (solutions_teacher.ipynb)

Every solution was re-derived by hand and cross-checked with the simulator.

### Confirmed correct
- Ex 1 (H, 50/50, [0.707, 0.707]); Ex 2 (all four starts give Φ⁺, Φ⁻, Ψ⁺, Ψ⁻ up to global phase, table and the "same counts, different phase" point are right; start `11` gives -Ψ⁻, global phase only).
- Ex 3 matrices: H, X, textbook CX (control q1, target q0 = swap of |10⟩↔|11⟩) and the mirror-image matrix for a bare `CXGate()` (control q0) are right. U_Bell columns are the Bell states.
- Ex 4: all five targets and their gate lists are right, including the step-by-step derivation of target 5 (checked by hand; the notebook's own assertions also verify state and counts).

### Errors found and fixed (text only, no solutions changed)
1. Teaching note on U_Bell said columns 1&3 map to the Φ states and 2&4 to the Ψ states; correct is columns 1&2 (inputs 00, 01) → Φ, columns 3&4 (10, 11) → Ψ.
2. Phase colours were described as "red = 0°, blue = 180°". `plot_statevector` uses hue = phase/2π + 0.5, so 0° is **cyan** and 180° is **red**. Fixed in the teacher notebook and in the one matching comment in the student notebook.
3. Convention note claimed the Bell/target circuits "seed the lowest qubit"; the 3-qubit targets seed qubit 2. Reworded: the seed qubit is the control.
4. Cell with `print(f"U|{start}\rangle ...")`: `\r` is a carriage return in a normal string, garbling the printed output. Replaced `\rangle` with `⟩`.

### Notes (not changed)
- The bonus claim of "~10 minutes of free execution per month" is IBM policy and may change; not verifiable offline.

## 4. Student notebook (exercises_student.ipynb)

Read cell by cell and compared with the teacher notebook.

### Confirmed correct
- Same sections in the same order as the teacher copy: intro/concepts, Ex 1, Ex 2, Ex 3, Ex 4 (five targets), Bonus, wrap-up.
- No solutions leaked: Ex 1/2/4 contain only `# TODO` stubs (target functions only have the measurement loop); stored outputs exist only in the demo cells (1, 5, 7, 8).
- Qubit-order explanation, the "ab → a is qubit 1" hint in Ex 2, the Ex 4 recipe examples (targets 3 and 4) and the colour note (cyan = 0°, red = 180°) are consistent with the verified conventions.
- The bonus cell is wrapped in try/except and prints a skip message.

### Fixed (text only)
- Ex 1 said the counts "will never be exactly 512/512"; that is false (about 2.5% of runs). Now: "almost never".

### Findings (not changed)
1. **Exercise 3 is already solved in the student notebook** (medium): the gate matrices (cell 23) and the full Bell matrix (cell 24) are given in full, and cell 25 does the H|0> check. The only student action is the optional "TODO: try other starting states". If Ex 3 should be a real exercise, remove or blank cells 23/24. Content decision for the owner.
2. **Ex 2 self-check prints ✅ without checking the point of the exercise** (medium): the comment says the two phi states "must NOT be identical" but the cell only prints `Same internal state? False`; nothing asserts it, and `✅` is printed regardless. Suggest `assert not np.allclose(...)` or a fidelity-based check (changes what the check accepts, so needs approval).
3. **Ex 1 cell 14**: "this may already be the right answer" gives the answer away; harmless, but could say "check this is the gate you used".
4. **Ex 1 TODO**: the measurement line is commented out (`# q1.measure(0, 0)`); a student who forgets to uncomment gets the raw Qiskit error from `simulate` (see section 1, finding 2). Add a hint "uncomment this line".
5. **Ex 4 recipe step 3** (anti-correlation) is the densest paragraph for beginners; "seed goes 0 → 1" is ambiguous about which target is the starting point. Suggest one worked circuit for target 4 or a wording like "in target 4 the two strings differ in qubits 2 and 0, in opposite directions".
6. **Ex 4 self-check** stops at the first failing target (assertion), fine, but later targets are not run; mention "fix targets in order".
7. Setup cell and intro tell students to use `.venv`; `.venv-container` is only the sandbox. Check against README in task 5.
8. Wrap-up: the nested bullet under the first point is oddly indented (cosmetic).

Remaining tasks (notebook run, README/pyproject, final summary) are still open.

Note: `pytest` is not in `pyproject.toml` (installed only in `.venv-container`). Adding it as an optional dev dependency needs the owner's approval (new dependency) — proposed, not done.
