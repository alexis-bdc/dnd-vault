---
tipo: mapa
campaña: "Bilbo Volador"
tags:
  - dnd/mapa
---

# 🗺️ Mapa del Mundo

> [!tip] Cómo usarlo (requiere el plugin **Leaflet**)
> 1. Guarda la imagen como `Mapa del Mundo.jpg` en esta misma carpeta (`10 - Mapas/`).
> 2. Los **lugares** aparecen solos como marcadores si su nota tiene `location: [y, x]`.
> 3. Clic derecho en el mapa → crear marcador y enlazarlo a una nota. Rueda para zoom.

```leaflet
id: mundo-bilbo-volador
image: [[Mapa del Mundo.jpg]]
height: 650px
minZoom: 1
maxZoom: 5
defaultZoom: 2
markerFolder: 01 - Campañas/Bilbo Volador/05 - Lugares
draw: true
```

## 📍 Lugares de la campaña
```dataview
TABLE tipo_lugar AS "Tipo", region AS "Región", location AS "Coordenadas"
FROM "01 - Campañas"
WHERE tipo = "lugar" AND startswith(file.folder, "01 - Campañas/Bilbo Volador")
SORT region ASC, file.name ASC
```
