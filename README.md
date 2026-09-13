# Resume Workflow

Build role-targeted Markdown resumes and matching PDFs from a trusted set of career facts, projects, skills, and work stories.

## What This Repo Does

The workflow:
1. Reads your fixed resume facts and supporting evidence.
2. Uses a job description or target role to select relevant content.
3. Creates a new, validated Markdown resume.
4. Renders a matching PDF.
5. Checks that the output is complete, factual, and correctly formatted.

Generated resumes are written to `career/files/md/` and `career/files/pdf/`. Those folders are created automatically, are outputs only, and are ignored by Git.

## Quick Start

1. Create your private profile once:
```bash
python3 scripts/init_profile.py
```
This creates `profiles/local/` from the public templates. The directory is ignored by Git and must remain private.

2. Update your profile information in `profiles/local/`:
   - `resumeSkeleton.md` - Name, contact details, employers, education, certifications
   - `profileFacts.md` - Professional identity and recurring strengths
   - `targetResume.md` - Resume-generation rules

3. Provide a job description in `jd.md`

4. Generate your tailored resume:
```bash
python3 scripts/create_resume.py
```

## Profile Structure

The system uses profiles/ as the source data, not files/. The key profile files are:

- `profiles/local/resumeSkeleton.md` - Fixed resume facts (name, contact, employers, education)
- `profiles/local/profileFacts.md` - Stable profile facts (professional identity)
- `profiles/local/targetResume.md` - Generation rules and examples
- `profiles/local/careerSummary/` - Role-specific summaries  
- `profiles/local/skills/skills.md` - Skills you have actually used
- `profiles/local/projects/` - Substantial projects and workstreams
- `profiles/local/firstPersonVoice/` - Interview stories and detailed context

## How It Works

1. The system reads `jd.md` to understand job requirements
2. It analyzes your profile data in `profiles/local/`
3. The AI-powered content generator (`generate_resume_content.py`) creates tailored resume content
4. The validation script ensures the output meets quality standards including proper bolding requirements
5. Final Markdown and PDF files are saved to `career/files/md/` and `career/files/pdf/`

## Usage Examples

### For Anil's Data Analyst Resume:
1. Place job description in `jd.md`
2. Run `python3 scripts/create_resume.py`
3. Find generated resume in `career/files/md/DataAnalyst-AnilDhage-*.md` and `career/files/pdf/DataAnalyst-AnilDhage-*.pdf`

### For a Different Role:
1. Update `jd.md` with new job description
2. Run `python3 scripts/create_resume.py`
3. System generates resume tailored to the new requirements

## Customization

To create your own customized version:
1. Edit files in `profiles/local/` to reflect your personal information
2. Update `jd.md` with any job description for which you want a tailored resume
3. Run the main script to generate your resume

## Requirements

- Python 3.7+
- Virtual environment with dependencies (installed via requirements.txt)
- All commands must run within the activated virtual environment (.venv) because PDF generation packages are installed there

## Security and Privacy

This repository handles highly sensitive personal and career information:
- Private profiles belong under `profiles/`, which is ignored by Git
- Generated resumes are output only, not tracked in Git
- Never commit real personal data, employer-confidential information, or generated resumes