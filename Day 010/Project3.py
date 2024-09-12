# Project 3: Number Guessing Game
# Task: Create a number guessing game where the computer randomly selects a number between 1 and 100, and the user has to guess it.

import random

def guess_game():
    # Randomly generate a number between 1 and 100
    number = random.randint(1, 100)
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print(f"Congratulations! You guessed it right, the number is {number}.")
            break
            
guess_game()
