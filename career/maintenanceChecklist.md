# Maintenance Checklist

Use this quick checklist whenever you refresh the repo with new experience, skills, or project work.

## Quick refresh routine

### Output isolation
- Treat `career/files/md/` and `career/files/pdf/` as write-only output during target-resume creation.
- Do not read, list, search, index, enter, or scan them for source material or drafting decisions.
- Access them only for final output creation, matching-file checks, and validation.

### 1. Review new experience
- Did you gain a new role, employer, or major responsibility?
- Do you need to update the fixed resume skeleton or just the evidence files under `profiles/local/`?
- If dates changed, let the skeleton-based calculator determine the experience claim.

### 2. Review stable profile facts
- Did your recurring professional identity, core strengths, or cross-role capabilities change?
- If yes, update `profiles/local/profileFacts.md` without duplicating project-specific details.

### 3. Update project evidence
- Have you completed a new project or meaningful workstream?
- If yes, create or update a project file under `profiles/local/projects/`.
- Use the shared template in `career/sourceNoteTemplate.md`.

### 4. Update narrative evidence
- Do you need new interview-ready examples or supporting context?
- If yes, add or update a note under `profiles/local/firstPersonVoice/`.

### 5. Update skills
- Did you learn new tools, methodologies, or platforms?
- If yes, add them to `profiles/local/skills/skills.md` only if they are directly relevant and actually used.

### 6. Update role summary
- Does the target-role summary still match your current experience and positioning?
- If not, update the relevant file in `profiles/local/careerSummary/`.

### 7. Update the log
- Add a new row to `career/updateLog.md` with the date, area, summary, and last refresh timestamp.

### 8. Validate the repo
- Review resume content for factual accuracy, role alignment, completeness, and evidence support before reviewing formatting.
- Apply cosmetic formatting only after the content review passes: bold target keywords in the summary and skills, then bold the supporting actions or outcomes in work-experience and project bullets.
- Confirm the final resume has strategic bolding in both keyword sections and supporting evidence sections; do not bold entire bullets or unsupported claims.
- Check `career/resumeFormatting.yml` before generation: use `evidence_bolding: true` for keyword/evidence emphasis or `false` for headings-only output. Use the writer’s `--bolding yes|no` option for a one-run override.
- Run `.venv/bin/python scripts/validate_resume.py --profile profiles/local`.
- If generating a new resume, use the `--profile profiles/local` option with the filename and writer scripts.
- Any semantic request to build or create a resume from JD or job-role details must produce both a validated Markdown file in `career/files/md/` and its matching PDF in `career/files/pdf/`.
- Confirm the matching PDF exists and begins with the PDF signature before delivery.

## Optional final check

Before closing the update session, confirm:

- no placeholders remain in generated output
- the repo still reflects only factual and supported experience
- generated experience claims match the dated roles in `resumeSkeleton.md`
- the update log is current
- the changelog or evidence files match your latest work history
