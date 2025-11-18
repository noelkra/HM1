import numpy as np
import matplotlib.pyplot as plt

print("--- Aufgabe 3: UV-Belastung Hawaii ---")

jahre_original = np.array([1997, 1999, 2006, 2010])
tage = np.array([150, 104, 172, 152])
x_verschoben = jahre_original - 1997
grad = 3
b = tage
x = x_verschoben
polynom_grad = 3

################################################################################################################
print("\n--- Aufgabe a ---")

col_x3 = x**3
col_x2 = x**2
col_x1 = x**1
col_x0 = x**0

A = np.column_stack([col_x3, col_x2, col_x1, col_x0])
b = tage


koeffizienten_a = np.linalg.solve(A, b)
print(f"\nKoeffizienten aus LGS (np.linalg.solve):\n{koeffizienten_a}")

x_plot_verschoben = np.arange(min(x_verschoben), max(x_verschoben) + 0.1, 0.1)
y_plot_a = np.polyval(koeffizienten_a, x_plot_verschoben)

x_plot_original = x_plot_verschoben + 1997

plt.figure(figsize=(10, 6))
plt.plot(x_plot_original, y_plot_a, label='Polynom 3. Grades (aus LGS)', color='blue', zorder=2)
plt.plot(jahre_original, tage, 'o', label='Datenpunkte', color='red', markersize=8, zorder=3)
plt.xlabel('Jahr')
plt.ylabel('Anzahl Tage')
plt.title('Extreme UV-Belastung auf Hawaii')
plt.grid(True, zorder=1)

################################################################################################################
print("\n--- Aufgabe b ---")

jahre_schaetzung = np.array([2003, 2004])
x_schaetzung_verschoben = jahre_schaetzung - 1997
print(f"Verschobene x-Werte für Schätzung: {x_schaetzung_verschoben}")

schaetzwerte_b = np.polyval(koeffizienten_a, x_schaetzung_verschoben)

print(f"Schätzwert für {jahre_schaetzung[0]} (x={x_schaetzung_verschoben[0]}): {schaetzwerte_b[0]:.2f} Tage")
print(f"Schätzwert für {jahre_schaetzung[1]} (x={x_schaetzung_verschoben[1]}): {schaetzwerte_b[1]:.2f} Tage")

################################################################################################################
print("\n--- Aufgabe c ---")

koeffizienten_c = np.polyfit(x_verschoben, tage, polynom_grad)
print(f"\nKoeffizienten aus (np.polyfit):\n{koeffizienten_c}")

vergleich = np.allclose(koeffizienten_a, koeffizienten_c)
print(f"Koeffizienten aus a) und c) sind identisch: {vergleich}")

schaetzwerte_c = np.polyval(koeffizienten_c, x_schaetzung_verschoben)

print(f"Schätzwert (polyfit) für {jahre_schaetzung[0]} (x={x_schaetzung_verschoben[0]}): {schaetzwerte_c[0]:.2f} Tage")
print(f"Schätzwert (polyfit) für {jahre_schaetzung[1]} (x={x_schaetzung_verschoben[1]}): {schaetzwerte_c[1]:.2f} Tage")

y_plot_c = np.polyval(koeffizienten_c, x_plot_verschoben)
plt.plot(x_plot_original, y_plot_c, '--', label='Polynom 3. Grades (aus polyfit)', color='lime', linewidth=3, zorder=1)

plt.plot(jahre_schaetzung, schaetzwerte_c, 'x', color='green', markersize=12, mew=3, label='Schätzwerte 2003/2004',
         zorder=4)

plt.legend()
plt.show()

print("\n--- Fazit ---")
print("Wie im Plot zu sehen ist, überlagern sich die blaue Linie (LGS) und die")
print("hellgrüne, gestrichelte Linie (polyfit) exakt. Beide Methoden führen")
print("zum selben Polynom und denselben Schätzwerten.")