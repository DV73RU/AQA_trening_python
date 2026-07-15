class BookStore:
    count_books = 0 # <- Количество книг (экземпляров)
    """Клас книжный магазин"""
    def __init__(self,title:str,price:float):
        """Магический метод. Конструктор экземпляра класса передаём атрибуты экземпляров"""
        self.title = title
        self.price = price
        BookStore.count_books = BookStore.count_books + 1

    def get_info(self):
        """Метод экземпляра класса вернёт информации """
        print(f"{self.title} | {self.price} Руб")

    @classmethod
    def total_books(cls):
        """Метод класса вернут количество книг (подсчёт созданных экземпляров)"""
        print(f"Всего книг {cls.count_books}")

    @classmethod
    def from_string(cls,data:str):
        """Метод класса конвертирует переданную строку в Название и цену"""
        title, price = data.split(",")
        return cls(str(title),int(price))

    @staticmethod
    def is_valid_price(price):
        return  price > 0



book1 = BookStore("Изучаем Python",1000)
book2 = BookStore("Война и Мир",1200)
book1.get_info()

BookStore.total_books()

book3 = BookStore.from_string("Строка,10")
book3.get_info()

res = BookStore.is_valid_price(-10)
print(res)