class Calculator:
    # def __init__(self):


    @classmethod
    def description(cls):

        return f"Это калькулятор"

    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def multyply(a,b):
        return a * b

print(Calculator.add(3,5))

print(Calculator.multyply(3,5))

print(Calculator.description())