class Book:
    def __init__(self, name: str, auther: str):
        self.__name = name
        self.__auther = auther

    @property
    def name(self):
        return self.__name

    @property
    def auther(self):
        return self.__auther

    def __str__(self):
        return f"{self.__name} - {self.__auther}"

class EBook(Book):

    def __init__(self, name, auther, file_size: int):
        super().__init__(name, auther)
        self.file_size = file_size

    def __str__(self):
        return f"{self.name} - {self.auther} (размер файла: {self.file_size} МБ)"


class Library:
    def __init__(self):
        self.__list_book = []

    def add_book(self, book: object):
        self.__list_book.append(book)

    def show_book(self):
        for book in self.__list_book:
            print(book)


b1 = Book("Война и Мир", "Леф Толстой")
eb1 = EBook("Война и Мир", "Леф Толстой", 4)
b2 = Book("Питон", "Автор")
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(eb1)

lib.show_book()

