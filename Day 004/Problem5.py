# Question: Write a Python program to print the following pattern of stars for a given number n (number of rows):
'''
*
**
***
****
*****
'''

n = int(input('Enter the number: '))
for i in range(1, n+1):
    print('*' * i)
