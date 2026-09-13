#!/usr/bin/env python3
"""
Helper script to extract detailed project information from Anil's profile projects
for better resume content generation.
"""

from pathlib import Path
import re

def extract_project_info(project_content):
    """Extract key information from a project markdown file"""

    # Parse the project content
    lines = project_content.strip().split('\n')

    project_info = {
        'name': '',
        'organization': '',
        'period': '',
        'role': '',
        'business_context': '',
        'problem_objective': '',
        'responsibilities': [],
        'tools_platforms': [],
        'outcomes': []
    }

    # Extract basic info from the header
    if len(lines) > 0:
        project_info['name'] = lines[0].replace('# ', '').strip()

    # Look for key-value pairs in the file
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Extract organization (from first line after header)
        if i == 2 and stripped.startswith('**Organization:**'):
            project_info['organization'] = stripped.replace('**Organization:**', '').strip()

        # Extract period
        elif i == 3 and stripped.startswith('**Period:**'):
            project_info['period'] = stripped.replace('**Period:**', '').strip()

        # Extract role
        elif i == 4 and stripped.startswith('**Role:**'):
            project_info['role'] = stripped.replace('**Role:**', '').strip()

        # Extract business context
        elif stripped.startswith('## Business context'):
            if i + 1 < len(lines):
                project_info['business_context'] = lines[i+1].strip()

        # Extract problem/objective
        elif stripped.startswith('## Problem or objective'):
            if i + 1 < len(lines):
                project_info['problem_objective'] = lines[i+1].strip()

        # Extract responsibilities
        elif stripped.startswith('## Responsibilities and contributions'):
            # Collect all responsibility items
            for j in range(i+1, len(lines)):
                if lines[j].startswith('## ') or lines[j].startswith('# '):
                    break
                if lines[j].strip().startswith('- ') and not lines[j].strip().startswith('- Tools'):
                    project_info['responsibilities'].append(lines[j].strip()[2:].strip())

        # Extract tools/platforms
        elif stripped.startswith('## Tools, platforms, and systems'):
            # Collect all tool items
            for j in range(i+1, len(lines)):
                if lines[j].startswith('## ') or lines[j].startswith('# '):
                    break
                if lines[j].strip().startswith('- '):
                    project_info['tools_platforms'].append(lines[j].strip()[2:].strip())

        # Extract outcomes
        elif stripped.startswith('## Outcomes and value'):
            # Collect all outcome items
            for j in range(i+1, len(lines)):
                if lines[j].startswith('## ') or lines[j].startswith('# '):
                    break
                if lines[j].strip().startswith('- ') and not lines[j].strip().startswith('- Tools'):
                    project_info['outcomes'].append(lines[j].strip()[2:].strip())

    return project_info

def main():
    """Main function to process all projects"""

    projects_dir = Path("profiles/anil/projects/")
    if not projects_dir.exists():
        print("No projects directory found")
        return 1

    all_projects = []

    for file_path in projects_dir.glob("*.md"):
        try:
            content = file_path.read_text(encoding="utf-8")
            project_info = extract_project_info(content)
            project_info['filename'] = file_path.name
            all_projects.append(project_info)
            print(f"Processed: {project_info['name']}")
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")

    # Display the results
    for project in all_projects:
        print(f"\n--- {project['name']} ---")
        print(f"Organization: {project['organization']}")
        print(f"Period: {project['period']}")
        print(f"Role: {project['role']}")
        print(f"Business Context: {project['business_context']}")
        print(f"Problem/Objective: {project['problem_objective']}")
        print("Responsibilities:")
        for resp in project['responsibilities']:
            print(f"  - {resp}")
        print("Tools/Platforms:")
        for tool in project['tools_platforms']:
            print(f"  - {tool}")
        print("Outcomes:")
        for outcome in project['outcomes']:
            print(f"  - {outcome}")

    return 0

if __name__ == "__main__":
    exit(main())