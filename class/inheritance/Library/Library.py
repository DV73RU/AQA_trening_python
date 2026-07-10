import json

class Book:
    """Класс книга"""
    def __init__(self,title,author,year,available=True):
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
        """Конвертирует  в JSON"""
        self.dst = {"title":self.title,"auther":self.author,"year":self.year,"available":self.available}
        self.json_str = json.dumps(self.dst,ensure_ascii=False, indent=4)
        return self.json_str

class Library:
    def __init__(self, file_path):
        self.books = []
        self.file_path = file_path

    def add_book(self,book):
        """Добавить книгу и записать в фал"""
        self.books.append(book)

        with open(self.file_path,"a") as f:
            f.write("")




book_1 = Book("Изучаем Python: программирование игр, визуализация данных, веб-приложения. 3-е изд","Мэтиз Эрик","2022",)
book_2 = Book("Простой Python. Современный стиль программирования. 2-е изд.","Любанович Билл",2026,available=False)
book_1.info()
book_2.info()
book_1.to_dict()

lib1 = Library("library.json")
lib1.add_book(book_1)