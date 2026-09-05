#!/usr/bin/env python3
"""Validate generated resume files in career/files.

Rules enforced:
- filename must match: RoleName-ProfileName-{N}.md
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
from profile import DEFAULT_PROFILE_DIRECTORY, load_profile
from write_resume import FormattingSettings, load_formatting_settings

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


def validate_pdf(pdf_path: Path) -> list[str]:
    if not pdf_path.is_file():
        return [f"Missing matching PDF '{pdf_path.name}' in {pdf_path.parent}."]
    try:
        content = pdf_path.read_bytes()
    except Exception as exc:  # pragma: no cover - defensive code
        return [f"Unable to read '{pdf_path}': {exc}"]
    if not content.startswith(b"%PDF-"):
        return [f"'{pdf_path.name}' is not a valid PDF file."]
    return []


def validate_file(
    file_path: Path,
    expected_experience_years: int,
    settings: FormattingSettings,
    profile_name: str,
    profile_display_name: str,
) -> list[str]:
    errors: list[str] = []
    file_name = file_path.name

    pattern = re.compile(rf"^[A-Za-z0-9]+-{re.escape(profile_name)}-\d+\.md$")
    if not pattern.fullmatch(file_name):
        errors.append(
            f"Invalid filename '{file_name}'. Expected format: RoleName-{profile_name}-<number>.md"
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
    if not lines or lines[0].strip() != f"# {profile_display_name}":
        errors.append(f"'{file_name}' must start with '# {profile_display_name}'.")
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
    if settings.evidence_bolding and (len(bold_spans) < settings.minimum_bold_spans or len(bold_spans) > settings.maximum_bold_spans):
        errors.append(
            f"'{file_name}' contains {len(bold_spans)} bold spans. "
            f"Evidence-bold formatting must contain between {settings.minimum_bold_spans} and "
            f"{settings.maximum_bold_spans} strategic bold spans."
        )
    if not settings.evidence_bolding and bold_spans:
        errors.append(f"'{file_name}' must contain no inline bold spans in headings-only mode.")

    work_start = next((index for index, line in enumerate(lines) if line.strip() == "## WORK EXPERIENCE"), None)
    education_start = next((index for index, line in enumerate(lines) if line.strip() == "## EDUCATION"), len(lines))
    projects_start = next((index for index, line in enumerate(lines) if line.strip() == "## PROJECTS"), None)
    if settings.evidence_bolding and settings.bold_supporting_actions and work_start is not None and not any(
        line.lstrip().startswith("- ") and BOLD_RE.search(line)
        for line in lines[work_start + 1 : education_start]
    ):
        errors.append(f"'{file_name}' must bold at least one supporting action in work experience bullets.")
    if settings.evidence_bolding and settings.bold_supporting_actions and projects_start is not None and not any(
        line.lstrip().startswith("- ") and BOLD_RE.search(line)
        for line in lines[projects_start + 1 :]
    ):
        errors.append(f"'{file_name}' must bold at least one supporting action in project bullets.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated resume files.")
    parser.add_argument(
        "--profile",
        type=Path,
        default=DEFAULT_PROFILE_DIRECTORY,
        help="Private profile directory (default: profiles/local).",
    )
    parser.add_argument(
        "--directory",
        type=Path,
        default=None,
        help="Directory containing generated Markdown resumes (default: career/files/md).",
    )
    parser.add_argument(
        "--skeleton",
        type=Path,
        default=None,
        help="Authoritative skeleton used to calculate experience (default: selected profile).",
    )
    parser.add_argument(
        "--pdf-directory",
        type=Path,
        default=None,
        help="Directory containing matching PDF resumes (default: career/files/pdf).",
    )
    parser.add_argument(
        "--formatting-config",
        type=Path,
        default=None,
        help="Cosmetic formatting configuration file.",
    )
    args = parser.parse_args()
    try:
        profile = load_profile(args.profile)
    except ValueError as exc:
        print(f"Formatting configuration failed: {exc}")
        return 1

    markdown_directory = args.directory or profile.output_root / "md"
    skeleton = args.skeleton or profile.skeleton
    pdf_directory = args.pdf_directory or profile.output_root / "pdf"
    formatting_config = args.formatting_config or profile.formatting_config

    resume_files = collect_resume_files(markdown_directory)
    pdf_files = {
        path.name for path in pdf_directory.iterdir()
        if path.is_file() and path.suffix.lower() == ".pdf"
    } if pdf_directory.exists() else set()

    if not resume_files:
        if pdf_files:
            print("Resume validation failed:")
            for pdf_file in sorted(pdf_files):
                print(f"- Unexpected PDF '{pdf_file}' has no matching Markdown resume.")
            return 1
        print(f"No generated resumes found in {markdown_directory}. Validation passed (empty output directory).")
        return 0

    expected_experience_years = experience_years(skeleton)
    try:
        settings = load_formatting_settings(formatting_config)
    except ValueError as exc:
        print(f"Formatting configuration failed: {exc}")
        return 1
    all_errors: list[str] = []
    for file_path in resume_files:
        all_errors.extend(validate_file(file_path, expected_experience_years, settings, profile.filename_name, profile.name))
        all_errors.extend(validate_pdf(pdf_directory / f"{file_path.stem}.pdf"))

    expected_pdf_files = {f"{file_path.stem}.pdf" for file_path in resume_files}
    for unexpected_pdf in sorted(pdf_files - expected_pdf_files):
        all_errors.append(f"Unexpected PDF '{unexpected_pdf}' has no matching Markdown resume.")

    if all_errors:
        print("Resume validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(resume_files)} resume file(s) in {markdown_directory}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
