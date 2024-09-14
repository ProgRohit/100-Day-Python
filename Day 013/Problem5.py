# Question: Create a Class for a Book Task: Write a Python program to create a Book class with attributes like title, author, and price, and a method to display the book's information.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

# Example usage:
book = Book("1984", "George Orwell", 9.99)
book.display_info()
