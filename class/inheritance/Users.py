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




class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        # for priveleg in self.privileges:
        #     print(priveleg)

        print(f"Привилегии : {self.privileges}")

class Admin(Users):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()




user1 = Users("Анатолий","Иванович",23)
admin1 = Admin("Василий","Петрович",49)

admin1.privileges.show_privileges()
admin1.describe_use()


# user1.describe_use()
# user1.greet_user()
# print(user1.login_attempts)
#
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)