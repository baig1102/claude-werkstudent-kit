#!/usr/bin/env python3
"""Structural checks for claude-werkstudent-kit.

Run from the repository root:  python3 scripts/check_kit.py
Exit code 0 = all checks pass. No network access, no third-party packages.

Checks:
1. Every skills/<name>/SKILL.md has frontmatter with `name` equal to the folder
   name and a `description` under 1024 characters without angle brackets.
2. Every tracker CSV parses, has exactly the columns listed in tracker/schema.md,
   and every row has as many fields as the header.
3. Placeholders in double curly braces appear only in template-type files.
4. Every relative Markdown link points to a file or folder that exists.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PLACEHOLDER_ALLOWED = {
    "project/project-instructions.template.md",
    "project/watchlist.template.md",
    "project/language-level.template.md",
    "project/scheduled-tasks.md",
    "countries/_template.md",
    "countries/de.md",          # names {{PERMIT_HOURS}} on purpose
    "docs/first-hour.md",       # explains the placeholders
    "tracker/build-prompt.md",
    "scripts/check_kit.py",
}

errors = []


def fail(msg):
    errors.append(msg)


def check_skills():
    skill_dirs = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if not skill_dirs:
        fail("skills/: no skill folders found")
    for d in skill_dirs:
        f = d / "SKILL.md"
        if not f.exists():
            fail(f"{d.relative_to(ROOT)}: SKILL.md missing")
            continue
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            fail(f"{f.relative_to(ROOT)}: no frontmatter at the top")
            continue
        fields = {}
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fields[k.strip()] = v.strip()
        if fields.get("name") != d.name:
            fail(f"{f.relative_to(ROOT)}: name '{fields.get('name')}' != folder '{d.name}'")
        desc = fields.get("description", "")
        if not desc:
            fail(f"{f.relative_to(ROOT)}: description missing")
        elif len(desc) >= 1024:
            fail(f"{f.relative_to(ROOT)}: description is {len(desc)} characters (limit 1023)")
        elif "<" in desc or ">" in desc:
            fail(f"{f.relative_to(ROOT)}: description contains an angle bracket")


def schema_fields():
    """Return {table: [field, ...]} from tracker/schema.md."""
    text = (ROOT / "tracker" / "schema.md").read_text(encoding="utf-8")
    tables, current = {}, None
    for line in text.splitlines():
        h = re.match(r"^## (\w+) ", line)
        if h:
            current = h.group(1)
            tables[current] = []
            continue
        if current and line.startswith("| `"):
            first_cell = line.split("|")[1]
            tables[current] += re.findall(r"`([a-z_]+)`", first_cell)
    return tables


def check_csv():
    tables = schema_fields()
    for name in ("jobs", "tasks", "contacts"):
        f = ROOT / "tracker" / f"{name}.csv"
        rel = f.relative_to(ROOT)
        if not f.exists():
            fail(f"{rel}: missing")
            continue
        with f.open(encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh))
        if not rows:
            fail(f"{rel}: empty")
            continue
        header = rows[0]
        if header != tables.get(name):
            fail(f"{rel}: columns do not match tracker/schema.md\n  csv:    {header}\n  schema: {tables.get(name)}")
        for i, row in enumerate(rows[1:], start=2):
            if len(row) != len(header):
                fail(f"{rel}: line {i} has {len(row)} fields, header has {len(header)}")


def text_files():
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and ".git" not in p.parts and p.suffix in {".md", ".csv", ".py", ".yml", ".txt", ""}:
            yield p


def check_placeholders():
    for p in text_files():
        rel = p.relative_to(ROOT).as_posix()
        if rel in PLACEHOLDER_ALLOWED:
            continue
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if "{{" in line:
                fail(f"{rel}:{n}: placeholder outside a template file: {line.strip()[:80]}")


def check_links():
    link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    for p in text_files():
        if p.suffix != ".md":
            continue
        text = p.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
        for target in link.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if not (p.parent / path).exists():
                fail(f"{p.relative_to(ROOT)}: broken relative link '{target}'")


def main():
    check_skills()
    check_csv()
    check_placeholders()
    check_links()
    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("PASS: skills, tracker CSV, placeholders, relative links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
