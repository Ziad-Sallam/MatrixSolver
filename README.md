## **Linear Equations Solver in Java**  

### **1. Gauss Elimination**  
A direct method for solving linear systems by:  
- **Transforming the matrix** into an upper triangular form.  
- **Performing back substitution** to compute the solution.  

### **2. Gauss-Jordan Elimination**  
An extension of Gauss Elimination that:  
- **Transforms the matrix** into reduced row echelon form (RREF).  
- **Provides the solution directly** without the need for back substitution.  

### **3. LU Decomposition**  
A method that decomposes a matrix into the product of:  
- **A lower triangular matrix (L).**  
- **An upper triangular matrix (U).**  

This facilitates easier computation of linear systems. There are multiple approaches to LU decomposition:  
- **Doolittle Method**: Produces a unit lower triangular matrix (L) and a regular upper triangular matrix (U).  
- **Crout Method**: Produces a lower triangular matrix (L) with non-zero diagonal elements and an upper triangular matrix (U) with unit diagonal elements.  
- **Cholesky Decomposition**: Specialized for symmetric positive-definite matrices, decomposing them into the product of a lower triangular matrix and its transpose.  

### **4. Gauss-Seidel Method**  
An iterative technique for solving systems of linear equations:  
- Particularly **useful for large systems** where direct methods become computationally expensive.  
- **Converges efficiently** for diagonally dominant matrices.  

### **5. Jacobi Iteration**  
Another iterative method designed for solving systems of linear equations:  
- **Works well with matrices** that are diagonally dominant.  
- Often used as a **simple iterative approach** in numerical computations.  

---
