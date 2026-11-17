// Reloj día/noche en tiempo real para un dashboard. Uso:  ```dataviewjs  await dv.view("90 - Plantillas/Scripts/reloj-dia")  ```
// Estado en el frontmatter de la nota: reloj_horas (horas de juego desde el día 1 a las 00:00) y reloj_inicio (ms reales en que se pulsó ▶, 0 = pausado).
const MIN_REALES_POR_HORA = 5;
const MS_POR_HORA = MIN_REALES_POR_HORA * 60 * 1000;

const file = app.vault.getAbstractFileByPath(dv.current().file.path);
const fm = app.metadataCache.getFileCache(file)?.frontmatter ?? {};
let base = Number(fm.reloj_horas ?? 7); // por defecto: día 1, 07:00
let inicio = Number(fm.reloj_inicio || 0);

const ahora = () => base + (inicio ? (Date.now() - inicio) / MS_POR_HORA : 0);

const fase = (h) =>
  h >= 6 && h < 7 ? "🌅 Amanecer" : h >= 7 && h < 18 ? "☀️ Día" : h >= 18 && h < 19 ? "🌇 Atardecer" : "🌙 Noche";
// De noche se tira aparición cada 2 h despiertos: a las 19, 21, 23, 01, 03, 05.
const tocaTirada = (h) => fase(h) === "🌙 Noche" && h % 2 === 1;

const guardar = async (total, corriendo) => {
  base = Math.max(0, total);
  inicio = corriendo ? Date.now() : 0;
  await app.fileManager.processFrontMatter(file, (f) => {
    f.reloj_horas = Math.round(base * 1000) / 1000;
    f.reloj_inicio = inicio;
  });
  pintar();
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

const boton = (txt, fn) => {
  const b = fila.createEl("button", { text: txt });
  b.onclick = fn;
  return b;
};
const bPlay = boton("", () => guardar(ahora(), !inicio));
boton("+1 h", () => guardar(ahora() + 1, !!inicio));
boton("😴 Dormir 8 h", () => guardar(ahora() + 8, !!inicio));
const inp = fila.createEl("input", { type: "number", value: "2", attr: { step: "0.5", "aria-label": "Horas a avanzar" } });
inp.style.width = "5em";
boton("Avanzar h", () => {
  const x = Number(inp.value);
  if (Number.isFinite(x) && x !== 0) guardar(ahora() + x, !!inicio);
});

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

  // Avisos al cruzar una hora con el reloj en marcha
  const hora = Math.floor(t);
  if (inicio && hora > ultimaHora) {
    const hh = hora % 24;
    if (fase(hh) !== fase((hh + 23) % 24)) new Notice(`Reloj: empieza ${fase(hh)} (Día ${Math.floor(hora / 24) + 1})`);
    if (tocaTirada(hh)) new Notice("🎲 Tirada de aparición nocturna");
  }
  ultimaHora = hora;
};
pintar();

// Se para solo cuando Dataview vuelve a pintar el bloque o se cierra la nota.
let montado = false;
const id = setInterval(() => {
  if (box.isConnected) { montado = true; pintar(); }
  else if (montado) clearInterval(id);
}, 1000);
