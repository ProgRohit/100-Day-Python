# Question: Write a Python program to count the number of vowels in a given string.

s = input('Enter string: ')
vowel = ['a', 'e', 'i', 'o', 'u']
n = 0
for v in range(0, 5):
  for i in range(0, len(s)):
    if s[i] == vowel[v]:
      n += 1
print(f'Number of vowels is {n}')

#OR

s = input('Enter string: ')
vowels = ['a', 'e', 'i', 'o', 'u']
n = 0
for char in s:
    if char in vowels:
        n = n+1
print(f'Number of vowels is {n}')
