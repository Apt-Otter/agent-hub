# Install - move the hub to a new machine

For whoever sets the hub up on Leon's Windows PC. Done once.

## Before you start

The machine needs Git, Python 3, the GitHub command line tool (`gh`, signed in as Leon), Traycer, and Leon's Claude connection inside Traycer.

On Windows the Python command may be `py` instead of `python`. If so, read `py` wherever these files say `python`.

## Steps

1. Get the hub onto the PC, somewhere short such as `C:\hub`: clone the blank hub repository, or copy the folder. A copy must include the hidden `.claude` folder: it holds the ICM skill the hub was built with.
2. In that folder, run `python -I _tools/links.py`. It should end with `0 broken`.
3. Give this hub its own private GitHub repository under Leon's account, so his tasks and reports never go back to the blank one. If the folder was cloned, run `git remote remove origin` first. Then run `gh repo create hub --private --source . --push`. The hub's history is its backup.
4. In Leon's Claude settings, connect Gmail.
5. In Traycer, open the `hub` folder as the workspace and start a chat with: `Read AGENTS.md. You are the Master. Start with setup/questionnaire.md.`
6. Answer the questionnaire with Leon. It ends with a test email: confirm it arrives.
7. Ask the Master to schedule the daily report at the time Leon chose, and confirm it tells you which scheduling tool it used.
8. Add the first project. Its checklist ends with the "Test baseline" task.

## Not yet proven

These were not testable where the hub was built. Check each on the PC and fix the file named if it does not hold.

| Assumption | Check | If wrong, edit |
|---|---|---|
| The Master can create and message Traycer agents and worktrees | ask it to run one stage of the Test baseline task | `_shared/master-role.md`, Running a stage |
| The Master can send mail through the Gmail connector | step 6 | `_shared/report-format.md`, Where |
| Traycer can wake the Master on a schedule while Leon is away | step 7, then see whether the next day's report arrives unprompted | `_shared/report-format.md`, When |
| The PC does not sleep while work is queued | Windows power settings | nothing in the hub |
| Leon's Claude plan can carry a task through all five stages in one session | watch the first full task | `_shared/master-role.md`, Pace |

## Changing the hub later

The hub follows the ICM method. To add a stage, a role or a new kind of record, ask the Master to use the `icm-architect` skill, and rerun `python -I _tools/links.py` afterwards.
