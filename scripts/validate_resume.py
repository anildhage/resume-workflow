#!/usr/bin/env python3
"""Validate generated resume files in career/files.

Rules enforced:
- filename must match: RoleName-AnilDhage-{N}.md
- placeholder text '- to be updated' must not appear
- output directory may be empty, but if files exist they must conform
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_PATTERN = re.compile(r"^[A-Za-z]+-AnilDhage-\d+\.md$")
PLACEHOLDER_RE = re.compile(r"(?i)-\s*to be updated")


def collect_resume_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(p for p in directory.iterdir() if p.is_file() and p.suffix.lower() == ".md")


def validate_file(file_path: Path) -> list[str]:
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

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated resume files.")
    parser.add_argument(
        "--directory",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "career" / "files",
        help="Directory containing generated resume files (default: career/files).",
    )
    args = parser.parse_args()

    resume_files = collect_resume_files(args.directory)

    if not resume_files:
        print(f"No generated resumes found in {args.directory}. Validation passed (empty output directory).")
        return 0

    all_errors: list[str] = []
    for file_path in resume_files:
        all_errors.extend(validate_file(file_path))

    if all_errors:
        print("Resume validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(resume_files)} resume file(s) in {args.directory}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
