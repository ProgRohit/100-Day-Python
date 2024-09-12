# Question: Write a Python function to check if a given list is sorted in ascending order.

def is_sorted(lst):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

numbers = [int(x) for x in input('Enter numbers separated by space: ').split()]
if is_sorted(numbers):
    print('The list is sorted.')
else:
    print('The list is not sorted.')
