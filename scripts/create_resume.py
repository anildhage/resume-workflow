#!/usr/bin/env python3
"""
Create a resume for Anil based on the current job description in jd.md.
This script is called when user prompts "create a resume" and will use
the role from jd.md to generate an appropriate resume.
"""

import subprocess
import sys
from pathlib import Path

def extract_role_from_jd(jd_content):
    """Extract role name from job description"""
    
    # Look for the main role in the first few lines
    lines = jd_content.strip().split('\n')
    
    # Try to find the role from "As a [Role] you will be..." pattern
    for line in lines:
        if line.strip().startswith('As a ') and 'you will be' in line:
            # Extract role from "As a Data Analyst you will be..."
            role_part = line.split('As a ')[1].split(' you will be')[0]
            return role_part.strip()
    
    # If that fails, try to find it from the first paragraph
    for line in lines:
        if line.strip() and not line.startswith('As a ') and not line.startswith('You\'ll'):
            # Check if this looks like a role name (not a description)
            if len(line.split()) <= 8:  # Reasonable length for a role name
                return line.strip()
    
    # If we still can't extract it, return a default
    return "Data Analyst"

def create_resume_from_jd():
    """Generate a resume using the role from jd.md"""
    
    # Read the job description file
    jd_path = Path("jd.md")
    if not jd_path.exists():
        print("Error: jd.md file not found in project root.")
        return 1
    
    jd_content = jd_path.read_text(encoding="utf-8")
    
    # Extract the role from the job description
    role_name = extract_role_from_jd(jd_content)
    
    if not role_name:
        print("Error: Could not extract role from job description.")
        return 1
    
    print(f"Creating resume for role: {role_name}")
    
    try:
        # Run the actual resume generation with the extracted role
        result = subprocess.run([
            sys.executable, "scripts/write_resume.py",
            "--profile", "profiles/anil",
            "--role", role_name
        ], check=True, capture_output=True, text=True)
        
        print("Resume created successfully!")
        print("Generated files are in career/files/md/ and career/files/pdf/")
        return 0
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating resume: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit(create_resume_from_jd())