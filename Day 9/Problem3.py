# Question: Write a Python program to calculate the sum of all numbers in a list of lists.

def sum_nested_lists(nested_list):
    total = 0
    for sublist in nested_list:
        for num in sublist:
            total += num
    return total

nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
total_sum = sum_nested_lists(nested_lists)
print(f'Sum of all numbers: {total_sum}')
