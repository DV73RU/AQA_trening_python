"""
Используй свой TestResult из задачи №6. Нужно обрабатывать список готовых результатов и формировать отчёты.

Реализуй три независимо расширяемые части:

Фильтры результатов: оставить все результаты; оставить только "FAILED" и "Ошибка".
Форматтеры: преобразовать выбранные результаты в обычный текст или JSON. Каждый форматтер возвращает строку.
Способы вывода: вывести готовую строку в консоль или сохранить её в файл.

В отчёт включай название теста, статус и описание ошибки.

Создай ReportService, который получает список результатов, выбранный фильтр, форматтер и способ вывода. Его метод generate() должен:

Отобрать результаты через фильтр.
Сформировать строку отчёта через форматтер.
Передать её выбранному способу вывода.
Вернуть эту же строку.

Если после фильтрации результатов нет, текстовый отчёт должен содержать сообщение «Нет результатов», а JSON — пустой массив.

Требование OCP: новые фильтры, форматы и способы вывода должны добавляться без изменения ReportService. Внутри него нельзя определять конкретные классы переданных объектов через type(), isinstance() или выбирать реализацию по её названию.

Продемонстрируй:

Все результаты — текстовый отчёт в консоль.
Только неуспешные результаты — JSON в файл.
Добавление нового форматтера CSV и его использование через тот же ReportService.

Для демонстрации подготовь результаты со всеми тремя статусами: "PASSED", "FAILED" и "Ошибка".
"""
import csv
from io import StringIO

import requests
import json

from abc import ABC, abstractmethod

urls = "https://catfact.ninja/fact"
urls2 = "catfact.ninja/fact"


class TestResult:
    """Класс результат теста"""

    # тут только храним данные
    def __init__(self, test_name, test_status, text_error, error=None):
        self.test_name = test_name
        self.test_status = test_status
        self.text_error = text_error
        self.exception = error


class GetResponse:
    """ Класс получения ответа HTTP запроса"""

    @staticmethod
    def get(url):
        try:
            response = requests.get(url, timeout=5)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")  # Если не достучались по URL
            raise


class BaseTest(ABC):
    """Класс проверки"""

    @abstractmethod
    def check(self):
        """Метод проверки"""
        pass


class HeaderTest(BaseTest):
    """Класс проверки значения заголовка"""

    def __init__(self, url, value_header):
        self.test_name = "Header Test"
        self.get_headers = GetResponse()  # Создай экземпляр
        self.url = url
        self.value_header = value_header

    def check(self):  # Метод проверяет заголовок
        """Метод проверки заголовка"""
        try:
            response = self.get_headers.get(self.url)  # Вызови get у GetResponse
        except requests.exceptions.RequestException as error:
            return TestResult(self.test_name, "Ошибка", str(error), error)

        content_type = response.headers.get("Content-Type", "")  # Забираем значение из "Content-Type"
        if content_type.split(";")[0].strip() == self.value_header:
            return TestResult(self.test_name, "PASSED", None)
        else:
            return TestResult(self.test_name, "FAILED", f"Ожидалось: {self.value_header}, Получено: {content_type}")


class CodeTest(BaseTest):
    """Класс проверки значения статус кода"""

    def __init__(self, url, value_code):
        self.test_name = "Status Code Test"
        self.get_code = GetResponse()
        self.url = url
        self.value_code = value_code

    def check(self):  # Метод проверяет предаваемое значение статус кода
        try:
            response = self.get_code.get(self.url)
        except requests.exceptions.RequestException as error:
            return TestResult(self.test_name, "Ошибка", str(error), error)

        if response.status_code == self.value_code:
            return TestResult(self.test_name, "PASSED", None)
        return TestResult(self.test_name, "FAILED", f"Ожидалось: {self.value_code}, Получено: {response.status_code}")


class TemporaryFailureTest(BaseTest):
    """Класс учебный тест"""

    def __init__(self, url):
        self.test_name = "Учебный тест"
        self.time = GetResponse()
        self.url = url
        self.count = 0

    def check(self):
        self.count = self.count + 1
        if self.count == 1:
            return TestResult(self.test_name, "Ошибка", "Учебный тест", requests.Timeout())
        return TestResult(self.test_name, "PASSED", None, error=None)


class BaseStrategy(ABC):
    """Абстрактный класс для всех стратегий"""

    @abstractmethod
    def execute(self, list_test):  # Метод применит список тестов
        """Каждая стратегия как пройтись по списку тестов"""
        pass


# =============================================
# Реализованы стратегии
# =============================================
class RunAllStrategy(BaseStrategy):
    """Стратегия 1: Запустить абсолютно все тесты из списка"""

    def execute(self, list_test: list):  # <- Принимает список тестов
        """Метод запускает тесты по стратегии"""
        list_result = []
        for test in list_test:  # Возьми один тест из преданного списка тестов
            result = test.check()  # У теста выполни метод проверки с преданным ответом запроса
            list_result.append(result)
        return list_result


class SingleRetryStrategy(BaseStrategy):
    """Стратегия 2: Запускать тесты повторно c результатом "FAILED" или "Ошибка" один раз"""

    def execute(self, list_test: list):
        list_result = []
        for test in list_test:  # Возьми каждый тест в списке
            print(f"Первая попытка запуска теста: {test.test_name}")
            result = test.check()  # Выполни метод

            if result.test_status == "FAILED" or result.test_status == "Ошибка":  # Если в результате встретили "FAILED", "Ошибка"
                print(f"Повторная попытка запуска теста: {test.test_name}")
                result = test.check()  # Запустить тот же тест ещё раз

            list_result.append(result)  # Добавь результат в список результатов
        return list_result  # Верни список результатов


class ThreeRetryStrategy(BaseStrategy):
    """Стратегия 3: Запустить тесты повторно 3 раза с результатом "FAILED" или "Ошибка" """

    def execute(self, list_test: list):
        list_result = []
        for test in list_test:  # Возьми каждый тест в списке
            result = None
            for att in range(1, 5):
                print(f"Попытка [{att}] запуска теста: {test.test_name}")
                result = test.check()
                if result.test_status not in ["FAILED", "Ошибка"]:
                    break

            list_result.append(result)  # Добавь результат в список результатов
        return list_result  # Верни список результатов


class ExceptionTypeRetryStrategy(BaseStrategy):
    """Стратегия 4: до двух повторов только при таймауте"""

    def execute(self, list_test: list):
        list_result = []
        for test in list_test:  # Возьми каждый тест в списке
            result = None
            for att in range(1, 4):
                print(f"Попытка [{att}] запуска теста: {test.test_name}")
                result = test.check()
                if not isinstance(result.exception, requests.exceptions.Timeout):
                    break

            list_result.append(result)  # Добавь результат в список результатов
        return list_result  # Верни список результатов


# Запускальщик тестов
class TestRunner:
    """Класс запуска тестов. Он абсолютно ЗАКРЫТ для изменений.
    Ему не важно, какие тесты внутри списка
    """

    def __init__(self, strategy: BaseStrategy, list_test: list):  # Принимает стратегию проверок
        self.strategy = strategy
        self.list_test = list_test

    def run(self):
        result = self.strategy.execute(self.list_test)
        return result  # Верни результат выполнения метода у экземпляра


# ========================================
#   Фильтры результатов теста
# ========================================
class Filter(ABC):
    """Базовый класс фильтрации результата тетсат"""

    @abstractmethod
    def apply_filter(self, list_results):
        """Метод применяет фильтрацию"""
        pass


class AllResultsFilter(Filter):
    """Класс фильтр вернёт все результаты"""

    def apply_filter(self, list_results: list):
        """Метод отфильтровывает результаты теста по статусу"""
        # Принимает список результатов тестов
        return list_results  # Верни все результаты


class FailedFilter(Filter):
    """Класс фильтр вернёт все результаты с FAILED и Ошибка"""

    def apply_filter(self, list_results: list):
        """Метод отфильтровывает результаты"""
        # Принимает список результатов тестов
        failed_list = []
        for res in list_results:
            if res.test_status == "FAILED" or res.test_status == "Ошибка":
                failed_list.append(res)
        return failed_list


# ================================================
# Форматы отчёта
# ================================================

class ReportFormatter(ABC):
    """Базовый класс форматера"""

    @abstractmethod
    def format(self, list_results: list):
        pass


class TextFormater(ReportFormatter):
    """Класс форматирования в строку"""

    def format(self, list_results: list) -> str:
        if not list_results:
            return "Нет результатов"
        sting = []
        for res in list_results:
            name = res.test_name
            status = res.test_status
            err = res.text_error

            sting.append(f"{name} | {status} | {err}")
        return "\n".join(sting)


class JsonFormater(ReportFormatter):
    """Класс форматирования в JSON"""

    def format(self, list_results: list) -> str:  # Принимает список обетов результатов тестирования
        if not list_results:
            return json.dumps([], ensure_ascii=False, indent=4)
        formated_list = []
        for res in list_results:
            test_data = {
                "test_name": res.test_name,
                "test_status": res.test_status,
                "text_error": res.text_error
            }
            formated_list.append(test_data)
        return json.dumps(formated_list, ensure_ascii=False, indent=4)


class CsvFormater(ReportFormatter):
    """Класс форматирования в CSV"""

    def format(self, list_results: list) -> str:
        if not list_results:
            return "test_name,test_status,text_error" # Верни только заголовки
        buffer = StringIO() # Создали пустой буфер
        writer = csv.writer(buffer) # Передали в csv.writer буфер
        list_title = ["test_name","test_status","text_error"] # Список названий атрибутов
        writer.writerow(list_title) # Пишем заголовки из списка
        for res in list_results:
            test_name = res.test_name
            test_status = res.test_status
            text_error = res.text_error
            writer.writerow([test_name, test_status, text_error])


        return buffer.getvalue()



# ===============================================
# Классы вывода
# ===============================================

class ReportOutput(ABC):
    """Класс вывода отчёта"""

    @abstractmethod
    def output(self, report_text: str) -> None:
        """Метод вывода отчёта"""

    pass


class ConsoleOutput(ReportOutput):
    """Класс вывода отчёта в консоль"""

    def output(self, report_text: str) -> None:
        print(report_text)


class FileOutput(ReportOutput):
    """Класс вывода отчёта в файл"""

    def __init__(self, file):
        self.file = file  # <- Принимает файл и путь к файлу

    def output(self, report_text: str) -> None:
        with open(self.file, "w", encoding="UTF-8", newline="") as file:
            file.write(report_text)


# =======================================
#   Сервис отчёта тестов
# =======================================

class BaseReportService(ABC):
    """Базовый класс репорт результатов теста"""

    def __init__(self, list_results: list, filters: Filter, formater: ReportFormatter, outputs: ReportOutput) -> None:
        self.list_results = list_results  # Принимает список результатов тестов
        self.filters = filters  # Принимает фильтр
        self.formater = formater  # Принимает формат вывода
        self.outputs = outputs  # Принимает способ вывода

    @abstractmethod
    def generate(self) -> str:
        """Возвращаем отчёт"""
        pass


class ReportService(BaseReportService):
    """Класс репорт результата теста"""

    def generate(self) -> str:
        # 1. Применяем фильтрацию к исходному списку результатов
        filtered_results = self.filters.apply_filter(self.list_results)

        # 2. Форматируем отфильтрованные данные
        formatted_report = self.formater.format(filtered_results)
        self.outputs.output(formatted_report)

        return formatted_report


header_test = HeaderTest(urls, 'application/json')  # Проверка заголовка PASSED
code_test = CodeTest(urls, 200)  # Проверка статус кода PASSED

header_test2 = HeaderTest(urls, 'application/jsons')  # Проверка заголовка FAILED
code_test2 = CodeTest(urls, 100)  # Проверка статус кода FAILED
code_test3 = CodeTest(urls2, 200)

temporary_test = TemporaryFailureTest(urls)

# Список проверок
list_tests = [header_test, header_test2, code_test, code_test2, code_test3]  # Список проверок

# # Стратегии
# strategy1 = RunAllStrategy()
# strategy2 = SingleRetryStrategy()
# strategy3 = ThreeRetryStrategy()
# strategy4 = ExceptionTypeRetryStrategy()
#
# runner12 = TestRunner(strategy4, list_tests)
# res = runner12.run()
#
# for data in res:
#     print(data.__dict__)

result1 = TestResult("Name_Test", "PASSED", None)
result2 = TestResult("Name_Test2", "FAILED", "Ожидалось одно, вернулось другое")
result3 = TestResult("Name_Test3", "Ошибка", "Не верный URL")

lis_1 = [result1, result2, result3]

all_result = AllResultsFilter()
failed_result = FailedFilter()
text_format = TextFormater()
json_format = JsonFormater()
csv_format = CsvFormater()
output = ConsoleOutput()
file_output = FileOutput("отчёт.txt")
csv_output = FileOutput("report.csv")

report = ReportService(lis_1, all_result, text_format, output)
report.generate()

report2 = ReportService(lis_1, failed_result, json_format, file_output)
report2.generate()


report3 = ReportService(lis_1,all_result, csv_format, csv_output)
report3.generate()
