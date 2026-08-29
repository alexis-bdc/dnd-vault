---
tipo: bbdd_recetas
campaña: "Comunidad del Alba"
nombre: "Base de Datos de Recetas y Rendimientos Alquímicos"
recetas_alquimia:
  Poción de Curación (2d4+2):
    descripcion: "Cura 2d4 + 2 PG (+3 INT Tratamiento Alquímico)."
    delta:
      Agua Fresca: -1
      Extracto Vital: -1
      Polvo Inerte: -1
      Poción de Curación (2d4+2): 1
  Poción de Curación Mayor (4d4+4):
    descripcion: "Cura 4d4 + 4 PG (+3 INT Tratamiento Alquímico)."
    delta:
      Agua Fresca: -1
      Extracto Vital: -2
      Polvo Inerte: -1
      Poción de Curación Mayor (4d4+4): 1
  Antitoxina:
    descripcion: "Ventaja en tiradas de salvación contra veneno (1 hora)."
    delta:
      Agua Fresca: -1
      Extracto Vital: -1
      Polvo Inerte: -1
      Antitoxina: 1
  Vial de Ácido (2d6):
    descripcion: "Arrojadizo (20 pies). Inflige 2d6 de daño de ácido al impactar."
    delta:
      Ácido: -1
      Vitriolo Corrosivo: -1
      Polvo Inerte: -1
      Vial de Ácido (2d6): 1
  Fuego de Alquimista (1d4/t):
    descripcion: "Arrojadizo (20 pies). Inflige 1d4 de daño de fuego al inicio de cada turno hasta apagarse."
    delta:
      Vino: -1
      Polvo Ígneo: -2
      Fuego de Alquimista (1d4/t): 1
  Veneno Básico (1d4):
    descripcion: "Aplica a arma o 3 municiones. +1d4 de daño de veneno (duración 1 min)."
    delta:
      Veneno Básico: -1
      Toxina Concentrada: -1
      Polvo Acre: -1
      Veneno Básico (1d4): 1
  Bomba de Humo (Ceguera):
    descripcion: "Área 15 pies. Crea ceguera visual y cobertura pesada por humo denso."
    delta:
      Agua Salada: -1
      Polvo Acre: -1
      Polvo Inerte: -1
      Bomba de Humo (Ceguera): 1
  Bomba de Hedor (Fétida):
    descripcion: "Área 20 pies. Olor nauseabundo (TS Constitución CD 12 o pierde la acción)."
    delta:
      Agua Fresca: -1
      Sales de Choque: -1
      Polvo Acre: -1
      Bomba de Hedor (Fétida): 1
  Bomba Psicoledia:
    descripcion: "Área 20 pies. Humo psicodélico que distorsiona la percepción feérica y sentidos."
    delta:
      Vinagre: -1
      Esencia Psicoactiva: -1
      Bomba Psicoledia: 1
  Bomba Venenosa (1d4/t):
    descripcion: "Área 30 pies. Inflige 1d4 de daño de veneno continuo por asalto."
    delta:
      Veneno Básico: -1
      Cristal Cinético: -1
      Toxina Concentrada: -1
      Bomba Venenosa (1d4/t): 1
  Bomba de Peste (2d4 Necrótico):
    descripcion: "Área 20 pies. Inflige 2d4 de daño necrótico por putrefacción acelerada."
    delta:
      Veneno Básico: -1
      Vitriolo Corrosivo: -1
      Bomba de Peste (2d4 Necrótico): 1
  Bomba de Sueño (Letargo):
    descripcion: "Área 15 pies. Induce sopor mágico y sueño profundo a criaturas con TS fallida."
    delta:
      Vino: -1
      Esencia Psicoactiva: -1
      Polvo Inerte: -1
      Bomba de Sueño (Letargo): 1
  Poción de Trepar:
    descripcion: "Velocidad de escalada igual a terrestre (1 hora) y ventaja en Atletismo."
    delta:
      Mayonesa: -1
      Esencia Adaptativa: -1
      Poción de Trepar: 1
  Poción de Respirar Agua:
    descripcion: "Permite respirar bajo el agua con normalidad durante 1 hora."
    delta:
      Agua Salada: -1
      Esencia Adaptativa: -1
      Polvo Inerte: -1
      Poción de Respirar Agua: 1
  Poción de Forma Gaseosa:
    descripcion: "Transforma al usuario en nube brumosa (conjuro Forma Gaseosa) durante 1 hora."
    delta:
      Vinagre: -1
      Cristal Cinético: -2
      Polvo Inerte: -1
      Poción de Forma Gaseosa: 1
  Incienso Místico (1d4 Nv 1):
    descripcion: "Descanso corto: permite recuperar 1d4 espacios de conjuro de Nivel 1."
    delta:
      Agua Fresca: -1
      Polvo Ígneo: -1
      Esencia Psicoactiva: -1
      Sales de Choque: -1
      Incienso Místico (1d4 Nv 1): 1
  cabezal de fuerza:
    descripcion: "Cabezal para virote. +1d6 de daño de fuerza, empuja al enemigo 5 pies y a quienes estén alrededor."
    delta:
      Cristal Cinético: -2
      Polvo Ígneo: -1
      cabezal de fuerza: 2
  cabezal de ácido:
    descripcion: "Cabezal para virote impregnado en ácido. +1d6 de daño de ácido al impactar."
    delta:
      Ácido: -1
      Vitriolo Corrosivo: -1
      Polvo Inerte: -1
      cabezal de ácido: 2
  cabezal de fuego:
    descripcion: "Cabezal para virote impregnado en aceite inflamable. +1d4 de daño de fuego al impactar."
    delta:
      Aceite: -1
      Polvo Ígneo: -1
      cabezal de fuego: 2
rendimientos_materias:
  Hongos Feéricos de Zadash:
    delta:
      Hongos Feéricos de Zadash: -1
      Esencia Psicoactiva: 1
      Polvo Acre: 1
  Hierbas Medicinales Silvestres:
    delta:
      Hierbas Medicinales Silvestres: -1
      Extracto Vital: 1
      Polvo Inerte: 1
  Glándulas de Veneno de Monstruo:
    delta:
      Glándulas de Veneno de Monstruo: -1
      Toxina Concentrada: 1
      Polvo Acre: 1
  Cristales de Resonancia en Bruto:
    delta:
      Cristales de Resonancia en Bruto: -1
      Cristal Cinético: 1
      Polvo Inerte: 1
  Azufre Volcánico y Piritas:
    delta:
      Azufre Volcánico y Piritas: -1
      Polvo Ígneo: 1
      Polvo Inerte: 1
  Raíces y Tubérculos Adaptógenos:
    delta:
      Raíces y Tubérculos Adaptógenos: -1
      Esencia Adaptativa: 1
      Polvo Inerte: 1
  Menas Sulfúricas y Rocas Ácidas:
    delta:
      Menas Sulfúricas y Rocas Ácidas: -1
      Vitriolo Corrosivo: 1
      Polvo Inerte: 1
  Restos Biológicos Mutantes:
    delta:
      Restos Biológicos Mutantes: -1
      Extracto Mutagénico: 1
      Polvo Acre: 1
  Sales Minerales Conductoras:
    delta:
      Sales Minerales Conductoras: -1
      Sales de Choque: 1
      Polvo Inerte: 1
  Cenizas y Turba Humosa:
    delta:
      Cenizas y Turba Humosa: -1
      Polvo Acre: 2
      Polvo Inerte: 1
  Hongo venenoso:
    delta:
      Hongo venenoso: -1
      Toxina Concentrada: 2
tags:
  - dnd/bbdd
  - dnd/recetas
  - dnd/alquimia
---

# 📜 Base de Datos: Catálogo Maestro de Recetas y Rendimientos

> [!database] **Tabla de Persistencia: Fórmulas y Reglas de Alquimia (Modelo Vectorial)**
> Este archivo almacena la **Fuente Única de Verdad** para el catálogo de recetas y rendimientos de extracción representados como **vectores de transformación ($\Delta \vec{I}$)**. Los crafteos interactivos y consumos se gestionan desde el [[01 - Campañas/Comunidad del Alba/07 - Inventario/Laboratorio Alquimico|Laboratorio Alquímico Portátil]].

---

## ⚗️ 1. Catálogo Completo de Fórmulas y Recetas

```dataviewjs
const p = dv.current();
const fm = p?.file?.frontmatter || p || {};
const recetas = fm.recetas_alquimia || {};

const rows = [];
let index = 1;

for (const [nombre, data] of Object.entries(recetas)) {
  const code = `**REC-${index.toString().padStart(2, "0")}**`;
  index++;

  const delta = data.delta || {};
  const insumos = [];
  let prodCant = 1;

  for (const [item, cant] of Object.entries(delta)) {
    if (cant < 0) {
      insumos.push(`${Math.abs(cant)}x ${item}`);
    } else if (cant > 0) {
      prodCant = cant;
    }
  }

  // Fallback para formato antiguo si existiera
  if (insumos.length === 0 && data.costes) {
    if (data.costes.bases_liquidas) {
      for (const [b, c] of Object.entries(data.costes.bases_liquidas)) insumos.push(`${c}x ${b}`);
    }
    if (data.costes.esencias) {
      for (const [e, c] of Object.entries(data.costes.esencias)) insumos.push(`${c}x ${e}`);
    }
    prodCant = Number(data.cantidad_producida) || 1;
  }

  const lote = prodCant > 1 ? `⚡ ${prodCant}x / lote` : "1x";
  rows.push([code, `**${nombre}**`, lote, insumos.join(" + ") || "⚪ Sin insumos", data.descripcion || ""]);
}

dv.table(["Código", "Receta / Producto", "Lote", "Insumos Requeridos (ΔI < 0)", "Efecto / Reglas Mecánicas"], rows);
```

---

## 🔬 2. Catálogo de Rendimientos de Materias Primas

```dataviewjs
const p = dv.current();
const fm = p?.file?.frontmatter || p || {};
const rendimientos = fm.rendimientos_materias || {};

const rows = [];
for (const [mat, formula] of Object.entries(rendimientos)) {
  const delta = formula.delta || formula;
  const parts = [];
  for (const [item, cant] of Object.entries(delta)) {
    if (cant > 0) {
      parts.push(`🧪 +${cant}x ${item}`);
    }
  }
  rows.push([`**${mat}**`, parts.join(", ")]);
}

dv.table(["Materia Prima en Bruto", "Rendimiento Obtenido al Extraer (ΔI > 0)"], rows);
```
