class Dog:
    """Класс собака"""
    def __init__(self,name,age,bread):
        """Атрибуты обьекта собока"""
        self.name = name #Имя
        self.age = age # Возрост
        self.bread = bread # Порода

    """Методы класса собака"""
    def bark(self):
        """Метод гавкнуть и сказать своё имя"""
        print(f"Гав!Меня зовут {self.name} ")

    def info_dog(self):
        """Метод сказать информацию о собаку"""
        print(f"Я собка по имение {self.name}, мне {self.age} лет, породой {self.bread}")

dog1 = Dog("Рекс",2,"Бульдог")
dog2 = Dog("Маркиз",3,"Пудиль")

dog1.bark()
dog2.info_dog()