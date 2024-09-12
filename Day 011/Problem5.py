# Question: Write a Python program to search for a specific word in a file and display the line numbers where it appears.

word_to_find = input("Enter the word to search: ")

with open('output.txt', 'r') as file:
    line_number = 1
    for line in file:
        if word_to_find in line:
            print(f"Found '{word_to_find}' on line {line_number}")
            break
        line_number += 1
    else:
        print(f"'{word_to_find}' not found in the file.")
