import sys
import unittest
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "skills" / "scout-geo" / "assets"
sys.path.insert(0, str(ASSETS))

import geo_lint  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def read(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


class TestSectionParsing(unittest.TestCase):
    def test_parses_every_required_section(self):
        sections = geo_lint.parse_sections(read("discoverability-good.md"))
        self.assertEqual(set(sections), set(geo_lint.REQUIRED_SECTIONS))

    def test_parses_bullets_with_line_numbers(self):
        sections = geo_lint.parse_sections(read("discoverability-good.md"))
        results = sections["Results"]
        self.assertEqual(len(results), 2)
        line_no, text = results[0]
        self.assertIsInstance(line_no, int)
        self.assertTrue(text.startswith("is there a tool"))

    def test_missing_section_is_an_error(self):
        text = (
            "# Discoverability\n\n"
            "## Queries\n"
            "- a query — source: lexicon.md\n"
        )
        findings = geo_lint.lint_text(text)
        messages = [f.message for f in findings]
        self.assertIn("missing required section: Results", messages)
        self.assertIn("missing required section: Fix", messages)

    def test_good_fixture_has_no_missing_section_errors(self):
        findings = geo_lint.lint_text(read("discoverability-good.md"))
        missing = [f for f in findings if "missing required section" in f.message]
        self.assertEqual(missing, [])


class TestRequiredFields(unittest.TestCase):
    def test_field_labels_extracts_labels(self):
        bullet = "a query — assistant: Claude — found: no — as: nothing came up — on: 2026-08-15"
        self.assertEqual(
            geo_lint.field_labels(bullet),
            {"assistant", "found", "as", "on"},
        )

    def test_queries_bullet_needs_source(self):
        findings = geo_lint.lint_text(read("discoverability-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Queries: bullet is missing 'source:'", messages)

    def test_results_bullet_needs_assistant(self):
        findings = geo_lint.lint_text(read("discoverability-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Results: bullet is missing 'assistant:'", messages)

    def test_results_bullet_needs_found(self):
        findings = geo_lint.lint_text(read("discoverability-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Results: bullet is missing 'found:'", messages)

    def test_results_bullet_needs_on(self):
        findings = geo_lint.lint_text(read("discoverability-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Results: bullet is missing 'on:'", messages)

    def test_fix_bullet_needs_because(self):
        findings = geo_lint.lint_text(read("discoverability-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn("Fix: bullet is missing 'because:'", messages)

    def test_findings_carry_the_offending_line_number(self):
        findings = [
            f
            for f in geo_lint.lint_text(read("discoverability-bad.md"))
            if "missing 'because:'" in f.message
        ]
        self.assertEqual(len(findings), 1)
        self.assertGreater(findings[0].line_no, 0)

    def test_good_fixture_has_no_field_errors(self):
        findings = geo_lint.lint_text(read("discoverability-good.md"))
        field_errors = [f for f in findings if "missing '" in f.message]
        self.assertEqual(field_errors, [])


class TestGradingIntegrity(unittest.TestCase):
    def test_field_value_reads_a_value(self):
        bullet = "a query — assistant: Claude — found: no — on: 2026-08-15"
        self.assertEqual(geo_lint.field_value(bullet, "on"), "2026-08-15")

    def test_field_value_returns_none_when_absent(self):
        self.assertIsNone(geo_lint.field_value("plain text", "on"))

    def test_found_must_be_yes_or_no(self):
        findings = geo_lint.lint_text(read("discoverability-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn(
            "Results: 'found:' must be yes or no, got 'maybe'", messages
        )

    def test_found_accepts_yes_or_no(self):
        text = (
            "## Results\n"
            "- a query — assistant: Claude — found: yes — on: 2026-08-15\n"
            "- another query — assistant: Claude — found: no — on: 2026-08-15\n"
        )
        messages = [f.message for f in geo_lint.lint_text(text)]
        self.assertEqual([m for m in messages if "'found:' must be" in m], [])

    def test_on_must_be_an_iso_date(self):
        findings = geo_lint.lint_text(read("discoverability-bad.md"))
        messages = [f.message for f in findings]
        self.assertIn(
            "Results: 'on:' must be a YYYY-MM-DD date, got 'next week'", messages
        )

    def test_on_with_a_valid_date_is_accepted(self):
        text = (
            "## Results\n"
            "- a query — assistant: Claude — found: yes — on: 2026-08-15\n"
        )
        messages = [f.message for f in geo_lint.lint_text(text)]
        self.assertEqual([m for m in messages if "'on:' must be" in m], [])

    def test_on_rejects_a_trailing_date_not_the_whole_value(self):
        text = (
            "## Results\n"
            "- a query — assistant: Claude — found: yes — on: sometime 2026-08-15\n"
        )
        messages = [f.message for f in geo_lint.lint_text(text)]
        self.assertIn(
            "Results: 'on:' must be a YYYY-MM-DD date, got 'sometime 2026-08-15'",
            messages,
        )

    def test_good_fixture_passes_grading_rules(self):
        findings = geo_lint.lint_text(read("discoverability-good.md"))
        grading = [f for f in findings if "must be" in f.message]
        self.assertEqual(grading, [])


import contextlib  # noqa: E402
import io  # noqa: E402


class TestCli(unittest.TestCase):
    def run_main(self, name):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = geo_lint.main([str(FIXTURES / name)])
        return code, buffer.getvalue()

    def test_clean_file_exits_zero(self):
        code, output = self.run_main("discoverability-good.md")
        self.assertEqual(code, 0)
        self.assertIn("clean", output)

    def test_dirty_file_exits_one(self):
        code, _ = self.run_main("discoverability-bad.md")
        self.assertEqual(code, 1)

    def test_dirty_file_prints_path_line_and_message(self):
        _, output = self.run_main("discoverability-bad.md")
        self.assertIn("discoverability-bad.md:", output)
        self.assertIn("missing 'because:'", output)

    def test_missing_file_exits_one_with_a_reason(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = geo_lint.main([str(FIXTURES / "nope.md")])
        self.assertEqual(code, 1)
        self.assertIn("cannot read", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
