#!/usr/bin/env python3
"""Regenerate one PDF from a selected Markdown resume and shared PDF settings."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from render_resume import render_resume
from write_resume import DEFAULT_FORMATTING_CONFIG, load_formatting_settings

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "career" / "pdfBuild.yml"
MARKDOWN_DIRECTORY = ROOT / "career" / "files" / "md"
PDF_DIRECTORY = ROOT / "career" / "files" / "pdf"
CSS_PATH = ROOT / "career" / "resume.css"


@dataclass(frozen=True)
class PdfBuildSettings:
    markdown_file: str
    pdf_file: str
    overwrite: bool = False


def load_build_settings(config_path: Path) -> PdfBuildSettings:
    if not config_path.is_file():
        raise ValueError(f"Build configuration not found: {config_path}")

    values: dict[str, str | bool] = {}
    section = None
    for line in config_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, raw_value = (part.strip() for part in stripped.split(":", 1))
        if key == "pdf_build" and not raw_value:
            section = key
            continue
        if section != "pdf_build" or key not in {"markdown_file", "pdf_file", "overwrite"}:
            raise ValueError(f"Unsupported PDF build setting: {key}")
        value = raw_value.strip('"\'')
        if key == "overwrite":
            if value.lower() not in {"true", "false"}:
                raise ValueError("overwrite must be true or false")
            values[key] = value.lower() == "true"
        else:
            values[key] = value

    try:
        settings = PdfBuildSettings(
            markdown_file=str(values["markdown_file"]),
            pdf_file=str(values["pdf_file"]),
            overwrite=bool(values.get("overwrite", False)),
        )
    except KeyError as exc:
        raise ValueError(f"Missing PDF build setting: {exc.args[0]}") from exc

    for filename, label in ((settings.markdown_file, "markdown_file"), (settings.pdf_file, "pdf_file")):
        if Path(filename).name != filename or not re.fullmatch(r"[^/\\]+", filename):
            raise ValueError(f"{label} must be a filename, not a path")

    if not settings.markdown_file.lower().endswith(".md"):
        raise ValueError("markdown_file must end with .md")
    if not settings.pdf_file.lower().endswith(".pdf"):
        raise ValueError("pdf_file must end with .pdf")
    return settings


def main() -> int:
    config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CONFIG
    try:
        build_settings = load_build_settings(config_path)
        formatting_settings = load_formatting_settings(DEFAULT_FORMATTING_CONFIG)
        if not formatting_settings.pdf.enabled:
            raise ValueError("PDF rendering is disabled in career/resumeFormatting.yml")

        markdown_path = MARKDOWN_DIRECTORY / build_settings.markdown_file
        pdf_path = PDF_DIRECTORY / build_settings.pdf_file
        if not markdown_path.is_file():
            raise FileNotFoundError(f"Markdown resume not found: {markdown_path}")
        if pdf_path.exists() and not build_settings.overwrite:
            raise FileExistsError(
                f"PDF already exists: {pdf_path}. Set overwrite: true in {config_path.name} to replace it."
            )

        render_resume(markdown_path, pdf_path, CSS_PATH, formatting_settings.pdf)
        if not pdf_path.read_bytes().startswith(b"%PDF-"):
            raise ValueError(f"Generated output is not a valid PDF: {pdf_path}")
    except (FileExistsError, FileNotFoundError, ValueError, OSError) as exc:
        print(f"PDF build failed: {exc}")
        return 1

    print(f"PDF saved: {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
