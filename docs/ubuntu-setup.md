# Ubuntu Setup

## Requirements

- Python 3
- `python3-venv`
- `python3-pip`
- Git
- Native libraries required by WeasyPrint

## Install System Dependencies

```bash
sudo apt update
sudo apt install -y \
  git \
  python3 \
  python3-venv \
  python3-pip \
  libcairo2 \
  libgdk-pixbuf-2.0-0 \
  libpango-1.0-0 \
  libpangoft2-1.0-0 \
  libharfbuzz0b \
  libharfbuzz-subset0 \
  libffi-dev
```

## Get the Repository

```bash
git clone <repository-url> resume-workflow
cd resume-workflow
```

If the repository is already present, change to its root directory, the folder containing `README.md`, `career/`, and `scripts/`.

## Create the Environment

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

You can activate it with `source .venv/bin/activate`, or use `.venv/bin/python` explicitly as shown in this guide.

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

Use the agent workflow described in the root README, or test the writer manually:

```bash
.venv/bin/python scripts/write_resume.py \
  --profile profiles/local \
  --role "Data Scientist" \
  --content "<generated Markdown draft>"
```

Then validate:

```bash
.venv/bin/python scripts/validate_resume.py --profile profiles/local
```

## VS Code

Open the repository root in VS Code. Select `.venv/bin/python` with **Python: Select Interpreter** if needed.

## Common Problems

If `markdown` is missing, reinstall `requirements.txt` inside `.venv`. If WeasyPrint cannot load Pango, Cairo, or GObject, reinstall the native packages above and rerun the verification command.
