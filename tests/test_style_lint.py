from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents" / "skills" / "thesis-research-and-writing" / "scripts" / "lint_vi_academic.py"
SPEC = importlib.util.spec_from_file_location("lint_vi_academic", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class StyleLintTests(unittest.TestCase):
    def test_generic_fixture_exposes_multiple_failure_classes(self) -> None:
        path = ROOT / "tests" / "fixtures" / "style_generic_vi.md"
        findings = MODULE.lint_file(path)
        rules = {item.rule for item in findings}
        self.assertTrue({"VI001", "VI002", "VI005", "VI008"}.issubset(rules))
        self.assertGreaterEqual(len(findings), 7)

    def test_grounded_fixture_avoids_formulaic_phrase_rules(self) -> None:
        path = ROOT / "tests" / "fixtures" / "style_grounded_vi.md"
        findings = MODULE.lint_file(path)
        phrase_findings = [item for item in findings if item.rule <= "VI010"]
        self.assertEqual([], phrase_findings)

    def test_publication_mode_rejects_unresolved_labels(self) -> None:
        findings = MODULE.lint_text("Kết quả này còn [CẦN DỮ LIỆU].", publication=True)
        self.assertTrue(any(item.rule == "VI015" and item.severity == "error" for item in findings))

    def test_long_line_with_short_sentences_is_not_a_long_sentence(self) -> None:
        text = (
            "Cấu hình A hoàn tất ba lần đo. Cấu hình B không hoàn tất bắt tay TCP. "
            "Kết quả này chỉ áp dụng cho topology phòng lab đã mô tả."
        )
        findings = MODULE.lint_text(text)
        self.assertFalse(any(item.rule == "VI011" for item in findings))


if __name__ == "__main__":
    unittest.main()
