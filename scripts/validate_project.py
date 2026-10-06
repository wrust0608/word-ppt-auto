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
        clean_text = re.sub(r"```[\s\S]*?```", "", text)
        clean_text = re.sub(r"`[^`\n]*`", "", clean_text)
        for match in LINK_RE.finditer(clean_text):
            target = match.group(1).strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "file:")):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            if not resolved.exists():
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    if SKILL.exists():
        validate_skill(errors)
    validate_json(errors)
    validate_links(errors)
    if errors:
        print("Project validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Project validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
