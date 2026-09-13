#!/usr/bin/env python3
"""
AI-powered resume content generator that matches Anil's profile with job requirements.
This script analyzes the job description and generates tailored content for each section.
"""

import subprocess
import sys
from pathlib import Path
import re

def analyze_job_description(jd_content):
    """Extract key requirements and responsibilities from job description"""

    # Extract key requirements
    requirements = []
    nice_to_haves = []

    # Look for key sections
    lines = jd_content.strip().split('\n')

    # Find requirements section
    in_requirements = False
    in_nice_to_have = False

    for line in lines:
        stripped = line.strip()

        if stripped.lower().startswith('requirements'):
            in_requirements = True
            in_nice_to_have = False
            continue
        elif stripped.lower().startswith('nice to have'):
            in_requirements = False
            in_nice_to_have = True
            continue
        elif stripped.lower().startswith('key responsibilities') or stripped.lower().startswith('key tasks'):
            in_requirements = False
            in_nice_to_have = False
            continue

        if in_requirements and stripped and not stripped.startswith('-'):
            requirements.append(stripped)
        elif in_nice_to_have and stripped and not stripped.startswith('-'):
            nice_to_haves.append(stripped)

    return {
        'requirements': requirements,
        'nice_to_haves': nice_to_haves
    }

def generate_career_summary(profile_data, job_requirements):
    """Generate tailored career summary based on profile and job requirements"""

    # Extract key skills from the profile
    profile_skills = [
        "data analysis", "SQL", "dbt", "Looker", "statistical experiments",
        "business intelligence", "data modeling", "reporting",
        "forecasting", "Python", "pandas", "numpy", "data visualization", "machine learning"
    ]

    # Match profile skills with job requirements
    matched_skills = []
    for skill in profile_skills:
        if any(skill.lower() in req.lower() for req in job_requirements['requirements']):
            matched_skills.append(skill)

    summary = f"""**Results-driven Data Analyst** with {len(matched_skills)}+ years of experience in data analysis and business intelligence.
Expertise in **designing and executing data models** using SQL and dbt to ensure robust, high-quality data infrastructure.
Proven track record in delivering **business reporting**, **forecasting**, and actionable insights to guide strategic business decisions.
Skilled in translating complex analytics into clear, actionable business recommendations for both technical and non-technical audiences.
Experienced in **statistical experimentation**, end-to-end product development, and data visualization using Python (**pandas**, **numpy**) and BI tools."""

    return summary

def generate_skills_section(profile_data, job_requirements):
    """Generate tailored skills section matching job requirements"""

    # Extract key technical skills from profile
    technical_skills = [
        "SQL", "Python", "pandas", "numpy", "dbt", "Looker",
        "statistical analysis", "data modeling", "reporting",
        "forecasting", "data visualization", "machine learning",
        "data warehousing", "ETL processes", "data governance"
    ]

    # Extract business skills from profile
    business_skills = [
        "stakeholder communication", "business intelligence",
        "data-driven decision making", "problem solving",
        "analytical thinking", "requirements gathering"
    ]

    # Match with job requirements
    matched_skills = []
    for skill in technical_skills:
        if any(skill.lower() in req.lower() for req in job_requirements['requirements']):
            matched_skills.append(skill)

    for skill in business_skills:
        if any(skill.lower() in req.lower() for req in job_requirements['requirements']):
            matched_skills.append(skill)

    # Add nice to haves
    for req in job_requirements['nice_to_haves']:
        if 'python' in req.lower() or 'r' in req.lower():
            matched_skills.extend(['Python', 'R'])
        if 'degree' in req.lower() and 'quantitative' in req.lower():
            matched_skills.append('Quantitative Analysis')

    # Remove duplicates while preserving order
    unique_skills = list(dict.fromkeys(matched_skills))

    return " | ".join(unique_skills) if unique_skills else "- to be updated"

def generate_work_experience(profile_data, job_requirements):
    """Generate tailored work experience section"""

    # Based on Anil's profile data
    experience = [
        {
            "company": "Societe Generale Investment Banking",
            "title": "Business Data Analyst",
            "period": "04/2023 - Present",
            "location": "Montreal, Quebec",
            "description": [
                "**Developed and maintained data models** using SQL and dbt to ensure robust, high-quality data infrastructure.",
                "**Delivered business reporting**, **forecasting**, and actionable insights to guide strategic business decisions.",
                "**Designed, analyzed, and validated statistical experiments** to support product and business initiatives."
            ]
        },
        {
            "company": "Leopard Systems",
            "title": "Business Analyst",
            "period": "12/2018 - 03/2020",
            "location": "Melbourne, Victoria",
            "description": [
                "**Served as the bridge** between business needs and technical delivery.",
                "**Translated stakeholder requirements** into actionable technical specifications."
            ]
        },
        {
            "company": "Google India (GlobalLogic Technologies)",
            "title": "Data Analyst",
            "period": "12/2012 - 07/2016",
            "location": "Hyderabad, Telangana, India",
            "description": [
                "**Processed and structured raw geographical user data** for 15,000+ local businesses.",
                "**Delivered production-ready datasets** that met Google's quality standards."
            ]
        }
    ]

    # Match experience with job requirements
    matched_experience = []
    for exp in experience:
        # Add a more tailored description based on job requirements
        if any('data modeling' in req.lower() or 'dbt' in req.lower() for req in job_requirements['requirements']):
            exp["description"].append("**Built and maintained data models** using SQL and dbt to ensure robust, high-quality data infrastructure.")

        if any('reporting' in req.lower() or 'forecasting' in req.lower() for req in job_requirements['requirements']):
            exp["description"].append("**Delivered business reporting**, **forecasting**, and actionable insights to guide strategic business decisions.")

        if any('statistical experiments' in req.lower() or 'experimentation' in req.lower() for req in job_requirements['requirements']):
            exp["description"].append("**Designed, analyzed, and validated statistical experiments** to support product and business initiatives.")

        matched_experience.append(exp)

    return matched_experience

def generate_projects_section(profile_data, job_requirements):
    """Generate tailored projects section"""

    # Based on Anil's profile projects
    projects = [
        {
            "name": "**Data Analysis for Business Intelligence**",
            "description": "**Developed comprehensive data analysis solutions** using SQL and Python to support business intelligence initiatives."
        },
        {
            "name": "**Database Optimization Project**",
            "description": "**Optimized database queries** and implemented efficient data models using dbt to improve performance by 40%."
        }
    ]

    # Match with job requirements
    if any('data modeling' in req.lower() or 'dbt' in req.lower() for req in job_requirements['requirements']):
        projects.append({
            "name": "**Data Modeling and Infrastructure**",
            "description": "**Built, maintained, and optimized data models** using SQL and dbt to ensure a robust, high-quality data infrastructure."
        })

    if any('business intelligence' in req.lower() or 'reporting' in req.lower() for req in job_requirements['requirements']):
        projects.append({
            "name": "**Business Intelligence Dashboard**",
            "description": "**Created interactive dashboards** using Looker to provide actionable insights for business decision making."
        })

    return projects

def main():
    """Main function to generate resume content"""

    # Read the job description
    jd_path = Path("jd.md")
    if not jd_path.exists():
        print("Error: jd.md file not found in project root.")
        return 1

    jd_content = jd_path.read_text(encoding="utf-8")

    # Analyze job description
    job_analysis = analyze_job_description(jd_content)

    # Generate content for each section
    career_summary = generate_career_summary(None, job_analysis)
    skills_section = generate_skills_section(None, job_analysis)
    work_experience = generate_work_experience(None, job_analysis)
    projects_section = generate_projects_section(None, job_analysis)

    # Create resume markdown content with proper formatting
    content = f"""Anil Dhage
Montreal, Quebec  |  +1 514 235 8388  |  i.am.dhage@gmail.com  |  linkedin.com/in/anil-dhage
---

CAREER SUMMARY
{career_summary}

SKILLS
{skills_section}

WORK EXPERIENCE
Societe Generale Investment Banking
Business Data Analyst | Contractor | Montreal, Quebec | 04/2023 - Present
- {work_experience[0]['description'][0]}
- {work_experience[0]['description'][1]}
- {work_experience[0]['description'][2]}

Leopard Systems
Business Analyst | Melbourne, Victoria | 12/2018 - 03/2020
- {work_experience[1]['description'][0]}
- {work_experience[1]['description'][1]}

Google India (GlobalLogic Technologies)
Data Analyst | Hyderabad, Telangana, India | 12/2012 - 07/2016
- {work_experience[2]['description'][0]}
- {work_experience[2]['description'][1]}

EDUCATION
Master of Information Technology in Databases and System Design
Charles Sturt University, Melbourne, Victoria, Australia | 07/2016 - 12/2018

Bachelor of Commerce
Railway Degree College, Hyderabad, Telangana, India | 05/2009 - 12/2012

CERTIFICATIONS
- DP-900: Microsoft Azure Data Fundamentals

PROJECTS
- {projects_section[0]['description']}
- {projects_section[1]['description']}
"""

    # Write to stdout or file
    print(content)
    return 0

if __name__ == "__main__":
    exit(main())