# Project 1: Simple Calculator
# Task: Create a Python program that performs addition, subtraction, multiplication, and division based on user input.

def calculator():
    # Take input for numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Take input for operation
    operation = input("Choose operation (+, -, *, /): ")
    
    # Perform operation and display result
    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operation.")
        
calculator()
