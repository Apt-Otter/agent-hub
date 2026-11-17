# 05_merge - merge to the development branch

One job: merge the reviewed branch into the development branch and say, in plain English, what Leon now has. Role: Builder.

## Inputs
- Working (this run): `../01_intake/output/brief.md`
- Working (this run): `../03_build/output/build.md`
- Working (this run): `../04_review/output/check.md`
- Reference (every run): `../../../projects/{project}/CONTEXT.md`
- Reference (every run): `../../../_shared/git-flow.md`

Do NOT load: the plan, the review's findings, other tasks.

## Process
1. If the review check does not say `pass`, stop. Do not merge.
2. Update the development branch, then merge `task/{task}` into it. If there is a conflict you cannot resolve without changing behaviour, abort the merge and fail the check.
3. Run the project's test command on the development branch.
4. If it passes, push. If it fails, undo the merge before pushing anything.
5. Write `summary.md` for Leon, under 150 words: what now works that did not before, anything he should try by hand, anything he should know before the next release. Then the branch, and the link to the merge commit. No description of how the agents worked.

## Outputs
- `summary.md` -> `output/`
- the merge commit on the development branch

## Check
A script: the project's test command, run on the development branch after the merge. Exit code 0 writes `output/check.md` with first line `pass`; anything else means the merge was undone, and writes `fail: <why>`. Never merge to the production branch from this stage.
