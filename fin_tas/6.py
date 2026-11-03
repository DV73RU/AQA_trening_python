from abc import ABC, abstractmethod


class BaseTest(ABC):
    def __init__(self, name):
        self.name = name
        self.status = None

    @abstractmethod
    def run(self):
        pass


class ApiTest(BaseTest):
    def __init__(self, name, endpoint):
        super().__init__(name)
        self.endpoint = endpoint

    def run(self):
        return f"{self.name} PASSED {self.endpoint}"


class UiTest(BaseTest):
    def __init__(self, name, browser):
        super().__init__(name)
        self.browser = browser

    def run(self):
        return f"{self.name}: UI {self.browser} PASSED"


class ConnectDataBase(ABC):

    def __init__(self, connected: bool):
        self.connected = connected

    @abstractmethod
    def is_connected(self):
        pass


class FakeConnection(ConnectDataBase):

    def is_connected(self):
        return self.connected


class DatabaseTest(BaseTest):
    def __init__(self, name: str, bd: object):
        super().__init__(name)
        self.bd = bd  # Объект подключения к БД

    def run(self):
        if self.bd.is_connected():
            return "PASSED"
        else:
            return "FAILED"


class BrokenTest(BaseTest):
    pass


class TestRunner:
    def __init__(self, tests: list[BaseTest]):
        self.tests = tests.copy()  # Экземпляр принимает список тестов
        self.list_result = []
        """Экземпляр принимает список объектов тестов"""

    def run_all(self):
        # self.list_result.clear()
        self.list_result = []

        for test in self.tests:
            res = test.run()
            self.list_result.append(res)

    def get_results(self):
        new_list_result = self.list_result.copy()
        return new_list_result

    def add_test(self, test: BaseTest):  # Принимает объект экземпляр класса BaseTest
        self.tests.append(test)

    def remove_test(self, name: str):  # Принимает имя из экземпляра класса BaseTest
        for test in self.tests:
            if test.name == name:
                self.tests.remove(test)
                return True

        return False


fake_con1 = FakeConnection(False)
fake_con2 = FakeConnection(True)

test_bd = DatabaseTest("Name BD", fake_con1)
test_bd = DatabaseTest("Name BD2", fake_con2)

test_bd.run()
test_bd.run()

assert test_bd.run() == "FAILED"
assert test_bd.run() == "PASSED"

tests = [
    ApiTest("test_login", "/api/login"),
    ApiTest("test_logout", "/api/logout"),
    UiTest("test_profile", "Chrome")
]

runner = TestRunner(tests)

assert runner.remove_test("test_logout") == True
assert runner.remove_test("test_unknown") == False
assert len(runner.tests) == 2, \
    "Количество тестов не равно 2"  # Количество тестов в списке

assert not any(test.name == "test_logout" for test in runner.tests), \
    "Тест 'test_logout' всё ещё присутствует в тест-раннере"
