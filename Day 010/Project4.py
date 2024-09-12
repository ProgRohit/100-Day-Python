# Project 4: Prime Number Generator
# Task: Create a program that generates all prime numbers up to a given number.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Ask the user for a limit
n = int(input("Generate prime numbers up to: "))
print(f"Prime numbers up to {n}: {prime_numbers(n)}")
