# class TestCase:
#     """Класс тест кейс"""
#     def __init__(self,name):
#         self.name = name
#         self._status = "NEW"
#
#     def get_test(self):
#         """Метод вернёт инфо о тесте"""
#         return f"Название: {self.name} | Статус: {self._status}"
#
#
# test = TestCase("Авторизация")
#
# print(test.get_test())
#
# class User:
#     """Класс пользователь"""
#     def __init__(self,login,password):
#         self.login = login
#         self.__password = password
#
#     def check_password(self,password):
#         return password == self.__password # Сравниваем пароль установленный в экземпляре с переданным паролем в метод
#
#
# user = User("inan","1234")
# print(user.check_password("1"))
# print(user.check_password("1234"))
# # print("_____________________")

# class TestCase:
#     """Класс тест кейс"""
#     def __init__(self,name):
#         self.name = name # <- Имя теста (передаём при создании  экземпляра)
#         self.__status = "NEW" # <- Статус теста
#
#     @property
#     def status(self): # < - читаем как обычный атрибут
#         return self.__status
#
#
#     def pass_test(self):
#         """Метод устанавливает статус теста PASSED"""
#         self.__status = "PASSED"
#
#     def fail_test(self):
#         """Метод устанавливает статус теста FAILED"""
#         self.__status = "FAILED"
#
#
# test = TestCase("Логин")
# print(test.status)
# test.fail_test()
# print(test.status)
# test.pass_test()
# print(test.status)

# test.status = "радном сататус" # < - не получится напрямую установить статус (AttributeError: property 'status' of 'TestCase' object has no setter)


print("____")

"""
Средняя 4. Валидация времени выполнения

Создай класс TestResult.

Требования:

Объект получает название теста и время его выполнения.
Время выполнения хранится во внутреннем атрибуте.
Для чтения и изменения времени используй свойство duration.
Время должно быть числом больше или равным нулю.
При попытке установить некорректное значение должно возникать исключение ValueError.
Проверка должна выполняться как при создании объекта, так и при последующем изменении времени.
"""

class TestResult:
    def __init__(self,name,time_run):
        self.name = name # <- Имя теста, передаем при создании объекта
        self.set_time_run(time_run)
        # Ограничим значение time_run при создании объекта (экземпляра)
        # if not isinstance(time_run, (int,float)): # Если передали не инт и флоат
        #     raise TypeError(f"Не доступное значение: '{time_run}', передали не 'int' или 'float'")
        # elif time_run < 0: # Если передали меньше 0
        #     raise ValueError(f"Не доступное значение: '{time_run}', не должно быть меньше 0") # Выбросим ошибку
        # else:
        #     self.__time_run = time_run # Иначе присвоим значение атрибута экземпляра значение параметра класса






    def get_time_run(self):
        """Метод для получения времени выполнения теста"""
        return self.__time_run # Вернём время выполнения теста

    def set_time_run(self,time_run): # <- передадим значение времени в метод
        """Метод для установки времени выполнения теста"""

        # Ограничим значение time_run при изменении атрибута объекта (экземпляра)
        if not isinstance(time_run, (int,float)): # Если передали не инт и флоат
            raise TypeError(f"Не доступное значение: '{time_run}', передали не 'int' или 'float'") # Выбросим ошибку
        elif time_run < 0: # Если передали меньше 0
            raise ValueError(f"Не доступное значение: '{time_run}', не должно быть меньше 0") # Выбросим ошибку
        else:
            self.__time_run = time_run # Иначе присвоим значение атрибута экземпляра значение параметра класса



test = TestResult("Логин",10)
try:
    test.set_time_run(-10)
except ValueError as err:
    print(f"Ошибка: {err}")

print(test.get_time_run())
print(test.__dict__)





