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
- [ ] Review qclab/check.py and qclab/viz.py. Test every self-check with the correct answer, a wrong answer and an edge case. Don't change what checks accept without asking; list proposed changes in REVIEW.md. (💡 accepted suggestion S10)
- [ ] Review the teacher notebook exercise by exercise: verify each solution, physics claims and gate conventions (CX control/target, bit order, phases). Record errors in REVIEW.md and fix clear factual mistakes in the text. (💡 accepted suggestion S10)
- [ ] Review the student notebook: no solutions, same exercises in same order as teacher copy, wording clear for beginners. Record findings in REVIEW.md. (💡 accepted suggestion S10)
- [ ] Run both notebooks top to bottom in .venv-container with the IBM bonus skipped; confirm the bonus skips cleanly without using the token. Check pyproject.toml dependencies and README accuracy. (💡 accepted suggestion S10)
- [ ] Write the final summary in REVIEW.md: confirmed correct, bugs fixed, prioritised suggestions (incl. changes needing owner approval). (💡 accepted suggestion S10)

## Session log
<!-- Newest first: YYYY-MM-DD — task — result — how verified — Qwen used? (y/n) -->
- 2026-10-18 — M1 task 1: review states.py/runner.py — done; no bugs, 5 minor findings in REVIEW.md, 15 pytest checks added in tests/ — pytest 15 passed in .venv-container — n
- 2026-10-18 — bookkeeping cleanup (S9) — done — checked PROGRESS/PLAN/DECISIONS agree, PR #1 confirmed merged via gh — n
- 2026-10-15 — minimal plan written at the owner's request (no session) — done — PR #1 merged 2026-10-15 — n
