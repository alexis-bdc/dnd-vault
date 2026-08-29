---
tipo: faccion
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
alcance: Local # Local / Regional / Global / Planar
lider: ""
sede_principal: ""
relacion_grupo: Neutral # Aliados / Amistosos / Neutrales / Sospechosos / Enemigos
tags:
  - dnd/faccion
---

# <% tp.file.title %>

> [!shield] Resumen de Facción
> **Líder:** `$= dv.current().lider`
> **Sede:** `$= dv.current().sede_principal`
> **Relación con nosotros:** `$= dv.current().relacion_grupo`

---

## 🎯 Objetivos e Ideología
- 

---

## 👥 Miembros Conocidos
```dataview
TABLE clase_o_rol AS "Rol", ubicacion AS "Ubicación", actitud AS "Actitud"
FROM "01 - Campañas"
WHERE tipo = "npc" AND contains(faccion, this.file.name)
SORT file.name ASC
```

---

## 📜 Historial de Interacciones con la Facción
- 
