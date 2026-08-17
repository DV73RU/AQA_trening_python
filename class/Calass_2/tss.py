class Animal:
    def __init__(self,name):
        self.name = name

    def say(self):
        return f"{self.name} -"

class Cat(Animal):
    def say(self):
        return  "Муя"

class Dog(Animal):
    def say(self):
        return "Гаффф"



cat = Cat("Вася")
dog = Dog("Тузик")

print(cat.say())
print(dog.say())

