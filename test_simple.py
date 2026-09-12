#!/usr/bin/env python3
"""
Simple test to check if the issue is with PDF generation
"""

import subprocess
import sys
from pathlib import Path

def main():
    print("Testing resume creation without PDF generation...")
    
    # Test just the markdown part by temporarily disabling PDF generation
    try:
        result = subprocess.run([
            sys.executable, "scripts/write_resume.py",
            "--profile", "profiles/anil",
            "--role", "Data Analyst",
            "--no-pdf"  # This would be a new option to skip PDF generation
        ], check=True, capture_output=True, text=True, timeout=30)
        
        print("Success!")
        print("STDOUT:", result.stdout[:200])
        if result.stderr:
            print("STDERR:", result.stderr[:200])
            
    except subprocess.TimeoutExpired:
        print("Timeout occurred")
        return 1
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())