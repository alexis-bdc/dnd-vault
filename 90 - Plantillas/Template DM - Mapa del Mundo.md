---
tipo: mapa
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
tags:
  - dnd/mapa
---

# 🗺️ Mapa del Mundo

> [!tip] Cómo usarlo (requiere el plugin **Leaflet**)
> 1. Guarda la imagen como `Mapa del Mundo.jpg` en esta misma carpeta (`10 - Mapas/`).
> 2. Los **lugares** aparecen solos como marcadores si su nota tiene `location: [y, x]`.
> 3. Clic derecho en el mapa → crear marcador y enlazarlo a una nota. Rueda para zoom.

```leaflet
id: mundo-<% tp.file.folder(true).split('/')[1].toLowerCase().replace(/[^a-z0-9]+/g, '-') %>
image: [[Mapa del Mundo.jpg]]
height: 650px
minZoom: 1
maxZoom: 5
defaultZoom: 2
markerFolder: <% tp.file.folder(true).split('/').slice(0, 2).join('/') %>/05 - Lugares
draw: true
```

## 📍 Lugares de la campaña
```dataview
TABLE tipo_lugar AS "Tipo", region AS "Región", location AS "Coordenadas"
FROM "01 - Campañas"
WHERE tipo = "lugar" AND startswith(file.folder, "<% tp.file.folder(true).split('/').slice(0, 2).join('/') %>")
SORT region ASC, file.name ASC
```
