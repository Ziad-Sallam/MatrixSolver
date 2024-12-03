import numpy as np
import time

class GaussSeidelSolver:
    def __init__(self, A, b, initial_guess=None, max_iter=100, tol=1e-5, precision=None):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.num_variables = len(b)
        self.initial_guess = np.zeros(self.num_variables) if initial_guess is None else np.array(initial_guess, dtype=float)
        self.max_iter = max_iter
        self.tol = tol
        self.precision = precision if precision is not None else 6
        self.ans_str = ""

    def max_error(self, x_new, x_old):
        max_err = 0
        for i in range(self.num_variables):
            if x_old[i] != 0:
                max_err = max(max_err, abs((x_new[i] - x_old[i]) / x_old[i]))
            else:
                max_err = max(max_err, abs(x_new[i] - x_old[i]))
        return max_err

    def format_significant_figures(self, number):
        # Handle the case where number is zero
        if number == 0:
            return f"{number:.{self.precision}f}"
        
        # Get the number of significant figures before the decimal point
        num_digits_before_decimal = len(str(int(abs(number))))  

        # Calculate how many decimal places we need
        significant_digits_needed = self.precision - num_digits_before_decimal

        # If we need fewer decimal places than the precision allows
        if significant_digits_needed < 0:
            # Just round the number to the specified precision
            return f"{number:.{self.precision}f}"

        # Otherwise, format the number based on significant digits
        return f"{number:.{significant_digits_needed}f}"

    def gauss_seidel_iteration(self, single_step=False):
        x = self.initial_guess
        start_time = time.time()

        for k in range(self.max_iter):
            x_old = np.copy(x)
            print(f"\nIteration {k + 1}:")
            self.ans_str += f"\nIteration {k + 1}:"

            for i in range(self.num_variables):
                sum_ = 0
                terms = []
                for j in range(self.num_variables):
                    if j != i:
                        term = self.A[i][j] * x[j]
                        sum_ += term
                        terms.append(f"{self.A[i][j]} * {self.format_significant_figures(x[j])}")
                
                x[i] = (self.b[i] - sum_) / self.A[i][i]
                computation_details = f"x{i + 1} = ({self.b[i]} - ({' + '.join(terms)})) / {self.A[i][i]}"
                print(f"    {computation_details} = {self.format_significant_figures(x[i])}")
                self.ans_str += f"\n    {computation_details} = {self.format_significant_figures(x[i])}"
            
            if single_step:
                print(f"\n    Current solution: {[self.format_significant_figures(val) for val in x]}")
                self.ans_str += f"\n    Current solution: {[self.format_significant_figures(val) for val in x]}"
            if self.max_error(x, x_old) < self.tol:
                break

        end_time = time.time()
        execution_time = end_time - start_time
        solution = np.round(x, self.precision)

        return solution, k + 1, execution_time

################################################################################
# Example usage
if __name__ == "__main__":
    A = [[4, -1, 0, 0],
         [-1, 4, -1, 0],
         [0, -1, 4, -1],
         [0, 0, -1, 3]]
    B = [15, 10, 10, 10]

    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else None

    # Prompt user to enter initial guess with default shown
    default_initial_guess = " ".join(["0.0"] * len(A[0]))  # Default: 0.0 0.0 0.0 0.0
    initial_guess_input = input(f"Enter the initial guess as space-separated values (default: {default_initial_guess}): ")
    
    if initial_guess_input:
        initial_guess = list(map(float, initial_guess_input.split()))
    else:
        initial_guess = None  # Default to zero if input is empty

    solver = GaussSeidelSolver(A, B, initial_guess=initial_guess, max_iter=100, tol=1e-5, precision=precision)

    # Solve with optional single-step simulation
    step_mode = input("Enable single-step mode? (y/n, default n): ").strip().lower() == 'y'
    solution, iterations, exec_time = solver.gauss_seidel_iteration(single_step=step_mode)

    print(f"\nSolution: {[solver.format_significant_figures(val) for val in solution]}")
    print(f"Iterations: {iterations}")
    print(f"Execution Time: {exec_time:.6f} seconds")
