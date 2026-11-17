# 03_build - write the code and tests

One job: implement the plan on the task's branch, with tests. Role: Builder.

## Inputs
- Working (this run): `../01_intake/output/brief.md`
- Working (this run): `../02_plan/output/plan.md`
- Working (this run): `../04_review/output/review.md`, only if it exists
- Working (this run): `output/check.md`, only if it exists and says fail
- Reference (every run): `../../../projects/{project}/CONTEXT.md`
- Reference (every run): `../../../_shared/git-flow.md`

Do NOT load: other tasks, the review standard, the whole `_shared/` folder.

## Process
1. If the plan is missing or its check did not pass, stop and say so.
2. Work in the product repository on branch `task/{task}`, cut from the development branch. If the branch exists, continue on it.
3. Implement the plan. Write the tests it names. If this is a retry, fix every finding in the review first.
4. Run the project's test command from its profile. Fix failures you caused. Do not delete or weaken a test to make it pass.
5. Commit and push the branch.
6. Write `build.md`: the branch name, the commits, what was changed in plain English, and the last lines of the test run.
7. If the plan turned out to be wrong, write why in `build.md`, write `check.md` as `fail: plan is wrong, <why>`, and stop.

## Outputs
- `build.md` -> `output/`
- commits on `task/{task}` in the product repository

## Check
A script: run the project's test command on the task branch. Exit code 0 writes `output/check.md` with first line `pass`; anything else writes `fail: <the first failing test>`. If the project profile has no test command, this task must be the one that creates it; otherwise write `fail: project has no test command` and stop.
