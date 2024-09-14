# Question: Create a Class for a Car Task: Write a Python program to create a Car class with attributes like make, model, and year, and a method to display the car's information.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Example usage:
car = Car("Toyota", "Corolla", 2021)
car.display_info()
