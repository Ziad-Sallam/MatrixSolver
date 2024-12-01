import time
import numpy as np

class LUDecomposition:
    def __init__(self, A, B, steps=False, significant_digits=6):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)
        self.steps = steps
        self.precision = significant_digits
        self.ans_str = ""
        self.isSingular = False

    def format_significant_figures(self, value, significant_digits):
        """Format a number to the specified number of significant digits."""
        if value == 0:
            return f"{0:.{significant_digits}f}"
        else:
            return f"{value:.{significant_digits-1}e}".rstrip('0').rstrip('.')  # Use scientific notation and strip unnecessary zeros

    def decompose(self):
        """Perform LU Decomposition of matrix A with partial pivoting."""
        n = len(self.A)
        L = np.eye(n)  # Initialize L as the identity matrix (L diagonal is 1)
        U = self.A.copy()  # Start with U as a copy of A

        print("Starting LU Decomposition with partial pivoting...")
        self.ans_str += "\nStarting LU Decomposition with partial pivoting...\n"

        for i in range(n):
            # Partial pivoting: Find the row with the largest absolute value in the column
            max_row = np.argmax(np.abs(U[i:n, i])) + i  # Index of the maximum element
            if i != max_row:
                # Swap rows in U
                U[[i, max_row]] = U[[max_row, i]]
                # Swap corresponding entries in B
                self.B[[i, max_row]] = self.B[[max_row, i]]
                # Swap rows in L for the multipliers
                L[[i, max_row], :i] = L[[max_row, i], :i]
                print(f"Swapped rows {i+1} and {max_row+1} due to partial pivoting.")
                self.ans_str += f"\nSwapped rows {i+1} and {max_row+1} due to partial pivoting.\n"
            
            for j in range(i + 1, n):
                # Calculate the multiplier for the L matrix
                factor = U[j][i] / U[i][i]
                L[j][i] = factor
                U[j, i:] -= factor * U[i, i:]
                
                if self.steps:
                    print(f"R{j+1} <- R{j+1} - ({factor:.{self.precision}f}) * R{i+1}")
                    self.ans_str += f"\nR{j+1} <- R{j+1} - ({factor:.{self.precision}f}) * R{i+1}\n"
                    self.display_matrices(L, U)

        print("LU Decomposition complete.")
        self.ans_str += "\nLU Decomposition complete.\n"
        return L, U

    def forward_substitution(self, L, B):
        """Solve L * Y = B using forward substitution."""
        n = len(L)
        Y = np.zeros(n)

        print("Solving L * Y = B...")
        self.ans_str += "\nSolving L * Y = B...\n"

        for i in range(n):
            print("herererere")
            sum_ly = sum(L[i][j] * Y[j] for j in range(i))
            Y[i] = (B[i] - sum_ly) / L[i][i]

            if self.steps:
                print(f"Step {i+1}: Y[{i+1}] = ({B[i]:.{self.precision}f} - ({sum_ly:.{self.precision}f})) / {L[i][i]:.{self.precision}f} = {self.format_significant_figures(Y[i], self.precision)}")
                self.ans_str += f"\nStep {i+1}: Y[{i+1}] = ({B[i]:.{self.precision}f} - ({sum_ly:.{self.precision}f})) / {L[i][i]:.{self.precision}f} = {self.format_significant_figures(Y[i], self.precision)}\n"

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
                print(f"Step {n-i}: X[{i+1}] = ({Y[i]:.{self.precision}f} - ({sum_ux:.{self.precision}f})) / {U[i][i]:.{self.precision}f} = {self.format_significant_figures(X[i], self.precision)}")
                self.ans_str += f"Step {n-i}: X[{i+1}] = ({Y[i]:.{self.precision}f} - ({sum_ux:.{self.precision}f})) / {U[i][i]:.{self.precision}f} = {self.format_significant_figures(X[i], self.precision)}\n"

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
        start_time = time.time()  # Start timer
        print("The initial matrix A and vector B:")
        self.display_matrices(np.eye(len(self.A)), self.A)

        # Perform LU Decomposition
        try:
            L, U = self.decompose()
        except ValueError as e:
            print(str(e))
            self.isSingular = True
            return False

        # Solve L * Y = B
        Y = self.forward_substitution(L, self.B)

        # Solve U * X = Y
        X = self.back_substitution(U, Y)
        execution_time = time.time() - start_time  # End timer

        print(f"Execution Time: {execution_time:.6f} seconds")
        self.ans_str += f"Execution Time: {execution_time:.6f} seconds\n"
        return X


if __name__ == "__main__":
    # Example input
    A = [
        [2, 5, 1],
        [16, 1, 1],
        [33, 12, 1]
    ]  # Example system
    B = [10, 300, 15]
    
    # User input for precision and steps
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6

    steps_choice = input("Show steps during calculation? (y/n, default n): ").strip().lower()
    steps = steps_choice == 'y'

    # Create an instance of the LUDecomposition class
    solver = LUDecomposition(A, B, steps=steps, significant_digits=precision)

    # Solve the system
    X = solver.solve()

    if X is not None:
        print("\nFinal Solution:")
        for i, val in enumerate(X):
            print(f"x{i+1} = {solver.format_significant_figures(val, precision)}")
    else:
        print("The system has no solution or infinite solutions.")
