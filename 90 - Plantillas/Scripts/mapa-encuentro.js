// Muestra el mapa de un encuentro y el acceso a PlanarAlly.
// Uso:  ```dataviewjs  await dv.view("90 - Plantillas/Scripts/mapa-encuentro")  ```
// Lee `mapa` ("[[cueva.jpg]]") y `escena_planarally` de la nota, y `planarally_sala` del dashboard de la campaña.
const cur = dv.current();
const raiz = cur.file.folder.split("/").slice(0, 2).join("/");
const sala = dv.pages(`"${raiz}"`).where((p) => p.tipo === "dashboard" && p.planarally_sala).first()?.planarally_sala;

const linea = [];
if (sala) linea.push(`[▶️ Abrir sala en PlanarAlly](${sala})`);
else linea.push("⚠️ Pon `planarally_sala` en el dashboard de la campaña para tener el botón.");
if (cur.escena_planarally) linea.push(`escena: **${cur.escena_planarally}**`);
dv.paragraph(linea.join(" · "));

const ruta = cur.mapa?.path ?? (cur.mapa ? String(cur.mapa).replace(/^\[\[|\]\]$/g, "") : "");
const archivo = ruta && app.metadataCache.getFirstLinkpathDest(ruta, cur.file.path);
if (archivo) dv.span(dv.fileLink(archivo.path, true));
else dv.paragraph(`Sin mapa. Guarda la imagen en \`${raiz}/10 - Mapas/Encuentros/\` y pon \`mapa: "[[nombre.jpg]]"\`.`);
