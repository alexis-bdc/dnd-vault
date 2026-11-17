// Encuentros de una sesión. Uso en la nota de sesión:
//   ```dataviewjs
//   await dv.view("90 - Plantillas/Scripts/encuentros-sesion")
//   ```
// - Lista los encuentros planeados (`sesion`) o jugados (`jugado_en`) en esta sesión.
// - La casilla marca el encuentro como Jugado en esta sesión (o lo devuelve a Preparado).
// - Abajo lista los encuentros Preparados de la campaña sin sesión asignada (o de otra sesión) para traerlos aquí.
const cur = dv.current();
const raiz = cur.file.folder.split("/").slice(0, 2).join("/");
const link = `[[${cur.file.path.replace(/\.md$/, "")}|${cur.file.name}]]`;
const esEsta = (v) => !!v && dv.page(v)?.file.path === cur.file.path;
const nombreSesion = (v) => (v && dv.page(v)?.file.name) || "—";

const encuentros = dv.pages(`"${raiz}"`).where((p) => p.tipo === "encuentro");
const deEsta = encuentros.where((p) => esEsta(p.sesion) || esEsta(p.jugado_en)).sort((p) => p.file.name);
const pendientes = encuentros.where((p) => p.estado === "Preparado" && !esEsta(p.sesion)).sort((p) => p.file.name);

const editar = async (p, cambio) => {
  await app.fileManager.processFrontMatter(app.vault.getAbstractFileByPath(p.file.path), cambio);
};

const tabla = (filas, cabecera, celdas) => {
  const t = dv.container.createEl("table");
  const h = t.createEl("tr");
  cabecera.forEach((c) => h.createEl("th", { text: c }));
  for (const p of filas) {
    const tr = t.createEl("tr");
    celdas(p).forEach((c) => {
      const td = tr.createEl("td");
      typeof c === "string" ? td.setText(c) : td.appendChild(c);
    });
  }
};

const enlace = (p) => {
  const a = createEl("a", { text: p.file.name, cls: "internal-link", href: p.file.path });
  a.dataset.href = p.file.path;
  return a;
};

dv.header(4, "Encuentros de esta sesión");
if (!deEsta.length) {
  dv.paragraph("Ninguno todavía. Usa la lista de abajo o pon `sesion: " + link + "` en un encuentro.");
} else {
  tabla(deEsta, ["Hecho", "Encuentro", "Tipo", "Estado"], (p) => {
    const cb = createEl("input", { type: "checkbox" });
    cb.checked = esEsta(p.jugado_en);
    cb.onchange = () => editar(p, (fm) => {
      fm.estado = cb.checked ? "Jugado" : "Preparado";
      fm.jugado_en = cb.checked ? link : "";
      if (!fm.sesion) fm.sesion = link;
    });
    return [cb, enlace(p), p.tipo_encuentro ?? "", p.estado ?? ""];
  });
}

if (pendientes.length) {
  dv.header(4, "Encuentros pendientes de la campaña");
  tabla(pendientes, ["", "Encuentro", "Tipo", "Planeado para"], (p) => {
    const b = createEl("button", { text: "➕ A esta sesión" });
    b.onclick = () => editar(p, (fm) => { fm.sesion = link; });
    return [b, enlace(p), p.tipo_encuentro ?? "", nombreSesion(p.sesion)];
  });
}
