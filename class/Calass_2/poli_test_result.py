class TestResult:
    """
    Класс результат теста


    """
    list_status = ["PASSED", "FAILED", "SKIPPED"]  # Статусы доступных тестов

    def __init__(self, name, status, text_error):
        self.name = name
        self.status = status
        self.text_error = text_error


class ResultReporter:
    """Класс Отправки Результат теста (родитель)"""

    def __init__(self):
        pass

    def publish(self, text):
        """Метод публикует отчёт"""
        return f"{text}"


class ConsoleReporter(ResultReporter):
    """Класс публикация отчета в консоль (дочерний)"""

    def __init__(self, name_run):
        super().__init__()
        self.name_run = name_run  # Принимает название запуска

    def publish(self,
                test_result_object: TestResult):  # Метод принимает результат теста как объект экземпляра класса TestResult
        """Метод публикации отчёта в консоль"""
        # Вернём куда отправили Имя теста, его статус и текст ошибки
        if test_result_object.status == "FAILED":
            return f"Отправка в консоль: {self.name_run}\nИмя теста: {test_result_object.name}, Статус теста: {test_result_object.status} , Текст ошибки: {test_result_object.text_error}"
        else:  # Если другие статусы верни так:
            return f"Отправка в консоль: {self.name_run}\nИмя теста: {test_result_object.name}, Статус теста: {test_result_object.status}"


class TelegramReporter(ResultReporter):
    """Класс публикация отчета в телеграм сообщество (дочерний)"""

    def __init__(self, id_chat):
        super().__init__()
        self.id_chat = id_chat  # Экземпляр принимает id часта в телеграм

    def publish(self,
                test_result_object: TestResult):  # Метод принимает результат теста как объект экземпляра класса TestResult
        """Метод публикации отчёта в Telegram"""
        # Вернём куда отправили Имя теста, его статус и текст ошибки
        if test_result_object.status == "FAILED":
            return f"Отправка в Телеграмм чат: {self.id_chat}\nИмя теста: {test_result_object.name}, Статус теста: {test_result_object.status} , Текст ошибки: {test_result_object.text_error}"
        else:  # Если другие статусы верни так:
            return f"Отправка в Телеграмм чат: {self.id_chat}\nИмя теста: {test_result_object.name}, Статус теста: {test_result_object.status}"


class JiraReporter(ResultReporter):
    """Класс публикации отчёта в Jira"""

    def __init__(self, project_name):
        super().__init__()
        self.project_name = project_name  # Экземпляр принимает название проекта в Jira

    def publish(self,
                test_result_object: TestResult):  # Метод принимает результат теста как объект экземпляра класса TestResult
        """Метод публикации отчёта в Jira"""
        # Вернём куда отправили Имя теста, его статус и текст ошибки
        if test_result_object.status == "FAILED":
            return f"Отправка в Jira в проект: {self.project_name}\nИмя теста: {test_result_object.name}, Статус теста: {test_result_object.status} , Текст ошибки: {test_result_object.text_error}"
        else:  # Если другие статусы верни так:
            return f"Отправка в Jira в проект: {self.project_name}\nИмя теста: {test_result_object.name}, Статус теста: {test_result_object.status}"


def publish_results(object_reporter: object, list_results: list):
    """
    Функция
    Принимает объект репортёр, то-есть кому шлём.
    Принимает список результатов тестов, то есть что шлём.
    Возвращает список подготовленных сообщений.
    """
    list_messages = []  # Список подготовленных сообщений
    for res in list_results:  # Перебираем список объектов результатов теста
        message = object_reporter.publish(res)  # Для каждого объекта результат теста выполним метод
        list_messages.append(message)  # Добавь текст тестов в список с текстами
    return list_messages


test1 = TestResult("Логин", "FAILED", "GET CODE: 403")  # Экземпляр результат теста (объект)
test2 = TestResult("Добавление в корзину", "PASSED", "")  # Экземпляр результат теста (объект)
test3 = TestResult("Подписка на новости", "PASSED", "")

consol = ConsoleReporter("Вывод в консоль: ")

telegram_chat = TelegramReporter("id_OZON_чат")  # Экземпляр отправляет в чат

jira = JiraReporter("OZON_SELLERS")

list_results = [test1, test2, test3]  # Формируем список из результатов теста(кладём туда объекты)

for message in publish_results(jira, list_results):
    print(message)
