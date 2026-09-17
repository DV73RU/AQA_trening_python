"""
Open/Closed Principal
Программные сущности должны быть закрыты от изменения и открыты для расширения
Новые возможности лучше добавлять, а не изменять существующие

1. Запуск разных тестов — простая

Создай классы:

ApiTest;
UiTest;
DatabaseTest.

Каждый тест должен хранить название и иметь метод run(), который возвращает сообщение о запуске.

Создай функцию run_test(test), которая запускает любой переданный тест.

Добавление нового типа теста не должно требовать изменения функции run_test().
"""
from abc import ABC, abstractmethod


class BaseTest(ABC):
    """Абстрактный класс теста"""

    def __init__(self, name_test):
        # Храним имя теста
        self.name_test = name_test

    @abstractmethod  # Декоратор абстрактного метода (обязывает дочернего класса иметь этот метод)
    def run(self) -> str:
        # Метод вернёт информации о запуске теста
        pass


# Реализуем принцип O.(Open/Closed) из  S.O.L.I.D.
class ApiTest(BaseTest):
    """Класс API теста"""

    def run(self) -> str:  # Метод запускает тест
        return f"{self.name_test} - запущен..."


class UiTest(BaseTest):
    """Класс UI теста"""

    def run(self) -> str:  # Метод запуска теста UI
        return f"{self.name_test} - запущен..."


# Добавляем новый класс DataBase
# При этом функция  run_test не требует изменения
class DataBaseTest(BaseTest):
    """Класс теста Базы данных"""

    def run(self) -> str:
        return f"{self.name_test} - запущен..."


def run_test(test: object) -> str:  # Функция запускает тест, передаём тест и выполняем у него метод run
    # return f"{type(test).__name__} тест: {test.run()}"  <-  Нарушает паттерн S
    # Оставим только
    return test.run()


login_test = ApiTest("Логин")
sub_test = ApiTest("Подписка")

button_test = UiTest("Кнопка")
data_base = DataBaseTest("Проверка таблицы Users")

print(run_test(login_test))
print(run_test(sub_test))
print(run_test(button_test))
print(run_test(data_base))
