# Decisions: QC

<!--
One entry per decision, newest first:

## D<n> — <short title> (YYYY-MM-DD)
- Context:
- Decision / default taken:
- Asked owner: no | yes (question id, answer)
- Status: decided | provisional (awaiting answer) | superseded by D<m>
-->

## D2 — Bookkeeping cleanup (2026-10-18)
- Context: accepted suggestion S9: "clean up the bookkeeping of this project. Apparently you're waiting on an open PR and I didn't find one." PROGRESS.md still said the M0 PR was open, but PR #1 was merged.
- Decision: set Current milestone to "M0 done (merged, PR #1)" and fix the M0 log line. The merged branch feat/m0-plan is kept (not deleted, per rules); the owner can delete it.
- Asked owner: no
- Status: decided

## D1 — Minimal plan, work arrives as suggestions (2026-10-15)
- Context: QC is an existing project with nothing new to plan; the owner adds work as
  suggestions via Telegram.
- Decision: no milestones up front; `Status: done` so the runner stays idle until a suggestion is
  accepted, which then adds a milestone and reactivates the project.
- Asked owner: yes
- Status: decided
