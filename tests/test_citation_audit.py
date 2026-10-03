from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_ieee_citations.py"
SPEC = importlib.util.spec_from_file_location("audit_ieee_citations", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CitationAuditTests(unittest.TestCase):
    def test_clean_ieee_document(self) -> None:
        text = "Nội dung [1]. Tiếp theo [2].\n\n## TÀI LIỆU THAM KHẢO\n\n[1] Nguồn A.\n[2] Nguồn B."
        summary, issues = MODULE.audit_text(text)
        self.assertEqual([1, 2], summary["first_appearance"])
        self.assertEqual([], issues)

    def test_missing_orphan_and_order_are_reported(self) -> None:
        text = "Nội dung [2].\n\n## TÀI LIỆU THAM KHẢO\n\n[1] Nguồn A.\n[3] Nguồn C."
        _, issues = MODULE.audit_text(text)
        codes = {item.code for item in issues}
        self.assertTrue({"IEEE003", "IEEE004", "IEEE005", "IEEE006"}.issubset(codes))

    def test_range_is_expanded(self) -> None:
        text = "Nội dung [1–3].\n\n## TÀI LIỆU THAM KHẢO\n\n[1] A.\n[2] B.\n[3] C."
        summary, _ = MODULE.audit_text(text)
        self.assertEqual([1, 2, 3], summary["used_numbers"])


if __name__ == "__main__":
    unittest.main()
