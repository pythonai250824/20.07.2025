# main.py
from book import Book
from user import User
from library import Library

b1 = Book("Python 101", "Alice", 2020)
b2 = Book("Python 201", "Bob", 2020)

# u1 = User("Dana", 1001)
#
# lib = Library()
# lib.add_book(b1)
# lib.add_book(b2)
# lib.add_user(u1)
#
# u1.borrow_books(b1, b2, lib)
#
# print(u1)
print(b1 <= b2)
print(b1 > 2018)
print(b1 < 2021)