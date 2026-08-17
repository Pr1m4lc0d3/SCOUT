#!/usr/bin/env python3
"""outcome-lint: check .monkeys/outcome.md carries the fields a human needs.

The linter checks FORM. It cannot know whether a metric actually moved, only
whether the line says what changed, what caused it, where it was measured, and
when. A line that omits those is not wrong; it is uncheckable, which is worse,
because it reads as settled.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple

REQUIRED_SECTIONS = ("Moved", "Flat", "Prune")

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
BULLET_RE = re.compile(r"^-\s+(.*\S)\s*$")
LABEL_RE = re.compile(r"—\s*([a-z][a-z ]*?):", re.IGNORECASE)

ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

SECTION_FIELDS = {
    "Moved": ("by", "after", "source", "on"),
    "Flat": ("measured", "source", "on"),
    "Prune": ("because",),
}


class Finding(NamedTuple):
    line_no: int
    level: str
    message: str


def parse_sections(text):
    """Return {section_name: [(line_no, bullet_text), ...]} for '## ' headings."""
    sections = {}
    current = None
    for line_no, line in enumerate(text.splitlines(), start=1):
        heading = SECTION_RE.match(line)
        if heading:
            current = heading.group(1)
            sections.setdefault(current, [])
            continue
        if current is None:
            continue
        bullet = BULLET_RE.match(line)
        if bullet:
            sections[current].append((line_no, bullet.group(1)))
    return sections


def field_labels(bullet):
    """Return the set of ' — label:' field labels present on one bullet."""
    return {m.group(1).strip().lower() for m in LABEL_RE.finditer(bullet)}


def field_value(bullet, label):
    """Return the text of ' — <label>: value', stopping at the next ' — '."""
    pattern = re.compile(
        r"—\s*" + re.escape(label) + r":\s*(.*?)(?=\s+—\s|$)",
        re.IGNORECASE,
    )
    match = pattern.search(bullet)
    return match.group(1).strip() if match else None


def lint_text(text):
    findings = []
    sections = parse_sections(text)
    for name in REQUIRED_SECTIONS:
        if name not in sections:
            findings.append(
                Finding(0, "error", f"missing required section: {name}")
            )
    for name, required in SECTION_FIELDS.items():
        for line_no, bullet in sections.get(name, []):
            present = field_labels(bullet)
            for label in required:
                if label not in present:
                    findings.append(
                        Finding(
                            line_no,
                            "error",
                            f"{name}: bullet is missing '{label}:'",
                        )
                    )
            on = field_value(bullet, "on")
            if on is not None and not ISO_DATE_RE.match(on):
                findings.append(
                    Finding(
                        line_no,
                        "error",
                        f"{name}: 'on:' must be a YYYY-MM-DD date, got '{on}'",
                    )
                )
    return findings


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="outcome-lint",
        description="Check .monkeys/outcome.md carries its required fields.",
    )
    parser.add_argument("path", help="path to outcome.md")
    args = parser.parse_args(argv)

    path = Path(args.path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"cannot read {path}: {exc}")
        return 1

    findings = lint_text(text)
    if not findings:
        print(f"{path}: clean")
        return 0

    for finding in sorted(findings, key=lambda f: (f.line_no, f.message)):
        print(f"{path}:{finding.line_no}: {finding.level}: {finding.message}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
