// Muestra el mapa de un encuentro (para subirlo al tablero de Nivel20).
// Uso:  ```dataviewjs  await dv.view("90 - Plantillas/Scripts/mapa-encuentro")  ```
// Lee `mapa` ("[[cueva.jpg]]") de la nota.
const cur = dv.current();
const raiz = cur.file.folder.split("/").slice(0, 2).join("/");
const ruta = cur.mapa?.path ?? (cur.mapa ? String(cur.mapa).replace(/^\[\[|\]\]$/g, "") : "");
const archivo = ruta && app.metadataCache.getFirstLinkpathDest(ruta, cur.file.path);
if (archivo) dv.span(dv.fileLink(archivo.path, true));
else dv.paragraph(`Sin mapa. Guarda la imagen en \`${raiz}/10 - Mapas/Encuentros/\` y pon \`mapa: "[[nombre.jpg]]"\`.`);
