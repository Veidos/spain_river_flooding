# Data Intake Log

## Entry 1 - Anuario de Aforos Guadalquivir - 2026-02-17

### Source

- **Provider**: Confederación Hidrográfica del Guadalquivir (CHG)
- **Dataset**: Anuario de Aforos (historical gauging stations data)
- **URL**: <https://www.chguadalquivir.es/saih/DatosHistoricos> (or specific source if different)
- **Extraction date**: 2026-02-17 (approximate)
- **Format**: Multiple CSV files (semicolon-separated, latin1 encoding)

### Files ingested

Local path (gitignored): `data/raw/GUADALQUIVIR_DATA/`

| File | Rows (approx) | Purpose | Status |
| ------ | --------------- | --------- | -------- |
| `afliq.csv` | ~357k | Daily river stage & discharge | **CORE - pilot** |
| `estaf.csv` | ~100 | Station metadata (location, catchment) | **CORE - pilot** |
| `anuala.csv` | ~5k | Annual statistics | Secondary (validation) |
| `extremosaav.csv` | ~3k | Corrected annual maxima | Secondary (validation) |
| `afliqc.csv` | - | Daily canal data | Out of scope v0 |
| `afliqi.csv` | - | Instantaneous peaks | TBD (if needed for event definition) |
| `afliqe.csv` | - | Reservoir data | TBD (if upstream of Jerez) |

### Data quality issues identified

1. **Encoding**: Files require `encoding='latin1'` (UTF-8 fails with UnicodeDecodeError at byte 0xd1).
2. **Column structure differs**:
   - Daily tables (AFLIQ): `indroea`, `fecha`, `altura`, `caudal`
   - Annual tables (ANUALA, EXTREMOSAAV): `indroea`, `anohidr` (no `fecha`)
3. **Numeric parsing**: All numeric columns initially read as object dtype, require explicit conversion.

### Decisions

- **Pilot scope**: Use AFLIQ (daily series) + ESTAF (station metadata) only.
- **Station selection**: TBD - pending identification of `indroea` for Guadalete-Jerez station.
- **Temporal scope**: Full available range in AFLIQ (dates to be confirmed after station selection).
- **Validation**: ANUALA/EXTREMOSAAV reserved for validating event detection (compare calculated annual maxima vs. reported corrected maxima).

### Processing steps

1. Load with `sep=';'`, `encoding='latin1'`, `dtype={'indroea': str}`.
2. Parse dates: `fecha` → `pd.to_datetime(..., dayfirst=True, errors='coerce')`.
3. Convert numeric columns: `pd.to_numeric(..., errors='coerce')`.
4. Generated summary: `data/processed/anuariotablesummary.csv` (4 tables, shape, station count, date range, missingness).

### Next steps

1. Inspect ESTAF to find `indroea` for station "Guadalete" + "Jerez".
2. Filter AFLIQ to that station → generate pilot subset.
3. Visual QA: plot stage/discharge time series, identify gaps/outliers.

### References

- See `reports/data_glossary.md` for terminology (q/h, instantaneous vs daily, embalse, etc.).
- See `reports/guadalete_jerez_event_definition.md` for hazard/impact framework.
