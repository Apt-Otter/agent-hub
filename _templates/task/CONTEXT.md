---
title: {title_yaml}
description: {project}
status: queued
project: {project}
created: {date}
---

# Task {task} - {title}

One piece of work for the `{project}` project, carried through five stages. Its rules are in the [project profile](../../projects/{project}/CONTEXT.md).

| Stage | Job | Output |
|---|---|---|
| [01_intake](01_intake/CONTEXT.md) | write down what Leon wants | `brief.md` |
| [02_plan](02_plan/CONTEXT.md) | decide what to change | `plan.md` |
| [03_build](03_build/CONTEXT.md) | write the code and tests | `build.md` |
| [04_review](04_review/CONTEXT.md) | read the change cold | `review.md` |
| [05_merge](05_merge/CONTEXT.md) | merge to the development branch | `summary.md` |

Branch in the product repository: `task/{task}`.

## Status

The `status:` line above is one of `queued`, `in-progress`, `waiting-on-leon`, `blocked`, `done`. Only the Master changes it. A stage is complete when its `output/check.md` starts with `pass`.

## When a check fails

1. Leave the failed `check.md` in place: it is the next attempt's input.
2. Find the stage to redo. A failed plan check redoes `02_plan`. A failed build, review or merge check redoes `03_build`.
3. Start a fresh agent on that stage. It reads the failed `check.md` and the review, fixes the cause, and overwrites the stage's output.
4. Rerun every later stage in order.
5. Add one line under Notes: the date, the stage that failed, and why.

After three failures of the same check, set `status: blocked`, write the reason under Notes, and stop work on this task.

## Notes

