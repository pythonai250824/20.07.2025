from functools import total_ordering

@total_ordering
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    @staticmethod
    def validate_book_data(book):
        #return all(k in data for k in ["title", "author", "year"])
        if book.get('title') and book.get('author') and book.get('year'):
            return True
        return False

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if value:
            self.__author = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value > 1455:  # printer invented :)
            self.__year = value

    def __str__(self):
        return f"{self.title} by {self.author} {self.year}"

    def __repr__(self):
        return f"Book('{self.__title}', '{self.__author}', {self.__year})"

    def __eq__(self, other):
        # return isinstance(other, Book) and self.title == other.title and self.author == other.author
        if isinstance(other, Book):
            if self.title == other.title and self.author == other.author:
                return True
        return False

    def __hash__(self):
        return hash((self.title, self.author)) # ('mobi dik', 'Herman Melville')

    def __gt__(self, other):
        if isinstance(other, int):
            return self.year > other
        if isinstance(other, Book):
            return self.year > other.year
        else:
            raise NotImplementedError('Book gt not support ' + type(other))
