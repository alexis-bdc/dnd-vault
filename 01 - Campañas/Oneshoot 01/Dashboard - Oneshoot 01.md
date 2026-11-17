---
tipo: dashboard
rol: dm
campaña: "Oneshoot 01"
tags:
  - dnd/dashboard
  - dnd/dm
---

# 🎲 Oneshoot 01 (DM)

## ⏳ Amenaza principal
**Quién / qué:** 
**Qué quiere:** 

Reloj (marca un paso cuando los PJ no la frenan):
1. [ ] 
2. [ ] 
3. [ ] 
4. [ ] 
5. [ ] ¿Qué pasa si llega al final?

---

## 🛡️ Party
```dataview
TABLE jugador AS "Jugador", clase AS "Clase", nivel AS "Nv", ca AS "CA", pg_max AS "PG", percepcion_pasiva AS "PP", estado AS "Estado"
FROM "01 - Campañas"
WHERE tipo = "pj" AND startswith(file.folder, this.file.folder)
SORT jugador ASC
```

## 🔍 Cabos sueltos abiertos
```dataview
TASK
FROM "01 - Campañas"
WHERE !completed AND text != "" AND startswith(file.folder, this.file.folder + "/01 - Sesiones") AND contains(meta(section).subpath, "Cabos sueltos")
GROUP BY file.link
```

---

## ⚔️ Encuentros

```meta-bind-button
label: ⚡ Generar encuentro rápido
icon: zap
style: primary
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/generar_encuentro.md
```

### Preparados (sin jugar)
```dataview
TABLE tipo_encuentro AS "Tipo", sesion AS "Planeado para", ubicacion AS "Dónde"
FROM "01 - Campañas"
WHERE tipo = "encuentro" AND estado = "Preparado" AND startswith(file.folder, this.file.folder)
SORT file.mtime DESC
```

### 💰 Botín sin entregar
```dataview
TASK
FROM "01 - Campañas"
WHERE !completed AND text != "" AND startswith(file.folder, this.file.folder + "/09 - Encuentros") AND (contains(meta(section).subpath, "Botín") OR contains(meta(section).subpath, "Recompensa"))
GROUP BY file.link
```

## 🎯 Misiones activas
```dataview
TABLE prioridad AS "Prioridad", dada_por AS "Otorgada por", ubicacion AS "Lugar"
FROM "01 - Campañas"
WHERE tipo = "mision" AND estado = "Activa" AND startswith(file.folder, this.file.folder)
SORT prioridad ASC
```

## 📜 Últimas sesiones
```dataview
TABLE fecha_real AS "Fecha", lugar_fin AS "Terminó en"
FROM "01 - Campañas"
WHERE tipo = "sesion" AND startswith(file.folder, this.file.folder)
SORT file.name DESC
LIMIT 5
```

## 👥 PNJ
```dataview
TABLE clase_o_rol AS "Rol", ubicacion AS "Dónde", actitud AS "Actitud", estado AS "Estado"
FROM "01 - Campañas"
WHERE tipo = "npc" AND startswith(file.folder, this.file.folder)
SORT file.name ASC
```

## 🏰 Facciones
```dataview
TABLE lider AS "Líder", relacion_grupo AS "Relación"
FROM "01 - Campañas"
WHERE tipo = "faccion" AND startswith(file.folder, this.file.folder)
```

---

## 🗺️ Mapas
```dataviewjs
await dv.view("90 - Plantillas/Scripts/mapas-campana")
```

---

## 💡 Ideas sueltas
- 
