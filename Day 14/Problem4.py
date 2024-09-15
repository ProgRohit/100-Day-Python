# Question: Create a Class for Animals and a Derived Class for Birds Task: Write a Python program to create a base class Animal with a method sound().
# Create a derived class Bird that overrides the sound() method to display a bird-specific sound.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

class Bird(Animal):
    def sound(self):
        print(f"{self.name} chirps.")

# Example usage:
bird = Bird("Parrot")
bird.sound()
