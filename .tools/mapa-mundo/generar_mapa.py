#!/usr/bin/env python3
"""Genera el mapa del mundo de una semilla de Minecraft Java para una campaña del vault.

Uso (desde la raíz del vault; en Windows, `py` en vez de `python3`):
  python3 .tools/mapa-mundo/generar_mapa.py <semilla> <version> [--lado 8000] [--bpp 2] [--cuadricula 500] [--nether]
      [--campaña "Tierra de Bloques"]

Necesita Python 3, git y gcc (en Windows: w64devkit o MSYS2 MinGW). Ver "00 - Instalar en Windows.md".

Crea:
  01 - Campañas/<campaña>/10 - images/Mapa del Mundo.png   (o "Mapa del Nether.png")
  01 - Campañas/<campaña>/Mapa del Mundo.md                (nota con el mapa Leaflet y marcadores)
"""
import argparse, csv, json, os, struct, subprocess, sys, zlib
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VAULT = AQUI.parent.parent
CUBIOMES = AQUI.parent / "cubiomes"
BIN = AQUI / ("mapa.exe" if os.name == "nt" else "mapa")
CUBIOMES_COMMIT = "e61f905"  # versión probada (soporta hasta Java 1.21.4)
FUENTES = ["noise", "biomes", "layers", "biomenoise", "generator", "finders", "util", "quadbase"]

# Estructuras con marcador clicable en Leaflet: tipo -> (tipo de marcador, icono Font Awesome, color).
# Ruinas, iglús y portales en ruinas salen cientos: solo van dibujados en la imagen.
TIPOS = {
    "Aldea": ("aldea", "home", "#ffd700"),
    "Puesto de saqueadores": ("saqueadores", "flag", "#9a9a9a"),
    "Mansión del bosque": ("mansion", "dungeon", "#a0522d"),
    "Monumento oceánico": ("monumento", "water", "#00d0d0"),
    "Templo del desierto": ("templo", "monument", "#f0c060"),
    "Templo de la jungla": ("templo", "monument", "#f0c060"),
    "Cabaña de bruja": ("bruja", "hat-wizard", "#50c040"),
    "Ciudad antigua": ("ciudad", "skull", "#5080b0"),
    "Fortaleza del End": ("fortaleza_end", "chess-rook", "#e600e6"),
    "Cámaras de desafío": ("camaras", "key", "#e08030"),
    "Punto de aparición": ("spawn", "star", "#ffffff"),
    "Fortaleza del Nether": ("fortaleza_nether", "chess-rook", "#c03030"),
    "Bastión": ("bastion", "skull", "#303030"),
}
# Nombre en español y qué ofrece cada bioma en la partida (para la leyenda de colores)
BIOMAS = {
    "ocean": ("Océano", "Peces, algas; ahogados de noche"), "deep_ocean": ("Océano profundo", "Monumentos, naufragios; ahogados"),
    "frozen_ocean": ("Océano helado", "Icebergs, osos polares"), "deep_frozen_ocean": ("Océano helado profundo", "Monumentos; agua gélida"),
    "cold_ocean": ("Océano frío", "Salmón, ruinas oceánicas"), "deep_cold_ocean": ("Océano frío profundo", "Monumentos, ruinas"),
    "lukewarm_ocean": ("Océano templado", "Delfines, peces tropicales"), "deep_lukewarm_ocean": ("Océano templado profundo", "Monumentos, naufragios"),
    "warm_ocean": ("Océano cálido", "Arrecifes de coral, tortugas"),
    "river": ("Río", "Agua, arcilla, caña de azúcar; se cruza nadando o con puente"), "frozen_river": ("Río helado", "Hielo transitable"),
    "beach": ("Playa", "Arena, tortugas; buen sitio de puerto"), "stony_shore": ("Costa pedregosa", "Piedra a la vista"),
    "snowy_beach": ("Playa nevada", "Arena y nieve"),
    "plains": ("Llanura", "Aldeas, caballos; viaje fácil"), "sunflower_plains": ("Llanura de girasoles", "Como la llanura; los girasoles marcan el este"),
    "snowy_plains": ("Llanura nevada", "Aldeas de nieve, iglús; frío"), "ice_spikes": ("Picos de hielo", "Hielo compacto; terreno difícil"),
    "desert": ("Desierto", "Templos, aldeas, cactus; sin agua ni madera"),
    "swamp": ("Pantano", "Cabañas de bruja, slimes; terreno difícil"), "mangrove_swamp": ("Manglar", "Barro, ranas; terreno difícil"),
    "forest": ("Bosque", "Madera, lobos"), "flower_forest": ("Bosque de flores", "Tintes, abejas, miel"),
    "birch_forest": ("Bosque de abedules", "Madera clara"), "old_growth_birch_forest": ("Bosque de abedules antiguo", "Abedules altos"),
    "dark_forest": ("Bosque oscuro", "Mansiones; mobs de día por la sombra"),
    "old_growth_pine_taiga": ("Taiga de pinos antigua", "Podzol, setas"), "old_growth_spruce_taiga": ("Taiga de abetos antigua", "Abetos gigantes"),
    "taiga": ("Taiga", "Aldeas, lobos, zorros, bayas"), "snowy_taiga": ("Taiga nevada", "Zorros, iglús; frío"),
    "savanna": ("Sabana", "Aldeas, caballos, llamas"), "savanna_plateau": ("Meseta de sabana", "Sabana en alto"),
    "windswept_hills": ("Colinas ventosas", "Esmeraldas en mineral, cabras; escalada"),
    "windswept_gravelly_hills": ("Colinas ventosas de grava", "Grava, desprendimientos"),
    "windswept_forest": ("Bosque ventoso", "Colinas con árboles"), "windswept_savanna": ("Sabana ventosa", "Terreno muy accidentado"),
    "jungle": ("Jungla", "Templos, ocelotes, cacao; terreno difícil"), "sparse_jungle": ("Jungla dispersa", "Jungla más transitable"),
    "bamboo_jungle": ("Jungla de bambú", "Pandas, bambú"),
    "badlands": ("Tierras baldías", "Terracota, oro en superficie, minas"), "eroded_badlands": ("Tierras baldías erosionadas", "Agujas de terracota"),
    "wooded_badlands": ("Tierras baldías boscosas", "Meseta con robles"),
    "meadow": ("Pradera alpina", "Flores, abejas, aldeas en altura"), "cherry_grove": ("Cerezal", "Madera de cerezo, cerdos"),
    "grove": ("Arboleda nevada", "Lobos; nieve polvo (cuidado)"), "snowy_slopes": ("Laderas nevadas", "Cabras, nieve polvo; escalada"),
    "frozen_peaks": ("Picos helados", "Hielo; montaña muy alta"), "jagged_peaks": ("Picos escarpados", "Montaña muy alta e infranqueable a pie"),
    "stony_peaks": ("Picos rocosos", "Calcita, piedra; montaña alta"),
    "mushroom_fields": ("Campos de champiñones", "Champiñacas; sin mobs hostiles de noche"),
    "deep_dark": ("Oscuridad profunda", "Ciudades antiguas, Warden (subterráneo)"),
    "dripstone_caves": ("Cuevas de espeleotemas", "Colinas o montaña con cuevas debajo: estalactitas, cobre"),
    "lush_caves": ("Cuevas frondosas", "Colinas con cuevas frondosas debajo: bayas brillantes, axolotes"),
    "pale_garden": ("Jardín pálido", "Creaking de noche"),
    "nether_wastes": ("Páramo del Nether", "Cuarzo, ghasts, piglins zombificados"), "soul_sand_valley": ("Valle de arena de almas", "Esqueletos, ghasts; terreno lento"),
    "crimson_forest": ("Bosque carmesí", "Piglins, hoglins"), "warped_forest": ("Bosque distorsionado", "Endermen; zona tranquila"),
    "basalt_deltas": ("Deltas de basalto", "Cubos de magma; terreno difícil"),
}

PUERTO = ("puerto", "anchor", "#3fa9f5")  # aldea con ruta marítima

# Caminos: celdas de 64 bloques. Coste por celda según la máscara (0 tierra, 1 río, 2 océano); None = intransitable.
CELDA = 64
COSTE_TIERRA = {"0": 1, "1": 4, "2": None}   # los caminos cruzan ríos con puente pero no el mar
COSTE_MAR = {"0": 6, "1": 1, "2": 1}         # los barcos van por agua y pisan tierra solo para llegar al puerto
DESVIO_MAX = 2.0  # si el camino por tierra es más del doble que la línea recta, se va en barco

LEYENDA = [("🟨", "Aldea"), ("⬛ gris", "Puesto de saqueadores"), ("🟫", "Mansión del bosque"), ("🟦 cian", "Monumento oceánico"),
           ("🟧 arena", "Templo del desierto"), ("🟩", "Templo de la jungla / cabaña de bruja (verde oscuro)"),
           ("🟪 grande", "Fortaleza del End"), ("🟪 pequeño", "Portal en ruinas"), ("⬜", "Punto de aparición / iglú"),
           ("🟧", "Cámaras de desafío"), ("⬛ azul noche", "Ciudad antigua"), ("🟥 líneas", "Ejes 0,0")]


def run(cmd, **kw):
    r = subprocess.run(cmd, **kw)
    if r.returncode:
        sys.exit(f"Falló: {' '.join(map(str, cmd))}")


def compilar():
    if not CUBIOMES.exists():
        run(["git", "clone", "https://github.com/Cubitect/cubiomes.git", str(CUBIOMES)])
        run(["git", "-C", str(CUBIOMES), "checkout", "-q", CUBIOMES_COMMIT])
    src = AQUI / "mapa.c"
    if not BIN.exists() or BIN.stat().st_mtime < src.stat().st_mtime:
        # Se compilan las fuentes de cubiomes directamente: no hace falta `make` (no viene en Windows)
        run(["gcc", "-O2", str(src), *[str(CUBIOMES / f"{f}.c") for f in FUENTES], f"-I{CUBIOMES}", "-lm", "-o", str(BIN)])


def ppm_a_png(ppm, png):
    """PPM (P6) -> PNG solo con la librería estándar, para no depender de ImageMagick."""
    datos = Path(ppm).read_bytes()
    partes = datos.split(maxsplit=4)  # P6, ancho, alto, 255, píxeles
    assert partes[0] == b"P6" and partes[3] == b"255", "PPM inesperado"
    w, h, px = int(partes[1]), int(partes[2]), partes[4]
    fila = 3 * w
    crudo = b"".join(b"\0" + px[y * fila:(y + 1) * fila] for y in range(h))
    trozo = lambda tipo, d: struct.pack(">I", len(d)) + tipo + d + struct.pack(">I", zlib.crc32(tipo + d) & 0xFFFFFFFF)
    Path(png).write_bytes(b"\x89PNG\r\n\x1a\n" + trozo(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                          + trozo(b"IDAT", zlib.compress(crudo, 6)) + trozo(b"IEND", b""))


def camino(agua, coste, a, b):
    """Dijkstra 8-vecinos sobre la máscara. Devuelve (celdas, longitud en celdas) o None."""
    import heapq, math
    n = len(agua)
    dist, prev, cola = {a: 0.0}, {}, [(0.0, a)]
    while cola:
        d, c = heapq.heappop(cola)
        if c == b:
            celdas = [c]
            while c in prev:
                c = prev[c]; celdas.append(c)
            celdas.reverse()
            largo = sum(math.dist(celdas[i], celdas[i + 1]) for i in range(len(celdas) - 1))
            return celdas, largo
        if d > dist[c]:
            continue
        for dx in (-1, 0, 1):
            for dz in (-1, 0, 1):
                v = (c[0] + dx, c[1] + dz)
                if v == c or not (0 <= v[0] < n and 0 <= v[1] < n):
                    continue
                w = coste[agua[v[1]][v[0]]]
                if w is None and v != b:
                    continue
                nd = d + math.hypot(dx, dz) * (w or 1)
                if nd < dist.get(v, 1e18):
                    dist[v], prev[v] = nd, c
                    heapq.heappush(cola, (nd, v))
    return None


def rutas(aldeas, agua, x0):
    """Árbol de expansión mínima entre aldeas; cada tramo va por tierra o, si no se puede, por mar."""
    import math
    celda = lambda a: (min(len(agua) - 1, round((a["x"] - x0) / CELDA)), min(len(agua) - 1, round((a["z"] - x0) / CELDA)))
    pares = sorted((math.dist((a["x"], a["z"]), (b["x"], b["z"])), i, j)
                   for i, a in enumerate(aldeas) for j, b in enumerate(aldeas) if i < j)
    grupo = list(range(len(aldeas)))
    def raiz(i):
        while grupo[i] != i:
            grupo[i] = grupo[grupo[i]]; i = grupo[i]
        return i
    out = []
    for recta, i, j in pares:
        if raiz(i) == raiz(j):
            continue
        grupo[raiz(i)] = raiz(j)
        a, b = celda(aldeas[i]), celda(aldeas[j])
        tierra = camino(agua, COSTE_TIERRA, a, b)
        if tierra and tierra[1] * CELDA <= max(recta, CELDA) * DESVIO_MAX:
            tipo, (celdas, largo) = "camino", tierra
        else:
            tipo, (celdas, largo) = "mar", camino(agua, COSTE_MAR, a, b)
        # Solo los puntos donde cambia la dirección
        puntos = [celdas[0]] + [c for k, c in enumerate(celdas[1:-1], 1)
                                if (c[0] - celdas[k - 1][0], c[1] - celdas[k - 1][1]) != (celdas[k + 1][0] - c[0], celdas[k + 1][1] - c[1])] + [celdas[-1]]
        coords = [[x0 + c[0] * CELDA, x0 + c[1] * CELDA] for c in puntos]
        coords[0] = [aldeas[i]["x"], aldeas[i]["z"]]; coords[-1] = [aldeas[j]["x"], aldeas[j]["z"]]
        out.append({"i": i, "j": j, "tipo": tipo, "bloques": round(largo * CELDA), "coords": coords})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("semilla")
    ap.add_argument("version", help="ej. 1.21 (Java Edition, 1.18 o superior)")
    ap.add_argument("--lado", type=int, default=8000, help="bloques de lado, centrado en 0,0")
    ap.add_argument("--bpp", type=int, default=2, choices=[1, 2, 4], help="bloques por píxel")
    ap.add_argument("--cuadricula", type=int, default=500, help="bloques entre líneas (500 = 1 h a pie)")
    ap.add_argument("--nether", action="store_true")
    ap.add_argument("--campaña", default="Tierra de Bloques")
    a = ap.parse_args()

    camp = VAULT / "01 - Campañas" / a.campaña
    if not camp.is_dir():
        sys.exit(f"No existe la campaña: {camp}")
    nombre = "Mapa del Nether" if a.nether else "Mapa del Mundo"
    carpeta_img = camp / "10 - images"
    carpeta_img.mkdir(exist_ok=True)
    salida = carpeta_img / nombre

    compilar()
    cuad = a.cuadricula if not a.nether else max(1, a.cuadricula // 8)  # en el Nether 1 bloque = 8 del mundo
    # El binario escribe en su carpeta con un nombre ASCII: en Windows, fopen() falla con rutas con tildes o ñ
    tmp = AQUI / "_salida"
    run([str(BIN), a.semilla, a.version, str(a.lado), str(a.bpp), "nether" if a.nether else "overworld", str(cuad), tmp.name], cwd=AQUI)
    ppm_a_png(f"{tmp}.ppm", f"{salida}.png")
    with open(f"{tmp}.csv", newline="", encoding="utf-8") as f:
        filas = [dict(r, x=int(r["x"]), z=int(r["z"])) for r in csv.DictReader(f)]
    with open(f"{tmp}.agua", encoding="utf-8") as f:
        agua = f.read().split()
    with open(f"{tmp}.biomas", encoding="utf-8") as f:
        presentes = [l.strip().split(",") for l in f if l.strip()]
    for ext in ("ppm", "csv", "agua", "biomas"):
        os.remove(f"{tmp}.{ext}")
    total = sum(int(b[5]) for b in presentes)
    leyenda_biomas = "\n".join(
        f'| <span style="display:inline-block;width:1.6em;height:1em;background:rgb({r},{g},{b});border:1px solid #000"></span> '
        f'| {BIOMAS.get(nom, (nom, ""))[0]} | {int(c) * 100 / total:.1f} % | {BIOMAS.get(nom, ("", ""))[1]} |'
        for _, nom, r, g, b, c in sorted(presentes, key=lambda b: -int(b[5])))

    # Aldeas numeradas por cercanía al punto de aparición, y red de caminos / rutas marítimas entre ellas
    spawn = next((r for r in filas if r["tipo"] == "Punto de aparición"), {"x": 0, "z": 0})
    aldeas = sorted((r for r in filas if r["tipo"] == "Aldea"), key=lambda r: (r["x"] - spawn["x"]) ** 2 + (r["z"] - spawn["z"]) ** 2)
    for k, r in enumerate(aldeas, 1):
        r["nombre"] = f"Aldea {k}"
    red = rutas(aldeas, agua, -(a.lado - a.lado % 4) // 2) if len(aldeas) > 1 else []
    puertos = {t[k] for t in red if t["tipo"] == "mar" for k in ("i", "j")}
    for k in puertos:
        aldeas[k]["puerto"] = True

    # Tipos de marcador para las notas de esta carpeta (el plugin lee markers.json junto a la nota)
    iconos = {v[0]: v for v in [*TIPOS.values(), PUERTO]}
    (camp / "markers.json").write_text(json.dumps(
        [{"type": t, "iconName": i, "color": c, "layer": False, "alpha": 1} for t, i, c in iconos.values()],
        ensure_ascii=False, indent=2), encoding="utf-8")

    # Leaflet: latitud = -Z (norte arriba), longitud = X. Así 1 unidad del mapa = 1 bloque.
    m = a.lado // 2
    def marcador(r):
        tipo = PUERTO[0] if r.get("puerto") else TIPOS[r["tipo"]][0]
        nombre = r.get("nombre", r["tipo"]) + (" ⚓ puerto" if r.get("puerto") else "")
        return f'    - "{tipo},{-r["z"]},{r["x"]},,{nombre} (X {r["x"]} · Z {r["z"]})"'
    # Una sola clave `marker:` con lista: si se repite la clave, el YAML falla y Leaflet pierde `bounds`
    marcadores = [marcador(r) for r in filas if r["tipo"] in TIPOS]
    resumen = {}
    for r in filas:
        resumen[r["tipo"]] = resumen.get(r["tipo"], 0) + 1

    # GeoJSON con las rutas: coordenadas [longitud, latitud] = [X, -Z]
    geo = camp / f"Rutas - {nombre}.geojson"
    filas_rutas = []
    if red:
        feats = []
        for t in sorted(red, key=lambda t: (t["i"], t["j"])):
            A, B = aldeas[t["i"]]["nombre"], aldeas[t["j"]]["nombre"]
            horas = t["bloques"] / (500 if t["tipo"] == "camino" else 1000)
            medio = "a pie" if t["tipo"] == "camino" else "en barco"
            feats.append({"type": "Feature",
                          "properties": {"name": f"{'🛤️ Camino' if t['tipo'] == 'camino' else '⛵ Ruta marítima'} {A} ↔ {B}: {t['bloques']} bloques, {horas:.1f} h {medio}",
                                         "stroke": "#a0522d" if t["tipo"] == "camino" else "#1e90ff", "stroke-width": 3, "stroke-opacity": 0.9},
                          "geometry": {"type": "LineString", "coordinates": [[x, -z] for x, z in t["coords"]]}})
            filas_rutas.append(f"| {A} ↔ {B} | {'🛤️ Camino' if t['tipo'] == 'camino' else '⛵ Mar'} | {t['bloques']} | {horas:.1f} h {medio}"
                               + (f" ({t['bloques'] / 1000:.1f} h a caballo)" if t["tipo"] == "camino" else "") + " |")
        geo.write_text(json.dumps({"type": "FeatureCollection", "features": feats}, ensure_ascii=False), encoding="utf-8")

    escala_nota = ("1 bloque del Nether = 8 del mundo: 1 h de viaje aquí = 8 h en la superficie."
                   if a.nether else f"Cada cuadro de la cuadrícula = {a.cuadricula} bloques = 1 hora a pie (½ a caballo).")
    nota = f"""---
tipo: mapa
campaña: "{a.campaña}"
semilla: "{a.semilla}"
version: "{a.version}"
dimension: {"nether" if a.nether else "overworld"}
tags:
  - dnd/mapa
---

# 🗺️ {nombre}

Semilla **{a.semilla}** · Java {a.version} · {a.lado}×{a.lado} bloques centrados en 0,0 · generado con cubiomes.
{escala_nota}
Qué se puede encontrar en cada lugar: [[Botín por Lugar]].

> [!tip] Cómo usarlo (plugin **Leaflet**)
> - **Medir:** Shift + clic en un punto y Shift + clic en otro. La distancia sale en bloques (abajo a la izquierda).
> - **Horas de viaje:** bloques ÷ 500 a pie, ÷ 1000 a caballo o en barco, y ÷ 8 adicional por el Nether.\n> - **Pasa el ratón** por un icono o una ruta para ver qué es.
> - **Coordenadas:** el mapa usa las del juego. En `location: [lat, long]` de un lugar pon **[−Z, X]** (la Z cambia de signo para que el norte quede arriba).
> - Clic derecho → crear marcador propio.

```leaflet
id: {nombre.lower().replace(' ', '-')}-{a.campaña.lower().replace(' ', '-')}
image: [[{nombre}.png]]
bounds:
    - [{m}, {-m}]
    - [{-m}, {m}]
height: 700px
minZoom: -5
maxZoom: 3
defaultZoom: -3
zoomDelta: 0.5
unit: bloques
scale: 1
markerFolder: 01 - Campañas/{a.campaña}/05 - Lugares
draw: true
{f'geojson: [[{geo.name}]]' + chr(10) if red else ''}marker:
{chr(10).join(marcadores)}
```

## 📍 Estructuras en el mapa
| Estructura | Cantidad |
|---|---|
{chr(10).join(f"| {k} | {v} |" for k, v in sorted(resumen.items()))}

{"## 🛤️ Caminos y rutas marítimas" + chr(10) + "Red mínima que une todas las aldeas. Los caminos rodean el mar y cruzan los ríos con puente; si por tierra hay que dar un rodeo de más del doble, se va en barco entre puertos (⚓)." + chr(10) + chr(10) + "| Ruta | Tipo | Bloques | Tiempo |" + chr(10) + "|---|---|---|---|" + chr(10) + chr(10).join(filas_rutas) + chr(10) + chr(10) if filas_rutas else ""}## 🧭 Iconos de Leaflet
🏠 Aldea · ⚓ Aldea con puerto · 🚩 Puesto de saqueadores · 🏚️ Mansión · 🌊 Monumento oceánico · 🗿 Templo · 🧙 Cabaña de bruja · 💀 Ciudad antigua · ♜ Fortaleza del End · 🔑 Cámaras de desafío · ⭐ Punto de aparición

## 🌍 Biomas (colores del mapa)
Ordenados de más a menos extensión. El mapa se toma a nivel del mar: donde hay colinas o montañas sale el bioma de la cueva que hay debajo (manchas marrones y verde oscuro).

| Color | Bioma | Del mapa | En la partida |
|---|---|---|---|
{leyenda_biomas}

## 🎨 Estructuras dibujadas en la imagen
{chr(10).join(f"- {c}: {t}" for c, t in LEYENDA)}
- Líneas oscuras: cuadrícula cada {cuad} bloques.

> [!warning] Aproximado
> Las estructuras se calculan por bioma. En el juego alguna puede no generarse por el terreno (sobre todo aldeas en laderas).
"""
    (camp / f"{nombre}.md").write_text(nota, encoding="utf-8")
    print(f"Imagen: {salida}.png\nNota:   {camp / (nombre + '.md')}\nEstructuras: {resumen}")


if __name__ == "__main__":
    main()
