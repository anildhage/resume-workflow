# Career Resume Generation Repository

This repository is designed to support a local LLM or agent that generates role-targeted resumes from a fixed resume skeleton and curated career-source material.

## Objective

The agent should read the target role, select the most relevant source files, and generate a new Markdown resume that remains grounded in verified career facts and does not invent details.

## Repository purpose

The repo separates fixed facts from dynamic content:

- Fixed structure and constant experience details live in `career/resumeSkeleton.md`
- Role-specific summaries live in `career/careerSummary/`
- Skills live in `career/skills/skills.md`
- Project evidence lives in `career/projects/`
- First-person narrative evidence lives in `career/firstPersonVoice/`
- Output resumes are written to `career/files/`

## Source priority order

When generating a resume, the model must follow this priority order:

1. `career/resumeSkeleton.md` — authoritative fixed content and resume layout
2. `career/targetResume.md` — generation rules and constraints
3. `career/careerSummary/*.md` — role-specific experience summary
4. `career/skills/skills.md` — skills selection
5. `career/projects/*.md` — project evidence and achievements
6. `career/firstPersonVoice/*.md` — detailed narrative and operational context
7. `career/files/` — output destination only; never as an input source

## Required workflow

1. Read `career/targetResume.md` and identify the target role.
2. Read `career/resumeSkeleton.md` and preserve all constant sections exactly.
3. Choose the matching summary from `career/careerSummary/`.
4. Select relevant skills from `career/skills/skills.md`.
5. Build the Societe Generale position bullets by synthesizing project files, first-person source files, and skills.
6. Select the most relevant project(s) from `career/projects/`.
7. Generate a new Markdown resume in `career/files/` using the required filename pattern.
8. Run final validation before saving.

## Non-negotiable rules

The model must not:

- invent employers, dates, technologies, metrics, or details not supported by the source files
- change the permanent content in the skeleton
- leave placeholder text such as `- to be updated`
- use first-person pronouns in the final resume language unless the skeleton or output format explicitly requires them
- overwrite an existing generated resume
- create a resume file with the wrong naming convention

## Output contract

Every generated resume must be a new `.md` file under `career/files/`.

Required pattern:

`RoleName-FirstLastName-{incrementNumberBasedOnFileCountInThisFolder}.md`

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
8. The experience statement remains `7+ years`.
9. Output is Markdown.
10. File is new and does not overwrite an existing resume.

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
- `career/targetResume.md` — only change if the generation rules or file contract change
- `career/careerSummary/` — update the relevant role summary when your experience or positioning changes
- `career/skills/skills.md` — add or refine skills as they become part of your professional toolkit
- `career/projects/` — create a new project note for each significant initiative or workstream
- `career/firstPersonVoice/` — add or expand narrative evidence that supports interviews or resume bullets
- `career/files/` — generated output only; do not use as an input source

### Recommended update workflow

1. Add a new project or workstream in `career/projects/` if the work is substantial.
2. Add supporting narrative context in `career/firstPersonVoice/` if the work needs interview-ready detail.
3. Update the relevant role summary in `career/careerSummary/` if the experience changes your target positioning.
4. Update `career/skills/skills.md` with any new tools or competencies that are now part of your work.
5. Keep the fixed skeleton stable unless the underlying factual details truly changed.
6. Generate and validate the output using the scripts in `scripts/` before saving a final resume.

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
- `career/targetResume.md` — generation rules
- `career/careerSummary/` — role-specific summary options
- `career/skills/skills.md` — reusable skill taxonomy
- `career/projects/` — project evidence
- `career/firstPersonVoice/` — narrative context
- `career/files/` — generated output files

This repo is intentionally designed to be deterministic: fixed facts stay fixed, dynamic content is selected from approved evidence, and final output remains faithful to the source material.
