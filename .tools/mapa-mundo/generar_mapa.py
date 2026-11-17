#!/usr/bin/env python3
"""Genera el mapa del mundo de una semilla de Minecraft Java para una campaña del vault.

Uso (desde la raíz del vault):
  python3 .tools/mapa-mundo/generar_mapa.py <semilla> <version> [--lado 8000] [--bpp 2] [--cuadricula 500] [--nether]
      [--campaña "Tierra de Bloques"]

Crea:
  01 - Campañas/<campaña>/10 - images/Mapa del Mundo.png   (o "Mapa del Nether.png")
  01 - Campañas/<campaña>/Mapa del Mundo.md                (nota con el mapa Leaflet y marcadores)
"""
import argparse, csv, os, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VAULT = AQUI.parent.parent
CUBIOMES = AQUI.parent / "cubiomes"
BIN = AQUI / "mapa"

# Estructuras que van como marcador clicable en Leaflet (el resto solo se dibuja en la imagen)
MARCADORES = {"Aldea", "Puesto de saqueadores", "Mansión del bosque", "Monumento oceánico", "Templo del desierto",
              "Templo de la jungla", "Cabaña de bruja", "Ciudad antigua", "Fortaleza del End",
              "Punto de aparición", "Fortaleza del Nether", "Bastión"}  # cámaras de desafío, ruinas e iglús salen cientos: solo en la imagen

LEYENDA = [("🟨", "Aldea"), ("⬛ gris", "Puesto de saqueadores"), ("🟫", "Mansión del bosque"), ("🟦 cian", "Monumento oceánico"),
           ("🟧 arena", "Templo del desierto"), ("🟩", "Templo de la jungla / cabaña de bruja (verde oscuro)"),
           ("🟪 grande", "Fortaleza del End"), ("🟪 pequeño", "Portal en ruinas"), ("⬜", "Punto de aparición / iglú"),
           ("🟧", "Cámaras de desafío"), ("⬛ azul noche", "Ciudad antigua"), ("🟥 líneas", "Ejes 0,0")]


def run(cmd, **kw):
    r = subprocess.run(cmd, **kw)
    if r.returncode:
        sys.exit(f"Falló: {' '.join(map(str, cmd))}")


def compilar():
    if not (CUBIOMES / "libcubiomes.a").exists():
        if not CUBIOMES.exists():
            run(["git", "clone", "--depth", "1", "https://github.com/Cubitect/cubiomes.git", str(CUBIOMES)])
        run(["make", "-C", str(CUBIOMES), "libcubiomes"])
    src = AQUI / "mapa.c"
    if not BIN.exists() or BIN.stat().st_mtime < src.stat().st_mtime:
        run(["gcc", "-O2", str(src), f"-I{CUBIOMES}", str(CUBIOMES / "libcubiomes.a"), "-lm", "-o", str(BIN)])


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
    tmp = os.environ.get("TMPDIR")  # ImageMagick necesita una carpeta temporal escribible
    env = dict(os.environ, MAGICK_TEMPORARY_PATH=tmp) if tmp else None
    cuad = a.cuadricula if not a.nether else max(1, a.cuadricula // 8)  # en el Nether 1 bloque = 8 del mundo
    run([str(BIN), a.semilla, a.version, str(a.lado), str(a.bpp), "nether" if a.nether else "overworld", str(cuad), str(salida)])
    run(["magick", f"{salida}.ppm", f"{salida}.png"], env=env)
    os.remove(f"{salida}.ppm")

    with open(f"{salida}.csv", newline="") as f:
        filas = list(csv.DictReader(f))
    os.remove(f"{salida}.csv")

    # Leaflet: latitud = -Z (norte arriba), longitud = X. Así 1 unidad del mapa = 1 bloque.
    m = a.lado // 2
    marcadores = [f'marker: default,{-int(r["z"])},{int(r["x"])},,{r["tipo"]} (X {r["x"]} · Z {r["z"]})'
                  for r in filas if r["tipo"] in MARCADORES]
    resumen = {}
    for r in filas:
        resumen[r["tipo"]] = resumen.get(r["tipo"], 0) + 1

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

> [!tip] Cómo usarlo (plugin **Leaflet**)
> - **Medir:** Shift + clic en un punto y Shift + clic en otro. La distancia sale en bloques (abajo a la izquierda).
> - **Horas de viaje:** bloques ÷ 500 a pie, ÷ 1000 a caballo, y ÷ 8 adicional por el Nether.
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
{chr(10).join(marcadores)}
```

## 📍 Estructuras en el mapa
| Estructura | Cantidad |
|---|---|
{chr(10).join(f"| {k} | {v} |" for k, v in sorted(resumen.items()))}

## 🎨 Leyenda de la imagen
{chr(10).join(f"- {c}: {t}" for c, t in LEYENDA)}
- Líneas oscuras: cuadrícula cada {cuad} bloques.

> [!warning] Aproximado
> Las estructuras se calculan por bioma. En el juego alguna puede no generarse por el terreno (sobre todo aldeas en laderas).
"""
    (camp / f"{nombre}.md").write_text(nota, encoding="utf-8")
    print(f"Imagen: {salida}.png\nNota:   {camp / (nombre + '.md')}\nEstructuras: {resumen}")


if __name__ == "__main__":
    main()
