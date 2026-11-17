// Tablas y cálculos de encuentros (presupuesto de XP de la DMG 2024).
// La cargan generar_encuentro.md y dificultad.js con: new Function(código)().
// Edita las tablas aleatorias libremente: son listas de texto.

const CR_XP = [
  ["0", 10], ["1/8", 25], ["1/4", 50], ["1/2", 100], ["1", 200], ["2", 450], ["3", 700],
  ["4", 1100], ["5", 1800], ["6", 2300], ["7", 2900], ["8", 3900], ["9", 5000], ["10", 5900],
  ["11", 7200], ["12", 8400], ["13", 10000], ["14", 11500], ["15", 13000], ["16", 15000],
  ["17", 18000], ["18", 20000], ["19", 22000], ["20", 25000], ["21", 33000], ["22", 41000],
  ["23", 50000], ["24", 62000], ["25", 75000], ["26", 90000], ["27", 105000], ["28", 120000],
  ["29", 135000], ["30", 155000],
];

// XP por personaje según nivel: [baja, moderada, alta]
const PRESUPUESTO = {
  1: [50, 75, 100], 2: [100, 150, 200], 3: [150, 225, 400], 4: [250, 375, 500],
  5: [500, 750, 1100], 6: [600, 1000, 1400], 7: [750, 1300, 1700], 8: [1000, 1700, 2100],
  9: [1300, 2000, 2600], 10: [1600, 2300, 3100], 11: [1900, 2900, 4100], 12: [2200, 3700, 4700],
  13: [2600, 4200, 5400], 14: [2900, 4900, 6200], 15: [3300, 5400, 7800], 16: [3800, 6100, 9800],
  17: [4500, 7200, 11700], 18: [5000, 8700, 14200], 19: [5500, 10700, 17200], 20: [6400, 13200, 22000],
};

const DIFICULTADES = ["Baja", "Moderada", "Alta"];

function xpDeCR(cr) {
  const fila = CR_XP.find(([c]) => c === String(cr).trim());
  return fila ? fila[1] : 0;
}

function presupuesto(niveles) {
  const tot = [0, 0, 0];
  for (const n of niveles) {
    const fila = PRESUPUESTO[Math.min(20, Math.max(1, Number(n) || 1))];
    fila.forEach((v, i) => (tot[i] += v));
  }
  return { Baja: tot[0], Moderada: tot[1], Alta: tot[2] };
}

function calificar(xp, p) {
  if (xp > p.Alta) return "☠️ Más que Alta (posible muerte)";
  if (xp > p.Moderada) return "🔴 Alta";
  if (xp > p.Baja) return "🟠 Moderada";
  if (xp >= p.Baja * 0.5) return "🟢 Baja";
  return "⚪ Trivial";
}

// CR más alto tal que `cantidad` monstruos de ese CR caben en el presupuesto.
function mejorCR(budget, cantidad) {
  let mejor = null;
  for (const [cr, xp] of CR_XP) if (xp * cantidad <= budget) mejor = { cr, xp };
  return mejor;
}

function opciones(budget) {
  const filas = [];
  for (const n of [1, 2, 3, 4, 5, 6, 8]) {
    const m = mejorCR(budget, n);
    if (m) filas.push({ desc: `${n} × CR ${m.cr}`, xp: m.xp * n });
  }
  const jefe = mejorCR(budget * 0.6, 1);
  if (jefe) {
    const sec = mejorCR(budget - jefe.xp, 4);
    if (sec) filas.push({ desc: `Jefe CR ${jefe.cr} + 4 × CR ${sec.cr}`, xp: jefe.xp + sec.xp * 4 });
  }
  return filas;
}

// 0: nv 1-4, 1: 5-10, 2: 11-16, 3: 17-20
function tier(nivel) {
  return nivel <= 4 ? 0 : nivel <= 10 ? 1 : nivel <= 16 ? 2 : 3;
}

// Trampas (DMG): CD y daño según severidad y tier
const TRAMPA_CD = { Molesta: "10-11", Peligrosa: "12-15", Mortal: "16-20" };
const TRAMPA_DANO = {
  Molesta: ["1d10", "2d10", "4d10", "10d10"],
  Peligrosa: ["2d10", "4d10", "10d10", "18d10"],
  Mortal: ["4d10", "10d10", "18d10", "24d10"],
};

const pick = (arr) => arr[Math.floor(Math.random() * arr.length)];

const TABLAS = {
  terreno: [
    "Columnas o pilares: cobertura media", "Barro o escombros: terreno difícil",
    "Zona elevada: ventaja para quien dispara desde arriba", "Antorchas o braseros que se pueden apagar o volcar",
    "Puente o cornisa estrecha sobre una caída", "Agua hasta la cintura", "Barriles de aceite inflamable",
    "Niebla espesa: zona muy oscura", "Puerta pesada que se puede atrancar", "Lámpara de araña que se puede derribar",
    "Carros o mesas que se pueden volcar como cobertura", "Maleza alta: se puede esconder cualquiera",
  ],
  objetivo_enemigo: [
    "Robar un objeto concreto de los PJ", "Proteger a alguien que está huyendo", "Ganar tiempo para un ritual",
    "Capturar vivo a un PJ", "Defender su territorio o su nido", "Cobrar una recompensa por un PJ",
    "Tienen hambre: quieren comida o provisiones", "Asustarlos para que se vayan", "Recuperar algo que los PJ se llevaron",
    "Obedecen órdenes y no quieren estar ahí",
  ],
  complicacion: [
    "Llegan refuerzos en la ronda 3", "Un inocente queda atrapado en medio", "El suelo empieza a ceder",
    "Fuego que se extiende cada ronda", "Un enemigo pide rendirse y ofrece información", "Aparece un tercer bando",
    "El líder intenta huir con algo importante", "Se apagan todas las luces", "Empieza una tormenta: desventaja a distancia",
    "Un PNJ aliado cambia de bando",
  ],
  nombres: [
    "Aldric", "Brenna", "Corvin", "Dalia", "Edrin", "Fenna", "Garrick", "Hilde", "Isolde", "Jorund",
    "Kaela", "Lucan", "Mirela", "Nedric", "Orla", "Perrin", "Quilla", "Rowan", "Sabela", "Tobías",
    "Ulma", "Vesna", "Wendel", "Yara", "Zoltan",
  ],
  oficio: [
    "tabernero/a", "guardia cansado/a", "mercader ambulante", "sacerdote/isa", "contrabandista", "noble menor",
    "herrero/a", "cazador/a", "mendigo/a con buena memoria", "erudito/a", "capataz de mina", "posadero/a",
  ],
  actitud: ["Amistoso", "Indiferente", "Indiferente", "Desconfiado", "Hostil"],
  quiere: [
    "Que alguien le pague una deuda", "Proteger a su familia", "Subir de posición", "Que se vayan de su pueblo",
    "Venganza contra alguien concreto", "Sacar dinero de los PJ", "Que nadie descubra su secreto",
    "Un objeto que los PJ tienen", "Ayuda contra una amenaza que nadie le cree", "Salir de la ciudad sin ser visto",
  ],
  secreto: [
    "Trabaja para la facción enemiga", "Vio algo que no debía", "No es quien dice ser", "Debe dinero a gente peligrosa",
    "Escondió a un fugitivo", "Tiene un objeto robado", "Es pariente de un villano", "Mintió sobre un crimen",
    "Sabe dónde está algo que los PJ buscan", "Está enfermo y lo oculta",
  ],
  rasgo: [
    "Habla muy rápido y se come palabras", "Nunca mira a los ojos", "Repite la última palabra que le dicen",
    "Ríe en momentos raros", "Mastica algo todo el tiempo", "Susurra como si alguien escuchara",
    "Usa refranes para todo", "Corrige la gramática de los demás", "Muy formal y ceremonioso",
    "Toca constantemente un amuleto",
  ],
  trampas: [
    "Dardos envenenados desde las paredes (daño perforante + CON o envenenado)",
    "Foso oculto con estacas (caída + perforante, DES para evitar)",
    "Bloque que cae del techo (contundente, DES para mitad)",
    "Runa de fuego en el suelo (fuego en área, DES para mitad)",
    "Red que cae y deja apresado (FUE o DES para escapar)",
    "Gas somnífero al abrir un cofre (CON o inconsciente 1 minuto)",
    "Sala que se inunda poco a poco (puzle contrarreloj)",
    "Hoja pendular en un pasillo (cortante, DES para evitar)",
    "Glifo de alarma que despierta a los guardias",
    "Suelo resbaladizo hacia un precipicio (DES o caer)",
  ],
  sensorial: [
    "Olor a humedad y metal oxidado", "Un goteo constante que hace eco", "Huesos pequeños crujen bajo los pies",
    "Corriente de aire frío desde una grieta", "Marcas de garras en las paredes", "Un zumbido grave e incesante",
    "Restos de una hoguera aún tibia", "Musgo que brilla débilmente", "Silencio absoluto: ni insectos",
  ],
  puzles: [
    "Estatuas que deben mirar hacia el símbolo correcto",
    "Puerta que se abre al decir el nombre del fundador (pista en un mural)",
    "Balanza que debe equilibrarse con objetos de la sala",
    "Secuencia de baldosas: solo se pisan las del elemento correcto",
    "Acertijo de un guardián: responder o pagar un precio",
    "Espejos para dirigir un rayo de luz hasta un cristal",
    "Cuatro palancas: el orden está escondido en una canción local",
  ],
  botin: [
    ["2d6 × 10 po", "Poción de curación", "Pergamino de conjuro de nivel 1", "Arma +1 (raro en este tier)", "Joya de 25 po", "Mapa o carta con una pista"],
    ["2d6 × 100 po", "Poción de curación mayor", "Objeto mágico poco común", "Pergamino de nivel 2-3", "Gema de 100 po", "Carta de un villano"],
    ["2d6 × 1000 po", "Poción de curación superior", "Objeto mágico raro", "Pergamino de nivel 4-5", "Objeto de arte de 750 po", "Llave de una cámara sellada"],
    ["2d6 × 10000 po", "Poción de curación suprema", "Objeto mágico muy raro", "Pergamino de nivel 6-8", "Objeto de arte de 7500 po", "Pista hacia un artefacto"],
  ],
};

return { CR_XP, PRESUPUESTO, DIFICULTADES, xpDeCR, presupuesto, calificar, mejorCR, opciones, tier, TRAMPA_CD, TRAMPA_DANO, pick, TABLAS };
