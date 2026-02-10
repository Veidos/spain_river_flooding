# Driver → Observable → Dataset → Resolution (v0)

| Driver / mechanism | Observable (measurable definition) | Candidate dataset | Resolution (space/time) |
| --- | --- | --- | --- |
| Recent precipitation | 1h/3h/6h accumulation; 1h maximum intensity | SAIH (rain gauges, if available in scope) | Point; 5–15 min to 1h |
| Recent precipitation | 24h/72h accumulation | SAIH; reanalysis (if coverage is incomplete) | Point / grid; hourly–daily |
| Antecedent wetness (proxy) | 7d/14d accumulated precipitation | SAIH / reanalysis | Point / grid; daily |
| Soil moisture | % saturation / soil moisture index (top layer) | Copernicus / ERA5-Land (if included) | Grid; hourly–daily |
| River state (response) | Instantaneous discharge; 1h mean discharge | SAIH-ROEA (discharge/stage time series at selected points) | Point; 5–15 min to 1h |
| River state (response) | Stage (m) and trend | SAIH (control points) | Point; 5–15 min |
| Snowmelt (if applicable) | Air temperature > 0°C + decreasing SWE | Reanalysis / snow products (if applicable to basin) | Grid; daily |
| Reservoir operations | Storage change; outflow discharge | SAIH (dams / major hydraulic works, if instrumented) | Point; 5–60 min |
| Channel capacity (proxy) | Stage–discharge relationship; changes over time by reach | SAIH (stage + discharge) + station metadata | Point; historical |
| Confluences / flood wave propagation | Lag between peaks at upstream vs downstream stations | SAIH (multi-station time series) | Network; 5–60 min |
| Urbanization (amplification) | Upstream impervious surface fraction (proxy) | HRL Imperviousness / SIOSE (if included) | Polygon / grid; annual |
| Land use | Agricultural/forest fraction; changes | CORINE / SIOSE (if included) | Polygon; multi-year |
| Topography | Mean catchment slope; TWI (proxy) | DEM (IGN or equivalent) | Grid; static |
| Geology / soils | Hydrologic soil group; infiltration capacity (proxy) | Soil / geology maps (if included) | Polygon; static |
| Economic exposure (if included) | Assets / land use in the floodplain | Cadastre / land-use + hazard maps (if included) | Parcel / polygon; multi-year |
