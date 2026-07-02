class Validator:
    """Класс Вилидировния данных пользователя"""
    # def __init__(self): #Инициализация класса его атрибутов (параметров).
    # Класс не принимает значения init не нужен
    @staticmethod # Статический метод валидации email
    def is_email(email): #Метод принимает майл  Заменить на тернальный оператор
        return True if "@" in email and "." in email else False

        if "@" in email and "." in email: # Проверяем наличие символов в строке
            return True
        else:
            return False

    # Тут пишем остальные методы валидации данных пользователя

    @classmethod # Метод класса
    def validate_user(cls,name,email,phone,age,password): # Метод принимает данные пользователя.
        print(f"{email} - Вал")



user1 = Validator()
user2 = Validator()

print(user1.is_email("ее"))
user1.validate_user("Иван","ivan@in.ru",1234,23,123456)

user2.validate_user("Иван","ivanin.ru",1234,23,123456)