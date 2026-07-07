class Dog:
    """Модель собаки"""
    def __init__(self,name, age):
        """Инициализация атрибутов"""
        self.name = name
        self.age = age

    def sit(self):
        """Метод собака сидит"""
        print(f"{self.name} - сейчас сидит")

    def info(self):
        """Метод вернёт атрибуты экземпляра"""
        print(self.name)
        print(self.age)

    def roll_over(self):
        """Метод собака перекатывается"""
        print(f"{self.name} - сейчас перекатывается")

class List_Dog:
    """Класс список собак"""

    def __init__(self):

        self.list_dog = []

    def add_dogs(self,dog):
        """
        Метод создаёт список собак
        [{name:"Name", age:int},{name:"Name", age:int}]
        """
        # 1. Создать локальный словарь
        dst_dog = {"name": dog.name , "age": dog.age}

        # 2. Добавляем этот новый словарь в список

        self.list_dog.append(dst_dog)

    def del_in_lisr(self,name_del):
        """Метод удаляет Собаку по Имени"""

        self.list_dog = [dst for dst in self.list_dog if dst["name"] != name_del]

        old_lst = len(self.list_dog)
        if old_lst == len(self.list_dog):
            print("Нет такой собаки")

    def info(self):
        print(self.list_dog)




my_dog = Dog("Тузик",3) # Создаём экземпляр класса, передовая емй атрибуты

my_dog2 = Dog("Вася",6)

my_dog3 = Dog("Муся",4)

my_list = List_Dog()

my_list.add_dogs(my_dog)
my_list.add_dogs(my_dog2)
my_list.add_dogs(my_dog3)

my_list.info()

my_list.del_in_lisr("авав")
my_list.info()






