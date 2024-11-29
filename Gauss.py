import numpy as np
import time


class GaussianElimination:
    def __init__(self, A_Matrix, B_Matrix, scaling, significant_digits=6):

        self.A_Matrix = np.array(A_Matrix)
        self.B_Matrix = np.array(B_Matrix)
        self.scaling = scaling
        self.significant_digits = significant_digits
        self.n = len(B_Matrix)  # Number of equations (rows)
        self.x = np.zeros(self.n)  # Solution array
        self.i = 0
        self.steps = []

    def validate_input(self):  # To make sure validation of the input
        if self.A_Matrix.shape[0] != self.A_Matrix.shape[1]:
            return False
        if self.B_Matrix.shape[1] > 1 or self.B_Matrix.shape[0] != self.A_Matrix.shape[0]:
            return False
        else:
            return True

    def forward_elimination(self):  # Forward elimination
        augmented_matrix = np.concatenate((self.A_Matrix, self.B_Matrix), axis=1)
        print(f"The initial augmented matrix is:\n{np.round(augmented_matrix, self.significant_digits)}")
        self.steps.append(augmented_matrix.copy())
        print("----------------------------------------------------")

        for i in range(self.n):
            if (self.scaling):  # Scaling only determine the pivot but the original coefficients are retained
                scaled_matrix = augmented_matrix.copy()
                for s in range(i, self.n):
                    max_value = np.max(np.abs(scaled_matrix[s]))
                    scaled_matrix[s] = scaled_matrix[s] / max_value
                max = abs(scaled_matrix[i][i])
                for k in range(i + 1, self.n):
                    if (abs(scaled_matrix[k, i]) > max):
                        max = abs(scaled_matrix[k, i])
                        row = k
                        change = True
                if change:
                    augmented_matrix[[row, i]] = augmented_matrix[[i, row]]
                    print(f"R{i + 1}<->R{row + 1}\n{np.round(augmented_matrix, self.significant_digits)}")
                    self.steps.append(augmented_matrix.copy())
                    print("----------------------------------------------------")
            else:
                # Pivoting to avoid division by small values
                max = abs(augmented_matrix[i][i])
                for k in range(i + 1, self.n):
                    if (abs(augmented_matrix[k, i]) > max):
                        max = abs(augmented_matrix[k, i])
                        row = k
                        change = True
                if change:
                    augmented_matrix[[row, i]] = augmented_matrix[[i, row]]
                    print(f"R{i + 1}<->R{row + 1}\n{np.round(augmented_matrix, self.significant_digits)}")
                    self.steps.append(augmented_matrix.copy())
                    print("----------------------------------------------------")

            for j in range(i + 1, self.n):
                factor = augmented_matrix[j][i] / augmented_matrix[i][i]
                factor = round(factor, self.significant_digits)
                augmented_matrix[j] = augmented_matrix[j] - (augmented_matrix[i] * factor)
                print(f"R{j + 1}<-R{j + 1} - ({factor} * R{i + 1})")
                print(np.round(augmented_matrix, self.significant_digits))
                self.steps.append(augmented_matrix.copy())
                print("----------------------------------------------------")

        return augmented_matrix

    def backward_substitution(self, augmented_matrix):  # Backward substitution
        self.x[self.n - 1] = augmented_matrix[self.n - 1, self.n] / augmented_matrix[self.n - 1, self.n - 1]

        for k in range(self.n - 2, -1, -1):
            self.x[k] = augmented_matrix[k, self.n]
            for j in range(k + 1, self.n):
                self.x[k] -= augmented_matrix[k, j] * self.x[j]
            self.x[k] /= augmented_matrix[k, k]

    def solve(self):
        np.set_printoptions(suppress=True, formatter={'all': lambda x: f'{x:.{self.significant_digits}f}'})

        if self.validate_input():
            start_time = time.time()
            augmented_matrix = self.forward_elimination()
            self.backward_substitution(augmented_matrix)

            for answer in range(self.n):
                print(f"X{answer} is {np.round(self.x[answer], self.significant_digits)}")
                self.steps.append(augmented_matrix.copy())
            print("----------------------------------------------------")

            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Execution Time: {execution_time:.6f} seconds")
        else:
            print("Invalid Input")
        print("Steps taken during the process:")
        for step in self.steps:
            print(np.round(step, self.significant_digits))
            print("----------------------------------------------------")
        return self.steps


matrix1 = [[25, 5, 1, 5],
           [64, 8, 1, 4],
           [144, 12, 1, 3],
           [2.22, 33.57, 12, 12]]

matrix2 = [[106.8],
           [2],
           [279.2],
           [301.254]]

# Instantiate the GaussianElimination class and solve the system
solver = GaussianElimination(matrix1, matrix2, True, significant_digits=5)
solver.solve()






