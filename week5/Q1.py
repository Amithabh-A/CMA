from Polynomial import Polynomial
import numpy as np
import matplotlib.pyplot as plt

"""
Proedure : 
function to compute poly of deg n which
is best fit for given set of points
"""

"""
Input : 
n
array of tuples
"""

"""
Output : 
object of type Polynomial ]
"""

"""
Methodology : Multiply the hessian matrix with the Polynomial and equatewith zero. Then solve
the equation. 
"""

def BestFitPoly(n, pts, plot = True):
    x = [pt[0] for pt in pts]
    y = [pt[1] for pt in pts]
    
    X = np.zeros([len(x), n+1])

    # Generate a matrix with x**i as each column
    for i in range(n+1):
        X[:,i] = np.array(x)**i

    # use linsolve to solve the system of linear equations for the coefficients
    coeff = np.linalg.solve(X.T @ X, X.T @ y)

    # construct a polynomial with the coefficients
    p = Polynomial(list(coeff))

    X_plot = np.linspace(min(x), max(x), 100)
    Y_plot = [p[i] for i in X_plot]

    if plot:
        plt.title("Best fit polynomial of degree " + str(n) + "on given points")
        plt.scatter(x,y,c="r")
        plt.plot(X_plot, Y_plot)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.show()

    return p

if __name__ == "__main__":
    inputpts = [(0,0), (-4,-3), (1,-2), (-5,-4), (-2, -2), (2, -2)]
    print("input points : ", inputpts)
    print("Degree 4")
    print(BestFitPoly(4, inputpts))
    print("Degree 7")
    print(BestFitPoly(7, inputpts))
