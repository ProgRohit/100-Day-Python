# Question: Write a Python program that takes input from the user and writes it to a file.

filename = "output.txt"
user_input = input("Enter text to write to the file: ")
with open(filename, 'w') as file:
    file.write(user_input)
print(f"'{user_input}' has been written to {filename}.")
