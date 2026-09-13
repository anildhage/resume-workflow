#!/usr/bin/env python3
"""
Test script to verify virtual environment requirements are met.
"""

import sys
import os

def check_virtual_environment():
    """Check if running in virtual environment"""
    # Check if we're in a virtual environment by looking for venv-related indicators
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Error: This script must be run within the activated virtual environment (.venv)")
        print("Please activate the virtual environment first: source .venv/bin/activate")
        return False
    return True

if __name__ == "__main__":
    if check_virtual_environment():
        print("✓ Virtual environment check passed")
        print(f"Python executable: {sys.executable}")
        print(f"Virtual environment path: {getattr(sys, 'real_prefix', getattr(sys, 'base_prefix', 'Not in venv'))}")
    else:
        sys.exit(1)