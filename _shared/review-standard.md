# Review standard

What a reviewer checks. A finding in the first four groups fails the review; the fifth is advice.

1. **Does it do what was asked?** Every acceptance criterion in the brief is met, and a test proves it. Nothing was built that the brief did not ask for.
2. **Is it correct?** Wrong results, unhandled errors, broken edge cases, queries that return the wrong rows, a migration that would lose data.
3. **Is it safe?** No secrets in the code. SQL is parameterised, never built by joining strings. User input is validated. Nothing in the project's "Off limits" list was touched.
4. **Do the tests mean anything?** They would fail if the feature were removed. They do not test only that the code runs.
5. **Does it fit?** Naming, structure and style match the code around it.

## Writing a finding

One per problem: the file and line, what is wrong, what input or situation shows it, and why it matters. No finding without a location. Do not rewrite the code in the review.

## The verdict

`check.md`, first line `pass` or `fail: <the most serious finding in one sentence>`. Pass means you would be content for this to go live as it is.
