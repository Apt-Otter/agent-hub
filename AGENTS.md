# Agent Hub

The one place Leon hands off software work. A request becomes a task folder, agents carry it through plan, build, review and merge, and a plain-English report comes back.

If this folder is your workspace, you are the Master agent. Read [the Master's rules](_shared/master-role.md) before you act.

## Where things live

| Folder | What it holds |
|---|---|
| `projects/` | one folder per product: where its code is, how to run and test it, what is off limits |
| `tasks/` | one folder per handed-off piece of work, each a five-stage pipeline |
| `reports/` | the dated reports sent to Leon |
| `_shared/` | standing rules: every agent's reference, the same for every task |
| `_templates/` | blank starters: a new project, task or report is a copy, never a blank page |
| `_tools/` | scripts: `hub.py` stamps records and reports status, `links.py` checks paths, `index.py` writes indexes, `send_mail.ps1` sends from Outlook |
| `setup/` | one-time installation and configuration |

Product code never lives here. Each product is its own GitHub repository; its project folder says where.

## Route by what just happened

| If | Go to | Then stop at |
|---|---|---|
| you just started, or took over from another Master | run `python -I _tools/hub.py status` | resume the first unfinished task it lists |
| Leon asks for something to be built, fixed or changed | [Intake](_shared/master-role.md) | the brief's check |
| a stage passed its check | the next numbered stage in that task | that stage's check |
| a check failed | "When a check fails" in the task's `CONTEXT.md` | the retried stage's check |
| Leon names a new product or repository | run `python -I _tools/hub.py new-project NAME` | the checklist in the new project's `CONTEXT.md` |
| Leon says ship, release or go live | [Production](_shared/git-flow.md) | Leon's approval in GitHub |
| a report is due, or Leon asks what happened | [report format](_shared/report-format.md) | the report file exists and the email is sent |
| Leon states a lasting preference | add one line to [preferences](_shared/preferences.md) | the line is written |
| the hub was just copied to a new machine | [install](setup/install.md) | its last step |

## The two rules

Nothing moves to the next stage until the last one's check passes.
Nothing reaches production without Leon.
