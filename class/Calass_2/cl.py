# """
# 1. Создай класс TestCase. У каждого объекта должны быть атрибуты: название теста и его статус.
# Создай два объекта с разными значениями атрибутов и выведи их на экран.
# """
#
#
#
# class TestCase:
#     """Класс TestCase"""
#
#     def __init__(self, name: str, status: str):
#         """Инициализация экземпляра принимает название теста, его статус """
#         self.name = name
#         self.status = status
#
#
# test1 = TestCase("Авторизация", "PASS")
#
# test2 = TestCase("Добавление в корзину", "FAILED")
#
# print(test1.name, test1.status)
# print(test2.name, test2.status)
#
# """
# 2. Создай класс User с атрибутами name и age. Добавь метод, который выводит информацию о пользователе.
# Создай один объект и вызови этот метод.
# """
#
#
# class User:
#     """Класс пользователь"""
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info_user(self):
#         print(f"Имя: {self.name} | Возраст: {self.age}")
#
#
# user1 = User("Толя", 23)
# user1.get_info_user()
#
# """
# 3. Создай класс BugReport с атрибутами: название бага, серьёзность и статус. Добавь методы:
# для вывода информации о баге;
# для изменения статуса бага.
# """
#
#
# class BugReport:
#     """Класс баг"""
#
#     def __init__(self, name, severity, status):
#         self.name = name
#         self.severity = severity
#         self.status = status
#
#     def get_bug_info(self):
#         """Метод вернёт информацию о баге"""
#         # print(f"Название бага: {self.name} | Серьёзность бага: {self.severity} | Статус бага: {self.status}")
#         return f"Название бага: {self.name} | Серьёзность бага: {self.severity} | Статус бага: {self.status}"
#
#     def set_status_bug(self, new_status):  # <- Принимает текст значения статуса бага
#         """Метод установит статус бага"""
#         self.status = new_status
#
#
# bug1 = BugReport("Ошибка авторизации", "Критическая", "Новый")
# print(bug1.get_bug_info())
# bug1.set_status_bug("Исправлено")
# print(bug1.get_bug_info())
# """
# 4. Создай класс TestRun, который хранит название теста, количество проверок и количество успешно пройденных проверок. Добавь методы:
#
# для регистрации успешной проверки;
# для регистрации проваленной проверки;
# для вывода текущего результата запуска.
#
# Проведи через методы несколько успешных и проваленных проверок.
# """
#
#
# class TestRun:
#     """Клас тест"""
#
#     def __init__(self, name: str):
#         self.name = name  # <- Название прогона
#         self.names = [] # <- Список названий тестов( храним не в классе, а каждом экземпляре)
#         self.count = 0  # <- Всего тестов
#         self.count_done = 0  # <- Пройденных тестов
#
#     def reg_pass_test(self, name):  # Метод принимает название теста
#         """Метод регистрирует успешного прохождение теста"""
#         self.names.append(name)
#         self.count = self.count + 1
#         self.count_done = self.count_done + 1
#
#     def reg_fail_test(self, name):
#         """Метод регистрирует проваленного теста"""
#         self.names.append(name)
#         self.count = self.count + 1  # Добавляем в общее количество тестов
#
#     def get_res(self):
#         """Метод печатает результат прогона"""
#         for name in self.names:
#
#             print(name)
#         print(f"Run: {self.name} | Всего тестов: {self.count} | Успешно пройдено: {self.count_done}")
#
#
# run1 = TestRun("Первый прогон")
#
# run1.reg_pass_test("Авторизация")
# run1.reg_pass_test("Logout")
# run1.reg_fail_test("Добавление товара в корзину")
#
# run2 = TestRun("Второй прогон")
# run2.reg_fail_test("Авторизация")
# run2.reg_fail_test("Добавление в корзину")
# run2.reg_fail_test("Logout")
#
# run1.get_res()
# run2.get_res()
#
# """
# Создай класс TestSuite для управления набором тестов. Объект должен хранить название набора и список тестов. Каждый тест представляется отдельным объектом класса TestCase и содержит название и статус.
#
# Добавь в TestSuite методы:
#
# добавления теста;
# изменения статуса выбранного теста;
# подсчёта тестов с определённым статусом;
# вывода полного отчёта;
# вычисления процента успешно пройденных тестов.
#
# Создай набор, добавь минимум пять тестов с разными статусами и вызови все методы.
# """
"""
Создай класс TestSuite для управления набором тестов. Объект должен хранить название набора и список тестов. Каждый тест представляется отдельным объектом класса TestCase и содержит название и статус.

Добавь в TestSuite методы:

добавления теста;
изменения статуса выбранного теста;
подсчёта тестов с определённым статусом;
вывода полного отчёта;
вычисления процента успешно пройденных тестов.

Создай набор, добавь минимум пять тестов с разными статусами и вызови все методы.
"""


class TestSuite:
    """Класс набор тестов"""

    def __init__(self, name: str): #Принимает параметр название тест сьюта
        self.name = name  # <- Название тестсьюта
        self.list_test_case = []  # <- Список тест кейсов

    def add_test(self,test): # Принимает экземпляр теста
        """Метод добавляет тест"""
        # self.name_test = None
        self.list_test_case.append(test)

    def set_status_test(self,name,status): #Принимает название теста и новый статус
        """Метод изменяет статус """
        for test in self.list_test_case:
            if test.name == name: # Если переданное имя теста есть в списке тесто
                test.status = status #<- Передаём новый статус тесту

    def get_rate(self,status): # Принимает статус тестов
        """Метод печатает процент выполнения тестов"""

        count_status = 0
        if len(self.list_test_case) == 0:
            print("Тест кейсы отсутствуют")
            return

        for test in self.list_test_case:
            if test.status == status:
                count_status = count_status + 1
        print(f"В {self.name}: {status} - {count_status}")
        # количество тестов с нужным статусом / общее количество тестов × 100

    def get_pass_rate(self):
        status = "PASSED"
        count_status = 0
        if len(self.list_test_case) == 0:
            print("Тест кейсы отсутствуют")
            return
        for test in self.list_test_case:
            if test.status == status:
                count_status = count_status + 1
        if len(self.list_test_case) == 0:
            print("Тест кейсы отсутствуют")
        print(f"В {self.name}: {status}:({(count_status / len(self.list_test_case)) * 100:.2F}%)")





    def get_result(self):
        """Метод выводи отчёт о тестах"""
        print(f"В {self.name}: {len(self.list_test_case)} тест")
        for test in self.list_test_case:
            print(f"{test.name} - {test.status}")


class TestCase:
    """Класс тест кейс"""

    def __init__(self, name, status):
        self.name = name  # <- Название теста
        self.status = status  # <- Статус теста

regress = TestSuite("Регресс") # < - Создали экземпляр класса TestSuite
regress2 = TestSuite("Регресс2") # < - Создали второй экземпляр класса TestSuite

test1 = TestCase("Авторизация","PASSED")# < - Создали экземпляр класса TestCase:
test2 = TestCase("Добавление товара в корзину","PASSED") # < - Создали экземпляр класса TestCase:
test3 = TestCase("Выход","PASSED")
test4 = TestCase("Подписка не рассылку","SKIPPED")
test5 = TestCase("Удаление из корзины","SKIPPED")

test1_2 = TestCase("Авторизация","PASSED")# < - Создали экземпляр класса TestCase:
test2_2 = TestCase("Добавление товара в корзину","PASSED") # < - Создали экземпляр класса TestCase:
test3_2 = TestCase("Выход","PASSED")
test4_2 = TestCase("Подписка не рассылку","SKIPPED")
test5_2 = TestCase("Удаление из корзины","SKIPPED")

regress.add_test(test1)
regress.add_test(test2)
regress.add_test(test3)
regress.add_test(test4)
regress.add_test(test5)

regress2.add_test(test1_2)
regress2.add_test(test2_2)
regress2.add_test(test3_2)
regress2.add_test(test4_2)
regress2.add_test(test5_2)



regress.get_result()
regress2.get_result()


regress.set_status_test("Авторизация","SKIPPED")
regress.get_result()
regress2.get_result()

regress2.get_rate("SKIPPED")
regress2.get_rate("PASSED")
regress2.get_rate("FAILED")

regress.get_rate("SKIPPED")
regress.get_rate("PASSED")
regress.get_rate("FAILED")
regress.get_pass_rate()
regress2.get_pass_rate()