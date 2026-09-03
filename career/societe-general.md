# Societe Generale Regulatory & PMPI Projects – April 09, 2026

## Role overview at Société Générale

- **Title:** Business Analyst / Tech BA for U.S. regulatory reporting and performance management at **Société Générale (SG)**.
- **Scope:** Support U.S.-based business users on **regulatory filings (FR Y‑15, FR 2052a)** and **performance management / P&L reporting (PMPI)** by owning data analysis, build data pipelines and transformations, and technical change delivery.
- **Teams:** Hybrid setup with **Bangalore** and **Montreal**, working closely with **BAs, UI devs, backend devs**, and U.S. business stakeholders.

***

## Project landscape – quick map

| Project      | Regulator / Audience                                | Business Purpose                                                                                          | Frequency (typical) | My Role Focus |
|-------------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------|---------------|
| **FR Y‑15** | U.S. Federal Reserve                                 | Systemic risk reporting for large banking organizations and GSIBs, supports capital surcharge and risk monitoring.[1][2][3] | Quarterly            | GL & balance data analysis, issue triage, ETL changes, production support |
| **FR 2052a**| U.S. Federal Reserve                                 | Liquidity risk monitoring via detailed cash flows, funding, collateral, and maturity buckets.[4][5][6][7]            | Daily / monthly (by firm size)[7] | Liquidity data quality checks, source gap analysis, ETL/process fixes |
| **PMPI**    | SG internal senior management (MARK, GLBA, GTPS)     | Daily **P&L and NBI performance management** vs budget (Daily Flash, Mark Exco, GLBA, GTPS reports).[8][9][10]           | Daily                | Lead BA + ETL dev for P&L reporting, variance analysis, and report automation |

***

## FR Y‑15 – Systemic Risk Reporting

### Business context (what FR Y‑15 is and why it exists)

- **FR Y‑15** is the **Banking Organization Systemic Risk Report**, a quarterly filing to the U.S. Federal Reserve by large U.S. bank holding companies, covered savings and loan holding companies, foreign banking organizations with significant U.S. assets, and U.S. institutions designated as **global systemically important banks (GSIBs)**.[1][2][3]
- The report collects indicators across **size, interconnectedness, substitutability, complexity, cross‑jurisdictional activity, and short‑term wholesale funding**, which are used to assess systemic risk and to calculate any **GSIB capital surcharge**.[2][1]
- FR Y‑15 data helps the Fed **monitor systemic risk profiles, identify institutions that may pose systemic risk, and analyze mergers/acquisitions from a financial stability perspective**.[1][2]

### My responsibilities on FR Y‑15

- Act as **technical BA** between U.S. business users and the technical teams, focusing on **journal balances, balance sheet data, GL data, and other financial metrics** feeding FR Y‑15.
- Perform **root-cause analysis** whenever business users find:
  - Inconsistent values in reports.
  - Missing or late data from specific sources.
  - Incorrect balances or unexplained movements in systemic risk indicators.
- Provide **written justifications** to business users:
  - Explain whether issues are due to upstream source delays, mapping errors, process failures, or expected business events.
  - Confirm if there are any **blocking issues** before reporting cycles start.
- When analysis shows a structural issue, drive the full change lifecycle:
  - **Design / spec change** to ETL, mappings, or calculations.
  - Coordinate **DEV → UAT** changes, manage user sign-off, and support **production deployment**.
  - Validate that post‑release reports are accurate and aligned with business expectations.

### Typical FR Y‑15 workflow (for talking in the interview)

1. **Daily / periodic data ingestion**
   - **Sources:** GL systems, transaction systems, balance sheet data, and other regulatory data feeds.
   - **Landing:** On‑prem **MS SQL Server** data store (heavily used, loaded daily).
   - **Formats:** APIs, CSV, and other file formats processed via scheduled ETL jobs.
2. **Job orchestration & monitoring**
   - Use **Autosys** to schedule and monitor daily loads and transformations.
   - Track job statuses to ensure required data is available **before business sanity checks** and reporting windows.
3. **Business pre-checks**
   - U.S. business teams run **sanity checks** and compare current period indicators vs historical trends and expectations.
   - They raise queries when they see unexpected spikes, drops, or missing data.
4. **Analysis & issue resolution**
   - Investigate in SQL:
     - Compare reported numbers vs raw GL/journal entries.
     - Check if all **sources arrived** and were processed.
     - Look for **mapping gaps**, **currency/FX issues**, or **double-counting**.
   - Summarize findings and propose fixes or workarounds.
5. **Change delivery (if needed)**
   - Implement ETL or transformation changes (e.g., in **FARMS ETL** when used).
   - Coordinate **DEV/UAT**, produce evidence, and get **user sign-off**.
   - Support production release and **post‑go‑live validation**.

### Tech stack used on FR Y‑15

- **Database:** On‑prem **MS SQL Server** storing daily GL, balances, and transactional data.
- **ETL / data transformation:** **FARMS ETL** where applicable (SG’s data factory-style tool covering sourcing, transformation, validation, and loading).
- **Scheduling & monitoring:** **Autosys** for batch orchestration, alerting on failures, and confirming all daily loads completed.
- **Reporting front-ends:** SG internal platforms such as **SG Markets**, **MicroStrategy**, and **Power BI** for consumption by U.S. business teams.
- **Languages / tools:**
  - **SQL** for heavy analysis and reconciliation.
  - **Python** for advanced checks, data quality tooling, and ad‑hoc analysis.
  - **Unix shell scripting** for file handling, process automation, and log analysis.
  - Handling of **business dates and holiday calendars** to ensure correct cut‑off dates and reporting windows.

***

## FR 2052a – Liquidity Monitoring

### Business context (what FR 2052a is and why it exists)

- **FR 2052a** is the **Complex Institution Liquidity Monitoring Report**, a key Federal Reserve filing focused on the **liquidity profile** of large, complex institutions.[4][5][6]
- It collects detailed **cash inflows, outflows, funding sources, collateral, and contingent liabilities** across business lines and legal entities to allow supervisors to monitor a firm’s ability to meet obligations and withstand stress events.[5][6][7][4]
- Data is segmented into **maturity buckets** (e.g., 1 day, 30 days, >1 year) and broad funding classifications (secured/unsecured, wholesale/retail, etc.), which feed metrics like **liquidity coverage ratio (LCR)** and **net stable funding ratio (NSFR)** used in supervisory oversight.[7][11][5]

### My responsibilities on FR 2052a

- Support U.S. business and risk teams by ensuring **liquidity data** (cash flows, positions, collateral) is correctly sourced, transformed, and available for reporting.
- Investigate cases where:
  - Certain **products or positions** do not appear in the report.
  - Maturity profile or notional balances appear inconsistent with underlying systems.
  - Aggregations by **time bucket or product type** do not reconcile.
- Perform data analysis similar to FR Y‑15:
  - Check completeness of **daily and monthly source loads**.
  - Validate mappings of products to correct **FR 2052a categories and buckets**.
  - Coordinate fixes in ETL / processes when errors are structural.

### Setup and workflow (shared with FR Y‑15)

- **Same data platform:** On‑prem **MS SQL Server** with daily loads of transactional and position data.
- **Same orchestration:** **Autosys** to manage ETL job chains and confirm that all relevant liquidity data sources are processed before reporting.
- **Same reporting channels:** Data ultimately consumed through SG reporting platforms (SG Markets, MicroStrategy, Power BI) for internal teams, and aggregated into the official FR 2052a submission.
- **Same working model:** Joint support between **Bangalore and Montreal**, rotating production support coverage for U.S. time zones.

### Interview phrasing for FR Y‑15 vs FR 2052a

You can summarize the difference like this:

- **FR Y‑15:** “I support the Fed’s **systemic risk reporting** for SG’s U.S. operations, focusing on balance sheet, GL, and exposure data that feeds the FR Y‑15 report, which the Fed uses to monitor GSIB risk profiles and calibrate capital surcharges.”[3][2][1]
- **FR 2052a:** “I also support **liquidity risk reporting** under FR 2052a, ensuring that detailed cash flows, funding, and collateral data are correctly captured across time buckets so supervisors can assess our liquidity resilience under stress.”[6][4][5][7]

***

## PMPI – Performance Management & P&L Reporting

### Business context (performance management in banks)

- Banks use **enterprise performance management (EPM)** systems to handle **budgeting, forecasting, management reporting, profitability analysis, and funds transfer pricing (FTP)** across products and channels.[8]
- Instead of manual spreadsheets, modern EPM setups centralize data and calculations, generate **average balances**, and provide **self‑service reporting** and drill‑downs for business leaders.[8]
- **Daily flash reporting** is widely used in banks to give management an early, approximate view of **P&L, balance sheet, and sales trends**, long before final month‑end numbers are closed.[9]

Your **PMPI** project fits exactly into this EPM / daily flash space for SG’s U.S. activities.

### Business units: MARK, GLBA, GTPS

- **MARK (Global Markets)** – trading and markets business, responsible for a large portion of U.S. **Net Banking Income (NBI)**.[10]
- **GLBA (Global Banking & Advisory)** – corporate and investment banking activities including structured finance and advisory.[10]
- **GTPS (Global Transaction & Payment Services)** – payments, cash management, and correspondent banking for SG affiliates and clients.[10]

These business lines generate NBI and P&L that your PMPI system aggregates into **Daily Flash, Mark Exco, GLBA, and GTPS** management reports.

### What PMPI does (from your perspective)

- **Purpose:** Provide **daily, MTD, QTD, and YTD P&L / NBI** views for each **business unit (MARK, GLBA, GTPS)** and sub‑business units, compared against **allocated budgets**.
- **Outputs:**
  - **Daily Flash Report:** High‑level performance snapshot across key business units (P&L, NBI, variances vs budget).
  - **Mark Exco Report:** More granular view for the MARK business line, tailored to executive committee consumption.
  - **GLBA & GTPS reports:** Similar structures focused on their respective portfolios.
  - **End-of-day PPT snapshots:** Automated slide outputs summarizing the day’s performance for management distribution.
- **Key metrics:**
  - **DTD (Day‑to‑Date)** P&L.
  - **MTD/QTD/YTD** cumulative P&L and NBI.
  - **Average balances** by business unit and sub‑unit.
  - **Budget allocation and prorations** on a daily basis.
  - **Variance analysis:** actual vs prorated budget, both in absolute and percentage terms.



This shows the kind of **daily aggregation and variance logic** you own in PMPI.

### My responsibilities on PMPI

- **Lead BA and data transformation developer** for PMPI:
  - Translate management reporting needs into **data models, metrics, and report layouts**.
  - Work closely with a dedicated **UI developer** to design and maintain front‑end dashboards and PPT outputs.
- Own end‑to‑end **ETL pipelines** (on **FARMS ETL**) for P&L/NBI reporting:
  - Ingest daily P&L feeds from MARK, GLBA, and GTPS.
  - Apply transformation logic for **DTD, MTD, QTD, YTD**, average balances, and budget prorations.
  - Implement **variance calculations** and aggregation by BU and sub‑BU.
- Ensure **data quality and completeness**:
  - Check that all relevant sub‑business units send feeds on time.
  - Handle **late or missing submissions**, reruns, and corrections.
  - Coordinate fixes in mapping/configuration when business restructures or new desks appear.
- Deliver **daily automated outputs**:
  - Generate reports and **PPT snapshots** at end‑of‑day.
  - Support business questions on **variances vs prior periods or budget** and adjust logic when required.

### PMPI architecture (in your words)

- **Source ** Daily P&L/NBI files or feeds from MARK, GLBA, GTPS sub‑business units.
- **ETL engine:** **FARMS ETL** orchestrating:
  - Sourcing (file/API ingestion).
  - Transformation (aggregations, calculations, validations).
  - Loading into reporting data marts.
- **Reporting layer:**
  - Data exposed to **SG Markets** and other reporting channels.
  - Automated generation of **Daily Flash**, **Mark Exco**, and other BU‑specific reports and PPTs.

***

## Common data platform & tooling across projects

### Core stack

- **Database:** Heavily used **on‑prem MS SQL Server** as the main regulatory and management reporting store.
- **ETL:** **FARMS ETL** as a “data factory” style tool supporting end‑to‑end flows from sourcing to validation and reporting for both regulatory (FR Y‑15, FR 2052a) and PMPI use cases.
- **Scheduling:** **Autosys** for:
  - Defining dependencies and calendars.
  - Triggering batch jobs (ingestion, transformation, reporting).
  - Sending alerts on failures or long‑running processes.
- **Reporting tools:** **SG Markets**, **MicroStrategy**, and **Power BI** for dashboards, ad‑hoc analysis, and distribution to U.S. business users and SG management.
- **Tech skills used daily:**
  - **SQL** for debugging balances, reconciling GL/journal vs reports, and complex joins on large datasets.
  - **Python** for advanced analysis, automation, and prototyping new checks.
  - **Unix shell** for file/system operations, log analysis, and integration with batch jobs.
  - **Business calendar logic** to correctly handle U.S. holidays, month‑end, and quarter‑end cut‑offs.


***

## Data governance – what you are already doing

### What data governance means in banking

- In banking, **data governance** is the framework of **policies, processes, and standards** that ensure data is **accurate, secure, consistent, and compliant with regulatory standards** across the organization.[12][13]
- A strong governance framework covers **data quality, lineage, access controls, metadata, and regulatory compliance**, making sure that critical reports (like FR Y‑15 and FR 2052a) can be traced back to reliable sources.[13][14][15][12]
- For regulatory reporting, regulators increasingly expect banks to demonstrate **front‑to‑back data quality, clear ownership, and transparent controls** over the data used in their filings.[14][15][16]

### How your current work maps to data governance

You are already doing a lot of **data governance work subconsciously**. You can reframe it as:

| Data Governance Area           | What it means in banking                                                                                   | What you currently do (how to phrase it) |
|--------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------|
| **Data quality management**    | Ensure data is accurate, complete, and fit for regulatory and management reporting.[12][13]        | Perform **root‑cause analysis** on data quality issues (missing feeds, incorrect balances, mapping errors) and drive permanent fixes. |
| **Data lineage & traceability**| Ability to trace reported figures back through systems and transformations to original sources.[15][16] | Trace FR Y‑15, FR 2052a, and PMPI figures back to GL, P&L, and transactional data via SQL and ETL flows, documenting findings for business users. |
| **Controls & attestation**     | Controls, reconciliations, and sign‑offs that support regulatory and management attestation.[15][16] | Support **pre‑report sanity checks**, validate numbers before reporting windows, and provide written justifications used by business to sign off on submissions. |
| **Change management**          | Controlled changes to data definitions, mappings, and processes with testing and approvals.[14][15] | Manage **DEV/UAT/PROD** changes in ETL and reporting logic, ensure user UAT, and confirm post‑deployment data integrity. |
| **Metadata & definitions**     | Common definitions for metrics, products, and attributes to ensure consistency.[12][13]            | Maintain and evolve the **definitions of KPIs** (P&L, NBI, DTD/MTD/QTD/YTD, budgets, variance) with business stakeholders. |
| **Regulatory compliance**      | Align data and reports with regulatory instructions and expectations.[14][12][13]               | Implement and maintain data transformations that respect **FR Y‑15** systemic risk indicators and **FR 2052a** liquidity classification schemes. |

### How to describe your data governance work in the interview

You can say things like:

- “Although my title is Business Analyst, a large part of my role is **data governance for regulatory and performance reporting**. I ensure that the data feeding FR Y‑15, FR 2052a, and PMPI is **complete, reconciled, and traceable** end‑to‑end.”[12][13][14]
- “I work on **front‑to‑back data quality**, from source system loads through ETL to final reports, and I coordinate with business users to document issues and sign‑offs before submissions.”[15][16][14]

### Data governance skills to polish

Areas you can explicitly grow into:

- **Formal data lineage documentation:** Using tools or diagrams to formally capture **source → transformation → report** flows.
- **Metadata and data cataloging:** Structuring definitions for KPIs, dimensions, and data elements in a centralized catalog.
- **Control frameworks:** Designing standard **reconciliation checkpoints, threshold‑based alerts, and data quality dashboards** for regulatory and PM reporting.[16][15]
- **Policy-level understanding:** Reading more on **regulatory expectations for data governance** in banking so you can reference them confidently.[13][14][12]

***

## Azure cloud migration – how it fits into your story

### Why banks move from on‑prem to Azure

- Financial institutions adopt cloud platforms like **Microsoft Azure** to gain **agility, scalability, and cost efficiency** beyond what on‑premises setups can provide.[17][18]
- Studies show that banks migrating workloads to cloud have realized **infrastructure cost reductions, higher ROI, and fewer security incidents** compared to purely on‑prem environments.[18][19][17]
- Azure offers built‑in **security, compliance, resilience, and disaster recovery**, which align well with banking regulatory expectations for uptime and data protection.[19][20][17][18]

### How to position your migration work

Your migration story:

- You are involved in moving **regulatory and performance reporting applications** from **on‑prem MS SQL + batch ETL** to **Azure‑based architectures**.
- Drivers you can cite:
  - **Cost optimization:** Reduce the cost of running and maintaining on‑prem data centers and hardware.[20][17]
  - **Scalability:** Handle larger data volumes and more frequent reporting without capacity constraints.[17][18]
  - **Modern data & AI capabilities:** Enable future use of **cloud‑native analytics and AI** on regulatory and P&L datasets.[21][18][19][17]
  - **Improved resilience & governance:** Use Azure’s built‑in **security, compliance, and monitoring** to strengthen data governance and operational resilience.[18][19][17]
- Talking point:  
  “We are progressively migrating our FR Y‑15, FR 2052a, and PMPI workloads from on‑premise MS SQL and legacy schedulers to Azure‑based services to improve scalability, reduce infrastructure costs, and leverage modern data governance and monitoring capabilities.”

***

## Interview-ready narratives (how to talk about your experience)

### 1. FR Y‑15 incident handling story

- **Situation:** Before a quarterly FR Y‑15 run, U.S. business users flagged an unexpected spike in a systemic risk indicator for a specific product line.
- **Task:** You had to quickly determine whether this was:
  - A real business movement.
  - A data quality issue.
  - A mapping or process failure.
- **Action:**
  - Used **SQL** to compare the FR Y‑15 output vs GL balances and underlying journal entries.
  - Verified **Autosys job statuses** and source file arrival; identified that one source file was delayed but a previous day’s file had been reused.
  - Worked with the ETL team to **reprocess the day with the correct file** and updated mappings where needed.
  - Coordinated with business to rerun **sanity checks** and documented the root cause.
- **Result:** The corrected report removed the artificial spike, and you implemented an additional **control** to prevent reuse of stale files in future.

### 2. FR 2052a liquidity profile correction

- **Situation:** Business noted that short‑term funding outflows appeared materially understated in the FR 2052a report.
- **Task:** Validate whether some products were being booked into the wrong **maturity bucket** or excluded.
- **Action:**
  - Checked **source system feed completeness** and ensured all relevant products were loaded.
  - Analyzed **mapping rules** from product codes to FR 2052a categories and time buckets, using SQL to see which records were missing or mis‑bucketed.
  - Updated transformation logic (e.g., in FARMS ETL) so these products flowed into the correct **liquidity buckets**, then coordinated UAT and sign‑off.
- **Result:** The liquidity profile became more accurate, supporting better supervisory monitoring and internal risk management.[4][5][6][7]

### 3. PMPI Daily Flash improvement story

- **Situation:** Management wanted clearer **variance vs budget** views in the Daily Flash and Mark Exco reports.
- **Task:** Enhance the PMPI process to show **DTD/MTD/QTD/YTD performance vs daily prorated budgets**.
- **Action:**
  - Designed **calculation logic** for daily budget prorations based on annual or monthly budgets.
  - Implemented transformations in **FARMS ETL** to compute cumulative P&L and NBI, average balances, and **variance metrics** by BU and sub‑BU.
  - Worked with the UI dev to update report layouts and **end‑of‑day PPT snapshots**.
- **Result:** Management received **more intuitive daily performance views**, with early warning on under‑performance vs budget, improving decision‑making.[9][8]

***

## Resume bullet ideas (business-focused, ≤ 2 lines each)

You can adapt these directly into your CV under **Société Générale – Business Analyst / Data Analytics**.

- Led **regulatory reporting support** for U.S. operations on **FR Y‑15 systemic risk** and **FR 2052a liquidity monitoring**, performing deep data analysis on GL, balance sheet, and liquidity data to resolve discrepancies before filings.[2][3][5][6][7][1][4]
- Owned end‑to‑end **PMPI performance management** reporting for MARK, GLBA, and GTPS, designing and implementing DTD/MTD/QTD/YTD **P&L and NBI** calculations and automated Daily Flash / Exco reports consumed by senior management.[8][9][10]
- Designed and implemented **ETL pipelines on FARMS ETL** and on‑prem **MS SQL** to ingest multi‑source financial data (APIs, CSVs, files), with **Autosys** orchestration and monitoring to ensure timely, complete data loads for reporting.  
- Collaborated with U.S. business users to define and refine **KPIs, budget prorations, and variance metrics**, translating management requirements into robust data models and production‑grade reporting solutions.  
- Performed **front‑to‑back data quality investigations**, tracing reported figures back to GL and transactional systems, delivering root‑cause analyses and driving DEV/UAT/PROD changes to permanently fix systemic issues.  
- Contributed to SG’s **data governance** by strengthening data lineage, reconciliations, and sign‑off processes for regulatory and performance reports, ensuring traceability and transparency of key financial metrics.[14][15][16][12][13]
- Supported the **migration of regulatory and performance reporting workloads** from on‑prem MS SQL to **Azure‑based platforms**, helping improve scalability, cost efficiency, and readiness for advanced analytics.[19][20][21][17][18]

***

## Quick checklist for interview

- Be ready to clearly explain **what FR Y‑15 and FR 2052a are** and why they matter to the Fed.
- Emphasize your **data investigation, root‑cause analysis, and change management** skills on regulatory data.
- For PMPI, stress the **business value**: daily management insights, early warning via **Daily Flash**, and performance vs budget for MARK, GLBA, GTPS.
- Explicitly call out your **data governance contribution** (quality, lineage, controls, and sign‑offs) even if your title is “Business Analyst”.
- Link your **Azure migration** experience to modernizing regulatory and performance reporting, and enabling future analytics and AI use cases.
- My expertise:
  - Python development:
      I primarily work on using Python to eliminate manual processes and improve efficiency across data workflows. In my current role, I identify tasks that require repetitive manual intervention and convert them into automated scripts or end-to-end workflows. The goal is always to save time, reduce errors, and modernize how data processes are handled.
      A significant part of my work involves enhancing and migrating ETL workflows. I upgrade existing pipelines to newer platforms by implementing Python-based transformations, while preserving or improving the underlying business logic. In cases where our existing ETL tools have limitations, I design and build custom Python-driven workflows to fill those gaps.
      I also develop backend services using frameworks like Flask and FastAPI to support internal applications or data services. Additionally, I’ve worked on extracting and processing data from unstructured sources—such as various file formats or raw inputs—by building custom parsing and scraping scripts, and then integrating that data into ETL pipelines for downstream reporting and analytics.
      Overall, I focus on using Python as a flexible tool to solve complex data challenges, especially in situations where traditional tools fall short.
  - ETL developments and python ETL tool:
      I’ve built over 100 ETL processes, handling everything from ingesting structured and unstructured data from files, APIs, and databases to performing filtering, aggregations, computed fields, looping, and distribution to multiple target applications.
      This has given me deep expertise in designing and implementing ETL pipelines both conceptually and technically, while also taking on full data engineering responsibilities.
      To address limitations in our existing ETL tool—like performance issues and dependency on another team’s support for troubleshooting and servers—I collaborated with developers to co-build a flexible, Python-based ETL solution.
      This tool lets us handle any business transformation in code, much like a traditional ETL platform but with full programmatic control, deployed on Azure Kubernetes Service (AKS) and orchestrated via Airflow DAGs.
      For each run, we pull a container image from Harbor into AKS, spin it up scalably using only the needed resources, process the data, then shut it down to free memory—saving costs since Azure resources idle when not transforming data.
      We’re continually enhancing it with new scripts as our needs grow, making our team fully self-sufficient.
  - SQL analysis.
  - Data ingestion for SG Markets and dashboards.
  - what are the things you built or co developed and how its providing value, what is their ROI
- AI at work:
  - How I use AI to support coding, analysis, and documentation.
  - data governance 
    data governance is basically the process of ensuring that all data in an organization/project is layered within  different pillars where we have data quality, security, privacy, compliance, etc.







