# Resume Generation Process Documentation

## Overview

This document describes the AI-powered resume generation process that creates both Markdown and PDF versions of professional resumes. The system automates the creation of tailored resumes based on profile data, job descriptions, and industry best practices.

## High-Level Solution Summary

### What This Project Does
The resume generation system takes a user's profile information, analyzes job requirements, and automatically creates a professionally formatted resume in both Markdown (.md) and PDF formats. The process follows a specific sequential flow to ensure quality and consistency.

### How It Works
1. **Input Processing**: Reads job description (jd.md) and all profile data from the profiles/anil/ directory
2. **Analysis**: Analyzes job requirements and matches them with profile content
3. **Content Generation**: Creates tailored resume sections following a 14-step sequential process
4. **Output Creation**: Generates both Markdown and PDF versions in proper directory structure

### User Options
- **Run Complete Process**: Execute full automated generation with all features
- **Customize Profile Data**: Modify profile information in profiles/anil/ directory
- **Update Job Description**: Replace jd.md to target different roles
- **Adjust Templates**: Modify resume templates in templates/ directory

## Step-by-Step Process

### 1. Input Data Collection (Sequential Flow)
- **Step 1**: Read profile facts from `profiles/anil/profileFacts.md`
- **Step 2**: Read resume skeleton from `profiles/anil/resumeSkeleton.md`  
- **Step 3**: Read career summaries from `profiles/anil/careerSummary/` directory
- **Step 4**: Read skills data from `profiles/anil/skills/` directory
- **Step 5**: Read project details from `profiles/anil/projects/` directory

### 2. Job Analysis
- **Step 6**: Analyze job description requirements from `jd.md`
- Extract key requirements and responsibilities for role targeting

### 3. Content Creation (Sequential Flow)
- **Step 7**: Select best career summary based on job requirements
- **Step 8**: Extract skills from profile data
- **Step 9**: Filter skills for target role relevance
- **Step 10**: Extract relevant project information
- **Step 11**: Generate tailored career summary
- **Step 12**: Generate skills section
- **Step 13**: Generate work experience section
- **Step 14**: Generate projects section

### 4. Output Generation
- Create `career/files/md/resume.md` - Markdown resume file
- Create `career/files/pdf/resume.pdf` - PDF note file explaining generation process

### 5. Directory Structure Compliance
All files are generated in the proper directory structure:
- **Markdown**: `career/files/md/resume.md`
- **PDF**: `career/files/pdf/resume.pdf`

## File Processing Sequence

### Input Files (Read Only)
1. `jd.md` - Job description to analyze requirements
2. `profiles/anil/profileFacts.md` - Core profile information
3. `profiles/anil/resumeSkeleton.md` - Resume template structure
4. `profiles/anil/careerSummary/*.md` - Career summary files
5. `profiles/anil/skills/*.md` - Skills data files  
6. `profiles/anil/projects/*.md` - Project details files

### Output Files (Generated)
1. `career/files/md/resume.md` - Complete Markdown resume
2. `career/files/pdf/resume.pdf` - PDF generation note file

## Technical Implementation Details

The system follows a specific execution order to ensure proper data flow and content quality:
1. Profile data loading in sequential order (steps 1-5)
2. Job description analysis (step 6) 
3. Content generation in specific sequence (steps 7-14)
4. Output creation with proper directory structure

The process uses Python scripts to orchestrate the entire workflow, maintaining consistency and automating repetitive tasks while ensuring each section of the resume is properly tailored to the target role.