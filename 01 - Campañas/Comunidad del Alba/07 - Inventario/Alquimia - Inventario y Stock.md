---
tipo: bbdd_inventario
campaña: Comunidad del Alba
nombre: Base de Datos de Inventario y Stock Alquímico
consumibles:
  Poción de Curación (2d4+2): 2
  Poción de Curación Mayor (4d4+4): 0
  Antitoxina: 1
  Vial de Ácido (2d6): 2
  Fuego de Alquimista (1d4/t): 0
  Veneno Básico (1d4): 2
  Incienso Místico (1d4 Nv 1): 2
  Bomba de Humo (Ceguera): 0
  Bomba de Hedor (Fétida): 0
  Bomba Psicoledia: 2
  Bomba Venenosa (1d4/t): 0
  Bomba de Peste (2d4 Necrótico): 0
  Bomba de Sueño (Letargo): 0
  Poción de Trepar: 0
  Poción de Respirar Agua: 0
  Poción de Forma Gaseosa: 0
  cabezal de fuerza: 3
  cabezal de ácido: 0
  cabezal de fuego: 1
bases_liquidas:
  Agua Fresca: 6
  Agua Salada: 5
  Miel: 2
  Vino: 4
  Cerveza: 4
  Vinagre: 2
  Mayonesa: 2
  Aceite: 4
  Ácido: 3
  Veneno Básico: 2
esencias:
  Extracto Vital: 8
  Extracto Mutagénico: 2
  Esencia Adaptativa: 4
  Esencia Psicoactiva: 2
  Toxina Concentrada: 6
  Polvo Acre: 16
  Polvo Inerte: 20
  Polvo Ígneo: 4
  Cristal Cinético: 2
  Sales de Choque: 6
  Vitriolo Corrosivo: 4
materias_primas:
  Hongos Feéricos de Zadash: 4
  Hierbas Medicinales Silvestres: 3
  Menas Sulfúricas y Rocas Ácidas: 2
  Hongo venenoso: 2
  Glándulas de Veneno de Monstruo: 0
  Cristales de Resonancia en Bruto: 0
  Azufre Volcánico y Piritas: 0
  Raíces y Tubérculos Adaptógenos: 0
  Restos Biológicos Mutantes: 0
  Sales Minerales Conductoras: 0
  Cenizas y Turba Humosa: 0
bandolera:
  ranura_1: Poción de Curación (2d4+2)
  ranura_2: Vacío
  ranura_3: Bomba Psicoledia
  ranura_4: cabezal de fuerza
bandolera_pila:
  ranura_1: Vacío
  ranura_2: Vacío
  ranura_3: Vacío
tags:
  - dnd/bbdd
  - dnd/inventario
  - dnd/alquimia
---

# 📦 Base de Datos: Stock e Inventario Alquímico

> [!database] **Tabla de Persistencia de Datos**
> Este archivo almacena la **Fuente Única de Verdad** del inventario alquímico de Frater Ren. La interacción táctica, uso y crafteo se gestionan desde el [[01 - Campañas/Comunidad del Alba/07 - Inventario/Laboratorio Alquimico|Laboratorio Alquímico Portátil]].

---

## 🎒 1. Tabla de Consumibles y Pociones

```dataviewjs
const p = dv.current();
const fm = p?.file?.frontmatter || p || {};
const consumibles = fm.consumibles || {};

const rows = Object.entries(consumibles).map(([item, cant]) => [`**${item}**`, cant > 0 ? `🟢 **${cant}**` : "⚪ 0"]);

dv.table(["Consumible / Preparado", "Stock Actual"], rows);
```

---

## 💧 2. Tabla de Bases Líquidas

```dataviewjs
const p = dv.current();
const fm = p?.file?.frontmatter || p || {};
const bases = fm.bases_liquidas || {};

const rows = Object.entries(bases).map(([base, cant]) => [`💧 **${base}**`, `**${cant}**`]);

dv.table(["Base Líquida (Vasija Alquímica)", "Cantidad en Stock"], rows);
```

---

## 🌿 3. Tabla de Esencias y Polvos Purificados

```dataviewjs
const p = dv.current();
const fm = p?.file?.frontmatter || p || {};
const esencias = fm.esencias || {};

const rows = Object.entries(esencias).map(([esencia, cant]) => [`🧪 **${esencia}**`, `**${cant}**`]);

dv.table(["Esencia / Polvo Purificado", "Stock Purificado"], rows);
```

---

## 🔬 4. Tabla de Materias Primas Sin Procesar

```dataviewjs
const p = dv.current();
const fm = p?.file?.frontmatter || p || {};
const materias = fm.materias_primas || {};

const rows = Object.entries(materias).map(([mat, cant]) => [`🌿 **${mat}**`, cant > 0 ? `🟢 **${cant}**` : "⚪ 0"]);

dv.table(["Materia Prima en Bruto", "Stock Disponible"], rows);
```
