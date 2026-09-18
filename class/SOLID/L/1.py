from abc import ABC, abstractmethod


class BaseTest(ABC):

    @abstractmethod
    def run(self):
        print("Тест запущен...")


class ApiTest(BaseTest):

    def run(self):
        print("Тест API запущен...")


class UiTest(BaseTest):
    def run(self):
        print("Тест UI запущен...")


class DbTest(BaseTest):
    def run(self): #Наследник обязан выполнять контракт родителя
        print("Тест DB запущен...")


class RunerTest:

    def __init__(self):
        self.test = None

    def execute(self, test):
        res = test.run()
        return res


api_test = ApiTest()
ui_test = UiTest()
db_test = DbTest()

list_test = [api_test, ui_test, db_test]

runer = RunerTest()
runer.execute(api_test)
