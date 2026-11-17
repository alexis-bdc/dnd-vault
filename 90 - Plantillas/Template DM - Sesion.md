---
tipo: sesion
campaña: "<% tp.file.folder(true).includes('01 - Campañas') ? tp.file.folder(true).split('/')[1] : '' %>"
sesion_num: 
fecha_real: <% tp.date.now("YYYY-MM-DD") %>
fecha_in_game: ""
lugar_inicio: ""
lugar_fin: ""
tags:
  - dnd/sesion
  - dnd/dm
---

# <% tp.file.title %>

## 🧰 Preparación (antes de jugar)

### Repaso
- ¿Dónde quedaron? ¿Qué cabo suelto quieren seguir?

### Inicio fuerte
- Escena con la que arranca la sesión:

### Escenas posibles
- 
- 

### Secretos y pistas
> Sin lugar fijo: suéltalos donde los PJ busquen.
1. 
2. 
3. 
4. 
5. 

### PNJ que pueden aparecer
- [[ ]]

### Lugares
- [[ ]]

### Encuentros
> Marca ✅ los que se jugaron. Los no jugados quedan pendientes para la próxima sesión.
```dataviewjs
await dv.view("90 - Plantillas/Scripts/encuentros-sesion")
```

```meta-bind-button
label: ⚡ Encuentro rápido para esta sesión
icon: zap
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/generar_encuentro.md
```

### Tesoro
- 

---

## 📝 Lo que pasó (llenar al terminar)
- 

## 🔍 Cabos sueltos
> Usa `- [ ]`. Aparecen en el dashboard hasta que los marques.
- [ ] 

## 💬 Para el reloj de amenaza
- ¿Los PJ frenaron o ignoraron a la amenaza?
