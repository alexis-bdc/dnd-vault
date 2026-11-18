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
> - **Horas de viaje:** bloques ÷ 500 a pie, ÷ 1000 a caballo, y ÷ 8 adicional por el Nether.
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
marker:
    - "default,-1184,-240,,Cabaña de bruja (X -240 · Z 1184)"
    - "default,-3920,2064,,Cabaña de bruja (X 2064 · Z 3920)"
    - "default,3376,-960,,Templo del desierto (X -960 · Z -3376)"
    - "default,3568,-176,,Templo del desierto (X -176 · Z -3568)"
    - "default,2912,-144,,Templo del desierto (X -144 · Z -2912)"
    - "default,1792,640,,Templo del desierto (X 640 · Z -1792)"
    - "default,976,-416,,Templo de la jungla (X -416 · Z -976)"
    - "default,-144,752,,Templo de la jungla (X 752 · Z 144)"
    - "default,3808,2384,,Puesto de saqueadores (X 2384 · Z -3808)"
    - "default,3968,2848,,Puesto de saqueadores (X 2848 · Z -3968)"
    - "default,3584,3408,,Puesto de saqueadores (X 3408 · Z -3584)"
    - "default,2368,-288,,Puesto de saqueadores (X -288 · Z -2368)"
    - "default,2016,-144,,Puesto de saqueadores (X -144 · Z -2016)"
    - "default,1488,1184,,Puesto de saqueadores (X 1184 · Z -1488)"
    - "default,784,-2512,,Puesto de saqueadores (X -2512 · Z -784)"
    - "default,880,3952,,Puesto de saqueadores (X 3952 · Z -880)"
    - "default,-736,-2048,,Puesto de saqueadores (X -2048 · Z 736)"
    - "default,-1024,-1184,,Puesto de saqueadores (X -1184 · Z 1024)"
    - "default,-1776,-2320,,Puesto de saqueadores (X -2320 · Z 1776)"
    - "default,-3168,128,,Puesto de saqueadores (X 128 · Z 3168)"
    - "default,-3792,-2416,,Puesto de saqueadores (X -2416 · Z 3792)"
    - "default,3728,-2384,,Aldea (X -2384 · Z -3728)"
    - "default,3536,-1792,,Aldea (X -1792 · Z -3536)"
    - "default,3488,-272,,Aldea (X -272 · Z -3488)"
    - "default,3776,368,,Aldea (X 368 · Z -3776)"
    - "default,3536,1872,,Aldea (X 1872 · Z -3536)"
    - "default,3440,2576,,Aldea (X 2576 · Z -3440)"
    - "default,3680,3664,,Aldea (X 3664 · Z -3680)"
    - "default,3488,3904,,Aldea (X 3904 · Z -3488)"
    - "default,3040,-2688,,Aldea (X -2688 · Z -3040)"
    - "default,2960,-2176,,Aldea (X -2176 · Z -2960)"
    - "default,3232,2432,,Aldea (X 2432 · Z -3232)"
    - "default,2880,3632,,Aldea (X 3632 · Z -2880)"
    - "default,3232,3904,,Aldea (X 3904 · Z -3232)"
    - "default,1952,720,,Aldea (X 720 · Z -1952)"
    - "default,1968,1680,,Aldea (X 1680 · Z -1968)"
    - "default,1280,-2528,,Aldea (X -2528 · Z -1280)"
    - "default,1504,32,,Aldea (X 32 · Z -1504)"
    - "default,1632,720,,Aldea (X 720 · Z -1632)"
    - "default,1616,1728,,Aldea (X 1728 · Z -1616)"
    - "default,1328,2496,,Aldea (X 2496 · Z -1328)"
    - "default,1344,3488,,Aldea (X 3488 · Z -1344)"
    - "default,1520,3968,,Aldea (X 3968 · Z -1520)"
    - "default,992,-2624,,Aldea (X -2624 · Z -992)"
    - "default,800,-1952,,Aldea (X -1952 · Z -800)"
    - "default,880,160,,Aldea (X 160 · Z -880)"
    - "default,880,2192,,Aldea (X 2192 · Z -880)"
    - "default,1088,2880,,Aldea (X 2880 · Z -1088)"
    - "default,752,3552,,Aldea (X 3552 · Z -752)"
    - "default,544,-3408,,Aldea (X -3408 · Z -544)"
    - "default,528,-2992,,Aldea (X -2992 · Z -528)"
    - "default,256,-2640,,Aldea (X -2640 · Z -256)"
    - "default,464,400,,Aldea (X 400 · Z -464)"
    - "default,320,3120,,Aldea (X 3120 · Z -320)"
    - "default,368,3600,,Aldea (X 3600 · Z -368)"
    - "default,-48,-4000,,Aldea (X -4000 · Z 48)"
    - "default,-400,-2864,,Aldea (X -2864 · Z 400)"
    - "default,-608,-2912,,Aldea (X -2912 · Z 608)"
    - "default,-576,-2624,,Aldea (X -2624 · Z 576)"
    - "default,-544,-1968,,Aldea (X -1968 · Z 544)"
    - "default,-624,-1616,,Aldea (X -1616 · Z 624)"
    - "default,-944,-848,,Aldea (X -848 · Z 944)"
    - "default,-640,3424,,Aldea (X 3424 · Z 640)"
    - "default,-1216,-3264,,Aldea (X -3264 · Z 1216)"
    - "default,-1440,-2592,,Aldea (X -2592 · Z 1440)"
    - "default,-1456,-1520,,Aldea (X -1520 · Z 1456)"
    - "default,-1936,1920,,Aldea (X 1920 · Z 1936)"
    - "default,-1904,2384,,Aldea (X 2384 · Z 1904)"
    - "default,-1840,2944,,Aldea (X 2944 · Z 1840)"
    - "default,-2528,-3216,,Aldea (X -3216 · Z 2528)"
    - "default,-2320,-2320,,Aldea (X -2320 · Z 2320)"
    - "default,-2352,-2000,,Aldea (X -2000 · Z 2352)"
    - "default,-2400,-1392,,Aldea (X -1392 · Z 2400)"
    - "default,-2176,1936,,Aldea (X 1936 · Z 2176)"
    - "default,-2320,2528,,Aldea (X 2528 · Z 2320)"
    - "default,-2240,2816,,Aldea (X 2816 · Z 2240)"
    - "default,-3024,-3408,,Aldea (X -3408 · Z 3024)"
    - "default,-2768,-2432,,Aldea (X -2432 · Z 2768)"
    - "default,-2784,-1280,,Aldea (X -1280 · Z 2784)"
    - "default,-2992,-976,,Aldea (X -976 · Z 2992)"
    - "default,-3120,-432,,Aldea (X -432 · Z 3120)"
    - "default,-2992,1840,,Aldea (X 1840 · Z 2992)"
    - "default,-3120,2720,,Aldea (X 2720 · Z 3120)"
    - "default,-3552,-1984,,Aldea (X -1984 · Z 3552)"
    - "default,-3280,-1280,,Aldea (X -1280 · Z 3280)"
    - "default,-3376,-768,,Aldea (X -768 · Z 3376)"
    - "default,-3344,-240,,Aldea (X -240 · Z 3344)"
    - "default,-3328,1808,,Aldea (X 1808 · Z 3328)"
    - "default,-3264,2352,,Aldea (X 2352 · Z 3264)"
    - "default,-3888,1840,,Aldea (X 1840 · Z 3888)"
    - "default,3344,-3968,,Monumento oceánico (X -3968 · Z -3344)"
    - "default,3408,-3376,,Monumento oceánico (X -3376 · Z -3408)"
    - "default,3360,832,,Monumento oceánico (X 832 · Z -3360)"
    - "default,2896,-3792,,Monumento oceánico (X -3792 · Z -2896)"
    - "default,2736,-3440,,Monumento oceánico (X -3440 · Z -2736)"
    - "default,3056,800,,Monumento oceánico (X 800 · Z -3056)"
    - "default,2880,1328,,Monumento oceánico (X 1328 · Z -2880)"
    - "default,2912,1632,,Monumento oceánico (X 1632 · Z -2912)"
    - "default,2464,-3920,,Monumento oceánico (X -3920 · Z -2464)"
    - "default,2384,-3344,,Monumento oceánico (X -3344 · Z -2384)"
    - "default,2288,-2864,,Monumento oceánico (X -2864 · Z -2288)"
    - "default,1968,-3888,,Monumento oceánico (X -3888 · Z -1968)"
    - "default,1792,-3312,,Monumento oceánico (X -3312 · Z -1792)"
    - "default,1248,-3408,,Monumento oceánico (X -3408 · Z -1248)"
    - "default,1408,-976,,Monumento oceánico (X -976 · Z -1408)"
    - "default,992,1152,,Monumento oceánico (X 1152 · Z -992)"
    - "default,336,-1136,,Monumento oceánico (X -1136 · Z -336)"
    - "default,352,-816,,Monumento oceánico (X -816 · Z -352)"
    - "default,-64,-1968,,Monumento oceánico (X -1968 · Z 64)"
    - "default,-768,48,,Monumento oceánico (X 48 · Z 768)"
    - "default,-784,1168,,Monumento oceánico (X 1168 · Z 784)"
    - "default,-1200,656,,Monumento oceánico (X 656 · Z 1200)"
    - "default,-1776,608,,Monumento oceánico (X 608 · Z 1776)"
    - "default,-2256,-320,,Monumento oceánico (X -320 · Z 2256)"
    - "default,-2080,144,,Monumento oceánico (X 144 · Z 2080)"
    - "default,-2816,720,,Monumento oceánico (X 720 · Z 2816)"
    - "default,-2768,1152,,Monumento oceánico (X 1152 · Z 2768)"
    - "default,-3248,752,,Monumento oceánico (X 752 · Z 3248)"
    - "default,-3776,736,,Monumento oceánico (X 736 · Z 3776)"
    - "default,-3776,1056,,Monumento oceánico (X 1056 · Z 3776)"
    - "default,656,-832,,Mansión del bosque (X -832 · Z -656)"
    - "default,3840,2496,,Ciudad antigua (X 2496 · Z -3840)"
    - "default,3456,2048,,Ciudad antigua (X 2048 · Z -3456)"
    - "default,2960,-2464,,Ciudad antigua (X -2464 · Z -2960)"
    - "default,2640,-2448,,Ciudad antigua (X -2448 · Z -2640)"
    - "default,-432,3136,,Ciudad antigua (X 3136 · Z 432)"
    - "default,-596,2052,,Fortaleza del End (X 2052 · Z 596)"
    - "default,-1396,-1548,,Fortaleza del End (X -1548 · Z 1396)"
    - "default,1772,-492,,Fortaleza del End (X -492 · Z -1772)"
    - "default,3820,2388,,Fortaleza del End (X 2388 · Z -3820)"
    - "default,-8,8,,Punto de aparición (X 8 · Z 8)"
```

## 📍 Estructuras en el mapa
| Estructura | Cantidad |
|---|---|
| Aldea | 69 |
| Cabaña de bruja | 2 |
| Ciudad antigua | 5 |
| Cámaras de desafío | 200 |
| Fortaleza del End | 4 |
| Iglú | 32 |
| Mansión del bosque | 1 |
| Monumento oceánico | 30 |
| Portal en ruinas | 155 |
| Puesto de saqueadores | 13 |
| Punto de aparición | 1 |
| Ruinas de sendero | 38 |
| Templo de la jungla | 2 |
| Templo del desierto | 4 |

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
