# Resume Workflow Project

## Overview
Automated resume generation system that creates tailored resumes from job descriptions by matching user profiles against job requirements.

## Key Files
- `jd.md` - Job description input file (required for each resume generation)
- `profiles/local/` - Source profile data (user's personal information and experience)
- `scripts/create_resume.py` - Main orchestration script

## How It Works
1. The system reads `jd.md` to understand job requirements
2. It loads profile data from `profiles/local/` 
3. The AI-powered content generator creates tailored resume content
4. The validation script ensures quality standards are met
5. Final Markdown and PDF files are saved to `career/files/md/` and `career/files/pdf/`

## Usage for Anil
1. Update `jd.md` with the job description
2. **Ensure virtual environment is activated**: `source .venv/bin/activate`
3. Run: `python3 scripts/create_resume.py`
4. Find generated resume in `career/files/md/DataAnalyst-AnilDhage-*.md` and `career/files/pdf/DataAnalyst-AnilDhage-*.pdf`

## Profile Structure
The system uses `profiles/local/` as the source data, not `files/`. Key files:
- `resumeSkeleton.md` - Name, contact details, employers, education, certifications
- `profileFacts.md` - Professional identity and recurring strengths  
- `targetResume.md` - Generation rules and examples

## Requirements
- Python 3.7+
- Virtual environment with dependencies (installed via requirements.txt)
- **All commands must run within the activated virtual environment (.venv)** because PDF generation packages are installed there

## Output Location
Generated resumes are written to:
- `career/files/md/` - Markdown files  
- `career/files/pdf/` - PDF files

Note: The `files/` directory is only for output, not source data. Source profile information comes from `profiles/local/`.