# Question: Write a Python program to count the number of times a specific character appears in a string provided by the user.

s = input('Enter String: ')
c = input('Enter Character: ')
count = s.count(c)
print(f'{c} appears {count} times in {s}')
