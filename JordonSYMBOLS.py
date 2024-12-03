import sympy as sp
import time

class GaussJordanElimination:
    def __init__(self, coeff_matrix, const_matrix):
        self.coeff_matrix = sp.Matrix(coeff_matrix)
        self.const_matrix = sp.Matrix(const_matrix)
        self.show_steps = False  # Default to not showing steps8
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
        
        if self.show_steps:
            print("Initial Augmented Matrix:")
            sp.pprint(augmented_matrix)
            print("-" * 70)

        # Forward elimination to get to row echelon form
        for i in range(n):
            for j in range(i + 1, n):
                if augmented_matrix[i, i] == sp.sympify(0):
                    print("Error: Pivot is zero.")
                    self.ans += "Error: Pivot is zero.\n"
                    return False, None
                factor = augmented_matrix[j, i] / augmented_matrix[i, i]
                if augmented_matrix[j, i] == sp.sympify(0):  # Use sympify to compare with zero
                    continue
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
                if self.show_steps:
                    print(f"R{j+1} <- R{j + 1} - ({factor} * R{i + 1})\n")
                    self.ans += f"R{j+1} - ({factor} * R{i + 1})\n"
                    sp.pprint(augmented_matrix)
                    print("-" * 70)

            for l in range(n):
                flag = True
                for k in range(0, n):
                    if augmented_matrix[l, k] != sp.sympify(0): 
                        flag = False
                        break  
                if flag:  
                    if augmented_matrix[l, -1] != sp.sympify(0): 
                        print("The system has no solution.")
                        self.ans += "The system has no solution.\n"
                        return False, None
                    else:
                        print("The system has infinite solutions.")
                        self.ans += "The system has infinite solutions.\n"
                        return False, None     
            # Normalize the current row
            if self.show_steps:
                print(f"R{i+1} <- R{i+1}/({augmented_matrix[i, i]})")
                self.ans += f"R{i+1} - ({augmented_matrix[i, i]})\n"
            augmented_matrix[i, :] /= augmented_matrix[i, i]
            if self.show_steps:
                sp.pprint(augmented_matrix)
                print("-" * 70)
                self.ans += "-" *70

        # Back substitution to eliminate above the pivots
        for i in range(n - 1, -1, -1):
            for j in range(i):
                factor = augmented_matrix[j, i]
                if augmented_matrix[j, i] == sp.sympify(0):  # Use sympify to compare with zero
                    continue
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
                if self.show_steps:
                    print(f"R{j+1} <- R{j + 1} - ({factor} * R{i + 1})\n")
                    self.ans += f"\nR{j+1} - ({factor} * R{i + 1})\n"
                    sp.pprint(augmented_matrix)
                    print("-" * 70)
                    self.ans += "-" * 70

        return True, augmented_matrix

    def solve(self):
        #show_steps = input("Do you want to see the steps? (y/n): ").strip().lower()
        self.show_steps = True

        if self.validate_input():
            start_time = time.time()
            valid, augmented_matrix = self.gauss_jordan()
            if valid:
                self.const_matrix = augmented_matrix[:, -1]  # Last column is the constants
                self.coeff_matrix = augmented_matrix[:, :-1]  # The rest is the coefficients
                print("Final Solutions:")
                self.ans += "\nFinal Solutions:\n"
                for i in range(self.coeff_matrix.shape[0]):
                    print(f"x[{i}] = {self.const_matrix[i]}")
                    self.ans += f"x[{i}] = {self.const_matrix[i]}\n"
                print("-" * 70)
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"Execution Time: {execution_time:.6f} seconds")
                self.ans += f"Execution Time: {execution_time:.6f} seconds"
        else:
            print("Invalid input")
            self.ans += "Invalid input"

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
    
    gauss_jordan_solver = GaussJordanElimination(coeff_matrix, const_matrix)
    gauss_jordan_solver.solve()
