# Guadalete (Jerez riverside hamlets) — Event definition (minimal v0)

## 0) Purpose

Define a **minimal, measurable** event framework to start data extraction and basic EDA.

We separate the following concepts.

- **Hazard**: what the river does (measured time series)
- **Impact**: human/economic consequences in the pilot area (record-based)

This is an observational project (“drivers/mechanisms”), not formal causal inference.

## 1) Spatial scope (impact geography)

In scope (pilot v0).

- El Portal
- La Ina
- La Greduela

Out of scope (v0).

- Any area outside these hamlets unless explicitly added later

## 2) Unit of analysis (required to proceed)

- Hazard time series: `station_id × timestamp` (one row = one measurement at one time)
- Impact records: `impact_event_id × source_url` (one row = one sourced claim/record)

## 3) What counts as an event (minimal)

### 3.1 Hazard event (TBD until we see data)

A hazard event will be defined from a river time series using the following parameters.

- Variable: TBD (stage H in meters, or discharge Q in m³/s)
- Threshold: TBD
- Minimum duration above threshold: TBD
- Separation rule (gap under threshold to start a new event): TBD

Note: We do not set thresholds before downloading at least one sample time series.

### 3.2 Impact event (usable immediately)

An impact event exists if at least one **hard signal** is reported for the pilot area.

- Evacuations/relocations > 0, or
- Injuries/fatalities > 0, or
- Quantified economic/material losses, or
- Critical service disruption (e.g., road closure, water/electric outage) explicitly linked to river flooding

Evidence grading (press-based).

- A: official source and/or multiple independent sources with consistent quantitative details
- B: reputable media source with at least one quantitative detail
- C: narrative mention without quantification (stored as a mention; not counted in the main event total)

## 4) Immediate deliverables (v0)

- This document (event definition)
- A raw CSV for impact events (A/B only) and optionally a second CSV for mentions (C)

## 5) Open decisions (max 5)

1) Select the primary hazard data source (SAIH portal/service endpoint)
2) Select the primary station_id for Guadalete near Jerez
3) Confirm which hazard variable(s) are available (H and/or Q) and their units
4) Decide hazard threshold(s) after seeing distributions and known impacted dates
5) Decide linkage window between hazard and impact (e.g., ±24–48h)
