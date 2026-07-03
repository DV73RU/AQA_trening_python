

class Validator:

    """Класс Вилидировния данных пользователя"""
    # def __init__(self): #Инициализация класса его атрибутов (параметров).
    # Класс не принимает значения init не нужен
    @staticmethod # Статический метод валидации email
    def is_email(email:str): #Метод принимает майл  Заменить на тернальный оператор
        return True if "@" in email and "." in email else False

    @staticmethod
    def is_phone(phone):
        return True if phone.isdigit() and len(phone) == 11  else False

    @staticmethod
    def is_age(age):
        return  True if 120 > age > 0 else False

    @staticmethod
    def is_password(password):
        return True if len(password) >= 8 else False


    # Тут пишем остальные методы валидации данных пользователя

    @classmethod # Метод класса
    # count = 0
    def validate_user(cls,name,email,phone,age,password): # Метод принимает данные пользователя.
        count = 0
        if cls.is_email(email):
            print(f"email:    ✓")
            count += 1
        else:
            print(f"email:    ✗")

        if cls.is_phone(phone):
            print(f"phone:    ✓")
            count += 1
        else:
            print(f"phone:    ✗")

        if cls.is_age(age):
            print(f"age:    ✓")
            count += 1
        else:
            print(f"age:    ✗")

        if cls.is_password(password):
            print(f"password:    ✓")
            count += 1
        else:
            print(f"password:    ✗")

        if count == 4:
            print(f"Пользователь: {name} - Valid" )
        else:
            print(f"Пользователь No Valid")






user1 = Validator()
user2 = Validator()

print(user1.is_email("ее"))
user1.validate_user("Иван","ivan@in.ru","12345678910",23,"12345678")

user2.validate_user("Иван","ivanin.ru","1234",23,"123456")