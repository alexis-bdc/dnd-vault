---
tipo: dashboard
campaña: "Bilbo Volador"
tags:
  - dnd/dashboard
---

# 🎲 Campaña: Bilbo Volador

> [!nav] **Navegación Rápida**
> 📜 [[01 - Campañas/Bilbo Volador/01 - Sesiones/|01 - Sesiones]] • 🛡️ [[01 - Campañas/Bilbo Volador/02 - Personajes/|02 - Personajes]] • 👥 [[01 - Campañas/Bilbo Volador/03 - NPCs/|03 - NPCs]]
> 🎯 [[01 - Campañas/Bilbo Volador/04 - Misiones/|04 - Misiones]] • 🏰 [[01 - Campañas/Bilbo Volador/05 - Lugares/|05 - Lugares]] • 🎪 [[01 - Campañas/Bilbo Volador/06 - Facciones/|06 - Facciones]]
> 🎒 [[01 - Campañas/Bilbo Volador/07 - Inventario/|07 - Inventario]] • 📖 [[01 - Campañas/Bilbo Volador/08 - Lore/|08 - Lore]]

---

## 🎮 Panel de Control de Sesión en Vivo ([[01 - Campañas/Bilbo Volador/02 - Personajes/Moxy|😈 Moxy]])

> [!abstract] **Estado Vital y Combate**
> **PG:** `INPUT[number:01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#pg_actual]` / `VIEW[{01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#pg_max}][text]` | **CA:** `VIEW[{01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#ca}][text]` | **Iniciativa:** +`VIEW[{01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#iniciativa}][text]`

### 🔮 Espacios de Conjuro Diarios

| Nivel de Espacio | Máximo | Usados | Restantes |
| :---: | :---: | :---: | :---: |
| **Nivel 1** | `VIEW[{01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv1_max}][text]` | `INPUT[number:01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv1_usados]` | **`VIEW[{01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv1_max} - {01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv1_usados}][math]`** |
| **Nivel 2** | `VIEW[{01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv2_max}][text]` | `INPUT[number:01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv2_usados]` | **`VIEW[{01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv2_max} - {01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv2_usados}][math]`** |

```meta-bind-button
label: 🌙 Descanso Largo para Moxy
icon: bed
style: primary
actions:
  - type: updateMetadata
    bindTarget: 01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#pg_actual
    evaluate: false
    value: 21
  - type: updateMetadata
    bindTarget: 01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv1_usados
    evaluate: false
    value: 0
  - type: updateMetadata
    bindTarget: 01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#espacios_conjuro.nv2_usados
    evaluate: false
    value: 0
```

### 💰 Monedero Personal de Moxy

```meta-bind-button
label: 💰 Gestionar Monedero de Moxy (Añadir / Gastar)
icon: coins
style: primary
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/gestionar_monedero.md
```

| 🟤 Cobre (PC) | ⚪ Plata (PP) | 🟢 Electro (PE) | 🟡 Oro (PO) | 🔘 Platino (PPT) |
| :---: | :---: | :---: | :---: | :---: |
| `INPUT[number:01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#monedas.pc]` | `INPUT[number:01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#monedas.pp]` | `INPUT[number:01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#monedas.pe]` | `INPUT[number:01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#monedas.po]` | `INPUT[number:01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md#monedas.ppt]` |

---

## 🛡️ Miembros de la Party (Grupo Aventurero)

```dataview
TABLE jugador AS "Jugador", raza AS "Raza", clase AS "Clase", subclase AS "Subclase", rol_combate AS "Rol / Función", estado AS "Estado"
FROM "01 - Campañas/Bilbo Volador/02 - Personajes"
WHERE tipo = "pj" OR tipo = "compañero"
SORT jugador ASC
```

---

## 👥 NPCs y Contactos del Mundo

```dataview
TABLE raza AS "Raza", clase_o_rol AS "Rol / Oficio", faccion AS "Facción", actitud AS "Actitud", estado AS "Estado"
FROM "01 - Campañas/Bilbo Volador/03 - NPCs"
WHERE tipo = "npc"
SORT actitud DESC, file.name ASC
```

---

## 📜 Últimas Sesiones Jugadas

```dataview
TABLE fecha_real AS "Fecha Real", lugar_fin AS "Destino/Fin"
FROM "01 - Campañas/Bilbo Volador/01 - Sesiones"
WHERE tipo = "sesion"
SORT file.name DESC
LIMIT 5
```

---

## 🎯 Misiones Activas y Cabos Sueltos

```dataview
TABLE prioridad AS "Prioridad", dada_por AS "Otorgada por", ubicacion AS "Lugar", recompensa AS "Recompensa"
FROM "01 - Campañas/Bilbo Volador/04 - Misiones"
WHERE tipo = "mision" AND estado = "Activa"
SORT prioridad DESC
```

---

## 🏰 Lugares Clave

```dataview
TABLE tipo_lugar AS "Tipo", region AS "Región", gobernante AS "Gobernante", peligro AS "Peligro"
FROM "01 - Campañas/Bilbo Volador/05 - Lugares"
WHERE tipo = "lugar"
SORT file.name ASC
```

---

## 🧪 Consumibles y Pociones de Uso Rápido

```dataview
TABLE cantidad AS "Stock", portador AS "Portador / Reparto", rareza AS "Rareza", categoria AS "Categoría"
FROM "01 - Campañas/Bilbo Volador/07 - Inventario"
WHERE tipo = "objeto" AND (contains(lower(string(categoria)), "consumible") OR contains(lower(string(categoria)), "poción") OR contains(lower(string(categoria)), "pocion"))
SORT file.name ASC
```

---

## 🎒 Inventario y Objetos Relevantes

```dataview
TABLE cantidad AS "Cant.", categoria AS "Categoría", rareza AS "Rareza", portador AS "Portador", sintonizacion AS "Sintonización"
FROM "01 - Campañas/Bilbo Volador/07 - Inventario"
WHERE tipo = "objeto" AND !contains(lower(string(categoria)), "consumible") AND !contains(lower(string(categoria)), "poción") AND !contains(lower(string(categoria)), "pocion")
SORT file.name ASC
```
