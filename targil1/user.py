from book import Book
from library import Library

class User:
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.__user_id = user_id  # read-only
        self.borrowed = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value:
            self.__name = value

    def borrow_books(self, *books: Book, lib: Library):
        from targil1.errors import BookNotFoundError
        for book in books:
            if lib.book_exist(book):
                if lib.is_available(book):
                    # lib.borrow_book(user_id, book)  # good
                    # better
                    lib.borrow_book(self, book)
                    self.borrowed.append(book.title)
                else:
                    print(f"no more copies for book '{book.title}'.")
            else:
                # print(f"Book '{book.title}' is not available.")
                raise BookNotFoundError(self, book)

    def return_book(self, *books: Book, lib: Library):
        from targil1.errors import BookNotBorrowedError
        for book in books:
            if book in lib.did_i_borrow(self, book):
                lib.return_book(self, book)
                self.borrowed.remove(book.title)
            else:
                # print(f"Book '{book.title}' is not borrowed.")
                raise BookNotBorrowedError(f"Book '{book.title}' is not borrowed.")

    def __str__(self):
        return f"{self.user_id} {self.name} borrowed: " + ", ".join(self.borrowed)

        '''
            ", ".join(self.borrowed) does this:
            result = ''
            for title in self.borrowed:
                result += title + ','            
        '''
