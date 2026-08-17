import sys
import unittest
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "skills" / "scout-outcome" / "assets"
sys.path.insert(0, str(ASSETS))

import outcome_lint  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def read(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


class TestSectionParsing(unittest.TestCase):
    def test_parses_every_required_section(self):
        sections = outcome_lint.parse_sections(read("outcome-good.md"))
        self.assertEqual(set(sections), set(outcome_lint.REQUIRED_SECTIONS))

    def test_parses_bullets_with_line_numbers(self):
        sections = outcome_lint.parse_sections(read("outcome-good.md"))
        moved = sections["Moved"]
        self.assertEqual(len(moved), 2)
        line_no, text = moved[0]
        self.assertIsInstance(line_no, int)
        self.assertTrue(text.startswith("newsletter signups"))

    def test_missing_section_is_an_error(self):
        text = "# Outcome\n\n## Moved\n- a metric — by: +1 — after: a move — source: x — on: 2026-08-10\n"
        findings = outcome_lint.lint_text(text)
        messages = [f.message for f in findings]
        self.assertIn("missing required section: Flat", messages)
        self.assertIn("missing required section: Prune", messages)

    def test_good_fixture_has_no_missing_section_errors(self):
        findings = outcome_lint.lint_text(read("outcome-good.md"))
        missing = [f for f in findings if "missing required section" in f.message]
        self.assertEqual(missing, [])


class TestRequiredFields(unittest.TestCase):
    def test_field_labels_extracts_labels(self):
        bullet = "a metric — by: +1 — after: a move — source: x — on: 2026-08-10"
        self.assertEqual(
            outcome_lint.field_labels(bullet),
            {"by", "after", "source", "on"},
        )

    def test_moved_bullet_needs_source(self):
        findings = outcome_lint.lint_text(read("outcome-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Moved: bullet is missing 'source:'", messages)

    def test_moved_bullet_needs_by(self):
        findings = outcome_lint.lint_text(read("outcome-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Moved: bullet is missing 'by:'", messages)

    def test_prune_bullet_needs_because(self):
        findings = outcome_lint.lint_text(read("outcome-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Prune: bullet is missing 'because:'", messages)

    def test_findings_carry_the_offending_line_number(self):
        findings = [
            f
            for f in outcome_lint.lint_text(read("outcome-bad.md"))
            if "missing 'because:'" in f.message
        ]
        self.assertEqual(len(findings), 1)
        self.assertGreater(findings[0].line_no, 0)

    def test_good_fixture_has_no_field_errors(self):
        findings = outcome_lint.lint_text(read("outcome-good.md"))
        field_errors = [f for f in findings if "missing '" in f.message]
        self.assertEqual(field_errors, [])


class TestGradingIntegrity(unittest.TestCase):
    def test_field_value_reads_a_value(self):
        bullet = "a metric — by: +1 — after: a move — source: x — on: 2026-08-10"
        self.assertEqual(outcome_lint.field_value(bullet, "on"), "2026-08-10")

    def test_field_value_returns_none_when_absent(self):
        self.assertIsNone(outcome_lint.field_value("plain text", "on"))

    def test_on_must_be_an_iso_date(self):
        findings = outcome_lint.lint_text(read("outcome-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn(
            "Flat: 'on:' must be a YYYY-MM-DD date, got 'next week'", messages
        )

    def test_on_with_a_valid_date_is_accepted(self):
        text = (
            "## Flat\n"
            "- a metric — measured: x — source: y — on: 2026-08-10\n"
        )
        messages = [f.message for f in outcome_lint.lint_text(text)]
        self.assertEqual([m for m in messages if "'on:' must be" in m], [])

    def test_on_rejects_a_trailing_date_not_the_whole_value(self):
        text = (
            "## Flat\n"
            "- a metric — measured: x — source: y — on: sometime 2026-08-10\n"
        )
        messages = [f.message for f in outcome_lint.lint_text(text)]
        self.assertIn(
            "Flat: 'on:' must be a YYYY-MM-DD date, got 'sometime 2026-08-10'",
            messages,
        )

    def test_good_fixture_passes_grading_rules(self):
        findings = outcome_lint.lint_text(read("outcome-good.md"))
        grading = [f for f in findings if "must be" in f.message]
        self.assertEqual(grading, [])


import contextlib  # noqa: E402
import io  # noqa: E402


class TestCli(unittest.TestCase):
    def run_main(self, name):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = outcome_lint.main([str(FIXTURES / name)])
        return code, buffer.getvalue()

    def test_clean_file_exits_zero(self):
        code, output = self.run_main("outcome-good.md")
        self.assertEqual(code, 0)
        self.assertIn("clean", output)

    def test_dirty_file_exits_one(self):
        code, _ = self.run_main("outcome-bad.md")
        self.assertEqual(code, 1)

    def test_dirty_file_prints_path_line_and_message(self):
        _, output = self.run_main("outcome-bad.md")
        self.assertIn("outcome-bad.md:", output)
        self.assertIn("missing 'because:'", output)

    def test_missing_file_exits_one_with_a_reason(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = outcome_lint.main([str(FIXTURES / "nope.md")])
        self.assertEqual(code, 1)
        self.assertIn("cannot read", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
