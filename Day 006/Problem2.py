# Question: Find the Largest of Three Numbers

a = int(input('Enter Number: '))
b = int(input('Enter Number: '))
c = int(input('Enter Number: '))
if a > b and a > c:
    print('Largest number is: ', a)
elif b > a and b > c:
    print('Largest number is: ', b)
else:
    print('Largest number is: ', c)
