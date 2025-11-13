#https://github.com/rahipat/lab11-rp

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero.")
    return a/b

def exp(a, b):
    return a ** b

def logarithm(a,b):
    if a <= 0:
        raise ValueError("Number has to be positive.")
    if b <= 0 or b == 1:
        raise ValueError("Must be positive or not 1.")
    return math.log(a, b)

def mul(a,b):
    return a * b

def hypotenuse(a,b):
    return math.sqrt((a * a) + (b * b))

def square_root(a):
    if a < 0:
        raise ValueError("The number has to positive.")
    return round(math.sqrt(a), 4)

