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

const materias = fmStock.materias_primas || {};
const formulas = fmRecetas.rendimientos_materias || {};

const disponibles = Object.entries(materias).filter(([_, qty]) => Number(qty) > 0);

if (disponibles.length === 0) {
  new Notice("⚠️ No tienes materias primas en stock para procesar.");
  return;
}

const seleccion = await tp.system.suggester(
  disponibles.map(([nombre, qty]) => `🔬 Extraer: ${nombre} (Stock: ${qty})`),
  disponibles.map(([n]) => n),
  false,
  "Selecciona la materia prima que deseas procesar:"
);

if (!seleccion) return;

const maxQty = Number(materias[seleccion]) || 0;
const formulaData = formulas[seleccion] || {};
const formulaDelta = formulaData.delta || formulaData;

// Obtener la esencia primaria que rinde esta materia (primer valor positivo)
let esenciaPrimaria = "Extracto Vital";
for (const [k, v] of Object.entries(formulaDelta)) {
  if (Number(v) > 0) {
    esenciaPrimaria = k;
    break;
  }
}

// 1. Preguntar cuántas materias en bruto gastar
const cantGastarStr = await tp.system.prompt(
  `¿Cuántas unidades de "${seleccion}" vas a procesar?\n(Stock disponible: ${maxQty})`,
  "1"
);
if (!cantGastarStr) return;
const cantGastar = Math.min(maxQty, Math.max(1, parseInt(cantGastarStr, 10) || 1));

// 2. Preguntar el resultado de la tirada de dados
const resultadoTiradaStr = await tp.system.prompt(
  `🎲 Ingresa el resultado total de tu tirada de dados para "${esenciaPrimaria}":\n(¿Cuántas unidades purificadas obtuviste?):`,
  String(cantGastar)
);
if (!resultadoTiradaStr) return;
const resultadoTirada = Math.max(1, parseInt(resultadoTiradaStr, 10) || 1);

// Vector de transformación de extracción
const deltaExtraccion = {
  [seleccion]: -cantGastar,
  [esenciaPrimaria]: resultadoTirada
};

await app.fileManager.processFrontMatter(stockFile, (fm) => {
  const categoriasStock = ["materias_primas", "esencias", "bases_liquidas", "consumibles"];
  
  for (const [item, val] of Object.entries(deltaExtraccion)) {
    let targetCat = null;
    for (const cat of categoriasStock) {
      if (fm[cat] && fm[cat][item] !== undefined) {
        targetCat = cat;
        break;
      }
    }
    if (!targetCat) {
      targetCat = val < 0 ? "materias_primas" : "esencias";
      if (!fm[targetCat]) fm[targetCat] = {};
    }
    fm[targetCat][item] = Math.max(0, (fm[targetCat][item] || 0) + val);
  }

  new Notice(
    `🔬 ¡Extracción Completada!\n• -${cantGastar}x "${seleccion}" gastados\n• +${resultadoTirada}x "${esenciaPrimaria}" añadidos según tu tirada de dados.`,
    6000
  );
});
_%>