# Windows Setup

## Requirements

- Windows 10 or Windows 11
- Python 3.11 or newer
- Git
- VS Code (optional)

Install Python from [python.org](https://www.python.org/downloads/windows/) and select **Add Python to PATH** during installation. Install Git from [git-scm.com](https://git-scm.com/download/win/).

## Get the Repository

Open PowerShell:

```powershell
git clone <repository-url> resume-workflow
cd resume-workflow
```

## Create the Environment

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Verify the Installation

```powershell
.venv\Scripts\python.exe --version
.venv\Scripts\python.exe -c "import markdown; print('Markdown is ready')"
.venv\Scripts\python.exe -c "from weasyprint import HTML; print('WeasyPrint is ready')"
.venv\Scripts\python.exe -m py_compile scripts\*.py
.venv\Scripts\python.exe scripts\validate_resume.py
```

The empty-output validation should pass when no resumes have been generated yet.

## Run the Workflow

Use the agent workflow described in the root README, or test the writer manually:

```powershell
.venv\Scripts\python.exe scripts\write_resume.py `
  --profile profiles/local `
  --role "Data Scientist" `
  --content "<generated Markdown draft>"
```

Then validate:

```powershell
.venv\Scripts\python.exe scripts\validate_resume.py --profile profiles/local
```

## VS Code

Open the repository root in VS Code and choose `.venv\Scripts\python.exe` with **Python: Select Interpreter**.

## Common Problems

If `markdown` or `weasyprint` is missing, rerun the dependency installation command using the `.venv` interpreter. If PDF rendering fails, update Python and reinstall the requirements in a newly created `.venv`.
