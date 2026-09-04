# Automated Data Cleanup Application

**Organization:** Societe Generale Investment Banking  
**Period:** 12/2023 - 03/2024  
**Role:** Data automation developer

## Business context
- Reporting performance was degrading because production databases were accumulating historical data no longer required in active reporting views.
- The solution was needed to reduce database volume without losing access to business-critical historical information.

## Problem or objective
- Active reporting views were carrying excessive historical records, which slowed report refreshes and reduced dashboard responsiveness.
- The objective was to create a controlled archive-and-cleanup workflow that preserved required data while improving reporting efficiency.

## Responsibilities and contributions
- Analyzed the relationship between database volume and reporting performance.
- Designed an archive-before-delete workflow to remove unnecessary records while retaining required history.
- Implemented configurable retention behavior based on business-controlled mappings.
- Automated the cleanup process after reporting cycles.
- Supported validation of retained, archived, and removed records.
- Ensured the cleanup process preserved access to required business data.

## Tools, platforms, and systems
- Microsoft SQL Server
- Business-controlled mapping configuration
- Automated reporting-cycle execution

## Outcomes and value
- Improved report refresh times and dashboard responsiveness.
- Reduced active production data volume.
- Prevented uncontrolled deletion by placing retention decisions into controlled configuration.
- Maintained access to business-critical historical information through a separate archive.
- Reduced recurring manual database-maintenance effort.

## Evidence or summary
- “I built an automated cleanup application to address slow reporting caused by oversized SQL Server databases. The process archives older records to a separate database and removes only records identified as unnecessary through business-controlled mappings. This improved report and dashboard performance while preserving access to important historical data.”
