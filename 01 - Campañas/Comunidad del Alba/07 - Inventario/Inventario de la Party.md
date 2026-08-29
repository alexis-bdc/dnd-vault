---
tipo: inventario_party
campaña: "Comunidad del Alba"
monedas_grupales:
  po: 2360
  pp: 0
  pc: 0
  pe: 0
  ppt: 0
suministros_comunes:
  raciones_viaje: 20
  antorchas: 10
  odres_agua: 8
  cuerda_canamo_50ft: 2
  pitones_escalada: 10
  tienda_campana: 2
  pociones_curacion_comunes: 0
tags:
  - dnd/inventario
  - dnd/party
  - dnd/comunidad-del-alba
---

# 🎒 Inventario Grupal y Objetos de la Party — Comunidad del Alba

> [!nav] **Navegación**
> 🎲 [[01 - Campañas/Comunidad del Alba/Dashboard - Comunidad del Alba|Volver al Dashboard de Campaña]] • 🧪 [[01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren|Ficha de Frater Ren]] • 📂 [[01 - Campañas/Comunidad del Alba/07 - Inventario/|Carpeta de Inventario]]

---

> [!info] **Control de Objetos en Posesión de la Party**
> Este panel registra todos los objetos relevantes, mágicos, reliquias y suministros que se encuentran en posesión de los miembros de la party (**Ethan Corvus, Pentius, Sante, Ulrich, P.I.L.A.** o el **Fondo Común**), excluyendo el inventario personal de **Frater Ren**.

---

## 💰 Tesorería y Monedero Grupal (Fondo Común)

```meta-bind-button
label: 💰 Gestionar Tesorería Grupal (Añadir / Gastar)
icon: coins
style: primary
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/gestionar_monedero.md
```

| 🟤 Cobre (PC) | ⚪ Plata (PP) | 🟢 Electro (PE) | 🟡 Oro (PO) | 🔘 Platino (PPT) |
| :---: | :---: | :---: | :---: | :---: |
| `INPUT[number:monedas_grupales.pc]` | `INPUT[number:monedas_grupales.pp]` | `INPUT[number:monedas_grupales.pe]` | `INPUT[number:monedas_grupales.po]` | `INPUT[number:monedas_grupales.ppt]` |

---

## 🎒 Objetos Relevantes y Equipamiento Mágico

```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", portador AS "Portador", sintonizacion AS "Sintonización", valor_estimado AS "Valor"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND !contains(lower(string(categoria)), "consumible") AND !contains(lower(string(categoria)), "poción") AND !contains(lower(string(categoria)), "pocion")
SORT portador ASC, file.name ASC
```

---

## 🧪 Consumibles y Pociones

```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", portador AS "Portador", valor_estimado AS "Valor"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND (contains(lower(string(categoria)), "consumible") OR contains(lower(string(categoria)), "poción") OR contains(lower(string(categoria)), "pocion"))
SORT portador ASC, file.name ASC
```

---

## 👥 Desglose de Objetos por Miembro de la Party

### 🗡️ [[01 - Campañas/Comunidad del Alba/02 - Personajes/Ethan Corvus|Ethan Corvus]] (Pícaro)
```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", sintonizacion AS "Sintonización", valor_estimado AS "Valor Estimado"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND contains(string(portador), "Ethan")
SORT file.name ASC
```

### 🛡️ [[01 - Campañas/Comunidad del Alba/02 - Personajes/Pentius|Pentius]] (Paladín)
```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", sintonizacion AS "Sintonización", valor_estimado AS "Valor Estimado"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND contains(string(portador), "Pentius")
SORT file.name ASC
```

### 🏹 [[01 - Campañas/Comunidad del Alba/02 - Personajes/Sante|Sante]] (Explorador)
```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", sintonizacion AS "Sintonización", valor_estimado AS "Valor Estimado"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND contains(string(portador), "Sante")
SORT file.name ASC
```

### 🪓 [[01 - Campañas/Comunidad del Alba/02 - Personajes/Ulrich|Ulrich]] (Bárbaro)
```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", sintonizacion AS "Sintonización", valor_estimado AS "Valor Estimado"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND contains(string(portador), "Ulrich")
SORT file.name ASC
```

### 🤖 [[01 - Campañas/Comunidad del Alba/03 - NPCs/P.I.L.A.|P.I.L.A.]] (Acompañante Autómata)
```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", sintonizacion AS "Sintonización", valor_estimado AS "Valor Estimado"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND contains(string(portador), "P.I.L.A")
SORT file.name ASC
```

### 📦 Cofre Común / Carro / Almacén del Grupo
```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", sintonizacion AS "Sintonización", valor_estimado AS "Valor Estimado"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND (contains(string(portador), "Grupo") OR contains(string(portador), "Común") OR contains(string(portador), "Party") OR !portador) AND !contains(string(portador), "Ren")
SORT file.name ASC
```

---

## ⛺ Suministros y Recursos de Campamento Compartidos

| Recurso / Suministro | Cantidad Compartida | Notas de Uso |
| :--- | :---: | :--- |
| **Raciones de Viaje** | 20 días | Repartidas para subsistencia del grupo en expediciones. |
| **Antorchas** | 10 unidades | 1 hora de luz brillante en radio de 20 pies + 20 pies de luz tenue. |
| **Odres de Agua Fresca** | 8 odres | Rellenables con la [[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Vasija Alquimica\|Vasija Alquímica]]. |
| **Cuerdas de Cáñamo (50 pies)** | 2 cuerdas | Con ganchos de agarre para escalada e infiltración. |
| **Tiendas de Campaña** | 2 tiendas | Capacidad para 3 personas cada una durante descansos largos. |
| **Kit de Escalada y Pitones** | 1 kit | Ventaja en pruebas de Fuerza (Atletismo) para escalar riscos. |

---

## 📜 Registro de Movimientos de Tesorería (Fondo Común)

| Sesión | Origen / Concepto | Monto | Saldo Restante | Notas |
| :---: | :--- | :---: | :---: | :--- |
| **02** | Recompensa: Caza de Gnolls | +560 PO | 560 PO | Cobrado en Zadash tras Sesión 01. |
| **02** | Recompensa: Eliminación de la Hag | +2000 PO | 2560 PO | Recompensa de autoridad municipal. |
| **02** | Préstamo a [[01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren\|Frater Ren]] | -200 PO | **2360 PO** | Para reposición de laboratorio alquímico (deuda pendiente). |
