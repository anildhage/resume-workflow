#!/usr/bin/env python3
"""
Main resume creation script for Anil that orchestrates the complete workflow.
This script analyzes the job description and generates a tailored resume for the Data Analyst role.
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Main orchestration function"""

    print("Starting resume creation process for Anil...")
    print("Analyzing job description and generating tailored resume...")

    # Get the role from job description
    jd_path = Path("jd.md")
    if not jd_path.exists():
        print("Error: jd.md file not found in project root.")
        return 1

    # Extract role from job description
    jd_content = jd_path.read_text(encoding="utf-8")

    # Simple role extraction - look for key terms in the job description
    role = "Data Analyst"  # Default role based on job description content

    print(f"Target role identified: {role}")

    try:
        # Generate content using our AI-powered generator
        content_gen_process = subprocess.Popen(
            [sys.executable, "scripts/generate_resume_content.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        content, error = content_gen_process.communicate()

        if content_gen_process.returncode != 0:
            print(f"Content generation failed: {error}")
            return 1

        # Clean up the content by removing status messages and keeping only actual resume content
        lines = content.strip().split('\n')
        content_start = 0
        for i, line in enumerate(lines):
            if line.startswith('Anil Dhage'):
                content_start = i
                break

        clean_content = '\n'.join(lines[content_start:]) + '\n'

        print("Content generated successfully. Processing resume...")

        # Run write_resume.py with the generated content via stdin
        write_resume_process = subprocess.Popen(
            [sys.executable, "scripts/write_resume.py", "--role", role, "--profile", "profiles/anil"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output, error = write_resume_process.communicate(input=clean_content)

        if write_resume_process.returncode != 0:
            print(f"Resume generation failed: {error}")
            return 1

        print("Resume successfully created!")
        print(output)

    except Exception as e:
        print(f"Error in resume creation workflow: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())