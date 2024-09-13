# Question: Write a Python program that counts the number of lines in a file and prints the result.

filename = "sample.txt"

with open(filename, 'r') as file:
    lines = file.readlines()

print(f"The file has {len(lines)} lines.")
