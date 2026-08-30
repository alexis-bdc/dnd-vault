<%*
const stockPath = "01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md";
const stockFile = app.vault.getAbstractFileByPath(stockPath);

if (!stockFile) {
  new Notice("❌ Error: No se encontró la base de datos de stock alquímico.");
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
const esencias = fmStock.esencias || {};

const listaEsencias = Object.keys(esencias);
const opciones = [
  "✨ Registrar NUEVA Esencia / Polvo",
  ...listaEsencias.map(e => `🧪 ${e} (Stock actual: ${esencias[e] || 0})`)
];
const valores = ["NUEVA", ...listaEsencias];

const seleccion = await tp.system.suggester(
  opciones,
  valores,
  false,
  "🧪 Selecciona la Esencia o Polvo a modificar:"
);

if (!seleccion) return;

let nombreEsencia = seleccion;
let stockActual = 0;

if (seleccion === "NUEVA") {
  const nuevoNombre = await tp.system.prompt("Nombre de la nueva esencia o polvo (ej: Esencia Astral):");
  if (!nuevoNombre || nuevoNombre.trim() === "") {
    new Notice("⚠️ Cancelado: Nombre no válido.");
    return;
  }
  nombreEsencia = nuevoNombre.trim();
  stockActual = 0;
} else {
  stockActual = Number(esencias[nombreEsencia]) || 0;
}

// Elegir operación
const accion = await tp.system.suggester(
  [
    `➕ Añadir stock a "${nombreEsencia}" (Hallazgo / Compra / Recompensa)`,
    `➖ Gastar / Reducir stock de "${nombreEsencia}"`,
    `✏️ Establecer cantidad fija exacta (Saldo actual: ${stockActual})`
  ],
  ["sumar", "restar", "fijo"],
  false,
  `¿Qué deseas hacer con "${nombreEsencia}"?`
);

if (!accion) return;

let promptTexto = "";
if (accion === "sumar") promptTexto = `¿Cuántas unidades de "${nombreEsencia}" deseas AÑADIR?`;
if (accion === "restar") promptTexto = `¿Cuántas unidades de "${nombreEsencia}" deseas RESTAR?`;
if (accion === "fijo") promptTexto = `Nuevo saldo total para "${nombreEsencia}":`;

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
  if (!fm.esencias) fm.esencias = {};
  fm.esencias[nombreEsencia] = nuevoSaldo;
  new Notice(`🧪 ¡Esencias actualizadas!\n"${nombreEsencia}": ${stockActual} ➔ ${nuevoSaldo}`, 5000);
});
_%>
