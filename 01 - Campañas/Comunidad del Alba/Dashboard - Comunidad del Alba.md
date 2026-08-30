---
tipo: dashboard
campaña: "Comunidad del Alba"
tags:
  - dnd/dashboard
---

# 🎲 Campaña: Comunidad del Alba

> [!nav] **Navegación Rápida**
> 📜 [[01 - Campañas/Comunidad del Alba/01 - Sesiones/|01 - Sesiones]] • 🛡️ [[01 - Campañas/Comunidad del Alba/02 - Personajes/|02 - Personajes]] • 👥 [[01 - Campañas/Comunidad del Alba/03 - NPCs/|03 - NPCs]]
> 🎯 [[01 - Campañas/Comunidad del Alba/04 - Misiones/|04 - Misiones]] • 🏰 [[01 - Campañas/Comunidad del Alba/05 - Lugares/|05 - Lugares]] • 🛡️ [[01 - Campañas/Comunidad del Alba/06 - Facciones/|06 - Facciones]]
> 🎒 [[01 - Campañas/Comunidad del Alba/07 - Inventario/|07 - Inventario]] • 📦 [[01 - Campañas/Comunidad del Alba/07 - Inventario/Inventario de la Party|Inventario de la Party]] • 📖 [[01 - Campañas/Comunidad del Alba/08 - Lore/|08 - Lore]]

---

## 🎮 Panel de Control de Sesión en Vivo ([[01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren|🧪 Frater Ren]])

> [!abstract] **Estado Vital y Combate**
> **PG:** `INPUT[number:01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#pg_actual]` / `VIEW[{01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#pg_max}][text]` | **CA:** `VIEW[{01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#ca}][text]` | **Iniciativa:** +`VIEW[{01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#iniciativa}][text]`


### 🔮 Espacios de Conjuro Diarios

| Nivel de Espacio | Máximo | Usados | Restantes |
| :---: | :---: | :---: | :---: |
| **Nivel 1** | `VIEW[{01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv1_max}][text]` | `INPUT[number:01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv1_usados]` | **`VIEW[{01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv1_max} - {01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv1_usados}][math]`** |
| **Nivel 2** | `VIEW[{01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv2_max}][text]` | `INPUT[number:01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv2_usados]` | **`VIEW[{01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv2_max} - {01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv2_usados}][math]`** |

```meta-bind-button
label: 🌙 Descanso Largo para Frater Ren
icon: bed
style: primary
actions:
  - type: updateMetadata
    bindTarget: 01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#pg_actual
    evaluate: false
    value: 50
  - type: updateMetadata
    bindTarget: 01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv1_usados
    evaluate: false
    value: 0
  - type: updateMetadata
    bindTarget: 01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#espacios_conjuro.nv2_usados
    evaluate: false
    value: 0
```

### 💰 Monedero Personal de Frater Ren

```meta-bind-button
label: 💰 Gestionar Monedero de Ren (Añadir / Gastar)
icon: coins
style: primary
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/gestionar_monedero.md
```

|                                       🟤 Cobre (PC)                                       |                                       ⚪ Plata (PP)                                        |                                      🟢 Electro (PE)                                      |                                        🟡 Oro (PO)                                        |                                      🔘 Platino (PPT)                                      |
| :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: |
| `INPUT[number:01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#monedas.pc]` | `INPUT[number:01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#monedas.pp]` | `INPUT[number:01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#monedas.pe]` | `INPUT[number:01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#monedas.po]` | `INPUT[number:01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md#monedas.ppt]` |

---
## 🧪 Alquimia de Combate y Consumibles ([[01 - Campañas/Comunidad del Alba/07 - Inventario/Laboratorio Alquimico|Laboratorio Alquímico]])

```meta-bind-button
label: ⚗️ Crafteo Rápido de Alquimia
icon: flask-conical
style: primary
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/craftear_alquimia.md
```
```meta-bind-button
label: 📜 Registrar Nueva Receta
icon: scroll
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/agregar_receta.md
```
```meta-bind-button
label: 📦 Comprar / Añadir Consumibles
icon: package-plus
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/agregar_consumible.md
```
```meta-bind-button
label: ➕ Recolectar / Añadir Materia Prima
icon: plus-circle
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/agregar_materia_prima.md
```
```meta-bind-button
label: 🧪 Modificar Esencias y Polvos
icon: flask-round
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/ajustar_esencias.md
```

### 🎽 Bandolera Táctica de Frater Ren (4 Ranuras — Acción Adicional)

```dataviewjs
const stockPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md";
const stockFile = app.vault.getAbstractFileByPath(stockPath);
const pStock = dv.page(stockPath);
const fmStock = (stockFile ? app.metadataCache.getFileCache(stockFile)?.frontmatter : null) || pStock?.file?.frontmatter || pStock || {};

const consumibles = fmStock.consumibles || {};
const bandolera = fmStock.bandolera || {};

// Solo consumibles con stock > 0
const availableItems = Object.keys(consumibles).filter(name => Number(consumibles[name]) > 0);

const container = dv.el("div", "");
container.setAttribute("contenteditable", "false");
container.addEventListener("click", (e) => e.stopPropagation());
container.addEventListener("mousedown", (e) => e.stopPropagation());
container.addEventListener("dblclick", (e) => e.stopPropagation());

const table = container.createEl("table", { cls: "dataview table-view-table" });
const thead = table.createEl("thead");
const hRow = thead.createEl("tr");
["Ranura", "Objeto Equipado", "Acción de Combate"].forEach(text => {
  hRow.createEl("th", { text, cls: "text-left" });
});

const tbody = table.createEl("tbody");

for (let i = 1; i <= 4; i++) {
  const slotKey = "ranura_" + i;
  let equipped = bandolera[slotKey] || "Vacío";
  const currentStock = Number(consumibles[equipped]) || 0;

  // Si lo asignado ya no existe en stock, pasa a Vacío
  if (equipped !== "Vacío" && currentStock <= 0) {
    equipped = "Vacío";
    if (stockFile) {
      app.fileManager.processFrontMatter(stockFile, (fm) => {
        if (!fm.bandolera) fm.bandolera = {};
        fm.bandolera[slotKey] = "Vacío";
      });
    }
  }

  const row = tbody.createEl("tr");

  // Col 1: Ranura
  const tdSlot = row.createEl("td");
  tdSlot.createEl("strong", { text: "Ranura " + i });

  // Col 2: Selector de objeto equipado (solo disponibles)
  const tdSelect = row.createEl("td");
  const select = tdSelect.createEl("select", { cls: "dropdown" });
  select.style.cursor = "pointer";
  select.style.padding = "4px 8px";
  select.style.borderRadius = "4px";

  const optVacio = select.createEl("option", { text: "⚪ Vacío / Sin Equipar", value: "Vacío" });
  if (equipped === "Vacío") optVacio.selected = true;

  for (const name of availableItems) {
    const opt = select.createEl("option", { text: "🧪 " + name, value: name });
    if (equipped === name) opt.selected = true;
  }

  select.onchange = async () => {
    const chosen = select.value;
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.bandolera) fm.bandolera = {};
      fm.bandolera[slotKey] = chosen;
    });
    new Notice("🎽 Ranura " + i + ": " + chosen);
  };

  // Col 3: Botón de Uso Directo (Siempre gasta 1 y deja la ranura en Vacío)
  const tdAction = row.createEl("td", { cls: "text-center" });
  const isEquipped = equipped !== "Vacío" && currentStock > 0;
  const btnUse = tdAction.createEl("button", {
    text: "⚡ Usar (Acción Adicional)",
    cls: "mod-cta btn-sm"
  });
  btnUse.style.cursor = isEquipped ? "pointer" : "not-allowed";
  btnUse.disabled = !isEquipped;

  btnUse.onclick = async () => {
    if (!isEquipped || !stockFile) return;

    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.consumibles || !fm.consumibles[equipped] || fm.consumibles[equipped] < 1) {
        new Notice("❌ No quedan unidades en stock de " + equipped);
        return;
      }

      // Restar 1 de stock
      fm.consumibles[equipped] -= 1;
      const rest = fm.consumibles[equipped];

      // Siempre vaciar la ranura al usarse
      if (!fm.bandolera) fm.bandolera = {};
      fm.bandolera[slotKey] = "Vacío";

      new Notice("⚡ ¡Usaste 1x \"" + equipped + "\" de la Ranura " + i + "!\n🎽 La Ranura " + i + " ahora está VACÍA. (Stock restante: " + rest + ")", 5000);
    });
  };
}
```

---

### 🧪 Pociones y Consumibles en Stock (Disponibles en el Lab)

```dataviewjs
const stockPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md";
const recetasPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Base de Recetas.md";

const stockFile = app.vault.getAbstractFileByPath(stockPath);
const recetasFile = app.vault.getAbstractFileByPath(recetasPath);

const pStock = dv.page(stockPath);
const pRecetas = dv.page(recetasPath);

const fmStock = (stockFile ? app.metadataCache.getFileCache(stockFile)?.frontmatter : null) || pStock?.file?.frontmatter || pStock || {};
const fmRecetas = (recetasFile ? app.metadataCache.getFileCache(recetasFile)?.frontmatter : null) || pRecetas?.file?.frontmatter || pRecetas || {};

const consumibles = fmStock.consumibles || {};
const recetas = fmRecetas.recetas_alquimia || {};

const enStock = Object.entries(consumibles).filter(([nombre, cant]) => Number(cant) > 0);

if (enStock.length === 0) {
  dv.paragraph("> [!info] 🧪 **No hay consumibles ni pociones en stock actualmente.** Las pociones con stock 0 quedan ocultas automáticamente. Usa los botones superiores para craftear o añadir existencias.");
} else {
  const container = dv.el("div", "");
  container.setAttribute("contenteditable", "false");
  container.addEventListener("click", (e) => e.stopPropagation());
  container.addEventListener("mousedown", (e) => e.stopPropagation());
  container.addEventListener("dblclick", (e) => e.stopPropagation());
  const table = container.createEl("table", { cls: "dataview table-view-table" });
  const thead = table.createEl("thead");
  const hRow = thead.createEl("tr");
  ["Consumible", "Stock", "Efecto Resumido", "Acción"].forEach(text => {
    hRow.createEl("th", { text, cls: "text-left" });
  });

  const tbody = table.createEl("tbody");

  for (const [nombre, cant] of enStock) {
    const row = tbody.createEl("tr");
    
    // Nombre
    const tdName = row.createEl("td");
    tdName.createEl("strong", { text: nombre });

    // Stock con controles +/-
    const tdStock = row.createEl("td", { cls: "text-center whitespace-nowrap" });
    const btnMinus = tdStock.createEl("button", { text: "➖", cls: "btn-sm" });
    btnMinus.style.cursor = "pointer";
    btnMinus.style.marginRight = "6px";
    btnMinus.onclick = async () => {
      if (!stockFile) return;
      await app.fileManager.processFrontMatter(stockFile, (fm) => {
        if (fm.consumibles && fm.consumibles[nombre] > 0) {
          fm.consumibles[nombre] -= 1;
        }
      });
    };

    const sp = tdStock.createEl("span", { text: ` ${cant} ` });
    sp.style.fontWeight = "bold";
    sp.style.color = "var(--text-accent, #38bdf8)";

    const btnPlus = tdStock.createEl("button", { text: "➕", cls: "btn-sm" });
    btnPlus.style.cursor = "pointer";
    btnPlus.style.marginLeft = "6px";
    btnPlus.onclick = async () => {
      if (!stockFile) return;
      await app.fileManager.processFrontMatter(stockFile, (fm) => {
        if (!fm.consumibles) fm.consumibles = {};
        fm.consumibles[nombre] = (fm.consumibles[nombre] || 0) + 1;
      });
    };

    // Efecto dinámico desde recetas_alquimia
    const desc = recetas[nombre]?.descripcion || "Consumible alquímico.";
    row.createEl("td", { text: desc });

    // Botón Usar 1x
    const tdAction = row.createEl("td", { cls: "text-center" });
    const btnUse = tdAction.createEl("button", { text: "⚡ Usar 1x", cls: "mod-cta btn-sm" });
    btnUse.style.cursor = "pointer";
    btnUse.onclick = async () => {
      if (!stockFile) return;
      await app.fileManager.processFrontMatter(stockFile, (fm) => {
        if (!fm.consumibles || (fm.consumibles[nombre] || 0) < 1) {
          new Notice(`❌ No tienes unidades de ${nombre}`);
          return;
        }
        fm.consumibles[nombre] -= 1;
        new Notice(`⚡ ¡Has utilizado 1x "${nombre}"! (Restantes: ${fm.consumibles[nombre]})`, 4000);
      });
    };
  }
}
```

---

## 🛡️ Miembros de la Party (Grupo Aventurero)

```dataview
TABLE jugador AS "Jugador", raza AS "Raza", clase AS "Clase", subclase AS "Subclase", rol_combate AS "Rol / Función", estado AS "Estado"
FROM "01 - Campañas/Comunidad del Alba/02 - Personajes"
WHERE tipo = "pj" OR tipo = "compañero"
SORT jugador ASC
```

---

## 👥 NPCs y Contactos del Mundo

```dataview
TABLE raza AS "Raza", clase_o_rol AS "Rol / Oficio", faccion AS "Facción", actitud AS "Actitud", estado AS "Estado"
FROM "01 - Campañas/Comunidad del Alba/03 - NPCs"
WHERE tipo = "npc"
SORT actitud DESC, file.name ASC
```

---

## 📜 Últimas Sesiones Jugadas

```dataview
TABLE fecha_real AS "Fecha Real", lugar_fin AS "Destino/Fin"
FROM "01 - Campañas/Comunidad del Alba/01 - Sesiones"
WHERE tipo = "sesion"
SORT file.name DESC
LIMIT 5
```

---

## 🎯 Misiones Activas y Cabos Sueltos

```dataview
TABLE prioridad AS "Prioridad", dada_por AS "Otorgada por", ubicacion AS "Lugar", recompensa AS "Recompensa"
FROM "01 - Campañas/Comunidad del Alba/04 - Misiones"
WHERE tipo = "mision" AND estado = "Activa"
SORT prioridad DESC
```

---

## 🏰 Lugares Clave

```dataview
TABLE tipo_lugar AS "Tipo", region AS "Región", gobernante AS "Gobernante", peligro AS "Peligro"
FROM "01 - Campañas/Comunidad del Alba/05 - Lugares"
WHERE tipo = "lugar"
SORT file.name ASC
```

---


## 🎒 Inventario y Objetos Relevantes

> [!nav] **Accesos Directos de Inventario:** 🧪 [[01 - Campañas/Comunidad del Alba/07 - Inventario/Laboratorio Alquimico|Laboratorio Alquímico]] • 🌀 [[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Agujero Portatil|Agujero Portátil]] • 🍶 [[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Vasija Alquimica|Vasija Alquímica]] • 📦 [[01 - Campañas/Comunidad del Alba/07 - Inventario/Inventario de la Party|Panel Completo de Inventario de la Party]]

```dataview
TABLE cantidad AS "Cant.", portador AS "Portador", categoria AS "Categoría", rareza AS "Rareza", sintonizacion AS "Sintonización"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND !contains(lower(string(categoria)), "consumible") AND !contains(lower(string(categoria)), "poción") AND !contains(lower(string(categoria)), "pocion")
SORT portador ASC, file.name ASC
```

---

## 🧪 Pociones y Consumibles de la Party (Objetos Físicos)

```dataview
TABLE cantidad AS "Cant.", portador AS "Portador", categoria AS "Categoría", rareza AS "Rareza"
FROM "01 - Campañas/Comunidad del Alba/07 - Inventario"
WHERE tipo = "objeto" AND (contains(lower(string(categoria)), "consumible") OR contains(lower(string(categoria)), "poción") OR contains(lower(string(categoria)), "pocion"))
SORT portador ASC, file.name ASC
```
