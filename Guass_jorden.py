import numpy as np
import Gauss
import time

class GaussianJordanElimination(Gauss.GaussianElimination):
    def gauss_jordan_elimination(self):
        augmented_matrix = np.concatenate((self.A_Matrix, self.B_Matrix), axis=1)

        print(f"Initial augmented matrix:\n{np.round(augmented_matrix, self.significant_digits)}")
        print("----------------------------------------------------")

        for i in range(self.n):
            if self.scaling:
                # Scaling for stability
                scaled_matrix = augmented_matrix.copy()
                row = i
                change = False  # Initialize change tracking
                for s in range(i, self.n):
                    max_value = np.max(np.abs(scaled_matrix[s]))
                    scaled_matrix[s] = scaled_matrix[s] / max_value

                max = abs(scaled_matrix[i][i])
                for k in range(i + 1, self.n):
                    if abs(scaled_matrix[k, i]) > max:
                        max = abs(scaled_matrix[k, i])
                        row = k
                        change = True
                if change:
                    augmented_matrix[[row, i]] = augmented_matrix[[i, row]]
                    print(f"R{i+1} <-> R{row+1}")
                    print(f"After scaling, augmented matrix:\n{np.round(augmented_matrix, self.significant_digits)}")
                    print("----------------------------------------------------")

            # Normalize pivot row
            pivot = augmented_matrix[i][i]
            augmented_matrix[i] = augmented_matrix[i] / pivot
            print(f"R{i+1} <- R{i+1} / {np.round(pivot, self.significant_digits)}")
            print(np.round(augmented_matrix, self.significant_digits))
            print("----------------------------------------------------")

            # Eliminate all other rows
            for j in range(self.n):
                if j != i:
                    factor = augmented_matrix[j][i]
                    augmented_matrix[j] = augmented_matrix[j] - (augmented_matrix[i] * factor)
                    print(f"R{j+1} <- R{j+1} - ({np.round(factor, self.significant_digits)} * R{i+1})")
                    print(np.round(augmented_matrix, self.significant_digits))
                    print("----------------------------------------------------")

        return augmented_matrix

    def solve_system(self):
        if self.validate_input():
            start_time = time.time()
            augmented_matrix = self.gauss_jordan_elimination()
            # Extract solutions from the last column
            self.x = augmented_matrix[:, -1]

            for i, value in enumerate(self.x):
                print(f"X{i+1} = {np.round(value, self.significant_digits)}")
            print("----------------------------------------------------")

            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Execution Time: {execution_time:.6f} seconds")
        else:
            print("Invalid Input")

matrix1 = [[25, 5, 1, 5],
           [64, 8, 1, 4],
           [144, 12, 1, 3],
           [2.22, 33.57, 12, 12]]

matrix2 = [[106.8],
           [2],
           [279.2],
           [301.254]]

# Instantiate the GaussianJordanElimination class
solver = GaussianJordanElimination(matrix1, matrix2, scaling=True, significant_digits=5)
solver.solve_system()