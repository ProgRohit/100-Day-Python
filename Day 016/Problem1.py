# Question: Write a Python program that takes two numbers as input and performs division. Handle the case where the second number is zero and print an appropriate message.

try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
