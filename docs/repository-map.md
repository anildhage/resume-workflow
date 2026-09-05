# Repository Map

This repository has four layers:

- `career/` contains resume facts, evidence, instructions, and styling.
- `scripts/` validates content, calculates experience, writes Markdown, and renders PDFs.
- `templates/` contains safe starter files for a new local profile.
- `profiles/` contains private, Git-ignored profile data.

## Files You Usually Change

| Need | File or folder |
|---|---|
| Name and contact details | `profiles/local/profile.yml` and `profiles/local/resumeSkeleton.md` |
| Fixed employers, titles, dates, education, certifications | `profiles/local/resumeSkeleton.md` |
| Professional identity and recurring strengths | `profiles/local/profileFacts.md` |
| Target-role generation rules | `profiles/local/targetResume.md` |
| Role summaries | `profiles/local/careerSummary/` |
| Skills | `profiles/local/skills/skills.md` |
| Project evidence | `profiles/local/projects/` |
| Interview and narrative evidence | `profiles/local/firstPersonVoice/` |
| PDF appearance | `career/resume.css` and `career/resumeFormatting.yml` |
| Change history | `career/updateLog.md` |

## Files You Normally Do Not Change

- `templates/` only when improving starter content.
- `scripts/` unless you are changing the generator itself.
- `career/` shared formatting and maintenance files, unless changing the workflow.
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
