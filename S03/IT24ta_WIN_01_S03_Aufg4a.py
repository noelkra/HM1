import numpy as np
import matplotlib.pyplot as plt

# Aufgabe a)

# h(x) = sqrt(100x^2 − 200x + 99) = sqrt((10x−10)^2 − 1) = sqrt((10x−11)(10x−9)).
# Für x ≈ 1.1 ist t := 10x−10 ≈ 1, also (10x−10)^2 ≈ 1 ⇒ die Differenz t^2−1 subtrahiert zwei fast gleiche Zahlen.
# Solche Subtraktionen sind schlecht konditioniert: kleine Rundungsfehler der Operanden werden stark verstärkt
# (klassische „Auslöschung“/cancellation). Auslöschung bei Addition/Subtraktion mit fast gleichem Betrag,
# Konditionszahl K(x) = |x|/|x+c| wird groß, wenn |x+c| klein ist.
# Dadurch ist die direkte Auswertung sqrt((10x−10)^2 − 1) nahe 1.1 numerisch instabil. Empfehlung: faktorisieren
# und als Produkt auswerten: sqrt((10x−11)(10x−9)); hier wird kein kleine Differenz gebildet → stabiler. 

# h(x) = sqrt((10x-10)^2 - 1)  → nahe x≈1.1 ist (10x-10)^2 ≈ 1 ⇒ Auslöschung in t^2-1.
# Stabil: benutze Faktorzerlegung t^2-1=(t-1)(t+1) = (10x-11)(10x-9).

def h_naiv(x):
    t = 10.0*x - 10.0
    return np.sqrt(t*t - 1.0)

def h_stabil(x):
    t = 10.0*x - 10.0
    return np.sqrt((t-1.0)*(t+1.0))  # vermeidet die Differenz fast gleicher Zahlen

# Bereich knapp über 1.1 (damit Ausdruck > 0 bleibt)
x = np.linspace(1.1000000001, 1.1005, 400)
y_naiv  = h_naiv(x)
y_stab  = h_stabil(x)
rel_err = np.abs((y_naiv - y_stab) / y_stab)

# Plot 1: h(x) naiv vs. stabil (zeigt gleiche Kurve, aber naiv ist numerisch anfälliger)
plt.figure()
plt.plot(x, y_naiv, label="naiv: √((10x−10)^2 − 1)")
plt.plot(x, y_stab, '--', label="stabil: √((10x−11)(10x−9))")
plt.title("Auslöschung bei h(x) nahe x=1.1: Differenz vs. Produkt")
plt.xlabel("x"); plt.ylabel("h(x)")
plt.legend(); plt.grid(True); plt.show()

# Plot 2: relative Abweichung (belegt die numerische Empfindlichkeit der naiven Form)
plt.figure()
plt.plot(x, rel_err)
plt.title("Relative Abweichung: naive − stabile Auswertung")
plt.xlabel("x"); plt.ylabel("relativer Fehler")
plt.grid(True); plt.show()