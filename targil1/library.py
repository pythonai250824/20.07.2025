import json
from user import User
from collections import defaultdict

class Library:
    def __init__(self):
        self.books = dict()  # Book -> quantity
        # { Book('80 days'): 1,  Book('Python'): 3 }
        self.users = set()

    def add_book(self, book: "Book"):
        # defaultdict(int)
        # self.books[book] += 1
        if self.books.get(book):
            self.books[book] = self.books[book] + 1
        else:
            self.books[book] = 1

        # shortcut -- 1 line
        # self.books[book] = self.books.get(book, 0) + 1

    def return_book(self, user: User, book: "Book"):
        from targil1.errors import BookNotExistInLibraryError

        if self.books.get(book):
            self.books[book] = self.books[book] + 1
        else:
            raise BookNotExistInLibraryError(f"book {book.title} not exist in lib")

    def add_user(self, user: User):
        self.users.add(user)

    def book_exist(self, book: "Book"):
        if self.books.get(book) is None:
            return False
        return True

    def is_available(self, book: "Book"):
        copies = self.books.get(book, 0)
        return copies > 0

    def borrow_book(self, user: User, book: "Book") -> bool:
        from targil1.errors import UserNotRegisteredError
        from targil1.errors import BookNotExistInLibraryError

        if user not in self.users:
            raise UserNotRegisteredError(f"user {user.name} is not registered")

        if book not in self.books:
            raise BookNotExistInLibraryError(f"book {book.title} not exist in lib")

        copies = self.books[book]
        if copies == 0:
            return False

        self.books[book] = copies - 1
        return True


    '''
        @classmethod to create a library from a file
        @staticmethod to validate book data
        __contains__ to check if book is in library
        __getitem__ to get a book by title
        Custom __iter__ to loop over books
    '''

    @classmethod
    def from_file(cls, filename):
        lib = cls()
        with open(filename, 'r') as f:
            data = json.load(f)  # [{ 'title': '80 days', 'year': 1980},{ 'title': '80 days', 'year': 1980}]
        for book in data:
            if Book.validate_book_data(book):
                b = Book(book["title"], book["author"], book["year"])
                # i.e. b = Book('80 days', 'Jul Vern', 1980)
                lib.add_book(b)
        return lib

    def __contains__(self, book):
        return book in self.books

    def __getitem__(self, book):
        for book in self.books:
            return self.books[book]  # copies
        raise KeyError(f"Book '{book}' not found")

    def __iter__(self):
        # just return the iterator of the dict
        return iter(self.books)
