// Reloj día/noche en tiempo real + control de hambre de la party. Uso:  ```dataviewjs  await dv.view("90 - Plantillas/Scripts/reloj-dia")  ```
// Estado en el frontmatter del dashboard:
//   reloj_horas  = horas de juego desde el día 1 a las 00:00
//   reloj_inicio = ms reales en que se pulsó ▶ (0 = pausado)
//   hambre_hasta = última hora de juego ya cobrada en hambre (evita cobrar dos veces con varios paneles abiertos)
// Hambre en el frontmatter de cada PJ (tipo: pj, estado Activo) de la campaña: campo `hambre` 0–10.
const MIN_REALES_POR_HORA = 5;
const MS_POR_HORA = MIN_REALES_POR_HORA * 60 * 1000;
const HAMBRE_MAX = 10;
const HAMBRE_AL_DORMIR = 4; // dormir 8 h cuesta 4, no 8
const COMIDAS = [
  ["Manzana / zanahoria / baya", 2], ["Carne o pescado crudo", 1], ["Pan", 3], ["Carne o pescado cocinado", 4],
  ["Estofado", 6], ["Tarta de calabaza", 5], ["Carne podrida", 1], ["Manzana dorada", 4], ["Zanahoria dorada", 4],
];

const cur = dv.current();
const file = app.vault.getAbstractFileByPath(cur.file.path);
const raiz = cur.file.folder.split("/").slice(0, 2).join("/");
const fm = app.metadataCache.getFileCache(file)?.frontmatter ?? {};
let base = Number(fm.reloj_horas ?? 7); // por defecto: día 1, 07:00
let inicio = Number(fm.reloj_inicio || 0);

const ahora = () => base + (inicio ? (Date.now() - inicio) / MS_POR_HORA : 0);
const fase = (h) =>
  h >= 6 && h < 7 ? "🌅 Amanecer" : h >= 7 && h < 18 ? "☀️ Día" : h >= 18 && h < 19 ? "🌇 Atardecer" : "🌙 Noche";
// De noche se tira aparición cada 2 h despiertos: a las 19, 21, 23, 01, 03, 05.
const tocaTirada = (h) => fase(h) === "🌙 Noche" && h % 2 === 1;

// --- Hambre ---
const pjs = dv.pages(`"${raiz}"`)
  .where((p) => p.tipo === "pj" && (p.estado ?? "Activo") === "Activo")
  .sort((p) => p.file.name)
  .map((p) => app.vault.getAbstractFileByPath(p.file.path)).array();
const leerHambre = (f) => {
  const v = Number(app.metadataCache.getFileCache(f)?.frontmatter?.hambre);
  return Number.isFinite(v) ? Math.min(HAMBRE_MAX, Math.max(0, Math.floor(v))) : HAMBRE_MAX;
};
const estadoHambre = (v) =>
  v >= 8 ? ["Saciado", "DG curan su máximo"] : v >= 4 ? ["Normal", "DG: tirada normal"] :
  v >= 1 ? ["Hambriento", "DG: mitad de la tirada · desv. CON"] : ["Inanición", "Sin DG · agotamiento cada 4 h"];

const sumarHambre = async (f, delta) => {
  let antes, despues;
  await app.fileManager.processFrontMatter(f, (x) => {
    antes = Number.isFinite(Number(x.hambre)) ? Number(x.hambre) : HAMBRE_MAX;
    despues = Math.min(HAMBRE_MAX, Math.max(0, antes + delta));
    x.hambre = despues;
  });
  if (estadoHambre(despues)[0] !== estadoHambre(antes)[0] && despues < antes)
    new Notice(`🍖 ${f.basename}: ${estadoHambre(despues)[0]} (${despues})`);
};
const cobrarATodos = (n) => Promise.all(pjs.map((f) => sumarHambre(f, -n)));

// Cobra 1 de hambre por cada hora entera que haya pasado desde hambre_hasta. Lee y escribe en la misma operación.
let cobrando = false;
const sincronizarHambre = async () => {
  if (cobrando) return;
  cobrando = true;
  try {
    const objetivo = Math.floor(ahora());
    let n = 0;
    await app.fileManager.processFrontMatter(file, (x) => {
      const hasta = Number.isFinite(Number(x.hambre_hasta)) ? Number(x.hambre_hasta) : objetivo;
      n = Math.max(0, objetivo - hasta);
      x.hambre_hasta = Math.max(hasta, objetivo); // retroceder el reloj no devuelve hambre ni la cobra dos veces
    });
    if (n > 0) await cobrarATodos(n);
  } finally {
    cobrando = false;
  }
};

// --- Reloj ---
const guardar = async (total, corriendo) => {
  base = Math.max(0, total);
  inicio = corriendo ? Date.now() : 0;
  await app.fileManager.processFrontMatter(file, (f) => {
    f.reloj_horas = Math.round(base * 1000) / 1000;
    f.reloj_inicio = inicio;
  });
  pintar();
};
const avanzar = async (h) => {
  await guardar(ahora() + h, !!inicio);
  await sincronizarHambre();
};
const dormir = async () => {
  await sincronizarHambre(); // cobra lo pendiente antes de acostarse
  const fin = ahora() + 8;
  await app.fileManager.processFrontMatter(file, (x) => { x.hambre_hasta = Math.floor(fin); });
  await cobrarATodos(HAMBRE_AL_DORMIR);
  await guardar(fin, !!inicio);
};

// --- UI ---
const box = dv.container.createDiv();
box.style.cssText = "border:1px solid var(--background-modifier-border);border-radius:8px;padding:12px;display:flex;flex-direction:column;gap:8px;";
const reloj = box.createDiv();
reloj.style.cssText = "font-size:1.4em;font-weight:600;";
const sub = box.createDiv();
sub.style.cssText = "color:var(--text-muted);";
const fila = box.createDiv();
fila.style.cssText = "display:flex;flex-wrap:wrap;gap:6px;align-items:center;";

const boton = (padre, txt, fn) => {
  const b = padre.createEl("button", { text: txt });
  b.onclick = fn;
  return b;
};
const bPlay = boton(fila, "", () => guardar(ahora(), !inicio));
boton(fila, "+1 h", () => avanzar(1));
boton(fila, "☕ Descanso corto (1 h)", () => avanzar(1));
boton(fila, `😴 Dormir 8 h (−${HAMBRE_AL_DORMIR} 🍖)`, dormir);
const inp = fila.createEl("input", { type: "number", value: "2", attr: { step: "0.5", "aria-label": "Horas a avanzar" } });
inp.style.width = "5em";
boton(fila, "Avanzar h", () => {
  const x = Number(inp.value);
  if (Number.isFinite(x) && x !== 0) avanzar(x);
});

// Tabla de hambre: una fila por PJ, construida una vez y actualizada cada segundo desde el caché.
const filasPj = [];
if (!pjs.length) {
  box.createDiv({ text: "🍖 No hay PJ activos (tipo: pj) en la campaña todavía." }).style.color = "var(--text-muted)";
} else {
  const tabla = box.createEl("table");
  tabla.style.width = "100%";
  const th = tabla.createEl("tr");
  for (const t of ["PJ", "🍖", "Estado", "Descanso corto", ""]) th.createEl("th", { text: t });
  for (const f of pjs) {
    const tr = tabla.createEl("tr");
    const nombre = tr.createEl("td").createEl("a", { text: f.basename, cls: "internal-link", href: f.path });
    nombre.onclick = (e) => { e.preventDefault(); app.workspace.openLinkText(f.path, cur.file.path); };
    const tdVal = tr.createEl("td");
    const tdEst = tr.createEl("td");
    const tdDg = tr.createEl("td");
    const acc = tr.createEl("td");
    acc.style.cssText = "display:flex;flex-wrap:wrap;gap:4px;";
    boton(acc, "−1", () => sumarHambre(f, -1));
    const sel = acc.createEl("select", { attr: { "aria-label": `Comida para ${f.basename}` } });
    for (const [n, v] of COMIDAS) sel.createEl("option", { text: `${n} (+${v})`, value: String(v) });
    boton(acc, "Comer", () => sumarHambre(f, Number(sel.value)));
    filasPj.push({ f, tdVal, tdEst, tdDg });
  }
}

let ultimaHora = Math.floor(ahora());
const pintar = () => {
  const t = ahora();
  const dia = Math.floor(t / 24) + 1;
  const h = Math.floor(t % 24);
  const m = Math.floor((t % 1) * 60);
  reloj.setText(`Día ${dia} · ${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")} · ${fase(h)}`);
  const minRestantes = Math.ceil((1 - (t % 1)) * MIN_REALES_POR_HORA);
  sub.setText(
    (inicio ? `▶ En marcha (1 h = ${MIN_REALES_POR_HORA} min reales; próxima hora en ~${minRestantes} min)` : "⏸ Pausado") +
      (tocaTirada(h) ? " · 🎲 Toca tirada de aparición a los que estén despiertos" : "")
  );
  bPlay.setText(inicio ? "⏸ Pausar" : "▶ Reanudar");

  for (const r of filasPj) {
    const v = leerHambre(r.f);
    const [est, dg] = estadoHambre(v);
    r.tdVal.setText(`${"■".repeat(v)}${"□".repeat(HAMBRE_MAX - v)} ${v}`);
    r.tdEst.setText(est);
    r.tdDg.setText(dg);
  }

  // Al cruzar una hora con el reloj en marcha: avisos y cobro de hambre
  const hora = Math.floor(t);
  if (inicio && hora > ultimaHora) {
    const hh = hora % 24;
    if (fase(hh) !== fase((hh + 23) % 24)) new Notice(`Reloj: empieza ${fase(hh)} (Día ${Math.floor(hora / 24) + 1})`);
    if (tocaTirada(hh)) new Notice("🎲 Tirada de aparición nocturna");
    sincronizarHambre();
  }
  ultimaHora = hora;
};
pintar();
sincronizarHambre(); // cobra las horas que pasaron con el reloj en marcha mientras la nota estaba cerrada

// Se para solo cuando Dataview vuelve a pintar el bloque o se cierra la nota.
let montado = false;
const id = setInterval(() => {
  if (box.isConnected) { montado = true; pintar(); }
  else if (montado) clearInterval(id);
}, 1000);
