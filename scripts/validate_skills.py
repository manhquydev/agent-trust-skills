#!/usr/bin/env python3
"""Validate the skills in this repo against the Agent Skills specification
(https://agentskills.io/specification).

Checks per skill directory under skills/:
- directory name matches ^[a-z0-9]+(-[a-z0-9]+)*$ and is 1-64 chars
- SKILL.md exists and starts with YAML frontmatter delimited by ---
- frontmatter name is present, valid, and equals the directory name
- frontmatter description is present and 1-1024 chars
- optional compatibility is at most 500 chars
- SKILL.md body stays under 500 lines (spec recommendation)
- skill.yaml, when present, parses and its name matches the directory

Exit code 0 when every skill passes, 1 otherwise.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"


def check_skill(path: Path) -> list[str]:
    errors = []
    name = path.name
    if len(name) > 64 or not NAME_RE.match(name):
        errors.append(f"{name}: directory name violates spec charset/length")
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{name}: SKILL.md missing")
        return errors
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 500:
        errors.append(f"{name}: SKILL.md is {len(lines)} lines, spec recommends under 500")
    if not text.startswith("---\n"):
        errors.append(f"{name}: SKILL.md has no YAML frontmatter")
        return errors
    end = text.find("\n---", 4)
    if end == -1:
        errors.append(f"{name}: frontmatter is not closed")
        return errors
    try:
        fm = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        errors.append(f"{name}: frontmatter YAML does not parse: {exc}")
        return errors
    if not isinstance(fm, dict):
        errors.append(f"{name}: frontmatter is not a mapping")
        return errors
    fname = fm.get("name")
    if not fname or not isinstance(fname, str):
        errors.append(f"{name}: frontmatter name missing")
    elif fname != name:
        errors.append(f"{name}: frontmatter name '{fname}' does not match directory")
    elif len(fname) > 64 or not NAME_RE.match(fname):
        errors.append(f"{name}: frontmatter name violates spec charset/length")
    desc = fm.get("description")
    if not desc or not isinstance(desc, str):
        errors.append(f"{name}: frontmatter description missing")
    elif not 1 <= len(desc) <= 1024:
        errors.append(f"{name}: description is {len(desc)} chars, spec allows 1-1024")
    compat = fm.get("compatibility")
    if compat is not None and len(str(compat)) > 500:
        errors.append(f"{name}: compatibility exceeds 500 chars")
    desc_yaml = path / "skill.yaml"
    if desc_yaml.exists():
        try:
            data = yaml.safe_load(desc_yaml.read_text(encoding="utf-8"))
            if data.get("name") != name:
                errors.append(f"{name}: skill.yaml name '{data.get('name')}' does not match directory")
        except yaml.YAMLError as exc:
            errors.append(f"{name}: skill.yaml does not parse: {exc}")
    return errors


def main() -> int:
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        print("No skill directories found under skills/")
        return 1
    all_errors: list[str] = []
    for d in skill_dirs:
        errs = check_skill(d)
        status = "PASS" if not errs else "FAIL"
        print(f"[{status}] {d.name}")
        all_errors.extend(errs)
    for e in all_errors:
        print("  ERROR:", e)
    print(f"\n{len(skill_dirs)} skills checked, {len(all_errors)} errors")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
