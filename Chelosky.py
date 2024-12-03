import numpy as np
import time  # Import time module for measuring execution time

class Cholesky_Decomposition:
    def __init__(self, A, B, precision=6, steps=False):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)
        self.n = len(A)
        self.L = np.zeros_like(self.A)
        self.precision = precision
        self.steps = steps
        self.ans_str = ""

    def is_symmetric(self):
        """Check if the matrix is symmetric."""
        if not np.allclose(self.A, self.A.T):
            print("Not symmetric")
            return False
        return True

    def is_positive_definite(self):
        """Check if the matrix is positive definite by testing if all the leading principal minors are positive."""
        try:
            np.linalg.cholesky(self.A)
            return True
        except np.linalg.LinAlgError:
            print("Not positive semi-definite")
            return False

    def round_significant(self, value, digits):
        """Round the value to the specified number of significant digits."""
        if value == 0:
            return 0
        else:
            return round(value, digits - int(np.floor(np.log10(abs(value)))) - 1)

    def decompose(self):
        """Cholesky decomposition: A = LL^T"""
        if not self.is_symmetric():
            raise ValueError("Matrix is not symmetric.")
        if not self.is_positive_definite():
            raise ValueError("Matrix is not positive definite.")
        
        for i in range(self.n):
            for j in range(i + 1):
                sum_L = 0
                if j == i:  # Diagonal elements
                    for k in range(i):
                        sum_L += self.L[i][k] ** 2
                    self.L[i][i] = np.sqrt(self.A[i][i] - sum_L)
                else:  # Off-diagonal elements
                    for k in range(j):
                        sum_L += self.L[i][k] * self.L[j][k]
                    self.L[i][j] = (self.A[i][j] - sum_L) / self.L[j][j]
                
                # Apply significant digits rounding
                self.L[i][j] = self.round_significant(self.L[i][j], self.precision)

                if self.steps:
                    print(f"L[{i+1},{j+1}] = {self.L[i][j]:.{self.precision}f}")
            
            if self.steps:
                self.display_matrix(self.L)
                print(f"After Step {i+1}:\n")
        
        return self.L

    def forward_substitution(self, L, B):
        """Solve L * Y = B using forward substitution."""
        n = len(L)
        Y = np.zeros(n)

        print("Solving L * Y = B...")
        self.ans_str += "Solving L * Y = B...\n"

        for i in range(n):
            sum_ly = 0
            for j in range(i):
                sum_ly += L[i][j] * Y[j]
            Y[i] = (B[i] - sum_ly) / L[i][i]

            # Apply significant digits rounding
            Y[i] = self.round_significant(Y[i], self.precision)

            if self.steps:
                print(f"Step {i+1}: Y[{i+1}] = ({B[i]:.{self.precision}f} - ({sum_ly:.{self.precision}f})) / {L[i][i]:.{self.precision}f} = {Y[i]:.{self.precision}f}")
                self.ans_str += f"Step {i+1}: Y[{i+1}] = ({B[i]:.{self.precision}f} - ({sum_ly:.{self.precision}f})) / {L[i][i]:.{self.precision}f} = {Y[i]:.{self.precision}f}\n"

        print(f"Y Vector: {Y}\n")
        self.ans_str += f"Y Vector: {Y}\n"
        return Y

    def back_substitution(self, L, Y):
        """Solve L^T * X = Y using back substitution."""
        n = len(L)
        X = np.zeros(n)

        print("Solving L^T * X = Y...")
        self.ans_str += "Solving L^T * X = Y...\n"

        for i in range(n - 1, -1, -1):
            sum_lx = 0
            for j in range(i + 1, n):
                sum_lx += L[j][i] * X[j]
            X[i] = (Y[i] - sum_lx) / L[i][i]

            # Apply significant digits rounding
            X[i] = self.round_significant(X[i], self.precision)

            if self.steps:
                print(f"Step {n-i}: X[{i+1}] = ({Y[i]:.{self.precision}f} - ({sum_lx:.{self.precision}f})) / {L[i][i]:.{self.precision}f} = {X[i]:.{self.precision}f}")
                self.ans_str += f"Step {n-i}: X[{i+1}] = ({Y[i]:.{self.precision}f} - ({sum_lx:.{self.precision}f})) / {L[i][i]:.{self.precision}f} = {X[i]:.{self.precision}f}\n"

        print(f"Solution Vector X: {X}\n")
        self.ans_str += f"Solution Vector X: {X}\n"
        return X

    def display_matrix(self, L):
        """Display the current state of L matrix."""
        print("L Matrix:")
        for row in L:
            print(" ".join([f"{val:.{self.precision}f}" for val in row]))
        print("-" * 50)

    def solve(self):
        """Solve the system of equations using Cholesky Decomposition."""
        start_time = time.time()  # Start timing
        
        # Perform Cholesky Decomposition
        L = self.decompose()

        # Solve L * Y = B
        Y = self.forward_substitution(L, self.B)

        # Solve L^T * X = Y
        X = self.back_substitution(L, Y)
        
        end_time = time.time()  # End timing
        print(f"\nExecution Time: {end_time - start_time:.6f} seconds")
        return X


# Test the Cholesky_Decomposition class
if __name__ == "__main__":
    A = [
        [6, 3, 4, 0],
        [3, 6, 5, 0],
        [4, 5, 10, 0],
        [0, 0, 0, 12]
    ]
    B = [0, 0, 0, 5]

    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6

    steps_choice = input("Show steps during calculation? (y/n, default n): ").strip().lower()
    steps = steps_choice == 'y'

    try:
        solver = Cholesky_Decomposition(A, B, precision=precision, steps=steps)
        X = solver.solve()

        print("\nFinal Solution:")
        for i, val in enumerate(X):
            print(f"x{i+1} = {val:.{precision}f}")
    
    except ValueError as e:
        print(e)
