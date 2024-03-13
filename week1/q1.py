import math
import matplotlib.pyplot as plt

# stirling's approximation function
def stirling(n):
    print("hello")
    return math.sqrt(2*math.pi*n) * (n/math.e)**n

# log of Stirling's approximation function
def stirlingLog(n):
    return 0.5*math.log(2*math.pi*n) + n*(math.log(n)-1)

# iterative factorial function. Does work for large n. 
def factorial(n):
    ans = 1
    for i in range(n):
        ans *= i
    return ans

def logOfFactorial(n):
    return math.log(factorial(n))


