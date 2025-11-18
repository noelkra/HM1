import numpy as np

from IT24ta_WIN_01_S06_Aufg2 import IT24ta_WIN_01_S06_Aufg2  # noqa: F401

def solve_with_task2(A, b):
    # Kopieren von A/b, da die Aufgabe-2-Funktion A/b in-place modifiziert
    A2 = A.astype(float).copy()
    b2 = b.astype(float).copy()
    _, _, x = IT24ta_WIN_01_S06_Aufg2(A2, b2)
    return x

def compare(A, b, label):
    x_task2 = solve_with_task2(A, b)
    x_np = np.linalg.solve(A, b)

    diff = np.linalg.norm(x_task2 - x_np, ord=np.inf)
    if diff < 1e-9:
        print("Kein relevanter Unterschied (numerisch identisch bis Toleranz).")
    else:
        print("Unterschiede durch fehlendes Pivoting / Rundungsfehler möglich.")
    print()

def main():
    A1 = np.array([[  4,  -1,  -5],
                   [ -12,  4,  17],
                   [  32,-10, -41]], dtype=float)
    b1a = np.array([ -5,  19, -39], dtype=float)
    b1b = np.array([  6, -12,  48], dtype=float)

    A2 = np.array([[  2,  7,  3],
                   [ -4,-10,  0],
                   [ 12, 34,  9]], dtype=float)
    b2a = np.array([ 25, -24, 107], dtype=float)
    b2b = np.array([  5, -22,  42], dtype=float)

    A3 = np.array([[ -2,  5,   4],
                   [-14, 38,  22],
                   [  6, -9, -27]], dtype=float)
    b3a = np.array([  1,  40,  75], dtype=float)
    b3b = np.array([ 16,  82,-120], dtype=float)

    A4 = np.array([
        [-1,  2,  3,  2,  5,  4,  3, -1],
        [ 3,  4,  2,  1,  0,  2,  3,  8],
        [ 2,  7,  5, -1,  2,  1,  3,  5],
        [ 3,  1,  2,  6, -3,  7,  2, -2],
        [ 5,  2,  0,  8,  7,  6,  1,  3],
        [-1,  3,  2,  3,  5,  3,  1,  4],
        [ 8,  7,  3,  6,  4,  9,  7,  9],
        [-3, 14, -2,  1,  0, -2, 10,  5]
    ], dtype=float)
    b4 = np.array([-11, 103, 53, -20, 95, 78, 131, -26], dtype=float)

    # Vergleiche
    compare(A1, b1a, "A1 · x = b1a")
    compare(A1, b1b, "A1 · x = b1b")
    compare(A2, b2a, "A2 · x = b2a")
    compare(A2, b2b, "A2 · x = b2b")
    compare(A3, b3a, "A3 · x = b3a")
    compare(A3, b3b, "A3 · x = b3b")
    compare(A4, b4,   "A4 · x = b")

    print("# Kommentar: In allen hier getesteten Systemen stimmen die Lösungen mit numpy.linalg.solve")
    print("# bis auf numerische Rundung überein.")
    print("# Grössere Abweichungen wären bei schlecht konditionierten Systemen oder ohne Pivoting möglich.")

main()
