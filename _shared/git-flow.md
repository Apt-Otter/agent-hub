# Git flow

The branch rules for every project. A project profile may rename the branches; it may not relax the rules.

## Branches

| Branch | What it is | Who writes to it |
|---|---|---|
| `production` | what is live | nobody directly: only a pull request Leon approves |
| `dev` | finished, checked work | the merge stage, after review passes |
| `task/<task-id>` | one task in progress, cut from `dev` | that task's builder |

## Rules for agents

- Start every task branch from the current `dev`.
- Commit in small steps with plain messages that say what changed and why.
- Merge to `dev` only from stage `05_merge`, only after `04_review` passed.
- Never force-push. Never rewrite history on `dev` or `production`.
- Never commit secrets, `.env` files, database dumps or customer data.
- Never connect to a production database. Use the development database named in the project profile.
- A schema migration is written as a migration file and run against the development database only.

## Production

Going live is Leon's call, every time.

1. Leon asks for a release.
2. The Master opens a pull request from `dev` to `production` in GitHub. Its description lists, in plain English, each task included since the last release, with a link to the task's `05_merge/output/summary.md`.
3. Leon reads it and approves or declines in GitHub.
4. The merge to `production` is what triggers deployment.

No agent approves or merges that pull request. Protect the `production` branch in GitHub so this is enforced by GitHub and not by good behaviour: require a pull request and one approval.

## Deployment

Each project records its own deployment under "Deploy" in its profile. Until a project has a hosting target, that section says `not set up`, and a release stops after step 3.
