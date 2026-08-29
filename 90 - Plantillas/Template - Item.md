---
tipo: objeto
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
categoria: Objeto Mágico # Arma / Armadura / Consumible / Accesorio / Objeto Mágico / Misceláneo
rareza: Común # Común / Poco Común / Raro / Muy Raro / Legendario / Artefacto
cantidad: 1
sintonizacion: false # true / false
portador: Grupo # Nombre del PJ / Carro / Cofre / Grupo
valor_estimado: ""
tags:
  - dnd/item
---

# <% tp.file.title %>

> [!quote] `$= dv.current().categoria` (`$= dv.current().rareza`)
> **Sintonización:** `$= dv.current().sintonizacion ? "Requiere sintonización" : "No requiere"`
> **Portador actual:** `$= dv.current().portador`
> **Valor estimado:** `$= dv.current().valor_estimado`

---

## ⚔️ Propiedades y Efectos Mecánicos
- 

---

## 📖 Historia / Origen del Objeto
- **Dónde se encontró:** 
- **Notas adicionales:** 
