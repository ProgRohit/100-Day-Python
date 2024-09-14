# Question: Create a Class for a Rectangle Task: Write a Python program to create a Rectangle class with methods to calculate the area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
rect = Rectangle(10, 5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
