# Make This Repository Yours

Personal resume data belongs in the ignored `profiles/` directory. The public repository contains safe starter templates under `templates/`.

## 0. Create Your Private Profile

From the repository root, run:

```bash
python3 scripts/init_profile.py
```

This creates `profiles/local/` and copies the starter templates into it. Do not force-add this directory to Git.

## 1. Replace the Resume Skeleton

Edit `profiles/local/resumeSkeleton.md` first. Replace:

- name and contact line
- employers and job titles
- employment types, locations, and dates
- education
- certifications

Keep the section names and overall structure. The experience calculator reads dated work entries from this file.

## 2. Replace Profile Facts

Edit `profiles/local/profileFacts.md` with your stable professional identity, strengths, and recurring capabilities. Keep this file short. Do not put every project detail here.

## 3. Add Your Evidence

Use the existing folders as a simple evidence library:

- Add role summaries to `profiles/local/careerSummary/`.
- Add skills you have actually used to `profiles/local/skills/skills.md`.
- Add one concise Markdown note per substantial project to `profiles/local/projects/`.
- Add interview-ready context to `profiles/local/firstPersonVoice/`.

Use `career/sourceNoteTemplate.md` when creating a new project or evidence note.

## 4. Update the Generation Rules

Edit `profiles/local/targetResume.md` so its examples and wording match your profile. Replace every starter placeholder with your own values.

The rules should say that the generator must:

- preserve your fixed facts from the skeleton
- use only evidence in your source files
- replace every placeholder
- calculate experience from the dated skeleton roles
- create a new Markdown file and matching PDF
- never use a generated resume as source material

## 5. Check the Scripts

The scripts load name, contact details, filename identity, and source paths from `profiles/local/profile.yml`. Use another profile directory with `--profile` when needed.

## 6. Update the Log

Add a row to `career/updateLog.md` describing your profile changes.

## 7. Generate a Test Resume

Use a real job description or target role and verify that the output contains your name, your contact details, your experience claim, and your supported evidence. Do not publish generated resumes containing private information.
