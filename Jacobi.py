import numpy as np
import time

class JacobiSolver: 
    def __init__(self, A, b, initial_guess=None, max_iter=100, tol=1e-5, precision=None, scaling=False):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.num_variables = len(b)
        self.initial_guess = np.zeros(self.num_variables) if initial_guess is None else np.array(initial_guess, dtype=float)
        self.max_iter = max_iter
        self.tol = tol
        self.precision = precision if precision is not None else 6
        self.scaling = scaling
        self.ans_str = ""
        if self.scaling:
            self.apply_scaling()

    def apply_scaling(self):
        for i in range(self.num_variables):
            max_coeff = max(abs(self.A[i]))
            self.A[i] /= max_coeff
            self.b[i] /= max_coeff

    def max_error(self, x_new, x_old):
        max_err = 0
        for i in range(self.num_variables):
            if x_old[i] != 0:
                max_err = max(max_err, abs((x_new[i] - x_old[i]) / x_old[i]))
            else:
                max_err = max(max_err, abs(x_new[i] - x_old[i]))
        return max_err

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
                        terms.append(f"{self.A[i][j]} * {x_old[j]:.{self.precision}f}")
                
                x_new[i] = (self.b[i] - sum_) / self.A[i][i]
                computation_details = f"x{i + 1} = ({self.b[i]} - ({' + '.join(terms)})) / {self.A[i][i]}"
                print(f"    {computation_details} = {x_new[i]:.{self.precision}f}")
                self.ans_str+=f"\n    {computation_details} = {x_new[i]:.{self.precision}f}"
            
            if single_step:
                print(f"    Current solution: {np.round(x_new, self.precision)}")
                self.ans_str+=f"\n    Current solution: {np.round(x_new, self.precision)}\n"
            if self.max_error(x_new, x_old) < self.tol:
                break

            x_old = np.copy(x_new)

        end_time = time.time()
        execution_time = end_time - start_time
        solution = np.round(x_new, self.precision)

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

    scaling_choice = input("Apply scaling? (y/n, default n): ").strip().lower()
    scaling = scaling_choice == 'y'

    solver = JacobiSolver(A, B, max_iter=100, tol=1e-5, precision=precision, scaling=scaling)

    # Solve with optional single-step simulation
    step_mode = input("Enable single-step mode? (y/n, default n): ").strip().lower() == 'y'
    solution, iterations, exec_time = solver.jacobi_iteration(single_step=step_mode)

    print(f"\nSolution: {solution}")
    print(f"Iterations: {iterations}")
    print(f"Execution Time: {exec_time:.6f} seconds")
