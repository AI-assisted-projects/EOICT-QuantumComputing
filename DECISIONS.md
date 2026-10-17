# Decisions: QC

<!--
One entry per decision, newest first:

## D<n> — <short title> (YYYY-MM-DD)
- Context:
- Decision / default taken:
- Asked owner: no | yes (question id, answer)
- Status: decided | provisional (awaiting answer) | superseded by D<m>
-->

## D3 — Add M1 full review (S10) (2026-10-18)
- Context: accepted suggestion S10: "since the project was written in the most part by Qwen, I don't trust it. Check everything and make some suggestions along the way." Placement: new M1 – Full review of qclab and notebooks.
- Decision: added M1 to PLAN.md and PROGRESS.md with the six proposed tasks. Branch feat/m1-full-review is stacked on feat/m0-bookkeeping-cleanup (PR #2 not yet merged), so D3 follows D2 from that branch.
- Asked owner: no
- Status: decided

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
