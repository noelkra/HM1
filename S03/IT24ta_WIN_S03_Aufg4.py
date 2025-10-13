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


# Aufgabe b)

# h(x) = sqrt(100x^2 - 200x + 99)
# Rel. Kondition (Skript-Def.): K(x) = |x * h'(x) / h(x)|.  :contentReference[oaicite:0]{index=0}
# Mit h'(x) = 100(x-1)/sqrt(100x^2 - 200x + 99) folgt
# ⇒ K(x) = | 100 * x * (x-1) / (100x^2 - 200x + 99) |.
# Diese Form vermeidet, h(x) separat zu berechnen (stabiler).

def K(x):
    D = 100.0*x*x - 200.0*x + 99.0            # D(x) = 100x^2−200x+99 = (10x−10)^2−1: Ausdruck unter der Wurzel von h(x)
    out = np.empty_like(x)                    # Ergebnis-Array anlegen (gleiche Form/Typ wie x) für K(x)
    m = D > 0.0                               # Maske: wo D>0 ist h(x)=sqrt(D) definiert; bei x=1.1 gilt D=0 ⇒ Pol (K=∞)
    out[~m] = np.nan                          # An nicht definierten Stellen (D≤0) NaN setzen, damit der Plot nichts zeichnet
    out[m]  = np.abs(100.0 * x[m] * (x[m] - 1.0) / D[m])  # Formel K=|x*h'(x)/h(x)| mit h'(x)=100(x−1)/sqrt(D), h=sqrt(D):
                                                         # K=|100·x·(x−1)/D|; nur auf gültigen Punkten m berechnen
    return out                                # Vektor der Konditionswerte zurückgeben

dx = 1e-7
# Bereich [1.1, 1.3] mit Δx = 1e-7; Start >1.1, damit D>0 (sonst Division durch 0)
x  = np.arange(1.1 + dx, 1.3 + 0.5*dx, dx)
Kx = K(x)

plt.semilogy(x, Kx)
plt.title(r"Kondition $K(x)$ von $h(x)=\sqrt{100x^2-200x+99}$  (Δx=$10^{-7}$)")
plt.xlabel("x")
plt.ylabel(r"$K(x)=|x\,h'(x)/h(x)|$")
plt.show()

# (c) Aussage zur Auslöschung & Kondition:
# - Relativer Fehler in f(x) verstärkt sich näherungsweise mit K(x). Große K ⇒ schlecht konditioniert,
#   algebraische Umformungen können die Empfindlichkeit nicht grundsätzlich beheben.
# - Bei x=1.1 wird der Nenner 100x^2 - 200x + 99 = 0 ⇒ K(1.1) = ∞. Schlechte Kondition ist intrinsisch.
#   Auslöschung (Subtraktion fast gleicher Zahlen) kann man numerisch entschärfen, aber die schlechte Kondition
#   nahe x=1.1 bleibt.
