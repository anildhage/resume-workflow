#!/usr/bin/env python3
"""Generate a valid resume filename and save a resume only after validation passes."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from generate_resume_filename import normalize_role_name, next_resume_index
from profile import DEFAULT_PROFILE_DIRECTORY, Profile, load_profile

# Formatting plug-in switch: edit resumeFormatting.yml to control the final cosmetic pass.
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
FORMATTING_KEYS = {
    "evidence_bolding",
    "bold_keywords",
    "bold_supporting_actions",
    "bold_employer_names",
    "bold_job_titles",
    "bold_project_names",
    "minimum_bold_spans",
    "maximum_bold_spans",
}
PDF_KEYS = {
    "enabled",
    "bold_inline_content",
    "bold_organization_names",
    "bold_role_metadata",
    "keep_work_entries_together",
    "body_font_size",
    "section_heading_size",
    "organization_name_size",
    "role_metadata_size",
    "page_margin",
    "body_color",
    "rule_color",
}
DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[1] / "career" / "files"
DEFAULT_MARKDOWN_DIRECTORY = DEFAULT_OUTPUT_ROOT / "md"
DEFAULT_PDF_DIRECTORY = DEFAULT_OUTPUT_ROOT / "pdf"


@dataclass(frozen=True)
class FormattingSettings:
    evidence_bolding: bool = True
    bold_keywords: bool = True
    bold_supporting_actions: bool = True
    bold_employer_names: bool = True
    bold_job_titles: bool = True
    bold_project_names: bool = True
    minimum_bold_spans: int = 10
    maximum_bold_spans: int = 45
    pdf: "PdfSettings" = field(default_factory=lambda: PdfSettings())


@dataclass(frozen=True)
class PdfSettings:
    enabled: bool = True
    bold_inline_content: bool = True
    bold_organization_names: bool = True
    bold_role_metadata: bool = True
    keep_work_entries_together: bool = True
    body_font_size: float = 10.5
    section_heading_size: float = 12.5
    organization_name_size: float = 11.5
    role_metadata_size: float = 10.0
    page_margin: str = "0.55in 0.65in"
    body_color: str = "#111111"
    rule_color: str = "#777777"


def section_name(line: str) -> str | None:
    match = SECTION_HEADING_RE.fullmatch(line.strip())
    if not match:
        return None
    name = match.group(1).strip()
    return name if name in SECTION_NAMES else None


def load_formatting_settings(config_path: Path) -> FormattingSettings:
    """Read the scalar Markdown and PDF cosmetic plug-in settings without a dependency."""
    if not config_path.exists():
        return FormattingSettings()
    formatting_values: dict[str, bool | int] = {}
    pdf_values: dict[str, bool | float | str] = {}
    section = None
    for line in config_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, raw_value = (part.strip() for part in stripped.split(":", 1))
        if key in {"formatting", "pdf"} and not raw_value:
            section = key
            continue
        if section == "formatting":
            valid_keys = FORMATTING_KEYS
        elif section == "pdf":
            valid_keys = PDF_KEYS
        else:
            raise ValueError(f"Unsupported formatting section for setting: {key}")
        if key not in valid_keys:
            raise ValueError(f"Unsupported formatting setting: {key}")
        value = raw_value.lower()
        if value in {"true", "yes"}:
            parsed_value: bool | float | str = True
        elif value in {"false", "no"}:
            parsed_value = False
        elif re.fullmatch(r"\d+(?:\.\d+)?", raw_value):
            parsed_value = float(raw_value) if "." in raw_value else int(raw_value)
        else:
            parsed_value = raw_value.strip('"\'')
        if section == "formatting":
            formatting_values[key] = parsed_value  # type: ignore[assignment]
        else:
            pdf_values[key] = parsed_value
    settings = FormattingSettings(**formatting_values, pdf=PdfSettings(**pdf_values))
    if settings.minimum_bold_spans < 0 or settings.maximum_bold_spans < settings.minimum_bold_spans:
        raise ValueError("Bold span limits must be non-negative and ordered minimum <= maximum")
    if any(
        value <= 0
        for value in (
            settings.pdf.body_font_size,
            settings.pdf.section_heading_size,
            settings.pdf.organization_name_size,
            settings.pdf.role_metadata_size,
        )
    ):
        raise ValueError("PDF font sizes must be positive")
    return settings


def remove_inline_bolding(content: str) -> str:
    return re.sub(r"\*\*([^*\n]+)\*\*", r"\1", content)


def remove_bolding_from_lines(lines: list[str], predicate) -> list[str]:
    return [remove_inline_bolding(line) if predicate(line) else line for line in lines]


def apply_formatting_settings(lines: list[str], settings: FormattingSettings) -> list[str]:
    if not settings.bold_keywords:
        summary_start = next((index for index, line in enumerate(lines) if line.strip() == "## CAREER SUMMARY"), None)
        skills_start = next((index for index, line in enumerate(lines) if line.strip() == "## SKILLS"), None)
        work_start = next((index for index, line in enumerate(lines) if line.strip() == "## WORK EXPERIENCE"), len(lines))
        if summary_start is not None:
            end = skills_start if skills_start is not None else work_start
            lines = [
                remove_inline_bolding(line) if summary_start < index < end else line
                for index, line in enumerate(lines)
            ]
        if skills_start is not None:
            end = work_start
            lines = [
                remove_inline_bolding(line) if skills_start < index < end else line
                for index, line in enumerate(lines)
            ]
    if not settings.bold_supporting_actions:
        work_start = next((index for index, line in enumerate(lines) if line.strip() == "## WORK EXPERIENCE"), None)
        education_start = next((index for index, line in enumerate(lines) if line.strip() == "## EDUCATION"), len(lines))
        projects_start = next((index for index, line in enumerate(lines) if line.strip() == "## PROJECTS"), None)
        if work_start is not None:
            lines = [
                remove_inline_bolding(line) if work_start < index < education_start and line.startswith("- ") else line
                for index, line in enumerate(lines)
            ]
        if projects_start is not None:
            lines = [
                remove_inline_bolding(line) if projects_start < index and line.startswith("  - ") else line
                for index, line in enumerate(lines)
            ]
    if not settings.bold_employer_names:
        lines = remove_bolding_from_lines(
            lines,
            lambda line: line.strip().startswith("**") and line.strip().endswith("**") and "|" not in line,
        )
    if not settings.bold_job_titles:
        lines = remove_bolding_from_lines(lines, lambda line: bool(re.search(r"\|\s*\d{2}/\d{4}\s*-", line)))
    if not settings.bold_project_names:
        lines = remove_bolding_from_lines(lines, lambda line: line.startswith("- **") and "|" in line)
    return lines


def normalize_resume_format(content: str, settings: FormattingSettings, profile: Profile) -> str:
    """Apply presentation formatting after the content-quality gate passes."""
    if not settings.evidence_bolding:
        content = remove_inline_bolding(content)
    lines = content.strip().splitlines()
    if not lines:
        return content

    name_index = next(
        (
            index
            for index, line in enumerate(lines)
            if re.sub(r"[#*\s]", "", line).lower() == re.sub(r"[\s]", "", profile.name).lower()
        ),
        None,
    )
    if name_index is not None:
        header_end = next(
            (index for index in range(name_index + 1, len(lines)) if section_name(lines[index]) == "CAREER SUMMARY"),
            name_index + 1,
        )
        lines = lines[:name_index] + [
            f"# {profile.name}  ",
            f"{profile.location}  |  {profile.phone}  |  {profile.email}  |  {profile.linkedin}",
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
                value = re.sub(r"^\s*(?:-\s+|\*\s+)", "", value).strip()
                if not settings.bold_keywords:
                    value = remove_inline_bolding(value)
                if value and not value.lower().startswith("to be updated"):
                    skill_values.append(value)
        lines = lines[: skills_index + 1] + ["  |  ".join(skill_values)] + lines[skills_end:]

    if settings.evidence_bolding:
        lines = apply_formatting_settings(lines, settings)

    formatted_content = "\n".join(lines).rstrip() + "\n"
    return formatted_content if settings.evidence_bolding else remove_inline_bolding(formatted_content)


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


def validate_presentation(content: str, settings: FormattingSettings, profile: Profile) -> list[str]:
    """Validate the final presentation after cosmetic formatting."""
    lines = content.splitlines()
    errors: list[str] = []
    expected_header = f"# {profile.name}"
    if not lines or lines[0].strip() != expected_header:
        errors.append(f"Formatted resume must start with '{expected_header}'.")
    for name in SECTION_NAMES:
        if f"## {name}" not in lines:
            errors.append(f"Formatted resume is missing the '## {name}' heading.")

    bold_spans = BOLD_RE.findall(content)
    if settings.evidence_bolding and (len(bold_spans) < settings.minimum_bold_spans or len(bold_spans) > settings.maximum_bold_spans):
        errors.append(
            f"Formatted resume must contain between {settings.minimum_bold_spans} and "
            f"{settings.maximum_bold_spans} strategic bold spans."
        )
    if not settings.evidence_bolding and bold_spans:
        errors.append("Headings-only formatting cannot contain inline bold spans.")

    work_start = next((index for index, line in enumerate(lines) if line.strip() == "## WORK EXPERIENCE"), None)
    education_start = next((index for index, line in enumerate(lines) if line.strip() == "## EDUCATION"), len(lines))
    projects_start = next((index for index, line in enumerate(lines) if line.strip() == "## PROJECTS"), None)
    if settings.evidence_bolding and settings.bold_supporting_actions and work_start is not None and not any(
        line.lstrip().startswith("- ") and BOLD_RE.search(line)
        for line in lines[work_start + 1 : education_start]
    ):
        errors.append("Formatted resume must bold at least one supporting action in work experience bullets.")
    if settings.evidence_bolding and settings.bold_supporting_actions and projects_start is not None and not any(
        line.lstrip().startswith("- ") and BOLD_RE.search(line)
        for line in lines[projects_start + 1 :]
    ):
        errors.append("Formatted resume must bold at least one supporting action in project bullets.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a resume file name and save the file only after validation passes.")
    parser.add_argument("--role", required=True, help="Target role, for example 'Data and AI Engineer'.")
    parser.add_argument(
        "--profile",
        type=Path,
        default=DEFAULT_PROFILE_DIRECTORY,
        help="Private profile directory (default: profiles/local).",
    )
    parser.add_argument("--content", help="Resume markdown content to write. If omitted, reads from stdin.")
    parser.add_argument("--formatting-config", type=Path, default=DEFAULT_FORMATTING_CONFIG)
    parser.add_argument("--bolding", choices=("yes", "no"), help="Override evidence_bolding for this generation.")
    parser.add_argument("--directory", type=Path, help="Override the Markdown output directory.")
    parser.add_argument("--pdf-directory", type=Path, help="Override the PDF output directory.")
    parser.add_argument("--css", type=Path, help="Override the CSS stylesheet used for PDF rendering.")
    args = parser.parse_args()

    try:
        profile = load_profile(args.profile)
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    try:
        role_name = normalize_role_name(args.role)
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    content = args.content if args.content is not None else sys.stdin.read()
    try:
        settings = load_formatting_settings(args.formatting_config)
        if args.bolding:
            settings = FormattingSettings(**{**settings.__dict__, "evidence_bolding": args.bolding == "yes"})
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    content_errors = validate_content(content)
    if content_errors:
        print("Content-quality validation failed before formatting:")
        for error in content_errors:
            print(f"- {error}")
        return 1

    formatted_content = normalize_resume_format(content, settings, profile)
    presentation_errors = validate_content(formatted_content) + validate_presentation(formatted_content, settings, profile)
    if presentation_errors:
        print("Final presentation validation failed:")
        for error in presentation_errors:
            print(f"- {error}")
        return 1

    output_dir = args.directory or profile.output_root / "md"
    pdf_directory = args.pdf_directory or profile.output_root / "pdf"
    css_path = args.css or profile.css
    output_dir.mkdir(parents=True, exist_ok=True)
    index = next_resume_index(output_dir, profile.filename_name)
    filename = f"{role_name}-{profile.filename_name}-{index}.md"
    target = output_dir / filename
    pdf_target = pdf_directory / f"{target.stem}.pdf"

    if target.exists() or pdf_target.exists():
        print(f"Error: output for '{target.stem}' already exists. Choose a new role or clean the output directories.")
        return 1

    target.write_text(formatted_content, encoding="utf-8")
    temporary_pdf = pdf_target.with_name(f".{pdf_target.name}.tmp")
    try:
        from render_resume import render_resume

        render_resume(target, temporary_pdf, css_path, settings.pdf)
        temporary_pdf.replace(pdf_target)
    except Exception as exc:
        target.unlink(missing_ok=True)
        temporary_pdf.unlink(missing_ok=True)
        print(f"PDF conversion failed: {exc}")
        return 1

    print(f"Markdown saved: {target}")
    print(f"PDF saved: {pdf_target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
