<%*
const activeFile = app.workspace.getActiveFile();
const activePath = activeFile?.path || "";

let targetFile = tp.config.target_file || activeFile;
let propKey = "monedas";

if (activePath.includes("Inventario de la Party")) {
  targetFile = app.vault.getAbstractFileByPath("01 - Campañas/Comunidad del Alba/07 - Inventario/Inventario de la Party.md");
  propKey = "monedas_grupales";
} else if (activePath.includes("Dashboard - Comunidad del Alba")) {
  targetFile = app.vault.getAbstractFileByPath("01 - Campañas/Comunidad del Alba/02 - Personajes/Frater Ren.md");
} else if (activePath.includes("Dashboard - Bilbo Volador")) {
  targetFile = app.vault.getAbstractFileByPath("01 - Campañas/Bilbo Volador/02 - Personajes/Moxy.md");
}

if (!targetFile) {
  new Notice("❌ Error: No se pudo identificar el archivo a modificar.");
  return;
}

const fmData = app.metadataCache.getFileCache(targetFile)?.frontmatter || {};
const monedas = fmData[propKey] || { pc: 0, pp: 0, pe: 0, po: 0, ppt: 0 };
const nombre = fmData.nombre || targetFile.basename;

// 1. Seleccionar tipo de moneda
const opcionesMonedas = [
  `🟡 Oro (PO): ${monedas.po || 0}`,
  `⚪ Plata (PP): ${monedas.pp || 0}`,
  `🟤 Cobre (PC): ${monedas.pc || 0}`,
  `🟢 Electro (PE): ${monedas.pe || 0}`,
  `🔘 Platino (PPT): ${monedas.ppt || 0}`
];

const claveSel = await tp.system.suggester(
  opcionesMonedas,
  ["po", "pp", "pc", "pe", "ppt"],
  false,
  `💰 Monedero (${nombre}) — Selecciona la moneda:`
);

if (!claveSel) return;

const nombreMoneda = {
  po: "Oro (PO)",
  pp: "Plata (PP)",
  pc: "Cobre (PC)",
  pe: "Electro (PE)",
  ppt: "Platino (PPT)"
}[claveSel];

const actual = Number(monedas[claveSel]) || 0;

// 2. Seleccionar acción
const accion = await tp.system.suggester(
  [
    `➕ Añadir a ${nombreMoneda} (Recompensa / Venta / Saqueo)`,
    `➖ Gastar de ${nombreMoneda} (Compra / Pago / Gasto)`,
    `✏️ Establecer cantidad exacta de ${nombreMoneda}`
  ],
  ["sumar", "restar", "fijo"],
  false,
  `¿Qué operación deseas realizar con ${nombreMoneda}? (Saldo actual: ${actual})`
);

if (!accion) return;

// 3. Prompt de cantidad
let promptTexto = "";
if (accion === "sumar") promptTexto = `¿Cuántas monedas de ${nombreMoneda} deseas AÑADIR?`;
if (accion === "restar") promptTexto = `¿Cuántas monedas de ${nombreMoneda} deseas GASTAR?`;
if (accion === "fijo") promptTexto = `Nuevo saldo total de ${nombreMoneda}:`;

const cantStr = await tp.system.prompt(promptTexto, accion === "fijo" ? String(actual) : "10");
if (!cantStr) return;

const cantNum = parseInt(cantStr, 10);
if (isNaN(cantNum) || cantNum < 0) {
  new Notice("⚠️ Cantidad no válida.");
  return;
}

let nuevoSaldo = actual;
if (accion === "sumar") nuevoSaldo = actual + cantNum;
if (accion === "restar") {
  if (cantNum > actual) {
    new Notice(`⚠️ No tienes suficiente ${nombreMoneda}. (Saldo actual: ${actual}, intento de gasto: ${cantNum})`, 5000);
    return;
  }
  nuevoSaldo = actual - cantNum;
}
if (accion === "fijo") nuevoSaldo = cantNum;

await app.fileManager.processFrontMatter(targetFile, (fm) => {
  if (!fm[propKey]) fm[propKey] = { pc: 0, pp: 0, pe: 0, po: 0, ppt: 0 };
  fm[propKey][claveSel] = nuevoSaldo;
  new Notice(`💰 ¡Monedero (${nombre}) actualizado!\n${nombreMoneda}: ${actual} ➔ ${nuevoSaldo}`, 5000);
});
_%>