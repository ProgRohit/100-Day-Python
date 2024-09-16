# Question: Use the random Module to Simulate a Dice Roll Task: Write a Python program that simulates the rolling of a six-sided dice using the random module.
# Each time the program is run, it should print a random number between 1 and 6.

import random

def roll_dice():
    return random.randint(1, 6)

print(f"The dice rolled: {roll_dice()}")
