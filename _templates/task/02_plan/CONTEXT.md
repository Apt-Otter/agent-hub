# 02_plan - decide what to change

One job: read the code and write the smallest plan that meets the brief. Role: Planner.

## Inputs
- Working (this run): `../01_intake/output/brief.md`
- Working (this run): `output/check.md`, only if it exists and says fail
- Reference (every run): `../../../projects/{project}/CONTEXT.md`
- Reference (every run): `../../../_shared/git-flow.md`

Do NOT load: other tasks, the review standard, the whole `_shared/` folder.

## Process
1. If the brief is missing or empty, stop and say so.
2. Read the parts of the product repository the brief touches. Change nothing in it.
3. Write `plan.md` with: **Approach** (three sentences), **Files to change** (path and what changes in each), **Tests to add** (one per acceptance criterion, naming the criterion), **Database changes** (migrations, or "none"), **Risks** (what could break that the tests would not catch).
4. If the brief cannot be met as written, say why at the top of the plan and stop.
5. A small task gets a short plan. Do not pad it.

## Outputs
- `plan.md` -> `output/`

## Check
A second agent, in the Reviewer role, reads the brief and the plan and answers: does every acceptance criterion have a change and a test, and does the plan stay inside the project's "Off limits" list? It writes `output/check.md`, first line `pass` or `fail: <why>`.
