#!/usr/bin/env python3
"""Generate a valid resume filename and save a resume only after validation passes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from generate_resume_filename import normalize_role_name, next_resume_index

PLACEHOLDER_RE = re.compile(r"(?i)-\s*to be updated")
SECTION_HEADING_RE = re.compile(r"^[A-Z][A-Z &/]+$")


def normalize_resume_format(content: str) -> str:
    """Apply the canonical header and skills layout before saving a resume."""
    lines = content.strip().splitlines()
    if not lines:
        return content

    name_index = next((index for index, line in enumerate(lines) if line.strip() == "Anil Dhage"), None)
    if name_index is not None:
        header_end = next(
            (index for index in range(name_index + 1, len(lines)) if lines[index].strip() == "CAREER SUMMARY"),
            name_index + 1,
        )
        lines = lines[:name_index] + [
            "Anil Dhage  ",
            "Montreal, Quebec  |  +1 514 235 8388  |  i.am.dhage@gmail.com  |  linkedin.com/in/anil-dhage",
            "---",
        ] + lines[header_end:]

    skills_index = next((index for index, line in enumerate(lines) if line.strip() == "SKILLS"), None)
    if skills_index is not None:
        skills_end = next(
            (
                index
                for index in range(skills_index + 1, len(lines))
                if SECTION_HEADING_RE.fullmatch(lines[index].strip())
            ),
            len(lines),
        )
        skill_values = []
        for line in lines[skills_index + 1 : skills_end]:
            for value in line.split("|"):
                value = re.sub(r"^\s*[-*]\s*", "", value).strip()
                if value and not value.lower().startswith("to be updated"):
                    skill_values.append(value)
        lines = lines[: skills_index + 1] + ["  |  ".join(skill_values)] + lines[skills_end:]

    return "\n".join(lines).rstrip() + "\n"


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
    content = normalize_resume_format(content)

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
