# Update Log

This file tracks the last refresh time for the repository and the latest material added or updated.

## Purpose

Use this log whenever you add or revise content in the repo so the author always knows what was updated recently and which sections may need attention.

## Rules

- Update this file whenever a significant repo change is made.
- Always include the date and a short description of the change.
- Keep entries brief and factual.
- If a file was updated, note which section or file changed.
- Treat this as the maintenance status sheet for the repository.

## Log

| Date | Area updated | Summary | Last refresh |
|---|---|---|---|
| 2026-09-05 | Public documentation | Replaced the long README with a public tutorial, organized setup and workflow guides under `docs/`, and moved Ubuntu setup documentation into `docs/ubuntu-setup.md`. | 2026-09-05 |
| 2026-09-05 | PDF-only regeneration | Added `career/pdfBuild.yml`, `scripts/build_pdf.py`, and `build-pdf.command` for controlled PDF regeneration from an edited Markdown resume using shared PDF cosmetics and explicit overwrite protection. | 2026-09-05 |
| 2026-09-05 | README workflow documentation | Updated the concise README contract for JD-triggered Markdown/PDF generation, `.venv` execution, PDF cosmetics, and page-break handling. | 2026-09-05 |
| 2026-09-05 | PDF pagination | Added PDF-only work-entry grouping and `keep_work_entries_together` control so organization names, role metadata, and bullets do not split awkwardly across pages when the entry fits. | 2026-09-05 |
| 2026-09-05 | Resume formatting configuration | Expanded `resumeFormatting.yml` comments to document every Markdown and PDF cosmetic control, switch behavior, units, and color formats without changing configuration values. | 2026-09-05 |
| 2026-09-05 | PDF cosmetic controls | Added independent PDF control for inline bold content while retaining separate organization-name and role-metadata emphasis switches. | 2026-09-05 |
| 2026-09-05 | PDF cosmetic plugin | Added YAML-controlled PDF presentation settings for typography, margins, colors, organization-name emphasis, and role metadata emphasis while keeping Markdown controls separate. | 2026-09-05 |
| 2026-09-05 | PDF resume styling | Improved PDF-only hierarchy with larger section headings, bold organization names, and smaller bold role/location/date metadata without changing Markdown generation. | 2026-09-05 |
| 2026-09-05 | Network Growth Analyst resume | Generated a validated, JD-tailored Markdown resume and matching styled PDF emphasizing SQL analysis, metric definition, hypothesis testing, financial modeling, data quality, and cross-functional recommendations. | 2026-09-05 |
| 2026-09-05 | Ubuntu setup documentation | Added `docs/ubuntu-setup.md` with system packages, virtual-environment setup, verification, JD-driven resume generation, PDF output, validation, and troubleshooting instructions. | 2026-09-05 |
| 2026-09-05 | Resume build contract | Audited the full workflow, required matching Markdown/PDF outputs, made PDF validation mandatory, cleaned up partial outputs on conversion failure, and configured VS Code to use `.venv`. | 2026-09-05 |
| 2026-09-05 | Job-description resume workflow | Clarified that a user-provided JD starts the complete agent workflow and produces validated Markdown followed by the matching PDF without requiring manual script inputs. | 2026-09-05 |
| 2026-09-04 | Markdown and PDF output workflow | Added a virtual-environment-based pipeline that validates and saves Markdown under `career/files/md/`, then renders the matching styled PDF under `career/files/pdf/`. | 2026-09-04 |
| 2026-09-04 | Resume output isolation | Restricted target-resume creation to approved source files and made `career/files/` write-only except for final save and filename uniqueness. | 2026-09-04 |
| 2026-09-04 | Data Scientist resume | Added a Data Scientist summary and generated a validated resume emphasizing operational analysis, Python/SQL automation, financial data quality, Azure workflows, reporting, and stakeholder communication. | 2026-09-04 |
| 2026-09-04 | Resume generation workflow | Enforced content-first quality validation, cosmetic-last formatting, canonical Markdown headings, and final presentation checks across the generation contract and scripts. | 2026-09-04 |
| 2026-09-04 | Resume cosmetic workflow | Required final keyword bolding plus supporting action and outcome bolding in work experience and projects, with save-time validation. | 2026-09-04 |
| 2026-09-04 | Resume formatting switch | Added YAML-controlled evidence bolding with per-run yes/no override and headings-only formatting support. | 2026-09-04 |
| 2026-09-04 | Cosmetic plug-in settings | Added configurable keyword, supporting-action, employer, job-title, project-name, and bold-span controls with consistent writer and validator behavior. | 2026-09-04 |
| 2026-09-04 | Resume generation | Added save-time normalization so contact details and selected skills are rendered consistently across generated resumes. | 2026-09-04 |
| 2026-09-04 | Resume formatting | Standardized the skeleton and generation guidance for a two-line contact header and pipe-separated one-line skills section. | 2026-09-04 |
| 2026-09-04 | Documentation and summaries | Documented the profile-maintenance workflow in README, aligned update guides and checklist, and refreshed role summaries to the skeleton-derived 8+ years claim. | 2026-09-04 |
| 2026-09-04 | Profile consistency | Added stable profile facts, skeleton-based experience calculation, validator enforcement, and refreshed generated experience claims to 8+ years. | 2026-09-04 |
| 2026-09-04 | Generated resume | Added SQL-focused Sales Database Associate Analyst resume emphasizing SQL Server integration, data cleansing, auditing, and reporting controls. | 2026-09-04 |
| 2026-09-03 | Repo setup | Added deterministic resume-generation workflow, validation scripts, README guidance, source index, source template, and maintainer update workflow. | 2026-09-03 |

## Recommended usage

Whenever you add or revise a project, role summary, skills, or first-person evidence file, add a new row with:

- the current date
- the file area or section updated
- a one-line summary of the change
- the last refresh timestamp

Example:

| 2026-09-15 | Career summary | Updated DataEngineer summary to include Azure migration and ETL modernization work. | 2026-09-15 |
