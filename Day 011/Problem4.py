# Question: Write a Python program to count the number of words in a text file.

with open('output.txt', 'r') as file:
    content = file.read()
    word_count = len(content.split())
    print(f'The file contains {word_count} words.')
