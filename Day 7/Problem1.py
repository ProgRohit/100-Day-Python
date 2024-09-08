# Question: Write a Python program that reverses a given string.

s = input('Enter String: ')
rev = ''
while s != '':
    rev = rev + s[-1]  # Add the last character to 'rev'
    s = s[:-1]         # Remove the last character from 's'
print(f'Reversed string is: {rev}')

#OR

s = input('Enter String: ')
rev = s[::-1]
print(rev)
