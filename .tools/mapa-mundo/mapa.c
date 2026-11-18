// Mapa de biomas + estructuras de una semilla de Minecraft Java (vía cubiomes).
// Uso: mapa <semilla> <version> <lado_bloques> <bloques_por_pixel 1|2|4> <overworld|nether> <cuadricula_bloques> <salida_sin_ext>
// Escribe <salida>.ppm (imagen) y <salida>.csv (tipo,x,z). Centro del mapa en 0,0.
#include "generator.h"
#include "finders.h"
#include "util.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

// Semilla de texto -> como Java: String.hashCode() con signo extendido a 64 bits.
static uint64_t parseSeed(const char *s) {
    char *end; errno = 0;
    long long v = strtoll(s, &end, 10);
    if (*s && !*end && !errno) return (uint64_t)v;
    int32_t h = 0;
    for (const unsigned char *p = (const unsigned char *)s; *p; p++) h = 31 * h + *p; // ASCII; tildes en UTF-8 difieren de Java
    return (uint64_t)(int64_t)h;
}

typedef struct { int type; const char *name; unsigned char r, g, b; } Est;

static unsigned char *img; static int W, H, X0, Z0, BPP;

static void px(int x, int y, unsigned char r, unsigned char g, unsigned char b) {
    if (x < 0 || y < 0 || x >= W || y >= H) return;
    unsigned char *p = img + 3 * ((size_t)y * W + x); p[0] = r; p[1] = g; p[2] = b;
}

// Cuadrado con borde negro centrado en el bloque (bx, bz)
static void marca(int bx, int bz, int rad, unsigned char r, unsigned char g, unsigned char b) {
    int cx = (bx - X0) / BPP, cy = (bz - Z0) / BPP;
    for (int dy = -rad - 1; dy <= rad + 1; dy++)
        for (int dx = -rad - 1; dx <= rad + 1; dx++) {
            int borde = abs(dx) == rad + 1 || abs(dy) == rad + 1;
            px(cx + dx, cy + dy, borde ? 0 : r, borde ? 0 : g, borde ? 0 : b);
        }
}

int main(int argc, char **argv) {
    if (argc != 8) { fprintf(stderr, "uso: mapa semilla version lado bpp overworld|nether cuadricula salida\n"); return 2; }
    uint64_t seed = parseSeed(argv[1]);
    int mc = str2mc(argv[2]);
    int lado = atoi(argv[3]); BPP = atoi(argv[4]);
    int nether = strcmp(argv[5], "nether") == 0;
    int grid = atoi(argv[6]);
    if (mc < 0 || mc < MC_1_18) { fprintf(stderr, "version no soportada: %s (usa 1.18 o superior, ej. 1.21)\n", argv[2]); return 2; }
    if (lado < 64 || (BPP != 1 && BPP != 2 && BPP != 4)) { fprintf(stderr, "lado >= 64 y bpp 1, 2 o 4\n"); return 2; }
    lado -= lado % 4;
    X0 = Z0 = -lado / 2;

    Generator g;
    setupGenerator(&g, mc, 0);
    applySeed(&g, nether ? DIM_NETHER : DIM_OVERWORLD, seed);

    // Biomas a escala 1:4 (resolución nativa del ruido) y ampliados a la escala pedida
    int n = lado / 4;
    Range r = { 4, X0 / 4, Z0 / 4, n, n, nether ? 16 : 15, 1 }; // y≈63 (nivel del mar) a escala 4
    int *ids = allocCache(&g, r);
    if (!ids || genBiomes(&g, ids, r)) { fprintf(stderr, "fallo al generar biomas\n"); return 1; }
    unsigned char colores[256][3];
    initBiomeColors(colores);
    W = H = lado / BPP;
    img = malloc((size_t)W * H * 3);
    biomesToImage(img, colores, ids, n, n, 4 / BPP, 1); // flip=1: fila 0 = norte (con 0 la imagen sale espejada N-S)

    // Máscara de agua cada 64 bloques para trazar caminos: 0 tierra, 1 río, 2 océano
    char ruta_agua[4096];
    snprintf(ruta_agua, sizeof ruta_agua, "%s.agua", argv[7]);
    FILE *agua = fopen(ruta_agua, "w");
    if (!agua) { perror(ruta_agua); return 1; }
    for (int j = 0; j < n; j += 16) {
        for (int i = 0; i < n; i += 16) {
            int id = ids[(size_t)j * n + i];
            fputc(isOceanic(id) ? '2' : (id == river || id == frozen_river) ? '1' : '0', agua);
        }
        fputc('\n', agua);
    }
    fclose(agua);
    // Biomas presentes con su color (para la leyenda): id,nombre,r,g,b,celdas
    {
        long cuenta[256] = {0};
        for (size_t k = 0; k < (size_t)n * n; k++) if (ids[k] >= 0 && ids[k] < 256) cuenta[ids[k]]++;
        char ruta_b[4096];
        snprintf(ruta_b, sizeof ruta_b, "%s.biomas", argv[7]);
        FILE *fb = fopen(ruta_b, "w");
        if (!fb) { perror(ruta_b); return 1; }
        for (int b = 0; b < 256; b++)
            if (cuenta[b]) fprintf(fb, "%d,%s,%d,%d,%d,%ld\n", b, biome2str(mc, b), colores[b][0], colores[b][1], colores[b][2], cuenta[b]);
        fclose(fb);
    }
    free(ids);

    // Cuadrícula de viaje (oscurece) y ejes 0,0 (rojo)
    for (int y = 0; y < H; y++)
        for (int x = 0; x < W; x++) {
            int bx = X0 + x * BPP, bz = Z0 + y * BPP;
            unsigned char *p = img + 3 * ((size_t)y * W + x);
            if (bx == 0 || bz == 0 || (bx > -BPP && bx <= 0) || (bz > -BPP && bz <= 0)) { p[0] = 220; p[1] = 30; p[2] = 30; }
            else if (grid > 0 && (((bx % grid) + grid) % grid < BPP || ((bz % grid) + grid) % grid < BPP)) { p[0] /= 2; p[1] /= 2; p[2] /= 2; }
        }

    char ruta[4096];
    snprintf(ruta, sizeof ruta, "%s.csv", argv[7]);
    FILE *csv = fopen(ruta, "w");
    if (!csv) { perror(ruta); return 1; }
    fprintf(csv, "tipo,x,z\n");

    const Est over[] = {
        { Ruined_Portal, "Portal en ruinas", 150, 60, 200 }, { Igloo, "Iglú", 230, 250, 255 },
        { Swamp_Hut, "Cabaña de bruja", 60, 110, 40 }, { Desert_Pyramid, "Templo del desierto", 240, 200, 90 },
        { Jungle_Temple, "Templo de la jungla", 40, 160, 60 }, { Trail_Ruins, "Ruinas de sendero", 180, 130, 90 },
        { Outpost, "Puesto de saqueadores", 90, 90, 90 }, { Village, "Aldea", 255, 230, 0 },
        { Monument, "Monumento oceánico", 0, 200, 200 }, { Mansion, "Mansión del bosque", 140, 70, 20 },
        { Ancient_City, "Ciudad antigua", 10, 40, 60 }, { Trial_Chambers, "Cámaras de desafío", 200, 120, 40 },
    };
    const Est neth[] = { { Ruined_Portal_N, "Portal en ruinas", 150, 60, 200 }, { Fortress, "Fortaleza del Nether", 120, 20, 20 }, { Bastion, "Bastión", 30, 30, 30 } };
    const Est *lista = nether ? neth : over;
    int nl = nether ? 3 : (int)(sizeof over / sizeof *over);
    int rad = W >= 3000 ? 4 : 2;

    for (int i = 0; i < nl; i++) {
        StructureConfig sc;
        if (!getStructureConfig(lista[i].type, mc, &sc)) continue;
        int reg = sc.regionSize * 16;
        int r0 = (X0 - reg + 1) / reg, r1 = (X0 + lado) / reg; // X0 <= 0: división redondeando hacia abajo; el mapa es cuadrado y centrado
        for (int rz = r0; rz <= r1; rz++)
            for (int rx = r0; rx <= r1; rx++) {
                Pos p;
                if (!getStructurePos(lista[i].type, mc, seed, rx, rz, &p)) continue;
                if (p.x < X0 || p.z < Z0 || p.x >= X0 + lado || p.z >= Z0 + lado) continue;
                if (!isViableStructurePos(lista[i].type, &g, p.x, p.z, 0)) continue;
                fprintf(csv, "%s,%d,%d\n", lista[i].name, p.x, p.z);
                marca(p.x, p.z, rad, lista[i].r, lista[i].g, lista[i].b);
            }
    }

    if (!nether) {
        StrongholdIter sh;
        initFirstStronghold(&sh, mc, seed);
        for (int i = 0; i < 128; i++) { // 128 fortalezas en total; nextStronghold devuelve cuántas quedan
            int quedan = nextStronghold(&sh, &g);
            Pos p = sh.pos;
            if (p.x >= X0 && p.z >= Z0 && p.x < X0 + lado && p.z < Z0 + lado) {
                fprintf(csv, "Fortaleza del End,%d,%d\n", p.x, p.z);
                marca(p.x, p.z, rad + 2, 230, 0, 230);
            }
            if (quedan <= 0) break;
        }
        Pos s = estimateSpawn(&g, NULL);
        fprintf(csv, "Punto de aparición,%d,%d\n", s.x, s.z);
        marca(s.x, s.z, rad + 1, 255, 255, 255);
    }
    fclose(csv);

    snprintf(ruta, sizeof ruta, "%s.ppm", argv[7]);
    if (savePPM(ruta, img, W, H)) { fprintf(stderr, "no se pudo escribir %s\n", ruta); return 1; }
    printf("ok %dx%d px, %d bloques de lado\n", W, H, lado);
    return 0;
}
