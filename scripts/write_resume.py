#!/usr/bin/env python3
"""Generate a valid resume filename and save a resume only after validation passes."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from generate_resume_filename import normalize_role_name, next_resume_index

# Formatting switch: set evidence_bolding to true for keyword/evidence emphasis or false for headings-only output.
DEFAULT_FORMATTING_CONFIG = Path(__file__).resolve().parents[1] / "career" / "resumeFormatting.yml"
PLACEHOLDER_RE = re.compile(r"(?i)-\s*to be updated")
BOLD_RE = re.compile(r"\*\*([^*\n]+)\*\*")
SECTION_NAMES = (
    "CAREER SUMMARY",
    "SKILLS",
    "WORK EXPERIENCE",
    "EDUCATION",
    "CERTIFICATIONS",
    "PROJECTS",
)
SECTION_HEADING_RE = re.compile(r"^\s*(?:#{1,6}\s*)?(?:\*\*)?([A-Z][A-Z &/]*)\s*(?:\*\*)?\s*$")


def section_name(line: str) -> str | None:
    match = SECTION_HEADING_RE.fullmatch(line.strip())
    if not match:
        return None
    name = match.group(1).strip()
    return name if name in SECTION_NAMES else None


def load_bolding_setting(config_path: Path) -> bool:
    """Read the intentionally small YAML switch without requiring a YAML package."""
    if not config_path.exists():
        return True
    for line in config_path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("evidence_bolding:"):
            value = line.split(":", 1)[1].strip().lower()
            if value in {"true", "yes"}:
                return True
            if value in {"false", "no"}:
                return False
            raise ValueError("evidence_bolding must be true/yes or false/no")
    return True


def remove_inline_bolding(content: str) -> str:
    return re.sub(r"\*\*([^*\n]+)\*\*", r"\1", content)


def normalize_resume_format(content: str, evidence_bolding: bool) -> str:
    """Apply presentation formatting after the content-quality gate passes."""
    if not evidence_bolding:
        content = remove_inline_bolding(content)
    lines = content.strip().splitlines()
    if not lines:
        return content

    name_index = next(
        (
            index
            for index, line in enumerate(lines)
            if re.sub(r"[#*\s]", "", line) == "AnilDhage"
        ),
        None,
    )
    if name_index is not None:
        header_end = next(
            (index for index in range(name_index + 1, len(lines)) if section_name(lines[index]) == "CAREER SUMMARY"),
            name_index + 1,
        )
        lines = lines[:name_index] + [
            "# Anil Dhage  ",
            "Montreal, Quebec  |  +1 514 235 8388  |  i.am.dhage@gmail.com  |  linkedin.com/in/anil-dhage",
            "---",
        ] + lines[header_end:]

    lines = [
        f"## {section_name(line)}" if section_name(line) else line
        for line in lines
    ]

    skills_index = next((index for index, line in enumerate(lines) if line.strip() == "## SKILLS"), None)
    if skills_index is not None:
        skills_end = next(
            (
                index
                for index in range(skills_index + 1, len(lines))
                if section_name(lines[index])
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

    formatted_content = "\n".join(lines).rstrip() + "\n"
    return formatted_content if evidence_bolding else remove_inline_bolding(formatted_content)


def validate_content(content: str) -> list[str]:
    """Validate the unformatted content draft before presentation changes."""
    errors: list[str] = []
    if not content.strip():
        errors.append("Resume content cannot be empty.")
    if PLACEHOLDER_RE.search(content):
        errors.append("Resume content contains the placeholder '- to be updated'. Remove it before saving.")
    missing_sections = [
        name for name in SECTION_NAMES
        if not any(section_name(line) == name for line in content.splitlines())
    ]
    if missing_sections:
        errors.append(f"Resume content is missing required sections: {', '.join(missing_sections)}.")
    return errors


def validate_presentation(content: str, evidence_bolding: bool) -> list[str]:
    """Validate the final presentation after cosmetic formatting."""
    lines = content.splitlines()
    errors: list[str] = []
    if not lines or lines[0].strip() != "# Anil Dhage":
        errors.append("Formatted resume must start with '# Anil Dhage'.")
    for name in SECTION_NAMES:
        if f"## {name}" not in lines:
            errors.append(f"Formatted resume is missing the '## {name}' heading.")

    bold_spans = BOLD_RE.findall(content)
    if evidence_bolding and (len(bold_spans) < 10 or len(bold_spans) > 45):
        errors.append("Formatted resume must contain between 10 and 45 strategic bold spans.")
    if not evidence_bolding and bold_spans:
        errors.append("Headings-only formatting cannot contain inline bold spans.")

    work_start = next((index for index, line in enumerate(lines) if line.strip() == "## WORK EXPERIENCE"), None)
    education_start = next((index for index, line in enumerate(lines) if line.strip() == "## EDUCATION"), len(lines))
    projects_start = next((index for index, line in enumerate(lines) if line.strip() == "## PROJECTS"), None)
    if evidence_bolding and work_start is not None and not any(
        line.lstrip().startswith("- ") and BOLD_RE.search(line)
        for line in lines[work_start + 1 : education_start]
    ):
        errors.append("Formatted resume must bold at least one supporting action in work experience bullets.")
    if evidence_bolding and projects_start is not None and not any(
        line.lstrip().startswith("- ") and BOLD_RE.search(line)
        for line in lines[projects_start + 1 :]
    ):
        errors.append("Formatted resume must bold at least one supporting action in project bullets.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a resume file name and save the file only after validation passes.")
    parser.add_argument("--role", required=True, help="Target role, for example 'Data and AI Engineer'.")
    parser.add_argument("--content", help="Resume markdown content to write. If omitted, reads from stdin.")
    parser.add_argument("--formatting-config", type=Path, default=DEFAULT_FORMATTING_CONFIG)
    parser.add_argument("--bolding", choices=("yes", "no"), help="Override evidence_bolding for this generation.")
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

    content = args.content if args.content is not None else sys.stdin.read()
    try:
        evidence_bolding = args.bolding != "no" if args.bolding else load_bolding_setting(args.formatting_config)
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    content_errors = validate_content(content)
    if content_errors:
        print("Content-quality validation failed before formatting:")
        for error in content_errors:
            print(f"- {error}")
        return 1

    formatted_content = normalize_resume_format(content, evidence_bolding)
    presentation_errors = validate_content(formatted_content) + validate_presentation(formatted_content, evidence_bolding)
    if presentation_errors:
        print("Final presentation validation failed:")
        for error in presentation_errors:
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

    target.write_text(formatted_content, encoding="utf-8")
    print(f"Saved: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
