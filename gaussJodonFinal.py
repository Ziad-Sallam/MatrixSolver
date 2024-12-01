import numpy as np
import time

class GaussJordanElimination:

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
        self.noSolution = False
        self.infiniteFlag = False

    def format_number(self, num):
        """Format a number to the specified significant digits."""
        if num == 0:
            return f"{0:.{self.precision}g}"
        else:
            return f"{num:.{self.precision}g}"

    def normalize_for_pivoting(self):
        """Normalize each row by dividing all elements by the largest element in that row."""
        normalized_A = self.A.copy()
        for i in range(len(self.A)):
            max_element = np.max(np.abs(normalized_A[i]))
            if max_element != 0:
                normalized_A[i] = normalized_A[i] / max_element
            if self.steps:
                print(f"Normalized row {i+1} for pivoting: {list(map(self.format_number, normalized_A[i]))}")
                self.ans_str += f"\nNormalized row {i+1} for pivoting: {list(map(self.format_number, normalized_A[i]))}"
        return normalized_A

    def forward_elimination(self):
        """Perform forward elimination to transform the system into upper triangular form."""
        n = len(self.A)

        for i in range(n):
            if self.scaling:
                normalized_A = self.normalize_for_pivoting()
            else:
                normalized_A = self.A

            # Pivoting: Find the row with the maximum value in the current column
            pivot_row = max(range(i, n), key=lambda x: abs(normalized_A[x, i]))

            if self.A[pivot_row, i] == 0:
                if self.B[pivot_row] != 0:
                    print("The system has no solution (singular matrix).")
                    self.noSolution = True
                    self.ans_str += "\nThe system has no solution (singular matrix)."
                    return False, None  # No solution
                else:
                    print("The system has infinite solutions (free variable detected).")
                    self.infiniteFlag = True
                    self.ans_str += "\nThe system has infinite solutions (free variable detected)."
                    return False, None  # Infinite solutions

            if pivot_row != i:  # Swap rows if necessary
                self.A[[i, pivot_row]] = self.A[[pivot_row, i]]
                self.B[i], self.B[pivot_row] = self.B[pivot_row], self.B[i]
                if self.steps:
                    print(f"R{i+1} <-> R{pivot_row+1}")
                    self.ans_str += f"\nR{i+1} <-> R{pivot_row+1}"
                    self.display_matrix()

            # Eliminate entries below the pivot
            for j in range(i + 1, n):
                if self.A[j, i] != 0:
                    ratio = self.A[j, i] / self.A[i, i]
                    self.A[j, i:] -= ratio * self.A[i, i:]
                    self.B[j] -= ratio * self.B[i]
                    if self.steps:
                        print(f"R{j+1} <- R{j+1} - ({self.format_number(ratio)}) * R{i+1}")
                        self.ans_str += f"\nR{j+1} <- R{j+1} - ({self.format_number(ratio)}) * R{i+1}"
                        self.display_matrix()

        return True, self.B

    def back_substitution(self):
        """Perform back substitution to find the solutions and reduce the matrix."""
        n = len(self.A)
        x = np.zeros(n)

        # Back substitution to reduce the system to RREF (Reduced Row Echelon Form)
        for i in range(n-1, -1, -1):
            if self.A[i, i] == 0:
                if self.B[i] != 0:
                    print("The system has no solution (singular matrix).")
                    self.noSolution = True
                    self.ans_str += "\nThe system has no solution (singular matrix)."
                    return None

            # Normalize the pivot element to 1
            pivot = self.A[i, i]
            self.A[i] /= pivot
            self.B[i] /= pivot
            if self.steps:
                print(f"Normalized pivot at row {i+1}: {list(map(self.format_number, self.A[i]))}")
                self.ans_str += f"\nNormalized pivot at row {i+1}: {list(map(self.format_number, self.A[i]))}"

            # Eliminate entries above the pivot
            for j in range(i-1, -1, -1):
                ratio = self.A[j, i]
                self.A[j] -= ratio * self.A[i]
                self.B[j] -= ratio * self.B[i]
                if self.steps:
                    print(f"R{j+1} <- R{j+1} - ({self.format_number(ratio)}) * R{i+1}")
                    self.ans_str += f"\nR{j+1} <- R{j+1} - ({self.format_number(ratio)}) * R{i+1}"
                    self.display_matrix()

        return self.B

    def display_matrix(self):
        """Display the augmented matrix [A | B]."""
        augmented_matrix = np.column_stack((self.A, self.B))
        self.ans.append(augmented_matrix)
        print("[", end="")
        self.ans_str += "\n["
        for row in augmented_matrix:
            print(" ".join([self.format_number(val) for val in row]), end=" \n")
            self.ans_str += f'\n{" ".join([self.format_number(val) for val in row]) + "\n"}'
        print("]")
        self.ans_str += "]\n"
        print("-" * 50)
        self.ans_str += "-" * 50

    def solve(self):
        """Solve the system of equations using Gauss-Jordan Elimination."""
        start_time = time.time()

        print("The initial augmented matrix is:")
        self.ans_str += "\nThe initial augmented matrix is:"
        self.display_matrix()

        # Forward elimination to transform the system to upper triangular form
        is_valid, B_result = self.forward_elimination()
        if not is_valid:
            return False

        # Back substitution to reduce the matrix to RREF and get the solutions
        solutions = self.back_substitution()

        # Check for infinite solutions
        if np.allclose(self.A[-1], np.zeros_like(self.A[-1])) and np.allclose(self.B[-1], 0):
            print("The system has infinite solutions.")
            self.noSolution = True
            self.ans_str += "\nThe system has infinite solutions."
            return False
        else:
            print("\nSolutions:")
            self.ans_str += "\nSolutions:\n"
            for i in range(len(solutions)):
                print(f"{self.variables[i]} = {self.format_number(solutions[i])}")
                self.ans_str += f"\n{self.variables[i]} = {self.format_number(solutions[i])}"
                self.finals.append(solutions[i])

        end_time = time.time()
        print(f"\nExecution time: {end_time - start_time:.6f} seconds")
        self.ans_str += f"\nExecution time: {end_time - start_time:.6f} seconds"
        return True


# Example setup with matrices predefined
if __name__ == "__main__":
    A = [
        [1, 2, -1],
        [0, 0, 0],
        [0, 0, 0]
    ]  # Example system
    B = [8, 0, 3]   

    # User input for precision, scaling, and steps
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6

    scaling_choice = input("Apply scaling? (y/n, default n): ").strip().lower()
    scaling = scaling_choice == 'y'

    steps_choice = input("Show steps during calculation? (y/n, default n): ").strip().lower()
    steps = steps_choice == 'y'

    solver = GaussJordanElimination(A, B, scaling, steps, significant_digits=precision)

    # Solve the system
    solver.solve()

