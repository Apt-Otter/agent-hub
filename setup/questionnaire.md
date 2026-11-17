# Setup questionnaire - configure the hub once

The Master asks Leon these, once, on first run. Answers are written where shown. No later run should ask them again.

1. Which email address should reports go to, and at what time each day? (the two lines under Reporting in `_shared/preferences.md`)
2. Should tasks run strictly one at a time, or may two run together when they are in different projects? (Working rules in `_shared/preferences.md`)
3. Is there anything no agent should ever do on this machine: folders to stay out of, services not to restart, accounts not to use? (Working rules in `_shared/preferences.md`)
4. What is the first product, and where is its repository? (run `python -I _tools/hub.py new-project NAME`, then follow that project's checklist)
5. How do you want to be told something needs you between reports: wait for the report, or a message straight away? (Reporting in `_shared/preferences.md`)

## Then find a way to send email

Leon uses Outlook. Try these in order, send a test message with each until one arrives, and record the one that worked as the "Email method" line under Reporting in `_shared/preferences.md`.

1. `connector`: a Microsoft 365 or Outlook tool available to you that can send mail, not only read it.
2. `outlook-desktop`: run `powershell -File _tools/send_mail.ps1 -To ADDRESS -Subject "Hub test" -BodyFile setup/questionnaire.md`. This needs classic Outlook for Windows, signed in.
3. `none`: neither worked. Reports are posted in Traycer only. Tell Leon, and say which of the two he would need to set up.

Leon confirms the test message arrived before the method is recorded.
