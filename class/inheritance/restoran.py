class Restaurant:
    """Класс ресторан"""
    def __init__(self,res_name,cuisine_type):
        self.res_name = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 #<- Количество обслуженных посетителей


    def describe_restaurant(self):
        """Метод выводит два атрибута"""
        print(f"{self.res_name} | Кухня: {self.cuisine_type}")
        print(f"Всего обслужено посетителей: {self.number_served}")

    def open_restaurant(self):
        print(f"Ресторан {self.res_name} - Открыт")

    def set_number_served(self,count):
        if self.number_served <= count:
            self.number_served = self.number_served + count
        else:
            print("Отрицательное число не доступно")

class IceCreamStand(Restaurant):
    """Класс киоск с мороженым"""
    def __init__(self,res_name,cuisine_type):
        super().__init__(res_name,cuisine_type)
        self.flavors = ["Яблочное"]


    def get_flavors(self):

        for ls in self.flavors:
            print(ls)


rest = Restaurant("У Палыча","Кавказская")
rest1 = Restaurant("Три корочки","Русская")
rest2 = Restaurant("Cи-ляо", "Китайская")

ice1 = IceCreamStand("Сахар и Лёд","Мороженое")


rest.describe_restaurant()
# rest.open_restaurant()
rest1.describe_restaurant()
rest2.describe_restaurant()


rest3 = Restaurant("Шаурмичка","Восточная")
print(rest3.number_served)
rest3.number_served = 10
print(rest3.number_served)

# rest3.set_number_served(10)
rest3.describe_restaurant()
rest3.set_number_served(23)
rest3.describe_restaurant()

ice1.describe_restaurant()
ice1.get_flavors()