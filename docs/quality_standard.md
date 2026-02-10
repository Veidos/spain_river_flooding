# Quality standard (Definition of Done)

This document defines the non-negotiable minimum required to consider a project “done” from a repository quality standpoint.

## Principles

- Reproducibility: a third party can regenerate results using the repository and the declared environment.
- Traceability: every relevant result has an identifiable origin (data → transformation → output).
- Auditability: assumptions, limitations, and decisions are documented.

## Definition of Done (DoD) — checklist

### Repository and environment

- [ ] The repo includes a `README.md` with: objective, environment setup, and how to run the minimal workflow.
- [ ] The environment is declared (`requirements.txt` or `environment.yml`) and can be installed without opaque manual steps.
- [ ] `.gitignore` excludes large/derived artifacts (by default `data/` and `models/`) and local environment files.
- [ ] Language policy is enforced: all repository artifacts are English-only (docs, reports, notebooks, code documentation).
- [ ] Commit messages are English-only and follow an agreed convention (Conventional Commits recommended).

### Data

- [ ] `data/raw/` is treated as immutable (no manual edits).
- [ ] `data/processed/` is produced only via reproducible code (notebooks + functions in `src/`).
- [ ] Data provenance is documented: source, extraction date / time cutoff, and usage/licensing constraints if applicable.

### Code and notebooks

- [ ] Notebooks are numbered by phase and can be executed in a reasonably linear way.
- [ ] Repeated or critical logic lives in `src/` (not copy-pasted across notebooks).
- [ ] Functions in `src/` follow single responsibility (I/O, features, visualization) with clear naming.

### Results and delivery

- [ ] At least one deliverable exists in `reports/` (report or equivalent) answering the project’s primary question.
- [ ] Final figures are saved by code into `reports/figures/` and are regenerable.
- [ ] The report includes: objective, methodology, results, limitations, and next steps.

## Stop-and-fix signals

- Results exist only “on screen” or were exported manually.
- Transformations are not traceable (unclear what generated `data/processed`).
- Dependencies are not declared or the environment cannot be recreated.
- Mixed-language artifacts exist (English/Spanish in the same document or across repository artifacts).
