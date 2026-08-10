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
        self.duration = time_run # <- Свойства для изменения и чтения времени выполнения теста

    @property #<- Метод вернёт время теста
    def duration(self):
        return self.__duration # <- Верни атрибут, но он приватный


    @duration.setter # <- Установщик времени выполнения теста
    def duration(self,time_run):
        if isinstance(time_run, (int,float)): #<- Если int
           self.__duration = time_run # Устанавливаем переданное значение (приватное) экземпляра
        else:
            raise ValueError("Не число") # <- Иначе выброси ошибку
        if time_run > 0:
            self.__duration = time_run  # Устанавливаем переданное значение (приватное) экземпляр
        else:
            raise  ValueError("Не положительное")




test = TestResult("Логин",10)
# test.duration = ""
# test.duration = -1

print(test.duration)

# test2 = TestResult("EXIT",-10)
test3 = TestResult("нОВ","DSDSD")



