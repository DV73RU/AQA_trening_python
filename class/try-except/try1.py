

class InvalidStatusError(Exception):
    pass

class TestExecutionError(Exception):
    pass


class TestResult:
    """Класс результат теста"""
    status_list = ("PASSED", "FAILED")

    def __init__(self, test_name, status):
        self.test_name = test_name
        self.validate_status(status)
        self.status = status

    @classmethod
    def validate_status(cls, status):
        """Метод валидации статуса"""
        if status not in cls.status_list:
            raise InvalidStatusError("Не допустимый статус")




try:
    res = TestResult("login_test", "BROKEN")
    print(res.__dict__)
except ValueError as error:
    raise TestExecutionError("Ошибка выполнения API-теста") from error
