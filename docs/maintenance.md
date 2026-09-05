# Maintenance Guide

Update the repository in small, factual changes.

## When Your Career Changes

- Employer, title, location, or dates: update `profiles/local/resumeSkeleton.md`.
- Recurring strengths: update `profiles/local/profileFacts.md`.
- New project: add a note under `profiles/local/projects/`.
- Interview story: add a note under `profiles/local/firstPersonVoice/`.
- New tool you have actually used: update `profiles/local/skills/skills.md`.
- New target role: add or update a file under `profiles/local/careerSummary/`.

## Before Generating

- Check that facts are supported.
- Remove stale placeholders from generated content.
- Keep generated output separate from source evidence.
- Review `career/resumeFormatting.yml` before changing presentation.

## After Generating

```bash
.venv/bin/python scripts/validate_resume.py --profile profiles/local
```

Confirm that every Markdown resume has a matching valid PDF. Add the change to `career/updateLog.md`.

For a quick review, use `career/maintenanceChecklist.md`.
