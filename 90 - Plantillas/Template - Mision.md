---
tipo: mision
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
estado: Activa # Activa / Completada / Fallida / En Pausa
prioridad: Media # Alta / Media / Baja
dada_por: ""
ubicacion: ""
recompensa: ""
tags:
  - dnd/mision
---

# <% tp.file.title %>

> [!todo] Estado: `$= dv.current().estado` | Prioridad: `$= dv.current().prioridad`
> **Otorgada por:** `$= dv.current().dada_por`
> **Lugar:** `$= dv.current().ubicacion`
> **Recompensa prometida:** `$= dv.current().recompensa`

---

## 📜 Descripción del Encargo
- 

---

## 🎯 Objetivos y Progreso
- [ ] Paso 1
- [ ] Paso 2

---

## 🕵️‍♂️ Pistas y Datos Descubiertos
- 

---

## 👥 Personajes Involucrados
- 
