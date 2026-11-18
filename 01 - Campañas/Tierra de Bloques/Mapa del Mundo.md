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
Qué se puede encontrar en cada lugar: [[Botín por Lugar]].

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
    - "camaras,3552,-3600,,Cámaras de desafío (X -3600 · Z -3552)"
    - "camaras,3616,-3152,,Cámaras de desafío (X -3152 · Z -3616)"
    - "camaras,3584,-2560,,Cámaras de desafío (X -2560 · Z -3584)"
    - "camaras,3536,-2016,,Cámaras de desafío (X -2016 · Z -3536)"
    - "camaras,3472,-1328,,Cámaras de desafío (X -1328 · Z -3472)"
    - "camaras,3536,-944,,Cámaras de desafío (X -944 · Z -3536)"
    - "camaras,3808,-224,,Cámaras de desafío (X -224 · Z -3808)"
    - "camaras,3664,272,,Cámaras de desafío (X 272 · Z -3664)"
    - "camaras,3680,864,,Cámaras de desafío (X 864 · Z -3680)"
    - "camaras,3792,1280,,Cámaras de desafío (X 1280 · Z -3792)"
    - "camaras,3712,1968,,Cámaras de desafío (X 1968 · Z -3712)"
    - "camaras,3712,3504,,Cámaras de desafío (X 3504 · Z -3712)"
    - "camaras,3600,3872,,Cámaras de desafío (X 3872 · Z -3600)"
    - "camaras,3008,-3568,,Cámaras de desafío (X -3568 · Z -3008)"
    - "camaras,3072,-3008,,Cámaras de desafío (X -3008 · Z -3072)"
    - "camaras,2992,-2704,,Cámaras de desafío (X -2704 · Z -2992)"
    - "camaras,3216,-2064,,Cámaras de desafío (X -2064 · Z -3216)"
    - "camaras,3264,-1536,,Cámaras de desafío (X -1536 · Z -3264)"
    - "camaras,3264,-784,,Cámaras de desafío (X -784 · Z -3264)"
    - "camaras,3184,-272,,Cámaras de desafío (X -272 · Z -3184)"
    - "camaras,3232,240,,Cámaras de desafío (X 240 · Z -3232)"
    - "camaras,2928,848,,Cámaras de desafío (X 848 · Z -2928)"
    - "camaras,2992,1264,,Cámaras de desafío (X 1264 · Z -2992)"
    - "camaras,3184,1760,,Cámaras de desafío (X 1760 · Z -3184)"
    - "camaras,3088,2384,,Cámaras de desafío (X 2384 · Z -3088)"
    - "camaras,3200,2784,,Cámaras de desafío (X 2784 · Z -3200)"
    - "camaras,3088,3328,,Cámaras de desafío (X 3328 · Z -3088)"
    - "camaras,3184,3872,,Cámaras de desafío (X 3872 · Z -3184)"
    - "camaras,2592,-3776,,Cámaras de desafío (X -3776 · Z -2592)"
    - "camaras,2624,-3072,,Cámaras de desafío (X -3072 · Z -2624)"
    - "camaras,2416,-2672,,Cámaras de desafío (X -2672 · Z -2416)"
    - "camaras,2608,-1968,,Cámaras de desafío (X -1968 · Z -2608)"
    - "camaras,2576,-1376,,Cámaras de desafío (X -1376 · Z -2576)"
    - "camaras,2432,-800,,Cámaras de desafío (X -800 · Z -2432)"
    - "camaras,2672,-528,,Cámaras de desafío (X -528 · Z -2672)"
    - "camaras,2464,272,,Cámaras de desafío (X 272 · Z -2464)"
    - "camaras,2448,608,,Cámaras de desafío (X 608 · Z -2448)"
    - "camaras,2640,1232,,Cámaras de desafío (X 1232 · Z -2640)"
    - "camaras,2720,1728,,Cámaras de desafío (X 1728 · Z -2720)"
    - "camaras,2720,2432,,Cámaras de desafío (X 2432 · Z -2720)"
    - "camaras,2640,2992,,Cámaras de desafío (X 2992 · Z -2640)"
    - "camaras,2640,3392,,Cámaras de desafío (X 3392 · Z -2640)"
    - "camaras,1856,-3632,,Cámaras de desafío (X -3632 · Z -1856)"
    - "camaras,2176,-2976,,Cámaras de desafío (X -2976 · Z -2176)"
    - "camaras,1840,-2592,,Cámaras de desafío (X -2592 · Z -1840)"
    - "camaras,1920,-1872,,Cámaras de desafío (X -1872 · Z -1920)"
    - "camaras,2016,-1584,,Cámaras de desafío (X -1584 · Z -2016)"
    - "camaras,2000,-1088,,Cámaras de desafío (X -1088 · Z -2000)"
    - "camaras,2144,-448,,Cámaras de desafío (X -448 · Z -2144)"
    - "camaras,2128,96,,Cámaras de desafío (X 96 · Z -2128)"
    - "camaras,2032,768,,Cámaras de desafío (X 768 · Z -2032)"
    - "camaras,2160,1168,,Cámaras de desafío (X 1168 · Z -2160)"
    - "camaras,1984,2304,,Cámaras de desafío (X 2304 · Z -1984)"
    - "camaras,2016,2976,,Cámaras de desafío (X 2976 · Z -2016)"
    - "camaras,1920,3264,,Cámaras de desafío (X 3264 · Z -1920)"
    - "camaras,1840,3904,,Cámaras de desafío (X 3904 · Z -1840)"
    - "camaras,1328,-3760,,Cámaras de desafío (X -3760 · Z -1328)"
    - "camaras,1392,-2928,,Cámaras de desafío (X -2928 · Z -1392)"
    - "camaras,1600,-2528,,Cámaras de desafío (X -2528 · Z -1600)"
    - "camaras,1344,-2144,,Cámaras de desafío (X -2144 · Z -1344)"
    - "camaras,1392,-1344,,Cámaras de desafío (X -1344 · Z -1392)"
    - "camaras,1472,-784,,Cámaras de desafío (X -784 · Z -1472)"
    - "camaras,1456,-320,,Cámaras de desafío (X -320 · Z -1456)"
    - "camaras,1600,256,,Cámaras de desafío (X 256 · Z -1600)"
    - "camaras,1312,816,,Cámaras de desafío (X 816 · Z -1312)"
    - "camaras,1408,1120,,Cámaras de desafío (X 1120 · Z -1408)"
    - "camaras,1456,2416,,Cámaras de desafío (X 2416 · Z -1456)"
    - "camaras,1456,2736,,Cámaras de desafío (X 2736 · Z -1456)"
    - "camaras,1520,3440,,Cámaras de desafío (X 3440 · Z -1520)"
    - "camaras,1024,-3664,,Cámaras de desafío (X -3664 · Z -1024)"
    - "camaras,896,-3136,,Cámaras de desafío (X -3136 · Z -896)"
    - "camaras,768,-2448,,Cámaras de desafío (X -2448 · Z -768)"
    - "camaras,896,-1600,,Cámaras de desafío (X -1600 · Z -896)"
    - "camaras,768,-944,,Cámaras de desafío (X -944 · Z -768)"
    - "camaras,1008,-352,,Cámaras de desafío (X -352 · Z -1008)"
    - "camaras,1008,48,,Cámaras de desafío (X 48 · Z -1008)"
    - "camaras,1008,736,,Cámaras de desafío (X 736 · Z -1008)"
    - "camaras,784,1296,,Cámaras de desafío (X 1296 · Z -784)"
    - "camaras,928,1920,,Cámaras de desafío (X 1920 · Z -928)"
    - "camaras,1008,2400,,Cámaras de desafío (X 2400 · Z -1008)"
    - "camaras,1072,3008,,Cámaras de desafío (X 3008 · Z -1072)"
    - "camaras,816,3312,,Cámaras de desafío (X 3312 · Z -816)"
    - "camaras,768,3984,,Cámaras de desafío (X 3984 · Z -768)"
    - "camaras,224,-3712,,Cámaras de desafío (X -3712 · Z -224)"
    - "camaras,240,-3248,,Cámaras de desafío (X -3248 · Z -240)"
    - "camaras,384,-2544,,Cámaras de desafío (X -2544 · Z -384)"
    - "camaras,448,-1872,,Cámaras de desafío (X -1872 · Z -448)"
    - "camaras,384,-1344,,Cámaras de desafío (X -1344 · Z -384)"
    - "camaras,448,-752,,Cámaras de desafío (X -752 · Z -448)"
    - "camaras,528,-288,,Cámaras de desafío (X -288 · Z -528)"
    - "camaras,464,176,,Cámaras de desafío (X 176 · Z -464)"
    - "camaras,336,704,,Cámaras de desafío (X 704 · Z -336)"
    - "camaras,320,1328,,Cámaras de desafío (X 1328 · Z -320)"
    - "camaras,448,1632,,Cámaras de desafío (X 1632 · Z -448)"
    - "camaras,272,2176,,Cámaras de desafío (X 2176 · Z -272)"
    - "camaras,464,2976,,Cámaras de desafío (X 2976 · Z -464)"
    - "camaras,384,3392,,Cámaras de desafío (X 3392 · Z -384)"
    - "camaras,-80,-3744,,Cámaras de desafío (X -3744 · Z 80)"
    - "camaras,-240,-3056,,Cámaras de desafío (X -3056 · Z 240)"
    - "camaras,-96,-2576,,Cámaras de desafío (X -2576 · Z 96)"
    - "camaras,-240,-1984,,Cámaras de desafío (X -1984 · Z 240)"
    - "camaras,-32,-1536,,Cámaras de desafío (X -1536 · Z 32)"
    - "camaras,-288,-1040,,Cámaras de desafío (X -1040 · Z 288)"
    - "camaras,-272,-480,,Cámaras de desafío (X -480 · Z 272)"
    - "camaras,-336,16,,Cámaras de desafío (X 16 · Z 336)"
    - "camaras,0,864,,Cámaras de desafío (X 864 · Z 0)"
    - "camaras,-32,1200,,Cámaras de desafío (X 1200 · Z 32)"
    - "camaras,-96,1872,,Cámaras de desafío (X 1872 · Z 96)"
    - "camaras,-288,2288,,Cámaras de desafío (X 2288 · Z 288)"
    - "camaras,-160,2832,,Cámaras de desafío (X 2832 · Z 160)"
    - "camaras,-160,3424,,Cámaras de desafío (X 3424 · Z 160)"
    - "camaras,-560,-3808,,Cámaras de desafío (X -3808 · Z 560)"
    - "camaras,-640,-3232,,Cámaras de desafío (X -3232 · Z 640)"
    - "camaras,-880,-2416,,Cámaras de desafío (X -2416 · Z 880)"
    - "camaras,-736,-2112,,Cámaras de desafío (X -2112 · Z 736)"
    - "camaras,-752,-1520,,Cámaras de desafío (X -1520 · Z 752)"
    - "camaras,-800,-832,,Cámaras de desafío (X -832 · Z 800)"
    - "camaras,-544,-400,,Cámaras de desafío (X -400 · Z 544)"
    - "camaras,-656,288,,Cámaras de desafío (X 288 · Z 656)"
    - "camaras,-704,832,,Cámaras de desafío (X 832 · Z 704)"
    - "camaras,-624,1328,,Cámaras de desafío (X 1328 · Z 624)"
    - "camaras,-816,1840,,Cámaras de desafío (X 1840 · Z 816)"
    - "camaras,-672,2496,,Cámaras de desafío (X 2496 · Z 672)"
    - "camaras,-864,2784,,Cámaras de desafío (X 2784 · Z 864)"
    - "camaras,-560,3392,,Cámaras de desafío (X 3392 · Z 560)"
    - "camaras,-1248,-3792,,Cámaras de desafío (X -3792 · Z 1248)"
    - "camaras,-1328,-3040,,Cámaras de desafío (X -3040 · Z 1328)"
    - "camaras,-1152,-2576,,Cámaras de desafío (X -2576 · Z 1152)"
    - "camaras,-1104,-1872,,Cámaras de desafío (X -1872 · Z 1104)"
    - "camaras,-1104,-1600,,Cámaras de desafío (X -1600 · Z 1104)"
    - "camaras,-1232,-848,,Cámaras de desafío (X -848 · Z 1232)"
    - "camaras,-1312,-288,,Cámaras de desafío (X -288 · Z 1312)"
    - "camaras,-1408,80,,Cámaras de desafío (X 80 · Z 1408)"
    - "camaras,-1312,848,,Cámaras de desafío (X 848 · Z 1312)"
    - "camaras,-1104,1232,,Cámaras de desafío (X 1232 · Z 1104)"
    - "camaras,-1328,1696,,Cámaras de desafío (X 1696 · Z 1328)"
    - "camaras,-1136,2384,,Cámaras de desafío (X 2384 · Z 1136)"
    - "camaras,-1392,2960,,Cámaras de desafío (X 2960 · Z 1392)"
    - "camaras,-1200,3392,,Cámaras de desafío (X 3392 · Z 1200)"
    - "camaras,-1264,3936,,Cámaras de desafío (X 3936 · Z 1264)"
    - "camaras,-1696,-3472,,Cámaras de desafío (X -3472 · Z 1696)"
    - "camaras,-1744,-3024,,Cámaras de desafío (X -3024 · Z 1744)"
    - "camaras,-1696,-2656,,Cámaras de desafío (X -2656 · Z 1696)"
    - "camaras,-1952,-2016,,Cámaras de desafío (X -2016 · Z 1952)"
    - "camaras,-1744,-1312,,Cámaras de desafío (X -1312 · Z 1744)"
    - "camaras,-1696,-1024,,Cámaras de desafío (X -1024 · Z 1696)"
    - "camaras,-1904,-224,,Cámaras de desafío (X -224 · Z 1904)"
    - "camaras,-1664,176,,Cámaras de desafío (X 176 · Z 1664)"
    - "camaras,-1968,592,,Cámaras de desafío (X 592 · Z 1968)"
    - "camaras,-1728,1168,,Cámaras de desafío (X 1168 · Z 1728)"
    - "camaras,-1904,1856,,Cámaras de desafío (X 1856 · Z 1904)"
    - "camaras,-1872,2272,,Cámaras de desafío (X 2272 · Z 1872)"
    - "camaras,-1920,3280,,Cámaras de desafío (X 3280 · Z 1920)"
    - "camaras,-2384,-3792,,Cámaras de desafío (X -3792 · Z 2384)"
    - "camaras,-2464,-3088,,Cámaras de desafío (X -3088 · Z 2464)"
    - "camaras,-2224,-2624,,Cámaras de desafío (X -2624 · Z 2224)"
    - "camaras,-2256,-1536,,Cámaras de desafío (X -1536 · Z 2256)"
    - "camaras,-2448,-1056,,Cámaras de desafío (X -1056 · Z 2448)"
    - "camaras,-2304,-384,,Cámaras de desafío (X -384 · Z 2304)"
    - "camaras,-2352,32,,Cámaras de desafío (X 32 · Z 2352)"
    - "camaras,-2192,768,,Cámaras de desafío (X 768 · Z 2192)"
    - "camaras,-2416,1200,,Cámaras de desafío (X 1200 · Z 2416)"
    - "camaras,-2448,1664,,Cámaras de desafío (X 1664 · Z 2448)"
    - "camaras,-2320,2208,,Cámaras de desafío (X 2208 · Z 2320)"
    - "camaras,-2480,3312,,Cámaras de desafío (X 3312 · Z 2480)"
    - "camaras,-2992,-3632,,Cámaras de desafío (X -3632 · Z 2992)"
    - "camaras,-2912,-3264,,Cámaras de desafío (X -3264 · Z 2912)"
    - "camaras,-3040,-2640,,Cámaras de desafío (X -2640 · Z 3040)"
    - "camaras,-3040,-2016,,Cámaras de desafío (X -2016 · Z 3040)"
    - "camaras,-2832,-1456,,Cámaras de desafío (X -1456 · Z 2832)"
    - "camaras,-2832,-944,,Cámaras de desafío (X -944 · Z 2832)"
    - "camaras,-2944,-512,,Cámaras de desafío (X -512 · Z 2944)"
    - "camaras,-2992,240,,Cámaras de desafío (X 240 · Z 2992)"
    - "camaras,-2832,864,,Cámaras de desafío (X 864 · Z 2832)"
    - "camaras,-2960,1280,,Cámaras de desafío (X 1280 · Z 2960)"
    - "camaras,-2768,1744,,Cámaras de desafío (X 1744 · Z 2768)"
    - "camaras,-2848,2448,,Cámaras de desafío (X 2448 · Z 2848)"
    - "camaras,-2784,2816,,Cámaras de desafío (X 2816 · Z 2784)"
    - "camaras,-2848,3552,,Cámaras de desafío (X 3552 · Z 2848)"
    - "camaras,-2848,3888,,Cámaras de desafío (X 3888 · Z 2848)"
    - "camaras,-3488,-3680,,Cámaras de desafío (X -3680 · Z 3488)"
    - "camaras,-3472,-3088,,Cámaras de desafío (X -3088 · Z 3472)"
    - "camaras,-3472,-2432,,Cámaras de desafío (X -2432 · Z 3472)"
    - "camaras,-3408,-1856,,Cámaras de desafío (X -1856 · Z 3408)"
    - "camaras,-3376,-1424,,Cámaras de desafío (X -1424 · Z 3376)"
    - "camaras,-3360,-752,,Cámaras de desafío (X -752 · Z 3360)"
    - "camaras,-3584,-544,,Cámaras de desafío (X -544 · Z 3584)"
    - "camaras,-3264,288,,Cámaras de desafío (X 288 · Z 3264)"
    - "camaras,-3440,608,,Cámaras de desafío (X 608 · Z 3440)"
    - "camaras,-3488,1392,,Cámaras de desafío (X 1392 · Z 3488)"
    - "camaras,-3296,1792,,Cámaras de desafío (X 1792 · Z 3296)"
    - "camaras,-3584,2192,,Cámaras de desafío (X 2192 · Z 3584)"
    - "camaras,-3264,3040,,Cámaras de desafío (X 3040 · Z 3264)"
    - "camaras,-3536,3376,,Cámaras de desafío (X 3376 · Z 3536)"
    - "camaras,-3376,3856,,Cámaras de desafío (X 3856 · Z 3376)"
    - "camaras,-3920,-3776,,Cámaras de desafío (X -3776 · Z 3920)"
    - "camaras,-3888,144,,Cámaras de desafío (X 144 · Z 3888)"
    - "camaras,-3888,736,,Cámaras de desafío (X 736 · Z 3888)"
    - "camaras,-3824,1776,,Cámaras de desafío (X 1776 · Z 3824)"
    - "camaras,-3984,2816,,Cámaras de desafío (X 2816 · Z 3984)"
    - "fortaleza_end,-596,2052,,Fortaleza del End (X 2052 · Z 596)"
    - "fortaleza_end,-1396,-1548,,Fortaleza del End (X -1548 · Z 1396)"
    - "fortaleza_end,1772,-492,,Fortaleza del End (X -492 · Z -1772)"
    - "fortaleza_end,3820,2388,,Fortaleza del End (X 2388 · Z -3820)"
    - "spawn,-8,8,,Punto de aparición (X 8 · Z 8)"
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
🏠 Aldea · ⚓ Aldea con puerto · 🚩 Puesto de saqueadores · 🏚️ Mansión · 🌊 Monumento oceánico · 🗿 Templo · 🧙 Cabaña de bruja · 💀 Ciudad antigua · ♜ Fortaleza del End · 🔑 Cámaras de desafío · ⭐ Punto de aparición

## 🌍 Biomas (colores del mapa)
Ordenados de más a menos extensión. El mapa se toma a nivel del mar: donde hay colinas o montañas sale el bioma de la cueva que hay debajo (manchas marrones y verde oscuro).

| Color | Bioma | Del mapa | En la partida |
|---|---|---|---|
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(5,102,33);border:1px solid #000"></span> | Bosque | 9.5 % | Madera, lobos |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(141,179,96);border:1px solid #000"></span> | Llanura | 8.9 % | Aldeas, caballos; viaje fácil |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(32,32,112);border:1px solid #000"></span> | Océano frío | 6.7 % | Salmón, ruinas oceánicas |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(49,85,74);border:1px solid #000"></span> | Taiga nevada | 6.2 % | Zorros, iglús; frío |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(255,255,255);border:1px solid #000"></span> | Llanura nevada | 6.1 % | Aldeas de nieve, iglús; frío |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(0,0,255);border:1px solid #000"></span> | Río | 5.4 % | Agua, arcilla, caña de azúcar; se cruza nadando o con puente |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(11,106,95);border:1px solid #000"></span> | Taiga | 5.0 % | Aldeas, lobos, zorros, bayas |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(0,0,112);border:1px solid #000"></span> | Océano | 4.9 % | Peces, algas; ahogados de noche |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(0,0,172);border:1px solid #000"></span> | Océano cálido | 3.4 % | Arrecifes de coral, tortugas |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(0,0,48);border:1px solid #000"></span> | Océano profundo | 3.3 % | Monumentos, naufragios; ahogados |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(32,32,56);border:1px solid #000"></span> | Océano frío profundo | 3.3 % | Monumentos, ruinas |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(189,178,95);border:1px solid #000"></span> | Sabana | 3.1 % | Aldeas, caballos, llamas |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(0,0,144);border:1px solid #000"></span> | Océano templado | 2.8 % | Delfines, peces tropicales |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(78,48,18);border:1px solid #000"></span> | Cuevas de espeleotemas | 2.5 % | Colinas o montaña con cuevas debajo: estalactitas, cobre |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(112,112,214);border:1px solid #000"></span> | Océano helado | 2.5 % | Icebergs, osos polares |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(7,249,178);border:1px solid #000"></span> | Pantano | 2.2 % | Cabañas de bruja, slimes; terreno difícil |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(0,0,64);border:1px solid #000"></span> | Océano templado profundo | 2.2 % | Monumentos, naufragios |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(160,160,255);border:1px solid #000"></span> | Río helado | 2.0 % | Hielo transitable |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(250,222,85);border:1px solid #000"></span> | Playa | 2.0 % | Arena, tortugas; buen sitio de puerto |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(64,81,26);border:1px solid #000"></span> | Bosque oscuro | 1.9 % | Mansiones; mobs de día por la sombra |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(250,148,24);border:1px solid #000"></span> | Desierto | 1.8 % | Templos, aldeas, cactus; sin agua ni madera |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(48,116,68);border:1px solid #000"></span> | Bosque de abedules | 1.5 % | Madera clara |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(89,102,81);border:1px solid #000"></span> | Taiga de pinos antigua | 1.2 % | Podzol, setas |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(40,60,0);border:1px solid #000"></span> | Cuevas frondosas | 1.2 % | Colinas con cuevas frondosas debajo: bayas brillantes, axolotes |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(88,156,108);border:1px solid #000"></span> | Bosque de abedules antiguo | 1.1 % | Abedules altos |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(96,147,15);border:1px solid #000"></span> | Jungla dispersa | 0.9 % | Jungla más transitable |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(80,123,10);border:1px solid #000"></span> | Jungla | 0.8 % | Templos, ocelotes, cacao; terreno difícil |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(96,164,69);border:1px solid #000"></span> | Pradera alpina | 0.8 % | Flores, abejas, aldeas en altura |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(162,162,132);border:1px solid #000"></span> | Costa pedregosa | 0.7 % | Piedra a la vista |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(180,220,220);border:1px solid #000"></span> | Picos de hielo | 0.7 % | Hielo compacto; terreno difícil |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(217,69,21);border:1px solid #000"></span> | Tierras baldías | 0.7 % | Terracota, oro en superficie, minas |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(64,64,144);border:1px solid #000"></span> | Océano helado profundo | 0.5 % | Monumentos; agua gélida |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(255,109,61);border:1px solid #000"></span> | Tierras baldías erosionadas | 0.5 % | Agujas de terracota |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(129,142,121);border:1px solid #000"></span> | Taiga de abetos antigua | 0.5 % | Abetos gigantes |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(250,240,192);border:1px solid #000"></span> | Playa nevada | 0.4 % | Arena y nieve |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(96,96,96);border:1px solid #000"></span> | Colinas ventosas | 0.3 % | Esmeraldas en mineral, cabras; escalada |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(167,157,100);border:1px solid #000"></span> | Meseta de sabana | 0.3 % | Sabana en alto |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(132,149,0);border:1px solid #000"></span> | Jungla de bambú | 0.3 % | Pandas, bambú |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(196,196,196);border:1px solid #000"></span> | Laderas nevadas | 0.3 % | Cabras, nieve polvo; escalada |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(136,136,136);border:1px solid #000"></span> | Colinas ventosas de grava | 0.2 % | Grava, desprendimientos |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(91,115,82);border:1px solid #000"></span> | Bosque ventoso | 0.2 % | Colinas con árboles |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(45,142,73);border:1px solid #000"></span> | Bosque de flores | 0.2 % | Tintes, abejas, miel |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(71,114,108);border:1px solid #000"></span> | Arboleda nevada | 0.2 % | Lobos; nieve polvo (cuidado) |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(229,218,135);border:1px solid #000"></span> | Sabana ventosa | 0.2 % | Terreno muy accidentado |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(176,151,101);border:1px solid #000"></span> | Tierras baldías boscosas | 0.2 % | Meseta con robles |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(181,219,136);border:1px solid #000"></span> | Llanura de girasoles | 0.1 % | Como la llanura; los girasoles marcan el este |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(255,145,200);border:1px solid #000"></span> | Cerezal | 0.1 % | Madera de cerezo, cerdos |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(255,0,255);border:1px solid #000"></span> | Campos de champiñones | 0.1 % | Champiñacas; sin mobs hostiles de noche |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(176,179,206);border:1px solid #000"></span> | Picos helados | 0.1 % | Hielo; montaña muy alta |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(123,143,116);border:1px solid #000"></span> | Picos rocosos | 0.0 % | Calcita, piedra; montaña alta |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(220,220,200);border:1px solid #000"></span> | Picos escarpados | 0.0 % | Montaña muy alta e infranqueable a pie |
| <span style="display:inline-block;width:1.6em;height:1em;background:rgb(105,109,149);border:1px solid #000"></span> | Jardín pálido | 0.0 % | Creaking de noche |

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
- Líneas oscuras: cuadrícula cada 500 bloques.

> [!warning] Aproximado
> Las estructuras se calculan por bioma. En el juego alguna puede no generarse por el terreno (sobre todo aldeas en laderas).
