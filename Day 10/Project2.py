# Project 2: Palindrome Checker for Lists
# Task: Write a Python program that checks if a list of numbers is a palindrome.

def is_palindrome(list):
    # Check if the list is equal to its reverse
    if list == list[::-1]:
        print("The list is a palindrome.")
    else:
        print("The list is not a palindrome.")
        
# Take input list from the user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
is_palindrome(numbers)
