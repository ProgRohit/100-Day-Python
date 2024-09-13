# Question: Write a Python program that reads a file and prints its content to the console.

filename = "sample.txt"
with open(filename, 'r') as file:
    content = file.read()
print("File Content:")
print(content)
