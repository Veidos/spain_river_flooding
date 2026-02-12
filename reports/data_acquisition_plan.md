# Data acquisition plan — Guadalete pilot

## Scope

- Basin / system: Guadalete (Hidrosur / SAIH)
- Pilot area: Jerez riverside hamlets (El Portal, La Ina, La Greduela)
- Time framing: hydrological years (1 October–30 September)
- Initial historical scope (v0): approximately 5 hydrological years

## Sources and constraints

- Primary source: Hidrosur "Datos a la carta" (manual CSV export).
- Known UI constraint: maximum of 31 days per query (observed).
- Aggregations used:
  - Hourly: level and, where available, discharge.
  - 5-minute (Cincominutal): level only, for event windows around impacts.

## Profiles

Profile A — Baseline history (hourly)

- Goal: multi-year patterns and seasonality.
- Aggregation: hourly.
- Stations: primary river-level station near Jerez (e.g., 212), plus candidate pluviometer(s) if needed.
- Windows: consecutive 31-day queries covering full hydrological years.

Profile B — Event windows (5-minute)

- Goal: detailed dynamics for known impact events.
- Aggregation: 5-minute (level only).
- Stations: same as Profile A, restricted to shorter windows around impact dates.

## Planned windows (to be refined)

- Hydrological years: HY_2021, HY_2022, HY_2023, HY_2024, HY_2025.
- For each hydrological year:
  - Monthly (or 31-day) windows per station and variable (exact list to be filled as we progress).

## Link to policy

- Data access must comply with `docs/data_access_policy.md` (no scraping unless explicitly allowed by provider; manual exports and official open-data endpoints preferred).
