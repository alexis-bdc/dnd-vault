---
tipo: pj
campaña: Comunidad del Alba
jugador: Yo
nombre: Frater Ren
edad: 30
genero: Masculino
raza: Gnomo de los Bosques
clase: Artífice
subclase: Alquimista
nivel: 5
alineamiento: Legal Neutral
trasfondo: Ermitaño
rol_combate: Soporte Alquímico / Sanación Potenciada / Francotirador de Ballesta
estado: Activo
iniciativa: 2
ca: 17
velocidad: 25 pies
pg_max: 50
pg_actual: 50
bonif_competencia: 3
caracteristica_magica: int
fue: 12
des: 14
con: 14
int: 17
sab: 10
car: 8
salvaciones_competentes:
  - con
  - int
habilidades:
  Acrobacias: 0
  Arcanos: 1
  Atletismo: 0
  Engañar: 0
  Historia: 1
  Interpretación: 0
  Intimidar: 0
  Investigación: 0
  Juego de Manos: 0
  Medicina: 1
  Naturaleza: 0
  Percepción: 0
  Perspicacia: 0
  Persuasión: 0
  Religión: 1
  Sigilo: 0
  Supervivencia: 0
  Trato con Animales: 0
monedas:
  pc: 0
  pp: 2
  pe: 0
  po: 3833
  ppt: 0
espacios_conjuro:
  nv1_max: 4
  nv1_usados: 0
  nv2_max: 2
  nv2_usados: 0
conjuros_preparados:
  - Palabra de Curación
  - Rayo Nauseabundo
  - Esfera de Llamas
  - Flecha Ácida de Melf
  - Brebaje Caústico de Tasha
  - Curar Heridas
  - Grasa
  - Identificar
  - Calentar Metal
  - Recado
tags:
  - dnd/pj
  - dnd/comunidad-del-alba
---
# 🧪 Frater Ren

> [!statblock] **Gnomo de los Bosques — Artífice Alquimista (Nivel `VIEW[{nivel}][text]`)**
> **Alineamiento:** `VIEW[{alineamiento}][text]` | **Trasfondo:** `VIEW[{trasfondo}][text]` (Rasgo: *Descubrimiento*)
> **CA:** `INPUT[number:ca]` *(Cuero tachonado +1 y Escudo)* | **Iniciativa:** +`INPUT[number:iniciativa]` | **Velocidad:** `VIEW[{velocidad}][text]`
> **PG:** `INPUT[number:pg_actual]` / `INPUT[number:pg_max]` | **Bonif. Competencia:** +`VIEW[2 + floor(({nivel} - 1) / 4)][math]`
> **Idiomas:** Común, Gnomo

---

### 📊 Características y Modificadores Calculados

| Característica         |   Puntuación Base   |                Modificador                 |
| :--------------------- | :-----------------: | :----------------------------------------: |
| **Fuerza (FUE)**       | `INPUT[number:fue]` | **`VIEW[floor(({fue} - 10) / 2)][math]`** |
| **Destreza (DES)**     | `INPUT[number:des]` | **`VIEW[floor(({des} - 10) / 2)][math]`** |
| **Constitución (CON)** | `INPUT[number:con]` | **`VIEW[floor(({con} - 10) / 2)][math]`** |
| **Inteligencia (INT)** | `INPUT[number:int]` | **`VIEW[floor(({int} - 10) / 2)][math]`** |
| **Sabiduría (SAB)**    | `INPUT[number:sab]` | **`VIEW[floor(({sab} - 10) / 2)][math]`** |
| **Carisma (CAR)**      | `INPUT[number:car]` | **`VIEW[floor(({car} - 10) / 2)][math]`** |

---

### ✨ Estadísticas de Magia (Artífice Alquimista)

| Estadística Mágica                   | Cálculo                     |                                        Valor Actual                                        |
| :----------------------------------- | :-------------------------- | :----------------------------------------------------------------------------------------: |
| **Atributo de Conjuración**          | Inteligencia                |           `VIEW[{int}][text]` (Mod: **+`VIEW[floor(({int} - 10) / 2)][math]`**)            |
| **CD de Salvación de Conjuros**      | `8 + Competencia + Mod INT` |     **CD `VIEW[8 + (2 + floor(({nivel} - 1) / 4)) + floor(({int} - 10) / 2)][math]`**      |
| **Bonificador de Ataque de Conjuro** | `Competencia + Mod INT`     |        **+`VIEW[(2 + floor(({nivel} - 1) / 4)) + floor(({int} - 10) / 2)][math]`**         |
| **Máximo de Conjuros Preparados**    | `Nivel / 2 + Mod INT`       | **`VIEW[floor({nivel} / 2) + floor(({int} - 10) / 2)][math]`** conjuros (+4 de Alquimista) |

---

### 💰 Monedero Interactivo

```meta-bind-button
label: 💰 Gestionar Monedero (Añadir / Gastar)
icon: coins
style: primary
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/gestionar_monedero.md
```

|       🟤 Cobre (PC)        |        ⚪ Plata (PP)        |      🟢 Electro (PE)       |        🟡 Oro (PO)         |      🔘 Platino (PPT)       |
| :------------------------: | :------------------------: | :------------------------: | :------------------------: | :-------------------------: |
| `INPUT[number:monedas.pc]` | `INPUT[number:monedas.pp]` | `INPUT[number:monedas.pe]` | `INPUT[number:monedas.po]` | `INPUT[number:monedas.ppt]` |

---

### 🔮 Espacios de Conjuro Diarios

| Nivel de Espacio | Máximo | Usados | Restantes |
| :---: | :---: | :---: | :---: |
| **Nivel 1** | `INPUT[number:espacios_conjuro.nv1_max]` | `INPUT[number:espacios_conjuro.nv1_usados]` | **`VIEW[{espacios_conjuro.nv1_max} - {espacios_conjuro.nv1_usados}][math]`** |
| **Nivel 2** | `INPUT[number:espacios_conjuro.nv2_max]` | `INPUT[number:espacios_conjuro.nv2_usados]` | **`VIEW[{espacios_conjuro.nv2_max} - {espacios_conjuro.nv2_usados}][math]`** |

```meta-bind-button
label: 🌙 Descanso Largo (Restablecer PG y Espacios)
icon: bed
style: primary
actions:
  - type: updateMetadata
    bindTarget: pg_actual
    evaluate: false
    value: 50
  - type: updateMetadata
    bindTarget: espacios_conjuro.nv1_usados
    evaluate: false
    value: 0
  - type: updateMetadata
    bindTarget: espacios_conjuro.nv2_usados
    evaluate: false
    value: 0
```

---

### 🎭 Habilidades Vinculadas

| Habilidad | Atributo Base | Nivel de Competencia | Modificador Base |
| :--- | :--- | :---: | :---: |
| **Acrobacias** | Destreza | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Acrobacias"]]` | +`VIEW[floor(({des} - 10) / 2)][math]` |
| **Arcanos** | Inteligencia | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Arcanos"]]` | +`VIEW[floor(({int} - 10) / 2)][math]` |
| **Atletismo** | Fuerza | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Atletismo"]]` | +`VIEW[floor(({fue} - 10) / 2)][math]` |
| **Engañar** | Carisma | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Engañar"]]` | +`VIEW[floor(({car} - 10) / 2)][math]` |
| **Historia** | Inteligencia | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Historia"]]` | +`VIEW[floor(({int} - 10) / 2)][math]` |
| **Interpretación** | Carisma | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Interpretación"]]` | +`VIEW[floor(({car} - 10) / 2)][math]` |
| **Intimidar** | Carisma | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Intimidar"]]` | +`VIEW[floor(({car} - 10) / 2)][math]` |
| **Investigación** | Inteligencia | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Investigación"]]` | +`VIEW[floor(({int} - 10) / 2)][math]` |
| **Juego de Manos** | Destreza | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Juego de Manos"]]` | +`VIEW[floor(({des} - 10) / 2)][math]` |
| **Medicina** | Sabiduría | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Medicina"]]` | +`VIEW[floor(({sab} - 10) / 2)][math]` |
| **Naturaleza** | Inteligencia | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Naturaleza"]]` | +`VIEW[floor(({int} - 10) / 2)][math]` |
| **Percepción** | Sabiduría | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Percepción"]]` | +`VIEW[floor(({sab} - 10) / 2)][math]` |
| **Perspicacia** | Sabiduría | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Perspicacia"]]` | +`VIEW[floor(({sab} - 10) / 2)][math]` |
| **Persuasión** | Carisma | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Persuasión"]]` | +`VIEW[floor(({car} - 10) / 2)][math]` |
| **Religión** | Inteligencia | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Religión"]]` | +`VIEW[floor(({int} - 10) / 2)][math]` |
| **Sigilo** | Destreza | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Sigilo"]]` | +`VIEW[floor(({des} - 10) / 2)][math]` |
| **Supervivencia** | Sabiduría | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Supervivencia"]]` | +`VIEW[floor(({sab} - 10) / 2)][math]` |
| **Trato con Animales** | Sabiduría | `INPUT[inlineSelect(option(0, ⚪ Normal), option(1, ✅ Competente), option(2, ⭐ Pericia)):habilidades["Trato con Animales"]]` | +`VIEW[floor(({sab} - 10) / 2)][math]` |

---

### 📖 Conjuros Preparados

`INPUT[inlineList:conjuros_preparados]`

---

## ⚔️ Ataques y Armamento

| Arma / Ataque | Bonif. Ataque | Daño / Tipo | Propiedades y Notas |
| :--- | :---: | :--- | :--- |
| **Ballesta de Hermandad +1** | **+6** | **1d8 + 3** perforante | Distancia (80/320), a dos manos, mágica (+1 a tirada y daño). Ignora recarga por dote. |
| **Daga** | **+4** | **1d4 + 1** perforante | Sutil, ligera, arrojadiza (20/60). |
| [[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Ballesta de Mano|Ballesta de Mano]] | **+2** | **1d6 + 2** perforante | *(En posesión de Ethan)* Ligera, distancia (30/120). |

---

## 🎯 Dote: Experto en Ballestas (Crossbow Expert)
- **Sin desventaja en combate cuerpo a cuerpo:** Estar a 5 pies o menos de una criatura hostil no te impone desventaja en las tiradas de ataque a distancia con ballestas.
- **Ignorar Recarga:** Ignoras la propiedad *recarga* de las ballestas con las que eres competente.
- **Disparo con Acción Adicional:** Al atacar con un arma a una mano en tu turno, puedes usar tu acción adicional para disparar con una ballesta de mano que estés empuñando.

---

## 🥋 Mecánicas de Alquimia Táctica en Combate

### 🎽 La Bandolera Táctica
- **Capacidad:** **4 ranuras** (igual a tu Bonif. de Competencia +3). Aloja únicamente preparados clasificados como *(Ligeros)*.
- **Uso Rápido (Acción Adicional):** Extraer y lanzar/beber un preparado de la bandolera cuesta **1 Acción Adicional** (en lugar de una Acción).
- **Recarga:** Rellenar un espacio vacío de la bandolera durante el combate cuesta **1 Acción**.

### 💥 Catálisis Inestable
- **Efecto (Acción Adicional):** Mezclas un *Mineral Volátil (Polvo Ígneo o Cristal Cinético)* con tu foco. Tu próximo hechizo o ataque de bomba en este turno que cause daño de **Fuego, Ácido o Veneno** inflige **+1d4 de daño adicional**.
- **Riesgo:** Si sacas un **1 natural** al atacar (o el objetivo saca un **20 natural** en su TS), la mezcla estalla y sufres el daño adicional tú mismo.

---

## 🛠️ Competencias con Equipo y Herramientas

- **Armaduras y Defensas:** Armadura ligera, Armadura intermedia, Escudos.
- **Armas:** Armas sencillas, Armas de fuego.
- **Herramientas (con Pericia de Artífice - doble bono de competencia):**
  - ⚗️ **Suministros de Alquimista**
  - 🌿 **Kit de Herborista** *(por trasfondo Ermitaño)*
  - 🗝️ **Herramientas de Ladrón**
  - ⚙️ **Herramientas de Manitas (Tinker's Tools)**
  - 🔨 **Herramientas de Artesano**

---

## 🔮 Magia de Artífice & Subclase Alquimista

### 🔹 Espacios de Conjuro Diarios (Nivel 5)
- **Nivel 1:** `[ ] [ ] [ ] [ ]` (4 espacios)
- **Nivel 2:** `[ ] [ ]` (2 espacios)

---

### 🪄 Trucos (Cantrips - Uso Ilimitado)

| Truco | Escuela | Tiempo | Alcance | Comp. | Efecto / Daño (con Tratamiento Alquímico) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Descarga de Fuego** | Evocación | 1 Acción | 120 pies | V, S | Ataque a distancia (+6). **2d10 + 3 fuego** (por foco alquímico). Incinera objetos inflamables sueltos. |
| **Rociada Venenosa** | Conjuración | 1 Acción | 10 pies | V, S | TS Constitución (CD 14) o sufre **2d12 + 3 veneno** (por foco alquímico). |
| **Ilusión Menor** *(Racial)* | Ilusión | 1 Acción | 30 pies | S, M | Genera sonido o imagen de 5 pies (1 min). CD 14 Investigación para detectar. |

---

### 📜 Lista de Conjuros Preparados de Frater Ren
> [!tip] **Espacios de Conjuro:** 4 de Nivel 1 `[ ] [ ] [ ] [ ]` • 2 de Nivel 2 `[ ] [ ]`
> **Tratamiento Alquímico (Nivel 5):** Sumas tu Inteligencia (**+3**) a una tirada de curación o daño de tipo *ácido, fuego, necrótico o veneno* al canalizar mediante suministros de alquimista.

| Prep | Conjuro | Nivel | Escuela | Tiempo | Alcance | Conc / Rit | Efecto / Daño Potenciado |
| :---: | :--- | :---: | :--- | :--- | :--- | :---: | :--- |
| 🧪 | **Palabra de Curación** *(Alquimista)* | 1 | Evocación | 1 Ac. Adic. | 60 pies | No | Cura **1d4 + 6 PG** *(1d4 + 3 INT + 3 Alquimia)*. |
| 🧪 | **Rayo Nauseabundo** *(Alquimista)* | 1 | Nigromancia | 1 Acción | 60 pies | No | Ataque (+6). **2d8 + 3 veneno** + TS Con o Envenenado 1 turno. |
| 🧪 | **Esfera de Llamas** *(Alquimista)* | 2 | Conjuración | 1 Acción | 60 pies | Conc. (1 min) | Esfera 5'. TS Des o **2d6 + 3 fuego**. Mover 30' con ac. adicional. |
| 🧪 | **Flecha Ácida de Melf** *(Alquimista)* | 2 | Evocación | 1 Acción | 90 pies | No | Ataque (+6). **4d4 + 3 ácido** de inmediato y **2d4 ácido** al siguiente turno. |
| [x] | **Brebaje Caústico de Tasha** | 1 | Evocación | 1 Acción | Personal (30'x5') | Conc. (1 min) | Chorro de ácido. TS Des o empapado (**2d4 + 3 ácido** por turno). |
| [x] | **Curar Heridas** | 1 | Evocación | 1 Acción | Toque | No | Cura **1d8 + 6 PG** *(1d8 + 3 INT + 3 Alquimia)*. |
| [x] | **Grasa (Grease)** | 1 | Conjuración | 1 Acción | 60 pies | No (1 min) | Cuadrado 10' terreno difícil. TS Des o cae derribado (*Prone*). |
| [x] | **Identificar** | 1 | Adivinación | 1 Minuto | Toque | **Ritual** | Revela propiedades, uso, cargas y sintonización de objetos/criaturas. |
| [x] | **Calentar Metal** | 2 | Transmutación | 1 Acción | 60 pies | Conc. (1 min) | **2d8 + 3 fuego** a quien toque metal + TS Con o soltarlo. |
| [x] | **Recado (Sending)** | 3 | Evocación | 1 Acción | Ilimitado | No (1 asalto) | Mensaje mental de 25 palabras a criatura conocida (incluso entre planos). |

---

### ⚗️ Rasgos de Alquimista
- **Elixir Experimental:** Tras finalizar un descanso largo (o gastando espacios de conjuro), creas mágicamente 1 elixir en un frasco con efecto especial (Curación $2d4+3$ PG, Rapidez +10', Resiliencia +1 CA, Audacia +1d4 a tiradas, Vuelo 10', Transformación).
- **Experto en Alquimia / Tratamiento Alquímico (Nivel 5):** Bono pasivo de +3 a conjuros curativos y de ácido, fuego, necrótico o veneno.

---

### 📖 Detalles Mecánicos de Conjuros

<details>
<summary><b>🔍 Ver descripción completa de cada conjuro</b></summary>

- **Descarga de Fuego (*Fire Bolt*):** Realiza un ataque de conjuro a distancia (+6). Si aciertas, causa 2d10 + 3 de daño por fuego (a nivel 5). Incinera objetos inflamables que no se estén transportando.
- **Rociada Venenosa (*Poison Spray*):** Proyectas una nube de gas nocivo a 10 pies. El objetivo debe superar una TS de Constitución (CD 14) o sufrir 2d12 + 3 de daño por veneno.
- **Ilusión Menor (*Minor Illusion*):** Creas un sonido o la imagen de un objeto dentro de 30 pies durante 1 minuto. Requiere prueba de Inteligencia (Investigación) vs CD 14 para discernir.
- **Brebaje Caústico de Tasha (*Tasha's Caustic Brew*):** Chorro de ácido en línea de 30 pies x 5 pies. Criaturas deben superar TS de Destreza o quedan cubiertas de ácido sufriendo 2d4 + 3 de daño por ácido al inicio de cada turno hasta limpiarse con una acción.
- **Catapulta (*Catapult*):** Lanzas un objeto de 1 a 5 libras en línea recta hasta 90 pies. La primera criatura en la trayectoria debe superar una TS de Destreza o recibir 3d8 puntos de daño contundente.
- **Curar Heridas (*Cure Wounds*):** Tocas a una criatura para sanarle 1d8 + 6 PG (incluyendo bonos de INT y Alquimia).
- **Detectar Magia (*Detect Magic*):** Sientes y ves auras mágicas a 30 pies y determinas su escuela. Se puede lanzar como ritual sin gastar espacio.
- **Grasa (*Grease*):** Cubre un área de 10x10 pies de grasa resbaladiza. Terreno difícil; criaturas en el área o que entren deben superar TS de Destreza o caer tumbadas.
- **Identificar (*Identify*):** Tocas un objeto mágico para descifrar sus propiedades, uso, cargas y sintonización. Lanzable como ritual (+10 min).
- **Palabra de Curación (*Healing Word*):** Como acción adicional a 60 pies, curas 1d4 + 6 PG a una criatura visible.
- **Rayo Nauseabundo (*Ray of Sickness*):** Impacto de conjuro a distancia (+6) inflige 2d8 + 3 de daño por veneno y obliga a una TS de Constitución para no quedar envenenado hasta el final de tu próximo turno.
- **Calentar Metal (*Heat Metal*):** Calientas al rojo vivo una pieza de metal (armadura, arma) a 60 pies. Causa 2d8 + 3 de fuego y obliga a soltarla o impone desventaja. Usas acción adicional en siguientes turnos para repetir el daño.
- **Esfera de Llamas (*Flaming Sphere*):** Esfera de fuego de 5 pies que inflige 2d6 + 3 de fuego en área (TS Destreza). Puedes moverla 30 pies con tu acción adicional cada turno.
- **Flecha Ácida de Melf (*Melf's Acid Arrow*):** Flecha reluciente que causa 4d4 + 3 de daño ácido al impactar y 2d4 adicionales al final del turno enemigo (mitad inicial si falla).
- **Recado (*Sending*):** Comunicación mental bidireccional instantánea de hasta 25 palabras sin importar la distancia (incluso entre planos).

</details>

---

## ⚙️ Infusiones de Artífice (Nivel 5)
> [!info] **Infusiones conocidas: 4** | **Objetos imbuidos activos simultáneos: 2**

1. 🏹 **Arma Mejorada:** Concede un bonificador de **+1 a las tiradas de ataque y de daño** con un arma sencilla o marcial *(aumenta a +2 a nivel 10)*.
2. 🛡️ **Defensa Mejorada:** Concede un bonificador de **+1 a la Clase de Armadura** mientras se lleva una armadura o escudo infusionado *(aumenta a +2 a nivel 10)*.
3. 🎒 **Replicar Objeto Mágico: Bolsa de Contención (Bag of Holding):** Espacio extradimensional de hasta 500 lb / 64 pies cúbicos. Peso fijo de 15 lb.
4. 🤖 **Sirviente Homúnculo (Homunculus Servant):** Requiere una gema/cristal de 100+ po como corazón. Crea un fiel autómata mágico volador que obedece tus órdenes.

---

## 🌟 Rasgos Raciales y de Clase

### 🌲 Rasgos de Raza: Gnomo de los Bosques
- **Astucia Gnómica:** **Ventaja** en todas las tiradas de salvación de Inteligencia, Sabiduría y Carisma contra magia.
- **Visión en la Oscuridad:** 60 pies.
- **Ilusionista Natural:** Conoces el truco *Ilusión Menor*.
- **Hablar con las Bestias Pequeñas:** Puedes comunicar conceptos e ideas simples a bestias de tamaño Pequeño o menor (ardillas, tejones, topos, pájaros).

---

### 🔧 Rasgos de Clase: Artífice
- **Arreglos Mágicos (Magical Tinkering):** Imbuyes propiedades sensoriales menores (luz tenue de 5 pies, mensaje grabado de 6 segundos, emisión de olor/sonido, o imagen/texto estático) en objetos diminutos no mágicos.
- **La Herramienta Adecuada para la Tarea:** Con herramientas a mano, creas mágicamente cualquier juego de herramientas de artesano en 1 hora de trabajo.
- **Lanzamiento Ritual:** Puedes lanzar como ritual cualquier conjuro de artífice de tu lista que tenga la etiqueta «ritual» y tengas preparado.

---

### 📜 Rasgo de Trasfondo: Ermitaño
- **Descubrimiento:** Durante tu prolongado aislamiento y vida de ermitaño en soledad/comunidad monástica, tuviste acceso a una verdad o revelación trascendental (un secreto cósmico, reliquia planar, sitio jamás visto o conocimiento oculto).

---

## 🎒 Inventario y Equipo

### ⚔️ Equipo Equipado
- **Armadura:** Cuero tachonado +1 *(CA 12 + 1 + 2 DES = 15)*
- **Escudo:** Escudo de madera y bronce *(+2 CA -> CA Total 17)*
- **Arma principal:** Ballesta de Hermandad +1
- **Arma secundaria:** Daga ligera
- **Canalizador / Foco:** [[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Baston Foco de Recado|Bastón Foco de Recado]] (sintonizado), suministros de alquimista y herramientas de manitas

### 🌀 Objetos Mágicos y Laboratorio
- 🪄 **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Baston Foco de Recado|Bastón Foco de Recado (Staff of Sending)]]:** *(Sintonizado)* Bastón arcano que actúa como foco de conjuros y permite canalizar el hechizo **Recado (Sending)** para comunicación mental a cualquier distancia.
- 🌀 **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Agujero Portatil|Agujero Portátil (Portable Hole)]]:** Pañuelo de seda circular que se despliega sobre una superficie sólida para abrir un pozo extradimensional de 6 pies de diámetro y 10 pies de profundidad.
- ⚗️ **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Laboratorio Alquimico|Laboratorio Alquímico Portátil (Mesa de Crafteo y Reactivos)]]:** Instalación completa montada en el interior del Agujero Portátil, recientemente reconstruida en Zadash por 380 PO tras su pérdida en el cautiverio.
- 🍶 **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Vasija Alquimica|Vasija Alquímica (Alchemy Jug)]]:** Recipiente mágico capaz de producir líquidos diarios por orden (ácido, veneno básico, cerveza, vino, aceite, miel, mayonesa, agua dulce, agua salada, vinagre).
- 🍄 **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Pocion de Psicodelia|Poción de Psicodelia (2 min)]]:** Vial de brebaje alucinógeno sensorial conservado en la bandolera.
- 📖 **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Libro en Lenguaje Feerico|Libro en Lenguaje Feérico]]:** Tomo rúnico rescatado en Zadash, actualmente en fase de estudio y descifrado.
- 📜 **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Rollo Magico Primordial|Rollo Mágico en Lenguaje Primordial]]:** Pergamino arcano en lengua elemental primordial para estudio.
- 🎽 **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Bandolera Tactica (4 Ranuras)|Bandolera Táctica (4 Ranuras — Equipada)]]:** Arnés equipado para uso rápido de consumibles con acción adicional.
- 🎽 **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Bandolera Tactica (3 Ranuras)|Bandolera Táctica (3 Ranuras — Equipada por P.I.L.A.)]]:** Entregada y equipada a [[01 - Campañas/Comunidad del Alba/03 - NPCs/P.I.L.A.|P.I.L.A.]] para soporte táctico y uso rápido de consumibles.

### 🎒 Mochila y Posesiones
- Paquete de explorador
- Suministros de alquimista (reabastecidos con [[01 - Campañas/Comunidad del Alba/03 - NPCs/Bracus|Bracus]])
- Herramientas de ladrón
- Herramientas de manitas

---

## 📖 Trasfondo e Historia

### 🌲 Orígenes en los Bosques de Hupperdook
Ren (30 años) nació y creció en una pacífica comunidad gnoma asentada en los frondosos bosques colindantes con la ciudad industrial de **[[01 - Campañas/Comunidad del Alba/05 - Lugares/Hupperdook|Hupperdook]]**. Allí compartió sus primeros años junto a su amigo inseparable de la infancia, **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Ozzley|Ozzley]]**, explorando la naturaleza y maravillándose con los extraños inventos y mecanismos que ocasionalmente llegaban desde los talleres de la ciudad.

### 🏔️ Vocación y Reclusión en el Monasterio de Silberquel
A los 17 años, impulsado por una profunda curiosidad intelectual y el deseo de comprender los misterios de la materia, Ren ingresó al **[[01 - Campañas/Comunidad del Alba/05 - Lugares/Monasterio de Silverquel|Monasterio de la Garganta de Silberquel]]**, una orden consagrada al estudio, preservación y forja de artefactos mágicos.
- **8 Años de Silencio y Estudio:** Vivió en estricta reclusión académica, dedicándose al estudio sistemático de la naturaleza, sus propiedades e interacciones sutiles entre sales minerales, plantas y catalizadores.
- **La Tutela de la Abadesa Nandes:** Su mentora, la maga elfa de los bosques **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Nandes|Abadesa Nandes]]**, fue su mayor fuente de inspiración, enseñándole cómo los elementos interactúan, se potencian y se transmutan.
- **Compañerismo:** Compartió talleres, experimentos y debates con **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Marciel|Marciel]]**, una joven artífice humana con quien forjó una estrecha amistad.

### 📜 La Misión de Egreso: El Artefacto Sagrado
Para culminar formalmente su etapa de formación en el monasterio y ser ordenado de pleno derecho, Ren debe cumplir su **Misión de Egreso**: salir al mundo exterior, **conseguir un artefacto místico o mágico de verdadero poder, y entregarlo en consagración al monasterio**.
- **La Búsqueda Frustrada de Ozzley:** Al romper su reclusión de 8 años para iniciar su viaje, Ren intentó buscar a su amigo **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Ozzley|Ozzley]]** (a quien no veía desde su segundo año en el claustro). Sin embargo, no logró dar con él antes de partir, dejando una herida y preocupación constante en su corazón.

### ⚔️ Cautiverio y Unión a la Comunidad del Alba
En su viaje hacia el sur en busca de pistas sobre artefactos antiguos, Ren fue emboscado por la bruja **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Rina|Rina]]**, quien le despojó de sus pertenencias y lo dejó prisionero a merced de una partida de gnolls. Tras ser rescatado por sus actuales compañeros en la **[[01 - Campañas/Comunidad del Alba/01 - Sesiones/Sesión 01 - El Rescate de Frater Ren|Sesión 01]]**, Ren encontró en la *Comunidad del Alba* a sus más leales aliados para avanzar en su misión de egreso, descubrir el destino de su amigo y enfrentar las amenazas que acechan el continente.

### 📘 Contacto con El Alma de Cobalto en Zadash
Tras rastrear y derrotar a la bruja Rina en Zadash, Ren acudió a la sede local de **[[01 - Campañas/Comunidad del Alba/06 - Facciones/El Alma de Cobalto|El Alma de Cobalto]]**, una gran orden monástica y biblioteca de magos y monjes consagrados a la diosa **Ioun (La Mentora del Saber)**, la misma deidad tutelar de su monasterio de origen.
- **El Guardia Elaion:** En las puertas del templo fue recibido por **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Elaion|Elaion]]**, un monje guardia que reconoció de inmediato su afinidad espiritual y lo guio a través del santuario.
- **El Encargo de la Maestra Ingka:** Fue recibido en audiencia por la **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Ingka|Maestra Ingka]]**, líder de la sucursal de Zadash, quien reconoció el valor de la party y le encomendó a Ren una misión de máxima confianza: **cuidar y tutelar a [[01 - Campañas/Comunidad del Alba/03 - NPCs/P.I.L.A.|P.I.L.A.]]**, reportando periódicamente al Alma de Cobalto sobre cualquier información relevante, recuerdo desbloqueado o facultad arcana que el constructo vaya recuperando durante su travesía hacia el norte.

---

## 👥 Vínculos Personales

| Personaje | Raza / Rol | Vínculo con Ren | Estado / Paradero |
| :--- | :--- | :--- | :--- |
| **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Ozzley\|Ozzley]]** | Gnomo de los Bosques (35 años) | Amigo íntimo de la infancia en los bosques de Hupperdook. No lo ve desde hace años. | Desconocido (Desaparecido) |
| **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Nandes\|Abadesa Nandes]]** | Elfa de los Bosques (Maga) | Mentora y líder del monasterio natal en Silberquel. Lo inspiró en la ciencia botánica y alquímica. | En el [[01 - Campañas/Comunidad del Alba/05 - Lugares/Monasterio de Silverquel\|Monasterio de Silberquel]] |
| **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Marciel\|Marciel]]** | Humana (25 años, Artífice) | Compañera de estudios monásticos. También cumpliendo su misión de egreso. | En tránsito por Wildemount |
| **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Ingka\|Maestra Ingka]]** | Alta Archivista (Alma de Cobalto) | Líder de la orden en Zadash. Le encomendó la custodia e informes sobre P.I.L.A. | En el [[01 - Campañas/Comunidad del Alba/05 - Lugares/Templo del Alma de Cobalto (Zadash)\|Templo del Alma de Cobalto]] |
| **[[01 - Campañas/Comunidad del Alba/03 - NPCs/Elaion\|Elaion]]** | Monje Guardia (Alma de Cobalto) | Guardia del templo en Zadash que lo recibió y guio fraternalmente. | En el [[01 - Campañas/Comunidad del Alba/05 - Lugares/Templo del Alma de Cobalto (Zadash)\|Templo del Alma de Cobalto]] |

---

## 🏹 Metas y Objetivos Personales
- [ ] **Misión de Egreso de Ioun:** Conseguir un artefacto místico o mágico de gran valor y consagrarlo formalmente en el [[01 - Campañas/Comunidad del Alba/05 - Lugares/Monasterio de Silverquel|Monasterio de la Garganta de Silberquel]].
- [ ] **Custodia e Informes de P.I.L.A.:** Proteger a [[01 - Campañas/Comunidad del Alba/03 - NPCs/P.I.L.A.|P.I.L.A.]] de la codicia de [[01 - Campañas/Comunidad del Alba/03 - NPCs/Bracus|Bracus]] y reportar a la [[01 - Campañas/Comunidad del Alba/03 - NPCs/Ingka|Maestra Ingka]] sobre las memorias y habilidades arcanas que vaya recuperando en el viaje hacia [[01 - Campañas/Comunidad del Alba/05 - Lugares/Eiselcross|Eiselcross]].
- [ ] **Rastro de Ozzley:** Investigar el paradero de [[01 - Campañas/Comunidad del Alba/03 - NPCs/Ozzley|Ozzley]] y descubrir qué ocurrió con él tras su partida de la comunidad natal.
- [x] **Derrota de la Bruja Rina:** Desmantelar la red de la bruja [[01 - Campañas/Comunidad del Alba/03 - NPCs/Rina|Rina]] y sus [[01 - Campañas/Comunidad del Alba/08 - Lore/Hongos Feericos de Zadash|hongos feéricos]] en [[01 - Campañas/Comunidad del Alba/05 - Lugares/Zadash|Zadash]].
- [ ] **Descifrar el Tomo Feérico:** Traducir con ayuda del Alma de Cobalto el [[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Libro en Lenguaje Feerico|Libro en Lenguaje Feérico]] recuperado de Rina.
- [ ] **Deuda de Honor:** Devolver los **200 PO** prestados del tesoro de la *Comunidad del Alba*.
- [ ] **Soporte Alquímico:** Fabricar elixires, pociones y bombas de alta eficiencia para mantener a la party a salvo.
