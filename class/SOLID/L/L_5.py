"""
Формально правильный тип, но неправильный смысл. Есть BaseTest.run() -> bool, где True означает: «тест действительно выполнен и успешно прошёл».
Создай UiTest, который реально выполняет проверку. Затем создай FakeTest, который ничего не проверяет и всегда возвращает True.
Объясни, почему сигнатура правильная, но LSP всё равно нарушается. После этого измени поведение FakeTest, чтобы контракт соблюдался.
"""

from abc import ABC, abstractmethod
import requests



class BasePage(ABC):

    def open_page(self)-> bool:
        pass


class BaseTest(ABC):
    @abstractmethod
    def run(self) -> bool:
        pass


class UiTest(BaseTest):
    def __init__(self,page: BasePage):
        self.page = page


    def run(self) -> bool:
        return  self.page.is_open()



class FakeTest(BaseTest):
    def run(self) -> bool:
        return True  # Структура правильная, но логика не верная, что нарушает LSP (отсутствует проверка)
