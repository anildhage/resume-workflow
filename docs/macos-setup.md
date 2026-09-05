# macOS Setup

## Requirements

- macOS
- Python 3
- Git
- VS Code (optional)
- Homebrew (recommended for native PDF libraries)

## Install System Dependencies

Install Homebrew from [brew.sh](https://brew.sh/) if it is not already installed, then run:

```bash
brew install python@3.13 cairo pango gdk-pixbuf libffi
```

## Get the Repository

```bash
git clone <repository-url> resume-workflow
cd resume-workflow
```

If the repository is already downloaded, open Terminal in its root directory, the folder containing `README.md`, `career/`, and `scripts/`.

## Create the Environment

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

## Verify the Installation

```bash
.venv/bin/python --version
.venv/bin/python -c "import markdown; print('Markdown is ready')"
.venv/bin/python -c "from weasyprint import HTML; print('WeasyPrint is ready')"
.venv/bin/python -m py_compile scripts/*.py
.venv/bin/python scripts/validate_resume.py
```

The empty-output validation should pass when no resumes have been generated yet.

## Run the Workflow

Use the agent workflow described in the root README, or test the writer manually with a complete Markdown draft:

```bash
.venv/bin/python scripts/write_resume.py \
  --role "Data Scientist" \
  --content "<generated Markdown draft>"
```

Then validate:

```bash
.venv/bin/python scripts/validate_resume.py
```

## VS Code

Open the repository root in VS Code. Select `.venv/bin/python` with **Python: Select Interpreter** if VS Code does not select it automatically.

## Common Problems

If `markdown` is missing, reinstall `requirements.txt` inside `.venv`. If WeasyPrint cannot load native libraries, rerun the Homebrew install command and recreate the virtual environment.
