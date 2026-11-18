#!/usr/bin/env python3
"""Battlemap pixel-art de la arena del End de Tierra de Bloques (solo librería estándar).

Uso (desde la raíz del vault):  python3 .tools/battlemaps/battlemaps.py
Escribe los PNG en  01 - Campañas/Tierra de Bloques/10 - images/Battlemaps/
1 casilla = 1 bloque = 1,5 m. Norte arriba.

La arena sale de la semilla (pilares con end_pilares.py, suelo de end_suelo.txt generado con cubiomes).
Las estructuras se exportan del mundo real (ver nota Battlemaps), no se dibujan aquí.
Si ImageMagick (`magick`) está instalado, añade etiquetas de texto a los pilares del End.
"""
import random, shutil, struct, subprocess, sys, zlib
from pathlib import Path

AQUI = Path(__file__).resolve().parent
VAULT = AQUI.parent.parent
SALIDA = VAULT / "01 - Campañas" / "Tierra de Bloques" / "10 - images" / "Battlemaps"
SEMILLA = -4697940382757111526
sys.path.insert(0, str(AQUI))
from end_pilares import pilares  # noqa: E402

T = 16  # píxeles de textura por bloque

# ---------------------------------------------------------------- materiales
# char -> (nombre, color base, estilo, sólido)
MAT = {
    ".": ("Hierba", (96, 150, 60), "ruido", False),
    ",": ("Camino de tierra", (140, 105, 65), "ruido", False),
    "s": ("Arena", (219, 207, 160), "arena", False),
    "n": ("Nieve", (240, 248, 250), "arena", False),
    "w": ("Agua", (50, 90, 190), "agua", False),
    "l": ("Nenúfar", (50, 90, 190), "nenufar", False),
    "h": ("Hojas / maleza (terreno difícil)", (40, 110, 35), "hojas", False),
    "p": ("Tablones de roble", (160, 125, 75), "tablas", False),
    "k": ("Tablones de abeto", (110, 80, 50), "tablas", False),
    "q": ("Tablones de roble oscuro", (70, 48, 25), "tablas", False),
    "S": ("Arenisca", (215, 200, 145), "ladrillo_liso", False),
    "T": ("Terracota naranja", (160, 85, 40), "ruido", False),
    "A": ("Terracota azul", (75, 60, 95), "ruido", False),
    "c": ("Ladrillo de piedra", (122, 122, 122), "ladrillo", False),
    "j": ("Suelo de piedra", (150, 145, 132), "ruido", False),
    "u": ("Toba", (100, 102, 95), "ruido", False),
    "U": ("Cobre", (190, 110, 80), "ladrillo_liso", False),
    "r": ("Alfombra roja", (160, 40, 40), "ruido", False),
    "e": ("Piedra del End", (221, 223, 165), "piedras", False),
    "v": ("Vacío", (8, 6, 14), "vacio", False),
    "V": ("Portal de salida (inactivo hasta matar al dragón)", (8, 6, 14), "vacio", False),
    # sólidos (muros, columnas): no se pueden atravesar
    "X": ("Muro de arenisca", (165, 140, 85), "ladrillo_liso", True),
    "C": ("Muro de roca", (118, 118, 118), "piedras", True),
    "M": ("Muro de roca musgosa", (100, 120, 90), "piedras_musgo", True),
    "R": ("Muro de ladrillo de piedra", (110, 110, 110), "ladrillo", True),
    "L": ("Tronco", (105, 80, 50), "tronco", True),
    "K": ("Muro de abeto", (95, 68, 40), "tablas_v", True),
    "D": ("Muro de roble oscuro", (60, 40, 20), "tablas_v", True),
    "N": ("Muro de nieve", (230, 238, 242), "ladrillo_liso", True),
    "Y": ("Muro de ladrillo de toba", (85, 88, 80), "ladrillo", True),
    "B": ("Roca madre", (70, 70, 70), "piedras", True),
    "O": ("Obsidiana", (25, 18, 40), "obsidiana", True),
    "H": ("Barrotes de hierro", (150, 150, 150), "barrotes", True),
    "y": ("Tienda (lana)", (225, 225, 220), "ruido", True),
}

# Objetos: char -> (nombre, sólido). Se dibujan encima del suelo del mapa.
OBJ = {
    "#": ("Cofre", True), "*": ("Generador", True), "o": ("Caldero", True), "=": ("Cama", False),
    "+": ("Mesa de crafteo", True), "f": ("Horno", True), "t": ("TNT", True), "_": ("Placa de presión", False),
    "/": ("Palanca", True), "d": ("Dispensador de flechas", True), "!": ("Antorcha", False),
    "@": ("Cristal del End", True), "&": ("Cristal del End enjaulado", True), "%": ("Vasija / maceta", True),
    "$": ("Bóveda (se abre con llave)", True), "b": ("Soporte de pociones", True), "a": ("Aldeano", False),
    "z": ("Aldeano zombi", False), "G": ("Gólem de hierro", False), "^": ("Escalera / trampilla", False),
    "x": ("Cable trampa", False), "P": ("Pilar central con antorchas", True),
}


def clamp(v):
    return 0 if v < 0 else 255 if v > 255 else int(v)


def tono(c, f):
    return tuple(clamp(x * f) for x in c)


def textura(ch, variante):
    """16x16 lista de filas de tuplas RGB."""
    nombre, base, estilo, _ = MAT[ch]
    rnd = random.Random(f"{ch}{variante}")
    px = [[base] * T for _ in range(T)]
    def ruido(a):
        for y in range(T):
            for x in range(T):
                px[y][x] = tono(base, 1 + rnd.uniform(-a, a))
    if estilo in ("ruido", "arena", "hojas", "nenufar"):
        ruido({"ruido": 0.12, "arena": 0.06, "hojas": 0.25, "nenufar": 0.08}[estilo])
        if estilo == "hojas":
            for _ in range(10):
                x, y = rnd.randrange(T), rnd.randrange(T)
                px[y][x] = tono(base, 0.5)
        if estilo == "nenufar":
            cx, cy = 8, 8
            for y in range(T):
                for x in range(T):
                    if (x - cx) ** 2 + (y - cy) ** 2 < 30 and not (x > cx and abs(y - cy) < 2):
                        px[y][x] = tono((60, 140, 40), 1 + rnd.uniform(-0.1, 0.1))
    elif estilo == "agua":
        ruido(0.05)
        for y in range(2 + variante % 3, T, 5):
            for x in range(T):
                if (x + y + variante) % 6 < 3:
                    px[y][x] = tono(base, 1.35)
    elif estilo in ("tablas", "tablas_v"):
        ruido(0.06)
        for y in range(T):
            for x in range(T):
                a, b = (y, x) if estilo == "tablas" else (x, y)
                if a % 4 == 3 or (b == (5 * (a // 4) + 3 * variante) % T and a % 4 != 3):
                    px[y][x] = tono(base, 0.68)
    elif estilo == "tronco":
        for y in range(T):
            for x in range(T):
                d = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** 0.5
                px[y][x] = tono(base, (0.8 if int(d) % 3 == 0 else 1.1) if d < 6.5 else 0.7)
    elif estilo in ("piedras", "piedras_musgo", "obsidiana"):
        ruido(0.1 if estilo != "obsidiana" else 0.3)
        for _ in range(7):
            cx, cy, r = rnd.randrange(T), rnd.randrange(T), rnd.uniform(1.5, 3.5)
            f = rnd.choice((0.75, 1.2))
            for y in range(T):
                for x in range(T):
                    if (x - cx) ** 2 + (y - cy) ** 2 < r * r:
                        px[y][x] = tono(px[y][x], f)
        if estilo == "piedras_musgo":
            for _ in range(25):
                x, y = rnd.randrange(T), rnd.randrange(T)
                px[y][x] = tono((70, 130, 50), 1 + rnd.uniform(-0.2, 0.2))
        if estilo == "obsidiana":
            for _ in range(4):
                x, y = rnd.randrange(T), rnd.randrange(T)
                px[y][x] = (110, 60, 160)
    elif estilo in ("ladrillo", "ladrillo_liso"):
        ruido(0.05 if estilo == "ladrillo_liso" else 0.1)
        for y in range(T):
            for x in range(T):
                fila = y // 4
                if y % 4 == 3 or (estilo == "ladrillo" and (x + (fila % 2) * 4) % 8 == 7):
                    px[y][x] = tono(base, 0.72)
    elif estilo == "vacio":
        for y in range(T):
            for x in range(T):
                px[y][x] = tono(base, 1 + rnd.uniform(-0.3, 0.3))
        for _ in range(2):
            px[rnd.randrange(T)][rnd.randrange(T)] = (200, 190, 230)
    elif estilo == "barrotes":
        for y in range(T):
            for x in range(T):
                px[y][x] = (150, 150, 150) if x % 4 == 1 or y % 8 == 1 else (40, 40, 45)
    return px


def dibujar_objeto(px, ch):
    """Pinta el icono del objeto sobre una textura 16x16."""
    def rect(x0, y0, x1, y1, c):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                px[y][x] = c
    def circulo(cx, cy, r, c, hueco=0):
        for y in range(T):
            for x in range(T):
                d = (x - cx) ** 2 + (y - cy) ** 2
                if hueco ** 2 <= d <= r * r:
                    px[y][x] = c
    if ch == "#":
        rect(2, 3, 13, 13, (60, 40, 15)); rect(3, 4, 12, 12, (150, 100, 40)); rect(3, 7, 12, 7, (60, 40, 15)); rect(7, 6, 8, 9, (230, 200, 80))
    elif ch == "*":
        rect(1, 1, 14, 14, (30, 30, 40)); circulo(7.5, 7.5, 3.5, (240, 120, 30))
        for i in range(1, 15, 3):
            rect(i, 1, i, 14, (90, 90, 100)); rect(1, i, 14, i, (90, 90, 100))
    elif ch == "o":
        circulo(7.5, 7.5, 6.5, (45, 45, 50)); circulo(7.5, 7.5, 4.5, (120, 60, 160))
    elif ch == "=":
        rect(2, 1, 13, 14, (170, 30, 30)); rect(3, 2, 12, 4, (235, 235, 235))
    elif ch == "+":
        rect(1, 1, 14, 14, (120, 85, 45)); rect(3, 3, 12, 12, (165, 120, 70))
        for i in (5, 8, 11):
            rect(i, 3, i, 12, (90, 60, 30)); rect(3, i, 12, i, (90, 60, 30))
    elif ch == "f":
        rect(1, 1, 14, 14, (95, 95, 95)); rect(4, 7, 11, 12, (25, 25, 25)); rect(5, 10, 10, 11, (240, 140, 30))
    elif ch == "t":
        rect(1, 1, 14, 14, (200, 40, 30)); rect(1, 6, 14, 9, (235, 235, 235)); rect(4, 7, 11, 8, (30, 30, 30))
    elif ch == "_":
        rect(3, 3, 12, 12, (90, 90, 90)); rect(4, 4, 11, 11, (135, 135, 135))
    elif ch == "/":
        rect(4, 10, 11, 13, (110, 110, 110))
        for i in range(6):
            rect(6 + i // 2, 9 - i, 7 + i // 2, 9 - i, (120, 85, 45))
        rect(9, 2, 10, 3, (200, 30, 30))
    elif ch == "d":
        rect(1, 1, 14, 14, (110, 110, 110)); rect(5, 5, 10, 10, (20, 20, 20)); rect(6, 6, 9, 9, (60, 60, 60))
    elif ch == "!":
        rect(7, 6, 8, 13, (120, 85, 45)); rect(6, 3, 9, 6, (255, 200, 50)); rect(7, 4, 8, 5, (255, 255, 200))
    elif ch in "@&":
        for y in range(T):
            for x in range(T):
                d = abs(x - 7.5) + abs(y - 7.5)
                if d < 7:
                    px[y][x] = (230, 120, 230) if d > 3 else (255, 240, 255)
        if ch == "&":
            for i in range(0, T, 4):
                rect(i, 0, i, 15, (170, 170, 175)); rect(0, i, 15, i, (170, 170, 175))
    elif ch == "%":
        circulo(7.5, 8.5, 6, (150, 75, 45)); circulo(7.5, 8.5, 2.5, (60, 30, 20))
    elif ch == "$":
        rect(1, 1, 14, 14, (40, 40, 45)); circulo(7.5, 7.5, 4.5, (230, 170, 40), 2.5)
    elif ch == "b":
        circulo(7.5, 7.5, 2, (90, 90, 90))
        for cx, cy in ((3, 11), (12, 11), (7, 3)):
            circulo(cx, cy, 2, (200, 60, 200))
    elif ch in "azG":
        cuerpo = {"a": (120, 80, 50), "z": (60, 120, 60), "G": (200, 195, 185)}[ch]
        circulo(7.5, 7.5, 6.5, (20, 20, 20)); circulo(7.5, 7.5, 5.5, cuerpo)
        rect(5, 6, 6, 7, (20, 20, 20)); rect(9, 6, 10, 7, (20, 20, 20))
    elif ch == "^":
        rect(3, 0, 4, 15, (120, 85, 45)); rect(11, 0, 12, 15, (120, 85, 45))
        for y in (2, 6, 10, 14):
            rect(3, y, 12, y, (150, 110, 60))
    elif ch == "x":
        rect(0, 7, 15, 7, (200, 200, 200)); rect(0, 6, 1, 9, (110, 110, 110)); rect(14, 6, 15, 9, (110, 110, 110))
    elif ch == "P":
        rect(3, 3, 12, 12, (70, 70, 70))
        for cx, cy in ((7, 1), (7, 14), (1, 7), (14, 7)):
            rect(cx, cy, cx + 1, cy, (255, 200, 50))


_cache = {}


def tile(ch, base, var, k, luz=1.0):
    """Filas (bytes) de la casilla ya escalada (16*k px) con relieve y cuadrícula."""
    clave = (ch, base, var, k, round(luz, 2))
    if clave in _cache:
        return _cache[clave]
    px = textura(ch if ch in MAT else base, var)
    if ch in OBJ:
        dibujar_objeto(px, ch)
    solido = MAT[ch][3] if ch in MAT else OBJ[ch][1]
    if solido:  # relieve: borde claro arriba-izquierda, oscuro abajo-derecha
        for i in range(T):
            for j in (0, 1):
                px[j][i] = tono(px[j][i], 1.3); px[i][j] = tono(px[i][j], 1.3)
                px[T - 1 - j][i] = tono(px[T - 1 - j][i], 0.55); px[i][T - 1 - j] = tono(px[i][T - 1 - j], 0.55)
    filas = []
    for y in range(T):
        fila = bytes(v for x in range(T) for c in [tono(px[y][x], luz)] for v in c * k)
        filas += [fila] * k
    lado = T * k
    # cuadrícula: primera fila y columna de cada casilla más oscuras
    filas[0] = bytes(clamp(v * 0.55) for v in filas[0])
    filas = [bytes(clamp(v * 0.55) for v in f[:3]) + f[3:] for f in filas]
    assert len(filas) == lado and len(filas[0]) == lado * 3
    _cache[clave] = filas
    return filas


def png(ruta, filas_px):
    w, h = len(filas_px[0]) // 3, len(filas_px)
    crudo = b"".join(b"\0" + f for f in filas_px)
    trozo = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    Path(ruta).write_bytes(b"\x89PNG\r\n\x1a\n" + trozo(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                           + trozo(b"IDAT", zlib.compress(crudo, 9)) + trozo(b"IEND", b""))


def render(nombre, filas, suelo, k=4, luz=None, base_obj=None):
    alto, ancho = len(filas), max(map(len, filas))
    filas = [f.ljust(ancho, suelo) for f in filas]
    out = []
    for y, f in enumerate(filas):
        tiles = [tile(ch, (base_obj or {}).get(ch, suelo), (x * 73856093 ^ y * 19349663) % 4, k, luz(x, y) if luz else 1.0)
                 for x, ch in enumerate(f)]
        for r in range(T * k):
            out.append(b"".join(t[r] for t in tiles))
    ruta = SALIDA / f"{nombre}.png"
    png(ruta, out)
    print(f"{ruta.name}: {ancho}x{alto} casillas, {ancho * T * k}x{alto * T * k} px")
    return ruta


class Rejilla:
    def __init__(self, w, h, ch):
        self.g = [[ch] * w for _ in range(h)]

    def set(self, x, y, ch):
        if 0 <= y < len(self.g) and 0 <= x < len(self.g[0]):
            self.g[y][x] = ch

    def rect(self, x0, y0, x1, y1, ch, borde=None):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                es_borde = x in (x0, x1) or y in (y0, y1)
                if borde is None or es_borde:
                    self.set(x, y, borde if es_borde and borde else ch)
                else:
                    self.set(x, y, ch)

    def filas(self):
        return ["".join(f) for f in self.g]


# ---------------------------------------------------------------- mapas
def arena_end():
    suelo = [list(map(int, l.split())) for l in open(AQUI / "end_suelo.txt")]
    R0 = (len(suelo) - 1) // 2  # el archivo cubre -64..64
    R = 60
    g = Rejilla(2 * R + 1, 2 * R + 1, "e")
    alt = lambda x, y: suelo[y - R + R0][x - R + R0]
    for y in range(2 * R + 1):
        for x in range(2 * R + 1):
            if alt(x, y) == 0:
                g.set(x, y, "v")
    # Portal de salida en 0,0: borde de roca madre, hueco del portal y pilar central
    for y in range(-4, 5):
        for x in range(-4, 5):
            d = (x * x + y * y) ** 0.5
            if d <= 2.5:
                g.set(R + x, R + y, "V")
            elif d <= 3.5:
                g.set(R + x, R + y, "B")
    g.set(R, R, "P")
    datos = []
    for i, (px_, pz, radio, h, jaula) in enumerate(pilares(SEMILLA), 1):
        for z in range(-radio, radio + 1):
            for x in range(-radio, radio + 1):
                if x * x + z * z <= radio * radio + 1:
                    g.set(R + px_ + x, R + pz + z, "O")
        g.set(R + px_, R + pz, "&" if jaula else "@")
        datos.append((i, px_, pz, radio, h, jaula, alt(R + px_, R + pz)))
    luz = lambda x, y: 1 + (alt(x, y) - 60) * 0.035 if alt(x, y) else 1.0
    filas = g.filas()
    sobre = {"@": "O", "&": "O", "P": "B"}  # el cristal va encima del pilar de obsidiana
    completo = render("End - Arena del Dragón", filas, "e", k=3, luz=luz, base_obj=sobre)
    c = 22  # zona central (perchado del dragón)
    centro = render("End - Centro y portal", [f[R - c:R + c + 1] for f in filas[R - c:R + c + 1]], "e", k=4,
                    luz=lambda x, y: luz(x + R - c, y + R - c), base_obj=sobre)
    return completo, datos, R


def etiquetas_end(ruta, datos, R, k):
    """Texto sobre la imagen con ImageMagick si está disponible (opcional)."""
    if not shutil.which("magick"):
        print("magick no está instalado: arena del End sin etiquetas")
        return
    lado = T * k
    fuentes = ["/usr/share/fonts/liberation/LiberationSans-Bold.ttf", "/usr/share/fonts/noto/NotoSans-Bold.ttf",
               "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", "C:/Windows/Fonts/arialbd.ttf"]
    fuente = next((f for f in fuentes if Path(f).exists()), None)
    args = ["magick", str(ruta)] + (["-font", fuente] if fuente else []) + ["-pointsize", "110",
            "-stroke", "black", "-strokewidth", "3", "-fill", "white"]
    for i, x, z, radio, h, jaula, y0 in datos:
        px_ = (R + x + radio + 1) * lado + 10
        py_ = (R + z) * lado + 40
        args += ["-annotate", f"+{px_}+{py_}", f"{i}"]
    args += ["-annotate", f"+{R * lado - 40}+{(R - 6) * lado}", "N"]
    args.append(str(ruta))
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError:
        print("No se pudieron poner etiquetas (fuente no encontrada)")


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    completo, datos, R = arena_end()
    etiquetas_end(completo, datos, R, 3)
    print("\nPilares del End (n, x, z, radio, altura y, enjaulado, suelo y):")
    for d in datos:
        print(d)


if __name__ == "__main__":
    main()
