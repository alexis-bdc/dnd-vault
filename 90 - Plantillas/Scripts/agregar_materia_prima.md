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
const materias = fmStock.materias_primas || {};

const conocidas = Object.keys(materias);
const opciones = [
  "✨ Registrar NUEVA Materia Prima en Catálogo",
  ...conocidas.map(c => `🌿 ${c} (Stock actual: ${materias[c] || 0})`)
];

const seleccion = await tp.system.suggester(
  opciones,
  ["NUEVA", ...conocidas],
  false,
  "🌿 Selecciona la Materia Prima a gestionar:"
);

if (!seleccion) return;

if (seleccion === "NUEVA") {
  const nombre = await tp.system.prompt("Nombre de la nueva materia prima (ej: Raíz de Mandrágora):");
  if (!nombre || nombre.trim() === "") return;
  const nombreLimpio = nombre.trim();

  const cantStr = await tp.system.prompt(`¿Cuántas unidades de "${nombreLimpio}" has recolectado?`, "1");
  const cant = Math.max(1, parseInt(cantStr, 10) || 1);

  const esenciasDisponibles = Object.keys(fmStock.esencias || {
    "Extracto Vital": 1, "Polvo Inerte": 1, "Toxina Concentrada": 1, "Polvo Acre": 1
  });

  const esencia1 = await tp.system.suggester(
    esenciasDisponibles.map(e => `🧪 Rendimiento Principal: ${e}`),
    esenciasDisponibles,
    false,
    "¿Qué reactivo purificado rinde al extraerse?"
  );
  if (!esencia1) return;

  const rendimiento = {
    delta: {
      [nombreLimpio]: -1,
      [esencia1]: 1,
      "Polvo Inerte": 1
    }
  };

  await app.fileManager.processFrontMatter(recetasFile, (fm) => {
    if (!fm.rendimientos_materias) fm.rendimientos_materias = {};
    fm.rendimientos_materias[nombreLimpio] = rendimiento;
  });

  await app.fileManager.processFrontMatter(stockFile, (fm) => {
    if (!fm.materias_primas) fm.materias_primas = {};
    fm.materias_primas[nombreLimpio] = (fm.materias_primas[nombreLimpio] || 0) + cant;
  });

  new Notice(`🌿 Nueva materia prima registrada: "${nombreLimpio}" (+${cant} en stock)`, 6000);
} else {
  const stockActual = Number(materias[seleccion]) || 0;
  const accion = await tp.system.suggester(
    [
      `➕ Añadir stock a "${seleccion}" (Recolección / Botín / Compra)`,
      `➖ Gastar / Descartar stock de "${seleccion}"`,
      `✏️ Establecer cantidad fija exacta (Saldo actual: ${stockActual})`
    ],
    ["sumar", "restar", "fijo"],
    false,
    `¿Qué deseas hacer con "${seleccion}"?`
  );

  if (!accion) return;

  let promptTexto = "";
  if (accion === "sumar") promptTexto = `¿Cuántas unidades de "${seleccion}" deseas AÑADIR?`;
  if (accion === "restar") promptTexto = `¿Cuántas unidades de "${seleccion}" deseas RESTAR?`;
  if (accion === "fijo") promptTexto = `Nuevo saldo total de "${seleccion}":`;

  const cantStr = await tp.system.prompt(promptTexto, accion === "fijo" ? String(stockActual) : "1");
  if (!cantStr) return;

  const cantNum = parseInt(cantStr, 10);
  if (isNaN(cantNum) || cantNum < 0) {
    new Notice("⚠️ Cantidad no válida.");
    return;
  }

  let nuevoSaldo = stockActual;
  if (accion === "sumar") nuevoSaldo = stockActual + cantNum;
  if (accion === "restar") {
    if (cantNum > stockActual) {
      new Notice(`⚠️ No puedes restar ${cantNum} porque solo tienes ${stockActual}. Saldo fijado en 0.`);
      nuevoSaldo = 0;
    } else {
      nuevoSaldo = stockActual - cantNum;
    }
  }
  if (accion === "fijo") nuevoSaldo = cantNum;

  await app.fileManager.processFrontMatter(stockFile, (fm) => {
    if (!fm.materias_primas) fm.materias_primas = {};
    fm.materias_primas[seleccion] = nuevoSaldo;
    new Notice(`🌿 Stock actualizado:\n"${seleccion}": ${stockActual} ➔ ${nuevoSaldo}`, 5000);
  });
}
_%>