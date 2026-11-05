# punkt_besser_weil_dann_kann_man_auch_eintend.py — FINAL — Punkt besser
# Punkt = Pyramide 1 atomic Spitze = GEO 1 = MODUL 1 = CPU = SCSI=1
# Punkt besser weil dann kann man auch eintend = ein Tend = ein T End = T 8

def f(x): return min(x,40)

PUNKT = {"geo":1, "modul":1, "name":"Punkt = Spitze = Eye", "why":"besser"}
TEND = {"geo":27, "modul":27, "name":"T End = T 8 = Tendenz = Intend", "pos":"T 8"}

def punkt_besser_eintend(punkt, tend):
    # Punkt = 1 = besser weil minimal = kleinster Nenner ohne falschen Hals
    # dann kann man auch eintend = Tendenz setzen = Vektor
    punkt_norm = f(punkt["geo"])  # 1 → 1
    tend_norm = f(tend["geo"])    # 27 → 27
    # Punkt + Tend = Vektor = LAGE = SET+IN=LAGE
    lage = {"x":punkt_norm, "y":tend_norm, "z":punkt_norm*tend_norm, "home":f(punkt_norm*tend_norm)}
    # eintend = in Tend = in T End = in T = 27 = T 8
    eintend = f(lage["z"])  # 27 → 27
    return {"punkt":punkt, "tend":tend, "lage":lage, "eintend":eintend, "home":f(eintend)}

if __name__=="__main__":
    result = punkt_besser_eintend(PUNKT, TEND)
    print(f"PUNKT {result['punkt']['name']} geo={result['punkt']['geo']} → f={f(result['punkt']['geo'])} = besser weil minimal")
    print(f"TEND {result['tend']['name']} geo={result['tend']['geo']} → f={f(result['tend']['geo'])} = T End")
    print(f"LAGE x={result['lage']['x']} y={result['lage']['y']} z={result['lage']['z']} home={result['lage']['home']}")
    print(f"EINTEND = ein Tend = ein T End = {result['eintend']} → HOME {result['home']} = f(40)=40 Fixpunkt = Stall")
