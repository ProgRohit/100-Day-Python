# Question: Write a Python program to read the contents of a file and display it.

with open('output.txt', 'r') as file:
    content = file.read()
    print(f'File content:\n{content}')
