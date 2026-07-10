import json

class Book:
    """Класс книга"""
    def __init__(self, title, author, year, available=True):
        # self.dst = None
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def info(self):
        """Метод информация о книге"""
        print(f"{self.author}")
        print(f"{self.title}")
        print(f"{self.year}")
        if not self.available:
            print(f"❌ Нет в наличии")
        else:
            print("✅ В наличи")


    def to_dict(self):
        """Вернёт словарь"""
        self.dst = {"title":self.title,"author":self.author,"year":self.year,"available":self.available}
        # self.json_str = json.dumps(self.dst,ensure_ascii=False, indent=4)
        return self.dst

class Library:
    def __init__(self, file_path):
        self.books = []
        self.file_path = file_path

    def save(self):
        """Сохраняем все книги в файл"""
        with open(self.file_path,"w",encoding="utf-8") as f:
             json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self,book):
        """Добавить книгу и записать в фал"""
        self.books.append(book) # < - добавили книгу в список
        self.save() #<- записали в файл вызвав метод save

    def load(self):
        with open(self.file_path,"r",encoding="utf-8") as f:
            data = json.load(f)

        self.books = [Book(**d) for d in data]

    def info(self):
        """Метод выводит все книги"""
        for b in self.books:
            status = "✅" if b.available else "❌"
            print(f"{status}{b.title} | {b.author} | {b.year}")

    def find_by_author(self,author):
        found = False
        for b in self.books:
            if b.author == author:
                status = "✅" if b.available else "❌"
                print(f"{status}  {b.title} | {b.author} | {b.year}")
                found = True
        if not found:
            print(f"Книги автора '{author}' не найдены")

    def take_book(self,title):
        """Меняем статус книги - Взять книгу"""
        # Как поменять статус если книга уже на руках?
        found = False
        for b in self.books:
            if b.title == title:
                if not b.available:
                    print(f"{b.title} уже взята")#< - Если нашли такую книгу
                else:
                    b.available = False
                    found = True
                    self.save() # < - Сохраняем в файл
        if not found:
            print(f"Нет такой книги: {title}")

    def return_book(self,title):
        """Меняем статус книги - Вернуть книгу"""
        found = False
        for b in self.books:
            if b.title == title: #< - Если нашли такую книгу
                b.available = True
                found = True
                self.save() # < - Сохраняем в файл
        if not found:
            print(f"Нет такой книги: {title}")


book_1 = Book("Изучаем Python: программирование игр, визуализация данных, веб-приложения. 3-е изд","Мэтиз Эрик","2022",)
book_2 = Book("Простой Python. Современный стиль программирования. 2-е изд.","Любанович Билл",2026,available=False)
# book_1.info()
# book_2.info()
# print(book_1.to_dict())
# print(book_2.to_dict())

lib1 = Library("library.json")
lib1.add_book(book_1)
lib1.add_book(book_2)
# lib1.info()
lib1.find_by_author("Любанович Билл")
lib1.take_book("Изучаем Python: программирование игр, визуализация данных, веб-приложения. 3-е изд")
lib1.take_book("ddfdf")
lib1.take_book("Простой Python. Современный стиль программирования. 2-е изд.")
lib1.info()
lib1.return_book("Простой Python. Современный стиль программирования. 2-е изд.")
lib1.return_book("Изучаем Python: программирование игр, визуализация данных, веб-приложения. 3-е изд")
lib1.info()