class Peson:
    def __init__(self,age):
        self.age = age


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value): # Установка атрибута через сеттер
        if value < 0:
            print("Установили не правильное значение атрибута age")
            self._age = "Не установлен"
        else:
            self._age = value # Устанавливаем значение атрибута

    def info(self):
        return self.age




p = Peson(-12)
