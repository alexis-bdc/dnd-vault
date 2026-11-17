<%*
// Descanso largo: PG al máximo y todos los espacios de conjuro "_usados" a 0.
// En un dashboard, usa la nota indicada en su propiedad `pj_panel`.
const active = app.workspace.getActiveFile();
const fmActive = active ? app.metadataCache.getFileCache(active)?.frontmatter : null;
const target = fmActive?.pj_panel ? app.vault.getAbstractFileByPath(fmActive.pj_panel) : active;

if (!target) {
  new Notice("❌ No se encontró la nota del personaje.");
  return;
}

let ok = true;
await app.fileManager.processFrontMatter(target, (fm) => {
  if (fm.pg_max == null) { ok = false; return; }
  fm.pg_actual = fm.pg_max;
  for (const k of Object.keys(fm.espacios_conjuro || {})) {
    if (k.endsWith("_usados")) fm.espacios_conjuro[k] = 0;
  }
});

new Notice(ok ? `🌙 Descanso largo: ${target.basename} recuperado.` : `❌ ${target.basename} no tiene pg_max.`, 4000);
%>
