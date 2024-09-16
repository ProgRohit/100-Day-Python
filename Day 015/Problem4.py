# Question: Create a Package for Geometry Calculations Task: Create a Python package called geometry with two modules: circle.py and rectangle.py. 
# The circle.py module should contain a function to calculate the area of a circle, and rectangle.py should calculate the area of a rectangle.

# geometry/circle.py
import math
def area(radius):
    return math.pi * radius ** 2

# geometry/rectangle.py
def area(length, width):
    return length * width

# Main script
from geometry import circle, rectangle

print(circle.area(5))
print(rectangle.area(4, 6))
