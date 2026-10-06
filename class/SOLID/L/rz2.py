class StatusDescriptor:
    def __init__(self, name_status):
        self.name_status = name_status

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # print(f"self = {self}, instance = {instance}, owner = {owner} ")
        return instance.__dict__.get(self.name_status)

    def __set__(self, instance, value):  # Вызываем метод __set__
        # print(f"instance (объект) = {instance}\nvalue (значение) = {value}")
        if value not in  ("PASSED", "FAILED"):
            raise ValueError(f"Пришло не верное значение {self.name_status} - '{value}'")
        instance.__dict__[self.name_status] = value


class TestResult:
    # status = StatusDescriptor("Статус теста")  # Экземпляр дескриптора (атрибут класса TestResult)
    status = "Pass"


res = TestResult()  # Экземпляр класса TestResult
res.status = "FAILED"  # У экземпляра класса мы меняем значение атрибута через  класс StatusDescriptor()

# print(TestResult.status)
#
# print(res.__dict__)
#
# res.status = "PASSED"
# print(res.__dict__)
print(res.status)
print(res.__dict__)
#
try:
    res.status = "Всё работает"
except ValueError as error:
    # print(str(error))
    pass

print(res.status)

