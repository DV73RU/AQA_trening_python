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
class Users:
    """Класс пользователи"""

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_use(self):
        print(f"Имя: {self.first_name}")
        print(f"Отчество: {self.last_name}")
        print(f"Года: {self.age}")

    def greet_user(self):
        print(f"Приветствую вас {self.first_name} у нас")



rest = Restaurant("У Палыча","Кавказская")
rest1 = Restaurant("Три корочки","Русская")
rest2 = Restaurant("Cи-ляо", "Китайская")

user1= Users("Сергей","Иванов",23)
user2 =Users("Александр","Петров",20)
user3 = Users("Си","Дзен",44)

user1.describe_use()
user2.describe_use()
user3.describe_use()

user2.greet_user()
user3.greet_user()
#
# print(rest.res_name)
# print(rest.cuisine_type)

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