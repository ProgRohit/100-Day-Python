# Question: Write a Python program to calculate simple interest based on user inputs for principal, rate, and time.

p = float(input('Principal amount: '))
r = float(input('Annual interest rate (in %): '))
t = float(input('Time in years: '))

SI = (p * r * t) / 100
print("Simple Interest:", SI)
