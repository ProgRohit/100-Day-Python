# Question: Write a Python program to reverse a list.

l = [1, 2, 3, 4, 5]
rev = []
for i in range(len(l)):
    rev.append(l[len(l) - 1 - i])  # Access elements from the end to the beginning
print(rev)
