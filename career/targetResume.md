# Target Resume Generation Instructions

## Purpose

This file is the instruction contract for generating role-targeted resumes. When an API reads this file, it should use these rules to create a new Markdown resume from the fixed resume skeleton and the career information stored in the folders described below.

The generated resume must remain accurate to my experience, relevant to the target role, concise, professional, and compatible with the structure of the skeleton.

## Generation sequence

Follow this order for every resume:

1. Build the content draft from the target role, the fixed skeleton, and verified career evidence.
2. Perform a content-quality review before applying Markdown formatting or keyword emphasis.
3. Apply the final resume structure, heading levels, bolding, spacing, and other presentation rules.
4. Run the final structural and placeholder validation after formatting.

Formatting is the last presentation stage. It must never be used to hide missing content, unsupported claims, weak evidence, or unresolved placeholders.

### Content-quality gate

Before any cosmetic formatting, confirm that the content draft:

- preserves every fixed employer, title, location, date, education, and certification fact from `resumeSkeleton.md`
- contains a synthesized, role-specific summary rather than a copied summary file
- uses only skills and claims supported by the source files
- contains evidence-grounded Société Générale responsibilities and relevant projects
- uses the skeleton-derived experience claim
- replaces every dynamic placeholder
- has complete `CAREER SUMMARY`, `SKILLS`, `WORK EXPERIENCE`, `EDUCATION`, `CERTIFICATIONS`, and `PROJECTS` content

Only after all checks pass may the draft receive heading levels, bolding, spacing, or other cosmetic treatment.

## Inputs

The resume-generation process receives a target role, for example:

- Business Analyst
- Data Analyst
- Data Engineer
- Data and AI Engineer
- Finance Production Support Analyst

The target role determines which career summary, skills, work-experience bullets, and projects are selected. The process must not invent employers, dates, technologies, responsibilities, achievements, metrics, or qualifications that are not supported by the source files.

Before generating a resume, also read `notes/career/profileFacts.md` for stable cross-role positioning. Treat `notes/career/resumeSkeleton.md` as the sole authority for fixed personal facts and dated work history.

## Resume skeleton

Always begin with the file:

`notes/career/resumeSkeleton.md`

The skeleton contains the constant information that must remain unchanged in every generated resume. Copy the following constant sections exactly as they appear in the skeleton:

- Name and contact details.
- Employer names.
- Job titles, employment types, locations, and employment dates.
- Existing fixed work-history details for Professional Career Development, Leopard Systems, and Google India (GlobalLogic Technologies).
- Education.
- Certifications.
- The overall section order and headings, unless a target role requires a clearly labeled and minimal formatting adjustment.

Do not modify, rewrite, or remove the constant information. Only replace the explicit placeholder content described below.

## Dynamic content rules

The skeleton uses the consistent placeholder `- to be updated`. This placeholder indicates content that must be generated for the target role.

Replace only the relevant placeholders. Do not leave placeholder text in the generated resume, and do not alter unrelated constant sections.

### Career summary

For the `CAREER SUMMARY` placeholder, read the files in:

`notes/career/careerSummary/`

Do not copy a single summary file verbatim into the resume. Instead, treat the summary folder as a knowledge base and synthesize a role-specific summary based on the target role, the overall pattern across the available summary files, and the actual evidence in the project and first-person source material.

Use the existing summary files as reference material to understand the common themes, strengths, and phrasing patterns for the target role. Then generate a concise, role-tailored summary for the resume that is grounded in your actual experience and aligned to the job being targeted.

If a summary file for the exact target role already exists, use it as context and guidance, not as a direct copy. If no suitable summary exists for the target role, create a new summary file in `notes/career/careerSummary/` using the same professional style and then use that new summary as the basis for the generated resume.

Available summaries currently include:

- `businessAnalyst.md`
- `dataAnalyst.md`
- `dataEngineer.md`
- `dataAndAIEngineer.md`
- `financeProductionSupportAnalyst.md`

Calculate the experience statement from the dated professional roles in `notes/career/resumeSkeleton.md` using the current date. Use the resulting floor in the format `{calculated years}+ years of experience`. Do not copy an old experience number from another generated resume or summary file. The validator is authoritative if a generated resume and a summary file disagree.

### Skills

For the `SKILLS` placeholder, read:

`notes/career/skills/skills.md`

Select the skills that best match the target role and the requirements of the opportunity. Preserve the category structure from the skills file where practical. Prioritize relevant categories and skills rather than copying unrelated skills into every resume.

Use only skills supported by `skills.md` and the other career source files. Keep skill names clear, searchable, and easy for an ATS or API consumer to parse.

### Resume formatting

Use a natural Markdown resume hierarchy:

- Put `# Anil Dhage` on the first line by itself.
- Put the location, phone, email, and LinkedIn URL on one second line separated by `  |  `.
- Put `---` immediately below the contact line.
- Render `CAREER SUMMARY`, `SKILLS`, `WORK EXPERIENCE`, `EDUCATION`, `CERTIFICATIONS`, and `PROJECTS` as level-two Markdown headings, each on its own line.
- Put all section content below its heading; never place body text on the same line as a section heading.
- Render the selected `SKILLS` entries on one line, separated by `  |  `, without bullet markers.

Use restrained Markdown bolding to improve recruiter scanability:

- Do not bold section headings or the candidate name because their heading levels provide the visual hierarchy.
- Bold employer names, job titles, and project names.
- Review the target job description and identify a small set of high-value matching skills, responsibilities, tools, and domain terms.
- Bold those matching terms only where the resume statement is directly supported by the source files and the term appears naturally in the summary, skills, experience, or project content.
- Prefer approximately 10-15 strategically distributed keyword highlights across the resume; do not bold every occurrence or entire bullet sentences.
- Do not bold unsupported qualifications, inferred experience, or requirements that are only present in the job description.
- Keep the resume readable for human reviewers; bolding is for emphasis and scanning, not keyword stuffing.

### Société Générale work experience

For the placeholder under:

`Societe Generale Investment Banking`

`Business Data Analyst | Contractor | Montreal, Quebec | 04/2023 - Present`

read and synthesize information from all three locations below:

- `notes/career/projects/`
- `notes/career/skills/`
- `notes/career/firstPersonVoice/`

Use these sources to create strong, role-specific resume bullets describing what I did at Société Générale. Select the details that are most relevant to the target role.

The bullets should focus on concrete responsibilities, technologies, business outcomes, production support, data quality, reporting, automation, cloud migration, stakeholder collaboration, and delivery activities where relevant. Use concise resume language rather than essay language. Convert first-person source material into professional resume bullets without changing the underlying facts.

For example:

- For a Business Analyst target, emphasize requirements translation, stakeholder collaboration, KPI definitions, regulatory reporting, UAT, sign-off, and change delivery.
- For a Data Analyst target, emphasize SQL analysis, reconciliation, anomaly investigation, data quality, financial reporting, and insights.
- For a Data Engineer target, emphasize ETL, Python, SQL, APIs, files, Azure, Airflow, AKS, Parquet, Azure SQL, and production-grade pipelines.
- For a Data and AI Engineer target, emphasize Python automation, cloud data workflows, backend services, AI-assisted development, structured and unstructured data, and modernization.
- For a Finance Production Support Analyst target, emphasize incident investigation, production support, batch monitoring, source-feed issues, reruns, root-cause analysis, controlled releases, and post-deployment validation.

Do not duplicate the same bullet with minor wording changes. Prefer a focused set of high-value bullets that fits a professional resume.

### Projects

For the `PROJECTS` placeholder, read the files in:

`notes/career/projects/`

Select the projects most relevant to the target role. Include the project name, organization, period, and concise achievement-focused details supported by the project file. Do not include projects that are unrelated when space or relevance is limited.

The current project files include:

- `pythonBasedEtlDataTransformationApplication.md`
- `frY15AndFr2052aRegulatoryReporting.md`
- `profitAndLossReporting.md`
- `fastApiChangeManagementProcess.md`
- `automatedDataCleanupApplication.md`

Project descriptions should explain the problem or purpose, what I built or co-developed, the technologies involved, and the resulting business value where the source supports it. Do not invent numerical ROI or performance improvements. Use qualitative value such as improved scalability, lower infrastructure cost, faster delivery, better reporting responsiveness, stronger control, or improved data reliability when supported by the source files.

## Writing standards

- Write in polished, concise resume language.
- Use action verbs and past or present tense appropriate to the dates and ongoing work.
- Keep technical names accurate, including SQL Server, Azure SQL, Azure Kubernetes Service (AKS), Airflow, Autosys, FARMS ETL, Python, Pandas, FastAPI, Docker, Kubernetes, Parquet, Power BI, and GitHub Actions.
- Keep regulated-reporting names accurate, including FR Y-15, FR 2052a, and PMPI.
- Preserve the distinction between systemic-risk reporting, liquidity reporting, and internal P&L performance reporting.
- Avoid unsupported claims, inflated metrics, or technologies that do not appear in the source material.
- Do not use first-person pronouns in the final resume bullets unless the skeleton or target format specifically requires them. The source material may be first person, but the generated resume should follow standard professional resume conventions.
- Keep the final output in Markdown.

## Output location and filename

Create every generated resume as a new `.md` file inside:

`notes/career/files/`

Use this exact filename pattern:

`RoleName-FirstLastName-{incrementNumberBasedOnFileCountInThisFolder}.md`

For this profile, use `AnilDhage` for `FirstLastName`. Convert the target role into a filename-safe `RoleName` by removing spaces and punctuation and using PascalCase. Examples:

- `BusinessAnalyst-AnilDhage-1.md`
- `DataEngineer-AnilDhage-2.md`
- `DataAndAIEngineer-AnilDhage-3.md`
- `FinanceProductionSupportAnalyst-AnilDhage-4.md`

Before creating the file, count the existing `.md` files directly inside `notes/career/files/`. The new file’s increment number must be one greater than that count. Do not reuse an existing filename or overwrite an existing resume. If files have gaps in their numbers, still use the count plus one, as specified by this rule.

## Final checks before writing

Before saving a generated resume, confirm that:

1. It was based on `notes/career/resumeSkeleton.md`.
2. Constant skeleton information was preserved.
3. All dynamic placeholders were replaced.
4. The career summary came from `notes/career/careerSummary/`.
5. The skills came from `notes/career/skills/skills.md`.
6. Société Générale bullets were grounded in `projects/`, `skills/`, and `firstPersonVoice/`.
7. Projects came from `notes/career/projects/`.
8. The experience claim matches the value calculated from the dated professional roles in `resumeSkeleton.md`.
9. The output is Markdown and uses the required filename pattern.
10. The output is a new file in `notes/career/files/` and does not overwrite another file.
