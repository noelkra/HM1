import numpy as np


def run():
    A = np.array([[2.0, 1.0, 0.0],
                  [5.0, 3.0, 2.0],
                  [20.0, 15.0, 10.0]])
    b = np.array([15.0, 47.0, 215.0])
    IT24ta_WIN_01_S06_Aufg2(A, b)


def IT24ta_WIN_01_S06_Aufg2(A, b):
    print("Original matrix A:")
    print(A)
    print()
    print("Original vector b:")
    print(b)
    print()
    print("---- Gaussian elimination ----")
    print()
    # calculate
    A_triangle, b, x = gauss(A, b)
    detA = determinant(A_triangle)

    print("Triangle matrix A:")
    print(A_triangle)
    print()
    print("determinant:")
    print(detA)
    print()
    print("Solution vector x:")
    print(x)

    return A_triangle, detA, x


def gauss(A, b):
    A_triangle, b = gauss_forward(A, b)
    x = back_substitution(A_triangle, b)
    return A_triangle, b, x


# Forward elimination
def gauss_forward(A, b):
    n = len(A)
    for i in range(n):
        if A[i, i] == 0:
            pivot_row = None
            for j in range(i + 1, n):
                if A[j, i] != 0:
                    pivot_row = j
                    break
            if pivot_row is None:
                raise ValueError("Matrix is not regular.")
            # Swap rows
            A[i], A[pivot_row] = A[pivot_row], A[i]
            b[i], b[pivot_row] = b[pivot_row], b[i]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            for k in range(i, n):
                A[j, k] -= factor * A[i, k]
            b[j] -= factor * b[i]

    return A, b


# Back substitution
def back_substitution(A, b):
    n = len(A)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x


def determinant(A):
    n = len(A)
    det = 1.0
    for i in range(n):
        det *= A[i, i]
    return det


run()