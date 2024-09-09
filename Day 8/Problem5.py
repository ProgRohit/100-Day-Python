# Question: Function to Check if a Number is Prime

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False  # Return False if a divisor is found
    return True  # If no divisors are found, return True

n = int(input('Enter the number: '))

# Check for special cases
if n > 2:
    print(is_prime(n))
elif n == 2:
    print(True)  # 2 is prime
else:
    print(False)  # Numbers less than 2 are not prime

