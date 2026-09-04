# Source Note Template

Use this template for all files under `projects/` and `firstPersonVoice/` so the local LLM can extract facts consistently and with less ambiguity.

## Required structure

### 1. Title
- Short, descriptive title of the project, workstream, or narrative area.

### 2. Organization
- Name of the employer or business unit.

### 3. Period
- Start and end dates in a consistent format, for example `01/2026 - Present`.

### 4. Role
- Position or responsibility title.

### 5. Business context
- Brief description of the business problem, regulatory need, reporting area, or process context.

### 6. Problem or objective
- What problem was being solved, improved, or supported?
- Keep this outcome-focused and fact-based.

### 7. Responsibilities and contributions
- Use concise bullet points.
- Focus on concrete work performed, not broad narrative.
- Include technologies, data flows, stakeholder collaboration, UAT, production support, or controls when relevant.

### 8. Tools, platforms, and systems
- Record the technologies actually used.
- Keep names accurate and specific.
- Examples: Python, SQL, Airflow, Azure SQL, AKS, Docker, Kubernetes, Power BI, FARMS ETL, Autosys, GitHub Actions.

### 9. Outcomes and value
- Summarize the business or operational value.
- Prefer supported statements such as improved reliability, scalability, automation, control, reporting quality, modernization, or lower infrastructure cost.
- Avoid unsupported ROI claims.

### 10. Evidence or supporting quote
- If relevant, include a short summary quote or evidence sentence.
- Keep it brief and factual.

## Writing rules

- Prefer clear, professional, fact-based language.
- Do not add invented metrics, dates, teams, or technologies.
- Keep bullet points concise and easy for an LLM to parse.
- Use consistent headings across notes.
- Keep the tone close to resume language rather than long-form narrative.

## Example skeleton

# Project or Workstream Title

**Organization:**
**Period:**
**Role:**

## Business context
-

## Problem or objective
-

## Responsibilities and contributions
- 
- 
- 

## Tools, platforms, and systems
- 
- 

## Outcomes and value
- 
- 

## Evidence or summary
- 

## LLM extraction guidance

When a local model reads this note, it should extract facts in the following order:

1. organization
2. period
3. role
4. core problem
5. concrete responsibilities
6. technologies
7. business value
8. supporting evidence

This format keeps source notes compact, consistent, and easier to aggregate into resume-ready content with less drift.
