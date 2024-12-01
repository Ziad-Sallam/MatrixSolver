import sympy as sp
import time  # Importing time module for execution time measurement

class LU_Decomposition_Symbolic:
    def __init__(self, A, B, steps=False):
        self.A = sp.Matrix(A)
        self.B = sp.Matrix(B)
        self.n = self.A.shape[0]
        self.L = sp.zeros(self.n, self.n)
        self.U = sp.zeros(self.n, self.n)
        self.steps = steps
        self.ans_str = ""

    def decompose(self):
        """LU decomposition (L and U matrices) using the Crout method symbolically"""
        for i in range(self.n):
            # Calculate L[i, j] elements
            for j in range(i + 1):
                sum_LU = sum(self.L[i, k] * self.U[k, j] for k in range(j))
                self.L[i, j] = self.A[i, j] - sum_LU
                if self.steps:
                    print(f"L[{i+1},{j+1}] = {self.L[i, j]}")

            # Calculate U[i, j] elements
            for j in range(i, self.n):
                if self.L[i, i] != 0:
                    sum_LU = sum(self.L[i, k] * self.U[k, j] for k in range(i))
                    self.U[i, j] = (self.A[i, j] - sum_LU) / self.L[i, i]
                    if self.steps:
                        print(f"U[{i+1},{j+1}] = {self.U[i, j]}")

            # Display matrices at each step if needed
            if self.steps:
                self.display_matrices()

        return self.L, self.U

    def forward_substitution(self, L, B):
        """Solve L * Y = B symbolically using forward substitution."""
        Y = sp.zeros(self.n, 1)

        for i in range(self.n):
            sum_ly = sum(L[i, j] * Y[j] for j in range(i))
            Y[i] = (B[i] - sum_ly) / L[i, i]
            if self.steps:
                print(f"Y[{i+1}] = {Y[i]}")

        return Y

    def back_substitution(self, U, Y):
        """Solve U * X = Y symbolically using back substitution."""
        X = sp.zeros(self.n, 1)

        for i in reversed(range(self.n)):
            sum_ux = sum(U[i, j] * X[j] for j in range(i + 1, self.n))
            X[i] = (Y[i] - sum_ux) / U[i, i]
            if self.steps:
                print(f"X[{i+1}] = {X[i]}")

        return X

    def display_matrices(self):
        """Display the current state of L and U matrices."""
        print("L Matrix:")
        sp.pprint(self.L)
        print("\nU Matrix:")
        sp.pprint(self.U)
        print("-" * 50)

    def solve(self):
        """Solve the system of equations symbolically using LU Decomposition."""
        start_time = time.time()  # Start timing

        # Perform LU Decomposition
        L, U = self.decompose()

        # Solve L * Y = B
        Y = self.forward_substitution(L, self.B)

        # Solve U * X = Y
        X = self.back_substitution(U, Y)

        # End timing and print execution time
        print(f"Execution Time: {time.time() - start_time:.6f} seconds")
        return X


# Test the LU_Decomposition_Symbolic class
if __name__ == "__main__":
    # Example symbolic input
    A = [
        ["a", "b", "c"],
        ["0", "b", "0"],
        ["0", "b", "c"]
    ]
    B = ["x", "y", "z"]

    # User choice to show steps or not
    steps_choice = input("Show steps during calculation? (y/n, default n): ").strip().lower()
    steps = steps_choice == 'y'

    # Create an instance of the LU_Decomposition_Symbolic class
    solver = LU_Decomposition_Symbolic(A, B, steps=steps)

    # Solve the system
    X = solver.solve()

    print("\nFinal Solution (Symbolic):")
    sp.pprint(X)
