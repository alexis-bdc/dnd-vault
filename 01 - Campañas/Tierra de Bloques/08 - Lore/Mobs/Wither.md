---
statblock: true
tipo: mob
campaña: "Tierra de Bloques"
name: "Wither"
size: "Large"
type: "undead"
alignment: "lawful evil"
ac: 19
hp: 225
hit_dice: "18d10+126"
speed: "9 m, excavar 9 m, volar 9 m (flotar)"
stats: [19, 26, 25, 16, 21, 23]
saves: [{"constitution": 12}, {"wisdom": 10}]
damage_resistances: "contundente, perforante y cortante de ataques no mágicos"
damage_immunities: "fuego, necrótico, veneno"
condition_immunities: "hechizado, agotamiento, asustado, paralizado, envenenado"
senses: "visión verdadera 36 m, Percepción pasiva 15"
languages: "común, habla profunda, telepatía 36 m"
cr: "16"
traits: [{"name": "Alturas marchitas (rasgo mítico; 1/descanso)", "desc": "Si fuera a quedar a 0 PG, sus PG vuelven a 225. Entonces provoca una gran explosión: cada criatura a 6 m hace una TS de DES CD 19, recibe 28 (8d6) contundente si falla (la mitad si la supera) y es empujada hasta 6 m en línea recta. El wither pierde su velocidad de vuelo durante 1 hora, pero sus otras velocidades se duplican."}, {"name": "Aura de no vida", "desc": "Emite un aura de energía negativa de 9 m de radio. Las criaturas que no sean muertas vivientes en el área no pueden recuperar PG y tienen desventaja en las TS de muerte."}, {"name": "Excavación destructiva", "desc": "Puede excavar a través de cualquier material o estructura no mágica y deja un túnel de 3 m de diámetro."}, {"name": "Libertad de movimiento", "desc": "Ignora el terreno difícil, y los efectos mágicos no pueden reducir su velocidad ni dejarlo apresado. Puede gastar 1,5 m de movimiento para escapar de ataduras no mágicas o de un agarre."}, {"name": "Monstruo de asedio", "desc": "Hace el doble de daño a objetos y estructuras."}, {"name": "Tres cabezas", "desc": "Tiene ventaja en las pruebas de Sabiduría (Percepción) y en las TS contra quedar cegado, ensordecido, aturdido o inconsciente."}, {"name": "Wither", "desc": "Cuando una criatura falla su TS contra un cráneo de wither, queda envenenada. Al final de cada uno de sus turnos hace una TS de CON CD 20: si falla, recibe 7 (2d6) necrótico; si la supera, el efecto termina. Mientras esté envenenada así, no puede recuperar PG."}]
actions: [{"name": "Alarido", "desc": "Cada criatura que no sea muerta viviente a 36 m y pueda oírlo hace una TS de CON CD 19 o queda asustada hasta el final del siguiente turno del wither."}, {"name": "Invocar engendro", "desc": "Un esqueleto wither surge del suelo en un punto a 9 m. Actúa en el mismo turno que el wither y obedece sus órdenes. Puede tener como máximo cuatro esqueletos wither invocados a la vez."}, {"name": "Carga explosiva (Recarga 5–6)", "desc": "Se mueve hasta su velocidad en línea recta, atravesando el espacio de las criaturas sin provocar ataques de oportunidad. Cada criatura a 3 m de cualquier espacio por el que pase hace una TS de FUE CD 21: recibe 14 (4d6) contundente si falla (la mitad si la supera) y, si falla, queda derribada."}]
reactions: [{"name": "Alimentarse de la debilidad", "desc": "Cuando una criatura que no sea muerta viviente a 9 m falla una TS o queda a 0 PG, el wither recupera 20 PG o gana ventaja en su siguiente TS."}, {"name": "Ejército no muerto", "desc": "Cuando muere un humanoide a 9 m, puede usar Invocar engendro para alzar su cadáver como esqueleto wither. Este no cuenta para el máximo de cuatro."}]
legendary_description: "El wither puede hacer 3 acciones legendarias, elegidas entre las siguientes. Solo una a la vez, al final del turno de otra criatura. Recupera las acciones gastadas al inicio de su turno."
legendary_actions: [{"name": "Moverse", "desc": "Se mueve hasta la mitad de su velocidad."}, {"name": "Cráneo de wither", "desc": "Lanza un cráneo de wither hacia un punto a 36 m. Al llegar o chocar con una superficie sólida, explota: cada criatura y objeto a 4,5 m hace una TS de CON CD 20 y recibe 14 (4d6) necrótico si falla, o la mitad si la supera."}]
tags: [dnd/mob, dnd/dm]
---

# Wither

Jefe opcional. Se invoca con 3 cráneos de esqueleto wither y 4 bloques de arena de almas.

```statblock
monster: Wither
```

*Fuente: Badooga's Homebrew (Minecraft 5e.pdf).* ↩ [[Bestiario]]
