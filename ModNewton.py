import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify, diff
import time
import math

class ModNewtonRaphsonMethod:
    def __init__(self, equation, x_min, x_max, eps=1e-5, max_iter=50, show_steps=False, precision=6):
        self.x = symbols('x')
        self.f_sympy = sympify(equation)
        self.f = lambdify(self.x, self.f_sympy, 'numpy')
        self.f_prime_sympy = diff(self.f_sympy, self.x)
        self.f_prime = lambdify(self.x, self.f_prime_sympy, 'numpy')
        self.f_double_prime_sympy = diff(self.f_prime_sympy, self.x)
        self.f_double_prime = lambdify(self.x, self.f_double_prime_sympy, 'numpy')
        self.x_min = x_min
        self.x_max = x_max
        self.eps = eps
        self.max_iter = max_iter
        self.show_steps = show_steps
        self.precision = precision
        self.n = 1
        self.relative_error = 0
        self.ans = ""
    
    def format_significant_figures(self, num):
        """Format a number to the specified significant digits."""
        if num == 0:
            return f"{0:.{self.precision}g}"
        else:
            return f"{num:.{self.precision}g}"

    def plot_function(self):
        x = np.linspace(self.x_min, self.x_max, 400)
        y = self.f(x)
        plt.plot(x, y, label='f(x)')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()

    def find_root(self, x0):
        x_old = x0
        for self.n in range(1, self.max_iter + 1):
            f_value = self.f(x_old)
            f_prime_value = self.f_prime(x_old)
            f_double_prime_value = self.f_double_prime(x_old)
            if abs(f_value) == 0.0 :
                print(f"f(X{self.n}) = 0 , The actual root is reached.")
                self.ans += f"f(X{self.n}) = 0 , The actual root is reached.\n"
                x_new = x_old
                break
            
            if f_prime_value**2 - (f_value * f_double_prime_value) == 0.0:
                print("Divison by zero. No roots found.")
                self.ans += f"Division by zero. No roots found.\n"
                return None
            x_new = x_old - ((f_value * f_prime_value) / (f_prime_value**2 - (f_value * f_double_prime_value) ) )
           
            if self.show_steps:
                print(f"Iteration {self.n}:\nX{self.n-1} = {self.format_significant_figures(x_old)}")
                self.ans += f"Iteration {self.n}:\nX{self.n-1} = {self.format_significant_figures(x_old)}\n"
                print(f"f(X{self.n-1}) = {self.format_significant_figures(f_value)}, f'(X{self.n-1}) = {self.format_significant_figures(f_prime_value)} , f''(x{self.n-1}) = {self.format_significant_figures(f_double_prime_value)}")
                self.ans += f"f(X{self.n-1}) = {self.format_significant_figures(f_value)}, f'(X{self.n-1}) = {self.format_significant_figures(f_prime_value)} , f''(x{self.n-1}) = {self.format_significant_figures(f_double_prime_value)}\n"
                print(f"X{self.n} = {self.format_significant_figures(x_old)} - ( ({self.format_significant_figures(f_value)} * {self.format_significant_figures(f_prime_value)}) / ({self.format_significant_figures(f_prime_value**2)} - ({self.format_significant_figures(f_value)} * {self.format_significant_figures(f_double_prime_value)}))) = {self.format_significant_figures(x_new)}")
                self.ans += f"X{self.n} = {self.format_significant_figures(x_old)} - ( ({self.format_significant_figures(f_value)} * {self.format_significant_figures(f_prime_value)}) / ({self.format_significant_figures(f_prime_value**2)} - ({self.format_significant_figures(f_value)} * {self.format_significant_figures(f_double_prime_value)}))) = {self.format_significant_figures(x_new)}\n"
            if abs(x_new) < self.eps:  # Check if the root is close to zero
             print(f"The root is close to zero: {self.format_significant_figures(x_new)}")
             self.ans += f"The root is close to zero: {self.format_significant_figures(x_new)}\n"
             break
         
            if abs(x_new) > 1000:                                   #ASSUMPTION BY ME (MAY BE WRONG)              
                    print("The method will diverge.")
                    self.ans += f"The method will diverge.\n"
                    return None
            
            self.relative_error = abs((x_new - x_old) / x_new) * 100
            if self.show_steps:
                print(f"Relative error = {self.format_significant_figures(self.relative_error)} %")
                self.ans += f"Relative error = {self.format_significant_figures(self.relative_error)} %\n"
            if self.relative_error < self.eps:
                break
            if self.show_steps and self.n != self.max_iter:
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
            self.ans += '--------------------------------------------------------\n'
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
            self.ans += f"Execution Time: {execution_time:.8f} seconds\n"

if __name__ == "__main__":
    x = symbols('x')
    
    equation = ("x**3-(5*x**2)+7*x-3")
    
    x_min = float(input("Enter the minimum x value for plotting: "))
    x_max = float(input("Enter the maximum x value for plotting: "))
    
    eps = input("Enter the epsilon (default 1e-5): ")
    eps = float(eps) if eps else 1e-5
    
    max_iter = input("Enter the maximum number of iterations (default 50): ")
    max_iter = int(max_iter) if max_iter else 50
    
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6
    
    show_steps = input("Do you want to see the steps? (yes/no): ").strip().lower() == 'yes'
    
    solver = ModNewtonRaphsonMethod(equation, x_min, x_max, eps, max_iter, show_steps, precision)
    solver.solve()