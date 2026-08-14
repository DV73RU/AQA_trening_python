def send_report(object_repor: object, text_error: str):
    """Функция принимает объект отправки ошибки и текст ошибки"""
    return object_repor.send_report(text_error)  # Функция при вызове вернет результат метода объекта


class Reporter:
    """Класс отправки сообщений"""

    def send_report(self, text_error):
        return f"Отправка сообщения"


class JiraReporter(Reporter):
    """Класс отправит отчёт в Jira"""

    def __init__(self, project_name):
        self.project_name = project_name  # Принимает параметр название проекта

    def send_report(self, text_error):  # Метод отправки отчёта ( принимает на вход сообщение)
        return f"Отправлен отчёт в Jira Проект: {self.project_name} | Отчёт: {text_error}"


class TelegramReporter(Reporter):
    """Класс отправка отчёта в Telegram сообщество"""

    def __init__(self, id_telegram):
        self.id_telegram = id_telegram  # Принимает id телеграмм сообщества

    def send_report(self, text_error):
        return f"Отправлен отчёт в Телеграм сообщество: {self.id_telegram} | Отчёт: {text_error}"


class ConsoleReporter(Reporter):
    """Класс отправка отчёта в консоль"""

    def __init__(self, name_test_run):
        self.name_test_run = name_test_run  # Принимает название тестового запуска

    def send_report(self, text_error):
        return f"Отправка сообщения в консоль {self.name_test_run} | Отчёт: {text_error} "


jira = JiraReporter("OZON_Logistik")  # Объект (экземпляр) отправки в JIRA
telegram = TelegramReporter("123D_OZON")  # Объект (экземпляр) отправки в Telegram сообщество
consol = ConsoleReporter("Тест_run")

# print(jira.send_report("Ошибка"))
# print(telegram.send_report("Ошибка"))

list_reports = [jira, telegram, consol]  # Пишем в список все объекты
for report in list_reports:  # Циклом забираем объекты по одному
    print(send_report(report,
                      "Текст ошибок"))  # по очереди вызываем функцию send_report которая принимает объект и текст ошибки и возвращает результат
