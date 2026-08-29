---
tipo: compañero
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
jugador: "" # Nombre de tu amigo/compañero en la vida real
nombre_pj: "<% tp.file.title %>"
raza: ""
clase: ""
subclase: ""
rol_combate: "" # Tanque / Daño / Curador / Control / Soporte
ca_estimada: ""
percepcion_pasiva: ""
estado: "Activo" # Activo / Herido / Inconsciente / Ausente
tags:
  - dnd/compañero
---

# 🛡️ <% tp.file.title %> (PJ Aliado)

> [!info] **Ficha de Compañero de Party**
> **Jugador:** `$= dv.current().jugador || "Desconocido"` | **Raza y Clase:** `$= dv.current().raza` `$= dv.current().clase` (`$= dv.current().subclase || "N/A"`)
> **Rol en la Party:** `$= dv.current().rol_combate || "Polivalente"` | **CA Estimada:** `$= dv.current().ca_estimada || "?"` | **Percepción Pasiva:** `$= dv.current().percepcion_pasiva || "?"`
> **Estado Actual:** `$= dv.current().estado`

---

## ⚔️ Habilidades y Recursos Clave en Combate
- **Hechizos / Habilidades que suele usar:**
  - 
- **Sinergias con mi PJ (combos o apoyo mutuo):**
  - 
- **Puntos débiles o cuidados especiales:**
  - 

---

## 🤝 Dinámica y Relación con mi Personaje
- **Nivel de confianza:** ⭐⭐⭐☆☆ (3/5)
- **Opinión que tiene mi PJ de él/ella:** 
- **Deudas, favores o promesas pendientes:**
  - [ ] 

---

## 📖 Lo que sabemos de su Historia / Secretos Revelados
- **Trasfondo conocido:** 
- **Motivación personal:** 
- **Detalles sospechosos o misterios:** 

---

## 🎒 Objetos Importantes que Lleva
- 
