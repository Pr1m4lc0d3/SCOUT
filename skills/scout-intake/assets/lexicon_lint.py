#!/usr/bin/env python3
"""lexicon-lint — check .monkeys/lexicon.md carries the fields a human needs.

The linter checks FORM. It cannot know whether a captured phrase is real, only
whether the line says where it was heard, how far it reached, and whether anyone
checked it. A line that omits those is not wrong; it is uncheckable, which is
worse, because it reads as settled.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple

REQUIRED_SECTIONS = (
    "Vocabulary",
    "Wants",
    "Objections",
    "Unanswered",
    "Demand signals",
)

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
BULLET_RE = re.compile(r"^-\s+(.*\S)\s*$")
LABEL_RE = re.compile(r"—\s*([a-z][a-z ]*?):", re.IGNORECASE)

ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
REACH_RE = re.compile(r"^(?:unknown|[\d,]+)$", re.IGNORECASE)

SECTION_FIELDS = {
    "Vocabulary": ("heard in", "verified"),
    "Wants": ("because", "verified"),
    "Objections": ("heard in", "reach", "verified"),
    "Unanswered": ("asked in", "reach"),
    "Demand signals": ("measure", "source", "on", "verified"),
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
            verified = field_value(bullet, "verified")
            if verified is not None:
                head = verified.split(",")[0].strip().lower()
                if head not in ("yes", "no"):
                    findings.append(
                        Finding(
                            line_no,
                            "error",
                            f"{name}: 'verified:' must be yes or no, "
                            f"got '{verified}'",
                        )
                    )
                elif head == "yes" and not ISO_DATE_RE.search(verified):
                    findings.append(
                        Finding(
                            line_no,
                            "error",
                            f"{name}: 'verified: yes' needs the YYYY-MM-DD "
                            "it was checked",
                        )
                    )
            reach = field_value(bullet, "reach")
            if reach is not None and not REACH_RE.match(reach):
                findings.append(
                    Finding(
                        line_no,
                        "error",
                        f"{name}: 'reach:' must be a number or 'unknown', "
                        f"got '{reach}'",
                    )
                )
    return findings


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="lexicon-lint",
        description="Check .monkeys/lexicon.md carries its required fields.",
    )
    parser.add_argument("path", help="path to lexicon.md")
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
