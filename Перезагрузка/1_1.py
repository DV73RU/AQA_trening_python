class TestReport:
    def __init__(self, results: list):
        self.results = results

    def __add__(self, other):
        if not isinstance(other, TestReport):
            return NotImplemented("Не реализовано с таким типом")
        return TestReport(self.results + other.results)

    # def __gt__(self, other):
    #     if not isinstance(other, TestReport):
    #         return NotImplemented
    #     return self.results.count("PASSED") > other.results.count("PASSED")

    def __gt__(self,other):
        if isinstance(other,TestReport):
            return self.results.count("FAILED") > other.results.count("FAILED")
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other,TestReport):
            return self.results.count("PASSED") >= other.results.count("PASSED")
        return NotImplemented


report1 = TestReport(["PASSED", "FAILED"])
report2 = TestReport(["PASSED", "FAILED"])
report3 = TestReport(["FAILED"])

print(report1.results)
print(report2.results)
#
# print(report1 > report2)  # True
# # print(report1 != report3)  # False
# print(sorted(report1.results))
# print(report2.results)
print(report1 > report2)
print(report1 < report2)
