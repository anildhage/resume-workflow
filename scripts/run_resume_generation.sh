#!/bin/bash

# Script to run resume generation in the proper virtual environment
echo "Starting resume generation process..."

# Activate virtual environment
source .venv/bin/activate

# Run the Python script
python3 generate_resume_content_v2.py

echo "Resume generation complete!"