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

## 🏛️ Estructuras reales del mundo

Exportadas del **mundo real de la semilla** (servidor de Minecraft 1.21.1 + uNmINeD), planta por planta. **1 casilla = 1 bloque = 64 px.**
- **Exterior:** vista desde arriba (tejados y terreno).
- **Planta N (Y …):** corte horizontal a esa altura: se ve el suelo, los muebles y los muros, sin techo. El negro es vacío o caída.
- Los colores son la paleta de uNmINeD (sin texturas del juego).
- Regenerar: `python3 .tools/mundo/planos.py` (ver `.tools/mundo/`).

### 🏛️ Superficie y subsuelo

#### Cámaras de desafío 1
X 16 · Z 336

![[Cámaras de desafío 1 - Planta 1 (Y -29).png|400]]
![[Cámaras de desafío 1 - Planta 2 (Y -4).png|400]]
![[Cámaras de desafío 1 - Planta 3 (Y 8).png|400]]

#### Cámaras de desafío 2
X 176 · Z -464

![[Cámaras de desafío 2 - Planta 1 (Y -50).png|400]]
![[Cámaras de desafío 2 - Planta 2 (Y -40).png|400]]
![[Cámaras de desafío 2 - Planta 3 (Y -14).png|400]]

#### Cabaña de bruja
X -240 · Z 1184

![[Cabaña de bruja - Exterior.png|400]]
![[Cabaña de bruja - Planta 1 (Y 63).png|400]]

#### Templo del desierto
X -144 · Z -2912

![[Templo del desierto - Exterior.png|400]]
![[Templo del desierto - Planta 1 (Y 52).png|400]]
![[Templo del desierto - Planta 2 (Y 64).png|400]]
![[Templo del desierto - Planta 3 (Y 70).png|400]]

#### Templo de la jungla 1
X 752 · Z 144

![[Templo de la jungla 1 - Exterior.png|400]]
![[Templo de la jungla 1 - Planta 1 (Y 63).png|400]]
![[Templo de la jungla 1 - Planta 2 (Y 67).png|400]]
![[Templo de la jungla 1 - Planta 3 (Y 73).png|400]]

#### Templo de la jungla 2
X -416 · Z -976

![[Templo de la jungla 2 - Exterior.png|400]]
![[Templo de la jungla 2 - Planta 1 (Y 60).png|400]]
![[Templo de la jungla 2 - Planta 2 (Y 64).png|400]]
![[Templo de la jungla 2 - Planta 3 (Y 70).png|400]]

#### Puesto de saqueadores 1
X -1184 · Z 1024

![[Puesto de saqueadores 1 - Exterior.png|400]]
![[Puesto de saqueadores 1 - Planta 1 (Y 69).png|400]]

#### Puesto de saqueadores 2
X 1184 · Z -1488

![[Puesto de saqueadores 2 - Exterior.png|400]]
![[Puesto de saqueadores 2 - Planta 1 (Y 63).png|400]]
![[Puesto de saqueadores 2 - Planta 2 (Y 72).png|400]]

#### Iglú 1
X -1472 · Z 1072

![[Iglú 1 - Exterior.png|400]]
![[Iglú 1 - Planta 1 (Y 29).png|400]]

#### Iglú 2
X -2000 · Z 640

![[Iglú 2 - Exterior.png|400]]
![[Iglú 2 - Planta 1 (Y 64).png|400]]

#### Aldea 1
X 400 · Z -464

![[Aldea 1 - Exterior.png|400]]

#### Aldea 2
X 160 · Z -880

![[Aldea 2 - Exterior.png|400]]

#### Mansión del bosque
X -832 · Z -656

![[Mansión del bosque - Exterior.png|400]]
![[Mansión del bosque - Planta 1 (Y 72).png|400]]
![[Mansión del bosque - Planta 2 (Y 80).png|400]]
![[Mansión del bosque - Planta 3 (Y 88).png|400]]

#### Ciudad antigua
X 3136 · Z 432

![[Ciudad antigua - Planta 1 (Y -52).png|400]]
![[Ciudad antigua - Planta 2 (Y -46).png|400]]
![[Ciudad antigua - Planta 3 (Y -40).png|400]]
![[Ciudad antigua - Planta 4 (Y -34).png|400]]

#### Fortaleza del End
X -496 · Z -1776

![[Fortaleza del End - Planta 2 (Y 3).png|400]]

#### Monumento oceánico
X 48 · Z 768

![[Monumento oceánico - Planta 1 (Y 39).png|400]]
![[Monumento oceánico - Planta 2 (Y 45).png|400]]
![[Monumento oceánico - Planta 3 (Y 51).png|400]]

### 🔥 Nether

#### Fortaleza del Nether 1
X 112 · Z -96 (Nether)

![[Fortaleza del Nether 1 - Planta 1 (Y 48).png|400]]
![[Fortaleza del Nether 1 - Planta 2 (Y 55).png|400]]

#### Fortaleza del Nether 2
X -128 · Z -80 (Nether)

![[Fortaleza del Nether 2 - Planta 1 (Y 48).png|400]]

#### Bastión 1
X 112 · Z 272 (Nether)

![[Bastión 1 - Planta 1 (Y 29).png|400]]
![[Bastión 1 - Planta 2 (Y 43).png|400]]
![[Bastión 1 - Planta 3 (Y 76).png|400]]

#### Bastión 2
X -256 · Z 304 (Nether)

![[Bastión 2 - Planta 1 (Y 29).png|400]]
![[Bastión 2 - Planta 2 (Y 43).png|400]]
![[Bastión 2 - Planta 3 (Y 48).png|400]]
![[Bastión 2 - Planta 4 (Y 78).png|400]]

### 🌌 End

#### Ciudad del End
X 352 · Z 976 (End)

![[Ciudad del End - Planta 1 (Y 61).png|400]]
![[Ciudad del End - Planta 2 (Y 70).png|400]]
![[Ciudad del End - Planta 3 (Y 96).png|400]]
![[Ciudad del End - Planta 4 (Y 102).png|400]]
![[Ciudad del End - Planta 5 (Y 157).png|400]]
![[Ciudad del End - Planta 6 (Y 164).png|400]]

---

## 🔑 Leyenda (End)
- **Rombo rosa:** cristal del End. Con rejilla encima: enjaulado.
- **Negro con relieve:** pilar de obsidiana. **Gris:** roca madre del portal. **Negro liso:** vacío o pozo del portal.
- **Números:** pilar de la tabla.
