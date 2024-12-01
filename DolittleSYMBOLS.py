import time
import sympy as sp
class LUDecomposition:
    def __init__(self, A, B, steps=False, significant_digits=6):
        self.A = sp.Matrix(A)
        self.B = sp.Matrix(B)
        self.steps = steps
        self.precision = significant_digits
        self.ans_str = ""

    def decompose(self):
        """Perform LU Decomposition of matrix A."""
        n = self.A.shape[0]
        L, U, _ = self.A.LUdecomposition()

        print("Starting LU Decomposition...")
        self.ans_str += "Starting LU Decomposition...\n"

        if self.steps:
            self.display_matrices(L, U)

        print("LU Decomposition complete.")
        self.ans_str += "LU Decomposition complete.\n"
        return L, U

    def forward_substitution(self, L, B):
        """Solve L * Y = B using forward substitution."""
        n = L.shape[0]
        Y = sp.zeros(n, 1)

        print("Solving L * Y = B...")
        self.ans_str += "Solving L * Y = B...\n"

        for i in range(n):
            sum_ly = sum(L[i, j] * Y[j] for j in range(i))
            Y[i] = (B[i] - sum_ly) / L[i, i]

            if self.steps:
                print(f"Step {i+1}: Y[{i+1}] = ({B[i]} - ({sum_ly})) / {L[i, i]} = {Y[i]}")
                self.ans_str += f"Step {i+1}: Y[{i+1}] = ({B[i]} - ({sum_ly})) / {L[i, i]} = {Y[i]}\n"

        print(f"Y Vector: {Y}\n")
        self.ans_str += f"Y Vector: {Y}\n"
        return Y

    def back_substitution(self, U, Y):
        """Solve U * X = Y using back substitution."""
        n = U.shape[0]
        X = sp.zeros(n, 1)

        print("Solving U * X = Y...")
        self.ans_str += "Solving U * X = Y...\n"

        for i in range(n - 1, -1, -1):
            sum_ux = sum(U[i, j] * X[j] for j in range(i + 1, n))
            X[i] = (Y[i] - sum_ux) / U[i, i]

            if self.steps:
                print(f"Step {n-i}: X[{i+1}] = ({Y[i]} - ({sum_ux})) / {U[i, i]} = {X[i]}")
                self.ans_str += f"Step {n-i}: X[{i+1}] = ({Y[i]} - ({sum_ux})) / {U[i, i]} = {X[i]}\n"

        print(f"Solution Vector X: {X}\n")
        self.ans_str += f"Solution Vector X: {X}\n"
        return X

    def display_matrices(self, L, U):
        """Display the current state of L and U matrices."""
        print("L Matrix:")
        print(L)
        print("\nU Matrix:")
        print(U)
        print("-" * 50)

    def solve(self):
        """Solve the system of equations using LU Decomposition."""
        start_time = time.time()  # Start timer
        print("The initial matrix A and vector B:")
        print(self.A)

        # Perform LU Decomposition
        try:
            L, U = self.decompose()
        except ValueError as e:
            print(str(e))
            return None

        # Solve L * Y = B
        Y = self.forward_substitution(L, self.B)

        # Solve U * X = Y
        X = self.back_substitution(U, Y)
        execution_time = time.time() - start_time  # End timer

        print(f"Execution Time: {execution_time:.6f} seconds")
        self.ans_str += f"Execution Time: {execution_time:.6f} seconds\n"
        return X


if __name__ == "__main__":
    # Example input using symbolic variables
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sp.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = sp.symbols('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')

    A = [
        [a, b, c],
        [0, b, 0],
        [0, b, c]
    ]
    B = [x, y, z]

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
            print(f"x{i+1} = {val}")
    else:
        print("The system has no solution or infinite solutions.")
