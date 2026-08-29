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

const basesDisponibles = Object.keys(fmStock.bases_liquidas || {
  "Agua Fresca": 20, "Agua Salada": 5, "Miel": 2, "Vino": 4, "Cerveza": 4,
  "Vinagre": 2, "Mayonesa": 2, "Aceite": 4, "Ácido": 3, "Veneno Básico": 2
});

const esenciasDisponibles = Object.keys(fmStock.esencias || {
  "Extracto Vital": 8, "Extracto Mutagénico": 2, "Esencia Adaptativa": 4,
  "Esencia Psicoactiva": 16, "Toxina Concentrada": 6, "Polvo Acre": 16,
  "Polvo Inerte": 27, "Polvo Ígneo": 19, "Cristal Cinético": 4,
  "Sales de Choque": 20, "Vitriolo Corrosivo": 4
});

// 1. Nombre de la nueva receta
const nombre = await tp.system.prompt("Nombre de la nueva receta / consumible (ej: Flecha Explosiva):");
if (!nombre || nombre.trim() === "") {
  new Notice("⚠️ Cancelado: Nombre no válido.");
  return;
}
const nombreLimpio = nombre.trim();

// 2. Cantidad producida por lote
const cantProdStr = await tp.system.prompt(
  `¿Cuántas unidades de "${nombreLimpio}" produce CADA crafteo/lote?\n(1 para objeto estándar, o 2+ para lotes múltiples):`,
  "1"
);
if (!cantProdStr) return;
const cantProducida = Math.max(1, parseInt(cantProdStr, 10) || 1);

// 3. Vector Delta de la nueva receta
const delta = {};

// 4. Base líquida requerida (opcional)
const baseOpciones = ["⚪ Ninguna (Sin base líquida)", ...basesDisponibles];
const baseSel = await tp.system.suggester(
  baseOpciones.map(b => b.startsWith("⚪") ? b : `💧 Base Líquida: ${b}`),
  [null, ...basesDisponibles],
  false,
  "Selecciona la Base Líquida requerida:"
);

if (baseSel) {
  const cantBaseStr = await tp.system.prompt(`¿Cuántas unidades de "${baseSel}" se requieren por lote?`, "1");
  if (!cantBaseStr) return;
  const cantBase = Math.max(1, parseInt(cantBaseStr, 10) || 1);
  delta[baseSel] = -cantBase;
}

// 5. Primera Esencia obligatoria
const esencia1 = await tp.system.suggester(
  esenciasDisponibles.map(e => `🧪 Esencia / Polvo: ${e}`),
  esenciasDisponibles,
  false,
  "Selecciona el 1er ingrediente reactivo (Esencia o Polvo):"
);
if (!esencia1) {
  new Notice("⚠️ Cancelado: Toda receta requiere al menos un reactivo de esencia.");
  return;
}

const cantEsencia1Str = await tp.system.prompt(`¿Cuántas unidades de "${esencia1}" se requieren por lote?`, "1");
if (!cantEsencia1Str) return;
const cantEsencia1 = Math.max(1, parseInt(cantEsencia1Str, 10) || 1);
delta[esencia1] = -cantEsencia1;

// 6. Ingredientes adicionales
let agregando = true;
while (agregando) {
  const opcionesExtra = ["✅ Finalizar ingredientes y guardar receta", ...esenciasDisponibles];
  const esenciaExtra = await tp.system.suggester(
    opcionesExtra.map(o => o.startsWith("✅") ? o : `➕ Añadir otro reactivo: ${o}`),
    [null, ...esenciasDisponibles],
    false,
    "¿Deseas añadir otro ingrediente a la fórmula?"
  );

  if (!esenciaExtra) {
    agregando = false;
  } else {
    const cantExtraStr = await tp.system.prompt(`¿Cuántas unidades de "${esenciaExtra}" se requieren por lote?`, "1");
    if (cantExtraStr) {
      const cantExtra = Math.max(1, parseInt(cantExtraStr, 10) || 1);
      delta[esenciaExtra] = (delta[esenciaExtra] || 0) - cantExtra;
    }
  }
}

// Añadir producto final al vector (+cantProducida)
delta[nombreLimpio] = cantProducida;

// 7. Efecto / Descripción
const efecto = await tp.system.prompt(`Descripción o efecto resumido de "${nombreLimpio}":`, "") || "Consumible personalizado.";

// 8. Guardar en Base de Datos de Recetas (Vector Delta)
await app.fileManager.processFrontMatter(recetasFile, (fm) => {
  if (!fm.recetas_alquimia) fm.recetas_alquimia = {};
  fm.recetas_alquimia[nombreLimpio] = {
    descripcion: efecto,
    delta: delta
  };
});

// 9. Guardar en Base de Datos de Stock
await app.fileManager.processFrontMatter(stockFile, (fm) => {
  if (!fm.consumibles) fm.consumibles = {};
  if (fm.consumibles[nombreLimpio] === undefined) {
    fm.consumibles[nombreLimpio] = 0;
  }
});

const listaInsumos = [];
for (const [item, cant] of Object.entries(delta)) {
  if (cant < 0) listaInsumos.push(`${Math.abs(cant)}x ${item}`);
}

new Notice(
  `✨ ¡Receta "${nombreLimpio}" registrada con éxito en formato vectorial!\n• Rendimiento: +${cantProducida}x por lote\n• Insumos: ${listaInsumos.join(" + ") || "Sin coste"}`,
  7000
);
_%>