class TestRun:
    def __init__(self, name, count_run):
        self.name = name  # Имя теста
        self.attempts = count_run  # Количество запусков теста (Эта строка вызывает сеттер метод def attempts)

    @property  # Декоратор для превращения метода в атрибут
    def attempts(self):
        return self.__attempts  # Верни значение атрибута(приватный)

    @attempts.setter
    def attempts(self, count_run):  # Получаем значение count_run
        if isinstance(count_run,
                      int) and count_run > 0:  # Проверка валидности переданного значения из условия: что оно больше 0 и целое число
            self.__attempts = count_run
        else:
            raise ValueError(f"Неверное значение count_run: '{count_run}'")


#
tst1 = TestRun("Логин", -1)
