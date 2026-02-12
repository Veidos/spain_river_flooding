# Project contract — River Flood Risk (Spain) — Guadalete pilot

Fill this file at project start. Its purpose is to lock deliverables and acceptance criteria to prevent unfocused work.

## 1) Objective (decision)

- Decision this work is meant to support:
  - Define measurable flood-generating mechanisms (drivers) for riverine overbank flooding in a pilot reach of the Guadalete River (riverside hamlets of Jerez de la Frontera, Spain) and decide what data is required to test those mechanisms observationally (no causal claims by default).

- Primary question:
  - Which combinations of recent precipitation, antecedent wetness/soil moisture proxies (and, where relevant, reservoir operations) are associated with sharp increases in river stage/discharge consistent with overbank flooding in the Guadalete–Jerez pilot area?

- Secondary questions (max 3):
  - Which measurable indicators (lags, accumulations, thresholds) best represent each driver for the Guadalete–Jerez pilot?
  - How does river response differ across stations (fast vs slow catchment response) within the Guadalete basin near Jerez?
  - What data-quality limitations (provisional data, gaps, sensor changes) constrain the analysis for this pilot?

- Out of scope:
  - Any prediction/early-warning component and any ML until a target, metric, and validation strategy are defined upfront.
  - Formal causal inference (we use “drivers/mechanisms” as observational framing).

## 2) Data

- Sources:
  - SAIH real-time hydrometeorological and hydraulic variables within the Guadalete basin (Hidrosur / SAIH scope; exact endpoints to be documented for the pilot).
  - SAIH-ROEA / Anuario de Aforos station metadata and historical series (where available; station locations and descriptive attributes).

- Time framing:
  - We use hydrological years (1 October–30 September) instead of calendar years for aggregation and reporting.

- Initial historical scope (v0):
  - Target: approximately 5 hydrological years of data for the Guadalete–Jerez pilot (to be extended later if needed).

- Time cutoff / extraction date:
  - YYYY-MM-DD HH:MM CET (recorded for each ingestion into `data/raw/`).

- Constraints (privacy/licensing):
  - Public-sector sources; confirm terms of use per provider (Hidrosur, SAIH-ROEA, etc.) and record them here.
  - Automation of data access (scripts) is only implemented when explicitly allowed by the provider; otherwise, manual CSV exports and official open-data endpoints are used.

- Unit of analysis (what is one row/observation):
  - Time series: station (control/gauging point) × timestamp.
  - Station metadata: one row per station ID with coordinates and attributes.
  - Impact records (press/official reports): one row per impact event × source URL.

## 3) Deliverable(s)

- Primary deliverable (HTML/PDF/table/dataset/dashboard):
  - A “Driver → Observable → Dataset → Resolution” table plus a dataset inventory and data-quality rules for the Guadalete–Jerez pilot (v0).
  - A documented event framework for the pilot (hazard vs impact events) and at least one processed dataset linking hydrological series to a basic event inventory.

- Repo path(s) (e.g., `reports/`):
  - `reports/project_contract.md`
  - `reports/driver_observable_dataset_resolution.md`
  - `reports/guadalete_jerez_event_definition.md`
  - `reports/data_acquisition_plan.md`
  - `reports/data_intake_log.md`

- Audience:
  - Technical project team and risk-management stakeholders (clear, audit-friendly wording).

- Language policy:
  - All repository artifacts (reports, notebooks, code documentation) are written in English only. Team communication may be in Spanish, but technical terms and artifact names are referenced in English.
