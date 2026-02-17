# Data Glossary - SAIH Guadalquivir Anuario de Aforos

## Core Concepts

### River (río) vs Canal

- **River**: Natural watercourse. Measures natural flow.
- **Canal**: Artificial channel. Measures managed/diverted flow.

### Reservoir (embalse)

Dam that stores river water. Affects downstream flow (releases controlled).

### Instantaneous vs Daily

- **Daily (AFLIQ)**: Average of the full day.
- **Instantaneous (AFLIQI)**: Peak value at exact moment. Critical for extreme events.

---

## Variable Naming Convention

| Prefix | Meaning | Unit | Example |
| ------ | ------- | ---- | --------- |
| q | Discharge (caudal) | m³/s | qmed = mean discharge |
| h | Stage/level (altura) | m | hc = max daily stage |
| aport | Volume (aportación) | hm³ | aportano = annual volume |

### Suffixes

- `med`: mean/average
- `c`: daily maximum (from Spanish "crecida")
- `ci`: instantaneous maximum
- `n`: minimum
- `ano`: annual
- `mes`: monthly

---

## Tables Structure

### Time Series (data)

- **AFLIQ**: Daily river stage & discharge (`indroea` + `fecha`)
- **AFLIQI**: Instantaneous monthly peaks
- **ANUALA**: Annual statistics
- **EXTREMOSAAV**: Corrected annual maxima (gap-filled, quality-controlled)

### Metadata

- **ESTAF**: Station catalog (`indroea`, location, coordinates, catchment area)

### Lookup

- MUNI/PROV/AUTON: Administrative codes

---

## Data Quality Notes

**Corrected maxima (EXTREMOSAAV)**:
Historical data has gaps/sensor changes. Experts fill/adjust using statistical methods.
Use for frequency analysis (return periods).

**Provisional data**:
Real-time data may be revised. Check `origdatoid` and station `observ` fields.

---

## Geographic Context

**Guadalete River**: Independent river in Cádiz province (Jerez de la Frontera).
**Guadalquivir Basin Authority (CHG)**: Manages data for multiple rivers including Guadalete.
Folder name `GUADALQUIVIR_DATA` refers to the authority, not the river.
