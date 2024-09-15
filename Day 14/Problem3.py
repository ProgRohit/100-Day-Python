# Question: Create a Class for Shapes and a Derived Class for Circle Task: Write a Python program to create a base class Shape and a derived class Circle that inherits from it. 
# Add a method in Circle to calculate the area.

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Shape: {self.name}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage:
circle = Circle(5)
circle.display_name()
print(f"Area: {circle.area()}")
