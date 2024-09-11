# Project 5: Word Frequency Counter
# Task: Write a Python program to count the frequency of each word in a given sentence.

def word_frequency(sentence):
    # Split the sentence into words
    words = sentence.split()
    freq = {}
    
    # Count the frequency of each word
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    # Display the word frequencies
    for word, count in freq.items():
        print(f"{word}: {count}")
        
# Take input from the user
sentence = input("Enter a sentence: ")
word_frequency(sentence)
