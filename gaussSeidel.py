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
        self.relativeError = 0
        self.ans_str = ''
        self.precision = precision if precision is not None else 6

    def max_error(self, x_new, x_old):
        max_err = 0
        for i in range(self.num_variables):
            # Format the values to significant figures before calculating error
            x_new_sf = float(self.format_significant_figures(x_new[i]))
            x_old_sf = float(self.format_significant_figures(x_old[i]))
            
            if x_old_sf != 0:
                max_err = max(max_err, abs((x_new_sf - x_old_sf) / x_old_sf))
            else:
                max_err = max(max_err, abs(x_new_sf - x_old_sf))
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
                print(f"    Current solution: {[self.format_significant_figures(val) for val in x]}")
                self.ans_str += f"\n    Current solution: {[self.format_significant_figures(val) for val in x]}"

            if self.max_error(x, x_old) < self.tol:
                break

        end_time = time.time()
        execution_time = end_time - start_time
        solution = [self.format_significant_figures(val) for val in x]

        return solution, k + 1, execution_time

################################################################################
# Example usage
if __name__ == "__main__":
    A = [
        [8, 3, 2],  # Coefficients of the first equation
        [1, 5, 1],  # Coefficients of the second equation
        [2, 1, 6]   # Coefficients of the third equation
    ]
    B = [13, 7, 9]  # Constants on the right-hand side
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

    print(f"\nSolution: {solution}")
    print(f"Iterations: {iterations}")
    print(f"Execution Time: {exec_time:.6f} seconds")
    print(f"Maximum Relative Error: {solver.relativeError:.6f}")
