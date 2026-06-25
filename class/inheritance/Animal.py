class Animal:
    """Класс животные"""
    def __init__(self,name,age):
        self.name = name # Атрибуты класса животные
        self.age = age

    def info(self):
        """Метод класса Животное информация о животном"""
        print(f"Имя: {self.name} | Возраст: {self.age} ")

    def eat(self):
        """Метод класа Животное - ест"""
        print(f"{self.name} - Ест")


class Dog(Animal):
    """Класс собака (Наследник класса животные) """
    def __init__(self,name,age,breed): # <- Инициализация класса с атрибутами.
        super().__init__(name,age) # <- Возьмём атрибуты родительского класа Животные
        self.breed = breed # <- Создаём собственный атрибут класса Dog

    def info(self):
        print(f"Имя: {self.name} | Возраст: {self.age} | порода: {self.breed}") # Переопределяем метод каласса анимал для класса собака


    def bark(self):
        """Метод лаять"""
        print(f"{self.name} говорит: Гав!")

class Cat(Animal):
    """Класс кот (Наследник класса Животные)"""
    def __init__(self,name,age,color): # <- Коструктор класа с атрибутами экхемпляров.
        super().__init__(name,age) #<- Забираем атрибуты у родительского класса Животные
        self.color = color # <- Создаём атрибут класса кот.

    def info(self):
        print(f"Имя: {self.name} | Возраст: {self.age} | порода: {self.color}") # Переопределяем метод каласса анимал для класса собака



    def meow(self):
        """Метод котя мяукать"""
        print(f"{self.name} говорит: Мяу!")

class Bird(Animal):
    """Клас Птица (Наследник класса животное)"""
    def __init__(self,name,age,can_fly): # Конструктор клсаса с атрибутами
        super().__init__(name,age) # Забираем атрибуты у родителького класса
        self.can_fly = can_fly # Свой атрибут для птички

    def info(self):
        print(f"Имя: {self.name} | Возраст: {self.age} ") # Переопределяем метод каласса анимал для класса собака


    def fly(self):
        """Метод летать для класса Птица"""
        print(f"{self.name} летит" if self.can_fly else f"{self.name} не летит")

dog = Dog("Рекс",4,"Бульдог")
cat = Cat("Барскик",2,"Рыжий")
bird = Bird("Кеша",1,True)

bird2 = Bird("Киви",2,False)

dog.info()
cat.info()
bird.info()

dog.eat()
cat.eat()
bird.eat()

dog.bark()
cat.meow()
bird.fly()

bird2.fly()