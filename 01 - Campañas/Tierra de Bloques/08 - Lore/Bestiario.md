---
tipo: lore
campaña: "Tierra de Bloques"
tags:
  - dnd/lore
  - dnd/reglas-caseras
---

# 🧟 Bestiario rápido (stats de 5e)

↩ [[Reglas de Supervivencia]]

Cada mob tiene su nota con statblock del plugin en [[#📚 Statblocks|Mobs/]]. En un encuentro se usan con:

```statblock
monster: Zombi
```

## 📚 Statblocks

| VD | Mob | Dónde aparece |
|---|---|---|
| 0 | [[Slime Pequeño]] | Restos de un slime |
| 1/4 | [[Zombi]] · [[Esqueleto]] · [[Araña]] · [[Ahogado]] | Superficie de noche, cuevas, ríos |
| 1/4 | [[Zombi Momificado]] · [[Araña de Cueva]] · [[Slime Mediano]] | Desierto · minas · pantanos ⚔️ |
| 1/2 | [[Creeper Joven]] · [[Saqueador]] | Hierba y bosques · patrullas, aldeas |
| 1/2 | [[Esqueleto Empantanado]] · [[Esqueleto Glacial]] · [[Enjambre de Lepismas]] | Pantano · tundra · fortaleza del End ⚔️ |
| 1 | [[Creeper]] · [[Piglin Zombificado]] · [[Slime Grande]] | Superficie (nivel 3+) · Nether · pantanos ⚔️ |
| 2 | [[Brisa]] | Solo en cámaras de desafío ⚔️ |
| 3 | [[Capitán de Saqueadores]] · [[Esqueleto Wither]] | Incursiones · fortaleza del Nether |
| 5 | [[Devastador]] · [[Blaze]] | Incursiones · fortaleza del Nether |
| 7 | [[Enderman]] | Cualquier lugar de noche, el End |
| 9 | [[Ghast]] | Nether |
| 16 | [[Wither]] | Jefe invocado |
| 20 | [[Warden]] | Oscuridad Profunda |
| 26 | [[Dragón del End]] | Jefe final |

⚔️ = sale de los generadores de las [[#⚔️ Cámaras de desafío|cámaras de desafío]] (mobs caseros, no están en el PDF).

Las brujas usan los statblocks de las hags del SRD (ver abajo).

---

## Brujas

Las brujas son **arpías (hags) de 5e** que pelean con pociones. Son astutas, cobardes y hacen tratos. Nunca luchan limpio.
*Origen:* un aldeano alcanzado por un rayo se convierte en bruja. Las aldeas temen las tormentas.

### Reglas comunes a todas las brujas

Se usa el bloque de estadísticas de la arpía correspondiente, con estos cambios:

- **Pociones arrojadizas** *(sustituye a las Garras como ataque principal)*. Acción. Alcance 9 m, nube de 1,5 m de radio, TS **DES** CD de la bruja. Tira 1d6:

| d6 | Poción | Efecto si falla la TS (mitad o nada si la supera) |
|---|---|---|
| 1–2 | Daño | 3d6 necrótico (mitad) |
| 3 | Veneno | 2d6 veneno y *envenenado* 1 min (TS CON al final de cada turno) |
| 4 | Lentitud | Velocidad a la mitad y sin reacciones durante 1 min (TS CON al final de cada turno) |
| 5 | Debilidad | Desventaja en ataques y pruebas de FUE durante 1 min |
| 6 | Hambre | −2 de [[Hambre]] y la criatura tiene que comer en su próximo turno o queda *aturdida* hasta el final de ese turno |

- **Beber** *(reacción, 3/día)*. Cuando recibe daño, bebe una poción:
  - *Curación:* recupera 2d4+2 PG.
  - *Resistencia al fuego:* resistencia al fuego durante 1 min.
  - *Invisibilidad:* invisible hasta el final de su siguiente turno.
  - *Respiración acuática:* respira bajo el agua.
- **Trato de bruja.** Ninguna bruja ataca si puede negociar. Vende pociones (ver [[Recetas de Crafteo#🧪 Pociones]]) pero no cobra esmeraldas. Pide a cambio un recuerdo, un año de vida, el nombre verdadero, el punto de reaparición de alguien… Cumple el trato al pie de la letra, nunca en su espíritu.
- **Botín:** 1d4 de cada uno: botellas, redstone, piedra luminosa, azúcar, pólvora, ojo de araña. Además, 1 poción intacta (tira en la tabla de arriba o en la de beber).

---

### 🌿 Bruja del pantano
**Usa:** *Green Hag* (VD 3). Vive en una cabaña sobre pilotes en un pantano, a menudo con un gato negro.
Conserva **Anfibia**, **Imitación**, **Apariencia ilusoria** (se hace pasar por una aldeana) y **Paso invisible**.
- **Lanzamiento de conjuros innato:** cambia *luces danzantes* por *enredar* (raíces del pantano).
- **Gancho:** se esconde en una aldea con su Apariencia ilusoria y envenena el pozo. Los aldeanos enferman y suben los precios.

### 🌙 Bruja de la noche
**Usa:** *Night Hag* (VD 5). Es la bruja que persigue a los **viajeros que duermen al raso**.
Conserva **Resistencias**, **Etereidad** y **Piedra corazón**.
- **Embrujar pesadillas** *(adaptado al [[Juego Nómada#Campamento|campamento]])*: solo puede actuar sobre PJ que duerman **sin cama** o fuera de un campamento iluminado. Esa noche, el PJ no recupera el descanso largo y su máximo de PG baja 5 (1d10 en 5e) hasta que la bruja muera.
- **Invocar phantoms:** cuando un PJ lleva **3 noches sin dormir en cama**, la bruja envía 1d4 phantoms (*Stirge* con vuelo 15 m y Sensibilidad a la luz solar).
- **Botín extra:** su **Piedra corazón** (una gema que late) vale 50 E y es componente para encantar *Reparación* sin coste de XE, una sola vez.
- **Gancho:** si los PJ abusan del descanso al raso, aparece. Con ella, la mecánica del campamento importa.

### 🌊 Bruja del mar
**Usa:** *Sea Hag* (VD 2). Habita ruinas oceánicas y monumentos, rodeada de **ahogados** que le obedecen.
Conserva **Anfibia**, **Aspecto horrible**, **Mirada mortal** e **Imitación**.
- **Pociones arrojadizas** bajo el agua: alcance 4,5 m. Solo la nube de Daño y la de Lentitud funcionan.
- **Gancho:** custodia un **corazón del mar** y ofrece tratos a cambio de respiración acuática.

---

### 🕯️ Aquelarre

Cuando **3 brujas** están a 9 m entre sí, forman un aquelarre (*Hag Coven*, del Manual de Monstruos):
- Comparten los conjuros del aquelarre: *identificar, rayo de enfermedad, inmovilizar persona, localizar objeto, imponer maldición, contraconjuro, relámpago, asesino fantasmal, polimorfar, contactar otro plano, escudriñar, mordedura ocular*.
- **Caldero del aquelarre** *(sustituye al Ojo de arpía)*: las 3 brujas ven todo lo que se refleja en el caldero y pueden lanzar *escudriñar* a través de él. Si se rompe (CA 15, 20 PG), cada bruja recibe 3d10 psíquico.
- **Pociones de aquelarre:** cada bruja puede lanzar 2 pociones por acción en lugar de 1.
- **Ritual de tormenta** *(1/semana)*: invocan una tormenta sobre una aldea. Cada aldeano al aire libre tiene 1 entre 20 de que le alcance un rayo **y se convierta en bruja**. Así crece el aquelarre.
- **Gancho de era:** un aquelarre completo es un jefe adecuado para la era del Hierro o del Diamante (ver [[Progresión por Eras]]).

---

## ⚔️ Cámaras de desafío

Complejos subterráneos de cobre y toba (marcados con 🔑 en el [[Mapa del Mundo]]). Cada sala tiene un **generador de desafío** que suelta oleadas de mobs cuando alguien se acerca. Botín en [[Botín por Lugar#⚔️ Cámaras de desafío]]. **Nivel recomendado: 3+.** A nivel 1–2 usa una sola oleada por generador.

### Reglas del generador
- **Se activa** cuando un PJ entra a 9 m o menos (está detectando jugadores: el número de PJ cercanos decide el tamaño de la oleada).
- **Oleadas:** 2 por generador. La segunda sale al inicio de la ronda siguiente a que caiga el último mob, o en la ronda 4 si aún quedan.
- **No se puede romper** (es de bloque irrompible). Solo se apaga ganando.
- **Al vencerlo:** suelta 1 **llave de desafío** por PJ que luchó (cada llave abre 1 bóveda) y queda apagado **1 hora** del [[Ciclo Día y Noche|reloj]].
- **Ominoso:** si un PJ lleva el efecto *Mal presagio* (de beber una botella ominosa o matar a un [[Capitán de Saqueadores]]), los generadores se vuelven ominosos: sus mobs tienen **+2 CA y +1d4 de daño**, cada ronda pasa algo de la tabla de *objetos ominosos*, y sueltan **llaves ominosas**.

### Qué sale de cada generador (d8)
Mobs **por oleada** según el número de PJ.

| d8 | Generador | 4 PJ | 5 PJ | 6 PJ |
|---|---|---|---|---|
| 1 | 🧟 Zombis | 4 [[Zombi]] | 3 [[Zombi]] + 2 [[Zombi Momificado]] | 3 [[Zombi]] + 3 [[Zombi Momificado]] |
| 2 | 💀 Esqueletos | 2 [[Esqueleto]] + 1 [[Esqueleto Glacial]] | 2 [[Esqueleto]] + 2 [[Esqueleto Glacial]] | 3 [[Esqueleto]] + 2 [[Esqueleto Glacial]] |
| 3 | 🍄 Empantanados | 2 [[Esqueleto Empantanado]] | 3 [[Esqueleto Empantanado]] | 3 [[Esqueleto Empantanado]] + 1 [[Esqueleto]] |
| 4 | 🕷️ Arañas | 4 [[Araña de Cueva]] | 5 [[Araña de Cueva]] | 6 [[Araña de Cueva]] |
| 5 | 🟩 Slimes | 1 [[Slime Grande]] + 1 [[Slime Mediano]] | 2 [[Slime Grande]] | 2 [[Slime Grande]] + 1 [[Slime Mediano]] |
| 6 | 🐛 Lepismas | 2 [[Enjambre de Lepismas]] | 2 [[Enjambre de Lepismas]] + 1 [[Araña de Cueva]] | 3 [[Enjambre de Lepismas]] |
| 7 | 🌪️ Brisa | 1 [[Brisa]] | 1 [[Brisa]] + 2 [[Zombi]] | 2 [[Brisa]] |
| 8 | 🎲 Mixto | 2 [[Zombi]] + 1 [[Esqueleto Glacial]] + 1 [[Araña de Cueva]] | + 1 [[Zombi Momificado]] | + 1 [[Esqueleto Empantanado]] |

*Dificultad:* cada oleada es **Baja–Moderada** a nivel 3 y la pareja de oleadas cuenta como **Alta**. Usa el bloque de dificultad del generador de encuentros si cambias la mezcla.

### Salas y eventos (d8)
Tira al entrar en cada sala para saber qué más hay además del generador.

| d8 | Sala | Qué pasa |
|---|---|---|
| 1 | 🌀 Sala de las cargas | Dispensadores disparan cargas de viento: el primer PJ que cruza hace TS de FUE CD 12 o sale empujado 3 m (a un foso de 1d6 si lo hay) |
| 2 | 🏺 Vasijas decoradas | 2d4 vasijas: romper una es una acción; tira 1d10: 1–6 nada, 7–8 1d4 esmeraldas, 9 1d4 flechas con efecto, 10 sale una [[Araña de Cueva]] o un [[Enjambre de Lepismas]] |
| 3 | 💡 Bombillas de cobre | Las luces parpadean con palancas: si alguien toca la equivocada, oscuridad total 1d4 rondas durante el combate |
| 4 | 🧱 Pasillo de toba | Laberinto: Supervivencia CD 13 para no perder 1 hora (−1 de [[Hambre]]) |
| 5 | 🔒 Bóveda visible | Una bóveda cerrada detrás de rejas: hay que vencer el generador de esta sala para alcanzarla |
| 6 | 🛏️ Sala de descanso | Camas y un cofre con 1d4 pan: se puede hacer un **descanso corto seguro** |
| 7 | 🌪️ Patio central | Sala grande de dos alturas con **2 generadores** a la vez (tira dos veces en la tabla de arriba) |
| 8 | 🗝️ Bóveda ominosa | Solo se abre con una llave ominosa. Si no la tienen: una **botella ominosa** en un pedestal (beberla da *Mal presagio*) |

### Objetos ominosos (d6, cada ronda en salas ominosas)
| d6 | Cae del techo junto a un PJ al azar |
|---|---|
| 1–2 | Lluvia de **flechas envenenadas**: TS de DES CD 13 o 2d4 perforante + envenenado 1 ronda |
| 3 | **Poción de lentitud** que se rompe: TS de CON CD 13 o ralentizado 1 ronda |
| 4 | **Telaraña**: el PJ queda apresado (FUE CD 12 para soltarse) |
| 5 | **Carga de viento**: TS de FUE CD 13 o empujado 3 m y derribado |
| 6 | Un **mob extra** del generador de la sala aparece junto al PJ |

### Fuera de las cámaras
Estos mobs también sirven como encuentros de viaje:
- [[Zombi Momificado]]: noches en el desierto (en lugar de zombis).
- [[Esqueleto Glacial]]: noches en la tundra y picos helados.
- [[Esqueleto Empantanado]] y [[Slime Grande]]: pantanos y manglares (slimes en luna llena).
- [[Araña de Cueva]]: minas abandonadas, en grupos de 1d4+2.
- [[Enjambre de Lepismas]]: fortalezas del End y montañas (picar piedra infestada).
- [[Brisa]]: solo en las cámaras de desafío.
