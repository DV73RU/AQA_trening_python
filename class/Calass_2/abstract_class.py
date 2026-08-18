from abc import ABC, abstractmethod


class BaseTest(ABC):
    """Базовый класс абстрактный"""

    def __init__(self, test_name):
        self.test_name = test_name  # Имя теста

    @abstractmethod  # Декоратор абстрактного метода
    def run(self):
        """Абстрактный метод класса"""
        return f"{BaseTest.__class__.__name__} тест: {self.test_name} - запущен..."


class ApiTest(BaseTest):
    """Класс тестирования API (дочерний от BaseTest)"""

    def run(self):
        """Метод о тестирования api"""
        return f"API тест: {self.test_name} - запущен... "


class UiTest(BaseTest):
    """Класс тест UI"""

    def run(self):
        """Метод UI теста"""
        return f"UI тест: {self.test_name} - запущен..."


class DataBaseTest(BaseTest):
    """Класс тест базы данных"""

    def run(self):
        """Метод тест Базы данных"""
        return f"Тест базы: {self.test_name} - запущен..."


class NoTest(BaseTest):
    """Класс без обязательного метода"""

    def no_run(self):
        return f"{self.test_name}"

api = ApiTest("Return token")
ui = UiTest("Кнопка 'Войти'")
db = DataBaseTest("Удаление из корзины")

no_test = NoTest("Имя теста")


list_tests_colections = [api, ui, db]
for test in list_tests_colections:  # Перебери все тесты в списке
    print(test.run())
