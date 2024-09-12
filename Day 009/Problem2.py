# Question: Write a Python program that takes a list of numbers and returns a new list containing only the even numbers.

def filter_even_numbers(list):
    return [num for num in list if num % 2 == 0]

numbers = [int(x) for x in input('Enter numbers separated by space: ').split()]
evens = filter_even_numbers(numbers)
print(f'Even numbers: {evens}')
