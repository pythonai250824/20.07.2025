## Mega OOP Exercise: Virtual Library System

### Goal

Design a library system using object-oriented Python that includes books, users, and borrowing functionality. Use as many OOP concepts as possible.

### Class 1: `Book`

* Private attributes: `__title`, `__author`, `__year`, `__copies`
* Methods:

  * `@property` and `@setter` for each attribute
  * `__str__` and `__repr__`
  * `__eq__`, `__hash__`
  * `__add__`, `__sub__` for adding/removing copies
  * `__gt__` to compare books by year

### Class 2: `User`

* Attributes: `name`, `user_id`, borrowed books (list of Book)
* Methods:

  * Borrow a book (check if available)
  * Return a book
  * Use `*args` to allow borrowing multiple books
  * Implement `__str__` to print borrowed books nicely

### Class 3: `Library`

* Attributes:

  * List of books (as a dictionary using Book as key)
  * List of users
* Methods:

  * `@classmethod` to create a library from a file
  * `@staticmethod` to validate book data
  * `__contains__` to check if book is in library
  * `__getitem__` to get a book by title
  * Custom `__iter__` to loop over books

### Extra Features

* Create custom exception `BookNotAvailableError`
* Add file saving/loading for books (simulate inventory)
* Add threading example where multiple users borrow books simultaneously (ThreadPoolExecutor)
* Use `memory-profiler` to profile your library object

### Bonus

* Organize into modules: `book.py`, `user.py`, `library.py`, `main.py`
* Use try-except-finally when borrowing books

### Sample Usage

```python
# main.py
from book import Book
from user import User
from library import Library

b1 = Book("Python 101", "Alice", 2020, 3)
b2 = Book("Python 201", "Bob", 2022, 2)

u1 = User("Dana", 1001)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_user(u1)

u1.borrow_books(b1, b2)
print(u1)
```

> Try to include `@override` where relevant
