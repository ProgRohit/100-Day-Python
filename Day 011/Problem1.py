# Question: Create a Python program that writes user input to a text file.

with open('output.txt', 'w') as file:
    data = input('Enter data to write to the file: ')
    file.write(data)
