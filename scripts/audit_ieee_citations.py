#!/usr/bin/env python3
"""Audit numeric IEEE-style citations in a Markdown document.

The audit is structural: it detects missing, orphan, duplicate and out-of-order
references. It does not verify that a source supports a claim.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path


CITATION_RE = re.compile(r"\[(\d+(?:\s*[-–,]\s*\d+)*)\]")
REFERENCE_RE = re.compile(r"^\s*\[(\d+)\]\s+(.+?)\s*$")


@dataclass(frozen=True)
class Issue:
    code: str
    severity: str
    message: str


def normalize(text: str) -> str:
    return " ".join(unicodedata.normalize("NFC", text).casefold().split())


def expand_citation(payload: str) -> list[int]:
    values: list[int] = []
    for part in re.split(r"\s*,\s*", payload):
        range_match = re.fullmatch(r"(\d+)\s*[-–]\s*(\d+)", part)
        if range_match:
            start, end = map(int, range_match.groups())
            values.extend(range(start, end + 1) if start <= end else range(start, end - 1, -1))
        elif part.isdigit():
            values.append(int(part))
    return values


def split_document(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        heading = normalize(re.sub(r"^#+\s*", "", line))
        if heading == "tài liệu tham khảo":
            return "\n".join(lines[:index]), "\n".join(lines[index + 1 :])
    return text, ""


def audit_text(text: str) -> tuple[dict[str, object], list[Issue]]:
    body, bibliography = split_document(text)
    issues: list[Issue] = []

    first_order: list[int] = []
    used: set[int] = set()
    for match in CITATION_RE.finditer(body):
        for value in expand_citation(match.group(1)):
            if value not in used:
                first_order.append(value)
                used.add(value)

    references: dict[int, str] = {}
    duplicates: list[int] = []
    for line in bibliography.splitlines():
        match = REFERENCE_RE.match(line)
        if not match:
            continue
        number = int(match.group(1))
        if number in references:
            duplicates.append(number)
        references[number] = match.group(2)

    if not bibliography:
        issues.append(Issue("IEEE001", "error", "Không tìm thấy mục TÀI LIỆU THAM KHẢO."))
    if duplicates:
        issues.append(Issue("IEEE002", "error", f"Số tham khảo bị khai báo lặp: {sorted(set(duplicates))}."))

    missing = sorted(used - set(references))
    orphan = sorted(set(references) - used)
    if missing:
        issues.append(Issue("IEEE003", "error", f"Citation không có mục tham khảo: {missing}."))
    if orphan:
        issues.append(Issue("IEEE004", "warning", f"Tài liệu tham khảo chưa được dùng: {orphan}."))

    expected_order = list(range(1, len(first_order) + 1))
    if first_order and first_order != expected_order:
        issues.append(
            Issue(
                "IEEE005",
                "error",
                f"Thứ tự xuất hiện đầu tiên là {first_order}, kỳ vọng {expected_order}.",
            )
        )

    reference_numbers = sorted(references)
    expected_references = list(range(1, max(reference_numbers) + 1)) if reference_numbers else []
    if reference_numbers != expected_references:
        issues.append(
            Issue(
                "IEEE006",
                "error",
                f"Đánh số danh mục không liên tục: {reference_numbers}.",
            )
        )

    bodies: dict[str, list[int]] = {}
    for number, value in references.items():
        bodies.setdefault(normalize(value), []).append(number)
    duplicate_bodies = [numbers for numbers in bodies.values() if len(numbers) > 1]
    if duplicate_bodies:
        issues.append(Issue("IEEE007", "warning", f"Nội dung tham khảo trùng: {duplicate_bodies}."))

    summary: dict[str, object] = {
        "citation_count": len(list(CITATION_RE.finditer(body))),
        "used_numbers": sorted(used),
        "first_appearance": first_order,
        "reference_numbers": reference_numbers,
        "missing_references": missing,
        "orphan_references": orphan,
    }
    return summary, issues


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8", errors="replace")
    args = parse_args(argv or sys.argv[1:])
    text = args.file.read_text(encoding="utf-8")
    summary, issues = audit_text(text)
    if args.json:
        print(json.dumps({"summary": summary, "issues": [asdict(item) for item in issues]}, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        if issues:
            for issue in issues:
                print(f"{issue.severity.upper()} {issue.code}: {issue.message}")
        else:
            print("Không phát hiện lỗi cấu trúc citation IEEE.")
    if args.fail_on_error and any(item.severity == "error" for item in issues):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
