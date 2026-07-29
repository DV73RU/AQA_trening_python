class Cat:

    __slots__ = ("_name","_age")

    def __init__(self,name,age):
        self.name = name
        self.age = age


    @property # Геттре атрибута
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if value == "":
            print("Не передали атрибут")
        else:
            self._name = value


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value > 5:
            raise AttributeError("Не допустимый значение атрибута")
        else:
            self._age = value

    def __repr__(self):
        return f"Cat(name = {self.name}, age = {self.age})"

    def __str__(self):
        return f"Кот: {self.name}, возраст: {self.age}"



tom = Cat("Tom",2)
tom2 = Cat("SDS",0)
tom2.name = ("ааааааааааа")


tom2.name2 = " dfd"
print(tom2)
print(tom2.name)
print(tom2.age)