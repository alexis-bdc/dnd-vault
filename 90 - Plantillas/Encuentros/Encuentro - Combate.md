---
tipo: encuentro
tipo_encuentro: Combate
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
estado: Preparado # Preparado / Jugado / Descartado
sesion: "" # sesión para la que está planeado: "[[Sesión 03]]"
jugado_en: "" # se llena solo al marcarlo en la sesión
ubicacion: ""
mapa: "" # "[[cueva.jpg]]" (imagen en <campaña>/10 - Mapas/Encuentros/)
escena_planarally: "" # nombre de la escena/ubicación en PlanarAlly
dificultad_objetivo: Moderada # Baja / Moderada / Alta
enemigos_cr: [] # un CR por enemigo, ej: ["1/4", "1/4", "1/4", 2]
tags:
  - dnd/encuentro
  - dnd/dm
---

# ⚔️ <% tp.file.title %>

## 🗺️ Mapa
```dataviewjs
await dv.view("90 - Plantillas/Scripts/mapa-encuentro")
```

## 📊 Dificultad
```dataviewjs
await dv.view("90 - Plantillas/Scripts/dificultad")
```

## 🎯 Situación
- **Por qué pelean / qué quieren los enemigos:** 
- **Cómo empieza (emboscada, negociación que sale mal, los PJ atacan…):** 

## 👹 Enemigos
| Enemigo | Cant. | CR | CA | PG | Notas |
| :--- | :---: | :---: | :---: | :---: | :--- |
|  |  |  |  |  |  |

> Statblock del SRD (nombre en inglés, ej. Goblin):
> ```statblock
> monster: Goblin
> ```

## 🗺️ Terreno (2-3 rasgos)
- 

## 🧠 Tácticas
- **Al empezar:** 
- **Si van perdiendo (mitad de PG / líder caído):** 

## 🌀 Complicación (ronda 2-3)
- 

## 💰 Botín
> Marca lo que se llevaron.
- [ ] 
- [ ] 

## 📝 Resultado
- 
