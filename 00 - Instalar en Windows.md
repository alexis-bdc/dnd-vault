---
tipo: guia
tags:
  - dnd/inicio
---

# 🪟 Instalar esta bóveda en Windows

Todo lo necesario está en el repositorio: notas, plantillas, scripts, **plugins con su configuración**, imágenes, tokens y los **mapas ya generados**. No hay que instalar nada más que Obsidian y Git.

---

## 1. Programas

| Programa | Para qué | Descarga |
|---|---|---|
| **Obsidian** | Abrir la bóveda | obsidian.md |
| **Git for Windows** | Bajar el repositorio y que el plugin Git haga copias automáticas | git-scm.com (opciones por defecto; incluye *Git Credential Manager*) |

## 2. Bajar el repositorio

En PowerShell, dentro de la carpeta donde quieras la bóveda (por ejemplo `Documentos`):

```powershell
git clone https://github.com/alexis-bdc/dnd-vault.git
```

La primera vez que el plugin Git haga *push*, Windows abrirá una ventana para iniciar sesión en GitHub.

> [!tip] ¿Prefieres SSH (como en Linux)?
> `ssh-keygen -t ed25519`, sube `C:\Users\<tú>\.ssh\id_ed25519.pub` a GitHub (*Settings → SSH keys*) y clona con `git clone git@github.com:alexis-bdc/dnd-vault.git`.

## 3. Abrir en Obsidian

1. *Abrir carpeta como bóveda* → la carpeta `dnd-vault`.
2. Cuando pregunte por los plugins de la comunidad: **Confiar en el autor y activar** (desactiva el modo restringido).
3. Recarga una vez (`Ctrl + R`).

Los plugins vienen dentro de `.obsidian/plugins/` con su configuración, así que no hay que instalarlos:

| Plugin | Se usa para |
|---|---|
| **Dataview** (JS activado) | Dashboard, reloj del día, hambre, tablas de party y encuentros |
| **Templater** (carpeta `90 - Plantillas`) | Plantillas de notas y el generador de encuentros (`Scripts/generar_encuentro.md`) |
| **Meta Bind** | Botones y campos editables de las notas |
| **Fantasy Statblocks** | Statblocks de los mobs (`08 - Lore/Mobs/`) |
| **Leaflet** | Mapa del mundo y del Nether con marcadores, rutas y medición de distancias |
| **Git** | Copia automática cada 5 minutos y *pull* al abrir |
| **Iconize**, **Advanced Tables**, **DataLoom** | Iconos de carpetas, edición de tablas, bases de datos |
| **Terminal** | Terminal dentro de Obsidian (ver abajo) |

## 4. Comprobaciones tras abrir

- [ ] **Statblocks:** abre `08 - Lore/Mobs/Zombi`. Si no se ve el statblock, ejecuta el comando *Fantasy Statblocks: Parse frontmatter for creatures* (`Ctrl + P`).
- [ ] **Dashboard:** abre `Dashboard - Tierra de Bloques`. Debe verse el reloj con ▶/⏸ y la tabla de hambre.
- [ ] **Mapas:** abre `Mapa del Mundo` y `Mapa del Nether`. Si el mapa se ve en blanco, recarga con `Ctrl + R`. Los iconos (🏠 ⚓ 🔑…) vienen de `markers.json` en la carpeta de la campaña.
- [ ] **Encuentros:** con una nota de la campaña abierta, `Ctrl + P` → *Templater: Insert template* → `generar_encuentro`. Las opciones deben listar mobs de la campaña (🧟).
- [ ] **Terminal:** sus perfiles se configuraron en Linux. En *Ajustes → Terminal* crea un perfil de **PowerShell** si quieres usarlo.

> [!warning] Saltos de línea
> Si `git status` muestra todos los archivos modificados sin haber tocado nada, ejecuta una vez `git config --global core.autocrlf true`.

---

## 🗺️ Mapas (ya generados)

Están listos en `01 - Campañas/Tierra de Bloques/`:

| Archivo | Qué es |
|---|---|
| `Mapa del Mundo.md` + `10 - images/Mapa del Mundo.png` | Superficie, 8000×8000 bloques, semilla `-4697940382757111526` (Java 1.21) |
| `Mapa del Nether.md` + `10 - images/Mapa del Nether.png` | Nether, 2000×2000 bloques (= 16 000 de superficie) |
| `Rutas - Mapa del Mundo.geojson` | Caminos y rutas marítimas entre aldeas |
| `markers.json` | Iconos de cada tipo de estructura |

**Solo hace falta regenerarlos si cambias de semilla.** Para eso (opcional):

1. Instala **Python 3** (python.org, marca *Add to PATH*) y un **gcc**: [w64devkit](https://github.com/skeeto/w64devkit/releases) (descomprimir y añadir su carpeta `bin` al PATH) o MSYS2 MinGW.
2. Desde la carpeta de la bóveda:
   ```powershell
   py .tools/mapa-mundo/generar_mapa.py <semilla> 1.21 --bpp 1
   py .tools/mapa-mundo/generar_mapa.py <semilla> 1.21 --bpp 1 --nether --lado 2000
   ```
   La primera vez descarga y compila cubiomes solo (no necesita `make` ni ImageMagick).

> [!danger] Regenerar sobrescribe
> Vuelve a escribir `Mapa del Mundo.md` / `Mapa del Nether.md`, el `.geojson` y `markers.json`. Lo que hayas editado a mano en esas notas se pierde (los marcadores que crees con clic derecho en Leaflet no, porque se guardan en el plugin).

---

## 📦 Qué contiene la campaña *Tierra de Bloques*

| Dónde | Qué |
|---|---|
| `Dashboard - Tierra de Bloques` | Reloj del día en tiempo real (1 h = 5 min), hambre por PJ, party |
| `08 - Lore/` | Reglas de supervivencia: día y noche, hambre, recolección, durabilidad, juego nómada, muerte, eras, bestiario |
| `08 - Lore/Mobs/` | 26 statblocks (17 del PDF *Minecraft 5e* + 9 caseros de las cámaras de desafío) |
| `07 - Inventario/` | Recetas de crafteo, comercio y equivalencias, botín por lugar |
| `10 - images/Tokens/` | Tokens de los mobs para el VTT (cuerpo entero y `Caras/`) |
| `90 - Plantillas/Scripts/` | `reloj-dia.js`, `encuentros-lib.js`, `dificultad.js`, `generar_encuentro.md` |
| `99 - Adjuntos/Minecraft 5e.pdf` | Fuente original de los statblocks |
