import numpy as np
import time


class JacobiSolver:
    def __init__(self, A, b, initial_guess=None, max_iter=100, tol=1e-5, precision=None):
        self.A = np.array(A)
        self.b = np.array(b)
        self.num_variables = len(b)
        self.initial_guess = np.zeros(self.num_variables) if initial_guess is None else np.array(initial_guess)
        self.max_iter = max_iter
        self.tol = tol
        self.precision = precision if precision is not None else 6

    ################################################################################
    def max_error(self, x_new, x_old):
        max_err = 0
        for i in range(self.num_variables):
            if x_old[i] != 0:
                max_err = max(max_err, abs((x_new[i] - x_old[i]) / x_old[i]))
            else:
                max_err = max(max_err, abs(x_new[i] - x_old[i]))
        return max_err

    ################################################################################
    def jacobi_iteration(self):
        x_old = self.initial_guess
        start_time = time.time()
        for k in range(self.max_iter):
            x_new = np.copy(x_old)
            for i in range(self.num_variables):
                sum_ = np.dot(self.A[i], x_old) - self.A[i][i] * x_old[i]
                x_new[i] = (self.b[i] - sum_) / self.A[i][i]

            if self.max_error(x_new, x_old) < self.tol:
                break

            x_old = np.copy(x_new)

        end_time = time.time()
        execution_time = end_time - start_time
        solution = np.round(x_new, self.precision)

        return solution, k + 1, execution_time


################################################################################
# ِan example :
if __name__ == "__main__":
    A = [[4, -1, 0, 0],
         [-1, 4, -1, 0],
         [0, -1, 4, -1],
         [0, 0, -1, 3]]
    b = [15, 10, 10, 10]

    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else None

    solver = JacobiSolver(A, b, max_iter=100, tol=1e-5, precision=precision)
    solution, iterations, exec_time = solver.jacobi_iteration()

    print(f"Solution: {solution}")
    print(f"Iterations: {iterations}")
    print(f"Execution Time: {exec_time:.6f} seconds")

