class User:
    """Класс пользователь"""
    def __init__(self,username,password):
        # Принимает параметры
        self._username = username # Имя пользователя (приватный)
        self.password = password # Пароль

    @property
    def username(self): # Геттр дял имени пользователя
        return self._username

    @property
    def password(self): # Геттр для пароля
        return f"Пароль: Не доступно для чтения"

    @password.setter # Сеттер для пароля
    def password(self,value: str):
        if len(value) < 8:
            print(f"Пароль короткий")
            self._password = None # Если не валидный передали то пароль затерли
            return
        if not any(i.isdigit() for i in value):
            print("Пароль должен содержать цифру")
            self._password = None # Если не валидный передали то затерли пароль
            return
        else:
            self._password = value
            print(f"Пароль установлен") # Если валидный установаили пароль


    def check_password(self,pwd):
        return self._password  == pwd # Если передали верный пароль то труе


user = User("Толя","asdfghjk1")
# print(user.password)
print(user.username)
# user.password = "1asderererer"

# user.password = "12"
# user.password = "a1"
# user.check_password("1asderererer")

print(user.check_password("asdfghjk1"))
print(user.check_password("dsds"))
user.password = "dfdf"
print(user.password)