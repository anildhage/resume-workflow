# Ubuntu Setup

This guide prepares an Ubuntu machine to build role-targeted resumes from this repository. A successful build creates both files:

- Markdown: `career/files/md/RoleName-AnilDhage-N.md`
- PDF: `career/files/pdf/RoleName-AnilDhage-N.pdf`

The Markdown file is validated and written first. PDF conversion starts only after the Markdown content and presentation checks pass.

## Requirements

Use a supported Ubuntu installation with:

- Python 3
- `python3-venv`
- `python3-pip`
- Native libraries required by WeasyPrint
- Git, if cloning the repository

The commands below work from a normal Ubuntu terminal. The `sudo` commands require an account allowed to install system packages.

## Install System Packages

Update the package index and install Python, Git, and the native PDF-rendering libraries:

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

These packages provide the operating-system libraries used by WeasyPrint for fonts, text layout, graphics, and PDF generation. The macOS Homebrew packages are not used on Ubuntu.

## Get the Repository

If the repository is already present, change into its root directory. The root directory is the one containing `README.md`, `requirements.txt`, `career/`, and `scripts/`.

```bash
cd /path/to/notes
```

If cloning for the first time:

```bash
git clone <repository-url> notes
cd notes
```

All commands in this guide should be run from the repository root.

## Create the Virtual Environment

Create a local virtual environment and install the pinned Python dependencies:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

The repository uses the virtual environment so Python package versions are isolated from the Ubuntu system Python. Do not install the project dependencies globally.

To activate the environment for an interactive shell:

```bash
source .venv/bin/activate
```

After activation, `python` and `pip` refer to the project environment. You can also avoid activation and use `.venv/bin/python` explicitly, which is the more deterministic option for scripts and automation.

## Verify the Environment

Check Python and the two required Python packages:

```bash
.venv/bin/python --version
.venv/bin/python -c "import markdown; print('Markdown is ready')"
.venv/bin/python -c "from weasyprint import HTML; print('WeasyPrint is ready')"
```

Compile all repository scripts and run the empty-output validation check:

```bash
.venv/bin/python -m py_compile scripts/*.py
.venv/bin/python scripts/validate_resume.py
```

The validator should report that no generated resumes were found and that validation passed when `career/files/md/` is empty.

## Output Directories

The writer creates these directories automatically when it generates a resume:

```text
career/files/
  md/     validated Markdown resumes
  pdf/    matching styled PDF resumes
```

Generated files are outputs only. Do not use them as source material for later resume drafting.

## Build a Resume From a Job Description

The normal user-facing workflow is to provide a job description or job-role details and ask the agent to create a tailored resume. The request does not need to contain a literal command. Any request that means build or create a resume from job requirements should follow the complete workflow:

1. Identify the target role and requirements from the job description.
2. Read the repository instructions, skeleton, profile facts, summaries, skills, projects, and first-person evidence.
3. Draft a role-aligned resume using only supported facts.
4. Apply the final Markdown headings, spacing, and strategic bolding.
5. Validate the content and presentation rules.
6. Save the Markdown file under `career/files/md/`.
7. Convert the validated Markdown file to a styled PDF under `career/files/pdf/`.
8. Confirm that both matching files exist before reporting success.

The user should not normally run `scripts/write_resume.py` manually. That script is the internal save-and-convert step used after the agent has created the Markdown draft.

## Manual Writer Invocation

For testing or automation, the writer accepts a complete generated Markdown draft through `--content`:

```bash
.venv/bin/python scripts/write_resume.py \
  --role "Data Scientist" \
  --content "<generated Markdown draft>"
```

The placeholder text above is not a valid resume. The content must include all required sections, fixed facts, supported evidence, valid experience claims, and the configured bold spans.

On success, the writer prints the Markdown and PDF paths. It refuses to overwrite an existing matching output. If PDF conversion fails, it removes the incomplete Markdown output so the repository does not report a partial build as successful.

## Validate Generated Outputs

Run validation after a build:

```bash
.venv/bin/python scripts/validate_resume.py
```

Validation checks include:

- Markdown filename and required sections
- Placeholder removal
- Skeleton-derived experience claim
- Strategic bolding limits and evidence bolding
- Matching PDF existence
- PDF file signature
- Unexpected PDFs without matching Markdown files

A resume build is complete only when this validation succeeds.

## Regenerate One PDF

After editing an existing Markdown resume, update `career/pdfBuild.yml` with the Markdown and PDF filenames, then run:

```bash
chmod +x build-pdf.command
./build-pdf.command
```

The command reuses the PDF settings in `career/resumeFormatting.yml`. It refuses to replace an existing PDF unless `overwrite: true` is set in `career/pdfBuild.yml`.

Run `.venv/bin/python scripts/validate_resume.py` after editing and after regeneration to confirm the Markdown/PDF pair is valid.

## PDF Appearance

PDF styling is defined in `career/resume.css`. The renderer uses standard Markdown conversion, so Markdown such as:

```markdown
**SQL**
```

becomes bold text in the PDF. The stylesheet controls page size, margins, font stack, headings, spacing, bullets, rules, and bold weight.

PDF-only cosmetic settings are controlled in the `pdf:` section of `career/resumeFormatting.yml`. This section can adjust organization and role metadata emphasis, heading and body sizes, page margins, text color, and rule color without changing the Markdown generation settings under `formatting:`.

To change the visual appearance, update `career/resume.css` and generate a new resume. Do not manually edit generated PDFs as the primary fix.

## VS Code on Ubuntu

Open the repository root in VS Code. The repository setting in `.vscode/settings.json` points Python to:

```text
.venv/bin/python
```

If VS Code still reports unresolved imports, select the interpreter manually with **Python: Select Interpreter**, then choose the repository's `.venv/bin/python`.

## Common Problems

### `No module named markdown`

Install the Python dependencies inside the project environment:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

### WeasyPrint cannot load Pango, Cairo, or GObject

Install the native Ubuntu packages again:

```bash
sudo apt update
sudo apt install -y libcairo2 libgdk-pixbuf-2.0-0 libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b libharfbuzz-subset0 libffi-dev
```

Then repeat the verification command:

```bash
.venv/bin/python -c "from weasyprint import HTML; print('WeasyPrint is ready')"
```

### Validation says the PDF is missing

The Markdown file was not successfully converted. Check the writer output and rerun the build with `.venv/bin/python`. Confirm the PDF libraries are installed and that `career/files/pdf/` is writable.

### The output already exists

The writer never overwrites an existing resume. Keep the existing pair or remove it deliberately before generating a replacement:

```bash
ls career/files/md/
ls career/files/pdf/
```

### Fonts look different on Ubuntu

PDF rendering uses fonts available on the Ubuntu host. For predictable output, install the fonts referenced by the stylesheet or change `career/resume.css` to a font available on the deployment machine. Rebuild the PDF after changing fonts.

## Updating the Environment

When dependencies change, update `requirements.txt` and repeat:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

When moving the repository to another Ubuntu machine, repeat the system package installation and virtual-environment setup. Do not copy `.venv` between operating systems or CPU architectures; recreate it on the target machine.
