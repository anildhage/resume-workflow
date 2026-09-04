# Keeping the Repo Current

This file explains how to keep the repository accurate as your career grows and your experience changes.

## Goal

The repo should act as a living source of truth for future resume generation. As you gain work experience, new projects, new responsibilities, and new skills, the evidence files should be updated in a structured way so the local LLM can stay current and produce better, more accurate resumes.

## Core rule

Do not rewrite the fixed resume structure unless the underlying factual content truly changes.

Keep these files stable unless they are intentionally changing:

- `resumeSkeleton.md`
- `targetResume.md`

Update the dynamic evidence files as your professional experience grows.

## Update workflow

When you add new work experience, use this order:

1. Review the existing summaries in `career/careerSummary/` and synthesize the role narrative instead of copying one file verbatim.
2. Add or update the role summary in `career/careerSummary/` if the new experience changes your target role narrative or if the target role does not yet have a summary.
3. Update `career/profileFacts.md` when your recurring professional identity, core strengths, or cross-role capabilities change.
4. Update `career/skills/skills.md` when new tools, platforms, or capabilities become relevant.
5. Add a new project note in `career/projects/` for a substantial project, initiative, or workstream.
6. Add or expand a supporting narrative note in `career/firstPersonVoice/` when you want to preserve interview-ready context.
7. Keep the resume skeleton unchanged unless the fixed factual details changed. Its dated roles determine the experience claim.
8. Update `career/updateLog.md`.
9. Validate generated resumes using the scripts in `scripts/`.

## Summary synthesis rule

Do not copy a single summary file directly into a generated resume.

Instead:

- read all available summary files in `career/careerSummary/`
- identify the strongest themes relevant to the target role
- create a tailored, synthesized summary grounded in actual experience
- add a new summary file when the target role is new or not yet represented well enough
- use the summary as a generated artifact, not as a pasted duplicate

## What to update when

### If you change employers or roles

- Update the fixed facts only if the core resume skeleton needs a new employer, role title, location, or date.
- Add a new project or narrative note if the work added new responsibilities, business context, or technologies.
- Refresh the relevant role summary file if the new experience significantly shifts your target positioning.

### If you complete a new project

- Create a new project file in `career/projects/`.
- Use the shared template in `career/sourceNoteTemplate.md`.
- Include the business context, problem, responsibilities, tools, and outcomes.
- Keep the description fact-based and concise.

### If you learn new tools or technologies

- Add the relevant items to `career/skills/skills.md`.
- Only add tools that you have actually used in a professional or demonstrable context.
- Avoid adding speculative or aspirational tools just because they are trending.

### If you want a new resume angle

- Update the summary in the relevant file under `career/careerSummary/`.
- Do not manually preserve an old experience statement. Calculate it from the dated professional roles in `career/resumeSkeleton.md`.
- Use only evidence already present in the repo to support the role positioning.

## Additions to keep the repo maintainable

Use this pattern when adding new material:

- New project file under `career/projects/`
- New first-person narrative under `career/firstPersonVoice/` when needed
- New role summary under `career/careerSummary/` if relevant to a target role
- New skill entries in `career/skills/skills.md`
- Optional new generated output under `career/files/` after a successful resume generation

## Naming and file conventions

Follow these conventions consistently:

- Project files: use clear descriptive names
- Role summary files: use the target-role naming convention, such as `dataEngineer.md`
- Output resumes: follow the pattern from `targetResume.md` and the validation scripts
- Keep the file names readable and search-friendly

## Validation before finalizing edits

After any update, check the following:

1. The structure still aligns with the resume skeleton.
2. No placeholders remain in generated output.
3. New facts are grounded in actual evidence files.
4. Skills, projects, and summaries are still consistent with your work history.
5. Resume output still follows the repo naming and validation rules.

## Suggested maintainer habits

- Add new facts as new content, not by overwriting old facts unless they are demonstrably wrong.
- Keep evidence concise, specific, and business-relevant.
- Prefer a maintained evidence set over a large narrative dump.
- Treat the repo as a source-of-truth system, not as a long-form journal.

## Practical note

The repository is most reliable when the author updates it in small, structured increments rather than waiting for a large rewrite. Incremental updates keep the LLM output more consistent and make it easier to confirm that the output is still truthful.
