import datetime
from datetime import datetime, date
class Product:
    """Класс продукт"""
    def __init__(self,name,price,quantity):
        self.name = name #Название
        self.price = price # Цена
        self.quantity = quantity #Количество


    def info(self):
        """Метод класса информация о продукте"""


        print(f"{self.name} | Цена: {self.price} | Количество {self.quantity}")


class Food(Product):
    """Класс еда"""
    def __init__(self,name,price,quantity,expiry_date): #Свои атрибуты
        super().__init__(name, price, quantity)  #Позаимствованные атрибуты
        self.expiry_date = expiry_date #Свой атрибут

    def info(self):
        data_object = datetime.strptime(self.expiry_date,"%Y-%m-%d").date() #Из строки в дату

        print(f"{self.name} | Цена: {self.price} | Количество {self.quantity} | Срок до: {data_object}" )



banan = Food("Бананы",100,10,"2026-11-01")
banan.info()