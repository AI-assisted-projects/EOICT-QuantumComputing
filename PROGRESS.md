# Progress: QC

Status: active
<!-- The runner reads this line: planning | active | blocked | done -->
Blocked reason: -
Current milestone: M2 (approved M1 suggestions)

## Tasks

### M0 — Minimal plan
- [x] Write PLAN.md, PROGRESS.md and DECISIONS.md

<!-- Accepted suggestions add their milestone and tasks below, marked (💡 accepted suggestion S<n>). -->

### M1 — Full review of qclab and notebooks (💡 accepted suggestion S10)
- [x] Review qclab/states.py and qclab/runner.py: qubit order (Qiskit little-endian), normalisation, shots and seeds. Add quick pytest-style checks for known states (Bell, GHZ, H, X). Write findings to REVIEW.md. (💡 accepted suggestion S10)
- [x] Review qclab/check.py and qclab/viz.py. Test every self-check with the correct answer, a wrong answer and an edge case. Don't change what checks accept without asking; list proposed changes in REVIEW.md. (💡 accepted suggestion S10)
- [x] Review the teacher notebook exercise by exercise: verify each solution, physics claims and gate conventions (CX control/target, bit order, phases). Record errors in REVIEW.md and fix clear factual mistakes in the text. (💡 accepted suggestion S10)
- [x] Review the student notebook: no solutions, same exercises in same order as teacher copy, wording clear for beginners. Record findings in REVIEW.md. (💡 accepted suggestion S10)
- [x] Run both notebooks top to bottom in .venv-container with the IBM bonus skipped; confirm the bonus skips cleanly without using the token. Check pyproject.toml dependencies and README accuracy. (💡 accepted suggestion S10)
- [x] Write the final summary in REVIEW.md: confirmed correct, bugs fixed, prioritised suggestions (incl. changes needing owner approval). (💡 accepted suggestion S10)

### M2 — Apply approved M1 review suggestions (owner-approved on PR #3)
- [ ] Ex 2 self-check in the student notebook must assert the point of the exercise (the two phi states differ) instead of always printing. (REVIEW.md M1 suggestion 1; student notebook section 4 #2)
- [ ] Ex 3 must NOT stay pre-solved in the student notebook: remove or blank the given gate matrices and Bell matrix cells (cells 23/24) so students do the work; keep the teacher notebook as the solution. (REVIEW.md M1 suggestion 2; owner decision)
- [ ] Add `ipykernel` to the dependencies and `pytest` as an optional dev dependency in pyproject.toml. (REVIEW.md M1 suggestion 3)
- [ ] Validate bit-string length and expected probabilities in `check.py` and raise clear `ValueError`s; add tests. (REVIEW.md M1 suggestion 4)
- [ ] Optional `seed` argument in `simulate`, and a friendly error when a circuit has no measurements; add tests. (REVIEW.md M1 suggestion 5)
- [ ] Student-notebook wording: "uncomment this line" hint in Ex 1, clearer Ex 4 recipe step 3, better bonus skip message, cosmetic indentation in the wrap-up. (REVIEW.md M1 suggestion 6)
- [ ] Low priority: fix the float-fragile boundary in `assert_distribution` and review the statistical power of the 5% tolerance. (REVIEW.md M1 suggestion 7)

## Session log
<!-- Newest first: YYYY-MM-DD — task — result — how verified — Qwen used? (y/n) -->
- 2026-10-18 — PR #3 feedback — added M2 with 7 tasks for the owner-approved suggestions (Ex 3 must not stay pre-solved); no code changed — docs only, checked against REVIEW.md lines 118-126 and PR comments — n
- 2026-10-18 — M1 task 6: final summary in REVIEW.md — done; confirmed-correct list, fixes and 7 prioritised suggestions (4 need owner approval) — docs only, re-read against sections 1-5 — n
- 2026-10-18 — M1 task 5: run notebooks, check pyproject/README — done; teacher runs clean, student runs up to its TODO stubs, bonus skips cleanly; run in a copy without .env so the token was never used; 4 findings (IPython/ipykernel missing from deps) in REVIEW.md — custom exec runner (no nbconvert), pytest 22 passed — n
- 2026-10-18 — M1 task 4: review student notebook — done; no leaked solutions, order matches teacher; 1 text error fixed ("never 512/512"), 8 findings in REVIEW.md (Ex 3 is pre-solved, Ex 2 check doesn't assert) — read cell by cell vs teacher notebook, JSON still valid; not executed (task 5) — n
- 2026-10-18 — M1 task 3: review teacher notebook — done; 4 text errors fixed (column mapping, phase colours, convention note, \r in f-string), solutions all correct — hand derivation + simulator checks of matrices/states; notebook not re-executed yet (task 5) — n
- 2026-10-18 — M1 task 2: review check.py/viz.py — done; no bugs fixed, 8 findings (5 proposals needing approval) in REVIEW.md, 7 tests added — pytest 22 passed in .venv-container — n
- 2026-10-18 — M1 task 1: review states.py/runner.py — done; no bugs, 5 minor findings in REVIEW.md, 15 pytest checks added in tests/ — pytest 15 passed in .venv-container — n
- 2026-10-18 — bookkeeping cleanup (S9) — done — checked PROGRESS/PLAN/DECISIONS agree, PR #1 confirmed merged via gh — n
- 2026-10-15 — minimal plan written at the owner's request (no session) — done — PR #1 merged 2026-10-15 — n
