# You are tasked with creating a simple library management system using object-oriented programming (OOP) principles in Python. The system should allow you to add books, display their information, borrow and return books, and keep track of the number of available books in the library. Additionally, implement inheritance to create a specialized class for a specific type of book.
# In this exercise, we have defined three classes: Book, Novel (inheriting from Book), and Library. The Book class represents a generic book, while the Novel class is a specialized class for novels, including an additional attribute for the genre. The Library class is responsible for managing the books in the library.
#
# The Book class has several methods and special methods:
#
# •	__init__(self, title, author, publication_year): Initializes a book with the provided title, author, and publication year.
# •	__str__(self): Returns a string representation of the book.
# •	borrow(self): Marks the book as borrowed if it is currently available.
# •	return_book(self): Marks the book as returned if it was borrowed.
# •	The Novel class inherits from Book and adds the genre attribute. It overrides the __str__() method to include the genre in the string representation.
#
# The Library class has methods for managing the books:
#
# •	__init__(self): Initializes an empty list of books.
# •	add_book(self, book): Adds a book to the library.
# •	display_books(self): Displays information about all the books in the library.
# •	count_available_books(self): Counts and displays the number of available books in the library.

class Book:
    def __init__(self, title, author, publication_year):

    # Your code here

    def __str__(self):

    # Your code here

    def borrow(self):

    # Your code here

    def return_book(self):


# Your code here


class Novel(Book):
    def __init__(self, title, author, publication_year, genre):

    # Your code here

    def __str__(self):


# Your code here


class Library:
    def __init__(self):

    # Your code here

    def add_book(self, book):

    # Your code here

    def display_books(self):

    # Your code here

    def count_available_books(self):


# Your code here


# Example usage
library = Library()

book1 = Book("Python Programming", "John Smith", 2021)
book2 = Book("Data Science Essentials", "Jane Johnson", 2020)
novel1 = Novel("Pride and Prejudice", "Jane Austen", 1813, "Romance")

library.add_book(book1)
library.add_book(book2)
library.add_book(novel1)

library.display_books()

novel1.borrow()
book2.borrow()

library.count_available_books()

novel1.return_book()

library.count_available_books()
