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

**Coste en tramos:** viajar a otra zona, una sesión de minado, talar/recolectar, construir un módulo del refugio, fundir en el horno: **1 tramo** cada uno.

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
- **Explosión.** Radio 3 m: TS DES CD 12, 3d8 contundente (mitad si supera). Destruye bloques no reforzados del refugio en el área. El creeper muere.
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
