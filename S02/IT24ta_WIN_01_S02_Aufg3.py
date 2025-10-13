import math
import matplotlib.pyplot as plt

def teilaufgabe_a():
    n = 6
    s_n = 1.0
    u = n * s_n
    resultsA = [(n, s_n, u)]

    for _ in range(20):
        s_2n = math.sqrt(2-2*math.sqrt(1-((s_n**2)/4)))
        n *= 2
        u_neu = n * s_2n

        # Fehler ausgeben:
        print(f"n: {n}, s_n: {s_2n:.16f}, U_n: {u_neu:.16f}, |U_n-2π|: {abs(u_neu - 2*math.pi):.3e}")

        resultsA.append((n, s_2n, u_neu))
        if abs(u_neu - u) < 1e-10:
            break
        s_n, u = s_2n, u_neu
    return resultsA

def teilaufgabe_b():
    n = 6
    s_n = 1.0
    u = n * s_n
    resultsB = [(n, s_n, u)]

    for _ in range(20):
        s_2n = math.sqrt((s_n**2)/(2 * (1+ math.sqrt(1-((s_n**2)/4)))))
        n *= 2
        u_neu = n * s_2n

        # Fehler ausgeben:
        print(f"n: {n}, s_n: {s_2n:.16f}, U_n: {u_neu:.16f}, |U_n-2π|: {abs(u_neu - 2 * math.pi):.3e}")

        resultsB.append((n, s_2n, u_neu))
        if abs(u_neu - u) < 1e-10:
            break
        s_n, u = s_2n, u_neu
    return resultsB

resultsA = teilaufgabe_a()
resultsB = teilaufgabe_b()

nsA = [n for n,_,_ in resultsA]
usA = [u for _,_,u in resultsA]
nsB = [n for n,_,_ in resultsB]
usB = [u for _,_,u in resultsB]

plt.plot(nsA, usA, marker='o', label='Methode A')
plt.plot(nsB, usB, marker='x', label='Methode B')
plt.xscale('log', base=2)
plt.axhline(2 * math.pi, ls="--", label='2π')
plt.xlabel("n")
plt.ylabel("U_n = n · s_n")
plt.title("Annäherung an Pi")
plt.grid(True)
plt.legend()
plt.show()