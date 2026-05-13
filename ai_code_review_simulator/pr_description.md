# Pull Request: Add User Activity Log Export Feature

## Summary
This PR implements a new logging and export module that allows administrators to export system activity logs into JSON and CSV formats. It also includes a date-filtering mechanism to generate specific time-bound reports.

## Changes
- **Added `LogExporter` class**: A core utility for handling data transformation.
- **Implemented `filter_by_date()`**: logic to allow granular log analysis.
- **Export Formats**: Added support for both structured `JSON` and spreadsheet-friendly `CSV` outputs.
- **Directory Management**: Added automatic creation of an `/exports/` directory to store generated files.
- **Unit Tests**: Added 5 new tests in `tests/test_exporter.py` covering format validation and empty data handling.

## Context
This feature addresses the need for compliance reporting. Previously, logs were only viewable in raw text format, making it difficult for stakeholders to perform audits.

~120 LOC. Related issue: #58.
