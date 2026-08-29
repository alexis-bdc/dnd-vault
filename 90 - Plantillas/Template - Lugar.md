---
tipo: lugar
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
tipo_lugar: Ciudad # Ciudad / Pueblo / Mazmorra / Taberna / Tienda / Región
region: ""
gobernante: ""
faccion_control: ""
peligro: Bajo # Seguro / Bajo / Medio / Alto / Extremo
tags:
  - dnd/lugar
---

# <% tp.file.title %>

> [!map] `$= dv.current().tipo_lugar` en `$= dv.current().region`
> **Gobierno / Autoridad:** `$= dv.current().gobernante`
> **Facción al mando:** `$= dv.current().faccion_control`
> **Nivel de Peligro:** `$= dv.current().peligro`

---

## 🏰 Descripción y Ambiente
- 

---

## 📍 Puntos de Interés / Tiendas / Tabernas
- **Punto 1:** Descripción.

---

## 👥 Habitantes y NPCs Relevantes
```dataview
TABLE clase_o_rol AS "Rol", actitud AS "Actitud", faccion AS "Facción"
FROM "01 - Campañas"
WHERE tipo = "npc" AND contains(ubicacion, this.file.name)
SORT file.name ASC
```

---

## 📜 Eventos / Notas del Lugar
- 
