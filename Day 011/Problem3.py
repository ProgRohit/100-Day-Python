# Question: Write a Python program to append user input to a text file.

with open('output.txt', 'a') as file:
    data = input('Enter data to append to the file: ')
    file.write('\n' + data)
