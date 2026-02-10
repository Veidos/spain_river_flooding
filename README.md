# Project name

Short description of the project goal and context.

## Structure

- `data/raw/`: immutable source data.
- `data/processed/`: cleaned / transformed data produced by code.
- `notebooks/`: numbered notebooks by phase (intake, EDA, analysis, reporting).
- `src/`: reusable code (I/O, features, visualization).
- `reports/`: final deliverables and figures.
- `models/`: trained model artifacts (if applicable).

## Requirements

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Quickstart

1. Run `notebooks/01_data_download.ipynb`.
2. Run `notebooks/02_eda.ipynb`.
3. Run `notebooks/03_analysis.ipynb`.
4. Run `notebooks/04_reporting.ipynb`.

## Execution profile (criteria)

This repository is intended for rigorous, reproducible analysis.

- Fill `reports/project_contract.md` at project start.
- Use `docs/quality_standard.md` as the repo Definition of Done.
