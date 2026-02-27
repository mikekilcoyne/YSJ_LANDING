---
type: index
---

# Planning Start Here

| Item | Status | Notes |
|------|--------|-------|
| Workflow selected (`new app`, `extend app`, or `module`) | [ ] | |
| Epic drafted with minimum planning spec | [ ] | |
| Tasks pass Definition of Ready | [ ] | |
| Sprint commitment agreed | [ ] | |

## Purpose

Use this file when planning work so you can scope delivery without digging through unrelated repository areas.

## Choose a Workflow

1. Planning a new app: open `playbooks/new-app.md`.
2. Extending an existing app: open `playbooks/extend-app.md`.
3. Creating or extracting a module: open `playbooks/new-module.md`.
   - Run the "Module Decision Heuristics" section first.

## Required Reading Order

1. `sprint-summaries.md` — quick overview of what's been done and which epics are in flight
2. `process.md`
3. `agents.md`
4. Relevant playbook (`playbooks/new-app.md`, `playbooks/extend-app.md`, or `playbooks/new-module.md`)
5. Relevant epic docs in `epics/`

## Required Outputs

1. Epic doc using `templates/epic.md` with complete planning sections.
2. Task docs/checklist items that satisfy Definition of Ready.
3. Sprint file only after commitment is clear.

## Minimum Planning Standard

1. Scope and non-goals are explicit.
2. Impacted app/module/code touchpoints are listed.
3. Dependencies, risks, and rollout/validation approach are documented.
4. Acceptance criteria are testable.

## Guardrails

1. Use PM steering sections (`PM Expectations` and `PM Goals`) as source-of-truth direction.
2. Do not begin implementation from an epic missing core planning sections.
