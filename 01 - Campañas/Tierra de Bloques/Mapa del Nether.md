---
tipo: mapa
campaña: "Tierra de Bloques"
semilla: "-4697940382757111526"
version: "1.21"
dimension: nether
tags:
  - dnd/mapa
---

# 🗺️ Mapa del Nether

Semilla **-4697940382757111526** · Java 1.21 · 2000×2000 bloques centrados en 0,0 · generado con cubiomes.
1 bloque del Nether = 8 del mundo: 1 h de viaje aquí = 8 h en la superficie.
Qué se puede encontrar en cada lugar: [[Botín por Lugar]].

> [!tip] Cómo usarlo (plugin **Leaflet**)
> - **Medir:** Shift + clic en un punto y Shift + clic en otro. La distancia sale en bloques (abajo a la izquierda).
> - **Horas de viaje:** bloques ÷ 500 a pie, ÷ 1000 a caballo o en barco, y ÷ 8 adicional por el Nether.
> - **Pasa el ratón** por un icono o una ruta para ver qué es.
> - **Coordenadas:** el mapa usa las del juego. En `location: [lat, long]` de un lugar pon **[−Z, X]** (la Z cambia de signo para que el norte quede arriba).
> - Clic derecho → crear marcador propio.

```leaflet
id: mapa-del-nether-tierra-de-bloques
image: [[Mapa del Nether.png]]
bounds:
    - [1000, -1000]
    - [-1000, 1000]
height: 700px
minZoom: -5
maxZoom: 3
defaultZoom: -3
zoomDelta: 0.5
unit: bloques
scale: 1
markerFolder: 01 - Campañas/Tierra de Bloques/05 - Lugares
draw: true
marker:
    - "fortaleza_nether,640,-784,,Fortaleza del Nether (X -784 · Z -640)"
    - "fortaleza_nether,768,560,,Fortaleza del Nether (X 560 · Z -768)"
    - "fortaleza_nether,736,912,,Fortaleza del Nether (X 912 · Z -736)"
    - "fortaleza_nether,240,-688,,Fortaleza del Nether (X -688 · Z -240)"
    - "fortaleza_nether,80,-128,,Fortaleza del Nether (X -128 · Z -80)"
    - "fortaleza_nether,96,112,,Fortaleza del Nether (X 112 · Z -96)"
    - "fortaleza_nether,-224,-624,,Fortaleza del Nether (X -624 · Z 224)"
    - "fortaleza_nether,-176,432,,Fortaleza del Nether (X 432 · Z 176)"
    - "fortaleza_nether,-768,-96,,Fortaleza del Nether (X -96 · Z 768)"
    - "fortaleza_nether,-672,320,,Fortaleza del Nether (X 320 · Z 672)"
    - "fortaleza_nether,-480,432,,Fortaleza del Nether (X 432 · Z 480)"
    - "bastion,736,-112,,Bastión (X -112 · Z -736)"
    - "bastion,512,256,,Bastión (X 256 · Z -512)"
    - "bastion,224,688,,Bastión (X 688 · Z -224)"
    - "bastion,-304,-256,,Bastión (X -256 · Z 304)"
    - "bastion,-272,112,,Bastión (X 112 · Z 272)"
    - "bastion,-112,992,,Bastión (X 992 · Z 112)"
    - "bastion,-784,-688,,Bastión (X -688 · Z 784)"
    - "bastion,-544,992,,Bastión (X 992 · Z 544)"
    - "bastion,-880,688,,Bastión (X 688 · Z 880)"
```

## 📍 Estructuras en el mapa
| Estructura | Cantidad |
|---|---|
| Bastión | 9 |
| Fortaleza del Nether | 11 |
| Portal en ruinas | 10 |

## 🧭 Iconos de Leaflet
🏠 Aldea · ⚓ Aldea con puerto · 🚩 Puesto de saqueadores · 🏚️ Mansión · 🌊 Monumento oceánico · 🗿 Templo · 🧙 Cabaña de bruja · 💀 Ciudad antigua · ♜ Fortaleza del End · 🔑 Cámaras de desafío · ⭐ Punto de aparición

## 🌍 Biomas (colores del mapa)
Ordenados de más a menos extensión. El mapa se toma a nivel del mar: donde hay colinas o montañas sale el bioma de la cueva que hay debajo (manchas marrones y verde oscuro).

| Color | Bioma | Del mapa | En la partida |
|---|---|---|---|
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(87,37,38);border:1px solid #000"></span> | Páramo del Nether | 41.1 % | Cuarzo, ghasts, piglins zombificados |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(100,95,99);border:1px solid #000"></span> | Deltas de basalto | 18.5 % | Cubos de magma; terreno difícil |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(77,58,46);border:1px solid #000"></span> | Valle de arena de almas | 18.5 % | Esqueletos, ghasts; terreno lento |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(152,26,17);border:1px solid #000"></span> | Bosque carmesí | 18.3 % | Piglins, hoglins |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(73,144,123);border:1px solid #000"></span> | Bosque distorsionado | 3.7 % | Endermen; zona tranquila |

## 🎨 Estructuras dibujadas en la imagen
- 🟨: Aldea
- ⬛ gris: Puesto de saqueadores
- 🟫: Mansión del bosque
- 🟦 cian: Monumento oceánico
- 🟧 arena: Templo del desierto
- 🟩: Templo de la jungla / cabaña de bruja (verde oscuro)
- 🟪 grande: Fortaleza del End
- 🟪 pequeño: Portal en ruinas
- ⬜: Punto de aparición / iglú
- 🟧: Cámaras de desafío
- ⬛ azul noche: Ciudad antigua
- 🟥 líneas: Ejes 0,0
- Líneas oscuras: cuadrícula cada 62 bloques.

> [!warning] Aproximado
> Las estructuras se calculan por bioma. En el juego alguna puede no generarse por el terreno (sobre todo aldeas en laderas).
