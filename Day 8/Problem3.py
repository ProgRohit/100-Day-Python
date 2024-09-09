# Question: Recursive Function to Calculate Factorial

def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    else:
        print('Invalid input')

n = int(input('Enter the number: '))
if n >= 0:
    fact = factorial(n)
    print(f'The factorial of {n} is {fact}')
else:
    print('Invalid input')
