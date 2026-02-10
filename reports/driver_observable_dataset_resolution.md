# Driver → Observable → Dataset → Resolution (v0)

| Driver/mecanismo | Observable (definición medible) | Dataset candidato | Resolución (espacio/tiempo) |
| --- | --- | --- | --- |
| Precipitación reciente | Acumulado 1h/3h/6h; intensidad máxima 1h | SAIH (pluviómetros si existen en el ámbito) | Puntual; 5–15 min a 1h |
| Precipitación reciente | Acumulado 24h/72h | SAIH; reanálisis (si falta cobertura) | Puntual / grilla; horario–diario |
| Humedad antecedente (proxy) | Acumulado 7d/14d de precipitación | SAIH / reanálisis | Puntual / grilla; diario |
| Humedad del suelo | % saturación/índice humedad suelo (top-layer) | Copernicus/ERA5-Land (si se incorpora) | Grilla; horario–diario |
| Estado del río (respuesta) | Caudal instantáneo; caudal medio 1h | SAIH-ROEA (series de caudal/nivel en puntos) | Puntual; 5–15 min a 1h |
| Estado del río (respuesta) | Nivel (m) y tendencia | SAIH (puntos de control) | Puntual; 5–15 min |
| Deshielo (si aplica) | Temperatura > 0°C + SWE decreciente | Reanálisis/nieve (si aplica a cuenca) | Grilla; diario |
| Operación de embalses | Cambio de volumen; caudal de salida | SAIH (presas/obras hidráulicas principales si están instrumentadas) | Puntual; 5–60 min |
| Capacidad del cauce (proxy) | Relación nivel–caudal; cambios por tramo | SAIH (nivel+caudal) + metadatos estación | Puntual; histórico |
| Confluencias/propagación | Lag entre picos en estaciones aguas arriba/abajo | SAIH (series multiestación) | Red; 5–60 min |
| Urbanización (amplificación) | % impermeable aguas arriba (proxy) | HRL Imperviousness / SIOSE (si se incorpora) | Polígono/grilla; anual |
| Uso del suelo | % agrícola/forestal, cambios | CORINE/SIOSE (si se incorpora) | Polígono; multi-año |
| Topografía | Pendiente media cuenca; TWI (proxy) | DEM (IGN o equivalente) | Grilla; estática |
| Geología/suelos | Grupo hidrológico; infiltración (proxy) | Mapas edafológicos (si se incorpora) | Polígono; estática |
| Exposición económica (si se incluye) | Activos/uso del suelo en llanura de inundación | Catastro/land use + mapas peligrosidad (si se incorporan) | Parcela/polígono; multi-año |
