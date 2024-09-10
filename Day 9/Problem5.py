# Question: Write a Python function that takes a list of words and returns the longest word.

def longest_word(words):
    max_len = 0
    longest = ''
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest = word
    return longest

word_list = input('Enter words separated by space: ').split()
longest = longest_word(word_list)
print(f'The longest word is: {longest}')
