# Question: Write a Python program to join a list of words into a single string with spaces in between.

s = input('Enter Words: ')
words_list = s.split()  # Split the input into a list of words
result_string = ' '.join(words_list)  # Join the list into a single string with spaces in between
print('String: ', result_string)
