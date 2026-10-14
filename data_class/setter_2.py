from dataclasses import dataclass, field
from enum import Enum


class TestStatus(Enum):
    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"


@dataclass
class TestResult:
    name: str
    status: TestStatus


@dataclass
class TestReport:
    name:str
    results: list[TestResult] = field(default_factory=list)

    def add_result(self,test_result: TestResult) -> None:
        """Метод добавляет результат тестов в репорт"""

        if not isinstance(test_result, TestResult):
            raise TypeError(f"Не верно предали тип {test_result}")
        else:
            self.results.append(test_result)

    # def count_failed(self) -> int:
    #     count = 0
    #     for res in self.results:
    #         if res.status == TestStatus.FAILED:
    #             count = count + 1
    #     return count

    def count_status(self,status: TestStatus)-> int:
        count = 0
        for res in self.results:
            if res.status == status:
                count = count + 1
        return count


    def get_failed_names(self) -> list[str]:
        list_failed_name = []
        for res in self.results:
            if res.status == TestStatus.FAILED:
                list_failed_name.append(res.name)
        return list_failed_name

    def get_summary(self) -> dict[str, int]:
        dict_summary = {}
        dict_summary.update({"total": len(self.results)})
        dict_summary.update({"passed": self.count_status(TestStatus.PASSED)})
        dict_summary.update({"failed": self.count_status(TestStatus.FAILED)})
        dict_summary.update({"skipped": self.count_status(TestStatus.SKIPPED)})

        return dict_summary


"""
{
    "total": 4,
    "passed": 1,
    "failed": 2,
    "skipped": 1
}
"""

result1 = TestResult("API Regression",TestStatus.PASSED)
result2 = TestResult("API subscription", TestStatus.SKIPPED)
print(result1) # Смотрю что в экземпляре
report = TestReport("Результат")
print(report) # Смотрю что в репорте
report.add_result(result1) # Добавим в репорт результат теста
report.add_result(result2) # Добавим в репорт результат теста
print(report) # Смотрю что в репорте

report.add_result(TestResult("Login", TestStatus.PASSED))
report.add_result(TestResult("Logout", TestStatus.FAILED))

print(report.results)

print(report.count_failed())

report = TestReport("API Regression")

report.add_result(TestResult("Login", TestStatus.PASSED))
report.add_result(TestResult("Logout", TestStatus.FAILED))
report.add_result(TestResult("Payment", TestStatus.FAILED))
report.add_result(TestResult("Profile", TestStatus.SKIPPED))

print(report.count_failed())
print(report.get_failed_names())
print(report.get_summary())