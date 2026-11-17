---
title: {project}
description: not described yet
status: onboarding
created: {date}
---

# Project {project}

Everything an agent needs to work on this product without asking. Stage agents read this file on every task, so keep it short and true.

## What it is

{One paragraph: what the product does and who uses it.}

## Where the code is

- GitHub repository: {url}
- Folder on this machine: {absolute path}
- Stack: {languages, framework, database}

## Commands

Run from the repository folder.

- Install: `{command}`
- Run locally: `{command}`
- Test: `{command}`
- Migrate the development database: `{command}`

## Branches

- Production: `production`
- Development: `dev`

## Databases

- Development: {name and how to connect; this is the only one agents use}
- Production: {name only, so agents can recognise and avoid it}

## Off limits

{Files, folders, tables or services no agent may change without Leon. "None" if none.}

## Deploy

not set up

## Onboarding checklist

The Master works through this once, then sets `status: active` above and runs `python -I _tools/index.py projects`.

1. Fill in every section above by reading the repository. Ask Leon only for what the code cannot tell you.
2. Confirm the repository is on GitHub and that this machine can push to it.
3. Create the `dev` and `production` branches if they do not exist.
4. Ask Leon to protect `production` in GitHub: require a pull request and one approval.
5. Confirm the app runs locally against a development database that is not the production one.
6. If there is no test command, the first task for this project is "Test baseline": choose a test runner, write tests for the paths that matter most, and record the command above. No other task can pass its build check until this one is done.
7. Run `python -I _tools/links.py` and fix anything it reports.
