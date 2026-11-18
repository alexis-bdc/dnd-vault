---
tipo: mapa
campaña: "Tierra de Bloques"
tags:
  - dnd/mapa
  - dnd/battlemap
---

# ⚔️ Battlemaps

Mapas de combate para el VTT. Están en `10 - images/Battlemaps/`.
- **Escala:** 1 casilla = 1 bloque = 1,5 m. El norte está arriba.
- **Tamaño en el VTT:** cada casilla mide 48 px en la arena completa del End y 64 px en el centro. Pon ese tamaño de cuadrícula al importar.
- Botín y guardianes de cada lugar en [[Botín por Lugar]]; mobs en el [[Bestiario]].

> [!note] De dónde salen
> - **La arena del End es la de tu semilla:** la forma de la isla está calculada con cubiomes, y los pilares con el mismo algoritmo del juego (posición, grosor, altura y jaulas). Para regenerarla: `python3 .tools/battlemaps/battlemaps.py`.

---

## 🐉 End: arena del Dragón (nivel 20)

![[End - Arena del Dragón.png]]

Ocupa 121×121 casillas, de −60 a +60 alrededor del portal de salida. El vacío (negro) es caída mortal: quien cae, muere (ver [[Muerte y Reaparición]]).

### Pilares de obsidiana

| Pilar | Posición (X, Z) | Ancho | Altura sobre el suelo | Cristal |
|---|---|---|---|---|
| 1 | 42, 0 | 5 casillas | 19 bloques (28,5 m) | 🔒 **enjaulado** |
| 2 | 33, 24 | 9 | 42 (63 m) | ✨ |
| 3 | 12, 39 | 9 | 34 (51 m) | ✨ |
| 4 | −13, 39 | 5 | 16 (24 m) | ✨ |
| 5 | −34, 24 | 9 | 35 (52,5 m) | ✨ |
| 6 | −42, −1 | 11 | 46 (69 m) | ✨ (el más alto) |
| 7 | −34, −25 | 7 | 26 (39 m) | ✨ |
| 8 | −13, −40 | 7 | 27 (40,5 m) | ✨ |
| 9 | 12, −40 | 7 | 30 (45 m) | ✨ |
| 10 | 33, −25 | 5 | 22 (33 m) | 🔒 **enjaulado** |

> [!warning] Cristales del End (regla casera, no está en el statblock del [[Dragón del End]])
> - **Curación:** al inicio de su turno, el dragón recupera **5 PG por cada cristal intacto** (hasta 50 por turno). Romperlos es el primer objetivo.
> - **Romper un cristal:** CA 10. Cualquier impacto lo destruye. Explota: cada criatura a 3 m hace una TS de DES CD 15 y recibe 22 (4d10) de fuego, o la mitad si la supera.
> - **Jaulas (pilares 1 y 10):** barrotes con CA 15 y 20 PG. Las flechas no pasan. Hay que subir y romperlos, o atacar desde dentro.
> - **Subir:** la obsidiana no tiene agarres, así que trepar es Atletismo CD 25. Lo práctico es subir **poniendo bloques bajo los pies**: 1 bloque (1,5 m) por acción. También se puede volar o usar perlas de ender.
> - **Pilares 2, 5 y 6:** su cristal queda a más de 50 m. Desde el suelo hay que disparar con desventaja por la distancia larga.

### Centro y portal (fase de perchado)

![[End - Centro y portal.png]]

Ocupa 45×45 casillas alrededor del portal. Úsalo cuando el dragón se posa en el pilar central para cargar su aliento.
- **Pilar central (roca madre):** el dragón se posa encima.
- **Pozo del portal:** caer dentro no hace nada hasta que el dragón muere. Después, lleva de vuelta al mundo.

---

## 🏛️ Estructuras reales (pendiente)

Se exportarán **del mundo real de la semilla**, planta por planta, con uNmINeD: cámaras de desafío, fortaleza del Nether, templos, cabaña de bruja, puesto de saqueadores, iglú… Irán en `10 - images/Battlemaps/`.

---

## 🔑 Leyenda (End)
- **Rombo rosa:** cristal del End. Con rejilla encima: enjaulado.
- **Negro con relieve:** pilar de obsidiana. **Gris:** roca madre del portal. **Negro liso:** vacío o pozo del portal.
- **Números:** pilar de la tabla.
