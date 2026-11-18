"""Pilares de obsidiana del End para una semilla (mismo algoritmo que SpikeFeature de Minecraft Java 1.9+)."""
import math

MASK = (1 << 48) - 1


class JavaRandom:
    def __init__(self, seed):
        self.seed = (seed ^ 0x5DEECE66D) & MASK

    def next(self, bits):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & MASK
        r = self.seed >> (48 - bits)
        return r - (1 << 32) if r >= 1 << 31 else r  # (int) de Java: solo next(32) puede salir negativo

    def next_long(self):
        return ((self.next(32) << 32) + self.next(32) + (1 << 63)) % (1 << 64) - (1 << 63)

    def next_int(self, bound):
        r = self.next(31)
        m = bound - 1
        if bound & m == 0:
            return (bound * r) >> 31
        u = r
        while True:
            r = u % bound
            if u - r + m < 1 << 31:
                return r
            u = self.next(31)


def pilares(semilla):
    """[(x, z, radio, altura_y, enjaulado)] para los 10 pilares."""
    clave = JavaRandom(semilla).next_long() & 0xFFFF
    orden = list(range(10))
    rnd = JavaRandom(clave)
    for j in range(10, 1, -1):  # Util.shuffle
        k = rnd.next_int(j)
        orden[j - 1], orden[k] = orden[k], orden[j - 1]
    out = []
    for i in range(10):
        ang = 2.0 * (-math.pi + math.pi / 10 * i)
        k = orden[i]
        out.append((math.floor(42 * math.cos(ang)), math.floor(42 * math.sin(ang)), 2 + k // 3, 76 + k * 3, k in (1, 2)))
    return out


if __name__ == "__main__":
    # Autocomprobación del generador Java: new Random(0).nextInt(10) == 0 y nextLong() conocido
    assert JavaRandom(0).next_long() == -4962768465676381896
    assert JavaRandom(42).next_int(10) == 0
    for p in pilares(-4697940382757111526):
        print(p)
