class ApiTest:
    def run(self):
        return f"Тест: {ApiTest.__name__} запущен..."

class UiTest:
    def run(self):
        return f"Тест: {UiTest.__name__} запущен..."


test1 = ApiTest()
test2 = UiTest()

list_tests = [test1,test2]


print(list_tests)
for test in list_tests:
    print(test.run())