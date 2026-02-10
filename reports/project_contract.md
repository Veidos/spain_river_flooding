# Project contract (fill per project)

Fill this file at project start. Its purpose is to lock deliverables and acceptance criteria to prevent unfocused work.

## 1) Objective (decision)

- Decision this work is meant to support:
  - Define measurable flood-generating mechanisms (drivers) for riverine overbank flooding in the initial pilot scope in Spain, and decide what data is required to test those mechanisms observationally (no causal claims by default).
- Primary question:
  - Which combinations of recent precipitation, antecedent wetness/soil moisture proxies (and where relevant, snowmelt and reservoir operations) are associated with sharp increases in river stage/discharge consistent with overbank flooding in the pilot scope?
- Secondary questions (max 3):
  - Which measurable indicators (lags, accumulations, thresholds) best represent each driver in the pilot scope?
  - How does response differ across stations (fast vs slow catchment response) within the pilot scope?
  - What data-quality limitations (provisional data, gaps, sensor changes) constrain the analysis?
- Out of scope:
  - Any prediction/early-warning component and any ML until a target, metric, and validation strategy are defined upfront.
  - Formal causal inference (we use “drivers/mechanisms” as observational framing).

## 2) Data

- Sources:
  - SAIH real-time hydrometeorological and hydraulic variables within the selected basin/SAIH scope (exact endpoints to be documented for the pilot).
  - SAIH-ROEA station metadata (geospatial dataset/service; station locations and descriptive attributes).
- Time cutoff / extraction date:
  - YYYY-MM-DD HH:MM CET (recorded for each ingestion into `data/raw/`).
- Constraints (privacy/licensing):
  - Public-sector sources; confirm terms of use per provider and record them here.
- Unit of analysis (what is one row/observation):
  - Time series: station (control/gauging point) × timestamp.
  - Station metadata: one row per station ID with coordinates and attributes.

## 3) Deliverable(s)

- Primary deliverable (HTML/PDF/table/dataset/dashboard):
  - A “Driver → Observable → Dataset → Resolution” table plus a dataset inventory and data-quality rules for the pilot scope (v0).
- Repo path(s) (e.g., `reports/`):
  - `reports/project_contract.md`
  - `reports/driver_observable_dataset_resolution.md`
- Audience:
  - Technical project team and risk-management stakeholders (clear, audit-friendly wording).
- Language policy:
  - All repository artifacts (reports, notebooks, code documentation) are written in English only. Team communication may be in Spanish, but technical terms and artifact names are referenced in English.
