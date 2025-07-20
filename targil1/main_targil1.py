# main.py
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor

from book import Book
from user import User
from library import Library

b1 = Book("Python 101", "Alice", 2020)
b2 = Book("Python 201", "Bob", 2020)
b3 = Book("Python 202", "Merlin", 2020)

u1 = User("Dana", 1001)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_user(u1)

print('lib[b1] number of copies for book b1', lib[b1])  # __getitem__ -- print number of copies

u1.borrow_books(lib, b1, b2)

for book in lib:  # __iter__
    print(book)

print('b1 in lib', b1 in lib)  #  __contains__

print('b1 <= b2', b1 <= b2)
print('b1 > 2018', b1 > 2018)
print('b1 < 2021', b1 < 2021)

u2 = User("Shlomi", 1002)
u3 = User("Rina", 1003)

lib.add_book(b3)
lib.add_user(u2)
lib.add_user(u3)

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(u2.borrow_books, lib, b3)
    executor.submit(u3.borrow_books, lib, b3)

def print1_10(i):
    time.sleep(0.05)
    for _ in range(1, 5):
        time.sleep(0.05)
        print('=============')
        print(f'thread {threading.get_ident()} ---> {i} ---> ', _)

with ThreadPoolExecutor(max_workers=1) as executor:
    for i in range(10):
        executor.submit(print1_10, i)



