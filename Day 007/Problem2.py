# Question: Write a Python program that checks if a string is a palindrome.

string = input('Enter String: ')
s = string
rev = ''
while s != '':
    rev = rev + s[-1]  # Add the last character to 'rev'
    s = s[:-1]         # Remove the last character from 's'
if rev == string:
  print('String is Palindrome')
else:
  print('String is not Palindrome')

#OR

s = "racecar"
rev = ""
for char in s:
    rev = char + rev
if rev == s:
  print('String is Palindrome')
else:
  print('String is not Palindrome')

