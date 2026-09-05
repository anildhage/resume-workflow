# Maintenance Guide

Update the repository in small, factual changes.

## When Your Career Changes

- Employer, title, location, or dates: update `career/resumeSkeleton.md`.
- Recurring strengths: update `career/profileFacts.md`.
- New project: add a note under `career/projects/`.
- Interview story: add a note under `career/firstPersonVoice/`.
- New tool you have actually used: update `career/skills/skills.md`.
- New target role: add or update a file under `career/careerSummary/`.

## Before Generating

- Check that facts are supported.
- Remove stale placeholders from generated content.
- Keep generated output separate from source evidence.
- Review `career/resumeFormatting.yml` before changing presentation.

## After Generating

```bash
.venv/bin/python scripts/validate_resume.py
```

Confirm that every Markdown resume has a matching valid PDF. Add the change to `career/updateLog.md`.

For a quick review, use `career/maintenanceChecklist.md`.
