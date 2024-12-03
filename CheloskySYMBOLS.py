import sympy as sp
import time  # Import time module for measuring execution time

class Cholesky_Decomposition:
    def __init__(self, A, B, precision=6, steps=False):
        self.A = sp.Matrix(A)  # Use sympy.Matrix for symbolic matrix
        self.B = sp.Matrix(B)  # Use sympy.Matrix for symbolic vector
        self.n = len(A)
        self.L = sp.zeros(self.n)  # Initialize symbolic zero matrix
        self.precision = precision
        self.steps = steps
        self.ans_str = ""
    def is_symmetric(self):
        """Check if the matrix is symmetric."""
        if not self.A.is_symmetric():
            print("Not symmetric")
            self.ans_str = "Not symmetric"
            return False
        return True

    def is_positive_definite(self):
        """Check if the matrix is positive definite by testing if all the leading principal minors are positive."""
        try:
            self.A.cholesky()  # Try Cholesky decomposition
            return True
        except ValueError:
            print("Matrix is not positive definite")
            return False

    def decompose(self):
        """Cholesky decomposition: A = LL^T"""
        if not self.is_symmetric():
            raise ValueError("Matrix is not symmetric.")
        # if not self.is_positive_definite():
        #     raise ValueError("Matrix is not positive definite.")
        
        for i in range(self.n):
            for j in range(i + 1):
                sum_L = 0
                if j == i:  # Diagonal elements
                    for k in range(i):
                        sum_L += self.L[i, k] ** 2
                    self.L[i, i] = sp.sqrt(self.A[i, i] - sum_L)
                else:  # Off-diagonal elements
                    for k in range(j):
                        sum_L += self.L[i, k] * self.L[j, k]
                    self.L[i, j] = (self.A[i, j] - sum_L) / self.L[j, j]
                
                if self.steps:
                    print(f"L[{i+1},{j+1}] = {self.L[i, j]}")
                    self.ans_str+=f"L[{i+1},{j+1}] = {self.L[i, j]}\n"
            
            if self.steps:
                self.display_matrix(self.L)
                print(f"After Step {i+1}:\n")
                self.ans_str+=f"After Step {i+1}:\n"
        
        return self.L

    def forward_substitution(self, L, B):
        """Solve L * Y = B using forward substitution."""
        Y = sp.zeros(self.n, 1)

        print("Solving L * Y = B...")
        self.ans_str += "Solving L * Y = B...\n"

        for i in range(self.n):
            sum_ly = 0
            for j in range(i):
                sum_ly += L[i, j] * Y[j]
            Y[i] = (B[i] - sum_ly) / L[i, i]

            if self.steps:
                print(f"Step {i+1}: Y[{i+1}] = ({B[i]} - ({sum_ly})) / {L[i, i]} = {Y[i]}")
                self.ans_str += f"Step {i+1}: Y[{i+1}] = ({B[i]} - ({sum_ly})) / {L[i, i]} = {Y[i]}\n"

        print(f"Y Vector: {Y}")
        self.ans_str += f"Y Vector: {Y}\n"
        return Y

    def back_substitution(self, L, Y):
        """Solve L^T * X = Y using back substitution."""
        X = sp.zeros(self.n, 1)

        print("Solving L^T * X = Y...")
        self.ans_str += "Solving L^T * X = Y...\n"

        for i in range(self.n - 1, -1, -1):
            sum_lx = 0
            for j in range(i + 1, self.n):
                sum_lx += L[j, i] * X[j]
            X[i] = (Y[i] - sum_lx) / L[i, i]

            if self.steps:
                print(f"Step {self.n-i}: X[{i+1}] = ({Y[i]} - ({sum_lx})) / {L[i, i]} = {X[i]}")
                self.ans_str += f"Step {self.n-i}: X[{i+1}] = ({Y[i]} - ({sum_lx})) / {L[i, i]} = {X[i]}\n"

        print(f"Solution Vector X: {X}")
        self.ans_str += f"Solution Vector X: {X}\n"
        return X

    def display_matrix(self, L):
        """Display the current state of L matrix."""
        print("L Matrix:")
        for row in L.tolist():
            print(" ".join([str(val) for val in row]))
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


# # Example input using symbolic variables
# a, b, c, x, y, z = sp.symbols('a b c x y z')
#
# A = [
#     [a, 0, x],
#     [0, b, 0],
#     [0, 0, c]
# ]
#
# B = [x, y, z]
#
# # Create solver instance
# solver = Cholesky_Decomposition(A, B, precision=6, steps=True)
# X = solver.solve()
#
# print("\nFinal Solution (symbolically):")
# for i, val in enumerate(X):
#     print(f"x{i+1} = {val}")
