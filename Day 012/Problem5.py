# Question: Write a Python program that reads content from one file and writes it to another file.

source_file = "source.txt"
destination_file = "destination.txt"

with open(source_file, 'r') as source:
    content = source.read()

with open(destination_file, 'w') as destination:
    destination.write(content)

print(f"Content from {source_file} has been copied to {destination_file}.")
