class Animal:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def get_info(self):
        return f"Имя: {self.name} | Возраст: {self.age}"


class Cat(Animal):
    def __init__(self,breed,age,name):
        super().__init__(age,name)
        self.breed = breed

    @property
    def cat_name(self):
        return self.name

    @cat_name.setter
    def cat_name(self,new_name: str):
        if not new_name.strip():
            print("Имя не может быть пустым")
        else:
            self.name = new_name

    def get_info(self):
        return f"Кот: {self.name} | Порода: {self.breed} | Возраст: {self.age}"

tom = Cat("Перс",2,"Tom")
print(tom.get_info())

tom.cat_name = "ваа"
print(tom.get_info())
print(tom.name)