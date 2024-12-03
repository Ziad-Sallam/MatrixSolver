import numpy as np
import time

class JacobiSolver: 
    def __init__(self, A, b, initial_guess=None, max_iter=100, tol=1e-5, precision=None):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.num_variables = len(b)
        self.initial_guess = np.zeros(self.num_variables) if initial_guess is None else np.array(initial_guess, dtype=float)
        self.max_iter = max_iter
        self.tol = tol
        self.ans_str = ''
        self.relativeError = 0
        self.precision = precision if precision is not None else 6

    def max_error(self, x_new, x_old):
        max_err = 0
        for i in range(self.num_variables):
            if x_old[i] != 0:
                max_err = max(max_err, abs((x_new[i] - x_old[i]) / x_old[i]))
            else:
                max_err = max(max_err, abs(x_new[i] - x_old[i]))
        self.relativeError = max_err
        return max_err

    def format_significant_figures(self, number):
        if number == 0:
            return f"{0:.{self.precision}f}"
    
        # Normalize using scientific notation
        normalized_number = f"{number:.{self.precision - 1}e}"  # Convert to scientific notation
        base, exponent = normalized_number.split('e')  # Separate base and exponent
        base = float(base)
        formatted_base = f"{base:.{self.precision - 1}f}"  # Format base with precision

        if int(exponent) == 0:  # If exponent is 0, omit it
            return formatted_base
        return f"{formatted_base}e{int(exponent)}"

    def jacobi_iteration(self, single_step=False):
        x_old = self.initial_guess
        start_time = time.time()

        for k in range(self.max_iter):
            x_new = np.copy(x_old)
            print(f"\nIteration {k + 1}:")
            self.ans_str += f"\nIteration {k + 1}:"

            for i in range(self.num_variables):
                sum_ = 0
                terms = []
                for j in range(self.num_variables):
                    if j != i:
                        term = self.A[i][j] * x_old[j]
                        sum_ += term
                        terms.append(f"{self.A[i][j]} * {self.format_significant_figures(x_old[j])}")
                
                x_new[i] = (self.b[i] - sum_) / self.A[i][i]
                computation_details = f"x{i + 1} = ({self.b[i]} - ({' + '.join(terms)})) / {self.A[i][i]}"
                print(f"    {computation_details} = {self.format_significant_figures(x_new[i])}")
                self.ans_str += f"\n    {computation_details} = {self.format_significant_figures(x_new[i])}"
            
            if single_step:
                formatted_solution = [self.format_significant_figures(val) for val in x_new]
                print(f"    Current solution: [{', '.join(formatted_solution)}]")
                self.ans_str += f"\n    Current solution: [{', '.join(formatted_solution)}]"
            
            if self.max_error(x_new, x_old) < self.tol:
                break

            x_old = np.copy(x_new)

        end_time = time.time()
        execution_time = end_time - start_time
        solution = [self.format_significant_figures(val) for val in x_new]

        return solution, k + 1, execution_time

################################################################################
# Example usage
if __name__ == "__main__":
    A = [
        [8, 3, 2],  # Coefficients of the first equation
        [1, 5, 1],  # Coefficients of the second equation
        [2, 9, 6]   # Coefficients of the third equation
    ]
    B = [13, 7, 9] 
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else None

    # Get initial guess from user
    initial_guess_input = input(f"Enter the initial guess as space-separated values (default: {' '.join(map(str, np.zeros(len(B))))}): ")
    initial_guess = np.array([float(x) for x in initial_guess_input.split()]) if initial_guess_input else np.zeros(len(B))

    solver = JacobiSolver(A, B, initial_guess=initial_guess, max_iter=100, tol=1e-5, precision=precision)

    # Solve with optional single-step simulation
    step_mode = input("Enable single-step mode? (y/n, default n): ").strip().lower() == 'y'
    solution, iterations, exec_time = solver.jacobi_iteration(single_step=step_mode)

    print(f"\nSolution: {solution}")
    print(f"Iterations: {iterations}")
    print(f"Execution Time: {exec_time:.6f} seconds")
