
class Product:
    """Класс продукты"""
    def __init__(self,name,price,quantity): # < - Атрибуты класса:
        self.name = name # Название
        self.price = price # Цена
        self.quantity = quantity # Количество

    def info(self): # <- Метод экземпляра класса.
        """Метод вернет все товары"""
        print(f"{self.name},{self.price},{self.quantity}")

class  Card:
    """Класс корзина"""
    def __init__(self):
        self.items = []

    def add_product(self,product,n ):
        """Метод добавления в корзину"""
        self.items.append({"name":product.name,"count": n, "price":product.price})

    def info(self):
        """Метод класса информация о корзине"""
        res = 0
        for dst in self.items:
            name = dst["name"]
            count = dst["count"]
            price = dst["price"]
            summa = count * price
            print(f"{name} x{count} - {summa}")
            res = res + summa
        print(f"Итого: {res}")

    def remove(self,name):
        """Метод удаляет товар из корзины по имени товара"""
        found = False
        for dst in  self.items:
            # print(dst)
            if dst["name"] == name:
                found = True
                self.items.remove(dst)
                break #<- Нашли удалили и вышли
        if not found:
            print("Нет такого отвара")

    def total(self):
        """Метод вернёт сумму заказа """

        res = 0
        for dst in self.items:
            prise = dst["price"]
            count = dst["count"]
            summa = prise * count
            res = res + summa
        return res

class Order:
    def __init__(self,card):
        self.card = card
        self.status = "Новый"

    def info(self):
        """Метод вернёт статус """
        print(f"Статус: {self.status} | Сумма : {self.card.total()}")


    def confirm(self):
        """Метод подтверждает заказ"""
        self.status = "Подтверждён"

    def cansel(self):
        """Метод отменяет заказ"""
        self.status = "Отменён"


prod1 = Product("Телефон",100,2)
prod2 = Product("Чехол",1.5,5)
prod3 = Product("Телевизор",300,3)
# prod1.info()

card = Card()
card.add_product(prod1,1)
card.add_product(prod2,2)
card.info()
card.remove("Чехол")
card.info()
card.remove("Нечто")

order = Order(card)
order.info()
order.confirm()
order.info()
order.cansel()
order.info()

