# Question: Write a Python program to find and print the maximum element in a list of numbers.

l = [1, 2, 3, 4, 5]
max_value = l[0]
for num in l:
    if num > max_value:
        max_value = num
print(max_value)
