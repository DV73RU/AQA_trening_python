class User:
    """Класс User"""
    def __init__(self,name,age, email): # Конструктор класса User
        self.name = name # Атрибуты класса
        self.age = age
        self.email = email

    def info(self):
        """Метод информации и User"""
        print(f"{self.name} | {self.age} лет | {self.email}")


    @classmethod #Декоратор метода класса
    def from_string(cls,user_str): # Метод класса примет строку и вернёт инфу о User.
        ls = user_str.split(":")
        name = ls[0]
        age  = ls[1]
        email = ls[2]
        return cls(name,age,email)


    @classmethod
    def from_dst(cls,user_dst): # Метод класса примет словарь и вернёт инфу o User
        name = user_dst["name"]
        age = user_dst["age"]
        email = user_dst["email"]
        return cls(name,age,email)



user = User("Толя",28,"tola@mail.ru")
user.info()

user_st = User.from_string("Мария:30:maria@mail.ru")
user_st.info()

user_ds = User.from_dst({"name": "Пётр", "age": 35, "email": "petr@mail.ru"})
user_ds.info()