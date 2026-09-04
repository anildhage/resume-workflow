# Python-Based ETL Data Transformation Application

**Organization:** Societe Generale Investment Banking  
**Period:** 01/2026 - Present  
**Role:** Co-developer / data transformation engineer

## Business context
- The team needed a more flexible and cost-efficient alternative to a legacy third-party ETL tool.
- The solution was designed to support scalable transformation workloads on Azure for reporting and dashboard consumption.

## Problem or objective
- The existing ETL dependency was costly and less flexible for direct business logic changes.
- The objective was to create a Python-based ETL framework on AKS that could ingest diverse sources, apply modular transformation logic, and produce reliable reporting outputs.

## Responsibilities and contributions
- Co-developed the Python ETL framework and reusable transformation capabilities.
- Built and enhanced modular scripts for ingestion, transformation, validation, and loading.
- Migrated business logic from legacy ETL workflows while preserving or improving expected outputs.
- Worked with diverse source formats and integrated outputs into reporting and dashboard data flows.
- Supported UAT, business-request testing, stakeholder sign-off, and production readiness.
- Used SQL and Python to investigate data structures, validate outputs, and troubleshoot transformation issues.
- Used GitHub Copilot to accelerate documentation, code understanding, refactoring, and legacy component adaptation for cloud architecture.

## Tools, platforms, and systems
- Python with Pandas
- Azure Kubernetes Service (AKS)
- Harbor
- Apache Airflow DAGs
- Azure Storage
- Parquet
- Azure SQL
- Docker and Kubernetes
- GitHub-centric CI/CD and deployment automation

## Outcomes and value
- Reduced reliance on a costly third-party ETL tool.
- Lowered idle infrastructure cost by scaling AKS workloads to processing needs and shutting down after completion.
- Improved scalability for hundreds of independent jobs.
- Increased flexibility because business transformations could be implemented directly in code.
- Improved team self-sufficiency and maintainability for new transformation scripts.
- Enabled reliable Parquet and Azure SQL outputs for downstream reporting and dashboards.

## Evidence or summary
- “I co-developed a Python-based ETL application deployed on AKS and orchestrated with Airflow. It ingests data from APIs, databases, files, and Azure Storage, applies modular transformations, and writes Parquet and Azure SQL outputs for reporting. The solution replaced a costly and less flexible ETL dependency, scales processing to the workload, and reduces infrastructure cost by using resources only while transformations are running.”
