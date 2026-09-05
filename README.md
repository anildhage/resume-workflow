# Career Resume Generation Repository

This repository is designed to support a local LLM or agent that generates role-targeted resumes from a fixed resume skeleton and curated career-source material.

## Objective

The agent should read the job description or target role, select the most relevant source files, and generate a validated Markdown resume plus matching PDF grounded in verified career facts.

## Repository purpose

The repo separates fixed facts from dynamic content:

- Fixed structure and constant experience details live in `career/resumeSkeleton.md`
- Stable cross-role professional identity and recurring capabilities live in `career/profileFacts.md`
- Role-specific summaries live in `career/careerSummary/`
- Skills live in `career/skills/skills.md`
- Project evidence lives in `career/projects/`
- First-person narrative evidence lives in `career/firstPersonVoice/`
- Output resumes are written as Markdown to `career/files/md/` and PDFs to `career/files/pdf/`

## Source priority order

When generating a resume, the model must follow this priority order:

1. `career/resumeSkeleton.md` — authoritative fixed content and resume layout
2. `career/profileFacts.md` — stable professional identity and recurring capabilities
3. `career/targetResume.md` — generation rules and constraints
4. `career/careerSummary/*.md` — summary knowledge base; read broadly and synthesize a tailored summary for the target role
5. `career/skills/skills.md` — skills selection
6. `career/projects/*.md` — project evidence and achievements
7. `career/firstPersonVoice/*.md` — detailed narrative and operational context
8. `career/files/md/` and `career/files/pdf/` — output destinations only; never as input sources

### Output isolation rule

During target-resume creation, never read, list, search, index, enter, or otherwise scan `career/files/md/` or `career/files/pdf/` for source material. Treat them as write-only output directories. Resume content, facts, summaries, skills, project selections, experience calculations, and validation decisions must come exclusively from approved source files outside `career/files/`.

## Summary generation rule

The model must not directly copy a single summary file into the final resume.

Instead, it must:

- read the full set of role summaries in `career/careerSummary/`
- identify the common strengths and themes relevant to the target role
- synthesize a new summary tailored to the job being targeted
- use an existing summary only as context, not as a verbatim block of text
- create a new summary file in `career/careerSummary/` when the target role has no suitable existing summary

### Required workflow

When a job description is provided, the user-facing action is simply to ask for a resume tailored to that job description. The agent extracts the role requirements, selects only supported evidence, drafts the Markdown resume, and invokes the writer. The writer then validates and saves the Markdown before converting it to PDF. The user does not need to supply a `--content` argument or run the scripts manually.

1. Read `career/targetResume.md` and identify the target role.
2. Read `career/resumeSkeleton.md` and preserve all constant sections exactly.
3. Read `career/profileFacts.md` for stable cross-role facts and recurring capabilities.
4. Calculate the experience statement from the dated professional roles in `career/resumeSkeleton.md`.
5. Choose the matching summary from `career/careerSummary/`.
6. Select relevant skills from `career/skills/skills.md`.
7. Build the Societe Generale position bullets by synthesizing project files, first-person source files, and skills.
8. Select the most relevant project(s) from `career/projects/`.
9. Assemble an unformatted content draft and review it for factual accuracy, completeness, role alignment, and placeholder removal.
10. Apply final Markdown headings and spacing only after the content gate passes, then apply strategic keyword and supporting-evidence bolding as the final cosmetic pass.
11. Save a new Markdown resume in `career/files/md/` using the required filename pattern. Do not inspect the output directory for source material during this process.
12. After the validated Markdown file is written, render its PDF counterpart into `career/files/pdf/`.
13. Run `.venv/bin/python scripts/validate_resume.py` before delivering the resume.

### Resume formatting

Generated resumes must use the standard Markdown header and skills layout:

```markdown
# Anil Dhage
Montreal, Quebec  |  +1 514 235 8388  |  i.am.dhage@gmail.com  |  linkedin.com/in/anil-dhage
---
## SKILLS
SQL Server  |  Advanced querying  |  Data analysis
```

Keep the contact details on one line separated by `  |  `, keep selected skills on one pipe-separated line without bullet markers, and put each section heading on its own line above its content.

Formatting is a final presentation step. It must not change the factual content selected during the content-quality stage.

After the content gate passes, bold important target-role keywords in the summary and skills sections. Then bold the supporting action, responsibility, or outcome in work-experience and project bullets that demonstrates how those keywords were used. Final validation requires strategic bolding in both the keyword sections and supporting evidence sections.

### Cosmetic mode switch

Set the switches in `career/resumeFormatting.yml`. `evidence_bolding: true` enables the cosmetic plug-in; `false` produces a clean resume with only Markdown headings. The category switches control keyword, supporting-action, employer, title, and project emphasis. Override the master setting for one run with `.venv/bin/python scripts/write_resume.py --role "Business Analyst" --bolding yes` or `--bolding no`.

## Non-negotiable rules

The model must not:

- invent employers, dates, technologies, metrics, or details not supported by the source files
- change the permanent content in the skeleton
- leave placeholder text such as `- to be updated`
- use first-person pronouns in the final resume language unless the skeleton or output format explicitly requires them
- overwrite an existing generated resume
- create a resume file with the wrong naming convention

## Output contract

Every generated resume must be a new `.md` file under `career/files/md/`, followed by a same-name `.pdf` file under `career/files/pdf/`.

Use the repository virtual environment for deterministic generation:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/write_resume.py --role "Data Scientist" --content "<generated Markdown draft>"
```

The writer completes Markdown content and presentation validation before starting PDF conversion. Markdown bold spans such as `**SQL**` are rendered as bold PDF text through `career/resume.css`.

The same `career/resumeFormatting.yml` file contains a separate `pdf:` section for PDF-only presentation controls. These settings do not change Markdown generation. They control PDF enablement, inline Markdown emphasis, organization-name emphasis, role/location/date emphasis, heading sizes, body size, margins, and colors. The renderer applies them as overrides to `career/resume.css`.

Set `pdf.keep_work_entries_together: true` to keep each organization, role/date line, and bullet list together when it fits on one page. The renderer also adds PDF-only structure for correct headings, lists, and page breaks; the source Markdown remains unchanged.

### Regenerate One PDF

To regenerate a PDF after editing an existing Markdown resume, edit `career/pdfBuild.yml`:

```yaml
pdf_build:
	markdown_file: NetworkGrowthAnalyst-AnilDhage-1.md
	pdf_file: NetworkGrowthAnalyst-AnilDhage-1.pdf
	overwrite: false
```

Then run:

```bash
./build-pdf.command
```

Run `.venv/bin/python scripts/validate_resume.py` after editing and after regeneration. The command reads the Markdown from `career/files/md/`, writes the PDF to `career/files/pdf/`, and reuses the `pdf:` settings from `career/resumeFormatting.yml`. Existing PDFs are protected unless `overwrite: true` is set intentionally.

Required pattern:

`RoleName-FirstLastName-{incrementNumberBasedOnFileCountInThisFolder}.md`

The writer uses the next unused numeric suffix in `career/files/md/`; the PDF uses the same filename stem.

For this profile:

- `FirstLastName = AnilDhage`
- role names must be converted to PascalCase without spaces or punctuation

Example:

- `BusinessAnalyst-AnilDhage-1.md`
- `DataEngineer-AnilDhage-2.md`

## Validation checklist before saving

Before writing the file, the model must confirm:

1. It started from `career/resumeSkeleton.md`.
2. Fixed sections were preserved.
3. All placeholders were replaced.
4. The career summary came from `career/careerSummary/`.
5. The skills came from `career/skills/skills.md`.
6. SG bullets were grounded in `career/projects/` and `career/firstPersonVoice/`.
7. Projects came from `career/projects/`.
8. The experience statement matches the value calculated from `career/resumeSkeleton.md` using the current date.
9. Output includes validated Markdown in `career/files/md/` and a matching PDF in `career/files/pdf/`.
10. File is new and does not overwrite an existing resume.
11. Content quality was checked before cosmetic formatting was applied.
12. Final formatting did not introduce placeholders or alter fixed facts.
13. Final cosmetic formatting includes keyword emphasis and supporting evidence emphasis in work experience and projects.
14. PDF rendering keeps work entries together when the PDF setting is enabled.

## Determinism guidance

To reduce drift and make the model more consistent:

- read the source files in the prescribed order
- prefer the most relevant files over everything else
- keep output tightly aligned to evidence
- prefer concise, ATS-friendly wording over narrative text
- validate against the source contract before writing the final file

## Keeping the repo current

This repository is intended to be maintained over time as your career grows. The key is to update the right files in the right places, without disturbing the fixed resume structure.

### When to update the repo

Update the repo whenever you:

- gain a new role or employer
- complete a new project or major initiative
- learn new technologies or tools that are relevant to your work
- expand your responsibilities in an existing role
- want to improve the resume angle for a new target role

### Where to update each type of information

- `career/resumeSkeleton.md` — only change when the fixed professional facts truly change
- `career/profileFacts.md` — update when your recurring professional identity, core strengths, or cross-role capabilities change; do not duplicate every project here
- `career/targetResume.md` — only change if the generation rules or file contract change
- `career/careerSummary/` — update the relevant role summary when your experience or positioning changes
- `career/skills/skills.md` — add or refine skills as they become part of your professional toolkit
- `career/projects/` — create a new project note for each significant initiative or workstream
- `career/firstPersonVoice/` — add or expand narrative evidence that supports interviews or resume bullets
- `career/files/md/` and `career/files/pdf/` — generated output only; do not use as input sources

### Recommended update workflow

1. Update `career/resumeSkeleton.md` when an employer, title, location, date, education, or certification changes. This is the authority for fixed facts and experience calculation.
2. Update `career/profileFacts.md` when your broad professional identity or recurring strengths change. Keep it concise and cross-role; do not put job-specific bullets here.
3. Add a new project or workstream in `career/projects/` if the work is substantial.
4. Add supporting narrative context in `career/firstPersonVoice/` if the work needs interview-ready detail.
5. Update `career/skills/skills.md` with new tools or competencies only after you have actually used them.
6. Update relevant files in `career/careerSummary/` when your target positioning changes. Do not hard-code an old experience number; use the skeleton-derived value.
7. Add the change to `career/updateLog.md`.
8. Generate and validate the output using the scripts in `scripts/` before saving a final resume.

### What to update over time

| Change | Update first | Also review |
|---|---|---|
| New employer, title, location, or employment dates | `resumeSkeleton.md` | `profileFacts.md`, summaries, experience claim, update log |
| New project or major workstream | `projects/` | `firstPersonVoice/`, skills, relevant summaries, update log |
| New tool or technical capability | `skills/skills.md` | project evidence, `profileFacts.md`, relevant summaries, update log |
| Broader professional strength or career direction | `profileFacts.md` | relevant summaries, skills, update log |
| New target job application | target-specific summary or new summary file | skills, projects, generated resume, validation |

The generated resume files under `career/files/md/` and `career/files/pdf/` are outputs, not source material. Normally, do not edit them as the primary fix. Update the source files first, then generate a new resume.

### Maintainer habits

- Prefer adding new evidence over rewriting old evidence unless the old fact is no longer true.
- Keep each file fact-based and concise.
- Do not invent technologies, dates, metrics, or responsibilities.
- Treat the repo as a living evidence base for future generation, not as a loose journal.

### Update log requirement

Whenever any substantive change is made to the repository, the author must update `career/updateLog.md`.

The update log is the maintenance status sheet for the repo and should record:

- the date of the update
- the area or file category updated
- a short summary of what changed
- the last refresh timestamp

This keeps the repository easy to maintain and makes it easy to see what was last refreshed and what may need attention next.

> Rule: if you add details, revise a summary, add a project, update skills, or change the evidence material, you should also log it in `career/updateLog.md`.

### Quick maintenance checklist

When you refresh the repo, use `career/maintenanceChecklist.md` as the fast review guide before finalizing updates.

The checklist covers:

- review of new experience or role changes
- project evidence updates
- narrative evidence updates
- skill updates
- role summary checks
- update log updates
- final validation

## Directory snapshot

- `career/resumeSkeleton.md` — fixed resume skeleton
- `career/profileFacts.md` — stable cross-role profile facts
- `career/targetResume.md` — generation rules
- `career/careerSummary/` — role-specific summary options
- `career/skills/skills.md` — reusable skill taxonomy
- `career/projects/` — project evidence
- `career/firstPersonVoice/` — narrative context
- `career/files/md/` — generated Markdown output only; never scan or read during resume creation
- `career/files/pdf/` — generated PDF output corresponding to validated Markdown

This repo is intentionally designed to be deterministic: fixed facts stay fixed, dynamic content is selected from approved evidence, and final output remains faithful to the source material.
