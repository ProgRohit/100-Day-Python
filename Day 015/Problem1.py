# Question: Create a Simple Math Module Task: Write a Python module simple_math.py that contains functions for basic arithmetic operations:addition, subtraction, multiplication, and division. 
# Import this module into a separate script to perform calculations.

# simple_math.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Main script
import simple_math

print(simple_math.add(5, 3))
print(simple_math.divide(10, 2))
