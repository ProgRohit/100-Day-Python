# Question: Write a Python program to replace all occurrences of a specific substring within a string provided by the user.

s = input('Enter String: ')
ss = input('Enter Substring: ')
ns = input('Enter New Substring: ')
mod_string = s.replace(ss, ns)
print('Modified String: ', mod_string)
