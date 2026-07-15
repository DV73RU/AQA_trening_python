

class User:
    """Класс пользователи"""
    def __init__(self,username):
        self.username = username
        self.password = None

    @staticmethod
    # """Статический метод проверки что длинна пароля больше 6 и содержит цифру"""
    def is_password_strong(password:str):
        return len(password) > 6 and any(char.isdigit() for char in password)

    def set_password(self,password):
        if self.is_password_strong(password):
            self.password = password
            print(f"Пароль установлен")
        else:
            print(f"Пассфорд не валтидный")

    def info_user(self):
        print(f"{self.username} - {self.password}")


user1 =User("user123")
user1.set_password("1234")
user1.info_user()
user1.set_password("qwerty1")
user1.info_user()