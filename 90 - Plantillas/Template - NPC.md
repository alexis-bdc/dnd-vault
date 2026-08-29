---
tipo: npc
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
raza: ""
clase_o_rol: ""
faccion: ""
ubicacion: ""
actitud: Neutral # Amigable / Neutral / Hostil / Aliado
estado: Vivo # Vivo / Muerto / Desaparecido / Desconocido
tags:
  - dnd/npc
---

# <% tp.file.title %>

> [!info] Ficha Resumida
> **Rol / Ocupación:** `$= dv.current().clase_o_rol || "Desconocido"`
> **Ubicación habitual:** `$= dv.current().ubicacion || "Desconocida"`
> **Facción:** `$= dv.current().faccion || "Ninguna"`
> **Actitud hacia el grupo:** `$= dv.current().actitud || "Neutral"`
> **Estado:** `$= dv.current().estado || "Vivo"`

---

## 🎭 Apariencia y Primera Impresión
- 

## 🧠 Personalidad y Motivaciones
- **Objetivo / Deseo:** 
- **Miedos / Secretos:** 

## 🤝 Relación con el Grupo / Mi PJ
- 

## 📌 Historial de Encuentros / Notas
- 
