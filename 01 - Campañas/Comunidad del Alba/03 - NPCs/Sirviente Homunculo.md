---
tipo: npc
campaña: "Comunidad del Alba"
nombre: "Sirviente Homúnculo"
raza: "Constructo"
tamaño: "Diminuto"
alineamiento: "Neutral"
clase_o_rol: "Sirviente de Frater Ren (Infusión de Artífice)"
faccion: "[[01 - Campañas/Comunidad del Alba/06 - Facciones/Comunidad del Alba|Comunidad del Alba]]"
ubicacion: "Con Frater Ren"
actitud: "Leal a su creador"
estado: "Activo"
ca: 13
pg_max: 10
pg_actual: 10
velocidad: "20 pies, volar 30 pies"
percepcion_pasiva: 16
tags:
  - dnd/npc
  - dnd/compañero
  - dnd/comunidad-del-alba
---

# 🪰 Sirviente Homúnculo (Constructo Diminuto)

> [!statblock] **Sirviente Homúnculo de [[01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren|Frater Ren]]**
> **CA:** 13 (armadura natural) | **PG:** `$= dv.current().pg_actual` / `$= dv.current().pg_max` *(1 + mod INT + nivel de artífice)* | **Velocidad:** 20 pies, volar 30 pies
> **Sentidos:** Visión en la oscuridad 60 pies, Percepción Pasiva 16
> **Inmunidades:** Daño de veneno; condición envenenado
> **Idiomas:** Entiende los idiomas que habla su creador

---

## 📊 Puntuaciones y Modificadores

| FUE | DES | CON | INT | SAB | CAR |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **4** (-3) | **15** (+2) | **12** (+1) | **10** (+0) | **10** (+0) | **7** (-2) |

- **Tiradas de Salvación:** Destreza **+5**
- **Habilidades:** Percepción **+6**, Sigilo **+5**

---

## 🔬 Rasgos Especiales

### 🌀 Evasión
- Si sufre un efecto que permite TS de Destreza para recibir la mitad de daño, no recibe daño si la supera y solo la mitad si falla. No funciona si está incapacitado.

---

## ⚔️ Acciones

### ⚡ Golpe de Fuerza
- **Ataque mágico a distancia:** +6 al impacto (competencia + mod INT de Ren), alcance 30 pies.
- **Impacto:** 1d4 + 3 de daño de fuerza.

---

## 🛡️ Reacciones

### ✨ Canalizar Magia
- Lanza un conjuro de toque de Ren a través de sí mismo (el homúnculo debe estar a 120 pies de Ren).

---

## 📜 Notas de Combate
- Actúa justo después de Ren en iniciativa. Si Ren no le da órdenes (acción adicional), solo esquiva.
- El conjuro *Reparar* lanzado sobre él le devuelve 2d6 PG.
- Si muere, se desvanece y deja su corazón (la gema) en su espacio; Ren puede crear otro rehaciendo la infusión.

---

## 🖼️ Imagen

![[SirvienteHomunculo.jpg]]
