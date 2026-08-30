---
tipo: objeto
cantidad: 1
campaña: "Comunidad del Alba"
nombre: "Laboratorio Alquímico Portátil"
categoria: "Laboratorio / Estación de Crafteo"
rareza: Especial
portador: "[[01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren|Frater Ren]]"
ubicacion_fisica: "Dentro del [[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Agujero Portatil|Agujero Portátil]]"
bbdd_stock: "[[01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock|Alquimia - Inventario y Stock]]"
bbdd_recetas: "[[01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Base de Recetas|Alquimia - Base de Recetas]]"
tags:
  - dnd/item
  - dnd/alquimia
  - dnd/comunidad-del-alba
---

# ⚗️ Laboratorio Alquímico Portátil (Panel de Control)

> [!info] **Estación de Alquimia Táctica de Frater Ren**
> **Alquimista:** `VIEW[{portador}][text]` | **Ubicación:** Desplegado en el **[[01 - Campañas/Comunidad del Alba/07 - Inventario/Objetos/Agujero Portatil|Agujero Portátil]]**
> **Bases de Datos Vinculadas:** 📦 [[01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock|Alquimia - Inventario y Stock]] • 📜 [[01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Base de Recetas|Alquimia - Base de Recetas]]

---

## 🎽 Bandolera Táctica (Acceso Rápido en Combate — Acción Adicional)

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

  // Col 2: Selector dinámico
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

  // Col 3: Botón de Uso Directo
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

      fm.consumibles[equipped] -= 1;
      const rest = fm.consumibles[equipped];

      if (!fm.bandolera) fm.bandolera = {};
      fm.bandolera[slotKey] = "Vacío";

      new Notice("⚡ ¡Usaste 1x \"" + equipped + "\" de la Ranura " + i + "!\n🎽 La Ranura " + i + " ahora está VACÍA. (Stock restante: " + rest + ")", 5000);
    });
  };
}
```

---

## 🛠️ Panel de Alquimia Táctica (Acciones Rápidas)

```meta-bind-button
label: ⚗️ Crafteo Rápido / Síntesis
icon: flask-conical
style: primary
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/craftear_alquimia.md
```
```meta-bind-button
label: 🔬 Procesar Materias Primas
icon: microchip
style: primary
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/procesar_materias.md
```
```meta-bind-button
label: 🌿 Registrar / Añadir Materia Prima
icon: leaf
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/agregar_materia_prima.md
```
```meta-bind-button
label: 🧪 Ajustar / Añadir Esencias
icon: flask-round
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/ajustar_esencias.md
```
```meta-bind-button
label: 📦 Añadir Consumible / Poción
icon: package-plus
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/agregar_consumible.md
```
```meta-bind-button
label: 📜 Registrar Nueva Receta
icon: scroll
style: default
actions:
  - type: runTemplaterFile
    templateFile: 90 - Plantillas/Scripts/agregar_receta.md
```

---

## 🧪 1. Consumibles, Pociones y Artificios en Stock

```dataviewjs
const stockPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md";
const stockFile = app.vault.getAbstractFileByPath(stockPath);
const pStock = dv.page(stockPath);
const fmStock = (stockFile ? app.metadataCache.getFileCache(stockFile)?.frontmatter : null) || pStock?.file?.frontmatter || pStock || {};
const consumibles = fmStock.consumibles || {};

const container = dv.el("div", "");
container.setAttribute("contenteditable", "false");
container.addEventListener("click", (e) => e.stopPropagation());
container.addEventListener("mousedown", (e) => e.stopPropagation());
container.addEventListener("dblclick", (e) => e.stopPropagation());

const table = container.createEl("table", { cls: "dataview table-view-table" });
const thead = table.createEl("thead");
const hRow = thead.createEl("tr");
["Consumible / Preparado", "Stock Actual", "Ajustar Stock", "Acción Rápida"].forEach(text => {
  hRow.createEl("th", { text, cls: "text-left" });
});

const tbody = table.createEl("tbody");

for (const [nombre, cant] of Object.entries(consumibles)) {
  const row = tbody.createEl("tr");
  
  // Col 1: Nombre
  const tdName = row.createEl("td");
  tdName.createEl("strong", { text: nombre });
  
  // Col 2: Stock
  const tdStock = row.createEl("td", { cls: "text-center whitespace-nowrap" });
  const stockVal = Number(cant) || 0;
  const stockSpan = tdStock.createEl("span", { text: stockVal.toString() });
  stockSpan.style.fontWeight = "bold";
  stockSpan.style.color = stockVal > 0 ? "var(--text-accent, #38bdf8)" : "var(--text-muted, #94a3b8)";
  
  // Col 3: Ajustes (+ / -)
  const tdAdj = row.createEl("td", { cls: "text-center whitespace-nowrap" });
  const btnMinus = tdAdj.createEl("button", { text: "➖", cls: "btn-sm" });
  btnMinus.style.marginRight = "4px";
  btnMinus.style.cursor = "pointer";
  btnMinus.onclick = async () => {
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.consumibles) fm.consumibles = {};
      fm.consumibles[nombre] = Math.max(0, (fm.consumibles[nombre] || 0) - 1);
    });
  };

  const btnPlus = tdAdj.createEl("button", { text: "➕", cls: "btn-sm" });
  btnPlus.style.cursor = "pointer";
  btnPlus.onclick = async () => {
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.consumibles) fm.consumibles = {};
      fm.consumibles[nombre] = (fm.consumibles[nombre] || 0) + 1;
    });
  };

  // Col 4: Botón Usar 1x
  const tdUse = row.createEl("td", { cls: "text-center" });
  const btnUse = tdUse.createEl("button", { text: "⚡ Usar 1x", cls: "mod-cta btn-sm" });
  btnUse.style.cursor = stockVal > 0 ? "pointer" : "not-allowed";
  btnUse.disabled = stockVal <= 0;
  btnUse.onclick = async () => {
    if (stockVal <= 0 || !stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.consumibles || !fm.consumibles[nombre] || fm.consumibles[nombre] <= 0) return;
      fm.consumibles[nombre] -= 1;
      new Notice(`⚡ Usaste 1x "${nombre}". Restantes: ${fm.consumibles[nombre]}`);
    });
  };
}
```

---

## 📜 2. Recetario de Alquimia Táctica (Catálogo Maestro)

```dataviewjs
const recPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Base de Recetas.md";
const stockPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md";

const recFile = app.vault.getAbstractFileByPath(recPath);
const stockFile = app.vault.getAbstractFileByPath(stockPath);

const pRec = dv.page(recPath);
const pStock = dv.page(stockPath);

const fmRec = (recFile ? app.metadataCache.getFileCache(recFile)?.frontmatter : null) || pRec?.file?.frontmatter || pRec || {};
const fmStock = (stockFile ? app.metadataCache.getFileCache(stockFile)?.frontmatter : null) || pStock?.file?.frontmatter || pStock || {};

const recetas = fmRec.recetas_alquimia || {};

// 1. Vector de Inventario Plano (I)
const flatStock = {};
const categoriasStock = ["consumibles", "bases_liquidas", "esencias", "materias_primas"];
for (const cat of categoriasStock) {
  if (fmStock[cat] && typeof fmStock[cat] === "object") {
    for (const [k, v] of Object.entries(fmStock[cat])) {
      flatStock[k] = Number(v) || 0;
    }
  }
}

// 2. Normalizar delta
function extraerDelta(data, nombre) {
  if (data.delta && typeof data.delta === "object") return data.delta;
  const d = {};
  if (data.costes?.bases_liquidas) {
    for (const [b, c] of Object.entries(data.costes.bases_liquidas)) d[b] = -(Number(c) || 1);
  }
  if (data.costes?.esencias) {
    for (const [e, c] of Object.entries(data.costes.esencias)) d[e] = -(Number(c) || 1);
  }
  const salida = data.salida || nombre;
  const cant = Math.max(1, Number(data.cantidad_producida) || 1);
  d[salida] = cant;
  return d;
}

const container = dv.el("div", "");
container.setAttribute("contenteditable", "false");
container.addEventListener("click", (e) => e.stopPropagation());
container.addEventListener("mousedown", (e) => e.stopPropagation());
container.addEventListener("dblclick", (e) => e.stopPropagation());

const table = container.createEl("table", { cls: "dataview table-view-table" });
const thead = table.createEl("thead");
const hRow = thead.createEl("tr");
["Receta / Producto", "Lote", "Insumos Requeridos (ΔI < 0)", "Estado / Disponibilidad", "Efecto / Reglas", "Crafteo Directo"].forEach(text => {
  hRow.createEl("th", { text, cls: "text-left" });
});

const tbody = table.createEl("tbody");

for (const [nombre, data] of Object.entries(recetas)) {
  const delta = extraerDelta(data, nombre);
  let maxLotes = Infinity;
  const faltantes = [];
  const insumosText = [];
  let prodNombre = nombre;
  let cantPorLote = 1;

  for (const [item, val] of Object.entries(delta)) {
    const num = Number(val) || 0;
    if (num < 0) {
      const req = Math.abs(num);
      insumosText.push(`${req}x ${item}`);
      const disp = flatStock[item] || 0;
      const pos = Math.floor(disp / req);
      if (pos < maxLotes) maxLotes = pos;
      if (disp < req) faltantes.push(`${item} (${disp}/${req})`);
    } else if (num > 0) {
      prodNombre = item;
      cantPorLote = num;
    }
  }

  if (maxLotes === Infinity) maxLotes = 0;

  const row = tbody.createEl("tr");

  // Col 1: Receta
  const tdName = row.createEl("td");
  tdName.createEl("strong", { text: nombre });

  // Col 2: Lote
  const tdLote = row.createEl("td", { cls: "text-center whitespace-nowrap" });
  tdLote.createEl("span", { text: cantPorLote > 1 ? `⚡ ${cantPorLote}x` : "1x" });

  // Col 3: Insumos
  const tdCost = row.createEl("td");
  tdCost.createEl("span", { text: insumosText.join(" + ") || "⚪ Sin insumos" });

  // Col 4: Estado / Disponibilidad
  const tdStatus = row.createEl("td", { cls: "whitespace-nowrap" });
  const statusSpan = tdStatus.createEl("span", {
    text: maxLotes > 0 ? `🟢 ${maxLotes} lote(s)` : `🔴 Falta: ${faltantes.join(", ")}`
  });
  statusSpan.style.color = maxLotes > 0 ? "var(--text-success, #22c55e)" : "var(--text-error, #ef4444)";

  // Col 5: Efecto
  const tdDesc = row.createEl("td");
  tdDesc.createEl("span", { text: data.descripcion || "" });

  // Col 6: Botón Crafteo 1x (Vector Delta: I += 1 * delta)
  const tdAction = row.createEl("td", { cls: "text-center" });
  const btnCraft = tdAction.createEl("button", { text: "⚗️ Craftear 1x", cls: "btn-sm" });
  btnCraft.style.cursor = maxLotes > 0 ? "pointer" : "not-allowed";
  btnCraft.disabled = maxLotes <= 0;

  btnCraft.onclick = async () => {
    if (maxLotes <= 0 || !stockFile) return;

    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      for (const [item, val] of Object.entries(delta)) {
        let targetCat = null;
        for (const cat of categoriasStock) {
          if (fm[cat] && fm[cat][item] !== undefined) {
            targetCat = cat;
            break;
          }
        }
        if (!targetCat) {
          targetCat = "consumibles";
          if (!fm[targetCat]) fm[targetCat] = {};
        }
        fm[targetCat][item] = Math.max(0, (fm[targetCat][item] || 0) + Number(val));
      }

      new Notice(`✨ ¡Has sintetizado ${cantPorLote}x "${prodNombre}"!`, 5000);
    });
  };
}
```

---

## 💧 3. Reactivos: Bases Líquidas y Esencias Purificadas

```dataviewjs
const stockPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md";
const stockFile = app.vault.getAbstractFileByPath(stockPath);
const pStock = dv.page(stockPath);
const fmStock = (stockFile ? app.metadataCache.getFileCache(stockFile)?.frontmatter : null) || pStock?.file?.frontmatter || pStock || {};

const bases = fmStock.bases_liquidas || {};
const esencias = fmStock.esencias || {};

const container = dv.el("div", "");
container.setAttribute("contenteditable", "false");
container.addEventListener("click", (e) => e.stopPropagation());
container.addEventListener("mousedown", (e) => e.stopPropagation());
container.addEventListener("dblclick", (e) => e.stopPropagation());

const grid = container.createEl("div");
grid.style.display = "grid";
grid.style.gridTemplateColumns = "1fr 1fr";
grid.style.gap = "16px";

// Tabla 1: Bases Líquidas
const divBases = grid.createEl("div");
divBases.createEl("h4", { text: "💧 Bases Líquidas (Vasija Alquímica)" });
const tBases = divBases.createEl("table", { cls: "dataview table-view-table" });
const thB = tBases.createEl("thead").createEl("tr");
["Base Líquida", "Stock", "Ajustar"].forEach(text => thB.createEl("th", { text, cls: "text-left" }));
const tbB = tBases.createEl("tbody");
for (const [b, cant] of Object.entries(bases)) {
  const r = tbB.createEl("tr");
  r.createEl("td").createEl("strong", { text: b });
  const tdS = r.createEl("td", { cls: "text-center whitespace-nowrap" });
  const sp = tdS.createEl("span", { text: String(cant) });
  sp.style.fontWeight = "bold";
  sp.style.color = Number(cant) > 0 ? "var(--text-accent, #38bdf8)" : "var(--text-muted, #94a3b8)";

  const tdAdj = r.createEl("td", { cls: "text-center whitespace-nowrap" });
  const btnMinus = tdAdj.createEl("button", { text: "➖", cls: "btn-sm" });
  btnMinus.style.marginRight = "4px";
  btnMinus.style.cursor = "pointer";
  btnMinus.onclick = async () => {
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.bases_liquidas) fm.bases_liquidas = {};
      fm.bases_liquidas[b] = Math.max(0, (fm.bases_liquidas[b] || 0) - 1);
    });
  };

  const btnPlus = tdAdj.createEl("button", { text: "➕", cls: "btn-sm" });
  btnPlus.style.cursor = "pointer";
  btnPlus.onclick = async () => {
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.bases_liquidas) fm.bases_liquidas = {};
      fm.bases_liquidas[b] = (fm.bases_liquidas[b] || 0) + 1;
    });
  };
}

// Tabla 2: Esencias Purificadas
const divEsencias = grid.createEl("div");
divEsencias.createEl("h4", { text: "🧪 Esencias y Polvos Purificados" });
const tEsencias = divEsencias.createEl("table", { cls: "dataview table-view-table" });
const thE = tEsencias.createEl("thead").createEl("tr");
["Esencia / Reactivo", "Stock", "Ajustar"].forEach(text => thE.createEl("th", { text, cls: "text-left" }));
const tbE = tEsencias.createEl("tbody");
for (const [e, cant] of Object.entries(esencias)) {
  const r = tbE.createEl("tr");
  r.createEl("td").createEl("strong", { text: e });
  const tdS = r.createEl("td", { cls: "text-center whitespace-nowrap" });
  const sp = tdS.createEl("span", { text: String(cant) });
  sp.style.fontWeight = "bold";
  sp.style.color = Number(cant) > 0 ? "var(--text-accent, #38bdf8)" : "var(--text-muted, #94a3b8)";

  const tdAdj = r.createEl("td", { cls: "text-center whitespace-nowrap" });
  const btnMinus = tdAdj.createEl("button", { text: "➖", cls: "btn-sm" });
  btnMinus.style.marginRight = "4px";
  btnMinus.style.cursor = "pointer";
  btnMinus.onclick = async () => {
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.esencias) fm.esencias = {};
      fm.esencias[e] = Math.max(0, (fm.esencias[e] || 0) - 1);
    });
  };

  const btnPlus = tdAdj.createEl("button", { text: "➕", cls: "btn-sm" });
  btnPlus.style.cursor = "pointer";
  btnPlus.onclick = async () => {
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.esencias) fm.esencias = {};
      fm.esencias[e] = (fm.esencias[e] || 0) + 1;
    });
  };
}
```

---

## 🌿 4. Materias Primas en Bruto y Extracción por Tirada de Dados

```dataviewjs
const recPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Base de Recetas.md";
const stockPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md";

const recFile = app.vault.getAbstractFileByPath(recPath);
const stockFile = app.vault.getAbstractFileByPath(stockPath);

const pRec = dv.page(recPath);
const pStock = dv.page(stockPath);

const fmRec = (recFile ? app.metadataCache.getFileCache(recFile)?.frontmatter : null) || pRec?.file?.frontmatter || pRec || {};
const fmStock = (stockFile ? app.metadataCache.getFileCache(stockFile)?.frontmatter : null) || pStock?.file?.frontmatter || pStock || {};

const materias = fmStock.materias_primas || {};
const formulas = fmRec.rendimientos_materias || {};

const container = dv.el("div", "");
container.setAttribute("contenteditable", "false");
container.addEventListener("click", (e) => e.stopPropagation());
container.addEventListener("mousedown", (e) => e.stopPropagation());
container.addEventListener("dblclick", (e) => e.stopPropagation());

const table = container.createEl("table", { cls: "dataview table-view-table" });
const thead = table.createEl("thead");
const hRow = thead.createEl("tr");
["Materia Prima", "Stock en Bruto", "Añadir / Quitar", "Esencia Producida", "Resultado Tirada (Uds)", "Extracción"].forEach(text => {
  hRow.createEl("th", { text, cls: "text-left" });
});

const tbody = table.createEl("tbody");

for (const [mat, cant] of Object.entries(materias)) {
  const stockVal = Number(cant) || 0;
  const formulaData = formulas[mat] || {};
  const formulaDelta = formulaData.delta || formulaData;
  let primaryEssence = "Esencia Alquímica";
  for (const [k, v] of Object.entries(formulaDelta)) {
    if (Number(v) > 0) {
      primaryEssence = k;
      break;
    }
  }

  const row = tbody.createEl("tr");

  // Col 1: Nombre
  const tdName = row.createEl("td");
  tdName.createEl("strong", { text: mat });

  // Col 2: Stock
  const tdStock = row.createEl("td", { cls: "text-center whitespace-nowrap" });
  const spStock = tdStock.createEl("span", { text: String(stockVal) });
  spStock.style.fontWeight = "bold";
  spStock.style.color = stockVal > 0 ? "var(--text-accent, #38bdf8)" : "var(--text-muted, #94a3b8)";

  // Col 3: Ajuste Rápido (+ / -)
  const tdAdj = row.createEl("td", { cls: "text-center whitespace-nowrap" });
  const btnMinus = tdAdj.createEl("button", { text: "➖", cls: "btn-sm" });
  btnMinus.style.marginRight = "4px";
  btnMinus.style.cursor = "pointer";
  btnMinus.onclick = async () => {
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.materias_primas) fm.materias_primas = {};
      fm.materias_primas[mat] = Math.max(0, (fm.materias_primas[mat] || 0) - 1);
    });
  };

  const btnPlus = tdAdj.createEl("button", { text: "➕", cls: "btn-sm" });
  btnPlus.style.cursor = "pointer";
  btnPlus.onclick = async () => {
    if (!stockFile) return;
    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.materias_primas) fm.materias_primas = {};
      fm.materias_primas[mat] = (fm.materias_primas[mat] || 0) + 1;
    });
  };

  // Col 4: Esencia
  const tdEssence = row.createEl("td");
  tdEssence.createEl("span", { text: "🧪 " + primaryEssence });

  // Col 5: Campo de llenado para resultado de dados
  const tdInput = row.createEl("td", { cls: "text-center whitespace-nowrap" });
  const inputQty = tdInput.createEl("input", {
    type: "number",
    value: "1",
    cls: "input-sm"
  });
  inputQty.style.width = "70px";
  inputQty.style.textAlign = "center";
  inputQty.style.padding = "4px 8px";
  inputQty.style.borderRadius = "4px";
  inputQty.style.border = "1px solid var(--background-modifier-border, #475569)";
  inputQty.min = "1";

  // Col 6: Botón Extraer 1x
  const tdAction = row.createEl("td", { cls: "text-center" });
  const btnExtract = tdAction.createEl("button", { text: "🔬 Extraer 1x", cls: "mod-cta btn-sm" });
  btnExtract.style.cursor = stockVal > 0 ? "pointer" : "not-allowed";
  btnExtract.disabled = stockVal <= 0;

  btnExtract.onclick = async () => {
    if (stockVal <= 0 || !stockFile) return;
    const gained = Math.max(1, parseInt(inputQty.value, 10) || 1);

    await app.fileManager.processFrontMatter(stockFile, (fm) => {
      if (!fm.materias_primas || !fm.materias_primas[mat] || fm.materias_primas[mat] <= 0) return;
      if (!fm.esencias) fm.esencias = {};

      fm.materias_primas[mat] -= 1;
      fm.esencias[primaryEssence] = (fm.esencias[primaryEssence] || 0) + gained;

      new Notice(`🔬 ¡Extracción completada!\n• -1x "${mat}"\n• +${gained}x "${primaryEssence}" (según tirada de dados)`, 5000);
    });
  };
}
```
