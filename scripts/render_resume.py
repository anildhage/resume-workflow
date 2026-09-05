#!/usr/bin/env python3
"""Render a validated Markdown resume as a styled PDF."""

from __future__ import annotations

from pathlib import Path

import markdown
from weasyprint import CSS, HTML


def render_resume(markdown_path: Path, pdf_path: Path, css_path: Path) -> None:
    """Convert one Markdown resume to PDF using the repository stylesheet."""
    if not markdown_path.is_file():
        raise FileNotFoundError(f"Markdown resume not found: {markdown_path}")
    if not css_path.is_file():
        raise FileNotFoundError(f"PDF stylesheet not found: {css_path}")

    content = markdown_path.read_text(encoding="utf-8")
    rendered_html = markdown.markdown(
        content,
        extensions=["extra", "sane_lists"],
        output_format="html5",
    )
    document = "<!doctype html><html><head><meta charset=\"utf-8\"></head><body>"
    document += rendered_html
    document += "</body></html>"

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=document, base_url=str(markdown_path.parent)).write_pdf(
        str(pdf_path),
        stylesheets=[CSS(filename=str(css_path))],
    )
