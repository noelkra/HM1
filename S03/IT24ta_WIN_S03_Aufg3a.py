import numpy as np
import matplotlib.pyplot as plt

c = 1
a = 2
x_lin = np.linspace(0, 100, 400)

# Exponentialfunktion
def f(x):
    return c * a**x

# Potenzfunktion
def g(x):
    return c * x**a

# Teilaufgabe a
plt.title("f(x)")
plt.semilogy(x_lin, f(x_lin))
plt.show()

plt.title("g(x)")
plt.loglog(x_lin, g(x_lin))
plt.xlim(1, 100)
plt.show()
