# Data access policy

## Principle

We only automate data extraction when it is explicitly allowed by the provider (documented API, open-data endpoint, or written permission).
Otherwise, we use manual exports and/or official open-data alternatives.

## Hidrosur (SAIH) web portal

- Access method (v0): manual CSV export via "Datos a la carta" UI.
- Known limitation: max 31 days per query (UI constraint).
- Automation status: TBD (do not implement scraping until terms allow it).

## Audit requirements

- Every acquisition must record: source URL, parameters, extraction timestamp (CET), and local raw path.
- Raw data is immutable and may be gitignored; metadata and code are versioned.
