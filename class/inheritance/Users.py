class Users:
    """Класс пользователи"""

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_use(self):
        print(f"Имя: {self.first_name}")
        print(f"Отчество: {self.last_name}")
        print(f"Года: {self.age}")

    def greet_user(self):
        print(f"Приветствую вас {self.first_name} у нас")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = Users("Анатолий","Иванович",23)
user1.describe_use()
user1.greet_user()
print(user1.login_attempts)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)