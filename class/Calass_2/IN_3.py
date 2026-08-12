class TestCase:
    """Класс тест кейс, описывает атрибуты и методы тест кейса"""
    lst_status = ["NEW", "PASSED", "FAILED"]  # Список доступных статусов

    def __init__(self, name: str,
                 status="NEW"):  # Метод инициализатор экземпляра тест кейса по умолчанию при создании экземпляра статус NEW
        self.name = name  # Параметр экземпляра принимает имя тест кейса
        self.stat = status  # Тут Вызываем сеттер @stat.setter

    @property  # Декорируем, метод становиться атрибутом (также для избегания гетеров и сетеров)
    def stat(self):
        return self.__status  # Верни приватное значение статуса

    @stat.setter  # Декоратор для установки статуса тест кейса
    def stat(self, status):
        if status in self.lst_status:  # Если статус присутствует в списке статусов
            self.__status = status  # забираем переданный статус и отдаем в экземпляр
        else:
            raise ValueError(f"Не верное значение status: {status}")  # Иначе выброси ошибку


class TestSuite:
    """Класс Набор тестов"""

    def __init__(self, suite_name):
        """Метод инициализации класса набор тестов"""
        self.suite_name = suite_name  # Название набора тестов

        self.list_test_case = []  # Список с тестами

    def add_test(self, test_case):
        """Метод добавляет тест в набор тестов"""
        self.list_test_case.append(test_case)  # Добавим объект тест кейс в список тест кейсов ()

    def get_report(self):
        """Метод вернёт названия всех тестов и их статус"""
        if self.list_test_case: # Если список не пустой
            print(f"В TestSuit: {self.suite_name}")
            for tst in self.list_test_case:  # Циклом пробегаемся по списку тестов
                print(f"Имя теста: {tst.name} | Статус теста: {tst.stat}")
        else:  # Иначе верни
            print(f"Нет тестов в: {self.suite_name}")  # Верни текст и название списка тестов

    def set_status_test(self, test_name, new_status):
        """Метод находит тест по названию и меняет на у него статус"""
        for tst in self.list_test_case:  # Циклом пробегаемся по списку тестов
            if tst.name == test_name:
                try:  # Что-то не срабатывает проверка валидности переданного статуса
                    tst.stat = new_status  # Установим новый статус. Вызываем  сеттер @stat.setter
                    print(f"Статус теста {tst.name} изменен на {new_status}")
                except ValueError as err:
                    print(f"Не верно передан статус: {new_status} в тест: {self.suite_name} : {err}")

        else:
            return f"Нет такого теста {test_name} в {self.suite_name}"  # Если не нашли такого теста в списке тестов

    def count_by_status(self, status):
        """Метод вернёт все тесты с переданным статусом """
        if status not in TestCase.lst_status:  # Если переданный статус нет в списке статусов
            raise ValueError(f"Статус '{status}' не доступен для передачи")
        else:  # Иначе подсчитай количество тестов с переданным статусом
            count_test = 0
            for tst in self.list_test_case:
                if tst.stat == status:
                    count_test = count_test + 1
            return count_test

    def get_rate(self):
        """Метод вернёт процент тестов сто статусом 'PASSED'"""
        if not self.list_test_case:  # Если список тестов пустой
            return f"Нет тестов в {self.suite_name} для вывода статистики 0%"

        all_statuses = [tst.stat for tst in self.list_test_case]  # Собираем все статусы в список

        count_passed = all_statuses.count("PASSED")  # Считаем количество PASSED через встроенный метод .count()

        res = (count_passed / len(self.list_test_case)) * 100  # Считаем процент (деление на ноль невозможно)

        return f"Процент тестов PASSED в {self.suite_name}: {round(res, 1)}%"  # round(res, 1) округлит до одного знака после запятой


# Список тестов
test1_suite1 = TestCase("Авторизация")
test1_suite2 = TestCase("Авторизация")
test2_suite1 = TestCase("Добавление в корзину")
test2_suite2 = TestCase("Добавление в корзину")
test3_suite1 = TestCase("Удаление из корзины")
test3_suite2 = TestCase("Удаление из корзины")
test4_suite1 = TestCase("Подписка на рассылку новостей")
test4_suite2 = TestCase("Подписка на рассылку новостей")
test5_suite1 = TestCase("Логаут")
test5_suite2 = TestCase("Логаут")

# Созданы списки тестов
suite1 = TestSuite("Регресс_1") # Первый список
suite2 = TestSuite("Регресс_2") # Второй список

# В первый список добавлены тесты
suite1.add_test(test1_suite1)
suite1.add_test(test2_suite1)
suite1.add_test(test3_suite1)
suite1.add_test(test4_suite1)
suite1.add_test(test4_suite1)

# Во второй список добавлены тесты
suite2.add_test(test1_suite2)
suite2.add_test(test2_suite2)
suite2.add_test(test3_suite2)
suite2.add_test(test4_suite2)
suite2.add_test(test5_suite2)

suite1.set_status_test("Авторизация", "PASSED")

print(suite1.get_rate())
print(suite2.get_rate())
suite1.get_report()
# print(suite1.count_by_status("NEW1"))
suite1.set_status_test("Авторизация", "PASSED")
print(suite1.count_by_status("PASSED"))
suite2.get_report()