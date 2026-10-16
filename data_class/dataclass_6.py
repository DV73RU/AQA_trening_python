from dataclasses import dataclass, field
from enum import Enum


class TestStatus(Enum):
    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    PENDING = "Pending"


@dataclass
class TestResult:
    name: str
    status: TestStatus = TestStatus.PENDING  # По умолчанию PENDING
    duration: float = 0.0  # По умолчанию 0.0
    errors: list[str] = field(default_factory=list)  # Список каждый свой для каждого экземпляра
    retries: int = field(default=0, init=False)  # По умолчанию 0 не входит в конструктор экземпляра

    def __post_init__(self):  # Проверим атрибуты экземпляра после его создания
        """Метод валидации атрибутов, написан для тренировки"""
        # ====== name ======
        if not isinstance(self.name, str):  # -> Ели передали не строку
            raise TypeError(f"Передали '{self.name}' - не строка ({type(self.name)})")
        if len(self.name) <= 0:  # Если передали пустую строку
            raise ValueError(f"{self.name} - передали пустую строку")
        # ====== status ======
        if not isinstance(self.status, TestStatus):  # -> Если не TestStatus
            raise TypeError(f"Передали '{self.status}' - не верный тип ({type(self.status)})")
        # ====== duration ======
        if type(self.duration) not in (float, int):  # -> Если не int и float
            raise TypeError(f"Передали '{self.duration}' - не верный тип ({type(self.duration)})")
        if self.duration < 0:
            raise ValueError(f"{self.duration} - не может быть отрицательным")

        # ====== errors ======
        if not isinstance(self.errors, list):  # -> Если не список
            raise TypeError(f"{self.errors} - не список")
        if any(not isinstance(x, str) for x in self.errors):
            invalid_item = next(x for x in self.errors if type(x) != str)
            raise TypeError(
                f"Элемент '{invalid_item}' (тип {type(invalid_item).__name__}) в {self.errors} не является строкой")

        # ====== retries ======
        # Не валидирем так как не входит в конструктор __init__

    def add_error(self, value: str) -> None:  # """Метод добавляет ошибку в атрибут errors элемент текст ошибки"""
        if not isinstance(value, str):
            raise TypeError(f" {value} - не строка а ,{type(value)}")
        self.errors.append(value)

    def add_retry(self) -> None:
        self.retries = self.retries + 1

    @property
    def is_success(self) -> bool:
        return self.status == TestStatus.PASSED  # Верни значение проверки этого выражения


@dataclass
class TestReport:
    name: str
    results: list[TestResult] = field(default_factory=list)

    def add_result(self, result: TestResult) -> None:
        """Метод принимает экземпляр результат теста"""
        if not isinstance(result, TestResult):  # Если переладил не результат теста
            raise TypeError(f"Передали не верный тип объекта {result}")

        self.results.append(result)

    def count_status(self, status: TestStatus) -> int:
        """Метод считает количество результатов с указанным статусом """
        count = 0
        if not isinstance(status, TestStatus):  # Если передали не тот тип в статус
            raise TypeError(f"Передали не верный тип объекта {status}")
        for res in self.results:  # Перебери результаты из списка результатов
            if res.status == status:
                count = count + 1
        return count

    def get_failed_names(self) -> list[str]:
        """Метод вернёт название тестов со статусом FAILED"""
        list_name = []
        for res in self.results:
            if res.status == TestStatus.FAILED:
                list_name.append(res.name)
        return list_name


class ReportManager:
    def __init__(self, report: TestReport):
        self.report = report

    def get_statistics(self) -> dict[str, int]:
        """Метод вернёт словарь статистики"""
        stata = {'total': 0, 'passed': 0, 'failed': 0, 'skipped': 0}

        total = len(self.report.results)  # Забрали длину списка
        passed = self.report.count_status(TestStatus.PASSED)  # Забрали количество Passed
        failed = self.report.count_status(TestStatus.FAILED)
        skipped = self.report.count_status(TestStatus.SKIPPED)

        if total == 0:
            return stata
        stata.update({"total": total})
        stata.update({"passed": passed})
        stata.update({"failed": failed})
        stata.update({"skipped": skipped})

        return stata

    def get_pass_rate(self) -> float:
        """Метод рассчитывает и возвращает процент успешных тестов """

        res = self.get_statistics()
        if res['total'] == 0:
            return 0.0

        pass_rate = (res['passed'] / res['total']) * 100

        return round(pass_rate,2)


report = TestReport("API Regression")

report.add_result(TestResult("Login", TestStatus.PASSED))
report.add_result(TestResult("Logout", TestStatus.FAILED))
report.add_result(TestResult("Payment", TestStatus.FAILED))
report.add_result(TestResult("Profile", TestStatus.SKIPPED))

print(report.count_status(TestStatus.PASSED))
print(report.count_status(TestStatus.FAILED))
print(report.count_status(TestStatus.SKIPPED))
print(report.get_failed_names())
print(report)
men = ReportManager(report)
print(men.get_statistics())
print(men.get_pass_rate())
