---
tipo: lugar
campaña: "Comunidad del Alba"
tipo_lugar: Ciudad
region: "Imperio Dwendalian / Wildemount"
gobernante: "Starosta Wyatt Maran"
faccion_control: "La Corona Dwendaliana / Guardia de Zadash"
peligro: Medio
tags:
  - dnd/lugar
  - dnd/ciudad
  - dnd/comunidad-del-alba
---

# 🏰 Ciudad de Zadash

> [!map] **`$= dv.current().tipo_lugar` en `$= dv.current().region`**
> **Gobierno / Autoridad:** `$= dv.current().gobernante`
> **Facción al mando:** `$= dv.current().faccion_control`
> **Nivel de Peligro:** `$= dv.current().peligro`

---

## 🏰 Descripción y Ambiente
Zadash es una bulliciosa metrópolis mercantil, centro neurálgico de comercio, tránsito militar y gremios de artesanos. Tras sus imponentes murallas y concurridas plazas se ocultan intrigas políticas, redes de contrabandistas y sombras mágicas.

---

## 📍 Puntos de Interés / Tiendas
- **[[01 - Campañas/Comunidad del Alba/05 - Lugares/Templo del Alma de Cobalto (Zadash)|Templo y Biblioteca del Alma de Cobalto]]:** Gran sede monástica de devotos de Ioun, liderada por la [[01 - Campañas/Comunidad del Alba/03 - NPCs/Ingka|Maestra Ingka]] y custodiada por [[01 - Campañas/Comunidad del Alba/03 - NPCs/Elaion|Elaion]], dedicada a la custodia de conocimiento y artefactos arcanos.
- **Botica y Tienda de Alquimia de [[01 - Campañas/Comunidad del Alba/03 - NPCs/Bracus|Bracus]]:** Establecimiento donde Frater Ren adquirió suministros para su laboratorio y donde Bracus mostró sospechosa fijación por P.I.L.A.
- **Panaderías y Molinos de la Ciudad:** Antiguos focos de la contaminación silenciosa de [[01 - Campañas/Comunidad del Alba/08 - Lore/Hongos Feericos de Zadash|hongos feéricos]] de la derrotada bruja [[01 - Campañas/Comunidad del Alba/03 - NPCs/Rina|Rina]].

---

## 👥 Habitantes y NPCs Relevantes
```dataview
TABLE clase_o_rol AS "Rol / Ocupación", actitud AS "Actitud hacia la Party", estado AS "Estado"
FROM "01 - Campañas/Comunidad del Alba/03 - NPCs"
WHERE contains(ubicacion, "Zadash")
SORT file.name ASC
```

---

## 📜 Eventos y Trama Activa
- **[[01 - Campañas/Comunidad del Alba/01 - Sesiones/Sesión 02 - La Sombra de Rina y los Hongos de Zadash|Sesión 02]]:** Llegada del grupo, cobro de 2560 PO de recompensas, reposición de equipo de Ren y descubrimiento de la conspiración de pan con hongos feéricos de Rina.
