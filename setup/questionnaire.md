# Setup questionnaire - configure the hub once

The Master asks Leon these, once, on first run. Answers are written where shown. No later run should ask them again.

1. Which email address should reports go to, and at what time each day? (the two lines under Reporting in `_shared/preferences.md`)
2. Should tasks run strictly one at a time, or may two run together when they are in different projects? (Working rules in `_shared/preferences.md`)
3. Is there anything no agent should ever do on this machine: folders to stay out of, services not to restart, accounts not to use? (Working rules in `_shared/preferences.md`)
4. What is the first product, and where is its repository? (run `python -I _tools/hub.py new-project NAME`, then follow that project's checklist)
5. How do you want to be told something needs you between reports: wait for the report, or a message straight away? (Reporting in `_shared/preferences.md`)

When all five are answered, send a test report by email so Leon sees one arrive.
