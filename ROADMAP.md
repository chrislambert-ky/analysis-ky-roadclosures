# Project Consolidation and Retirement Roadmap

## Goal

Consolidate the useful road-closure analysis features and data products into a
destination repository, then retire this repository without losing useful data,
documentation, or project history.

**Destination repository:** TBD

This roadmap is intentionally staged: do not disable the scheduled ETL or delete
this repository until the destination has been validated.

## Phase 1 — Stabilize and document this project

- [ ] Fix the 2022 timestamp assignments in the original notebook, or clearly
  label that notebook as archival and not a source of current results.
- [ ] Confirm the timezone meaning of source timestamps. Normalize timestamps
  consistently before calculating durations, including the 2021 data, and
  update the data dictionary to describe the actual timezone behavior.
- [ ] Make required ETL export failures fail the run; avoid reporting success
  when any required output is missing or stale.
- [ ] Add focused ETL checks for expected year coverage, output columns,
  positive durations, and successful CSV, Excel, and Parquet exports.
- [ ] Document that the latest yearly source file currently contains cumulative
  historical records, and validate that assumption before replacing existing
  cleaned outputs.
- [ ] Choose and document the supported Python version. Align it across the
  GitHub Actions workflow, notebook kernels, and setup instructions.
- [ ] Record tested dependency constraints or a lock file. Clarify whether
  JupyterLab and Notebook are optional dependencies; remove or explain unused
  direct dependencies.
- [ ] Correct the workflow's Eastern-time schedule description and stage only
  the generated data directories.

## Phase 2 — Decide what moves

- [ ] Identify the destination repository and its maintainers.
- [ ] Map each item to a destination location and owner:
  - ETL pipeline and scheduled automation
  - Current analysis notebook(s)
  - Raw, cleaned, and report-ready datasets
  - Data dictionary and setup documentation
  - Power BI file and PDF export
- [ ] Decide whether to retain the original notebook as project history or
  migrate only the refactored analysis.
- [ ] Decide whether to migrate the full data files and Git history, or only
  the latest report-ready outputs and source links.
- [ ] Confirm the destination's data retention, licensing, and repository-size
  requirements before copying large files.

## Phase 3 — Migrate and validate

- [ ] Move the selected code, documentation, and assets to the destination.
- [ ] Update paths, links, workflow configuration, and README instructions.
- [ ] Install dependencies in a clean environment using the documented setup.
- [ ] Run the ETL and notebook analysis in the destination.
- [ ] Verify year coverage, schemas, record counts, and duration calculations
  against the source project.
- [ ] Verify the migrated Power BI report and PDF still open and use the
  intended dataset.
- [ ] Confirm the destination workflow runs successfully and produces the
  expected outputs before cutting over.

## Phase 4 — Retire this repository

- [ ] Disable the scheduled workflow here only after the destination workflow
  is confirmed operational.
- [ ] Remove generated Python cache files and add repository ignore rules.
- [ ] Review `print_section.py` and other one-off development files; remove
  them only if they are not needed for the migration or project history.
- [ ] Replace the README with a brief archived-project notice linking to the
  destination repository and explaining where the datasets and reports moved.
- [ ] Archive this repository to preserve its history and provide a clear
  transition path. Delete it only if there is a separate, explicit decision to
  do so.

## Completion criteria

- The destination repository contains the agreed code, data, documentation,
  and deliverables.
- The destination can be installed and run independently.
- Its scheduled ETL and report outputs have been validated.
- The old scheduled workflow is disabled and this repository clearly points
  users to the destination.
