---
tipo: mapa
campaña: "Tierra de Bloques"
tags:
  - dnd/mapa
  - dnd/battlemap
---

# ⚔️ Battlemaps

Mapas de combate para el VTT. Están en `10 - images/Battlemaps/`.
- **Escala:** 1 casilla = 1 bloque = 1,5 m. El norte está arriba.
- **Tamaño en el VTT:** cada casilla mide 64 px (48 px en la arena completa del End). Pon ese tamaño de cuadrícula al importar.
- **Muros:** las casillas con relieve son muros, columnas o bloques sólidos. Las planas se pueden pisar.
- Botín y guardianes de cada lugar en [[Botín por Lugar]]; mobs en el [[Bestiario]].

> [!note] De dónde salen
> - **La arena del End es la de tu semilla:** la forma de la isla está calculada con cubiomes, y los pilares con el mismo algoritmo del juego (posición, grosor, altura y jaulas).
> - **Las estructuras son reconstrucciones aproximadas** de su distribución en el juego, no copias bloque a bloque.
> - Para regenerarlos: `python3 .tools/battlemaps/battlemaps.py`.

---

## 🐉 End: arena del Dragón (nivel 20)

![[End - Arena del Dragón.png]]

Ocupa 121×121 casillas, de −60 a +60 alrededor del portal de salida. El vacío (negro) es caída mortal: quien cae, muere (ver [[Muerte y Reaparición]]).

### Pilares de obsidiana

| Pilar | Posición (X, Z) | Ancho | Altura sobre el suelo | Cristal |
|---|---|---|---|---|
| 1 | 42, 0 | 5 casillas | 19 bloques (28,5 m) | 🔒 **enjaulado** |
| 2 | 33, 24 | 9 | 42 (63 m) | ✨ |
| 3 | 12, 39 | 9 | 34 (51 m) | ✨ |
| 4 | −13, 39 | 5 | 16 (24 m) | ✨ |
| 5 | −34, 24 | 9 | 35 (52,5 m) | ✨ |
| 6 | −42, −1 | 11 | 46 (69 m) | ✨ (el más alto) |
| 7 | −34, −25 | 7 | 26 (39 m) | ✨ |
| 8 | −13, −40 | 7 | 27 (40,5 m) | ✨ |
| 9 | 12, −40 | 7 | 30 (45 m) | ✨ |
| 10 | 33, −25 | 5 | 22 (33 m) | 🔒 **enjaulado** |

> [!warning] Cristales del End (regla casera, no está en el statblock del [[Dragón del End]])
> - **Curación:** al inicio de su turno, el dragón recupera **5 PG por cada cristal intacto** (hasta 50 por turno). Romperlos es el primer objetivo.
> - **Romper un cristal:** CA 10. Cualquier impacto lo destruye. Explota: cada criatura a 3 m hace una TS de DES CD 15 y recibe 22 (4d10) de fuego, o la mitad si la supera.
> - **Jaulas (pilares 1 y 10):** barrotes con CA 15 y 20 PG. Las flechas no pasan. Hay que subir y romperlos, o atacar desde dentro.
> - **Subir:** la obsidiana no tiene agarres, así que trepar es Atletismo CD 25. Lo práctico es subir **poniendo bloques bajo los pies**: 1 bloque (1,5 m) por acción. También se puede volar o usar perlas de ender.
> - **Pilares 2, 5 y 6:** su cristal queda a más de 50 m. Desde el suelo hay que disparar con desventaja por la distancia larga.

### Centro y portal (fase de perchado)

![[End - Centro y portal.png]]

Ocupa 45×45 casillas alrededor del portal. Úsalo cuando el dragón se posa en el pilar central para cargar su aliento.
- **Pilar central (roca madre):** el dragón se posa encima.
- **Pozo del portal:** caer dentro no hace nada hasta que el dragón muere. Después, lleva de vuelta al mundo.

---

## 🧙 Cabaña de bruja

![[Cabaña de bruja.png|500]]

La cabaña está sobre pilotes encima del pantano. El agua es **terreno difícil**, y caer del porche son 3 m. Dentro hay un **caldero** (pociones de la bruja), una mesa de crafteo y una maceta. Reglas de la bruja en [[Bestiario#Brujas]].

---

## 🧊 Iglú

| Superficie | Sótano |
|---|---|
| ![[Iglú - Superficie.png\|350]] | ![[Iglú - Sótano.png\|300]] |

- **Superficie:** cama, horno y mesa de crafteo. Bajo la alfombra del centro hay una **trampilla** (Investigación CD 12) que baja por una escalera de mano.
- **Sótano:** soporte de pociones, cofre y caldero. Detrás de los barrotes hay un **aldeano** y un **aldeano zombi** encerrados (ver [[Botín por Lugar#🧊 Iglú]]).

---

## 🗿 Templo del desierto

| Planta | Cámara del tesoro |
|---|---|
| ![[Templo del desierto - Planta.png\|450]] | ![[Templo del desierto - Cámara del tesoro.png\|350]] |

- **Planta:** dos torres en la fachada (norte) con escaleras al tejado. En el centro hay un dibujo de terracota naranja con una **baldosa azul**: debajo de ella hay un pozo de 12 m hasta la cámara (daño por caída: 4d6).
- **Cámara del tesoro:** 4 cofres metidos en las paredes. La **placa de presión** del centro activa las **9 TNT** que hay debajo (8d6, TS de DES CD 15 para la mitad). Hay que picarla sin pisarla.

---

## 🚩 Puesto de saqueadores

| Planta baja y alrededores | Azotea |
|---|---|
| ![[Puesto de saqueadores - Planta baja.png\|450]] | ![[Puesto de saqueadores - Azotea.png\|350]] |

- **Planta baja y alrededores:** la torre de roble oscuro tiene la puerta al sur y una escalera de mano en la esquina noreste. Fuera hay **tiendas**, una pila de troncos y una **jaula con un gólem de hierro** prisionero.
- **Azotea:** las almenas dan **cobertura media** a los ballesteros. Allí está el **cofre** del puesto. El [[Capitán de Saqueadores]] suele esperar arriba.

---

## 🌿 Templo de la jungla

| Planta | Sótano |
|---|---|
| ![[Templo de la jungla - Planta.png\|400]] | ![[Templo de la jungla - Sótano.png\|350]] |

- **Planta:** la maleza alrededor es terreno difícil. La sala interior tiene la escalera al sótano.
- **Sótano:**
  - **Pasillo oeste:** tiene **cables trampa** (Percepción CD 14) conectados a **dispensadores de flechas**, a +5 para impactar y 1d6 perforante cada uno.
  - **Puzle:** las **3 palancas** de la pared norte abren la cámara de los cofres.

---

## ⚔️ Cámaras de desafío: sala tipo

![[Cámaras de desafío - Sala.png|500]]

Sala de 19×19 con:
- el **generador** en el centro;
- 4 columnas que dan cobertura;
- **vasijas** junto a las paredes;
- una **bóveda** en la esquina noreste;
- una **plataforma de cobre** al sur (terreno elevado);
- dos dispensadores de cargas de viento.

Reutilízala para cada sala, tirando en las tablas de [[Bestiario#⚔️ Cámaras de desafío]].

---

## 🔑 Leyenda de iconos

| Icono | Qué es | Icono | Qué es |
|---|---|---|---|
| Caja marrón con cierre | Cofre | Jaula oscura con fuego | Generador |
| Círculo gris con líquido morado | Caldero | Rojo con almohada | Cama |
| Cuadrícula de madera | Mesa de crafteo | Gris con boca encendida | Horno |
| Rojo con franja blanca | TNT | Cuadrado gris pequeño | Placa de presión |
| Palo con punta roja | Palanca | Gris con agujero negro | Dispensador |
| Llama pequeña | Antorcha | Rombo rosa | Cristal del End (con rejilla: enjaulado) |
| Círculo de barro | Vasija o maceta | Negro con anillo dorado | Bóveda |
| Escalera de mano | Escalera o trampilla | Línea blanca | Cable trampa |
| Caras (marrón, verde, gris) | Aldeano, aldeano zombi, gólem de hierro | Barrotes | Rejas de hierro (bloquean, pero dejan ver) |
