# Question: Function with a Default Argument to Calculate Power

def power(base, exponent=2):
    return base ** exponent

n = int(input('Enter the base number: '))
result = power(n)
print(f'The result is: {result}')
