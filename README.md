# Resume Workflow

Build role-targeted Markdown resumes and matching PDFs from a trusted set of career facts, projects, skills, and work stories.

The repository currently contains Anil Dhage's profile. That is the working profile, not a requirement of the tool. To use a public copy for yourself, replace the profile content described below before generating a resume.

## What This Repo Does

The workflow:

1. Reads your fixed resume facts and supporting evidence.
2. Uses a job description or target role to select relevant content.
3. Creates a new, validated Markdown resume.
4. Renders a matching PDF.
5. Checks that the output is complete, factual, and correctly formatted.

Generated resumes are written to `career/files/md/` and `career/files/pdf/`. Those folders are outputs only and are ignored by Git.

## Quick Start

Choose the setup guide for your operating system:

- [macOS setup](docs/macos-setup.md)
- [Ubuntu setup](docs/ubuntu-setup.md)
- [Windows setup](docs/windows-setup.md)

After installation, open the repository root in VS Code or a terminal. The root is the folder containing `README.md`, `career/`, and `scripts/`.

## Make It Your Own

The current profile lives in `career/`. Keep the structure, and replace the content with your own information.

### 1. Fixed Resume Facts

Edit `career/resumeSkeleton.md` first. Replace your:

- name and contact details
- employers, titles, locations, and employment dates
- education
- certifications

Keep the section names and general structure. The experience calculator reads dated work entries from this file.

### 2. Stable Profile Facts

Edit `career/profileFacts.md` with your professional identity, recurring strengths, and capabilities. Keep it concise and avoid duplicating every project.

### 3. Evidence Library

Add your supporting material to the existing folders:

- `career/careerSummary/` for target-role summaries
- `career/skills/skills.md` for skills you have actually used
- `career/projects/` for substantial projects and workstreams
- `career/firstPersonVoice/` for interview stories and detailed context

Use `career/sourceNoteTemplate.md` when creating a new evidence note. Do not add unsupported tools, metrics, responsibilities, or achievements.

### 4. Generation Rules

Edit `career/targetResume.md` so its name, contact examples, filename examples, and instructions describe your profile. It should require the generator to preserve your fixed facts, use only approved evidence, calculate experience from the skeleton, replace placeholders, and produce both Markdown and PDF output.

### 5. Record Changes

Add a short entry to `career/updateLog.md` whenever you update your profile, evidence, or workflow.

For a visual map of the repository, see [docs/repository-map.md](docs/repository-map.md). For the full customization checklist, see [docs/profile-customization.md](docs/profile-customization.md).

## Generate a Resume

The intended workflow is to give your agent a job description and ask for a tailored resume. It should read the source material, draft the resume, invoke the writer, and confirm both output files.

For a manual test, provide a complete Markdown draft:

```bash
.venv/bin/python scripts/write_resume.py \
  --role "Data Scientist" \
  --content "<generated Markdown draft>"
```

Then validate the generated Markdown/PDF pair:

```bash
.venv/bin/python scripts/validate_resume.py
```

The writer does not overwrite an existing output. The normal output filename follows this pattern:

```text
RoleName-FirstLastName-Number.md
RoleName-FirstLastName-Number.pdf
```

For more commands, see [docs/resume-workflow.md](docs/resume-workflow.md).

## Where to Change Things

| What you want to change | Where to change it |
|---|---|
| Name, contact details, dates, education, certifications | `career/resumeSkeleton.md` |
| Professional identity and recurring strengths | `career/profileFacts.md` |
| Resume-generation rules | `career/targetResume.md` |
| Role summaries | `career/careerSummary/` |
| Skills | `career/skills/skills.md` |
| Projects | `career/projects/` |
| Interview stories | `career/firstPersonVoice/` |
| Markdown/PDF appearance | `career/resumeFormatting.yml`, `career/resume.css` |
| Maintenance history | `career/updateLog.md` |

See [docs/maintenance.md](docs/maintenance.md) for the update routine and [docs/repository-map.md](docs/repository-map.md) for source/output rules.

## Contributing

Contributions are welcome for improvements to the generator, documentation, setup instructions, and validation workflow.

1. Fork the repository and create a focused branch.
2. Make the smallest change that solves the problem.
3. Run the relevant setup checks and `python3 -m py_compile scripts/*.py`.
4. Run `.venv/bin/python scripts/validate_resume.py` when changing resume-generation behavior.
5. Open a pull request describing the change and how it was tested.

Do not include real phone numbers, email addresses, private employment details, employer-confidential information, generated resumes, or other personal data in an issue or pull request. Use fictional or redacted examples when demonstrating a bug.

## Security and Privacy

This repository handles highly sensitive personal and career information. Before publishing or contributing:

- Search the complete Git history as well as the current files for secrets and personal information.
- Keep private profiles and generated resumes out of commits.
- Never commit API keys, passwords, access tokens, `.env` files, or private job descriptions.
- Report a suspected secret or security issue privately through the repository's GitHub security contact instead of opening a public issue.

The repository does not currently include a CI workflow, CodeQL configuration, or dependency automation. If those are added later, keep permissions minimal, avoid printing secrets, and review workflow changes like application code.


## Public Repository Note

The scripts currently contain Anil-specific header and filename validation because this repository is currently used for Anil's profile. That is acceptable for this personal version.

If you want a genuinely multi-user repository, refactor the scripts to load name, contact details, and filename identity from a profile configuration file instead of hard-coding them. Keep each person's private source material in a separate profile directory and publish only example files. Do not publish personal phone numbers, email addresses, work history, or generated resumes without permission.

## Documentation

- [Repository map](docs/repository-map.md)
- [Make this repository yours](docs/profile-customization.md)
- [Resume workflow and commands](docs/resume-workflow.md)
- [macOS setup](docs/macos-setup.md)
- [Ubuntu setup](docs/ubuntu-setup.md)
- [Windows setup](docs/windows-setup.md)
- [Maintenance guide](docs/maintenance.md)

## License and Privacy

Before publishing this repository, review every file for personal, employer-confidential, or proprietary information. The source evidence is more sensitive than the generator scripts and should normally remain private.
