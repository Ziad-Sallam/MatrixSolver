import numpy as np

class LUDecomposition:
    def __init__(self, A, B, steps=False, significant_digits=6):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)
        self.steps = steps
        self.precision = significant_digits
        self.ans_str = ""

    def decompose(self):
        """Perform LU Decomposition of matrix A."""
        n = len(self.A)
        L = np.zeros_like(self.A)
        U = self.A.copy()

        print("Starting LU Decomposition...")
        self.ans_str += "Starting LU Decomposition...\n"

        for i in range(n):
            L[i][i] = 1  # Diagonal of L is 1
            for j in range(i + 1, n):
                factor = U[j][i] / U[i][i]
                L[j][i] = factor
                U[j, i:] -= factor * U[i, i:]
                
                if self.steps:
                    print(f"R{j+1} <- R{j+1} - ({factor:.{self.precision}f}) * R{i+1}")
                    self.ans_str += f"R{j+1} <- R{j+1} - ({factor:.{self.precision}f}) * R{i+1}\n"
                    self.display_matrices(L, U)

        print("LU Decomposition complete.")
        self.ans_str += "LU Decomposition complete.\n"
        return L, U

    def forward_substitution(self, L, B):
        """Solve L * Y = B using forward substitution."""
        n = len(L)
        Y = np.zeros(n)

        print("Solving L * Y = B...")
        self.ans_str += "Solving L * Y = B...\n"

        for i in range(n):
            sum_ly = sum(L[i][j] * Y[j] for j in range(i))
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
            sum_ux = sum(U[i][j] * X[j] for j in range(i + 1, n))
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
        for row in L:
            print(" ".join([f"{val:.{self.precision}f}" for val in row]))
        print("\nU Matrix:")
        for row in U:
            print(" ".join([f"{val:.{self.precision}f}" for val in row]))
        print("-" * 50)

    def solve(self):
        """Solve the system of equations using LU Decomposition."""
        print("The initial matrix A and vector B:")
        self.display_matrices(np.eye(len(self.A)), self.A)

        # Perform LU Decomposition
        L, U = self.decompose()

        # Solve L * Y = B
        Y = self.forward_substitution(L, self.B)

        # Solve U * X = Y
        X = self.back_substitution(U, Y)

        return X


if __name__ == "__main__":
    # Input matrix A and vector B
    A = [
        [6, 3, 4],
        [3, 6, 5],
        [4, 5, 10]
    ]
    B = [2, -4, 5]

    # User input for precision and steps
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6

    steps_choice = input("Show steps during calculation? (y/n, default n): ").strip().lower()
    steps = steps_choice == 'y'

    # Create an instance of the LUDecomposition class
    solver = LUDecomposition(A, B, steps=steps, significant_digits=precision)

    # Solve the system
    X = solver.solve()

    print("\nFinal Solution:")
    for i, val in enumerate(X):
        print(f"x{i+1} = {val:.{precision}f}")
