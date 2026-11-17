---
tipo: pj
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
jugador: ""
raza: ""
clase: ""
subclase: ""
nivel: 1
ca: 10
pg_max: 10
percepcion_pasiva: 10
ficha: "" # link a Nivel20
estado: Activo # Activo / Ausente / Muerto / Retirado
tags:
  - dnd/pj
  - dnd/dm
---

# <% tp.file.title %>

> [!info] Vista DM
> **Jugador:** `$= dv.current().jugador` | `$= dv.current().raza` `$= dv.current().clase` (`$= dv.current().subclase`) nv `$= dv.current().nivel`
> **CA** `$= dv.current().ca` | **PG** `$= dv.current().pg_max` | **Percepción pasiva** `$= dv.current().percepcion_pasiva`
> **Ficha completa:** `$= dv.current().ficha ? "[Nivel20](" + dv.current().ficha + ")" : "sin link"`

## 🪝 Ganchos (lo que más vas a usar)
- **Quiere:** 
- **Teme:** 
- **Vínculo / persona importante:** 
- **Secreto o deuda:** 

## 📖 Trasfondo resumido
- 

## 🎯 Arco personal
- [ ] 

## 🎁 Recompensas y objetos importantes
- 

## 📌 Notas de mesa
- (Estilo de juego del jugador, qué disfruta: combate, rol, exploración)
