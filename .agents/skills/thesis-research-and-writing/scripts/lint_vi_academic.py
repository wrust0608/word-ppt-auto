#!/usr/bin/env python3
"""Heuristic linter for Vietnamese academic Markdown.

This tool reports generic or formulaic prose. It is not an AI detector and does
not rewrite text. Rules intentionally favor explainable findings with line
locations over a single score.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


WORD_RE = re.compile(r"[0-9A-Za-zÀ-ỹĐđ]+", re.UNICODE)
CITATION_RE = re.compile(r"\[(?:\d+)(?:\s*[-,–]\s*\d+)*\]")
SENTENCE_RE = re.compile(r"[^.!?\n]+[.!?]?", re.UNICODE)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    rule: str
    severity: str
    message: str
    excerpt: str
    suggestion: str


@dataclass(frozen=True)
class PhraseRule:
    rule: str
    severity: str
    pattern: re.Pattern[str]
    message: str
    suggestion: str
    citation_required: bool = False


PHRASE_RULES = (
    PhraseRule(
        "VI001",
        "warning",
        re.compile(r"\btrong bối cảnh (?:hiện nay|ngày nay|hiện tại)\b", re.I),
        "Mở câu bằng bối cảnh rộng nhưng chưa nêu vấn đề cụ thể.",
        "Đi thẳng vào hệ thống, đối tượng, thay đổi hoặc khoảng trống đang xét.",
    ),
    PhraseRule(
        "VI002",
        "warning",
        re.compile(r"\b(?:đóng|giữ) vai trò (?:vô cùng |hết sức |rất )?(?:quan trọng|thiết yếu)\b", re.I),
        "Đánh giá tầm quan trọng nhưng chưa đưa tiêu chí hoặc hệ quả.",
        "Nêu tác động đo được, quyết định bị ảnh hưởng hoặc điều kiện cụ thể.",
    ),
    PhraseRule(
        "VI003",
        "warning",
        re.compile(r"\b(?:có thể thấy rằng|dễ dàng nhận thấy rằng|không khó để nhận thấy)\b", re.I),
        "Cụm dẫn quan sát không bổ sung nội dung.",
        "Bỏ cụm dẫn và phát biểu trực tiếp điều được quan sát cùng bằng chứng.",
    ),
    PhraseRule(
        "VI004",
        "warning",
        re.compile(r"\bkhông chỉ\b[^.!?\n]{0,120}\bmà còn\b", re.I),
        "Cấu trúc đối xứng dễ trở thành nhấn mạnh khuôn mẫu.",
        "Giữ lại nếu hai vế tạo tương phản cần thiết; nếu không, tách thành quan hệ cụ thể.",
    ),
    PhraseRule(
        "VI005",
        "warning",
        re.compile(
            r"\b(?:phân tích|đánh giá|nghiên cứu|khảo sát)\s+"
            r"(?:một cách\s+)?(?:toàn diện|kỹ lưỡng|chặt chẽ|chuyên sâu|hệ thống)\b",
            re.I,
        ),
        "Tính từ tự đánh giá đang thay cho mô tả phương pháp.",
        "Nêu dữ liệu, phép đo, tiêu chí, tham số hoặc quy trình đã thực hiện.",
    ),
    PhraseRule(
        "VI006",
        "warning",
        re.compile(r"\b(?:tạo tiền đề|tạo nền tảng|mở ra nhiều cơ hội|mang lại nhiều lợi ích)\b", re.I),
        "Kết luận chung chưa chỉ ra kết quả hoặc bước tiếp theo cụ thể.",
        "Chốt phát hiện, giới hạn hoặc quyết định mà phần sau kế thừa.",
    ),
    PhraseRule(
        "VI007",
        "warning",
        re.compile(r"\b(?:phần này sẽ|chương này sẽ lần lượt|chúng ta sẽ cùng|hãy cùng)\b", re.I),
        "Câu hướng dẫn người đọc thay cho nội dung học thuật.",
        "Nêu câu hỏi, phạm vi hoặc cấu trúc chỉ khi nó giúp theo dõi lập luận.",
    ),
    PhraseRule(
        "VI008",
        "error",
        re.compile(
            r"\b(?:các|nhiều|một số)\s+(?:nghiên cứu|chuyên gia|tài liệu|báo cáo)\s+"
            r"(?:cho thấy|chỉ ra|nhận định|khẳng định|đề xuất)\b",
            re.I,
        ),
        "Quy nguồn mơ hồ cho một khẳng định học thuật.",
        "Nêu nguồn cụ thể và citation; nếu chưa có, dùng [CẦN NGUỒN].",
        citation_required=True,
    ),
    PhraseRule(
        "VI009",
        "warning",
        re.compile(r"\b(?:có thể|có khả năng|dường như)\s+(?:có thể|có khả năng|được xem là)\b", re.I),
        "Nhiều lớp dè dặt che khuất mức chắc chắn thực tế.",
        "Giữ một mức bất định phù hợp và nêu căn cứ hoặc điều kiện.",
    ),
    PhraseRule(
        "VI010",
        "warning",
        re.compile(r"\b(?:giải pháp|phương pháp|mô hình)\s+(?:tối ưu|ưu việt|vượt trội|hoàn hảo)\b", re.I),
        "Tự xếp hạng giải pháp khi chưa nêu tiêu chí so sánh.",
        "Thay bằng kết quả theo từng tiêu chí và phạm vi đánh giá.",
    ),
)

TRANSITIONS = (
    "đồng thời",
    "qua đó",
    "từ đó",
    "bên cạnh đó",
    "hơn nữa",
    "do đó",
    "mặt khác",
)

PLACEHOLDER_RE = re.compile(
    r"\[(?:CẦN NGUỒN|CẦN DỮ LIỆU|CẦN TÁC GIẢ XÁC NHẬN|MÂU THUẪN NGUỒN|CHƯA ĐỦ BẰNG CHỨNG)\]",
    re.I,
)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text).lower()
    return " ".join(WORD_RE.findall(text))


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))


def visible_lines(text: str) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    fenced = False
    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            fenced = not fenced
            continue
        if fenced or not stripped or stripped.startswith("<!--"):
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            continue
        if re.match(r"^\s*(?:[-*+] |\d+[.)] )", raw):
            # List prose still matters, but remove the marker.
            raw = re.sub(r"^\s*(?:[-*+] |\d+[.)] )", "", raw)
        lines.append((number, raw.strip()))
    return lines


def paragraph_blocks(text: str) -> list[tuple[int, str]]:
    blocks: list[tuple[int, str]] = []
    start = 1
    current: list[str] = []
    fenced = False
    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            fenced = not fenced
        if fenced or stripped.startswith("#") or (stripped.startswith("|") and stripped.endswith("|")):
            if current:
                blocks.append((start, " ".join(current)))
                current = []
            continue
        if not stripped:
            if current:
                blocks.append((start, " ".join(current)))
                current = []
            continue
        if not current:
            start = number
        current.append(stripped)
    if current:
        blocks.append((start, " ".join(current)))
    return [(line, body) for line, body in blocks if word_count(body) >= 8]


def add_phrase_findings(path: str, lines: Iterable[tuple[int, str]]) -> list[Finding]:
    findings: list[Finding] = []
    for line_number, line in lines:
        for rule in PHRASE_RULES:
            if not rule.pattern.search(line):
                continue
            if rule.citation_required and CITATION_RE.search(line):
                continue
            findings.append(
                Finding(path, line_number, rule.rule, rule.severity, rule.message, line[:220], rule.suggestion)
            )
        for sentence in SENTENCE_RE.findall(line):
            count = word_count(sentence)
            if count > 55:
                findings.append(
                    Finding(
                        path,
                        line_number,
                        "VI011",
                        "warning",
                        f"Câu dài {count} từ, khó theo dõi quan hệ chính.",
                        sentence.strip()[:220],
                        "Tách tại ranh giới luận điểm; không tách danh sách điều kiện vốn cần đi cùng nhau.",
                    )
                )
    return findings


def add_structure_findings(path: str, text: str, publication: bool) -> list[Finding]:
    findings: list[Finding] = []
    blocks = paragraph_blocks(text)
    total_words = max(word_count(text), 1)

    openings: dict[str, list[int]] = {}
    for line, body in blocks:
        words = normalize(body).split()
        if len(words) >= 3:
            openings.setdefault(" ".join(words[:3]), []).append(line)
    for opening, locations in openings.items():
        if len(locations) >= 3:
            findings.append(
                Finding(
                    path,
                    locations[0],
                    "VI012",
                    "warning",
                    f"Có {len(locations)} đoạn mở bằng cùng cấu trúc: “{opening}”.",
                    ", ".join(str(item) for item in locations),
                    "Kiểm tra chức năng từng đoạn; thay cách mở khi sự lặp không mang dụng ý.",
                )
            )

    transition_hits: list[tuple[int, str]] = []
    for line, body in visible_lines(text):
        lowered = normalize(body)
        for transition in TRANSITIONS:
            if transition in lowered:
                transition_hits.append((line, transition))
    rate = len(transition_hits) * 1000 / total_words
    if len(transition_hits) >= 5 and rate > 8:
        findings.append(
            Finding(
                path,
                transition_hits[0][0],
                "VI013",
                "warning",
                f"Mật độ liên từ khuôn mẫu là {rate:.1f}/1.000 từ ({len(transition_hits)} lần).",
                ", ".join(f"{term}@{line}" for line, term in transition_hits[:12]),
                "Giữ liên từ chỉ khi quan hệ logic không thể hiện rõ bằng nội dung hai câu.",
            )
        )

    sentence_lengths: list[int] = []
    for _, body in blocks:
        for match in SENTENCE_RE.finditer(body):
            length = word_count(match.group())
            if length >= 4:
                sentence_lengths.append(length)
    if len(sentence_lengths) >= 8:
        mean = sum(sentence_lengths) / len(sentence_lengths)
        variance = sum((item - mean) ** 2 for item in sentence_lengths) / len(sentence_lengths)
        cv = math.sqrt(variance) / mean if mean else 0
        if 10 <= mean <= 35 and cv < 0.18:
            findings.append(
                Finding(
                    path,
                    1,
                    "VI014",
                    "info",
                    f"Độ dài {len(sentence_lengths)} câu khá đồng đều (CV={cv:.2f}).",
                    f"min={min(sentence_lengths)}, mean={mean:.1f}, max={max(sentence_lengths)}",
                    "Đọc lại nhịp câu; chỉ thay đổi khi độ phức tạp của ý đang bị san phẳng.",
                )
            )

    if publication:
        for line, body in visible_lines(text):
            for match in PLACEHOLDER_RE.finditer(body):
                findings.append(
                    Finding(
                        path,
                        line,
                        "VI015",
                        "error",
                        "Bản chuẩn bị xuất bản còn nhãn thiếu thông tin.",
                        match.group(),
                        "Bổ sung bằng chứng/dữ liệu/xác nhận hoặc ghi ngoại lệ đã được phê duyệt.",
                    )
                )
    return findings


def lint_text(text: str, path: str = "<memory>", publication: bool = False) -> list[Finding]:
    findings = add_phrase_findings(path, visible_lines(text))
    findings.extend(add_structure_findings(path, text, publication))
    return sorted(findings, key=lambda item: (item.line, item.rule))


def lint_file(path: Path, publication: bool = False) -> list[Finding]:
    return lint_text(path.read_text(encoding="utf-8"), str(path), publication)


def render_text(findings: list[Finding]) -> str:
    if not findings:
        return "Không phát hiện mẫu văn phong cần xem xét."
    rows = []
    for item in findings:
        rows.append(
            f"{item.file}:{item.line}: {item.severity.upper()} {item.rule} — {item.message}\n"
            f"  Trích: {item.excerpt}\n  Gợi ý: {item.suggestion}"
        )
    counts = Counter(item.severity for item in findings)
    rows.append(
        "Tổng hợp: " + ", ".join(f"{name}={counts.get(name, 0)}" for name in ("error", "warning", "info"))
    )
    return "\n".join(rows)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="Markdown or UTF-8 text files")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument("--publication", action="store_true", help="Treat unresolved labels as errors")
    parser.add_argument("--fail-on-error", action="store_true", help="Return exit code 1 when errors exist")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    # PowerShell on Vietnamese Windows can expose a legacy console encoding.
    # Keep diagnostics readable without requiring callers to set PYTHONUTF8.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8", errors="replace")
    args = parse_args(argv or sys.argv[1:])
    findings: list[Finding] = []
    for path in args.files:
        try:
            findings.extend(lint_file(path, args.publication))
        except (OSError, UnicodeError) as exc:
            print(f"Không đọc được {path}: {exc}", file=sys.stderr)
            return 2
    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    else:
        print(render_text(findings))
    if args.fail_on_error and any(item.severity == "error" for item in findings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
