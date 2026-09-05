# Repository Map

This repository has two layers:

- `career/` contains resume facts, evidence, instructions, and styling.
- `scripts/` validates content, calculates experience, writes Markdown, and renders PDFs.

## Files You Usually Change

| Need | File or folder |
|---|---|
| Name and contact details | `career/resumeSkeleton.md` |
| Fixed employers, titles, dates, education, certifications | `career/resumeSkeleton.md` |
| Professional identity and recurring strengths | `career/profileFacts.md` |
| Target-role generation rules | `career/targetResume.md` |
| Role summaries | `career/careerSummary/` |
| Skills | `career/skills/skills.md` |
| Project evidence | `career/projects/` |
| Interview and narrative evidence | `career/firstPersonVoice/` |
| PDF appearance | `career/resume.css` and `career/resumeFormatting.yml` |
| Change history | `career/updateLog.md` |

## Files You Normally Do Not Change

- `scripts/` unless you are changing the generator itself.
- `career/files/md/` and `career/files/pdf/`; these are generated outputs.
- `career/pdfBuild.yml`, unless regenerating one existing PDF.

## Source Priority

When preparing a resume, use sources in this order:

1. `resumeSkeleton.md`
2. `profileFacts.md`
3. `targetResume.md`
4. `careerSummary/`
5. `skills/skills.md`
6. `projects/`
7. `firstPersonVoice/`

Generated files are outputs only. Do not use them as source material.
