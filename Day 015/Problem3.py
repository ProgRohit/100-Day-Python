# Question: Create a Module for String Manipulation Task: Write a Python module string_utils.py that contains functions for reversing a string, checking if a string is a palindrome, 
# and converting a string to uppercase. Import and use this module in another script.

# string_utils.py
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def to_uppercase(s):
    return s.upper()

# Main script
import string_utils

s = "racecar"
print(string_utils.reverse_string(s))
print(string_utils.is_palindrome(s))
print(string_utils.to_uppercase(s))
