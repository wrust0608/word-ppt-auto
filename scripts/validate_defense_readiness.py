#!/usr/bin/env python3
"""Validate Defense Readiness artifacts according to fail-closed machine rules.

Machine Rules Enforced:
1. Closed Enum Status: READY, SIMPLIFY, AUTHOR_CONFIRM, EVIDENCE_GAP, REMOVE_CANDIDATE.
2. Closed Enum Text Action: KEEP, REWRITE, SIMPLIFY, REMOVE_PROPOSED, NO_TEXT_CHANGE.
3. Required 15 fields for every Defense Card.
4. Derivation Rule A: Evidence key = FAIL => Status MUST equal EVIDENCE_GAP.
5. Derivation Rule B: Evidence key = PASS and Ownership key = FAIL => Status MUST equal AUTHOR_CONFIRM.
6. Derivation Rule C: Status = READY => Evidence key = PASS and Ownership key in (PASS, NOT_APPLICABLE) and Review trace not empty.
7. Derivation Rule D: Ownership key = PASS => Author ownership evidence not empty and Author response is not placeholder.
8. Placeholder Integrity: If not confirmed, Author response must be exactly '[CHƯA CÓ PHẢN HỒI TÁC GIẢ]' (no extra text).
9. Banned status keywords: CLOSED, FIXED, RESOLVED, GAP CLOSED, KHÉP GAP, ĐÃ SỬA NỘI DUNG, ACCEPTED.
10. Banned headings/fields in Defense Review: 'Gợi ý bảo vệ', 'Câu trả lời mẫu', 'Sinh viên nên trả lời', 'Suggested defense answer', 'Model answer'.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

VALID_STATUSES = {
    "READY",
    "SIMPLIFY",
    "AUTHOR_CONFIRM",
    "EVIDENCE_GAP",
    "REMOVE_CANDIDATE",
}

VALID_TEXT_ACTIONS = {
    "KEEP",
    "REWRITE",
    "SIMPLIFY",
    "REMOVE_PROPOSED",
    "NO_TEXT_CHANGE",
}

VALID_EVIDENCE_KEYS = {"PASS", "FAIL"}
VALID_OWNERSHIP_KEYS = {"PASS", "FAIL", "NOT_APPLICABLE"}

BANNED_STATUS_PATTERNS = [
    "CLOSED",
    "FIXED",
    "RESOLVED",
    "GAP CLOSED",
    "KHÉP GAP",
    "ĐÃ SỬA NỘI DUNG",
    "ACCEPTED",
]

# Prohibited headings, list-item prefixes, or table labels in Defense Review artifacts
BANNED_ARTIFACT_PATTERNS = [
    r"gợi ý bảo vệ",
    r"câu trả lời mẫu",
    r"sinh viên nên trả lời",
    r"suggested defense answer",
    r"model answer",
]

BANNED_HEADING_OR_FIELD_RE = re.compile(
    r"(?m)^(?:\s*#{1,6}\s+|\s*[-*]\s+\*{0,2}|\s*\*{1,2}|\s*\|\s*)(?:gợi ý bảo vệ|câu trả lời mẫu|sinh viên nên trả lời|suggested defense answer|model answer)(?:\*{0,2}\s*:?|\s*\|)",
    re.IGNORECASE,
)

CANONICAL_PLACEHOLDER = "[CHƯA CÓ PHẢN HỒI TÁC GIẢ]"

REQUIRED_FIELD_KEYS = [
    "section_claim_id",
    "claim_type",
    "claim",
    "evidence_data",
    "evidence_boundary",
    "evidence_key",
    "author_ownership_evidence",
    "ownership_key",
    "why_needed",
    "author_must_explain",
    "author_response",
    "likely_defense_question",
    "text_action",
    "status",
    "review_trace",
]

FIELD_DISPLAY_NAMES = {
    "section_claim_id": "Section / Claim ID",
    "claim_type": "Claim type",
    "claim": "Claim",
    "evidence_data": "Evidence / Data",
    "evidence_boundary": "Evidence boundary",
    "evidence_key": "Evidence key",
    "author_ownership_evidence": "Author ownership evidence",
    "ownership_key": "Ownership key",
    "why_needed": "Why needed",
    "author_must_explain": "Author must explain",
    "author_response": "Author response",
    "likely_defense_question": "Likely defense question",
    "text_action": "Text action",
    "status": "Status",
    "review_trace": "Review trace",
}

CARD_HEADER_RE = re.compile(r"(?m)^#{2,4}\s+(DR-[A-Za-z0-9_-]+)(?:[^\n]*)")


def normalize_key(raw_key: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "_", raw_key.lower()).strip("_")
    # Aliases
    if cleaned in ("section", "claim_id", "section_claim_id"):
        return "section_claim_id"
    if cleaned in ("evidence", "data", "evidence_data"):
        return "evidence_data"
    return cleaned


class DefenseCard(NamedTuple):
    card_id: str
    fields: dict[str, str]
    raw_text: str


def parse_cards_from_markdown(content: str) -> list[DefenseCard]:
    cards: list[DefenseCard] = []
    matches = list(CARD_HEADER_RE.finditer(content))
    for i, match in enumerate(matches):
        card_id = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        card_text = content[start:end]

        fields: dict[str, str] = {}
        for line in card_text.splitlines():
            line_str = line.strip()
            if line_str.startswith("|") and line_str.endswith("|"):
                parts = [p.strip() for p in line_str.split("|")[1:-1]]
                if len(parts) >= 2:
                    raw_col0 = parts[0]
                    if (
                        raw_col0
                        and raw_col0.lower() not in ("field", "trường")
                        and not raw_col0.startswith("---")
                    ):
                        k = normalize_key(raw_col0)
                        v = "|".join(parts[1:]).strip()
                        fields[k] = v

        cards.append(DefenseCard(card_id=card_id, fields=fields, raw_text=card_text))
    return cards


def validate_defense_card(card: DefenseCard) -> list[str]:
    errors: list[str] = []
    card_id = card.card_id
    fields = card.fields

    # 1. Check all required fields present
    for req_key in REQUIRED_FIELD_KEYS:
        if req_key not in fields or not fields[req_key].strip():
            display_name = FIELD_DISPLAY_NAMES[req_key]
            # Special allowance: author_ownership_evidence can be empty or N/A only if ownership_key is NOT_APPLICABLE
            if req_key == "author_ownership_evidence":
                own_key = fields.get("ownership_key", "").strip().upper()
                if own_key == "NOT_APPLICABLE":
                    continue
            errors.append(f"[{card_id}] Thiếu trường bắt buộc: '{display_name}'")

    status = fields.get("status", "").strip()
    status_upper = status.upper()
    evidence_key = fields.get("evidence_key", "").strip().upper()
    ownership_key = fields.get("ownership_key", "").strip().upper()
    text_action = fields.get("text_action", "").strip().upper()
    author_response = fields.get("author_response", "").strip()
    ownership_evidence = fields.get("author_ownership_evidence", "").strip()
    review_trace = fields.get("review_trace", "").strip()

    # 2. Check Banned Status keywords
    for banned in BANNED_STATUS_PATTERNS:
        if banned in status_upper:
            errors.append(
                f"[{card_id}] Status chứa giá trị bị cấm '{banned}' (Status: '{status}')"
            )

    # 3. Check Closed Enum Status
    if status_upper not in VALID_STATUSES:
        errors.append(
            f"[{card_id}] Status '{status}' không thuộc closed enum hợp lệ {sorted(VALID_STATUSES)}"
        )

    # 4. Check Closed Enum Text Action
    if text_action not in VALID_TEXT_ACTIONS:
        errors.append(
            f"[{card_id}] Text action '{text_action}' không thuộc tập hợp hợp lệ {sorted(VALID_TEXT_ACTIONS)}"
        )

    # 5. Check Evidence Key validity
    if evidence_key not in VALID_EVIDENCE_KEYS:
        errors.append(
            f"[{card_id}] Evidence key '{evidence_key}' không hợp lệ (phải là PASS hoặc FAIL)"
        )

    # 6. Check Ownership Key validity
    if ownership_key not in VALID_OWNERSHIP_KEYS:
        errors.append(
            f"[{card_id}] Ownership key '{ownership_key}' không hợp lệ (phải là PASS, FAIL hoặc NOT_APPLICABLE)"
        )

    # 7. Placeholder integrity
    if CANONICAL_PLACEHOLDER in author_response:
        if author_response != CANONICAL_PLACEHOLDER:
            errors.append(
                f"[{card_id}] Author response không được kèm văn bản giả bên cạnh placeholder '{CANONICAL_PLACEHOLDER}': '{author_response}'"
            )

    # 8. Derivation Rule A: Evidence key = FAIL => Status MUST equal EVIDENCE_GAP
    if evidence_key == "FAIL":
        if status_upper != "EVIDENCE_GAP":
            errors.append(
                f"[{card_id}] Rule A vi phạm: Evidence key = FAIL bắt buộc Status phải là EVIDENCE_GAP (hiện tại: '{status}')"
            )

    # 9. Derivation Rule B: Evidence key = PASS and Ownership key = FAIL => Status MUST equal AUTHOR_CONFIRM
    if evidence_key == "PASS" and ownership_key == "FAIL":
        if status_upper != "AUTHOR_CONFIRM":
            errors.append(
                f"[{card_id}] Rule B vi phạm: Evidence key = PASS và Ownership key = FAIL bắt buộc Status phải là AUTHOR_CONFIRM (hiện tại: '{status}')"
            )

    # 10. Derivation Rule C: Status = READY requirements
    if status_upper == "READY":
        if evidence_key != "PASS":
            errors.append(
                f"[{card_id}] Rule C vi phạm: Status = READY bắt buộc Evidence key phải là PASS (hiện tại: '{evidence_key}')"
            )
        if ownership_key not in ("PASS", "NOT_APPLICABLE"):
            errors.append(
                f"[{card_id}] Rule C vi phạm: Status = READY bắt buộc Ownership key phải là PASS hoặc NOT_APPLICABLE (hiện tại: '{ownership_key}')"
            )
        if not review_trace:
            errors.append(
                f"[{card_id}] Rule C vi phạm: Status = READY bắt buộc Review trace không được để trống"
            )

    # 11. Derivation Rule D: Ownership key = PASS requirements
    if ownership_key == "PASS":
        if not ownership_evidence:
            errors.append(
                f"[{card_id}] Rule D vi phạm: Ownership key = PASS bắt buộc Author ownership evidence không được để trống"
            )
        if author_response == CANONICAL_PLACEHOLDER or not author_response:
            errors.append(
                f"[{card_id}] Rule D vi phạm: Ownership key = PASS bắt buộc Author response phải có phản hồi thực của tác giả, không được dùng placeholder"
            )

    # 12. Ownership key = FAIL requirement: author response MUST be placeholder
    if ownership_key == "FAIL":
        if author_response != CANONICAL_PLACEHOLDER:
            errors.append(
                f"[{card_id}] Ownership key = FAIL bắt buộc Author response phải là placeholder '{CANONICAL_PLACEHOLDER}', không được tự điền câu trả lời: '{author_response}'"
            )

    return errors


def validate_defense_readiness_text(content: str, filename: str = "document") -> list[str]:
    errors: list[str] = []

    # Check banned artifact-level patterns (headings, list items, fields)
    for match in BANNED_HEADING_OR_FIELD_RE.finditer(content):
        matched_str = match.group(0).strip()
        errors.append(
            f"[{filename}] Chứa heading/field bị cấm trong Defense Review: '{matched_str}'"
        )

    # Parse and validate Defense Cards
    cards = parse_cards_from_markdown(content)
    if not cards:
        # Check if the document appears to be a defense review document
        if "DEFENSE_REVIEW" in filename.upper() or "DEFENSE_READINESS" in filename.upper():
            errors.append(f"[{filename}] Không tìm thấy Defense Card nào dạng '### DR-...'")
        return errors

    for card in cards:
        card_errors = validate_defense_card(card)
        for err in card_errors:
            errors.append(f"[{filename}] {err}")

    return errors


def validate_file(file_path: Path) -> list[str]:
    if not file_path.is_file():
        return [f"File không tồn tại: {file_path}"]
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"Không thể đọc file {file_path}: {exc}"]
    return validate_defense_readiness_text(content, filename=file_path.name)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate Defense Readiness artifacts according to fail-closed rules."
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="Path(s) to Markdown Defense Review artifacts.",
    )
    args = parser.parse_args(argv)

    root = Path(__file__).resolve().parents[1]
    target_files = args.files
    if not target_files:
        # Default: discover defense review artifacts in work/
        target_files = sorted(root.glob("work/**/*DEFENSE_REVIEW*.md"))
        defense_readiness = root / "work" / "do-an" / "DEFENSE_READINESS.md"
        if defense_readiness.is_file() and defense_readiness not in target_files:
            target_files.append(defense_readiness)

    if not target_files:
        print("No Defense Readiness artifacts found to validate.")
        return 0

    all_errors: list[str] = []
    total_cards = 0

    for path in target_files:
        resolved_path = path.resolve()
        if not resolved_path.is_file():
            all_errors.append(f"File not found: {path}")
            continue

        try:
            content = resolved_path.read_text(encoding="utf-8")
        except Exception as exc:
            all_errors.append(f"Could not read {path}: {exc}")
            continue

        cards = parse_cards_from_markdown(content)
        total_cards += len(cards)

        file_errors = validate_defense_readiness_text(content, filename=resolved_path.name)
        all_errors.extend(file_errors)

    if all_errors:
        print(f"DEFENSE READINESS VALIDATION FAILED ({len(all_errors)} error(s)):")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(
        f"DEFENSE READINESS VALIDATION PASSED: {len(target_files)} file(s), {total_cards} card(s) checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
