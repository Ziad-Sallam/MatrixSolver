import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify
import time
import math

class SecantMethod:
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
        self.ans = ''
    
    def format_significant_figures(self, num):
     return num if num == 0 else round(num, -int(math.floor(math.log10(abs(num)))) + (self.precision - 1))
    

    def plot_function(self):
        x = np.linspace(self.x_min, self.x_max, 400)
        y = self.f(x)
        plt.plot(x, y, label='f(x)')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()

    def find_root(self, x0, x1):
       try: 
        x0 = self.format_significant_figures(x0)
        x1 = self.format_significant_figures(x1)
        for self.n in range(1, self.max_iter + 1):
            f_x0 = self.format_significant_figures(self.f(x0))  
            f_x1 = self.format_significant_figures(self.f(x1))   
            
            if abs(f_x0 - f_x1) == 0.0:
                print("Division by zero encountered. No roots found.")
                self.ans += "Division by zero encountered. No roots found.\n"
                return None
            
            x_new = self.format_significant_figures(x1 - ( f_x1 * (x0 - x1) / (f_x0 - f_x1) ))
            
            if abs(self.f(x_new)) == 0.0 :
                print(f"f(X{self.n}) = 0 , The actual root is reached.")
                self.ans += f"f(X{self.n}) = 0 , The actual root is reached.\n"
                break
            
            if self.show_steps:
                print(f"Iteration {self.n}:\nX{self.n-1} = {self.format_significant_figures(x0)}, X{self.n} = {self.format_significant_figures(x1)}")
                self.ans += f"Iteration {self.n}:\nX{self.n-1} = {self.format_significant_figures(x0)}, X{self.n} = {self.format_significant_figures(x1)}\n"
                print(f"f(X{self.n-1}) = {self.format_significant_figures(f_x0)}, f(X{self.n}) = {self.format_significant_figures(f_x1)}")
                self.ans += f"f(X{self.n-1}) = {self.format_significant_figures(f_x0)}, f(X{self.n}) = {self.format_significant_figures(f_x1)}\n"
                print(f"X{self.n+1} = {self.format_significant_figures(x1)} - ({self.format_significant_figures(f_x1)} * ({self.format_significant_figures(x0)} - {self.format_significant_figures(x1)}) / ({self.format_significant_figures(f_x0)} - {self.format_significant_figures(f_x1)})) = {self.format_significant_figures(x_new)}")
                self.ans += f"X{self.n+1} = {self.format_significant_figures(x1)} - ({self.format_significant_figures(f_x1)} * ({self.format_significant_figures(x0)} - {self.format_significant_figures(x1)}) / ({self.format_significant_figures(f_x0)} - {self.format_significant_figures(f_x1)})) = {self.format_significant_figures(x_new)}\n"

            if abs(x_new) < self.eps:  # Check if the root is close to zero
             print(f"The root is close to zero: {self.format_significant_figures(x_new)}")
             self.ans += f"The root is close to zero: {self.format_significant_figures(x_new)}\n"
             break
         
            
            self.relative_error = self.format_significant_figures(abs( (x_new - x1) / x_new ) * 100)
            if self.show_steps:
                print(f"Relative error = {self.relative_error} %")
                self.ans += f"Relative error = {self.relative_error} %\n"
            
            if self.relative_error < self.eps:
                break
             
            if abs(x_new) > 1000:  # Assumption for divergence
                print("The method will diverge.")
                self.ans += "The method will diverge."
                return None
            
            
            if self.show_steps and self.n != self.max_iter:
                print("-----------------------------------------")
                self.ans += "-----------------------------------------------\n"
            
            x0, x1 = x1, x_new
        return x_new
       except Exception as e:
            print(f"Error finding root: {e}")
            self.ans += f"Error finding root: {e}\n"
            return None


    def solve(self):
        #self.plot_function()
        x0 = self.x_min
        x1 = self.x_max
        start_time = time.time()
        root = self.find_root(x0, x1)
        if root is not None:
            print("-----------------------------------------------------")
            self.ans += f"--------------------------------------------------\n"
            if self.n == self.max_iter:
                print("Couldn't converge within the specified iterations")
                self.ans += "Couldn't converge within the specified iterations"
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
    
    equation = ("x**4-18*x**2+45")
    
    x_min = float(input("Enter the minimum x value for plotting: "))
    x_max = float(input("Enter the maximum x value for plotting: "))
    
    eps = input("Enter the epsilon (default 1e-5): ")
    eps = float(eps) if eps else 1e-5
    
    max_iter = input("Enter the maximum number of iterations (default 50): ")
    max_iter = int(max_iter) if max_iter else 50
    
    precision_input = input("Enter the number of significant figures (default 6): ")
    precision = int(precision_input) if precision_input else 6
    
    show_steps = input("Do you want to see the steps? (yes/no): ").strip().lower() == 'yes'
    
    solver = SecantMethod(equation, x_min, x_max, eps, max_iter, show_steps, precision)
    solver.solve()