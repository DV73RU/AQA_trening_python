from abc import ABC, abstractmethod


class BaseTest(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def run(self):
        pass


class ApiTest(BaseTest):
    def run(self):
        return f"API {self.name} PASSED"


class UiTest(BaseTest):
    def run(self):
        return f"Ui {self.name} PASSED"


test1 = ApiTest("test_login")
test2 = UiTest("test_login")

print(test2.run())
print(test1.run())
