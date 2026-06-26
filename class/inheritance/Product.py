from datetime import datetime, date
class Product:
    """Класс продукт"""
    def __init__(self,name,price,quantity):
        self.name = name #Название
        self.price = price # Цена
        self.quantity = quantity #Количество


    def info(self):
        """Метод класса информация о продукте"""
        print(f"{self.name} | Цена: {self.price} | Количество: {self.quantity}",end="")

    def buy(self,count):
        """Метод покупки продукта"""
        if self.quantity > 0:
            self.quantity = self.quantity - count
            print(f"Куплено: {count} шт. {self.name} Осталось {self.quantity}")
        else:
            print(f"Купить нельзя! {self.name} - {self.quantity} шт.")

class Food(Product):
    """Класс еда"""
    def __init__(self,name,price,quantity,expiry_date): #Свои атрибуты
        super().__init__(name, price, quantity)  #Позаимствованные атрибуты
        self.expiry_date = expiry_date #Свой атрибут

    def info(self):
        super().info() #Берем базовый инфо

        data_object = datetime.strptime(self.expiry_date,"%Y-%m-%d").date() #Из строки в дату
        print(f" | Срок до: {data_object}") # К базовой info добавили параметр

    def is_expired(self):
        today = date.today()
        data_object = datetime.strptime(self.expiry_date, "%Y-%m-%d").date()
        if today > data_object:
            print(f"{self.name} просрочен!")
        else:
            print(f"{self.name} свежий, срок до: {data_object}")

class Electronics(Product):
    """Класс электроника"""

    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty
    def info(self):
        super().info()
        print(f" | Гарантия: {self.warranty}")
    def claim_warranty(self):
        print(f"{self.name} | Гарантия {self.warranty} мес.")


class Clothing(Product):
    def __init__(self,name,price,quantity,size):
        super().__init__(name,price,quantity)
        self.size = size


    def try_on(self):
        print(f"Примеряете {self.name} | Размер: {self.size}")

banan = Food("Бананы",10,10,"2026-11-01")
telef = Electronics("Samsung",1000,2,24)

shirt = Clothing("Рубашка", 2000, 50, "L")

banan.info()
telef.info()


telef.claim_warranty()

banan.buy(5)
banan.info()
banan.buy(5)
banan.info()
banan.buy(5)
banan.info()
banan = Food("Бананы",10,10,"2026-11-01")
banan.buy(10)

shirt.try_on()