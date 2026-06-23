

class Card:
    """Класс корзина покупок"""
    def __init__(self): #Иницилизация класса и его атрибутов
        self.items = [] #Список покупок, внутри словар name: , price:

    def add_item(self,name,price):
        """Метод добавления в корзину товара"""
        dct = {"name":name,"price":price}
        self.items.append(dct)
        # self.items.append(self.total())/\

    def total(self):
        res = 0
        for i in self.items:
            pr = i["price"]
            res = res + pr
        return res


    def info(self):
        """Метод возвращяет товар -  цену и сумму заказа"""
        for key,val in enumerate(self.items,start=1):
            name = val["name"]
            price = val["price"]
            # total = self.items[-1]
            print(f"# {name} - {price} руб.")
        print(f"# Итого: {self.total()}")


    def remove_items(self,rem_name):
        """Метод удаляет товар из корзины"""
        # self.rem_name = rem_name
        self.items = [name for name in self.items if name["name"] != rem_name]




cr = Card()
cr.add_item("Хлеб",20)
cr.add_item("Кофе",1)
cr.add_item("Молоко",10)
# cr.info()
cr.remove_items("Кофе")
cr.info()

# cr.remove_items("Кофе")
# cr.info()