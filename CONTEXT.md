# Agent Hub - how work flows

The flow in one line: Leon asks, the Master writes it down, one agent per stage plans, builds, reviews and merges it, and Leon reads the report.

Two shelves and one pipeline:

- `projects/` is a shelf of project profiles. Each is a copy of `_templates/project/`.
- `tasks/` is a shelf of tasks. Each is a copy of `_templates/task/` and is itself a pipeline:

| Stage | Job | Checked by |
|---|---|---|
| `01_intake` | write down what Leon wants | the Master, with Leon if unclear |
| `02_plan` | decide what to change | a reviewer agent |
| `03_build` | write the code and tests | the project's test command |
| `04_review` | read the change cold | a reviewer agent that did not build it |
| `05_merge` | merge to the development branch | the tests, run again after the merge |

Each stage's own `CONTEXT.md` holds its inputs, outputs and check.

Factory (stable, every task): `_shared/` and each project's `CONTEXT.md`.
Product (new each task): each stage's `output/`, and the dated files in `reports/`.

## Status

Status is whatever is on disk. A stage is complete when its `output/` holds `check.md` with first line `pass`. A task's own state is the `status:` line in its `CONTEXT.md`:

`queued` -> `in-progress` -> `done`, with `waiting-on-leon` and `blocked` as the two places it can pause.

`python -I _tools/hub.py status` reads all of this and prints one line per open task. `projects/_index.md` and `tasks/_index.md` are generated; never edit them by hand.

## Production is not a stage

A finished task ends on the development branch. Going live is a separate act that Leon starts and Leon approves: see [git flow](_shared/git-flow.md).
