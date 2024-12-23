import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify, diff
import time
import math

class FixedPointMethod:
    def __init__(self, equation, x_min, x_max, eps=1e-5, max_iter=50, show_steps=False, precision=6):
        self.x = symbols('x')
        self.g_sympy = sympify(equation)
        self.g = lambdify(self.x, self.g_sympy, 'numpy')
        self.g_prime_sympy = diff(self.g_sympy, self.x)
        self.g_prime = lambdify(self.x, self.g_prime_sympy, 'numpy')
        self.x_min = x_min
        self.x_max = x_max
        self.eps = eps
        self.max_iter = max_iter
        self.show_steps = show_steps
        self.precision = precision
        self.n = 1
        self.relative_error = 0
        self.prev_relative_error = None
        self.ans = ''
    
    def format_significant_figures(self, num):
        """Format a number to the specified significant digits."""
        if num == 0:
            return f"{0:.{self.precision}g}"
        else:
            return f"{num:.{self.precision}g}"

    def plot_function(self):
        x = np.linspace(self.x_min, self.x_max, 400)
        y = self.g(x)
        plt.plot(x, y, label='g(x)')
        plt.plot(x, x, label='y = x', linestyle='--')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()

    def find_root(self, x0):
        x_old = x0
        for self.n in range(1, self.max_iter + 1):
            x_new = self.g(x_old)
            g_prime_value = abs(self.g_prime(x_old))
            
            if self.g(x_old) == x_old :
                print(f"The actual root is reached.")
                self.ans += f"The actual root is reached.\n"
                x_new = x_old
                break 
            
            if self.show_steps:
                print(f"Iteration {self.n}:\nX{self.n-1} = {self.format_significant_figures(x_old)}, X{self.n} = {self.format_significant_figures(x_new)}")
                self.ans += f"Iteration {self.n}:\nX{self.n-1} = {self.format_significant_figures(x_old)}, X{self.n} = {self.format_significant_figures(x_new)}\n"
                print(f"|g'(X{self.n-1})| = {self.format_significant_figures(g_prime_value)}")
                self.ans += f"|g'(X{self.n-1})| = {self.format_significant_figures(g_prime_value)}\n"
            
            if abs(x_new) < self.eps:  # Check if the root is close to zero
             print(f"The root is close to zero: {self.format_significant_figures(x_new)}")
             self.ans += f"The root is close to zero: {self.format_significant_figures(x_new)}\n"
             break
         
            self.relative_error = abs((x_new - x_old) / x_new) * 100
            if self.show_steps:
                print(f"Relative error = {self.format_significant_figures(self.relative_error)} %")
                self.ans += f"Relative error = {self.format_significant_figures(self.relative_error)} %\n"
            if g_prime_value > 1:     
                if abs(x_new) > 1000 :        #ASSUMPTION BY ME (MAY BE WRONG)              
                    print("The method will diverge.")
                    self.ans += f"The method will diverge.\n"
                    return None
            if self.relative_error < self.eps:
                break
            if self.show_steps and self.n != self.max_iter :
                print("-----------------------------------------")
                self.ans += "-------------------------------------------\n"
                
            x_old = x_new    
        return x_new

    def solve(self):
        #self.plot_function()
        x0 = self.x_min
        start_time = time.time()
        root = self.find_root(x0)
        if root is not None:
            print("-----------------------------------------------------")
            self.ans += f"-----------------------------------------------------\n"
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
    
    equation = ("x**3")
    
    x_min = float(input("Enter the minimum x value for plotting: "))
    x_max = float(input("Enter the maximum x value for plotting: "))
    
    eps = input("Enter the epsilon (default 1e-5): ")
    eps = float(eps) if eps else 1e-5
    
    max_iter = input("Enter the maximum number of iterations (default 50): ")
    max_iter = int(max_iter) if max_iter else 50
    
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6
    
    show_steps = input("Do you want to see the steps? (yes/no): ").strip().lower() == 'yes'
    
    solver = FixedPointMethod(equation, x_min, x_max, eps, max_iter, show_steps, precision)
    solver.solve()
    
    