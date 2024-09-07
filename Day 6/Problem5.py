# Question: Check if a String Contains a Specific Word

s = input('Enter String: ')
word = input('Which word do you want to find? ')
if word in s:
    print('The word exists in the string!')
else:
    print('The word does not exist in the string!')
