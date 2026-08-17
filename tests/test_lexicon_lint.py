import sys
import unittest
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "skills" / "raid-intake" / "assets"
sys.path.insert(0, str(ASSETS))

import lexicon_lint  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def read(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


class TestSectionParsing(unittest.TestCase):
    def test_parses_every_required_section(self):
        sections = lexicon_lint.parse_sections(read("lexicon-good.md"))
        self.assertEqual(
            set(sections), set(lexicon_lint.REQUIRED_SECTIONS)
        )

    def test_parses_bullets_with_line_numbers(self):
        sections = lexicon_lint.parse_sections(read("lexicon-good.md"))
        vocab = sections["Vocabulary"]
        self.assertEqual(len(vocab), 2)
        line_no, text = vocab[0]
        self.assertIsInstance(line_no, int)
        self.assertTrue(text.startswith('"structure the disagreement"'))

    def test_missing_section_is_an_error(self):
        text = "# Lexicon\n\n## Vocabulary\n- a term — heard in: x — verified: no\n"
        findings = lexicon_lint.lint_text(text)
        messages = [f.message for f in findings]
        self.assertIn("missing required section: Wants", messages)

    def test_good_fixture_has_no_missing_section_errors(self):
        findings = lexicon_lint.lint_text(read("lexicon-good.md"))
        missing = [f for f in findings if "missing required section" in f.message]
        self.assertEqual(missing, [])


class TestRequiredFields(unittest.TestCase):
    def test_field_labels_extracts_labels(self):
        bullet = '"a term" — heard in: a forum — reach: 50 — verified: no'
        self.assertEqual(
            lexicon_lint.field_labels(bullet),
            {"heard in", "reach", "verified"},
        )

    def test_vocabulary_bullet_needs_heard_in(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Vocabulary: bullet is missing 'heard in:'", messages)

    def test_wants_bullet_needs_because(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Wants: bullet is missing 'because:'", messages)

    def test_objections_bullet_needs_reach(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Objections: bullet is missing 'reach:'", messages)

    def test_unanswered_bullet_needs_reach(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Unanswered: bullet is missing 'reach:'", messages)

    def test_demand_signal_needs_on_date(self):
        findings = lexicon_lint.lint_text(read("lexicon-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Demand signals: bullet is missing 'on:'", messages)

    def test_findings_carry_the_offending_line_number(self):
        findings = [
            f
            for f in lexicon_lint.lint_text(read("lexicon-bad.md"))
            if "missing 'because:'" in f.message
        ]
        self.assertEqual(len(findings), 1)
        self.assertGreater(findings[0].line_no, 0)

    def test_good_fixture_has_no_field_errors(self):
        findings = lexicon_lint.lint_text(read("lexicon-good.md"))
        field_errors = [f for f in findings if "missing '" in f.message]
        self.assertEqual(field_errors, [])


class TestGradingIntegrity(unittest.TestCase):
    def test_field_value_reads_a_value(self):
        bullet = '"a term" — heard in: a forum — verified: yes, 2026-08-17'
        self.assertEqual(lexicon_lint.field_value(bullet, "heard in"), "a forum")

    def test_field_value_returns_none_when_absent(self):
        self.assertIsNone(lexicon_lint.field_value("plain text", "verified"))

    def test_verified_must_be_yes_or_no(self):
        text = (
            "## Vocabulary\n"
            "- a term — heard in: a forum — verified: maybe\n"
        )
        messages = [f.message for f in lexicon_lint.lint_text(text)]
        self.assertIn(
            "Vocabulary: 'verified:' must be yes or no, got 'maybe'", messages
        )

    def test_verified_yes_requires_a_date_on_the_line(self):
        text = (
            "## Vocabulary\n"
            "- a term — heard in: a forum — verified: yes\n"
        )
        messages = [f.message for f in lexicon_lint.lint_text(text)]
        self.assertIn(
            "Vocabulary: 'verified: yes' needs the YYYY-MM-DD it was checked",
            messages,
        )

    def test_verified_yes_with_a_date_is_accepted(self):
        text = (
            "## Vocabulary\n"
            "- a term — heard in: a forum — verified: yes, 2026-08-17\n"
        )
        messages = [f.message for f in lexicon_lint.lint_text(text)]
        self.assertNotIn(
            "Vocabulary: 'verified: yes' needs the YYYY-MM-DD it was checked",
            messages,
        )

    def test_reach_must_be_a_number_or_unknown(self):
        text = (
            "## Objections\n"
            "- a gripe — heard in: a forum — reach: lots — verified: no\n"
        )
        messages = [f.message for f in lexicon_lint.lint_text(text)]
        self.assertIn(
            "Objections: 'reach:' must be a number or 'unknown', got 'lots'",
            messages,
        )

    def test_reach_unknown_is_accepted(self):
        text = (
            "## Objections\n"
            "- a gripe — heard in: a forum — reach: unknown — verified: no\n"
        )
        messages = [f.message for f in lexicon_lint.lint_text(text)]
        self.assertEqual(
            [m for m in messages if "reach:" in m and "missing" not in m], []
        )

    def test_good_fixture_passes_grading_rules(self):
        findings = lexicon_lint.lint_text(read("lexicon-good.md"))
        grading = [
            f
            for f in findings
            if "must be" in f.message or "needs the" in f.message
        ]
        self.assertEqual(grading, [])

    def test_verified_yes_cannot_borrow_another_fields_date(self):
        text = (
            "## Demand signals\n"
            "- stars still climbing — measure: stars — source: an API — on: 2026-08-17 — verified: yes\n"
        )
        messages = [f.message for f in lexicon_lint.lint_text(text)]
        self.assertIn(
            "Demand signals: 'verified: yes' needs the YYYY-MM-DD it was checked",
            messages,
        )


import contextlib  # noqa: E402
import io  # noqa: E402


class TestCli(unittest.TestCase):
    def run_main(self, name):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = lexicon_lint.main([str(FIXTURES / name)])
        return code, buffer.getvalue()

    def test_clean_file_exits_zero(self):
        code, output = self.run_main("lexicon-good.md")
        self.assertEqual(code, 0)
        self.assertIn("clean", output)

    def test_dirty_file_exits_one(self):
        code, _ = self.run_main("lexicon-bad.md")
        self.assertEqual(code, 1)

    def test_dirty_file_prints_path_line_and_message(self):
        _, output = self.run_main("lexicon-bad.md")
        self.assertIn("lexicon-bad.md:", output)
        self.assertIn("missing 'because:'", output)

    def test_missing_file_exits_one_with_a_reason(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = lexicon_lint.main([str(FIXTURES / "nope.md")])
        self.assertEqual(code, 1)
        self.assertIn("cannot read", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
