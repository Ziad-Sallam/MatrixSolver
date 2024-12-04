import sympy as sp
from sympy import Matrix
import time
import numpy as np

class GaussianElimination2:
    def __init__(self, coeff_matrix, const_matrix):
        self.coeff_matrix = sp.Matrix(coeff_matrix)
        self.const_matrix = sp.Matrix(const_matrix)
        self.show_steps = True
        self.ans = ''
        
    def validate_input(self):
        # Validate that both matrices have the correct dimensions
        if self.coeff_matrix.shape[1] != self.coeff_matrix.shape[0]:
            return False
        if self.const_matrix.shape[1] > 1 or self.const_matrix.shape[0] != self.coeff_matrix.shape[0]:
            return False
        else:
            return True
        
    def forward_elimination(self):
        n = self.coeff_matrix.shape[0]
        if self.show_steps:
            print("Initial Augmented Matrix:")
            self.ans += "Initial Augmented Matrix:\n"
            augmented_matrix = self.coeff_matrix.row_join(self.const_matrix)
            sp.pprint(Matrix(augmented_matrix))
            
            # Convert the augmented matrix to a numpy array and print it
            augmented_matrix_np = np.array(augmented_matrix, dtype=object)
            self.ans += np.array2string(augmented_matrix_np, separator=', ')
            print("-" * 70)
            self.ans += "-" * 70
         
        for i in range(n):
            for j in range(i + 1, n):
                if self.coeff_matrix[i, i] == sp.sympify(0):
                    print("Error: Pivot is zero")
                    self.ans += "Error: Pivot is zero\n"
                    return False, None
                factor = self.coeff_matrix[j, i] / self.coeff_matrix[i, i]
                if self.coeff_matrix[j, i] == sp.sympify(0):  # Use sympify to compare with zero
                    continue
                # Update the row in the coefficient matrix
                self.coeff_matrix[j, :] = self.coeff_matrix[j, :] - factor * self.coeff_matrix[i, :]
                # Update the corresponding entry in the constant matrix
                self.const_matrix[j] = self.const_matrix[j] - factor * self.const_matrix[i]
                
                # Print the updated augmented matrix after each elimination step
                if self.show_steps:
                    augmented_matrix = self.coeff_matrix.row_join(self.const_matrix)
                    print(f"R{j+1} <- R{j + 1} - ({factor} * R{i + 1})\n")
                    self.ans+= f"\nR{j+1} <- R{j + 1} - ({factor} * R{i + 1})\n"
                    sp.pprint(augmented_matrix)
                    
                    # Convert to numpy array for display
                    augmented_matrix_np = np.array(augmented_matrix, dtype=object)
                    self.ans += np.array2string(augmented_matrix_np, separator=', ')
                    print("-" * 70)

                    self.ans += "-" * 70 +'\n\n'
                    print()
                
        for i in range(n):
            flag = True
            for k in range(0, n):
                if self.coeff_matrix[i, k] != sp.sympify(0): 
                    flag = False
                    break  
            if flag:  
                if self.const_matrix[i] != sp.sympify(0): 
                    print("The system has no solution.")
                    self.ans += "The system has no solution.\n"
                    return False, None
                else:
                    print("The system has infinite solutions.")
                    self.ans += "The system has infinite solutions.\n"
                    return False, None 
               
        return True, self.coeff_matrix.row_join(self.const_matrix)

    def back_substitution(self, augmented_matrix):
        n = self.coeff_matrix.shape[0]
        self.solutions = [0] * n
        
        for i in range(n - 1, -1, -1):
            sum_ = self.const_matrix[i]
            for j in range(i + 1, n):
                sum_ -= self.coeff_matrix[i, j] * self.solutions[j]
            self.solutions[i] = sum_ / self.coeff_matrix[i, i]
            
    def solve(self):
        if self.validate_input():

            start_time = time.time()
            valid, augmented_matrix = self.forward_elimination()
            if valid:
                self.back_substitution(augmented_matrix)
                print("Final Solutions:")
                self.ans += "Final Solutions:\n"
                for idx, sol in enumerate(self.solutions):
                    print(f"x[{idx}] = {sol}")
                    self.ans += f"x[{idx}] = {sol}\n\n"
                print("-" * 70)
                self.ans += "-" * 70
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
        [c, h, f],
        [l, 0, 0]
    ]
    
    const_matrix = [
        [j],
        [k],
        [l]]
    
    gaussian_solver = GaussianElimination2(coeff_matrix, const_matrix)
    gaussian_solver.solve()
