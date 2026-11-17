#!/usr/bin/env python3
"""Stamp new projects and tasks from _templates/, and report status from what is on disk.

Run from anywhere:
    python -I _tools/hub.py new-project NAME
    python -I _tools/hub.py new-task PROJECT "Short title"
    python -I _tools/hub.py status [--all]

new-project copies _templates/project/ to projects/NAME/.
new-task copies _templates/task/ to tasks/NNNN-short-title/, numbered after the highest task so far.
Both fill in the {project}, {task}, {title} and {date} placeholders and rebuild the indexes.
status prints one line per task that is not done (every task with --all): its status line, and
the first stage whose output/check.md does not start with "pass". Standard library only.
"""
import datetime
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40].strip("-")


def stamp(template, dest, values):
    if dest.exists():
        sys.exit(f"{dest.relative_to(ROOT).as_posix()} already exists")
    shutil.copytree(ROOT / "_templates" / template, dest)
    for f in dest.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        for key, value in values.items():
            text = text.replace("{" + key + "}", value)
        f.write_text(text, encoding="utf-8", newline="\n")


def reindex():
    subprocess.run([sys.executable, "-I", str(ROOT / "_tools" / "index.py"), "projects", "tasks"], check=True)


def field(path, name):
    m = re.search(rf"^{name}:\s*(.+)$", path.read_text(encoding="utf-8-sig", errors="replace"), re.M)
    return m.group(1).strip() if m else ""


def new_project(name):
    name = slug(name)
    if not name:
        sys.exit("a project needs a name")
    stamp("project", ROOT / "projects" / name, {"project": name, "date": datetime.date.today().isoformat()})
    reindex()
    print(f"created projects/{name}/ - work through the checklist in its CONTEXT.md")


def new_task(project, title):
    project = slug(project)
    if not (ROOT / "projects" / project / "CONTEXT.md").is_file():
        sys.exit(f"no project named {project}: run new-project first")
    if not slug(title):
        sys.exit("a task needs a title")
    numbers = [int(d.name[:4]) for d in (ROOT / "tasks").iterdir() if d.is_dir() and re.match(r"\d{4}-", d.name)]
    task = f"{max(numbers, default=0) + 1:04d}-{slug(title)}"
    stamp("task", ROOT / "tasks" / task, {
        "project": project, "task": task, "title": title, "title_yaml": json.dumps(title),
        "date": datetime.date.today().isoformat()})
    reindex()
    print(f"created tasks/{task}/ - start at 01_intake/CONTEXT.md")


def status(show_all):
    shown = 0
    for task in sorted(d for d in (ROOT / "tasks").iterdir() if (d / "CONTEXT.md").is_file()):
        state = field(task / "CONTEXT.md", "status") or "no status"
        if state == "done" and not show_all:
            continue
        where = "all stages passed"
        for stage in sorted(d for d in task.iterdir() if d.is_dir() and re.match(r"\d\d_", d.name)):
            check = stage / "output" / "check.md"
            lines = check.read_text(encoding="utf-8-sig", errors="replace").strip().splitlines() if check.is_file() else []
            verdict = lines[0].strip() if lines else ""
            if not verdict.lower().startswith("pass"):
                where = f"{stage.name}: {verdict}" if verdict else f"next: {stage.name}"
                break
        print(f"{task.name} [{state}] {field(task / 'CONTEXT.md', 'project')} - {where}")
        shown += 1
    if not shown:
        print("no tasks" if show_all else "no open tasks")


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == "new-project":
        new_project(args[1])
    elif len(args) == 3 and args[0] == "new-task":
        new_task(args[1], args[2])
    elif args and args[0] == "status" and args[1:] in ([], ["--all"]):
        status(args[1:] == ["--all"])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
