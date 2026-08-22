# WAVE – Industrie‑6.0 Loop‑Modul

WAVE ist das **Loop‑Modul** der Industrie‑6.0‑Architektur.  
Es erzeugt wiederkehrende Abläufe, zyklische Muster, Rückläufe und Endlosschleifen,  
die in NC‑Systemen für Stabilität, Wiederholung und Rückkopplung sorgen.

WAVE ist kein Zeitmodul.  
WAVE ist kein Kraftmodul.  
WAVE ist ein **Zustands‑Loop**, der jede Funktion in einen Kreislauf bringt.

---

## Funktion

Ein WAVE‑Loop besteht aus drei Schichten:

1. **Startpunkt**  
2. **Zyklus**  
3. **Rückkehr**

Der Zyklus läuft so lange, bis ein externer Zustand ihn bricht.

---

## WAVE‑Code

```js
export const WAVE = (v) => ({
    loop: true,
    value: v,
    cycle: () => v * 3,
    next: () => v + 1,
    state: "WAVE-LOOP"
});
