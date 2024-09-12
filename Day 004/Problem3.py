# Question: Write a Python program to calculate the sum of the first n natural numbers using a for loop. The value of n is provided by the user.

n = int(input('Enter the number: '))
sum = 0
for i in range(1, n+1):
    sum = sum+i
print(sum)
