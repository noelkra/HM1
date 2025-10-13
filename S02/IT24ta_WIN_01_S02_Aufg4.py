# Name_S02_Aufg4.py

def berechne_maschinengenauigkeit():
    eps = 1.0
    while 1.0 + eps != 1.0:
        eps /= 2.0
    eps *= 2.0
    return eps

def berechne_qmin():
    qmin = 1.0
    while (qmin / 2.0) > 0.0:
        qmin /= 2.0
        if 1.0 + qmin == qmin:
            break
    return qmin

def anzahl_signifikante_stellen(eps):
    import math
    return int(-math.log10(eps))

eps = berechne_maschinengenauigkeit()
qmin = berechne_qmin()
stellen = anzahl_signifikante_stellen(eps)

print(f"Maschinengenauigkeit (eps): {eps}")
print(f"Signifikante Dezimalstellen: {stellen}")
print(f"Kleinstmögliche positive Maschinenzahl (qmin): {qmin}")
print("Zusammenhang: qmin ist die kleinste positive Zahl, die noch von 0 unterscheidbar ist,")
print("während eps die kleinste Zahl ist, die zu 1 addiert noch einen Unterschied macht.")
