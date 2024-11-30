import numpy as np
import time  # Import time module for measuring execution time

class GaussianElimination:

    def __init__(self, A, B, scaling=False, steps=False, significant_digits=6):
        self.A = np.array(A, float)
        self.B = np.array(B, float)
        self.scaling = scaling
        self.steps = steps
        self.precision = significant_digits
        self.variables = [f"x{i+1}" for i in range(len(A[0]))]  # Default variable names
        self.ans = []
        self.ans_str = ""
        self.finals = []

    def normalize_for_pivoting(self):
        """Normalize each row by dividing all elements by the largest element in that row."""
        normalized_A = self.A.copy()  # Copy the matrix for normalization
        for i in range(len(self.A)):
            max_element = np.max(np.abs(normalized_A[i]))
            if max_element != 0:
                normalized_A[i] = normalized_A[i] / max_element
            if self.steps:
                print(f"Normalized row {i+1} for pivoting: {normalized_A[i]}")
        return normalized_A

    def forward_elimination(self):
        """Perform forward elimination to transform the system into upper triangular form."""
        n = len(self.A)

        for i in range(n):
            # Normalize the matrix for pivoting
            normalized_A = self.normalize_for_pivoting()

            # Pivoting: Find the row with the maximum value in the current column
            pivot_row = max(range(i, n), key=lambda x: abs(normalized_A[x, i]))

            if self.A[pivot_row, i] == 0:
                if self.B[pivot_row] != 0:
                    print("The system has no solution (singular matrix).")
                    self.ans_str += "The system has no solution (singular matrix)."
                    return False, None  # No solution
                else:
                    print("The system has infinite solutions (free variable detected).")
                    self.ans_str += "The system has infinite solutions (free variable detected)."
                    return False, None  # Infinite solutions

            if pivot_row != i:  # Swap rows if necessary
                self.A[[i, pivot_row]] = self.A[[pivot_row, i]]
                self.B[i], self.B[pivot_row] = self.B[pivot_row], self.B[i]
                if self.steps:
                    print(f"R{i+1} <-> R{pivot_row+1}")
                    self.display_matrix()

            # Eliminate entries below the pivot using the correct rows
            for j in range(i + 1, n):
                if self.A[j, i] != 0:
                    ratio = self.A[j, i] / self.A[i, i]
                    self.A[j, i:] -= ratio * self.A[i, i:]
                    self.B[j] -= ratio * self.B[i]
                    if self.steps:
                        print(f"R{j+1} <- R{j+1} - ({ratio:.2f}) * R{i+1}")
                        self.ans_str += f"\nR{j+1} <- R{j+1} - ({ratio:.2f}) * R{i+1}"
                        self.display_matrix()

        return True, self.B  # Continue if there's a valid solution

    def back_substitution(self):
        """Perform back substitution to find the solutions."""
        n = len(self.A)
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            sum = self.B[i]
            for j in range(i + 1, n):
                sum -= self.A[i, j] * x[j]
            x[i] = sum / self.A[i, i]
            if self.steps:
                print(f"x[{i}] = {x[i]:.{self.precision}f}")
                self.ans_str += f"\nx[{i}] = {x[i]:.{self.precision}f}"
        return x

    def display_matrix(self):
        """Display the augmented matrix [A | B]."""
        augmented_matrix = np.column_stack((self.A, self.B))
        self.ans.append(augmented_matrix)
        print("[", end="")
        self.ans_str += "\n["
        for row in augmented_matrix:
            print(" ".join([f"{val:.{self.precision}f}" for val in row]), end=" \n")
            self.ans_str += " ".join([f"{val:.{self.precision}f}" for val in row]) + "\n"
        print("]")
        self.ans_str += "]\n"
        print("-" * 50)
        self.ans_str += "-" * 50

    def solve(self):
        """Solve the system of equations using Gaussian Elimination."""
        start_time = time.time()  # Start measuring time

        print("The initial augmented matrix is:")
        self.ans_str += "The initial augmented matrix is:"
        self.display_matrix()

        # Forward elimination to transform the system to upper triangular form
        is_valid, B_result = self.forward_elimination()
        if not is_valid:
            return  # No valid solution (either no solution or infinite)

        # Back substitution to get the solutions if the system is consistent
        solutions = self.back_substitution()

        # Check for infinite solutions
        if np.allclose(self.A[-1], np.zeros_like(self.A[-1])) and np.allclose(self.B[-1], 0):
            print("The system has infinite solutions.")
            self.ans_str += "The system has infinite solutions."
        else:
            print("\nSolutions:")
            self.ans_str += "\nSolutions:\n"
            for i in range(len(solutions)):
                print(f"{self.variables[i]} = {solutions[i]:.{self.precision}f}")
                self.finals.append(solutions[i])

        end_time = time.time()  # End measuring time
        execution_time = end_time - start_time
        print(f"\nExecution time: {execution_time:.6f} seconds")
        self.ans_str += f"\nExecution time: {execution_time:.6f} seconds"


# Example setup with matrices predefined
if __name__ == "__main__":
    A = [
        [6.6, 5, 1],
        [150, 8, 1],
        [33, 12, 1]
    ]  # Example system
    B = [10, 300, 15]

    # User input for precision, scaling, and steps
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6

    scaling_choice = input("Apply scaling? (y/n, default n): ").strip().lower()
    scaling = scaling_choice == 'y'

    steps_choice = input("Show steps during calculation? (y/n, default n): ").strip().lower()
    steps = steps_choice == 'y'

    solver = GaussianElimination(A, B, scaling, steps, significant_digits=precision)

    # Solve the system
    solver.solve()
