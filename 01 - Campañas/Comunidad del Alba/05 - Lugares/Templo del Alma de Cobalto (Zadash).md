---
tipo: lugar
campaña: "Comunidad del Alba"
tipo_lugar: Templo / Gran Biblioteca Monástica
region: "Zadash / Imperio Dwendalian"
gobernante: "[[01 - Campañas/Comunidad del Alba/03 - NPCs/Ingka|Maestra Ingka]]"
faccion_control: "[[01 - Campañas/Comunidad del Alba/06 - Facciones/El Alma de Cobalto|El Alma de Cobalto]]"
peligro: Muy Bajo (Santuario Seguro)
tags:
  - dnd/lugar
  - dnd/templo
  - dnd/biblioteca
  - dnd/comunidad-del-alba
---

# 🏛️ Templo y Biblioteca del Alma de Cobalto (Zadash)

> [!map] **`$= dv.current().tipo_lugar` en `$= dv.current().region`**
> **Alta Archivista:** `$= dv.current().gobernante`
> **Facción a Cargo:** `$= dv.current().faccion_control`
> **Seguridad / Peligro:** `$= dv.current().peligro`

---

## 🏛️ Descripción y Ambiente
Situada en los distritos superiores de [[01 - Campañas/Comunidad del Alba/05 - Lugares/Zadash|Zadash]], la sede del Alma de Cobalto es un majestuoso complejo de cúpulas azules, altas columnas de mármol y silenciosas galerías repletas de manuscritos, mapas y cámaras acorazadas para artefactos mágicos. Está consagrado a la diosa **Ioun**, atrayendo a monjes marciales, historiadores y magos de transmutación.

---

## 📍 Puntos de Interés Internos
- **El Atrio de los Escribas:** Custodiado por guardias monásticos como [[01 - Campañas/Comunidad del Alba/03 - NPCs/Elaion|Elaion]].
- **El Sanctum de Conservación:** Talleres especializados donde se catalogan y protegen reliquias arcanas.
- **Los Aposentos de la Maestra Ingka:** Lugar donde Ren recibió el encargo de vigilar y reportar la evolución de [[01 - Campañas/Comunidad del Alba/03 - NPCs/P.I.L.A.|P.I.L.A.]].

---

## 👥 Personajes Presentes
```dataview
TABLE clase_o_rol AS "Rol / Título", actitud AS "Actitud", estado AS "Estado"
FROM "01 - Campañas/Comunidad del Alba/03 - NPCs"
WHERE contains(ubicacion, "Alma de Cobalto") OR contains(faccion, "Cobalto")
SORT file.name ASC
```
