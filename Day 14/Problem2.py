# Question: Create a Class Hierarchy for Vehicles Task: Write a Python program to create a base class Vehicle and derived classes Car and Bike that inherit from it. 
# Add methods like start_engine() and stop_engine() in the base class.

class Vehicle:
    def __init__(self, name):
        self.name = name

    def start_engine(self):
        print(f"{self.name}'s engine started.")

    def stop_engine(self):
        print(f"{self.name}'s engine stopped.")

class Car(Vehicle):
    def honk(self):
        print(f"{self.name} is honking.")

class Bike(Vehicle):
    def wheelie(self):
        print(f"{self.name} is doing a wheelie.")

# Example usage:
car = Car("Toyota")
car.start_engine()
car.honk()

bike = Bike("Yamaha")
bike.start_engine()
bike.wheelie()
