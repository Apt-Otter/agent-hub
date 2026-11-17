# 04_review - read the change cold

One job: judge the change on the task branch against the brief. Role: Reviewer. This agent must not be the one that built it.

## Inputs
- Working (this run): `../01_intake/output/brief.md`
- Working (this run): `../03_build/output/build.md`
- Working (this run): the diff of this task's branch (named in the task's own CONTEXT file) against the development branch, in the product repository
- Reference (every run): `../../../_shared/review-standard.md`
- Reference (every run): `../../../projects/{project}/CONTEXT.md`

Do NOT load: the plan, earlier reviews, other tasks. Judge what was built, not what was intended.

## Process
1. If the build check did not pass, stop and say so.
2. Read the whole diff, and the code around each change.
3. Run the tests yourself. Do not take `build.md`'s word for it.
4. Write `review.md`: one finding per problem, in the form the review standard gives, most serious first. If there are none, say so in one line.
5. Change no code.

## Outputs
- `review.md` -> `output/`

## Check
The reviewer writes `output/check.md`, first line `pass` or `fail: <the most serious finding>`, by the verdict rule in the review standard.
