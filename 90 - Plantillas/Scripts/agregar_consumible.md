<%*
const stockFile = app.vault.getAbstractFileByPath("01 - Campañas/Comunidad del Alba/07 - Inventario/Alquimia - Inventario y Stock.md");

if (!stockFile) {
  new Notice("❌ Error: No se encontró la base de datos de stock.");
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

const consumibles = Object.keys(fmStock.consumibles || {});
const opciones = ["✨ Nuevo Consumible Externo / Comprado", ...consumibles.map(c => `🧪 Añadir Unidades: ${c} (Actual: ${fmStock.consumibles[c] || 0})`)];

const seleccion = await tp.system.suggester(
  opciones,
  ["NUEVO", ...consumibles],
  false,
  "Selecciona el consumible:"
);

if (!seleccion) return;

if (seleccion === "NUEVO") {
  const nombre = await tp.system.prompt("Nombre del nuevo consumible:");
  if (!nombre || nombre.trim() === "") return;
  const nombreLimpio = nombre.trim();

  const cantStr = await tp.system.prompt(`¿Cuántas unidades de "${nombreLimpio}" deseas añadir?`, "1");
  const cant = Math.max(1, parseInt(cantStr, 10) || 1);

  await app.fileManager.processFrontMatter(stockFile, (fm) => {
    if (!fm.consumibles) fm.consumibles = {};
    fm.consumibles[nombreLimpio] = (fm.consumibles[nombreLimpio] || 0) + cant;
  });

  new Notice(`🧪 Consumible añadido: +${cant}x "${nombreLimpio}"`, 5000);
} else {
  const cantStr = await tp.system.prompt(`¿Cuántas unidades de "${seleccion}" deseas añadir?`, "1");
  if (!cantStr) return;
  const cant = Math.max(1, parseInt(cantStr, 10) || 1);

  await app.fileManager.processFrontMatter(stockFile, (fm) => {
    if (!fm.consumibles) fm.consumibles = {};
    fm.consumibles[seleccion] = (fm.consumibles[seleccion] || 0) + cant;
  });

  new Notice(`🧪 Stock actualizado: +${cant}x "${seleccion}"`, 5000);
}
_%>