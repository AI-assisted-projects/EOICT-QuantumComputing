# Progress: QC

Status: done
<!-- The runner reads this line: planning | active | blocked | done -->
Blocked reason: -
Current milestone: M2 done (PR open); no further milestones

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
- [x] Ex 2 self-check in the student notebook must assert the point of the exercise (the two phi states differ) instead of always printing. (REVIEW.md M1 suggestion 1; student notebook section 4 #2)
- [x] Ex 3 must NOT stay pre-solved in the student notebook: remove or blank the given gate matrices and Bell matrix cells (cells 23/24) so students do the work; keep the teacher notebook as the solution. (REVIEW.md M1 suggestion 2; owner decision)
- [x] Add `ipykernel` to the dependencies and `pytest` as an optional dev dependency in pyproject.toml. (REVIEW.md M1 suggestion 3)
- [x] Validate bit-string length and expected probabilities in `check.py` and raise clear `ValueError`s; add tests. (REVIEW.md M1 suggestion 4)
- [x] Optional `seed` argument in `simulate`, and a friendly error when a circuit has no measurements; add tests. (REVIEW.md M1 suggestion 5)
- [x] Student-notebook wording: "uncomment this line" hint in Ex 1, clearer Ex 4 recipe step 3, better bonus skip message, cosmetic indentation in the wrap-up. (REVIEW.md M1 suggestion 6)
- [x] Low priority: fix the float-fragile boundary in `assert_distribution` and review the statistical power of the 5% tolerance. (REVIEW.md M1 suggestion 7)

## Session log
- 2026-10-18 — final check: all plan tasks done, PR #4 open without review comments, no new answers or suggestions; Status set to done — bookkeeping only — n
<!-- Newest first: YYYY-MM-DD — task — result — how verified — Qwen used? (y/n) -->
- 2026-10-18 — M2 task 7: `assert_distribution` boundary fixed with 1e-9 epsilon (exactly-at-tol now passes); tol 0.05 left unchanged (statistical power: ~3σ at 1024 shots, documented in REVIEW.md, use `simulate(seed=...)` for determinism) — done — 2 new tests, pytest 26 passed — n
- 2026-10-18 — M2 task 6: student notebook wording (Ex 1 uncomment hint, Ex 4 step 3 summary line, bonus skip message with exception type and hint, wrap-up indentation) — done — notebook JSON loads, diff reviewed (text only, 9 lines); not executed — n
- 2026-10-18 — M2 task 5: `simulate(seed=None)` optional seed; ValueError with a measure_all hint when no measurements — done; old test expecting QiskitError updated, seed test added — pytest run — n
- 2026-10-18 — M2 task 4: check.py validates bit-string chars/length, expected_probs (non-empty, non-negative, sums to 1) and empty counts with ValueError — done; two old tests that documented the silent behaviour updated, one new test — pytest all passed — n
- 2026-10-18 — M2 task 3: ipykernel added to dependencies, pytest as optional `dev` extra — done — pyproject parses with tomllib, pytest 22 passed (deps not reinstalled) — n
- 2026-10-18 — M2 task 2: Ex 3 no longer pre-solved — done; student cells 23-25 replaced by TODO stubs with tool hints (CX textbook note kept), outputs cleared; teacher notebook untouched — notebook JSON loads, grep confirms no later cell uses the removed variables; not executed (stubs only) — n
- 2026-10-18 — M2 task 1: Ex 2 self-check asserts the phi states differ (overlap < 0.99) — done; student notebook cell 21 only — checked the logic with Qiskit on the correct pair (overlap 0 passes) and a wrong pair (same state, overlap 1 fails); notebook JSON diff is 4 lines — n
- 2026-10-18 — PR #3 feedback — added M2 with 7 tasks for the owner-approved suggestions (Ex 3 must not stay pre-solved); no code changed — docs only, checked against REVIEW.md lines 118-126 and PR comments — n
- 2026-10-18 — M1 task 6: final summary in REVIEW.md — done; confirmed-correct list, fixes and 7 prioritised suggestions (4 need owner approval) — docs only, re-read against sections 1-5 — n
- 2026-10-18 — M1 task 5: run notebooks, check pyproject/README — done; teacher runs clean, student runs up to its TODO stubs, bonus skips cleanly; run in a copy without .env so the token was never used; 4 findings (IPython/ipykernel missing from deps) in REVIEW.md — custom exec runner (no nbconvert), pytest 22 passed — n
- 2026-10-18 — M1 task 4: review student notebook — done; no leaked solutions, order matches teacher; 1 text error fixed ("never 512/512"), 8 findings in REVIEW.md (Ex 3 is pre-solved, Ex 2 check doesn't assert) — read cell by cell vs teacher notebook, JSON still valid; not executed (task 5) — n
- 2026-10-18 — M1 task 3: review teacher notebook — done; 4 text errors fixed (column mapping, phase colours, convention note, \r in f-string), solutions all correct — hand derivation + simulator checks of matrices/states; notebook not re-executed yet (task 5) — n
- 2026-10-18 — M1 task 2: review check.py/viz.py — done; no bugs fixed, 8 findings (5 proposals needing approval) in REVIEW.md, 7 tests added — pytest 22 passed in .venv-container — n
- 2026-10-18 — M1 task 1: review states.py/runner.py — done; no bugs, 5 minor findings in REVIEW.md, 15 pytest checks added in tests/ — pytest 15 passed in .venv-container — n
- 2026-10-18 — bookkeeping cleanup (S9) — done — checked PROGRESS/PLAN/DECISIONS agree, PR #1 confirmed merged via gh — n
- 2026-10-15 — minimal plan written at the owner's request (no session) — done — PR #1 merged 2026-10-15 — n
