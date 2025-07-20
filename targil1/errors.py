from user import User
from book import Book

class BookNotFoundError(Exception):
    def __init__(self, user: User, book: Book):
        self.user = user
        self.book = book
        super().__init__(f"user {user.name} tried to return a non-existing book {book.title}")

class BookNotBorrowedError(Exception):
    pass