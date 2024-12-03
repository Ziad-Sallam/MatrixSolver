import sympy as sp
import time
import numpy as np

class GaussJordanElimination2:
    def __init__(self, coeff_matrix, const_matrix):
        self.coeff_matrix = sp.Matrix(coeff_matrix)
        self.const_matrix = sp.Matrix(const_matrix)
        self.show_steps = False  # Default to not showing steps
        self.ans = ''

    def validate_input(self):
        if self.coeff_matrix.shape[1] != self.coeff_matrix.shape[0]:
            return False
        if self.const_matrix.shape[1] > 1 or self.const_matrix.shape[0] != self.coeff_matrix.shape[0]:
            return False
        return True

    def gauss_jordan(self):
        n = self.coeff_matrix.shape[0]
        augmented_matrix = self.coeff_matrix.row_join(self.const_matrix)
        
        # Convert augmented matrix to numpy array
        augmented_matrix_np = np.array(augmented_matrix, dtype=object)

        if self.show_steps:
            self.ans += "Initial Augmented Matrix:\n"
            self.ans += np.array2string(augmented_matrix_np, separator=', ') + "\n"
            self.ans += "-" * 70 + "\n"

        # Forward elimination to get to row echelon form
        for i in range(n):
            for j in range(i + 1, n):
                if augmented_matrix[i, i] == sp.sympify(0):
                    self.ans += "Error: Pivot is zero.\n"
                    return False, None
                factor = augmented_matrix[j, i] / augmented_matrix[i, i]
                if augmented_matrix[j, i] == sp.sympify(0):  # Use sympify to compare with zero
                    continue
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
                if self.show_steps:
                    self.ans += f"R{j+1} <- R{j + 1} - ({factor} * R{i + 1})\n"
                    augmented_matrix_np = np.array(augmented_matrix, dtype=object)
                    self.ans += np.array2string(augmented_matrix_np, separator=', ') + "\n"
                    self.ans += "-" * 70 + "\n"

            # Normalize the current row
            if self.show_steps:
                self.ans += f"R{i+1} <- R{i+1}/({augmented_matrix[i, i]})\n"
            augmented_matrix[i, :] /= augmented_matrix[i, i]
            if self.show_steps:
                augmented_matrix_np = np.array(augmented_matrix, dtype=object)
                self.ans += np.array2string(augmented_matrix_np, separator=', ') + "\n"
                self.ans += "-" * 70 + "\n"

        # Back substitution to eliminate above the pivots
        for i in range(n - 1, -1, -1):
            for j in range(i):
                factor = augmented_matrix[j, i]
                if augmented_matrix[j, i] == sp.sympify(0):  # Use sympify to compare with zero
                    continue
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
                if self.show_steps:
                    self.ans += f"R{j+1} <- R{j + 1} - ({factor} * R{i + 1})\n"
                    augmented_matrix_np = np.array(augmented_matrix, dtype=object)
                    self.ans += np.array2string(augmented_matrix_np, separator=', ') + "\n"
                    self.ans += "-" * 70 + "\n"

        return True, augmented_matrix

    def solve(self):
        self.show_steps = True  # Set this to True if you want to show the steps

        if self.validate_input():
            start_time = time.time()
            valid, augmented_matrix = self.gauss_jordan()
            if valid:
                self.const_matrix = augmented_matrix[:, -1]  # Last column is the constants
                self.coeff_matrix = augmented_matrix[:, :-1]  # The rest is the coefficients
                self.ans += "Final Solutions:\n"
                for i in range(self.coeff_matrix.shape[0]):
                    self.ans += f"x[{i}] = {self.const_matrix[i]}\n"
                self.ans += "-" * 70 + "\n"
                end_time = time.time()
                execution_time = end_time - start_time
                self.ans += f"Execution Time: {execution_time:.6f} seconds\n"
            else:
                self.ans += "Invalid input\n"
        else:
            self.ans += "Invalid input\n"
        
        # Return the final answer as a string
        return self.ans

if __name__ == "__main__":
    # Example input for coefficients and constants
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sp.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = sp.symbols('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
    coeff_matrix = [
        [h, c, c],
        [0, c, c],
        [h, 0, c]
    ]
    
    const_matrix = [
        [j],
        [k],
        [l]
    ]
    
    gauss_jordan_solver = GaussJordanElimination2(coeff_matrix, const_matrix)
    result = gauss_jordan_solver.solve()
    print(result)
