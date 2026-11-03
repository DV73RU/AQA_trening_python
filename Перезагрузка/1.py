class TestReport:
    def __init__(self, results: list):
        self.results = results

    def __add__(self, other):
        if not isinstance(other, TestReport):
            return NotImplemented("Не реализовано с таким типом")
        return TestReport(self.results + other.results)

    # def __iadd__(self, other):
    #     if isinstance(other, TestReport):
    #         self.results += other.results
    #         return self  # ОБЯЗАТЕЛЬНО возвращаем self
    #     return NotImplemented
    # #


report1 = TestReport(["PASSED"])
report2 = TestReport(["FAILED"])

report3 = report1

# report1 и report3 - ссылаются на один объект

print(f"{report1} - report1")
print(f"{report2} - report2")
print(f"{report3} - report3")

report1 = report1 + report2

# Тут мы изменяем report1 прибавляя report2

print(report3.results)
print(f"{report1} - report1")
print(f"{report2} - report2")
print(f"{report3} - report3")

report1 = TestReport(["PASSED"])
report2 = TestReport(["PASSED"])

print(report1 == report2)
print(report1 is report2)
