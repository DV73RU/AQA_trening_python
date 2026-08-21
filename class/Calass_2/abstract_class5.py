"""
6. Подготовка тестового окружения

Создай абстрактный класс BaseEnvironment с абстрактными методами:

setup()
teardown()

Создай окружения:

WebEnvironment — запускает и закрывает браузер;
ApiEnvironment — создаёт и закрывает API-сессию;
DatabaseEnvironment — подключается и отключается от базы данных.

Напиши функцию execute_test(), которая принимает объект окружения и название теста.

Функция должна:

Подготовить окружение.
Сообщить о запуске теста.
Завершить работу окружения.
Вернуть список выполненных действий.

"""
import time
from abc import ABC, abstractmethod


class BaseEnvironment(ABC):
    @abstractmethod
    def setup(self):
        return f"Установлены настройки окружения"

    @abstractmethod
    def teardown(self):
        return f"Возвращение в настроек в окружение в исходное состояние"


class WebEnvironment(BaseEnvironment):
    """Класс окружение для Веб браузера"""

    def setup(self):
        return "Запуск браузера..."

    def teardown(self):
        return f"Закрытие браузера...."


class ApiEnvironment(BaseEnvironment):
    """Клас окружение для API"""

    def setup(self):
        return "Установка соединения с API сервером..."

    def teardown(self):
        return "Закрытие соединения с API сервером..."


class DatabaseEnvironment(BaseEnvironment):
    """Класс окружение для Базы данных"""

    def setup(self):
        return "Подключение к DATABase"

    def teardown(self):
        return "Отключение от DATABase "


def execute_test(environment, test_name):  # Принимает окружение и имя теста
    """
    Функция подготавливает окружения
    """
    actions = []  # Список действий
    test_run = f"Выполнение теста: {test_name}"

    # 1. Подготовка кружения
    try:  # Проверим что setup не упал
        actions.append(environment.setup())  # Добавим в список действий
    except Exception as e:
        print(f"Ошибка при создание окружения (setup): {e}")  # В консоль
        return actions  # Если упало, то верни список действий очистка окружения не выполняй

    # 2. Выполнение теста
    try:
        test_run = f"Выполнение теста {test_name}"
        actions.append(test_run)  # Добавь в список действий
    except Exception as e:
        print(f"Тест {test_name} завершился с ошибкой: {e}")
        actions.append(f"Ошибка в тесте: {e}")
    finally:
        # Очистка окружения
        # 3. Очитка окружения
        try:
            actions.append(environment.teardown())  # Проверим что teardown не упал
        except Exception as e:
            print(f"Ошибка при очистки окружения (teardown): {e}")
            actions.append(f"Ошибка в teardown")  # Добавь в список действий
            return actions

    return actions  # Вернём все действия выполненные функцией


web_environment = WebEnvironment()
api_environment = ApiEnvironment()
data_environment = DatabaseEnvironment()
# print(execute_test(api_test, '"Логин"'))
# print(execute_test(web_test, "Наличие кнопка 'Корзина'"))
# print(execute_test(api_test, "Проверка записи в наличие ID"))

list_environment = [web_environment, api_environment, data_environment]  # Создаём список окружений
for environment in list_environment:  # Циклом проходимся по каждому окружению
    print(execute_test(environment, "Логин"))
