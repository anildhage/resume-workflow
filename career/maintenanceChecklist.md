# Maintenance Checklist

Use this quick checklist whenever you refresh the repo with new experience, skills, or project work.

## Quick refresh routine

### 1. Review new experience
- Did you gain a new role, employer, or major responsibility?
- Do you need to update the fixed resume skeleton or just the evidence files?

### 2. Update project evidence
- Have you completed a new project or meaningful workstream?
- If yes, create or update a project file under `career/projects/`.
- Use the shared template in `career/sourceNoteTemplate.md`.

### 3. Update narrative evidence
- Do you need new interview-ready examples or supporting context?
- If yes, add or update a note under `career/firstPersonVoice/`.

### 4. Update skills
- Did you learn new tools, methodologies, or platforms?
- If yes, add them to `career/skills/skills.md` only if they are directly relevant and actually used.

### 5. Update role summary
- Does the target-role summary still match your current experience and positioning?
- If not, update the relevant file in `career/careerSummary/`.

### 6. Update the log
- Add a new row to `career/updateLog.md` with the date, area, summary, and last refresh timestamp.

### 7. Validate the repo
- Run the validation script in `scripts/validate_resume.py`.
- If generating a new resume, use `scripts/generate_resume_filename.py` and `scripts/write_resume.py`.

## Optional final check

Before closing the update session, confirm:

- no placeholders remain in generated output
- the repo still reflects only factual and supported experience
- the update log is current
- the changelog or evidence files match your latest work history
