from dataclasses import dataclass, field
from enum import Enum
from itertools import count


class TestStatus(Enum):
    PENDING = "Pending"
    PASSED = "Passed"
    SKIPPED = "Skipped"
    FAILED = "Failed"


@dataclass
class TestResult:
    name: str
    status: TestStatus = TestStatus.PENDING
    duration: float = field(default=0.0, repr=False)  # По умолчанию 0.0, но не отображается в __repr__&#xA;
    errors: list[str] = field(default_factory=list,repr=False)  # По умолчанию пустой список, но не отображается в __repr__&#xA;
    retries: int = field(default=0, init=False)  # По умолчанию 0, но не передается в __init__&#xA;
    # success: bool = field(default=False, init=False)

    def __post_init__(self):  # После инита
        if not isinstance(self.status, TestStatus):  # Проверка типа status на TestStatus&#xA;
            raise TypeError(f"Не верный тип статуса: {self.status}")
        # self.success = self.status == TestStatus.PASSED

    @property
    def success(self) -> bool:
        return self.status == TestStatus.PASSED


class TestRunner:
    def run_test(self, name_test: str,
                 status: TestStatus) -> TestResult | None:  # метод принимает название теста и статус.
        try:
            test_result = TestResult(name_test, status)
            return test_result
        except TypeError:
            print("Ошибка создания результата теста")

            return None

    def is_passed(self, result: TestResult) -> bool:
        return result.status == TestStatus.PASSED

    def count_by_status(self, results: list[TestResult], status: TestStatus) -> int | None:
        count = 0
        for result in results:
            if result.status == status:
                count = count + 1
        return count

    # def get_pass_rate(self, results: list[TestResult]) -> float:

    def get_statistics(self, results: list[TestResult]) -> dict[str, int]:
        statistics = {}  # Создали пустой словарь
        statistics.update({"total": len(results)})
        statistics.update({"passed": self.count_by_status(results, TestStatus.PASSED)})
        statistics.update({"failed": self.count_by_status(results, TestStatus.FAILED)})
        statistics.update({"skipped": self.count_by_status(results, TestStatus.SKIPPED)})
        return statistics

    def get_pass_rate(self, results: list[TestResult]) -> float:
        statistics = self.get_statistics(results)
        if statistics["total"] > 0:
            return round((statistics["passed"] / statistics["total"] * 100),2)

        return 0.0



# Твоя реализация



res1 = TestResult("Login", TestStatus.PASSED)
res2 = TestResult("Login", TestStatus.PASSED)

runner = TestRunner()
res = runner.run_test("Login", TestStatus.PASSED)

if res is not None:
    print(res.status.value)
    print(res.status.name)

print(runner.is_passed(res1))
print(runner.is_passed(res2))

results = []

results = [
    TestResult("Login", TestStatus.PASSED),
    TestResult("Logout", TestStatus.FAILED),
    TestResult("Profile", TestStatus.PASSED),
    TestResult("Payment", TestStatus.SKIPPED),
]

print(runner.get_statistics(results))
print(runner.get_pass_rate(results))
