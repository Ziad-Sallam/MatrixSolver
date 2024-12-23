import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify
import time
import math

class FalsePosition:
    def __init__(self, equation, x_min, x_max, eps=1e-5, max_iter=50, show_steps=False, precision=6):
        self.x = symbols('x')
        self.f_sympy = sympify(equation)
        self.f = lambdify(self.x, self.f_sympy, 'numpy')
        self.x_min = x_min
        self.x_max = x_max
        self.eps = eps
        self.max_iter = max_iter
        self.show_steps = show_steps
        self.precision = precision
        self.n = 1
        self.relative_error = 0
        self.ans =''
    
    def format_significant_figures(self, num):
        """Format a number to the specified significant digits."""
        if num == 0:
            self.ans += f"{float(f"{0:.{self.precision}g}")}\n"
            return float(f"{0:.{self.precision}g}")
        else:
            self.ans += f"{float(f"{num:.{self.precision}g}")}\n"
            return float(f"{num:.{self.precision}g}")

    def plot_function(self):
        x = np.linspace(self.x_min, self.x_max, 400)
        y = self.f(x)
        plt.plot(x, y, label='f(x)')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()

    def find_root(self, a, b):
        if self.f(a) * self.f(b) >= 0:
            print("False Position method fails.")
            self.ans += "False Position method fails.\n"
            return None
        X_l = a
        X_u = b
        X_r_old = None
        for self.n in range(1, self.max_iter + 1):
            # False Position formula
            X_r = ( (self.f(X_u) * X_l ) -(self.f(X_l) * X_u) ) / (self.f(X_u) - self.f(X_l))
            f_m_n = self.f(X_r)
            if self.show_steps:
                print(f"Iteration {self.n}:\nX_l = {self.format_significant_figures(X_l)}, f(X_l) = {self.format_significant_figures(self.f(X_l))}\nX_u = {self.format_significant_figures(X_u)}, f(X_u) = {self.format_significant_figures(self.f(X_u))}\nX_r = {self.format_significant_figures(X_r)} , f(X_r) = {self.format_significant_figures(f_m_n)}")
                self.ans += f"Iteration {self.n}:\nX_l = {self.format_significant_figures(X_l)}, f(X_l) = {self.format_significant_figures(self.f(X_l))}\nX_u = {self.format_significant_figures(X_u)}, f(X_u) = {self.format_significant_figures(self.f(X_u))}\nX_r = {self.format_significant_figures(X_r)} , f(X_r) = {self.format_significant_figures(f_m_n)}\n"

            if abs(f_m_n) == 0.0:
                print("f(X_r) = 0 , The actual root is reached.")
                self.ans += "f(X_r) = 0 , The actual root is reached.\n"
                return X_r
            elif self.f(X_l) * f_m_n > 0:
                X_l = X_r
                if self.show_steps:
                    print(f"f(X_l) and f(X_r) have same sign, then X_l(new) = X_r = {self.format_significant_figures(X_l)}")
                    self.ans += f"f(X_l) and f(X_r) have same sign, then X_l(new) = X_r = {self.format_significant_figures(X_l)}\n"
            elif self.f(X_u) * f_m_n > 0:
                X_u = X_r
                if self.show_steps:
                    print(f"f(X_u) and f(X_r) have same sign, then X_u(new) = X_r = {self.format_significant_figures(X_u)}")
                    self.ans += f"f(X_u) and f(X_r) have same sign, then X_u(new) = X_r = {self.format_significant_figures(X_u)}\n"
            else:
                print("False Position method fails.")
                self.ans += "False Position method fails.\n"
                return None
            
            if X_r_old is not None:
                self.relative_error = abs((X_r - X_r_old) / X_r) * 100
                if self.show_steps:
                    print(f"Relative error = {self.format_significant_figures(self.relative_error)} %")
                    self.ans += f"Relative error = {self.format_significant_figures(self.relative_error)} %\n"
                if self.relative_error < self.eps:
                    break
            X_r_old = X_r
            
            if self.show_steps and self.n != self.max_iter :
                print("-----------------------------------------")
                self.ans += ("----------------------------------------------\n")
        return X_r

    def solve(self):
        self.plot_function()
        a = self.x_min
        b = self.x_max
        start_time = time.time()
        root = self.find_root(a, b)
        if root is not None:
            print("-----------------------------------------------------")
            self.ans += "----------------------------------------------\n"

            if self.n == self.max_iter:
                print("Couldn't converge within the specified iterations")
                self.ans += "Couldn't converge within the specified iterations\n"
            print(f"The root is: {self.format_significant_figures(root)}")
            self.ans += f"The root is: {self.format_significant_figures(root)}\n"
            print(f"Number of iterations = {self.n}")
            self.ans += f"Number of iterations = {self.n}\n"
            print(f"Approximate relative error = {self.format_significant_figures(self.relative_error)}%")
            self.ans += f"Approximate relative error = {self.format_significant_figures(self.relative_error)}%\n"
            if self.relative_error > 5:
              print("Number of correct significant figures = 0")
              self.ans += "Number of correct significant figures = 0\n"
            elif self.relative_error != 0.0 :
             print(f"Number of correct significant figures = {math.floor(2-math.log10(self.relative_error/0.5))}")
             self.ans += f"Number of correct significant figures = {math.floor(2-math.log10(self.relative_error/0.5))}\n"
            else:
             print("All significant figures are correct")
             self.ans += "All significant figures are correct\n"
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Execution Time: {execution_time:.8f} seconds")
            self.ans += f"Execution Time: {execution_time:.8f} seconds"

if __name__ == "__main__":
    x = symbols('x')
    equation = "x**4+3*x-4"  # Example equation
    
    x_min = float(input("Enter the minimum x value for plotting: "))
    x_max = float(input("Enter the maximum x value for plotting: "))
    
    eps = input("Enter the epsilon (default 1e-5): ")
    eps = float(eps) if eps else 1e-5
    
    max_iter = input("Enter the maximum number of iterations (default 50): ")
    max_iter = int(max_iter) if max_iter else 50
    
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6
    
    show_steps = input("Do you want to see the steps? (yes/no): ").strip().lower() == 'yes'
    
    solver = FalsePosition(equation, x_min, x_max, eps, max_iter, show_steps, precision)
    solver.solve()