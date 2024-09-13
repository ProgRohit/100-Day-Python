# Question: Write a Python program that appends content to an existing file without overwriting its current content.

filename = "output.txt"
user_input = input("Enter text to append to the file: ")

with open(filename, 'a') as file:
    file.write("\n" + user_input)

print(f"'{user_input}' has been appended to {filename}.")
