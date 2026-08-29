---
tipo: pj
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
jugador: "Yo"
nombre: "<% tp.file.title %>"
raza: ""
clase: ""
subclase: ""
nivel: 1
alineamiento: ""
trasfondo: ""
rol_combate: ""
estado: "Activo"
iniciativa: 0
ca: 10
velocidad: "30 pies"
pg_max: 10
pg_actual: 10
bonif_competencia: 2

# Característica de Lanzamiento de Conjuros: int, sab, car (deja vacío si no lanza conjuros)
caracteristica_magica: "int"

# Puntuaciones de Característica
fue: 10
des: 10
con: 10
int: 10
sab: 10
car: 10

# Salvaciones con competencia (añade: fue, des, con, int, sab, car)
salvaciones_competentes: []

# Nivel de Competencia en Habilidades:
# 0 = Normal | 0.5 = Media | 1 = Competente | 2 = Pericia | 3 = Maestría
habilidades:
  Acrobacias: 0
  Arcanos: 0
  Atletismo: 0
  Engañar: 0
  Historia: 0
  Interpretación: 0
  Intimidar: 0
  Investigación: 0
  Juego de Manos: 0
  Medicina: 0
  Naturaleza: 0
  Percepción: 0
  Perspicacia: 0
  Persuasión: 0
  Religión: 0
  Sigilo: 0
  Supervivencia: 0
  Trato con Animales: 0

# Monedero
monedas:
  pc: 0 # Cobre
  pp: 0 # Plata
  pe: 0 # Electro
  po: 10 # Oro
  ppt: 0 # Platino

espacios_conjuro:
  nv1_max: 2
  nv1_usados: 0
  nv2_max: 0
  nv2_usados: 0

conjuros_preparados: []

tags:
  - dnd/pj
---

# 👤 <% tp.file.title %>

> [!abstract] **Resumen del Personaje**
> **Nivel:** `INPUT[number:nivel]` | **Clase:** `VIEW[{clase}][text]` (`VIEW[{subclase}][text]`) | **Raza:** `VIEW[{raza}][text]`
> **Alineamiento:** `VIEW[{alineamiento}][text]` | **Trasfondo:** `VIEW[{trasfondo}][text]`
> **CA:** `INPUT[number:ca]` | **Iniciativa:** +`INPUT[number:iniciativa]` | **Velocidad:** `VIEW[{velocidad}][text]`
> **PG:** `INPUT[number:pg_actual]` / `INPUT[number:pg_max]` | **Bonif. Competencia:** +`VIEW[2 + floor(({nivel} - 1) / 4)][math]`

---

### 📊 Puntuaciones de Característica y Modificadores

| Característica         |   Puntuación Base   |           Modificador Calculado            |
| :--------------------- | :-----------------: | :----------------------------------------: |
| **Fuerza (FUE)**       | `INPUT[number:fue]` | **`VIEW[floor(({fue} - 10) / 2)][math]`** |
| **Destreza (DES)**     | `INPUT[number:des]` | **`VIEW[floor(({des} - 10) / 2)][math]`** |
| **Constitución (CON)** | `INPUT[number:con]` | **`VIEW[floor(({con} - 10) / 2)][math]`** |
| **Inteligencia (INT)** | `INPUT[number:int]` | **`VIEW[floor(({int} - 10) / 2)][math]`** |
| **Sabiduría (SAB)**    | `INPUT[number:sab]` | **`VIEW[floor(({sab} - 10) / 2)][math]`** |
| **Carisma (CAR)**      | `INPUT[number:car]` | **`VIEW[floor(({car} - 10) / 2)][math]`** |

---

### ✨ Estadísticas de Magia

| Estadística Mágica | Fórmula | Valor Actual |
| :--- | :--- | :---: |
| **Atributo de Conjuración** | Inteligencia / Sabiduría / Carisma | `VIEW[{int}][text]` (Mod: **+`VIEW[floor(({int} - 10) / 2)][math]`**) |
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
    value: 10
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

### 🔹 Espacios de Conjuro Diarios
- **Nivel 1:** `[ ] [ ] [ ] [ ]`
- **Nivel 2:** `[ ] [ ]`
- **Nivel 3:** `[ ] [ ]`

### 🪄 Trucos Conocidos (Cantrips - Ilimitados)
- **Truco 1:** *Descripción breve*
- **Truco 2:** *Descripción breve*
- **Truco 3:** *Descripción breve*

### 📜 Libro de Conjuros (Preparados marcados con `[x]`)
| Prep | Conjuro | Nivel | Escuela | Tiempo | Alcance | Conc / Rit | Efecto / Resumen |
| :---: | :--- | :---: | :--- | :--- | :--- | :---: | :--- |
| [x] | **Conjuro 1** | 1 | Escuela | 1 Acción | 60 pies | No | Efecto |

---

## 🎒 Inventario y Equipo

### 💰 Monedero y Fortuna
- **Cobre (PC):** `$= dv.current().monedas?.pc || 0`
- **Plata (PP):** `$= dv.current().monedas?.pp || 0`
- **Electro (PE):** `$= dv.current().monedas?.pe || 0`
- **Oro (PO):** `$= dv.current().monedas?.po || 0`
- **Platino (PPT):** `$= dv.current().monedas?.ppt || 0`

### ⚔️ Equipo Equipado
- **Mano Principal / Arma:** 
- **Mano Secundaria / Foco Arcano:** 
- **Armadura / Vestimenta:** 
- **Accesorios / Joyas:** 

### 🎒 Mochila y Posesiones
- Herramientas de oficio / herramientas de ladrón
- Paquete de explorador / erudito
- Raciones de viaje
- Cantimplora / Odre de agua
- Bolsa de componentes / Foco

---

## 🌟 Rasgos, Talentos y Habilidades Especiales

### 🧬 Rasgos Raciales
- **Visión en la Oscuridad:** 60 pies.

### ⚔️ Rasgos de Clase
- **Rasgo 1:** Descripción.

---

## 📖 Trasfondo e Historia
- **Origen:** 
- **Motivación para aventurarse:** 
- **Rasgo de personalidad:** 
- **Ideal:** 
- **Vínculo:** 
- **Defecto:** 

---

## 🏹 Metas y Objetivos Personales
- [ ] 
