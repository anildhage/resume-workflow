# LLM Source Index

This file exists to reduce drift and make resume generation more deterministic for local LLMs.

## Authoritative files

### Fixed resume structure
- `resumeSkeleton.md` — source of all permanent content and headings

### Stable profile facts
- `profileFacts.md` — cross-role professional identity, recurring capabilities, and constant resume rules

### Generation rules
- `targetResume.md` — the exact instruction contract for generating a target-role resume

### Role summary options
- `careerSummary/businessAnalyst.md`
- `careerSummary/dataAnalyst.md`
- `careerSummary/dataEngineer.md`
- `careerSummary/dataAndAIEngineer.md`
- `careerSummary/financeProductionSupportAnalyst.md`

### Skills inventory
- `skills/skills.md`

### Project evidence
- `projects/pythonBasedEtlDataTransformationApplication.md`
- `projects/frY15AndFr2052aRegulatoryReporting.md`
- `projects/profitAndLossReporting.md`
- `projects/fastApiChangeManagementProcess.md`
- `projects/automatedDataCleanupApplication.md`

### Narrative evidence
- `firstPersonVoice/responsibilitiesAtSg.md`
- `firstPersonVoice/platformAndTools.md`
- `firstPersonVoice/regulatoryReporting.md`
- `firstPersonVoice/pmpiReporting.md`
- `firstPersonVoice/dataGovernance.md`
- `firstPersonVoice/azureMigration.md`
- `firstPersonVoice/interviewStories.md`
- `firstPersonVoice/resumeAndInterviewPrep.md`

### Output location
- `files/` — generated resume outputs live here

## Deterministic operating rules

1. Read `targetResume.md` first.
2. Read `resumeSkeleton.md` second.
3. Select only one matching career summary file.
4. Select relevant skills from `skills/skills.md` only.
5. Build SG bullets from project and first-person evidence only.
6. Never invent unsupported claims.
7. Calculate the experience statement from dated professional roles in `resumeSkeleton.md`.
8. Preserve all fixed skeleton content without rewriting it.
9. Replace all placeholders before final output.
10. Assemble and quality-check an unformatted content draft before presentation formatting.
11. Apply Markdown headings and spacing only after the content gate passes.
12. As the final cosmetic pass, bold supported target-role keywords in the summary and skills, then bold the supporting actions or outcomes in work-experience and project bullets.
13. Save as a new file in `files/` using the exact naming convention.

## Validation checklist

The generation process is successful only if all of the following are true:

- Base file is `resumeSkeleton.md`
- Target role is matched to one summary file
- Skills are selected from `skills/skills.md`
- Projects are selected from `projects/`
- SG experience bullets are grounded in project + first-person evidence
- Final output is Markdown
- Final file is unique and not overwriting anything
- Filename uses `RoleName-FirstLastName-{n}.md`
- Summary and skills contain strategic keyword bolding
- Work experience and projects contain bold supporting evidence, not just repeated keywords

## Common drift risks to avoid

- mixing project evidence with unrelated notes
- editing fixed skeleton fields that are intentionally constant
- using unsupported technologies or unverified metrics
- generating project or role content from memory instead of source files
- allowing placeholder text to remain in the output
- copying a stale experience number from an older generated resume
- creating output files without checking the existing count in `files/`
- applying cosmetic formatting before content quality has been checked

## Suggested agent behavior

When a local model processes this repo, it should operate in a strict evidence-first loop:

- read source
- select relevant facts
- synthesize concise resume content
- validate the unformatted content against the skeleton and rules
- apply final presentation formatting, including keyword and supporting-evidence bolding
- validate the formatted output
- write output
- stop once validation passes

This structure is intentionally concise and repeatable so different LLMs follow the same path and produce more consistent results.
