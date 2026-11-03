class TestReport:
    def __init__(self, results: list):
        self.results = results
        # self.author = author

    def __add__(self, other):  # Метод складывает атрибуты экземпляра создавая новый экземпляр
        if not isinstance(other, TestReport):
            return NotImplemented
        return TestReport(self.results + other.results)

    def __iadd__(self, other):  # Метод складывает атрибуты класса, но не создаёт новый экземпляр
        if not isinstance(other, TestReport):
            return NotImplemented
        self.results += other.results
        return self

    def __eq__(self, other):  # Сравнение атрибутов
        if not isinstance(other, TestReport):
            return NotImplemented
        return sorted(self.results) == sorted(other.results)

    def __gt__(self, other):
        if not isinstance(other, TestReport):
            return NotImplemented
        return self.results.count("PASSED") == other.results.count("PASSED")

    def __ge__(self, other):
        if not isinstance(other, TestReport):
            return NotImplemented
        return self.results.count("PASSED") >= other.results.count("PASSED")

    def __str__(self):
        return f"{type(self).__name__}: {len(self.results)} tests"

    def __repr__(self):
        return f"{self.__class__.__name__}(results={self.results!r})"


report1 = TestReport(["PASSED", "FAILED"])
report2 = TestReport(["FAILED", "PASSED"])

print(report1 == report2)  # True

report3 = report1 + report2
print(report3.results)
# ['PASSED', 'FAILED', 'FAILED', 'PASSED']

report1 += report2
print(report1.results)
# ['PASSED', 'FAILED', 'FAILED', 'PASSED']
