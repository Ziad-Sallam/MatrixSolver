import numpy as np
import time  # Importing time module for execution time measurement

class LU_Decomposition:
    def __init__(self, A, B, precision=6, steps=False):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)
        self.n = len(A)
        self.L = np.zeros_like(self.A)
        self.U = np.zeros_like(self.A)
        self.precision = precision
        self.steps = steps
        self.ans_str = ""

    def decompose(self):
        """LU decomposition (L and U matrices) using the Crout method"""
        for i in range(self.n):
            # Calculate L[i, j] elements
            for j in range(i + 1):
                sum_LU = 0
                for k in range(j):
                    sum_LU += self.L[i][k] * self.U[k][j]
                self.L[i][j] = self.A[i][j] - sum_LU
                # Print L matrix elements at each step
                if self.steps:
                    print(f"L[{i+1},{j+1}] = {self.L[i][j]:.{self.precision}f}")

            # Calculate U[i, j] elements
            for j in range(i, self.n):
                if self.L[i][i] != 0:
                    sum_LU = 0
                    for k in range(i):
                        sum_LU += self.L[i][k] * self.U[k][j]
                    self.U[i][j] = (self.A[i][j] - sum_LU) / self.L[i][i]
                    # Print U matrix elements at each step
                    if self.steps:
                        print(f"U[{i+1},{j+1}] = {self.U[i][j]:.{self.precision}f}")

            # Display the matrices after each step
            if self.steps:
                self.display_matrices(self.L, self.U)
                print(f"After Step {i+1}:\n")

        return self.L, self.U

    def check_for_solution(self):
        """Check if the system has no solution or infinitely many solutions."""
        # Check for zero rows in U or L
        for i in range(self.n):
            if np.allclose(self.L[i], 0) and not np.allclose(self.B[i], 0):
                print("No solution: Row in L is zero, but corresponding B is non-zero.")
                return False
            if np.allclose(self.U[i], 0) and not np.allclose(self.B[i], 0):
                print("No solution: Row in U is zero, but corresponding B is non-zero.")
                return False
            if np.allclose(self.U[i], 0) and np.allclose(self.B[i], 0):
                print("Infinite solutions: Row in U is zero and corresponding B is zero.")
                return None  # Infinite solutions

        return True  # The system can be solved

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

            if self.steps:
                print(f"Step {i+1}: Y[{i+1}] = ({B[i]:.{self.precision}f} - ({sum_ly:.{self.precision}f})) / {L[i][i]:.{self.precision}f} = {Y[i]:.{self.precision}f}")
                self.ans_str += f"Step {i+1}: Y[{i+1}] = ({B[i]:.{self.precision}f} - ({sum_ly:.{self.precision}f})) / {L[i][i]:.{self.precision}f} = {Y[i]:.{self.precision}f}\n"

        print(f"Y Vector: {Y}\n")
        self.ans_str += f"Y Vector: {Y}\n"
        return Y

    def back_substitution(self, U, Y):
        """Solve U * X = Y using back substitution."""
        n = len(U)
        X = np.zeros(n)

        print("Solving U * X = Y...")
        self.ans_str += "Solving U * X = Y...\n"

        for i in range(n - 1, -1, -1):
            sum_ux = 0
            for j in range(i + 1, n):
                sum_ux += U[i][j] * X[j]
            X[i] = (Y[i] - sum_ux) / U[i][i]

            if self.steps:
                print(f"Step {n-i}: X[{i+1}] = ({Y[i]:.{self.precision}f} - ({sum_ux:.{self.precision}f})) / {U[i][i]:.{self.precision}f} = {X[i]:.{self.precision}f}")
                self.ans_str += f"Step {n-i}: X[{i+1}] = ({Y[i]:.{self.precision}f} - ({sum_ux:.{self.precision}f})) / {U[i][i]:.{self.precision}f} = {X[i]:.{self.precision}f}\n"

        print(f"Solution Vector X: {X}\n")
        self.ans_str += f"Solution Vector X: {X}\n"
        return X

    def display_matrices(self, L, U):
        """Display the current state of L and U matrices."""
        print("L Matrix:")
        self.ans_str += "\nL Matrix:\n"
        for row in L:
            print(" ".join([f"{val:.{self.precision}f}" for val in row]))
            self.ans_str += f'\n{" ".join([f"{val:.{self.precision}f}" for val in row])}'
        print("\nU Matrix:")
        self.ans_str += "\nU Matrix:\n"
        for row in U:
            print(" ".join([f"{val:.{self.precision}f}" for val in row]))
            self.ans_str+= f'\n{" ".join([f"{val:.{self.precision}f}" for val in row])}'
        self.ans_str += "\n"
        print("-" * 50)
        self.ans_str += "-" * 50

    def solve(self):
        """Solve the system of equations using LU Decomposition."""
        start_time = time.time()  # Start timing

        # Perform LU Decomposition
        L, U = self.decompose()

        # Check for no solution or infinite solutions
        solution_status = self.check_for_solution()
        if solution_status is False:
            print(f"Execution Time: {time.time() - start_time:.6f} seconds")
            return None  # No solution
        elif solution_status is None:
            print(f"Execution Time: {time.time() - start_time:.6f} seconds")
            return "Infinite solutions"

        # Solve L * Y = B
        Y = self.forward_substitution(L, self.B)

        # Solve U * X = Y
        X = self.back_substitution(U, Y)

        # End timing and print execution time
        print(f"Execution Time: {time.time() - start_time:.6f} seconds")
        return X


# Test the LU_Decomposition class
if __name__ == "__main__":
    # Example input
    A = [
        [0, 5, 1],
        [0, 12, 1],
        [0, 8, 1]
    ]
    B = [10, 20, 30]

    # User input for precision and steps
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6

    steps_choice = input("Show steps during calculation? (y/n, default n): ").strip().lower()
    steps = steps_choice == 'y'

    # Create an instance of the LU_Decomposition class
    solver = LU_Decomposition(A, B, precision=precision, steps=steps)
    
    # Solve the system
    X = solver.solve()

    if X is None:
        print("The system has no solution.")
    elif X == "Infinite solutions":
        print("The system has infinitely many solutions.")
    else:
        print("\nFinal Solution:")
        for i, val in enumerate(X):
            print(f"x{i+1} = {val:.{precision}f}")
