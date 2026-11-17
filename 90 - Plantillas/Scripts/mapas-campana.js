// Galería de los mapas de la campaña (imágenes dentro de <campaña>/10 - Mapas/), agrupados por carpeta,
// con los encuentros que usan cada uno. Uso:  ```dataviewjs  await dv.view("90 - Plantillas/Scripts/mapas-campana")  ```
const cur = dv.current();
const raiz = cur.file.folder.split("/").slice(0, 2).join("/");
const base = raiz + "/10 - Mapas/";
const imgs = app.vault.getFiles()
  .filter((f) => f.path.startsWith(base) && /^(png|jpe?g|webp|gif)$/i.test(f.extension))
  .sort((a, b) => a.path.localeCompare(b.path));

if (!imgs.length) {
  dv.paragraph(`No hay mapas todavía. Guarda imágenes en \`${base}\` (por ejemplo en \`Encuentros/\`).`);
  return;
}

// encuentro → archivo de mapa
const usos = {};
for (const p of dv.pages(`"${raiz}"`).where((p) => p.tipo === "encuentro" && p.mapa)) {
  const ruta = p.mapa.path ?? String(p.mapa).replace(/^\[\[|\]\]$/g, "");
  const f = app.metadataCache.getFirstLinkpathDest(ruta, p.file.path);
  if (f) (usos[f.path] ??= []).push(p.file);
}

const grupos = {};
for (const f of imgs) (grupos[f.parent.path.slice(base.length) || "General"] ??= []).push(f);

for (const [grupo, files] of Object.entries(grupos)) {
  dv.header(4, grupo);
  const grid = dv.container.createDiv();
  grid.style.cssText = "display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;";
  for (const f of files) {
    const card = grid.createDiv();
    const img = card.createEl("img", { attr: { src: app.vault.getResourcePath(f), loading: "lazy" } });
    img.style.cssText = "width:100%;height:120px;object-fit:cover;border-radius:6px;cursor:pointer;";
    img.onclick = () => app.workspace.getLeaf(true).openFile(f);
    card.createDiv({ text: f.basename }).style.fontSize = "0.85em";
    for (const e of usos[f.path] ?? []) {
      const a = card.createEl("a", { text: "⚔️ " + e.name, cls: "internal-link", href: e.path });
      a.dataset.href = e.path;
      a.style.cssText = "display:block;font-size:0.8em;";
    }
  }
}
