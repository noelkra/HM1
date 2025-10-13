import numpy as np
import matplotlib.pyplot as plt

x_lin = np.linspace(1e-8, 100, 400)
x_pos = np.logspace(-3, 2, 400)

def fb(x):
    return 5.0 / np.cbrt(2.0 * x**2)

def gb(x):
    return 10.0**5 * (2.0 * np.e)**(-x/100.0)

def hb(x):
    return ((20**(2*x))/(2**(5*x)))**2


# fb: Potenz -> loglog
plt.loglog(x_pos, fb(x_pos))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("fb (loglog)")
plt.show()

# gb: Exponential -> semilogy
plt.semilogy(x_lin, gb(x_lin))
plt.xlabel("x")
plt.ylabel("g(x)")
plt.title("gb (semilogy)")
plt.show()

# hb: Exponential -> semilogy
plt.semilogy(x_lin, hb(x_lin))
plt.xlabel("x")
plt.ylabel("h(x)")
plt.title("hb (semilogy)")
plt.show()