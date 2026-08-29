---
tipo: pj
campaña: Bilbo Volador
jugador: Yo
nombre: Moxy
raza: Tiefling
clase: Mago
subclase: Escuela de Ilusión
nivel: 3
alineamiento: Caótico neutral
trasfondo: Criminal (Chantajista)
rol_combate: DPS Arcano / Ilusión / Infiltración
estado: Activo
iniciativa: 2
ca: 12
velocidad: 30 pies
pg_max: 21
pg_actual: 21
bonif_competencia: 2
caracteristica_magica: int
fue: 9
des: 14
con: 12
int: 10
sab: 15
car: 15
salvaciones_competentes:
  - int
  - sab
habilidades:
  Acrobacias: 0
  Arcanos: 0
  Atletismo: 0
  Engañar: 1
  Historia: 0
  Interpretación: 0
  Intimidar: 0
  Investigación: 1
  Juego de Manos: 0
  Medicina: 0
  Naturaleza: 0
  Percepción: 0
  Perspicacia: 1
  Persuasión: 0
  Religión: 0
  Sigilo: 1
  Supervivencia: 0
  Trato con Animales: 0
monedas:
  pc: 0
  pp: 0
  pe: 0
  po: 220
  ppt: 0
espacios_conjuro:
  nv1_max: 4
  nv1_usados: 0
  nv2_max: 2
  nv2_usados: 0
conjuros_preparados:
  - "Disfrazarse"
  - "Rayo de Hechicería"
  - "Rociada de Color"
tags:
  - dnd/pj
  - dnd/bilbo-volador
---

# 😈 Moxy

> [!statblock] **Tiefling Mago (Nivel `VIEW[{nivel}][text]`) — Escuela de Ilusión**
> **Alineamiento:** `VIEW[{alineamiento}][text]` | **Trasfondo:** `VIEW[{trasfondo}][text]`
> **CA:** `INPUT[number:ca]` | **Iniciativa:** +`INPUT[number:iniciativa]` | **Velocidad:** `VIEW[{velocidad}][text]`
> **PG:** `INPUT[number:pg_actual]` / `INPUT[number:pg_max]` | **Bonif. Competencia:** +`VIEW[2 + floor(({nivel} - 1) / 4)][math]`
> **Idiomas:** Común, Élfico, Infernal

---

### 📊 Puntuaciones de Característica y Modificadores

| Característica | Puntuación Base | Modificador Calculado |
| :--- | :---: | :---: |
| **Fuerza (FUE)** | `INPUT[number:fue]` | **`VIEW[floor(({fue} - 10) / 2)][math]`** |
| **Destreza (DES)** | `INPUT[number:des]` | **`VIEW[floor(({des} - 10) / 2)][math]`** |
| **Constitución (CON)** | `INPUT[number:con]` | **`VIEW[floor(({con} - 10) / 2)][math]`** |
| **Inteligencia (INT)** | `INPUT[number:int]` | **`VIEW[floor(({int} - 10) / 2)][math]`** |
| **Sabiduría (SAB)** | `INPUT[number:sab]` | **`VIEW[floor(({sab} - 10) / 2)][math]`** |
| **Carisma (CAR)** | `INPUT[number:car]` | **`VIEW[floor(({car} - 10) / 2)][math]`** |

---

### ✨ Estadísticas de Magia (Mago de Ilusión)

| Estadística Mágica | Fórmula | Valor Actual |
| :--- | :--- | :---: |
| **Atributo de Conjuración** | Inteligencia | `VIEW[{int}][text]` (Mod: **+`VIEW[floor(({int} - 10) / 2)][math]`**) |
| **CD de Salvación de Conjuros** | `8 + Competencia + Mod INT` | **CD `VIEW[8 + (2 + floor(({nivel} - 1) / 4)) + floor(({int} - 10) / 2)][math]`** |
| **Bonificador de Ataque de Conjuro** | `Competencia + Mod INT` | **+`VIEW[(2 + floor(({nivel} - 1) / 4)) + floor(({int} - 10) / 2)][math]`** |
| **Máximo de Conjuros Preparados** | `Nivel + Mod INT` | **`VIEW[{nivel} + floor(({int} - 10) / 2)][math]`** conjuros |

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

| 🟤 Cobre (PC) | ⚪ Plata (PP) | 🟢 Electro (PE) | 🟡 Oro (PO) | 🔘 Platino (PPT) |
| :---: | :---: | :---: | :---: | :---: |
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
    value: 21
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

## 🔮 Grimorio y Conjuros

### 🔹 Espacios de Conjuro Diarios (Nivel 3)
- **Nivel 1:** `[ ] [ ] [ ] [ ]` (4 espacios)
- **Nivel 2:** `[ ] [ ]` (2 espacios)

---

### 🪄 Trucos (Cantrips - Uso Ilimitado)

| Truco | Escuela | Tiempo | Alcance | Comp. | Efecto Resumido |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Taumaturgia** *(Racial Tiefling)* | Transmutación | 1 Acción | 30 pies | V | Efectos sobrenaturales menores (voz retumbante x3, alterar llamas, temblores, abrir/cerrar puertas, ojos cambiantes). |
| **Ilusión Menor Mejorada** *(Escuela Ilusión)* | Ilusión | 1 Acción | 30 pies | S, M | Genera **sonido e imagen a la vez** en un único lanzamiento (1 min). Investigación vs CD 10 para distinguir. |
| **Agarre Electrizante** | Evocación | 1 Acción | Toque | V, S | Ataque c/c (+2). Daño **1d8 relámpago** y el objetivo **no puede usar reacciones** hasta su siguiente turno. Ventaja contra metal. |
| **Amistad** | Encantamiento | 1 Acción | Personal | S, M | **Ventaja** en pruebas de CAR hacia criatura no hostil (Conc. 1 min). Al terminar se vuelve hostil. |

---

### 📜 Libro de Conjuros de Moxy
> [!tip] Conjuros preparados hoy: **3 de 3** (Disfrazarse, Rayo de Hechicería, Rociada de Color).
> *Nota: Reprensión Infernal es racial (no consume límite de preparación diaria).*

| Prep | Conjuro | Nivel | Escuela | Tiempo | Alcance | Conc / Rit | Efecto / Daño |
| :---: | :--- | :---: | :--- | :--- | :--- | :---: | :--- |
| 🧬 | **Reprensión Infernal** *(Tiefling)* | 2 | Evocación | 1 Reacción | 60 pies | No | Cuando recibes daño: Salva DES. **3d10 fuego** (mitad si supera). 1 vez por descanso prolongado: `[ ]` |
| [x] | **Disfrazarse** | 1 | Ilusión | 1 Acción | Personal | No (1 h) | Modifica apariencia física, ropa y equipo (+-1 pie altura/complexión). Investigación vs CD 10 para detectar. |
| [x] | **Rayo de Hechicería** | 1 | Evocación | 1 Acción | 30 pies | Conc. (1 min) | Ataque a distancia (+2). **1d12 eléctrico**. En turnos siguientes usas tu acción para repetir 1d12 automático. |
| [x] | **Rociada de Color** | 1 | Ilusión | 1 Acción | Cono 15 pies | No (1 asalto) | Lanza **6d10**. Ciega a criaturas dentro del cono en orden ascendente según sus PG actuales. |
| [ ] | **Orbe Cromático** | 1 | Evocación | 1 Acción | 90 pies | No | Ataque a distancia (+2). **3d8 daño** (Ácido, Frío, Fuego, Relámpago, Veneno o Trueno). |
| [ ] | **Invisibilidad** | 2 | Ilusión | 1 Acción | Toque | Conc. (1 h) | Vuelve invisible al objetivo tocado hasta que ataque o lance un conjuro. |
| [ ] | **Travesura de Nathair** | 2 | Ilusión | 1 Acción | 60 pies (Cubo 20') | Conc. (1 min) | Oleada traviesa feérica/dracónica aleatoria en el área cada turno. |

---

### 📖 Detalles de Mecánicas de Conjuros

<details>
<summary><b>🔍 Ver descripción completa de cada conjuro</b></summary>

- **Agarre Electrizante (*Shocking Grasp*):** Realiza un ataque de conjuro cuerpo a cuerpo (+2). Si aciertas, 1d8 relámpago y el objetivo pierde sus reacciones hasta su siguiente turno. Tienes ventaja si viste armadura de metal. El daño aumenta al nivel 5 (2d8), nivel 11 (3d8) y nivel 17 (4d8).
- **Amistad (*Friends*):** Tienes ventaja en todas las pruebas de Carisma dirigidas a una criatura no hostil (Concentración, hasta 1 min). Al terminar el conjuro, la criatura comprende que usaste magia y se vuelve hostil hacia ti.
- **Ilusión Menor Mejorada (*Minor Illusion*):** Al ser de la Escuela de Ilusión, creas un sonido Y una imagen en el mismo lanzamiento (duración 1 min). Se disipa como acción o si vuelves a lanzarlo. Investigación vs CD 10 para distinguir.
- **Disfrazarse (*Disguise Self*):** Haces que tu apariencia física y atuendo parezcan distintos durante 1 hora. Puedes cambiar altura en 1 pie, contextura y detalles.
- **Orbe Cromático (*Chromatic Orb*):** Lanzas un orbe de energía de 4 pulgadas. Con un ataque de conjuro a distancia (+2), inflige 3d8 de daño del tipo elegido (Ácido, Frío, Fuego, Relámpago, Veneno o Trueno). Aumenta 1d8 por cada nivel superior.
- **Rayo de Hechicería (*Witch Bolt*):** Un arco eléctrico une al objetivo y a ti. Impacto a distancia inflige 1d12 eléctrico por nivel de conjuro. Puedes usar tu acción en turnos siguientes para infligir 1d12 automático continuo.
- **Rociada de Color (*Color Spray*):** Tira 6d10 (+2d10 por nivel superior). Ciega a criaturas dentro de un cono de 15 pies en orden ascendente de sus PG actuales durante 1 asalto.
- **Invisibilidad (*Invisibility*):** La criatura tocada se vuelve invisible junto a su equipo durante 1 hora (Concentración). Termina si ataca o lanza un conjuro.
- **Travesura de Nathair (*Nathair's Mischief*):** Llenas un cubo de 20 pies a 60 pies con magia feérica/dracónica (Concentración 1 min). Tiras en la tabla de Oleada Traviesa al inicio de cada turno.

</details>

---

## 🌟 Rasgos Raciales y de Clase

### 🧬 Rasgos de Raza: Tiefling
- **Visión en la Oscuridad:** Gracias a tu herencia infernal, tienes una visión superior en la oscuridad y penumbra. Puedes ver en la penumbra a una distancia de **60 pies** como si fuera luz brillante, y en la oscuridad como si fuera penumbra (en escala de grises).
- **Legado Infernal:**
  - *Taumaturgia:* Conoces el truco.
  - *Reprensión Infernal:* A nivel 3, puedes lanzarlo como conjuro de nivel 2 ($3d10$ de fuego) 1 vez por descanso prolongado: `[ ]`.
  - *Oscuridad:* Al alcanzar el nivel 5, podrás lanzarlo 1 vez por descanso prolongado.
- **Resistencia Infernal:** Tienes resistencia al daño por fuego (recibes la mitad de daño).

---

### 🔮 Rasgos de Clase: Mago (Nivel 3)
- **Lanzamiento de Conjuros:** Utilizas tu Inteligencia para la magia. Preparas tantos conjuros como tu $\text{Modificador de INT} + \text{Nivel de Mago}$ ($0 + 3 = 3$ conjuros).
- **Lanzamiento Ritual:** Puedes lanzar cualquier conjuro de tu libro como si fuera un ritual (+10 min) si tiene la etiqueta «ritual», sin necesidad de tenerlo preparado ni gastar espacios de conjuro.
- **Recuperación Arcana:** 1 vez al día durante un descanso breve, puedes recuperar espacios de conjuro con un nivel combinado igual o menor a la mitad de tu nivel de mago redondeado hacia arriba ($\le 2$ niveles de espacios a nivel 3): `[ ]`.
- **Libro de Conjuros:**
  - *Copiar conjuro nuevo:* 2 horas y 50 po por cada nivel del conjuro.
  - *Reemplazar / Copia de seguridad:* 1 hora y 10 po por cada nivel del conjuro.

---

### 🎭 Tradición Arcana: Escuela de Ilusión
- **Erudito de la Ilusión:** El oro y el tiempo para copiar un conjuro de la escuela de **Ilusión** en tu libro se reduce a la mitad (**1 hora y 25 po** por nivel).
- **Ilusión Menor Mejorada:** Aprendes el truco *Ilusión menor*. No cuenta para tu límite de trucos conocidos. Cuando lanzas *Ilusión menor*, **generas tanto sonido como imagen simultáneamente en un único lanzamiento**.

---

### 🗝️ Rasgo de Trasfondo: Criminal (Chantajista)
- **Contacto Criminal:** Tienes un contacto de confianza que actúa como enlace con una red de delincuentes, mensajeros locales, caravaneros corruptos y marineros de mala muerte para hacer llegar y recibir recados a grandes distancias.

---

## 🎒 Inventario y Equipo

### ⚔️ Equipo Equipado
- **Mano Principal / Arma:** Daga ligera (1d4 perforante, sutil, arrojadiza 20/60)
- **Mano Secundaria:** Foco Arcano (Varita / Cristal)
- **Armadura:** Ropa oscura de viaje (CA 12 con DES)
- **Herramientas preparadas:** Herramientas de ladrón

### 🎒 Mochila de Aventurero
- Libro de Conjuros (Grimorio)
- Herramientas de Ladrón
- Juego de Azar / Baraja marcada
- Paquete de Erudito (Tinta, pluma, 10 hojas de pergamino, yesca)
- [[01 - Campañas/Bilbo Volador/07 - Inventario/Objetos/Collar de Plata con Rubi|Collar de Plata con Rubí]] *(500-600 PO, cobrado al guardia semiorco)*
- [[01 - Campañas/Bilbo Volador/07 - Inventario/Objetos/Pocion de Curacion|1x Poción de Curación]] *(2d4+2 PG)*
- Diamante de 50 po *(pendiente para Orbe Cromático)*
- Raciones de viaje (x5)
- Cantimplora / Odre de agua

---

## 📖 Trasfondo e Historia
- **Origen:** Curtido en los barrios bajos y el crimen organizado.
- **En el Circo Ambulante:** Lleva más de 2 años en la compañía de [[01 - Campañas/Bilbo Volador/03 - NPCs/La Madam|La Madam]], trabajando mano a mano con [[01 - Campañas/Bilbo Volador/02 - Personajes/Saye|Saye]]. Es el veterano del grupo resolviendo asuntos oscuros y cobrando deudas a guardias despistados.
- **Especialidad:** Chantaje, recolección de secretos y extorsión sutil con magia de engaño e ilusión.

---

## 🏹 Metas y Objetivos Personales
- [ ] Recuperar el tesoro de La Madam y descubrir qué criatura o facción orquestó el robo.
- [ ] Conseguir un diamante de 50 po para activar el *Orbe Cromático*.
- [ ] Vender o utilizar el *Collar de Plata con Rubí* según convenga.
- [ ] Establecer una red de informantes y contactos en la región.
