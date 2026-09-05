#!/usr/bin/env python3
"""Render a validated Markdown resume as a styled PDF."""

from __future__ import annotations

from pathlib import Path
from xml.etree.ElementTree import Element

import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from weasyprint import CSS, HTML


class ResumeStructureTreeprocessor(Treeprocessor):
    """Add PDF-only classes without changing the source Markdown."""

    def run(self, root):
        children = list(root)
        for section_index, element in enumerate(children):
            if element.tag != "h2" or (element.text or "").strip() != "WORK EXPERIENCE":
                continue

            section_end = next(
                (index for index in range(section_index + 1, len(children)) if children[index].tag == "h2"),
                len(children),
            )
            index = section_index + 1
            while index < section_end - 2:
                organization, role_meta, bullets = children[index : index + 3]
                if not (
                    organization.tag == "p"
                    and role_meta.tag == "p"
                    and bullets.tag == "ul"
                ):
                    index += 1
                    continue

                organization.set("class", "organization")
                role_meta.set("class", "role-meta")
                entry = Element("div", {"class": "experience-entry"})
                root.remove(organization)
                root.remove(role_meta)
                root.remove(bullets)
                entry.extend([organization, role_meta, bullets])
                root.insert(index, entry)
                children = list(root)
                section_end -= 2
                index += 1


class ResumeStructureExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            ResumeStructureTreeprocessor(md),
            "resume-structure",
            5,
        )


def prepare_pdf_markdown(content: str) -> str:
    """Add PDF-only paragraph boundaries where the resume source is intentionally compact."""
    lines = content.splitlines()
    output: list[str] = []
    in_work_experience = False
    previous_nonempty = ""

    for line in lines:
        stripped = line.strip()
        if stripped == "## WORK EXPERIENCE":
            in_work_experience = True
        elif in_work_experience and stripped.startswith("## "):
            in_work_experience = False

        is_bullet = stripped.startswith("- ")
        if in_work_experience and stripped and previous_nonempty:
            previous_is_bullet = previous_nonempty.startswith("- ")
            if (is_bullet and not previous_is_bullet) or (not is_bullet and not previous_is_bullet):
                if output and output[-1] != "":
                    output.append("")

        output.append(line)
        if stripped:
            previous_nonempty = stripped
        elif in_work_experience:
            previous_nonempty = ""

    return "\n".join(output)


def pdf_settings_css(settings) -> str:
        """Build small PDF-only overrides from the cosmetic configuration."""
        if not settings.enabled:
                raise ValueError("PDF rendering is disabled by resumeFormatting.yml")

        organization_weight = "700" if settings.bold_organization_names else "400"
        role_weight = "700" if settings.bold_role_metadata else "400"
        inline_weight = "700" if settings.bold_inline_content else "400"
        entry_break = "avoid" if settings.keep_work_entries_together else "auto"
        return f"""
@page {{
    margin: {settings.page_margin};
}}

body {{
    color: {settings.body_color};
    font-size: {settings.body_font_size}pt;
}}

h2 {{
    color: {settings.body_color};
    font-size: {settings.section_heading_size}pt;
    border-bottom-color: {settings.rule_color};
}}

.organization {{
    font-size: {settings.organization_name_size}pt;
    font-weight: {organization_weight};
}}

.role-meta {{
    font-size: {settings.role_metadata_size}pt;
    font-weight: {role_weight};
}}

.experience-entry {{
    break-inside: {entry_break};
    page-break-inside: {entry_break};
}}

strong {{
    font-weight: {inline_weight};
}}

hr {{
    border-top-color: {settings.rule_color};
}}
"""


def render_resume(markdown_path: Path, pdf_path: Path, css_path: Path, pdf_settings=None) -> None:
    """Convert one Markdown resume to PDF using the repository stylesheet."""
    if not markdown_path.is_file():
        raise FileNotFoundError(f"Markdown resume not found: {markdown_path}")
    if not css_path.is_file():
        raise FileNotFoundError(f"PDF stylesheet not found: {css_path}")
    if pdf_settings is None:
        from write_resume import PdfSettings

        pdf_settings = PdfSettings()

    content = markdown_path.read_text(encoding="utf-8")
    rendered_html = markdown.markdown(
        prepare_pdf_markdown(content),
        extensions=["extra", "sane_lists", ResumeStructureExtension()],
        output_format="html5",
    )
    document = "<!doctype html><html><head><meta charset=\"utf-8\"></head><body>"
    document += rendered_html
    document += "</body></html>"

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=document, base_url=str(markdown_path.parent)).write_pdf(
        str(pdf_path),
        stylesheets=[CSS(filename=str(css_path)), CSS(string=pdf_settings_css(pdf_settings))],
    )
