<%*
const stockPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md";
const recetasPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Base de Recetas.md";

const stockFile = app.vault.getAbstractFileByPath(stockPath);
const recetasFile = app.vault.getAbstractFileByPath(recetasPath);

if (!stockFile || !recetasFile) {
  new Notice("❌ Error: No se encontraron los archivos de base de datos de alquimia.");
  return;
}

const parseY = tp?.obsidian?.parseYaml || window?.parseYaml || (typeof parseYaml !== "undefined" ? parseYaml : null);
const dv = app.plugins?.plugins?.dataview?.api || window?.DataviewAPI;

const getFrontmatter = async (file) => {
  if (!file) return {};
  if (dv) {
    const page = dv.page(file.path);
    if (page?.file?.frontmatter) return page.file.frontmatter;
    if (page) return page;
  }
  const cache = app.metadataCache?.getFileCache(file);
  if (cache?.frontmatter) return cache.frontmatter;
  if (parseY) {
    try {
      const raw = await app.vault.read(file);
      const m = raw.match(/^---\r?\n([\s\S]+?)\r?\n---/);
      if (m) return parseY(m[1]) || {};
    } catch(e) {}
  }
  return {};
};

const fmStock = await getFrontmatter(stockFile);
const fmRecetas = await getFrontmatter(recetasFile);
const recetas = fmRecetas.recetas_alquimia || {};

// 1. Construir Vector de Inventario Plano (I)
const flatStock = {};
const categorias = ["consumibles", "bases_liquidas", "esencias", "materias_primas"];
for (const cat of categorias) {
  if (fmStock[cat] && typeof fmStock[cat] === "object") {
    for (const [item, cant] of Object.entries(fmStock[cat])) {
      flatStock[item] = Number(cant) || 0;
    }
  }
}

// 2. Helper para normalizar el vector delta de cada receta
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

// 3. Procesar catálogo de recetas mediante álgebra vectorial
const listaRecetas = Object.entries(recetas).map(([nombre, data]) => {
  const delta = extraerDelta(data, nombre);
  let maxLotes = Infinity;
  const faltantes1x = [];
  let prodNombre = nombre;
  let cantPorLote = 1;

  for (const [item, val] of Object.entries(delta)) {
    const num = Number(val) || 0;
    if (num < 0) {
      const req = Math.abs(num);
      const disp = flatStock[item] || 0;
      const pos = Math.floor(disp / req);
      if (pos < maxLotes) maxLotes = pos;
      if (disp < req) {
        faltantes1x.push(`${item} (${disp}/${req})`);
      }
    } else if (num > 0) {
      prodNombre = item;
      cantPorLote = num;
    }
  }

  if (maxLotes === Infinity) maxLotes = 0;
  const totalUnidades = maxLotes * cantPorLote;
  const detalleLote = cantPorLote > 1 ? ` (${cantPorLote} uds/lote)` : "";

  const estado = maxLotes > 0 
    ? `🟢 ${maxLotes} lote(s) = ${totalUnidades} unidad(es)${detalleLote}` 
    : `🔴 Falta: ${faltantes1x.join(", ")}`;

  return {
    nombre: nombre,
    prodNombre: prodNombre,
    cantPorLote: cantPorLote,
    delta: delta,
    maxLotes: maxLotes,
    totalUnidades: totalUnidades,
    display: `${nombre} [${estado}]`
  };
});

if (listaRecetas.length === 0) {
  new Notice("⚠️ No hay recetas registradas en la base de datos.");
  return;
}

const seleccion = await tp.system.suggester(
  listaRecetas.map(r => r.display),
  listaRecetas,
  false,
  "⚗️ Selecciona la receta que deseas sintetizar:"
);

if (!seleccion) return;

if (seleccion.maxLotes <= 0) {
  new Notice(`❌ No tienes suficientes materiales para fabricar ni 1 lote de "${seleccion.nombre}".`, 5000);
  return;
}

const cantStr = await tp.system.prompt(
  `¿Cuántos LOTES de "${seleccion.nombre}" deseas fabricar?\n(1 lote produce ${seleccion.cantPorLote} unidades | Máximo posible: ${seleccion.maxLotes} lotes = ${seleccion.totalUnidades} unidades)`,
  "1"
);

if (!cantStr) return;

const lotes = parseInt(cantStr, 10);
if (isNaN(lotes) || lotes <= 0) {
  new Notice("⚠️ Cantidad no válida.");
  return;
}

// Verificación vectorial estricta
const faltantesTotal = [];
for (const [item, val] of Object.entries(seleccion.delta)) {
  const num = Number(val) || 0;
  if (num < 0) {
    const totalReq = Math.abs(num) * lotes;
    const disp = flatStock[item] || 0;
    if (disp < totalReq) {
      faltantesTotal.push(`${item} (Requieres: ${totalReq}, Tienes: ${disp})`);
    }
  }
}

if (faltantesTotal.length > 0) {
  new Notice(`❌ Materiales insuficientes para fabricar ${lotes} lote(s) de "${seleccion.nombre}":\n• ${faltantesTotal.join("\n• ")}`, 7000);
  return;
}

const unidadesProducidas = lotes * seleccion.cantPorLote;

// Aplicar transformación vectorial en la base de datos: I_new = I + lotes * delta
await app.fileManager.processFrontMatter(stockFile, (fm) => {
  const categoriasStock = ["consumibles", "bases_liquidas", "esencias", "materias_primas"];
  
  for (const [item, val] of Object.entries(seleccion.delta)) {
    const change = Number(val) * lotes;
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
    
    fm[targetCat][item] = Math.max(0, (fm[targetCat][item] || 0) + change);
  }

  new Notice(
    `✨ ¡Crafteo Alquímico Exitoso!\n• +${unidadesProducidas}x "${seleccion.prodNombre}" fabricados\n• ${lotes} lote(s) procesados.`,
    6000
  );
});
_%>