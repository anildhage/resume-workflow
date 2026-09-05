# Resume Workflow

## Normal Workflow

1. Add or paste a job description to your agent workflow.
2. Identify the target role and important requirements.
3. Read the skeleton and approved evidence files.
4. Draft a role-specific summary, skills line, work bullets, and project selection.
5. Check factual accuracy and remove all placeholders.
6. Apply Markdown headings and strategic bolding.
7. Run `scripts/write_resume.py`.
8. Confirm that both Markdown and PDF files were created.
9. Run the validator.

The normal user-facing action is to ask an agent to create a resume from a job description. The agent should perform the source selection and invoke the writer after drafting.

## Manual Test Command

The writer accepts a complete Markdown draft:

```bash
.venv/bin/python scripts/write_resume.py \
  --role "Data Scientist" \
  --content "<generated Markdown draft>"
```

The draft must contain all required sections and must satisfy the profile's fixed facts and formatting rules.

## Validate Outputs

```bash
.venv/bin/python scripts/validate_resume.py
```

Validation checks filenames, required sections, placeholder removal, the experience claim, bolding rules, matching PDFs, and PDF validity.

## Calculate Experience

```bash
.venv/bin/python scripts/calculate_experience.py
```

The calculation uses dated roles in `career/resumeSkeleton.md` and the current date. To test a historical date:

```bash
.venv/bin/python scripts/calculate_experience.py --as-of 2026-01-01
```

## Formatting

Markdown and PDF cosmetic settings live in `career/resumeFormatting.yml`. The PDF stylesheet is `career/resume.css`.

- Set `evidence_bolding: true` for keyword and evidence emphasis.
- Set it to `false` for headings-only Markdown.
- Use `--bolding yes` or `--bolding no` for a single run.

Generated files belong in `career/files/md/` and `career/files/pdf/`. Do not edit generated PDFs as the primary fix; update source files and generate again.
