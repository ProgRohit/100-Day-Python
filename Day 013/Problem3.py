# Question: Create a Class for a Student Task: Write a Python program to create a Student class with attributes like name, age, and grade, and a method to display the student's information.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Example usage:
student = Student("John", 16, "10th Grade")
student.display_info()
