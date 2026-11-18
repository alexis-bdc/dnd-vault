---
tipo: mapa
campaña: "Tierra de Bloques"
semilla: "-4697940382757111526"
version: "1.21"
dimension: overworld
tags:
  - dnd/mapa
---

# 🗺️ Mapa del Mundo

Semilla **-4697940382757111526** · Java 1.21 · 8000×8000 bloques centrados en 0,0 · generado con cubiomes.
Cada cuadro de la cuadrícula = 500 bloques = 1 hora a pie (½ a caballo).

> [!tip] Cómo usarlo (plugin **Leaflet**)
> - **Medir:** Shift + clic en un punto y Shift + clic en otro. La distancia sale en bloques (abajo a la izquierda).
> - **Horas de viaje:** bloques ÷ 500 a pie, ÷ 1000 a caballo o en barco, y ÷ 8 adicional por el Nether.
> - **Pasa el ratón** por un icono o una ruta para ver qué es.
> - **Coordenadas:** el mapa usa las del juego. En `location: [lat, long]` de un lugar pon **[−Z, X]** (la Z cambia de signo para que el norte quede arriba).
> - Clic derecho → crear marcador propio.

```leaflet
id: mapa-del-mundo-tierra-de-bloques
image: [[Mapa del Mundo.png]]
bounds:
    - [4000, -4000]
    - [-4000, 4000]
height: 700px
minZoom: -5
maxZoom: 3
defaultZoom: -3
zoomDelta: 0.5
unit: bloques
scale: 1
markerFolder: 01 - Campañas/Tierra de Bloques/05 - Lugares
draw: true
geojson: [[Rutas - Mapa del Mundo.geojson]]
marker:
    - "bruja,-1184,-240,,Cabaña de bruja (X -240 · Z 1184)"
    - "bruja,-3920,2064,,Cabaña de bruja (X 2064 · Z 3920)"
    - "templo,3376,-960,,Templo del desierto (X -960 · Z -3376)"
    - "templo,3568,-176,,Templo del desierto (X -176 · Z -3568)"
    - "templo,2912,-144,,Templo del desierto (X -144 · Z -2912)"
    - "templo,1792,640,,Templo del desierto (X 640 · Z -1792)"
    - "templo,976,-416,,Templo de la jungla (X -416 · Z -976)"
    - "templo,-144,752,,Templo de la jungla (X 752 · Z 144)"
    - "saqueadores,3808,2384,,Puesto de saqueadores (X 2384 · Z -3808)"
    - "saqueadores,3968,2848,,Puesto de saqueadores (X 2848 · Z -3968)"
    - "saqueadores,3584,3408,,Puesto de saqueadores (X 3408 · Z -3584)"
    - "saqueadores,2368,-288,,Puesto de saqueadores (X -288 · Z -2368)"
    - "saqueadores,2016,-144,,Puesto de saqueadores (X -144 · Z -2016)"
    - "saqueadores,1488,1184,,Puesto de saqueadores (X 1184 · Z -1488)"
    - "saqueadores,784,-2512,,Puesto de saqueadores (X -2512 · Z -784)"
    - "saqueadores,880,3952,,Puesto de saqueadores (X 3952 · Z -880)"
    - "saqueadores,-736,-2048,,Puesto de saqueadores (X -2048 · Z 736)"
    - "saqueadores,-1024,-1184,,Puesto de saqueadores (X -1184 · Z 1024)"
    - "saqueadores,-1776,-2320,,Puesto de saqueadores (X -2320 · Z 1776)"
    - "saqueadores,-3168,128,,Puesto de saqueadores (X 128 · Z 3168)"
    - "saqueadores,-3792,-2416,,Puesto de saqueadores (X -2416 · Z 3792)"
    - "aldea,3728,-2384,,Aldea 64 (X -2384 · Z -3728)"
    - "aldea,3536,-1792,,Aldea 52 (X -1792 · Z -3536)"
    - "aldea,3488,-272,,Aldea 42 (X -272 · Z -3488)"
    - "puerto,3776,368,,Aldea 51 ⚓ puerto (X 368 · Z -3776)"
    - "puerto,3536,1872,,Aldea 53 ⚓ puerto (X 1872 · Z -3536)"
    - "aldea,3440,2576,,Aldea 63 (X 2576 · Z -3440)"
    - "aldea,3680,3664,,Aldea 68 (X 3664 · Z -3680)"
    - "aldea,3488,3904,,Aldea 69 (X 3904 · Z -3488)"
    - "aldea,3040,-2688,,Aldea 58 (X -2688 · Z -3040)"
    - "aldea,2960,-2176,,Aldea 48 (X -2176 · Z -2960)"
    - "aldea,3232,2432,,Aldea 56 (X 2432 · Z -3232)"
    - "aldea,2880,3632,,Aldea 66 (X 3632 · Z -2880)"
    - "aldea,3232,3904,,Aldea 67 (X 3904 · Z -3232)"
    - "puerto,1952,720,,Aldea 8 ⚓ puerto (X 720 · Z -1952)"
    - "puerto,1968,1680,,Aldea 13 ⚓ puerto (X 1680 · Z -1968)"
    - "aldea,1280,-2528,,Aldea 20 (X -2528 · Z -1280)"
    - "puerto,1504,32,,Aldea 4 ⚓ puerto (X 32 · Z -1504)"
    - "puerto,1632,720,,Aldea 6 ⚓ puerto (X 720 · Z -1632)"
    - "aldea,1616,1728,,Aldea 12 (X 1728 · Z -1616)"
    - "aldea,1328,2496,,Aldea 19 (X 2496 · Z -1328)"
    - "aldea,1344,3488,,Aldea 49 (X 3488 · Z -1344)"
    - "aldea,1520,3968,,Aldea 61 (X 3968 · Z -1520)"
    - "aldea,992,-2624,,Aldea 18 (X -2624 · Z -992)"
    - "aldea,800,-1952,,Aldea 10 (X -1952 · Z -800)"
    - "aldea,880,160,,Aldea 2 (X 160 · Z -880)"
    - "aldea,880,2192,,Aldea 11 (X 2192 · Z -880)"
    - "aldea,1088,2880,,Aldea 28 (X 2880 · Z -1088)"
    - "aldea,752,3552,,Aldea 46 (X 3552 · Z -752)"
    - "aldea,544,-3408,,Aldea 37 (X -3408 · Z -544)"
    - "aldea,528,-2992,,Aldea 26 (X -2992 · Z -528)"
    - "aldea,256,-2640,,Aldea 14 (X -2640 · Z -256)"
    - "aldea,464,400,,Aldea 1 (X 400 · Z -464)"
    - "aldea,320,3120,,Aldea 30 (X 3120 · Z -320)"
    - "aldea,368,3600,,Aldea 45 (X 3600 · Z -368)"
    - "aldea,-48,-4000,,Aldea 54 (X -4000 · Z 48)"
    - "aldea,-400,-2864,,Aldea 21 (X -2864 · Z 400)"
    - "aldea,-608,-2912,,Aldea 24 (X -2912 · Z 608)"
    - "aldea,-576,-2624,,Aldea 15 (X -2624 · Z 576)"
    - "aldea,-544,-1968,,Aldea 7 (X -1968 · Z 544)"
    - "aldea,-624,-1616,,Aldea 5 (X -1616 · Z 624)"
    - "aldea,-944,-848,,Aldea 3 (X -848 · Z 944)"
    - "aldea,-640,3424,,Aldea 39 (X 3424 · Z 640)"
    - "aldea,-1216,-3264,,Aldea 40 (X -3264 · Z 1216)"
    - "aldea,-1440,-2592,,Aldea 23 (X -2592 · Z 1440)"
    - "aldea,-1456,-1520,,Aldea 9 (X -1520 · Z 1456)"
    - "aldea,-1936,1920,,Aldea 16 (X 1920 · Z 1936)"
    - "aldea,-1904,2384,,Aldea 25 (X 2384 · Z 1904)"
    - "aldea,-1840,2944,,Aldea 38 (X 2944 · Z 1840)"
    - "aldea,-2528,-3216,,Aldea 59 (X -3216 · Z 2528)"
    - "aldea,-2320,-2320,,Aldea 33 (X -2320 · Z 2320)"
    - "aldea,-2352,-2000,,Aldea 29 (X -2000 · Z 2352)"
    - "aldea,-2400,-1392,,Aldea 17 (X -1392 · Z 2400)"
    - "aldea,-2176,1936,,Aldea 22 (X 1936 · Z 2176)"
    - "aldea,-2320,2528,,Aldea 35 (X 2528 · Z 2320)"
    - "aldea,-2240,2816,,Aldea 44 (X 2816 · Z 2240)"
    - "aldea,-3024,-3408,,Aldea 65 (X -3408 · Z 3024)"
    - "aldea,-2768,-2432,,Aldea 47 (X -2432 · Z 2768)"
    - "aldea,-2784,-1280,,Aldea 27 (X -1280 · Z 2784)"
    - "aldea,-2992,-976,,Aldea 31 (X -976 · Z 2992)"
    - "aldea,-3120,-432,,Aldea 32 (X -432 · Z 3120)"
    - "aldea,-2992,1840,,Aldea 41 (X 1840 · Z 2992)"
    - "aldea,-3120,2720,,Aldea 60 (X 2720 · Z 3120)"
    - "aldea,-3552,-1984,,Aldea 57 (X -1984 · Z 3552)"
    - "aldea,-3280,-1280,,Aldea 43 (X -1280 · Z 3280)"
    - "aldea,-3376,-768,,Aldea 36 (X -768 · Z 3376)"
    - "aldea,-3344,-240,,Aldea 34 (X -240 · Z 3344)"
    - "aldea,-3328,1808,,Aldea 50 (X 1808 · Z 3328)"
    - "aldea,-3264,2352,,Aldea 55 (X 2352 · Z 3264)"
    - "aldea,-3888,1840,,Aldea 62 (X 1840 · Z 3888)"
    - "monumento,3344,-3968,,Monumento oceánico (X -3968 · Z -3344)"
    - "monumento,3408,-3376,,Monumento oceánico (X -3376 · Z -3408)"
    - "monumento,3360,832,,Monumento oceánico (X 832 · Z -3360)"
    - "monumento,2896,-3792,,Monumento oceánico (X -3792 · Z -2896)"
    - "monumento,2736,-3440,,Monumento oceánico (X -3440 · Z -2736)"
    - "monumento,3056,800,,Monumento oceánico (X 800 · Z -3056)"
    - "monumento,2880,1328,,Monumento oceánico (X 1328 · Z -2880)"
    - "monumento,2912,1632,,Monumento oceánico (X 1632 · Z -2912)"
    - "monumento,2464,-3920,,Monumento oceánico (X -3920 · Z -2464)"
    - "monumento,2384,-3344,,Monumento oceánico (X -3344 · Z -2384)"
    - "monumento,2288,-2864,,Monumento oceánico (X -2864 · Z -2288)"
    - "monumento,1968,-3888,,Monumento oceánico (X -3888 · Z -1968)"
    - "monumento,1792,-3312,,Monumento oceánico (X -3312 · Z -1792)"
    - "monumento,1248,-3408,,Monumento oceánico (X -3408 · Z -1248)"
    - "monumento,1408,-976,,Monumento oceánico (X -976 · Z -1408)"
    - "monumento,992,1152,,Monumento oceánico (X 1152 · Z -992)"
    - "monumento,336,-1136,,Monumento oceánico (X -1136 · Z -336)"
    - "monumento,352,-816,,Monumento oceánico (X -816 · Z -352)"
    - "monumento,-64,-1968,,Monumento oceánico (X -1968 · Z 64)"
    - "monumento,-768,48,,Monumento oceánico (X 48 · Z 768)"
    - "monumento,-784,1168,,Monumento oceánico (X 1168 · Z 784)"
    - "monumento,-1200,656,,Monumento oceánico (X 656 · Z 1200)"
    - "monumento,-1776,608,,Monumento oceánico (X 608 · Z 1776)"
    - "monumento,-2256,-320,,Monumento oceánico (X -320 · Z 2256)"
    - "monumento,-2080,144,,Monumento oceánico (X 144 · Z 2080)"
    - "monumento,-2816,720,,Monumento oceánico (X 720 · Z 2816)"
    - "monumento,-2768,1152,,Monumento oceánico (X 1152 · Z 2768)"
    - "monumento,-3248,752,,Monumento oceánico (X 752 · Z 3248)"
    - "monumento,-3776,736,,Monumento oceánico (X 736 · Z 3776)"
    - "monumento,-3776,1056,,Monumento oceánico (X 1056 · Z 3776)"
    - "mansion,656,-832,,Mansión del bosque (X -832 · Z -656)"
    - "ciudad,3840,2496,,Ciudad antigua (X 2496 · Z -3840)"
    - "ciudad,3456,2048,,Ciudad antigua (X 2048 · Z -3456)"
    - "ciudad,2960,-2464,,Ciudad antigua (X -2464 · Z -2960)"
    - "ciudad,2640,-2448,,Ciudad antigua (X -2448 · Z -2640)"
    - "ciudad,-432,3136,,Ciudad antigua (X 3136 · Z 432)"
    - "fortaleza_end,-596,2052,,Fortaleza del End (X 2052 · Z 596)"
    - "fortaleza_end,-1396,-1548,,Fortaleza del End (X -1548 · Z 1396)"
    - "fortaleza_end,1772,-492,,Fortaleza del End (X -492 · Z -1772)"
    - "fortaleza_end,3820,2388,,Fortaleza del End (X 2388 · Z -3820)"
    - "spawn,-8,8,,Punto de aparición (X 8 · Z 8)"
```

## 📍 Estructuras en el mapa
| Estructura            | Cantidad |
| --------------------- | -------- |
| Aldea                 | 69       |
| Cabaña de bruja       | 2        |
| Ciudad antigua        | 5        |
| Cámaras de desafío    | 200      |
| Fortaleza del End     | 4        |
| Iglú                  | 32       |
| Mansión del bosque    | 1        |
| Monumento oceánico    | 30       |
| Portal en ruinas      | 155      |
| Puesto de saqueadores | 13       |
| Punto de aparición    | 1        |
| Ruinas de sendero     | 38       |
| Templo de la jungla   | 2        |
| Templo del desierto   | 4        |

## 🛤️ Caminos y rutas marítimas
Red mínima que une todas las aldeas. Los caminos rodean el mar y cruzan los ríos con puente; si por tierra hay que dar un rodeo de más del doble, se va en barco entre puertos (⚓).

| Ruta | Tipo | Bloques | Tiempo |
|---|---|---|---|
| Aldea 1 ↔ Aldea 2 | 🛤️ Camino | 490 | 1.0 h a pie (0.5 h a caballo) |
| Aldea 2 ↔ Aldea 4 | 🛤️ Camino | 693 | 1.4 h a pie (0.7 h a caballo) |
| Aldea 3 ↔ Aldea 5 | 🛤️ Camino | 1210 | 2.4 h a pie (1.2 h a caballo) |
| Aldea 4 ↔ Aldea 6 | ⛵ Mar | 757 | 0.8 h en barco |
| Aldea 5 ↔ Aldea 7 | 🛤️ Camino | 347 | 0.7 h a pie (0.3 h a caballo) |
| Aldea 5 ↔ Aldea 9 | 🛤️ Camino | 938 | 1.9 h a pie (0.9 h a caballo) |
| Aldea 6 ↔ Aldea 8 | 🛤️ Camino | 320 | 0.6 h a pie (0.3 h a caballo) |
| Aldea 7 ↔ Aldea 15 | 🛤️ Camino | 667 | 1.3 h a pie (0.7 h a caballo) |
| Aldea 8 ↔ Aldea 13 | ⛵ Mar | 1066 | 1.1 h en barco |
| Aldea 10 ↔ Aldea 18 | 🛤️ Camino | 720 | 1.4 h a pie (0.7 h a caballo) |
| Aldea 11 ↔ Aldea 19 | 🛤️ Camino | 581 | 1.2 h a pie (0.6 h a caballo) |
| Aldea 12 ↔ Aldea 13 | 🛤️ Camino | 347 | 0.7 h a pie (0.3 h a caballo) |
| Aldea 12 ↔ Aldea 19 | 🛤️ Camino | 901 | 1.8 h a pie (0.9 h a caballo) |
| Aldea 14 ↔ Aldea 21 | 🛤️ Camino | 784 | 1.6 h a pie (0.8 h a caballo) |
| Aldea 14 ↔ Aldea 26 | 🛤️ Camino | 426 | 0.9 h a pie (0.4 h a caballo) |
| Aldea 15 ↔ Aldea 24 | 🛤️ Camino | 320 | 0.6 h a pie (0.3 h a caballo) |
| Aldea 16 ↔ Aldea 22 | 🛤️ Camino | 219 | 0.4 h a pie (0.2 h a caballo) |
| Aldea 16 ↔ Aldea 25 | 🛤️ Camino | 539 | 1.1 h a pie (0.5 h a caballo) |
| Aldea 17 ↔ Aldea 27 | 🛤️ Camino | 411 | 0.8 h a pie (0.4 h a caballo) |
| Aldea 17 ↔ Aldea 29 | 🛤️ Camino | 773 | 1.5 h a pie (0.8 h a caballo) |
| Aldea 18 ↔ Aldea 20 | 🛤️ Camino | 347 | 0.7 h a pie (0.3 h a caballo) |
| Aldea 18 ↔ Aldea 26 | 🛤️ Camino | 607 | 1.2 h a pie (0.6 h a caballo) |
| Aldea 19 ↔ Aldea 28 | 🛤️ Camino | 543 | 1.1 h a pie (0.5 h a caballo) |
| Aldea 20 ↔ Aldea 48 | 🛤️ Camino | 1797 | 3.6 h a pie (1.8 h a caballo) |
| Aldea 21 ↔ Aldea 24 | 🛤️ Camino | 219 | 0.4 h a pie (0.2 h a caballo) |
| Aldea 22 ↔ Aldea 41 | 🛤️ Camino | 885 | 1.8 h a pie (0.9 h a caballo) |
| Aldea 23 ↔ Aldea 33 | 🛤️ Camino | 1002 | 2.0 h a pie (1.0 h a caballo) |
| Aldea 23 ↔ Aldea 40 | 🛤️ Camino | 720 | 1.4 h a pie (0.7 h a caballo) |
| Aldea 24 ↔ Aldea 40 | 🛤️ Camino | 773 | 1.5 h a pie (0.8 h a caballo) |
| Aldea 25 ↔ Aldea 35 | 🛤️ Camino | 501 | 1.0 h a pie (0.5 h a caballo) |
| Aldea 26 ↔ Aldea 37 | 🛤️ Camino | 501 | 1.0 h a pie (0.5 h a caballo) |
| Aldea 27 ↔ Aldea 31 | 🛤️ Camino | 400 | 0.8 h a pie (0.4 h a caballo) |
| Aldea 28 ↔ Aldea 49 | 🛤️ Camino | 682 | 1.4 h a pie (0.7 h a caballo) |
| Aldea 29 ↔ Aldea 33 | 🛤️ Camino | 320 | 0.6 h a pie (0.3 h a caballo) |
| Aldea 30 ↔ Aldea 39 | 🛤️ Camino | 1029 | 2.1 h a pie (1.0 h a caballo) |
| Aldea 30 ↔ Aldea 45 | 🛤️ Camino | 645 | 1.3 h a pie (0.6 h a caballo) |
| Aldea 31 ↔ Aldea 36 | 🛤️ Camino | 464 | 0.9 h a pie (0.5 h a caballo) |
| Aldea 31 ↔ Aldea 43 | 🛤️ Camino | 453 | 0.9 h a pie (0.5 h a caballo) |
| Aldea 32 ↔ Aldea 34 | 🛤️ Camino | 336 | 0.7 h a pie (0.3 h a caballo) |
| Aldea 32 ↔ Aldea 36 | 🛤️ Camino | 528 | 1.1 h a pie (0.5 h a caballo) |
| Aldea 33 ↔ Aldea 47 | 🛤️ Camino | 501 | 1.0 h a pie (0.5 h a caballo) |
| Aldea 35 ↔ Aldea 44 | 🛤️ Camino | 283 | 0.6 h a pie (0.3 h a caballo) |
| Aldea 37 ↔ Aldea 54 | 🛤️ Camino | 890 | 1.8 h a pie (0.9 h a caballo) |
| Aldea 38 ↔ Aldea 39 | 🛤️ Camino | 2137 | 4.3 h a pie (2.1 h a caballo) |
| Aldea 38 ↔ Aldea 44 | 🛤️ Camino | 501 | 1.0 h a pie (0.5 h a caballo) |
| Aldea 41 ↔ Aldea 50 | 🛤️ Camino | 320 | 0.6 h a pie (0.3 h a caballo) |
| Aldea 42 ↔ Aldea 51 | 🛤️ Camino | 746 | 1.5 h a pie (0.7 h a caballo) |
| Aldea 42 ↔ Aldea 52 | 🛤️ Camino | 1669 | 3.3 h a pie (1.7 h a caballo) |
| Aldea 43 ↔ Aldea 57 | 🛤️ Camino | 799 | 1.6 h a pie (0.8 h a caballo) |
| Aldea 45 ↔ Aldea 46 | 🛤️ Camino | 411 | 0.8 h a pie (0.4 h a caballo) |
| Aldea 46 ↔ Aldea 49 | 🛤️ Camino | 656 | 1.3 h a pie (0.7 h a caballo) |
| Aldea 47 ↔ Aldea 59 | 🛤️ Camino | 874 | 1.7 h a pie (0.9 h a caballo) |
| Aldea 48 ↔ Aldea 52 | 🛤️ Camino | 735 | 1.5 h a pie (0.7 h a caballo) |
| Aldea 48 ↔ Aldea 58 | 🛤️ Camino | 539 | 1.1 h a pie (0.5 h a caballo) |
| Aldea 49 ↔ Aldea 61 | 🛤️ Camino | 565 | 1.1 h a pie (0.6 h a caballo) |
| Aldea 50 ↔ Aldea 55 | 🛤️ Camino | 565 | 1.1 h a pie (0.6 h a caballo) |
| Aldea 50 ↔ Aldea 62 | 🛤️ Camino | 576 | 1.2 h a pie (0.6 h a caballo) |
| Aldea 51 ↔ Aldea 53 | ⛵ Mar | 1669 | 1.7 h en barco |
| Aldea 52 ↔ Aldea 64 | 🛤️ Camino | 656 | 1.3 h a pie (0.7 h a caballo) |
| Aldea 53 ↔ Aldea 56 | 🛤️ Camino | 645 | 1.3 h a pie (0.6 h a caballo) |
| Aldea 55 ↔ Aldea 60 | 🛤️ Camino | 645 | 1.3 h a pie (0.6 h a caballo) |
| Aldea 56 ↔ Aldea 63 | 🛤️ Camino | 272 | 0.5 h a pie (0.3 h a caballo) |
| Aldea 59 ↔ Aldea 65 | 🛤️ Camino | 682 | 1.4 h a pie (0.7 h a caballo) |
| Aldea 61 ↔ Aldea 66 | 🛤️ Camino | 1477 | 3.0 h a pie (1.5 h a caballo) |
| Aldea 63 ↔ Aldea 68 | 🛤️ Camino | 1194 | 2.4 h a pie (1.2 h a caballo) |
| Aldea 66 ↔ Aldea 67 | 🛤️ Camino | 517 | 1.0 h a pie (0.5 h a caballo) |
| Aldea 67 ↔ Aldea 69 | 🛤️ Camino | 256 | 0.5 h a pie (0.3 h a caballo) |
| Aldea 68 ↔ Aldea 69 | 🛤️ Camino | 336 | 0.7 h a pie (0.3 h a caballo) |

## 🧭 Iconos de Leaflet
🏠 Aldea · ⚓ Aldea con puerto · 🚩 Puesto de saqueadores · 🏚️ Mansión · 🌊 Monumento oceánico · 🗿 Templo · 🧙 Cabaña de bruja · 💀 Ciudad antigua · ♜ Fortaleza del End · ⭐ Punto de aparición

## 🎨 Leyenda de la imagen
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
- Líneas oscuras: cuadrícula cada 500 bloques.

> [!warning] Aproximado
> Las estructuras se calculan por bioma. En el juego alguna puede no generarse por el terreno (sobre todo aldeas en laderas).
