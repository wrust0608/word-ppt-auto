from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_defense_readiness.py"
SPEC = importlib.util.spec_from_file_location("validate_defense_readiness", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def make_card_markdown(
    card_id: str = "DR-C1-01",
    section: str = "§1.2.1; C002",
    claim_type: str = "method/design decision",
    claim: str = "Mô tả kiểm thử CVE-2017-0144",
    evidence_data: str = "RESEARCH_MAP RQ2/O2; S005/S013",
    evidence_boundary: str = "Giới hạn trong lab kiểm thử",
    evidence_key: str = "PASS",
    ownership_evidence: str = "AUTHOR_VOICE.md dòng 67-71",
    ownership_key: str = "PASS",
    why_needed: str = "Xác định mục tiêu kiểm thử",
    author_must_explain: str = "Giải thích cơ chế lỗi",
    author_response: str = "Phản hồi thật từ tác giả",
    likely_defense_question: str = "Tại sao chọn CVE này?",
    text_action: str = "NO_TEXT_CHANGE",
    status: str = "READY",
    review_trace: str = "Reviewer / 2026-10-04 / Xác nhận",
) -> str:
    return f"""### {card_id} — Tiêu đề thẻ

| Field | Content |
|---|---|
| Section / Claim ID | {section} |
| Claim type | {claim_type} |
| Claim | {claim} |
| Evidence / Data | {evidence_data} |
| Evidence boundary | {evidence_boundary} |
| Evidence key | {evidence_key} |
| Author ownership evidence | {ownership_evidence} |
| Ownership key | {ownership_key} |
| Why needed | {why_needed} |
| Author must explain | {author_must_explain} |
| Author response | {author_response} |
| Likely defense question | {likely_defense_question} |
| Text action | {text_action} |
| Status | {status} |
| Review trace | {review_trace} |
"""


class DefenseReadinessValidationTests(unittest.TestCase):
    # --- PASS TESTS ---

    def test_valid_ready(self) -> None:
        """PASS: Valid READY card with Evidence PASS, Ownership PASS, Review trace."""
        doc = make_card_markdown(
            card_id="DR-TEST-01",
            evidence_key="PASS",
            ownership_key="PASS",
            ownership_evidence="Ghi nhận tại AUTHOR_VOICE.md dòng 67-71",
            author_response="Phản hồi chính thức của tác giả",
            status="READY",
            review_trace="Reviewer / 2026-10-04 / AUTHOR_VOICE.md",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertEqual([], errors)

    def test_valid_ready_not_applicable_ownership(self) -> None:
        """PASS: Valid READY card with Evidence PASS and Ownership NOT_APPLICABLE for technical fact."""
        doc = make_card_markdown(
            card_id="DR-TEST-02",
            evidence_key="PASS",
            ownership_key="NOT_APPLICABLE",
            ownership_evidence="",
            author_response="N/A",
            status="READY",
            review_trace="Reviewer / 2026-10-04 / Source inspection",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertEqual([], errors)

    def test_valid_author_confirm(self) -> None:
        """PASS: Valid AUTHOR_CONFIRM card with Evidence PASS, Ownership FAIL, placeholder response."""
        doc = make_card_markdown(
            card_id="DR-TEST-03",
            evidence_key="PASS",
            ownership_key="FAIL",
            ownership_evidence="Chưa có văn bản xác nhận",
            author_response="[CHƯA CÓ PHẢN HỒI TÁC GIẢ]",
            status="AUTHOR_CONFIRM",
            review_trace="Reviewer / 2026-10-04 / PROJECT_STATE.md",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertEqual([], errors)

    def test_valid_evidence_gap(self) -> None:
        """PASS: Valid EVIDENCE_GAP card with Evidence FAIL."""
        doc = make_card_markdown(
            card_id="DR-TEST-04",
            evidence_key="FAIL",
            ownership_key="FAIL",
            ownership_evidence="Chưa có",
            author_response="[CHƯA CÓ PHẢN HỒI TÁC GIẢ]",
            status="EVIDENCE_GAP",
            review_trace="Reviewer / 2026-10-04 / Source check",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertEqual([], errors)

    # --- FAIL TESTS ---

    def test_fail_ready_ownership_fail(self) -> None:
        """FAIL: READY with Ownership FAIL violates Rule C."""
        doc = make_card_markdown(
            card_id="DR-FAIL-01",
            evidence_key="PASS",
            ownership_key="FAIL",
            author_response="[CHƯA CÓ PHẢN HỒI TÁC GIẢ]",
            status="READY",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Rule C vi phạm" in e or "Rule B vi phạm" in e for e in errors))

    def test_fail_ready_evidence_fail(self) -> None:
        """FAIL: READY with Evidence FAIL violates Rule C and Rule A."""
        doc = make_card_markdown(
            card_id="DR-FAIL-02",
            evidence_key="FAIL",
            ownership_key="PASS",
            status="READY",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Rule C vi phạm" in e or "Rule A vi phạm" in e for e in errors))

    def test_fail_ready_missing_review_trace(self) -> None:
        """FAIL: READY without Review trace violates Rule C."""
        doc = make_card_markdown(
            card_id="DR-FAIL-03",
            evidence_key="PASS",
            ownership_key="PASS",
            status="READY",
            review_trace="",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Review trace không được để trống" in e for e in errors))

    def test_fail_evidence_fail_status_ready(self) -> None:
        """FAIL: Evidence FAIL but Status READY violates Rule A and Rule C."""
        doc = make_card_markdown(
            card_id="DR-FAIL-04",
            evidence_key="FAIL",
            ownership_key="NOT_APPLICABLE",
            status="READY",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Rule A vi phạm" in e for e in errors))

    def test_fail_ownership_fail_status_simplify(self) -> None:
        """FAIL: Ownership FAIL but Status SIMPLIFY violates Rule B."""
        doc = make_card_markdown(
            card_id="DR-FAIL-05",
            evidence_key="PASS",
            ownership_key="FAIL",
            author_response="[CHƯA CÓ PHẢN HỒI TÁC GIẢ]",
            status="SIMPLIFY",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Rule B vi phạm" in e for e in errors))

    def test_fail_status_khep_gap(self) -> None:
        """FAIL: Status 'Khép Gap' is a banned status value."""
        doc = make_card_markdown(
            card_id="DR-FAIL-06",
            status="Khép Gap",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Status chứa giá trị bị cấm 'KHÉP GAP'" in e for e in errors))

    def test_fail_status_banned_patterns(self) -> None:
        """FAIL: Status containing 'CLOSED', 'ĐÃ SỬA NỘI DUNG', 'RESOLVED'."""
        for banned in ("CLOSED", "ĐÃ SỬA NỘI DUNG", "RESOLVED", "FIXED", "ACCEPTED"):
            doc = make_card_markdown(card_id="DR-FAIL-07", status=banned)
            errors = MODULE.validate_defense_readiness_text(doc, "test.md")
            self.assertTrue(
                any(banned.upper() in e for e in errors),
                f"Expected error for banned status {banned}",
            )

    def test_fail_banned_heading_goi_y_bao_ve(self) -> None:
        """FAIL: Document contains banned heading 'Gợi ý bảo vệ'."""
        doc = (
            make_card_markdown(card_id="DR-FAIL-08")
            + "\n\n### Gợi ý bảo vệ\nSinh viên nên trả lời như sau..."
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Chứa heading/field bị cấm" in e for e in errors))

    def test_fail_banned_label_cau_tra_loi_mau(self) -> None:
        """FAIL: Document contains banned field/label '- **Câu trả lời mẫu:**'."""
        doc = (
            make_card_markdown(card_id="DR-FAIL-09")
            + "\n\n- **Câu trả lời mẫu:** Trả lời theo hướng này..."
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Chứa heading/field bị cấm" in e for e in errors))

    def test_fail_missing_required_field(self) -> None:
        """FAIL: Card missing a required field (e.g. 'Evidence boundary')."""
        doc = """### DR-FAIL-10 — Thiếu field

| Field | Content |
|---|---|
| Section / Claim ID | §1.2.1 |
| Claim type | method/design decision |
| Claim | Mô tả kiểm thử |
| Evidence / Data | S005 |
| Evidence key | PASS |
| Author ownership evidence | S005 |
| Ownership key | PASS |
| Why needed | Mục đích |
| Author must explain | Giải thích |
| Author response | Trả lời |
| Likely defense question | Câu hỏi |
| Text action | NO_TEXT_CHANGE |
| Status | READY |
| Review trace | Reviewer / 2026-10-04 |
"""
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Thiếu trường bắt buộc: 'Evidence boundary'" in e for e in errors))

    def test_fail_fake_author_response_without_ownership(self) -> None:
        """FAIL: Ownership key FAIL but agent provided a fake answer instead of placeholder."""
        doc = make_card_markdown(
            card_id="DR-FAIL-11",
            evidence_key="PASS",
            ownership_key="FAIL",
            author_response="Sinh viên nên trả lời rằng CVE-2017-0144 là trọng tâm",
            status="AUTHOR_CONFIRM",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(
            any("placeholder" in e and "Author response" in e for e in errors),
            f"Expected placeholder error, got: {errors}",
        )

    def test_fail_placeholder_tampered(self) -> None:
        """FAIL: Placeholder has extra generated text appended beside it."""
        doc = make_card_markdown(
            card_id="DR-FAIL-12",
            evidence_key="PASS",
            ownership_key="FAIL",
            author_response="[CHƯA CÓ PHẢN HỒI TÁC GIẢ] - sinh viên nên giải thích thêm",
            status="AUTHOR_CONFIRM",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("không được kèm văn bản giả bên cạnh placeholder" in e for e in errors))

    def test_fail_invalid_text_action(self) -> None:
        """FAIL: Invalid Text action outside closed enum."""
        doc = make_card_markdown(
            card_id="DR-FAIL-13",
            text_action="DO_NOTHING",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Text action 'DO_NOTHING' không thuộc tập hợp hợp lệ" in e for e in errors))

    # --- RULE D TESTS ---

    def test_rule_d_ownership_pass_with_placeholder_response(self) -> None:
        """FAIL: Ownership key = PASS but Author response is placeholder."""
        doc = make_card_markdown(
            card_id="DR-FAIL-D01",
            evidence_key="PASS",
            ownership_key="PASS",
            ownership_evidence="AUTHOR_VOICE.md dòng 67-71",
            author_response="[CHƯA CÓ PHẢN HỒI TÁC GIẢ]",
            status="READY",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Rule D vi phạm" in e for e in errors))

    def test_rule_d_ownership_pass_with_empty_ownership_evidence(self) -> None:
        """FAIL: Ownership key = PASS but Author ownership evidence is empty."""
        doc = make_card_markdown(
            card_id="DR-FAIL-D02",
            evidence_key="PASS",
            ownership_key="PASS",
            ownership_evidence="",
            author_response="Phản hồi thực của tác giả",
            status="READY",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Author ownership evidence" in e for e in errors))

    # --- READY / TEXT ACTION CONSISTENCY TESTS ---

    def test_fail_ready_with_simplify_text_action(self) -> None:
        """FAIL: Status = READY but Text action = SIMPLIFY violates consistency rule."""
        doc = make_card_markdown(
            card_id="DR-FAIL-TA01",
            status="READY",
            text_action="SIMPLIFY",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Status = READY bắt buộc Text action phải là KEEP hoặc NO_TEXT_CHANGE" in e for e in errors))

    def test_fail_ready_with_remove_proposed_text_action(self) -> None:
        """FAIL: Status = READY but Text action = REMOVE_PROPOSED violates consistency rule."""
        doc = make_card_markdown(
            card_id="DR-FAIL-TA02",
            status="READY",
            text_action="REMOVE_PROPOSED",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Status = READY bắt buộc Text action phải là KEEP hoặc NO_TEXT_CHANGE" in e for e in errors))

    def test_fail_ready_with_rewrite_text_action(self) -> None:
        """FAIL: Status = READY but Text action = REWRITE violates consistency rule."""
        doc = make_card_markdown(
            card_id="DR-FAIL-TA03",
            status="READY",
            text_action="REWRITE",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("Status = READY bắt buộc Text action phải là KEEP hoặc NO_TEXT_CHANGE" in e for e in errors))

    # --- DEC COLLISION TESTS ---

    def test_dec22_collision_unqualified(self) -> None:
        """FAIL: Bare DEC-22 reference without full qualification."""
        doc = make_card_markdown(
            card_id="DR-FAIL-DEC01",
            evidence_data="Căn cứ theo DEC-22 và S005",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("DEC_ID_COLLISION_HISTORICAL" in e and "DEC-22" in e for e in errors))

    def test_dec23_collision_unqualified(self) -> None:
        """FAIL: Bare DEC-23 reference without full qualification."""
        doc = make_card_markdown(
            card_id="DR-FAIL-DEC02",
            review_trace="Reviewer / 2026-10-04 / DEC-23",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertTrue(any("DEC_ID_COLLISION_HISTORICAL" in e and "DEC-23" in e for e in errors))

    def test_dec22_collision_qualified(self) -> None:
        """PASS: Properly qualified DEC-22 reference."""
        doc = make_card_markdown(
            card_id="DR-PASS-DEC01",
            ownership_evidence="Tác giả phê duyệt tại DEC-22 — Phê duyệt ba lựa chọn giọng 1B, 2A, 3A — 2026-10-04 — PROJECT_STATE: mục 'Quyết định mới'",
            review_trace="Reviewer / 2026-10-04 / DEC-22 — Phê duyệt ba lựa chọn giọng 1B, 2A, 3A — 2026-10-04 — PROJECT_STATE: mục 'Quyết định mới'",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertEqual([], errors)

    def test_dec23_collision_qualified(self) -> None:
        """PASS: Properly qualified DEC-23 reference."""
        doc = make_card_markdown(
            card_id="DR-PASS-DEC02",
            evidence_data="Căn cứ theo DEC-23 — Cấu hình môi trường lab — 2026-10-04 — PROJECT_STATE: bảng quyết định",
        )
        errors = MODULE.validate_defense_readiness_text(doc, "test.md")
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
