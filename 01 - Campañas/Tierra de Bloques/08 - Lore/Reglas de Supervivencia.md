---
tipo: lore
campaña: "Tierra de Bloques"
tags:
  - dnd/lore
  - dnd/reglas-caseras
---

# ⛏️ Reglas de supervivencia (D&D 5e + Minecraft)

Reglas caseras que se suman a las de 5e. Si hay conflicto, mandan estas.
Recetas y equipo: [[Recetas de Crafteo]].

---

## ☀️ Ciclo día/noche

Cada día tiene **4 tramos** (~4 h de juego cada uno):

| Tramo | Qué pasa |
|---|---|
| 🌅 Amanecer | Los no-muertos expuestos al sol arden (1d6 fuego/turno). |
| ☀️ Día | Seguro en el exterior salvo cuevas y zonas oscuras. |
| 🌇 Atardecer | Tirada de aparición con **desventaja** para el DM (menos monstruos). |
| 🌙 Noche | Tirada de aparición en cada tramo/hora fuera de zonas iluminadas. |

**Coste en tramos:** viajar a otra zona, una sesión de minado, talar/recolectar, levantar un muro de campamento, fundir en el horno: **1 tramo** cada uno.

**Tirada de aparición:** d20. Si sale ≤ **Amenaza** (empieza en 5, +2 por cada noche sin dormir en cama, +5 en cuevas profundas) → encuentro.

**Luz = seguridad:** una antorcha crea un radio de 6 m (4 casillas) donde no aparecen monstruos. Los monstruos pueden *entrar*, pero no *nacer* ahí.

**Dormir en cama:** solo de noche y sin hostiles a 9 m. Salta la noche, cuenta como descanso largo y **fija el punto de reaparición**.

---

## 🍖 Hambre

Cada PJ tiene **Hambre 0–10** (campo `hambre` en el frontmatter de su nota; empieza en 10).

- **−1** por cada tramo de actividad (viajar, minar, construir, combate).
- **−1 extra** al final de un combate en el que hayas corrido (Correr) o lanzado un conjuro de nivel 1+.

| Hambre | Efecto |
|---|---|
| 8–10 **Saciado** | Al final de un descanso corto recuperas PG = tu bonificador de competencia, gratis. |
| 4–7 **Normal** | Sin efectos. |
| 1–3 **Hambriento** | No puedes usar Dados de Golpe en descansos cortos. Desventaja en pruebas de Constitución. |
| 0 **Inanición** | +1 nivel de agotamiento por cada tramo. El descanso largo no lo quita hasta comer. |

**Comer** es una acción adicional (fuera de combate, gratis):

| Comida | Hambre | Notas |
|---|---|---|
| Manzana / zanahoria / baya | +2 | |
| Carne cruda / pescado crudo | +1 | TS CON CD 10 o *envenenado* 1 tramo |
| Pan | +3 | 3 trigo |
| Carne o pescado cocinado | +4 | Horno o fogata |
| Estofado (setas / conejo) | +6 | Cuenco + ingredientes |
| Carne podrida | +1 | TS CON CD 13 o *envenenado* y −2 hambre extra |
| Manzana dorada | +4 | + 2d4 PG temporales y ventaja en TS de veneno 1 h |

---

## ⛏️ Recolección

Una sesión de recolección cuesta **1 tramo**. El PJ elige qué busca y tira:

- **Talar / cosechar:** Supervivencia (SAB) o Atletismo (FUE).
- **Minar:** Atletismo (FUE). Ventaja con un pico de un nivel superior al necesario.
- **Cazar / pescar:** Supervivencia (SAB).

| Resultado vs CD | Rendimiento |
|---|---|
| Falla por 5+ | Nada, y tirada de aparición (te has hecho ruido / te has perdido) |
| Falla | 1 unidad |
| Supera | 1d4 + 1 unidades |
| Supera por 5+ / 20 natural | 2d4 + 2 unidades, o un hallazgo especial |

**CD y herramienta mínima:**

| Material | CD | Necesita | Dónde |
|---|---|---|---|
| Madera, tierra, arena, comida | 8 | Manos | Superficie |
| Piedra, carbón | 10 | Pico de madera | Superficie / cuevas |
| Hierro, cobre | 13 | Pico de piedra | Cuevas |
| Oro, redstone, lapislázuli | 15 | Pico de hierro | Cuevas profundas |
| Diamante | 18 | Pico de hierro | Cuevas profundas |
| Obsidiana | 15 | Pico de diamante | Junto a lava |
| Restos ancestrales | 20 | Pico de diamante | El Nether |

Sin la herramienta mínima: no se puede extraer.

---

## 🔨 Durabilidad

Herramientas, armas y armaduras crafteadas tienen **Durabilidad** (ver [[Recetas de Crafteo]]).
Pierden 1 punto cuando sacas un **1 natural** usándolas (arma/herramienta) o cuando te hacen un **crítico** (armadura).
A 0 se rompen. Reparar en la mesa de crafteo con 1 unidad del material la deja al máximo.

---

## 🎒 Juego nómada

**No hay base fija.** El grupo viaja, y lo que no puede cargar lo deja atrás. La "base" es lo que lleváis encima, más unos pocos **hitos** repartidos por el mundo.

### Inventario por ranuras
**Ranuras = 8 + mod. de FUE** (mínimo 6).
- 1 ranura = 1 objeto (arma, herramienta, cama, horno…) **o** una pila de hasta 16 unidades del mismo material o comida.
- Lo equipado (armadura puesta, arma en mano, escudo) **no ocupa ranuras**.
- Si te pasas: −3 m de velocidad y desventaja en pruebas de DES. Con más de 4 ranuras de exceso no puedes moverte.

| Ampliación | Ranuras | Cómo se consigue |
|---|---|---|
| Saco | 4 materiales en 1 ranura | Crafteo |
| Burro / mula con cofre | +15 (del grupo) | Domar (Trato con animales CD 13) + cofre |
| Llama con cofre | +3d4 (del grupo). Se atan en fila: caravana | Domar + cofre. Escupe (1d4) si la atacan |
| Barco con cofre | +9, solo por agua | Barco + cofre |
| Caballo | Sin carga. Viajar cuesta **½ tramo** | Domar (CD 15) + silla de montar |
| Cofre de ender | 9 ranuras **compartidas entre todos los cofres de ender del mundo** | 8 obsidiana + ojo de ender |
| Caja de shulker | 1 ranura que contiene 9 | 2 caparazones de shulker (End) + cofre |
| Élitros | Planear: viajar cuesta ½ tramo; sin daño por caída | Solo en las naves del End |

### Campamento
Montarlo lleva 10 min y no cuesta tramo. Se recoge todo al irse. Es acumulativo:

| Montaje | Efecto en la noche |
|---|---|
| Al raso | La noche **no se salta**. Descanso largo posible, pero **2 tiradas de aparición** |
| + Antorchas o fogata | Tiradas de aparición con desventaja |
| + Cama (cada PJ la suya) | La noche se salta y se fija la reaparición |
| + Muro improvisado (16 bloques, +1 tramo) | Los monstruos tienen que romperlo: nunca os sorprenden y tenéis ventaja en iniciativa |
| + Cable trampa | Alarma: nadie se queda dormido durante un ataque |

Acampar dentro de una aldea, con su gólem y sus camas, cuenta como campamento completo.

### Hitos (sustituyen a la base)
Un **hito** es un lugar del mapa al que el grupo ha atado algo. Como máximo hay **3 hitos activos** a la vez; para fijar uno nuevo hay que abandonar uno viejo.
- **Alijo:** cofre enterrado o escondido, con capacidad ilimitada. Cada semana que pase sin vigilancia, 1 entre 6 de que lo saqueen o lo destruya un creeper.
- **Piedra imán:** las brújulas imantadas a ella siempre apuntan al hito.
- **Portal:** un extremo de la red de portales (ver abajo).
- **Cama fija:** punto de reaparición permanente, aunque durmáis en otro sitio.

### Red de portales del Nether
- Un portal cuesta 10 obsidiana + un mechero.
- **1 tramo de viaje en el Nether equivale a 8 tramos en la superficie.** Viajar entre dos portales enlazados cuesta 1 tramo en el Nether, con tirada de aparición del Nether (Amenaza +5), en lugar de días de camino.
- Es la forma de moverse rápido a mitad de campaña, y una de las metas de la era del Nether.

### Progresión de la caravana
| Era | Qué desbloquea el grupo |
|---|---|
| 🪵 Madera y piedra | Sacos, camas, antorchas, campamento con muro |
| ⛓️ Hierro | Burros y mulas, brújula, linterna, mapas, cable trampa |
| 💎 Diamante | Mesa de encantar portátil, caballos, caravana de llamas |
| 🔥 Nether | Red de portales, brújula imantada, soporte de pociones |
| 🌌 El End | Cofre de ender, cajas de shulker, élitros |

---

## 💀 Muerte y reaparición *(opcional, recomendada)*

Al morir (3 fallos en TS de muerte) el PJ **reaparece** en su última cama al siguiente amanecer con:
- PG completos, Hambre 6, **1 nivel de agotamiento** que solo quita un descanso largo.
- **Todo su inventario** queda en el lugar de la muerte. Desaparece si nadie lo recoge en **3 tramos**.

Sin cama fijada → muerte normal de 5e.

---

## 🧟 Bestiario rápido (stats de 5e)

| Mob | Usa | Ajuste |
|---|---|---|
| Zombi | *Zombie* | Arde al sol |
| Esqueleto | *Skeleton* | Arde al sol |
| Araña | *Giant Wolf Spider* | Neutral de día |
| Ahogado | *Zombie* | Nada 9 m, a veces tridente (1d8+1, alcance 6/18 m) |
| Bruja | *Cult Fanatic* | Lanza pociones en vez de conjuros |
| Enderman | *Displacer Beast* sin desplazamiento | Teletransporte 9 m como reacción; hostil si le miras a los ojos (TS SAB CD 12 al verlo) |
| Creeper | Ver abajo | |

### Creeper
*Monstruosidad Mediana*, CA 12, PG 13 (3d8), Vel 9 m
FUE 8 · DES 14 · CON 12 · INT 3 · SAB 10 · CAR 3. Sigilo +4. VD 1/2.
- **Siseo.** Si empieza su turno a 1,5 m de una criatura, sisea (todos lo oyen). Al inicio de su siguiente turno, si sigue ahí, **explota**.
- **Explosión.** Radio 3 m: TS DES CD 12, 3d8 contundente (mitad si supera). Destruye muros improvisados y objetos colocados (fogata, mesa, cama) en el área. El creeper muere.
- **Recular.** Si recibe daño mientras sisea, el siseo se cancela.

---

## 🗺️ Progresión por eras

| Era | Niveles | Objetivo | Amenaza clave |
|---|---|---|---|
| 🪵 Madera y piedra | 1–2 | Refugio, cama, comida estable | La primera noche |
| ⛓️ Hierro | 3–5 | Armadura de hierro, horno, granjas | Cuevas, aldea asediada |
| 💎 Diamante | 6–8 | Mesa de encantamientos, portal | Cuevas profundas, mina abandonada |
| 🔥 Nether | 9–12 | Varas de blaze, perlas de ender | Fortaleza del Nether |
| 🌌 El End | 13+ | Encontrar y activar el portal final | El dragón |
