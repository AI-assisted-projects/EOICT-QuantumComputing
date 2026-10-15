# Plan: QC

## Goal
A beginner quantum-computing course with Python and Qiskit: a student workbook
(`exercises_student.ipynb`), a teacher copy with every exercise solved (`solutions_teacher.ipynb`)
and a small helper package `qclab/` (runner, states, viz, self-checks). Everything runs on the local
simulator; one optional bonus runs on real IBM Quantum hardware.

There is no new roadmap. Work arrives as accepted owner suggestions from Telegram; each one becomes a
milestone here (see Milestones).

## Constraints
- Python 3.11–3.13, dependencies in `pyproject.toml`, managed with uv on the host. `uv` isn't in the
  container image yet; until it is, install into `.venv-container` with its own pip
  (`.venv-container/bin/pip install -e .`).
- Python environments: `.venv` belongs to the owner on the host (Python 3.13) and doesn't work in
  this container (Python 3.12), and vice versa. Never create, rebuild or modify `.venv`. In the
  container use `.venv-container/` (gitignored): create it with `python3 -m venv .venv-container`
  if it's missing and install the project's dependencies there.
- Audience: beginners. Keep explanations short and concrete; every exercise keeps its self-check.
- The two notebooks stay in sync: the same exercises in the same order. The student notebook
  never contains solutions; the teacher notebook has every solution plus teaching notes.
- Verification: both notebooks run top to bottom without errors on the simulator (for example
  `.venv-container/bin/jupyter nbconvert --to notebook --execute <nb> --output /tmp/<nb>`),
  with the IBM bonus skipped (install `nbconvert` and `ipykernel` into `.venv-container` for this);
  plus a quick import/run of changed `qclab/` functions.
- Commit notebooks with their outputs cleared or as they were; don't commit large outputs.
- Never run destructive file operations (`git clean`, `git reset --hard`, `git checkout .`,
  `rm -rf`, mass deletes) in this repository, and never delete data, model weights, outputs or
  build artifacts to "clean up". Only remove what a task strictly needs; when in doubt, ask.
- Never print, log or commit secrets; `.env` stays local.

## Out of scope
- Running anything on real IBM Quantum hardware.

## Ask the owner about
- Changing the course structure (adding, removing or reordering exercises).
- Changing what the self-checks accept.
- New dependencies.

## Allowed external access
- None. Never use the IBM Quantum token in `.env` (real hardware has limited quota); the bonus is
  only checked to skip cleanly.
- Downloading Python packages.

## Milestones
None planned. Accepted suggestions add milestones here, marked `(💡 accepted suggestion S<n>)`.

### M0 — Minimal plan
- Deliverable: this plan, so suggestions can be added to the project.
- Verification: review of the plan files.

## Delegation notes
Qwen may draft explanation text and extra self-check cases. Not the solutions themselves.
