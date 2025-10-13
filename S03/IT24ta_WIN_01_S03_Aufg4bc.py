import numpy as np
import matplotlib.pyplot as plt

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
