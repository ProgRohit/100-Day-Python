# Question: Write a Python program to calculate the factorial of a given number n using a for loop.

n = int(input('Enter the number: '))
fac = 1
for i in range(1, n+1):
    fac = fac*i
print(fac)
