class Library:
    """Класс библиотека"""
    def __init__(self):
        """Метод инициализации класса"""
        self.books = [] #Атрибут класса


    def add_book(self,title,author,year):
        """Метод добавляет книгу в библиотеку"""
        i = len(self.books) + 1
        dst_book = {"id":i,"title":title,"author":author,"year":year}
        self.books.append(dst_book)

    def info(self):
        """Метод информации о всех книгах"""
        for dst in self.books:
            title = dst['title']
            author = dst['author']
            year = dst['year']
            id = dst["id"]
            print(f"# {id}. {title} | {author} | {year}")

    def find_by_author(self,author):
        """Метод поиска по автору"""
        for dst in self.books:
            if author == dst["author"]:
                print(f"{dst['title']} | {dst['year']}")

    def remove_book(self,title):
        """Метод удаляет книгу по названию"""
        self.books = [book for book in self.books if book["title"] != title]


my_library = Library()
my_library.add_book("Война и Мир","Толстой",1966)
my_library.add_book("Мастер и Маргарита","Булгаков",1967)
my_library.add_book("Собачье сердце","Булгаков",1925)


my_library.info()

my_library.find_by_author("Булгаков")
my_library.remove_book("Война и Мир")
my_library.info()