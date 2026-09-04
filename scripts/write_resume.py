#!/usr/bin/env python3
"""Generate a valid resume filename and save a resume only after validation passes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from generate_resume_filename import normalize_role_name, next_resume_index

PLACEHOLDER_RE = re.compile(r"(?i)-\s*to be updated")


def validate_content(content: str) -> list[str]:
    errors: list[str] = []
    if not content.strip():
        errors.append("Resume content cannot be empty.")
    if PLACEHOLDER_RE.search(content):
        errors.append("Resume content contains the placeholder '- to be updated'. Remove it before saving.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a resume file name and save the file only after validation passes.")
    parser.add_argument("--role", required=True, help="Target role, for example 'Data and AI Engineer'.")
    parser.add_argument("--content", help="Resume markdown content to write. If omitted, reads from stdin.")
    parser.add_argument(
        "--directory",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "career" / "files",
        help="Directory where resumes are saved.",
    )
    args = parser.parse_args()

    try:
        role_name = normalize_role_name(args.role)
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    content = args.content
    if content is None:
        content = sys.stdin.read()

    errors = validate_content(content)
    if errors:
        print("Pre-save validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    output_dir = args.directory
    output_dir.mkdir(parents=True, exist_ok=True)
    index = next_resume_index(output_dir)
    filename = f"{role_name}-AnilDhage-{index}.md"
    target = output_dir / filename

    if target.exists():
        print(f"Error: '{target.name}' already exists. Choose a new role or clean the directory.")
        return 1

    target.write_text(content, encoding="utf-8")
    print(f"Saved: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
