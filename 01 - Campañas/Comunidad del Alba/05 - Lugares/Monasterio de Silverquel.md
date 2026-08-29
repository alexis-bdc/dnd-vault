---
tipo: lugar
campaña: "Comunidad del Alba"
tipo_lugar: Monasterio / Santuario Aislado
region: "Garganta de Silberquel (Cadena Montañosa Norte)"
gobernante: "[[01 - Campañas/Comunidad del Alba/03 - NPCs/Nandes|Abadesa Nandes]]"
faccion_control: "Orden de la Garganta de Silberquel"
peligro: Medio (Terreno Escarpado)
tags:
  - dnd/lugar
  - dnd/monasterio
  - dnd/comunidad-del-alba
---

# 🏔️ Monasterio de la Garganta de Silberquel

> [!map] **`$= dv.current().tipo_lugar` en `$= dv.current().region`**
> **Abadesa / Autoridad:** `$= dv.current().gobernante`
> **Facción al mando:** `$= dv.current().faccion_control`
> **Nivel de Peligro:** `$= dv.current().peligro`

---

## 🏔️ Descripción y Misión de la Orden
Construido en los escarpes de una profunda garganta en la cordillera de Silberquel, este remoto monasterio es una institución consagrada a una triple vocación:
1. **El estudio y catalogación de fenómenos arcanos y naturales.**
2. **La preservación y custodia de reliquias y saberes antiguos.**
3. **La forja y fabricación de artefactos mágicos de alta precisión.**

En la paz austera de esta garganta, los iniciados pasan años de reclusión académica dedicándose a la transmutación, la interacción entre sales minerales y botánica mágica, y la creación de artilugios arcanos.

---

## 📜 El Rito de la Misión de Egreso
Para completar su formación y graduarse como miembros de pleno derecho de la orden, cada iniciado (como [[01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren|Frater Ren]] o [[01 - Campañas/Comunidad del Alba/03 - NPCs/Marciel|Marciel]]) debe partir al mundo exterior y cumplir una misión sagrada:
- **Localizar, recuperar o forjar un artefacto místico o mágico de verdadero mérito.**
- **Regresar a la garganta y consagrarlo formalmente al santuario del monasterio.**

---

## 👥 Miembros y Personajes Vinculados
```dataview
TABLE clase_o_rol AS "Rol / Ocupación", actitud AS "Vínculo con Ren", estado AS "Estado"
FROM "01 - Campañas/Comunidad del Alba/03 - NPCs"
WHERE contains(faccion, "Silberquel")
SORT file.name ASC
```
