<%*
// Genera un encuentro aleatorio y lo guarda en <campaña>/09 - Encuentros/.
const L = new Function(await app.vault.adapter.read("90 - Plantillas/Scripts/encuentros-lib.js"))();
const T = L.TABLAS;

// 1. Campaña: la de la nota activa o se elige de la lista
const activePath = app.workspace.getActiveFile()?.path || "";
let raiz = activePath.startsWith("01 - Campañas/") ? activePath.split("/").slice(0, 2).join("/") : null;
if (!raiz) {
  const camps = app.vault.getAbstractFileByPath("01 - Campañas").children.filter((c) => c.children).map((c) => c.path);
  raiz = await tp.system.suggester(camps.map((c) => c.split("/")[1]), camps, false, "¿Para qué campaña?");
  if (!raiz) return;
}

// 2. Party: PJ activos de la campaña, o se pregunta
const pjs = app.vault.getMarkdownFiles()
  .filter((f) => f.path.startsWith(raiz + "/"))
  .map((f) => app.metadataCache.getFileCache(f)?.frontmatter)
  .filter((fm) => fm?.tipo === "pj" && (fm.estado ?? "Activo") === "Activo");
let niveles = pjs.map((fm) => Number(fm.nivel) || 1);
if (!niveles.length) {
  const nv = Number(await tp.system.prompt("No hay PJ en la campaña. Nivel de la party:", "1")) || 1;
  const cant = Number(await tp.system.prompt("Cantidad de jugadores:", "4")) || 4;
  niveles = Array(cant).fill(nv);
}
const nivelProm = Math.round(niveles.reduce((a, b) => a + b, 0) / niveles.length);
const tier = L.tier(nivelProm);

// 3. Tipo de encuentro
const tipo = await tp.system.suggester(
  ["⚔️ Combate", "💬 Social (PNJ)", "🪤 Exploración / Trampa", "🧩 Puzle"],
  ["Combate", "Social", "Exploracion", "Puzle"], false, "Tipo de encuentro");
if (!tipo) return;

const botin = () => `- [ ] ${L.pick(T.botin[tier])}\n- [ ] ${L.pick(T.botin[tier])}`;
let fm = { tipo_encuentro: tipo };
let cuerpo = "";

if (tipo === "Combate") {
  const dif = await tp.system.suggester(L.DIFICULTADES, L.DIFICULTADES, false, "Dificultad");
  if (!dif) return;
  const p = L.presupuesto(niveles);
  const ops = L.opciones(p[dif]);
  fm.dificultad_objetivo = dif;
  cuerpo = `## ⚔️ Enemigos
> Presupuesto ${dif}: **${p[dif]} XP** para ${niveles.length} PJ (nv ${niveles.join(", ")}). Elige una combinación y llena \`enemigos_cr\`.

${ops.map((o) => `- ${o.desc} (${o.xp} XP)`).join("\n")}

\`\`\`dataviewjs
await dv.view("90 - Plantillas/Scripts/dificultad")
\`\`\`

## 🎯 Qué quieren los enemigos
- ${L.pick(T.objetivo_enemigo)}

## 🗺️ Terreno
- ${L.pick(T.terreno)}
- ${L.pick(T.terreno)}

## 🌀 Complicación
- ${L.pick(T.complicacion)}`;
} else if (tipo === "Social") {
  const nombre = L.pick(T.nombres);
  fm.pnj = nombre;
  cuerpo = `## 💬 ${nombre}, ${L.pick(T.oficio)}
- **Actitud inicial:** ${L.pick(T.actitud)}
- **Quiere:** ${L.pick(T.quiere)}
- **Secreto:** ${L.pick(T.secreto)}
- **Para interpretarlo:** ${L.pick(T.rasgo)}

## 🗝️ Información que puede dar
- [ ] 
- [ ] 

## 🎲 Tiradas
- Persuasión / Engaño / Intimidación: CD ${[10, 13, 15, 18][tier]}
- Perspicacia para notar que oculta algo: CD ${[12, 14, 16, 18][tier]}`;
} else if (tipo === "Exploracion") {
  const sev = await tp.system.suggester(["Molesta", "Peligrosa", "Mortal"], ["Molesta", "Peligrosa", "Mortal"], false, "Severidad de la trampa");
  if (!sev) return;
  cuerpo = `## 🗺️ Ambiente
- ${L.pick(T.sensorial)}
- ${L.pick(T.sensorial)}

## 🪤 Trampa (${sev})
- **Qué es:** ${L.pick(T.trampas)}
- **CD detectar / desactivar / salvación:** ${L.TRAMPA_CD[sev]}
- **Daño (nv ${nivelProm}):** ${L.TRAMPA_DANO[sev][tier]}

## 🔍 Qué se puede descubrir
- [ ] `;
} else {
  cuerpo = `## 🧩 Puzle
- **Planteamiento:** ${L.pick(T.puzles)}
- **Solución:** 
- **Pistas (de sutil a obvia):**
  1. 
  2. 
  3. 
- **Si fallan:** `;
}

const fecha = tp.date.now("YYYY-MM-DD HHmm");
// Si se genera desde una nota de sesión, queda planeado para esa sesión
const activa = app.workspace.getActiveFile();
const sesionLink = activa && app.metadataCache.getFileCache(activa)?.frontmatter?.tipo === "sesion"
  ? `[[${activa.path.replace(/\.md$/, "")}|${activa.basename}]]` : "";
const yaml = Object.entries(fm).map(([k, v]) => `${k}: "${v}"`).join("\n");
const contenido = `---
tipo: encuentro
campaña: "${raiz.split("/")[1]}"
${yaml}
estado: Preparado # Preparado / Jugado / Descartado
sesion: "${sesionLink}"
jugado_en: ""
ubicacion: ""
${tipo === "Combate" ? "enemigos_cr: []\n" : ""}tags:
  - dnd/encuentro
  - dnd/dm
---

# Encuentro rápido: ${tipo} (${fecha})

${cuerpo}

## 💰 Botín
${botin()}

## 📝 Resultado
- 
`;

const carpeta = raiz + "/09 - Encuentros";
if (!app.vault.getAbstractFileByPath(carpeta)) await app.vault.createFolder(carpeta);
const archivo = await app.vault.create(`${carpeta}/Encuentro rápido - ${tipo} - ${fecha}.md`, contenido);
await app.workspace.getLeaf(true).openFile(archivo);
new Notice(`⚡ Encuentro de ${tipo} creado.`);
%>
