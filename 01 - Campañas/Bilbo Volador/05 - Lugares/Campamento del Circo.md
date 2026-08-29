---
tipo: lugar
campaña: "Bilbo Volador"
tipo_lugar: "Campamento / Asentamiento Móvil"
region: "Alrededores del Bosque"
gobernante: "[[01 - Campañas/Bilbo Volador/03 - NPCs/La Madam|La Madam]]"
faccion_control: "[[01 - Campañas/Bilbo Volador/06 - Facciones/El Circo Ambulante|El Circo Ambulante]]"
peligro: "Bajo"
tags:
  - dnd/lugar
  - dnd/bilbo-volador
---

# 🎪 Campamento del Circo Ambulante

> [!map] **`$= dv.current().tipo_lugar` en `$= dv.current().region`**
> **Dirección / Autoridad:** `$= dv.current().gobernante` | **Control:** `$= dv.current().faccion_control`
> **Nivel de Peligro:** `$= dv.current().peligro`

---

## 🏰 Descripción y Ambiente
Un colorido y bullicioso conjunto de carretas, carpas, jaulas de espectáculo y puestos de artistas. Es la base de operaciones donde conviven acróbatas, magos, ilusionistas, adivinos y luchadores.

---

## 📍 Puntos de Interés
- **Carpa Principal:** Donde se celebran los espectáculos centrales.
- **Carromato de La Madam:** Sede de mando y residencia de la directora.
- **Puesto del Encargado / Intendencia:** Almacén de suministros, cuentas y pago de nóminas.

---

## 👥 NPCs Residentes
```dataview
TABLE clase_o_rol AS "Rol", actitud AS "Actitud", faccion AS "Facción"
FROM "01 - Campañas/Bilbo Volador/03 - NPCs"
WHERE tipo = "npc" AND contains(ubicacion, "Campamento del Circo")
SORT file.name ASC
```
