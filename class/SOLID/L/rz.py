

class ConsoleReporter:
    """Метод выводы в консоль"""
    # def __init__(self):
    #     self.test = None

    @staticmethod
    def publish(test):  # принимает объект тест
        print(f"Статус теста {test.test_name}: {test.status} ")


class Test:
    def __init__(self, test_name: str, status: str):
        self.test_name = test_name  # Имя теста (публичное)
        self.status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, input_status):
        if not isinstance(input_status, str):  # Если тип строка и есть совпадение в кортеже
            raise TypeError(f"Не верный тип статус: {input_status} теста {self.test_name}")
        if input_status not in ("FAILED", "PASSED"):

            raise ValueError(f"Не допустимый статус теста {self.test_name}: {input_status}")
        else:
            self.__status = input_status

    @property
    def test_name(self):
        return self.__test_name

    @test_name.setter
    def test_name(self, new_test_name):
        self.__test_name = new_test_name  # Пока нет проверок


tets1 = Test("Авторизация", "PASSED")

try:
    tets1.status = 12
except ValueError as error:
    print(str(error))
except TypeError as  error:
    print(str(error))

ConsoleReporter.publish(tets1)
