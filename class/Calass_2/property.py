class TestRun:
    def __init__(self,name,attempts):
        self.name = name # Имя теста
        self.__attempts = attempts # Количество запусков(приватный)

    @property # Декоратор для того что бы метод был атрибутом
    def attempts(self):
        return self.__attempts # Верни значение attempts


test = TestRun("Логин",2)
print(test.attempts)
test.attempts = 23 # Не установить на прямую так как приватный
print(test.attempts)