#!/usr/bin/env python3
"""Validate repository invariants without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "thesis-research-and-writing" / "SKILL.md"

REQUIRED = (
    ROOT / "README.md",
    ROOT / "HANDOFF.md",
    SKILL,
    ROOT / "prompts" / "ANTIGRAVITY_MASTER_PROMPT.md",
    ROOT / "templates" / "AUTHOR_VOICE.md",
    ROOT / "templates" / "REVIEW_REPORT.md",
    ROOT / ".agents" / "mcp_config.example.json",
    ROOT / "notebooklm-config.example.json",
)

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate_required(errors: list[str]) -> None:
    for path in REQUIRED:
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")


def validate_skill(errors: list[str]) -> None:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append("SKILL.md frontmatter is not closed")
        return
    frontmatter = parts[1]
    if not re.search(r"^name:\s*thesis-research-and-writing\s*$", frontmatter, re.M):
        errors.append("SKILL.md has an unexpected name")
    if not re.search(r"^description:\s*\S", frontmatter, re.M):
        errors.append("SKILL.md requires a non-empty description")
    if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", text, re.I):
        errors.append("SKILL.md contains unfinished scaffold text")
    if re.search(r"\b(?:SMB|Nmap|MS17-010)\b", text, re.I):
        errors.append("Core skill must remain domain-neutral")


def validate_json(errors: list[str]) -> None:
    for path in (
        ROOT / ".agents" / "mcp_config.example.json",
        ROOT / "notebooklm-config.example.json",
    ):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv", "chrome_profile_notebooklm"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "file:")):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            if not resolved.exists():
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")


def validate_defense_readiness_artifacts(errors: list[str]) -> None:
    # Only validate when Defense Readiness artifacts exist in work/
    defense_artifacts: list[Path] = []
    work_dir = ROOT / "work"
    if work_dir.is_dir():
        defense_artifacts.extend(work_dir.glob("**/*DEFENSE_REVIEW*.md"))
        defense_readiness = work_dir / "do-an" / "DEFENSE_READINESS.md"
        if defense_readiness.is_file() and defense_readiness not in defense_artifacts:
            defense_artifacts.append(defense_readiness)

    if not defense_artifacts:
        return

    scripts_dir = ROOT / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))

    try:
        from validate_defense_readiness import validate_file

        for path in defense_artifacts:
            file_errors = validate_file(path)
            for err in file_errors:
                errors.append(f"Defense Readiness ({path.relative_to(ROOT)}): {err}")
    except Exception as exc:
        errors.append(f"Defense Readiness validation runner failed: {exc}")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    if SKILL.exists():
        validate_skill(errors)
    validate_json(errors)
    validate_links(errors)
    validate_defense_readiness_artifacts(errors)
    if errors:
        print("Project validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Project validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
