#!/usr/bin/env python3
"""Validate generated resume files in career/files.

Rules enforced:
- filename must match: RoleName-AnilDhage-{N}.md
- placeholder text '- to be updated' must not appear
- final resume must contain a readable amount of strategic Markdown bolding
- output directory may be empty, but if files exist they must conform
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from calculate_experience import experience_years

DEFAULT_PATTERN = re.compile(r"^[A-Za-z]+-AnilDhage-\d+\.md$")
PLACEHOLDER_RE = re.compile(r"(?i)-\s*to be updated")
EXPERIENCE_RE = re.compile(r"\b(\d+)\+ years of experience\b")
BOLD_RE = re.compile(r"\*\*([^*\n]+)\*\*")
SECTION_NAMES = (
    "CAREER SUMMARY",
    "SKILLS",
    "WORK EXPERIENCE",
    "EDUCATION",
    "CERTIFICATIONS",
    "PROJECTS",
)


def collect_resume_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(p for p in directory.iterdir() if p.is_file() and p.suffix.lower() == ".md")


def validate_file(file_path: Path, expected_experience_years: int) -> list[str]:
    errors: list[str] = []
    file_name = file_path.name

    if not DEFAULT_PATTERN.fullmatch(file_name):
        errors.append(
            f"Invalid filename '{file_name}'. Expected format: RoleName-AnilDhage-<number>.md"
        )

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as exc:  # pragma: no cover - defensive code
        return [f"Unable to read '{file_path}': {exc}"]

    if PLACEHOLDER_RE.search(content):
        errors.append(
            f"Placeholder text found in '{file_name}'. Remove all '- to be updated' entries before saving."
        )

    lines = content.splitlines()
    if not lines or lines[0].strip() != "# Anil Dhage":
        errors.append(f"'{file_name}' must start with '# Anil Dhage'.")
    for section_name in SECTION_NAMES:
        if f"## {section_name}" not in lines:
            errors.append(f"'{file_name}' is missing the '## {section_name}' heading.")

    experience_claims = [int(value) for value in EXPERIENCE_RE.findall(content)]
    if not experience_claims:
        errors.append(
            f"No experience statement found in '{file_name}'. Include '{expected_experience_years}+ years of experience'."
        )
    elif any(value != expected_experience_years for value in experience_claims):
        errors.append(
            f"Experience statement in '{file_name}' does not match the skeleton-derived value of "
            f"'{expected_experience_years}+ years of experience'."
        )

    bold_spans = BOLD_RE.findall(content)
    if len(bold_spans) < 10 or len(bold_spans) > 30:
        errors.append(
            f"'{file_name}' contains {len(bold_spans)} bold spans. "
            "Final formatting must contain between 10 and 30 strategic bold spans."
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated resume files.")
    parser.add_argument(
        "--directory",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "career" / "files",
        help="Directory containing generated resume files (default: career/files).",
    )
    parser.add_argument(
        "--skeleton",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "career" / "resumeSkeleton.md",
        help="Authoritative skeleton used to calculate experience.",
    )
    args = parser.parse_args()

    resume_files = collect_resume_files(args.directory)

    if not resume_files:
        print(f"No generated resumes found in {args.directory}. Validation passed (empty output directory).")
        return 0

    expected_experience_years = experience_years(args.skeleton)
    all_errors: list[str] = []
    for file_path in resume_files:
        all_errors.extend(validate_file(file_path, expected_experience_years))

    if all_errors:
        print("Resume validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(resume_files)} resume file(s) in {args.directory}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
