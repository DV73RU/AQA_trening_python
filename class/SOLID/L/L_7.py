"""
Мини-архитектура TestRunner. Создай абстрактный BaseTest с run() -> TestResult. Сделай ApiTest, UiTest и DatabaseTest.
Затем создай TestRunner, который получает список тестов и запускает каждый только через общий run().
Условия: нельзя использовать type() и isinstance(); каждый тест должен возвращать TestResult; один из тестов не должен требовать дополнительных аргументов при run();
один из тестов не должен возвращать None; один из тестов не должен неожиданно выбрасывать исключение вместо результата.
Твоя задача — спроектировать классы так, чтобы любой наследник можно было подставить вместо BaseTest.
"""

from abc import ABC, abstractmethod


class TestResult:
    """Храним результаты"""

    def __init__(self, name, status, text_error=None):
        self.name = name
        self.status = status
        self.text_error = text_error


class BaseTest(ABC):
    @abstractmethod
    def run(self) -> TestResult:
        pass


class ApiTest(BaseTest):
    def __init__(self, response):
        self.response = response

    def run(self) -> TestResult:
        if self.response == 200:
            return TestResult("api_test", "PASSED")
        else:
            return TestResult("api_test", "FAILED")


class BasePage(ABC):

    @abstractmethod
    def is_open(self):
        pass


class LoginPage(BasePage):
    def __init__(self, url):
        self.url = url

    def is_open(self):
        return "login" in self.url



class UiTest(BaseTest):
    def __init__(self, page: BasePage):
        self.page = page

    def run(self) -> TestResult:
        if  self.page.is_open():
            return TestResult("ui_test", "PASSED")
        else:
            return TestResult("ui_test", "FAILED")





class DatabaseTest(BaseTest):

    def __init__(self, connection):
        self.connection = connection

    def run(self) -> TestResult:
        try:
            if self.connection == True:
                return TestResult("db_test", "PASSED")
            else:
                return TestResult("db_test", "FAILED")
        except Exception as err:
            return TestResult("db_test", "FAILED", str(err))


class TestRuner:

    def __init__(self, tests: list):
        self.tests = tests

    def execute(self):
        ls = []
        for test in self.tests:
            res = test.run()
            ls.append(res)
        return ls


api_test = ApiTest(200)
page_login = LoginPage("login/index.http")
ui_test = UiTest(page_login)
db_test = DatabaseTest(True)

list_test = [api_test, ui_test, db_test]

run1 = TestRuner(list_test)
print(run1.execute())
