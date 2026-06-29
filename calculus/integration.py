import sympy as sp

# Variable define করা
x = sp.symbols('x')

# Function: f(x) = x^2
expression = x**2

# Integration (সমাকলন) করা
result = sp.integrate(expression, x)

print(f"The integral of {expression} is: {result}")