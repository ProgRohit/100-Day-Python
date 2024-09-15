# Question: Create a Class for Books and a Derived Class for E-books Task: Write a Python program to create a base class Book and a derived class EBook
# that adds attributes for file size and format. Override the display method to show these additional details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

class EBook(Book):
    def __init__(self, title, author, price, file_size, file_format):
        super().__init__(title, author, price)
        self.file_size = file_size
        self.file_format = file_format

    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size}MB, Format: {self.file_format}")

# Example usage:
ebook = EBook("Digital Fortress", "Dan Brown", 5.99, 2, "PDF")
ebook.display_info()
