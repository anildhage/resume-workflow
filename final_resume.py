#!/usr/bin/env python3
"""
Direct resume creation script that bypasses the complex subprocess flow.
This script directly generates and saves a resume for Anil.
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Main function to generate and save resume directly"""

    print("Starting direct resume creation process...")

    # Create a temporary file with the content
    try:
        # Generate content using our AI-powered generator
        content_process = subprocess.Popen(
            [sys.executable, "scripts/generate_resume_content.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        content_output, error = content_process.communicate()

        if content_process.returncode != 0:
            print(f"Content generation failed: {error}")
            return 1

        # Extract just the resume content (skip the first few lines with status messages)
        lines = content_output.strip().split('\n')
        # Find where actual content starts
        content_start = 0
        for i, line in enumerate(lines):
            if line.startswith('Anil Dhage'):
                content_start = i
                break

        clean_content = '\n'.join(lines[content_start:]) + '\n'

        print("Content generated successfully. Saving resume...")

        # Save to temporary file and then use write_resume.py with that
        temp_file = Path("/tmp/resume_temp.md")
        temp_file.write_text(clean_content, encoding="utf-8")

        # Now run write_resume.py with the content from the temp file
        write_process = subprocess.Popen(
            [sys.executable, "scripts/write_resume.py", "--role", "Data Analyst", "--profile", "profiles/anil"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output, error = write_process.communicate(input=clean_content)

        if write_process.returncode != 0:
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