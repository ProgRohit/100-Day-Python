# Question: Write a Python program to count the frequency of a specified character in a given string.

s = input('Enter string: ')
c = input('Enter Character: ')
n = 0
for char in s:
    if char == c:
        n += 1
print(f'Frequency of character is {n}')
