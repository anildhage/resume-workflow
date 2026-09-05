# Make This Repository Yours

The repository currently contains Anil Dhage's resume information. That is intentional for the current user. Before using a public copy for yourself, replace the profile content carefully.

## 1. Replace the Resume Skeleton

Edit `career/resumeSkeleton.md` first. Replace:

- name and contact line
- employers and job titles
- employment types, locations, and dates
- education
- certifications

Keep the section names and overall structure. The experience calculator reads dated work entries from this file.

## 2. Replace Profile Facts

Edit `career/profileFacts.md` with your stable professional identity, strengths, and recurring capabilities. Keep this file short. Do not put every project detail here.

## 3. Add Your Evidence

Use the existing folders as a simple evidence library:

- Add role summaries to `career/careerSummary/`.
- Add skills you have actually used to `career/skills/skills.md`.
- Add one concise Markdown note per substantial project to `career/projects/`.
- Add interview-ready context to `career/firstPersonVoice/`.

Use `career/sourceNoteTemplate.md` when creating a new project or evidence note.

## 4. Update the Generation Rules

Edit `career/targetResume.md` so its examples and wording match your profile. Replace the Anil-specific name, contact examples, and filename examples with your own values.

The rules should say that the generator must:

- preserve your fixed facts from the skeleton
- use only evidence in your source files
- replace every placeholder
- calculate experience from the dated skeleton roles
- create a new Markdown file and matching PDF
- never use a generated resume as source material

## 5. Check the Scripts

The current scripts also contain Anil-specific header and filename validation. For a truly reusable public tool, either:

- keep the scripts as a personal version and document that users must replace those values, or
- refactor them to load name, contact details, and filename identity from a profile configuration file.

The second option is the better long-term design. See the main README's portability note before publishing a multi-user version.

## 6. Update the Log

Add a row to `career/updateLog.md` describing your profile changes.

## 7. Generate a Test Resume

Use a real job description or target role and verify that the output contains your name, your contact details, your experience claim, and your supported evidence. Do not publish generated resumes containing private information.
