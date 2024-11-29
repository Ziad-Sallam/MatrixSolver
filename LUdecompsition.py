import numpy as np
import time

class LUDecomposition:
    def __init__(self, A_Matrix, B_Matrix, significant_digits=6):
        self.A_Matrix = np.array(A_Matrix)
        self.B_Matrix = np.array(B_Matrix)
        self.significant_digits = significant_digits
        self.n = len(B_Matrix)  # Number of equations (rows)
        self.x = np.zeros(self.n)  # Solution array

    def validate_input(self):  # To ensure the validity of input matrices
        if self.A_Matrix.shape[0] != self.A_Matrix.shape[1]:
            return False
        if self.B_Matrix.shape[1] > 1 or self.B_Matrix.shape[0] != self.A_Matrix.shape[0]:
            return False
        return True

    def lu_decomposition(self):
        A = self.A_Matrix.copy()
        L = np.zeros_like(A)
        U = np.zeros_like(A)

        for i in range(self.n):
            # Upper Triangular Matrix (U)
            U[i, i:] = A[i, i:] - np.dot(L[i, :i], U[:i, i:])
            # Lower Triangular Matrix (L)
            if i < self.n - 1:
                L[i + 1:, i] = (A[i + 1:, i] - np.dot(L[i + 1:, :i], U[:i, i])) / U[i, i]

        # Set diagonal elements of L to 1
        np.fill_diagonal(L, 1)
        return L, U

    def forward_substitution(self, L, b):
        y = np.zeros_like(b)
        for i in range(self.n):
            y[i] = b[i] - np.dot(L[i, :i], y[:i])
        return y

    def backward_substitution(self, U, y):
        x = np.zeros_like(y)
        for i in range(self.n - 1, -1, -1):
            x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
        return x

    def solve(self):
        np.set_printoptions(suppress=True, formatter={'all': lambda x: f'{x:.{self.significant_digits}f}'})

        if self.validate_input():
            start_time = time.time()

            L, U = self.lu_decomposition()
            print(f"Lower Triangular Matrix (L):\n{np.round(L, self.significant_digits)}")
            print(f"Upper Triangular Matrix (U):\n{np.round(U, self.significant_digits)}")
            print("----------------------------------------------------")

            # Solve L * y = B
            y = self.forward_substitution(L, self.B_Matrix)

            # Solve U * x = y
            self.x = self.backward_substitution(U, y)

            for answer in range(self.n):
                print(f"X{answer} is {np.round(self.x[answer], self.significant_digits)}")
            print("----------------------------------------------------")

            end_time = time.time()
            self.execution_time = end_time - start_time
            print(f"Execution Time: {self.execution_time:.6f} seconds")
        else:
            print("Invalid Input")


# Example:
matrix1 = [[25, 5, 1, 5],
           [64, 8, 1, 4],
           [144, 12, 1, 3],
           [2.22, 33.57, 12, 12]]

matrix2 = [[106.8],
           [2],
           [279.2],
           [301.254]]

# Instantiate the LUDecomposition class and solve the system
solver = LUDecomposition(matrix1, matrix2, significant_digits=5)
solver.solve()