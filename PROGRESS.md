# Progress: QC

Status: active
<!-- The runner reads this line: planning | active | blocked | done -->
Blocked reason: -
Current milestone: M1 — Full review of qclab and notebooks

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
- [ ] Write the final summary in REVIEW.md: confirmed correct, bugs fixed, prioritised suggestions (incl. changes needing owner approval). (💡 accepted suggestion S10)

## Session log
<!-- Newest first: YYYY-MM-DD — task — result — how verified — Qwen used? (y/n) -->
- 2026-10-18 — M1 task 5: run notebooks, check pyproject/README — done; teacher runs clean, student runs up to its TODO stubs, bonus skips cleanly; run in a copy without .env so the token was never used; 4 findings (IPython/ipykernel missing from deps) in REVIEW.md — custom exec runner (no nbconvert), pytest 22 passed — n
- 2026-10-18 — M1 task 4: review student notebook — done; no leaked solutions, order matches teacher; 1 text error fixed ("never 512/512"), 8 findings in REVIEW.md (Ex 3 is pre-solved, Ex 2 check doesn't assert) — read cell by cell vs teacher notebook, JSON still valid; not executed (task 5) — n
- 2026-10-18 — M1 task 3: review teacher notebook — done; 4 text errors fixed (column mapping, phase colours, convention note, \r in f-string), solutions all correct — hand derivation + simulator checks of matrices/states; notebook not re-executed yet (task 5) — n
- 2026-10-18 — M1 task 2: review check.py/viz.py — done; no bugs fixed, 8 findings (5 proposals needing approval) in REVIEW.md, 7 tests added — pytest 22 passed in .venv-container — n
- 2026-10-18 — M1 task 1: review states.py/runner.py — done; no bugs, 5 minor findings in REVIEW.md, 15 pytest checks added in tests/ — pytest 15 passed in .venv-container — n
- 2026-10-18 — bookkeeping cleanup (S9) — done — checked PROGRESS/PLAN/DECISIONS agree, PR #1 confirmed merged via gh — n
- 2026-10-15 — minimal plan written at the owner's request (no session) — done — PR #1 merged 2026-10-15 — n
