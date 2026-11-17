# 01_intake - write down what Leon wants

One job: turn Leon's request into a brief an agent with no other context can build from. The Master does this stage itself.

## Inputs
- Working (this run): Leon's request, from the conversation
- Reference (every run): `../../../projects/{project}/CONTEXT.md`
- Reference (every run): `../../../_shared/preferences.md`

Do NOT load: the product's source code, other tasks.

## Process
1. Write `brief.md` with four sections: **Request** (Leon's own words, quoted), **Why** (what it is for, if he said), **Acceptance criteria** (numbered, each one something a test or a person can confirm true or false), **Out of scope** (what this task will not do).
2. If a criterion cannot be made checkable without a decision from Leon, ask him now, in the conversation. Ask once, with all the questions together.
3. If he is not there to answer, set the task's `status: waiting-on-leon` and write the questions under Notes in the task's `CONTEXT.md`.
4. Keep it under one page.

## Outputs
- `brief.md` -> `output/`

## Check
The Master rereads the brief as the builder would: could two different agents build from it and produce the same behaviour? If yes, write `output/check.md` with first line `pass`. If no, fix the brief or ask Leon.
