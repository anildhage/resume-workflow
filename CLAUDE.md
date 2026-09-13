# Resume Workflow Project

## Overview
Automated resume generation system that creates tailored resumes from job descriptions by matching user profiles against job requirements.

## Key Components
- `scripts/` - Main resume generation scripts  
- `profiles/` - User profile data
- `templates/` - Resume templates
- `jd.md` - Job description input file
- `.venv/` - Virtual environment (Python dependencies for PDF generation)

## Setup & Usage
1. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Critical**: All commands must run within the activated virtual environment (.venv) because PDF generation packages (weasyprint, Markdown) are installed there.

3. **Note**: The `requirements.txt` contains dependencies like `weasyprint==66.0` and `Markdown==3.9`. These are installed once when setting up the environment.

## Workflow
1. Provide job description in `jd.md`
2. Load profile data from `profiles/` 
3. Process and match requirements
4. Generate customized resume with PDF output

## Important Notes
- All scripts must run in `.venv` environment for PDF functionality
- `.venv` directory is in `.gitignore` (not tracked)