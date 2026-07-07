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


my_dog = Dog("Вася",7)
my_dog2 = Dog("Бим",6)

print(f"Мои собаки {my_dog.name}, {my_dog2.name} им {my_dog.age} и {my_dog2.age} лет соотвествеено")
