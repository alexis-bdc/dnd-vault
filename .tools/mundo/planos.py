#!/usr/bin/env python3
"""Planos por planta de estructuras REALES del mundo de la semilla (servidor Minecraft + uNmINeD).

Requisitos: el mundo ya generado en .tools/mundo/mundo (ver estructuras.json y la nota Battlemaps),
uNmINeD CLI en .tools/mundo/unmined y ImageMagick (`magick`) para escalar y poner la cuadrícula.

Para cada estructura lee del mundo sus piezas (cajas BB guardadas por el juego), agrupa las alturas
del suelo de las piezas en plantas y renderiza cada planta cortando por Y (--topY) con uNmINeD.
"""
import json, struct, subprocess, sys, zlib
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VAULT = AQUI.parent.parent
MUNDO = AQUI / "mundo"
UNMINED = next((AQUI / "unmined").glob("*/unmined-cli"))
SALIDA = VAULT / "01 - Campañas" / "Tierra de Bloques" / "10 - images" / "Battlemaps"
PX = 32  # píxeles por bloque en el PNG final (= casilla del VTT)
CLIENTE = AQUI / "client.jar"  # texturas del juego (Minecraft Java 1.21.1, descargado de Mojang)
DIMS = {"overworld": ("", 0), "the_nether": ("DIM-1", -1), "the_end": ("DIM1", 1)}
MAX_PLANTAS = 6
ALTAS = {"minecraft:monument", "minecraft:ancient_city", "minecraft:desert_pyramid", "minecraft:jungle_pyramid"}  # pocas piezas altas: corte cada 6 bloques
# Cortes revisados a ojo que solo muestran tejado, agua o terreno
DESCARTAR = {"Ciudad antigua - Planta 5 (Y -28)", "Fortaleza del End - Planta 1 (Y -3)", "Fortaleza del Nether 1 - Planta 3 (Y 66)",
             "Mansión del bosque - Planta 4 (Y 99)", "Monumento oceánico - Planta 4 (Y 57)", "Iglú 1 - Planta 2 (Y 35)"}


# ---------------------------------------------------------------- NBT (formato de Minecraft)
def nbt(datos):
    pos = 0
    def leer(fmt):
        nonlocal pos
        v = struct.unpack_from(">" + fmt, datos, pos); pos += struct.calcsize(">" + fmt)
        return v[0]
    def cadena():
        nonlocal pos
        n = leer("H"); s = datos[pos:pos + n].decode("utf-8", "replace"); pos += n
        return s
    def valor(t):
        nonlocal pos
        if t == 1: return leer("b")
        if t == 2: return leer("h")
        if t == 3: return leer("i")
        if t == 4: return leer("q")
        if t == 5: return leer("f")
        if t == 6: return leer("d")
        if t == 7: n = leer("i"); v = datos[pos:pos + n]; pos += n; return v
        if t == 8: return cadena()
        if t == 9:
            st, n = leer("b"), leer("i")
            return [valor(st) for _ in range(n)]
        if t == 10:
            d = {}
            while True:
                st = leer("b")
                if st == 0: return d
                k = cadena(); d[k] = valor(st)
        if t == 11: n = leer("i"); v = list(struct.unpack_from(f">{n}i", datos, pos)); pos += 4 * n; return v
        if t == 12: n = leer("i"); v = list(struct.unpack_from(f">{n}q", datos, pos)); pos += 8 * n; return v
        raise ValueError(f"tag NBT desconocido {t}")
    t = leer("b"); cadena()
    return valor(t)


def chunk(dim, cx, cz):
    carpeta = MUNDO / DIMS[dim][0] / "region" if DIMS[dim][0] else MUNDO / "region"
    reg = (carpeta / f"r.{cx >> 5}.{cz >> 5}.mca").read_bytes()
    i = 4 * ((cx & 31) + (cz & 31) * 32)
    sector = int.from_bytes(reg[i:i + 3], "big")
    if not sector:
        return None
    o = sector * 4096
    largo, comp = struct.unpack_from(">ib", reg, o)
    assert comp == 2, f"compresión {comp} no soportada"
    return nbt(zlib.decompress(reg[o + 5:o + 4 + largo]))


def piezas(dim, x, z):
    """Cajas [x0,y0,z0,x1,y1,z1] de la estructura cuyo inicio está en el chunk del bloque (x, z)."""
    starts = (chunk(dim, x >> 4, z >> 4) or {}).get("structures", {}).get("starts", {})
    validas = [s for s in starts.values() if s.get("id") != "INVALID" and s.get("Children")]
    assert validas, f"no hay estructura en el chunk de {x},{z} (¿mundo sin generar?)"
    s = max(validas, key=lambda s: len(s["Children"]))  # si coinciden dos (p. ej. con una mina), la mayor
    return s["id"], [c["BB"] for c in s["Children"]]


def plantas(cajas):
    """Alturas de suelo agrupadas: las piezas cuyo suelo está a ≤3 bloques forman una planta."""
    ys = sorted({b[1] for b in cajas})
    grupos = [[ys[0]]]
    for y in ys[1:]:
        (grupos[-1].append(y) if y - grupos[-1][-1] <= 3 else grupos.append([y]))
    while len(grupos) > MAX_PLANTAS:  # une las dos plantas más cercanas
        i = min(range(len(grupos) - 1), key=lambda i: grupos[i + 1][0] - grupos[i][-1])
        grupos[i:i + 2] = [grupos[i] + grupos[i + 1]]
    return [(g[0], g[-1]) for g in grupos]


def bloques_y(dim, area, *bloques):
    """Alturas reales de ciertos bloques en el área (cofres, generadores…): marcan dónde hay salas."""
    ys = set()
    for bloque in bloques:
        tmp = AQUI / "_bloques.csv"
        subprocess.run([str(UNMINED), "blockfind", "dump", f"--world={MUNDO}", f"--dimension={DIMS[dim][1]}", f"--block=minecraft:{bloque}",
                        f"--area=b(({area[0]},{area[1]}),({area[2]},{area[3]}))", f"--output={tmp}", "-c"], check=True, stdout=subprocess.DEVNULL)
        ys |= {int(l.split(";")[4]) for l in tmp.read_text().splitlines()[1:] if l.strip()}
        tmp.unlink()
    return sorted(ys)


def tramos(ys, alto=5):
    """Agrupa alturas en plantas de `alto` bloques: [(suelo_min, suelo_max)] (el bloque está 1 por encima del suelo)."""
    out = []
    for y in ys:
        if out and y - 1 - out[-1][0] < alto:
            out[-1] = (out[-1][0], y - 1)
        else:
            out.append((y - 1, y - 1))
    return out


def render(dim, area, salida, top=None, bottom=None):
    tmp = AQUI / "_render.png"
    cmd = [str(UNMINED), "image", "render", f"--world={MUNDO}", f"--output={tmp}", f"--dimension={DIMS[dim][1]}",
           f"--area=b(({area[0]},{area[1]}),({area[2]},{area[3]}))", "--zoom=3", "--blockrender=true", f"--java-client-jar={CLIENTE}", "--background=#141414", "-c"]
    if top is not None:
        cmd += [f"--topY={top}", f"--bottomY={bottom}"]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    # zoom 3 = 8 px por bloque con texturas: se escala sin suavizar y se le pone la cuadrícula de 1 bloque
    rejilla = AQUI / "_rejilla.png"
    if not rejilla.exists():
        subprocess.run(["magick", "-size", f"{PX}x{PX}", "xc:white", "-fill", "#00000060", "-draw", f"rectangle 0,0 {PX - 1},1",
                        "-draw", f"rectangle 0,0 1,{PX - 1}", str(rejilla)], check=True)
    w, h = (v // 8 for v in struct.unpack(">II", tmp.read_bytes()[16:24]))  # bloques, desde la cabecera PNG
    subprocess.run(["magick", str(tmp), "-filter", "point", "-resize", f"{PX * 100 // 8}%",
                    "(", "-size", f"{w * PX}x{h * PX}", f"tile:{rejilla}", ")",
                    "-compose", "multiply", "-composite", str(salida)], check=True)
    tmp.unlink()


def main():
    solo = sys.argv[1:]  # opcional: nombres de estructuras a procesar
    resumen = []
    for nombre, dim, x, z, radio in json.load(open(AQUI / "estructuras.json", encoding="utf-8")):
        if solo and nombre not in solo:
            continue
        sid, cajas = piezas(dim, x, z)
        x0 = max(min(b[0] for b in cajas) - 3, x - radio); z0 = max(min(b[2] for b in cajas) - 3, z - radio)
        x1 = min(max(b[3] for b in cajas) + 3, x + radio); z1 = min(max(b[5] for b in cajas) + 3, z + radio)
        carpeta = SALIDA / nombre
        carpeta.mkdir(parents=True, exist_ok=True)
        archivos = []
        if dim == "overworld" and sid not in ALTAS - {"minecraft:desert_pyramid", "minecraft:jungle_pyramid"} and max(b[4] for b in cajas) >= 55:
            # asoma a la superficie: vista desde arriba (tejados)
            render(dim, (x0, z0, x1, z1), carpeta / f"{nombre} - Exterior.png")
            archivos.append("Exterior")
        if sid.startswith("minecraft:village"):
            niveles = []  # cada casa está a la altura de su terreno: un corte horizontal no sirve
        elif sid in ALTAS:
            y0, y1 = min(b[1] for b in cajas), max(b[4] for b in cajas)
            niveles = [(y, y) for y in range(y0, y1 - 2, 6)][:MAX_PLANTAS]
            if "pyramid" in sid:  # la cámara/sótano queda fuera de la pieza: se añade a la altura de sus cofres
                niveles = sorted(niveles + [(y - 1, y - 1) for y in bloques_y(dim, (x0, z0, x1, z1), "chest") if y < y0])
        elif sid == "minecraft:trial_chambers":  # salas a muchas alturas: una planta por tramo con generadores/bóvedas
            # corte 3 bloques sobre el suelo más bajo del tramo: más arriba se vería el techo de las salas
            niveles = [(ya, ya) for ya, _ in tramos(bloques_y(dim, (x0, z0, x1, z1), "trial_spawner", "vault"))]
        else:
            niveles = plantas(cajas)
        for n, (ya, yb) in enumerate(niveles, 1):
            # cada planta se recorta a sus piezas y se corta 3 bloques sobre el suelo: suelo, muebles y muros, sin techo
            nivel = [b for b in cajas if b[1] <= yb and b[4] >= ya] or cajas  # piezas que ocupan esa altura (o todas)
            area = (max(min(b[0] for b in nivel) - 3, x0), max(min(b[2] for b in nivel) - 3, z0),
                    min(max(b[3] for b in nivel) + 3, x1), min(max(b[5] for b in nivel) + 3, z1))
            etiqueta = f"Planta {n} (Y {ya})"
            if f"{nombre} - {etiqueta}" in DESCARTAR:
                continue
            render(dim, area, carpeta / f"{nombre} - {etiqueta}.png", top=yb + 3, bottom=ya - 2)
            archivos.append(etiqueta)
        resumen.append({"nombre": nombre, "id": sid, "dim": dim, "x": x, "z": z, "area": [x0, z0, x1, z1],
                        "ancho": x1 - x0 + 1, "alto": z1 - z0 + 1, "planos": archivos})
        print(f"{nombre} ({sid}): {x1 - x0 + 1}x{z1 - z0 + 1} bloques, {len(archivos)} planos")
    (AQUI / "planos.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    # autocomprobación del agrupado de plantas
    assert plantas([[0, 10, 0, 0, 0, 0], [0, 12, 0, 0, 0, 0], [0, 20, 0, 0, 0, 0]]) == [(10, 12), (20, 20)]
    assert tramos([-25, -23, -19, -9, -2]) == [(-26, -24), (-20, -20), (-10, -10), (-3, -3)]
    main()
