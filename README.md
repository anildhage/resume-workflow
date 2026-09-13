# Resume Workflow

This project provides an automated resume creation workflow for generating tailored resumes based on job descriptions.

## Features

- **AI-Powered Content Generation**: Creates customized resume content based on your profile and job requirements
- **Multi-Format Output**: Generates both Markdown and PDF versions of your resume
- **Professional Formatting**: Applies consistent styling and structure to all generated resumes
- **Validation**: Ensures content meets quality standards before saving

## Files

### Profile Configuration
- `profiles/anil/profile.yml` - Personal information (name, contact details, etc.)

### Job Description
- `jd.md` - The job description to base your resume on

### Scripts
- `scripts/create_resume.py` - Main orchestration script
- `scripts/generate_resume_content.py` - AI-powered content generator
- `scripts/write_resume.py` - Formats and saves the resume
- `scripts/profile.py` - Profile loading utilities

## Usage

Run the main script to generate a tailored resume:
```bash
python3 scripts/create_resume.py
```

This will create both Markdown and PDF versions in:
- `career/files/md/`
- `career/files/pdf/`

## Output

Generated files include:
- Markdown (.md) version with proper formatting
- PDF (.pdf) version with professional styling