# Report format

How the Master reports to Leon. He is technical and can read a diff, but the report is plain English first.

## When

- Once a day, at the time set in [preferences](preferences.md), if anything changed since the last report.
- Whenever Leon asks what happened.
- Before handing over to a new Master.

## Where

1. Copy `_templates/report.md` to `reports/YYYY-MM-DD.md` and fill it in. A second report on the same day replaces the first.
2. Post the same text in the Traycer conversation.
3. Email it to the address in [preferences](preferences.md) from Leon's own Gmail, using the Gmail connector. Subject: `Hub report YYYY-MM-DD: N done, N waiting on you`.

If the Gmail connector is not available, say so in the Traycer post and under "Problems" in the report file. Never report an email as sent when it was not.

## What goes in

Build it from disk, not from memory: run `python -I _tools/hub.py status --all`, then read each task's `05_merge/output/summary.md`.

- Lead with what needs Leon. If nothing does, say that first.
- One short paragraph per finished task: what now works that did not before, in his words, not the code's. Then the branch and the link to the change.
- For anything blocked or waiting, the one question or decision that would unblock it.
- No play-by-play of what the agents did. No praise of the work.

## Check

The report file exists for today, every task named in it matches its `status:` on disk, and the email was sent or its failure is stated.
