from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3


class Product:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color


class Specification:
    """Класс элемент"""

    def is_specification(self, item):  # Принимает элемент
        pass


class Filter:
    """Класс фильтр"""

    def filter(self, items, spec):  # Принимает элементы и спецификацию
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_specification(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_specification(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_specification(item):
                yield item


apple = Product("Яблоко", Size.MEDIUM, Color.RED)


print(apple.size)
