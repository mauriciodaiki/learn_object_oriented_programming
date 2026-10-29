class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        keep_books: list[Book] = []
        for i in self.books:
            if i.title in book.title and i.author in book.author:
                pass
            else:
                keep_books.append(i)
        self.books = keep_books
            

    def search_books(self, search_string: str) -> list[Book]:
        search_books:list[Book] = []
        for i in self.books:
            if search_string.lower() in i.title.lower() or search_string.lower() in i.author.lower():
                search_books.append(i)
        return search_books
