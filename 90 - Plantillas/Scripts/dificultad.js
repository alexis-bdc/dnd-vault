// Calculadora de dificultad para encuentros de combate.
// Uso en una nota:  ```dataviewjs  await dv.view("90 - Plantillas/Scripts/dificultad")  ```
// Lee `enemigos_cr` y `dificultad_objetivo` de la nota y los PJ activos (tipo: pj) de la campaña.
const L = new Function(await app.vault.adapter.read("90 - Plantillas/Scripts/encuentros-lib.js"))();
const cur = dv.current();
const raiz = cur.file.folder.split("/").slice(0, 2).join("/");
const niveles = dv.pages(`"${raiz}"`)
  .where((p) => p.tipo === "pj" && (p.estado ?? "Activo") === "Activo")
  .map((p) => p.nivel ?? 1).array();

if (!niveles.length) {
  dv.paragraph("⚠️ No hay PJ activos (`tipo: pj`, `estado: Activo`) en esta campaña.");
  return;
}

const p = L.presupuesto(niveles);
dv.paragraph(`**Party:** ${niveles.length} PJ (nv ${niveles.join(", ")}) · **Presupuesto XP:** Baja ${p.Baja} · Moderada ${p.Moderada} · Alta ${p.Alta}`);

const crs = cur.enemigos_cr ?? [];
if (crs.length) {
  const xp = crs.reduce((s, c) => s + L.xpDeCR(c), 0);
  const raros = crs.filter((c) => L.xpDeCR(c) === 0 && String(c) !== "0");
  dv.paragraph(`**Enemigos:** CR ${crs.join(", ")} → **${xp} XP** · ${L.calificar(xp, p)}` + (raros.length ? ` · ⚠️ CR no reconocido: ${raros.join(", ")}` : ""));
}

const obj = L.DIFICULTADES.includes(cur.dificultad_objetivo) ? cur.dificultad_objetivo : "Moderada";
dv.paragraph(`**Combinaciones para dificultad ${obj}** (${p[obj]} XP):`);
dv.table(["Opción", "XP"], L.opciones(p[obj]).map((o) => [o.desc, o.xp]));
