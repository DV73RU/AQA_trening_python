class ApiTest:
    def run(self):
        return f"API test passed"


class UiTest:
    def run(self):
        return "UI test passed"


class DatabaseTest:
    def run(self):
        return "Database test passed"


def execute_tests(tests:list[object]) -> list:
    list_res = []
    for test in tests:
        res = test.run()
        list_res.append(res)
    return list_res

class BrokenTest:
    def execute(self):
        return "Broken test"



tests = [ApiTest(), BrokenTest(), DatabaseTest()]

results = execute_tests(tests)
print(results)