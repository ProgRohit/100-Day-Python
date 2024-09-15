# Question: Create a Base Class for Employees and a Derived Class for Managers Task: Write a Python program with an Employee class that has attributes
# like name and salary, and a method to display them. Then, create a Manager class that inherits from Employee and adds an attribute for the department.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

# Example usage:
manager = Manager("Alice", 80000, "HR")
manager.display_info()
