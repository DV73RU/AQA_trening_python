from netaddr.strategy.ipv6 import width


class Share:
    def __init__(self,width,height):
        self.width = width
        self.height = height


    @classmethod
    def square(cls,side): # Метод класса создаёт экземпляр квадрат
        return cls(side,side)

    @classmethod
    def from_string(cls, data): # Метод принимает строку и вернёт значение ширины и длинны.
        cls.data = data
        width, height = map(int, cls.data.split("x"))
        return cls(width, height)

    @classmethod
    def from_dict(cls,data):
        cls.data = data
        width = data.get("width")
        height = data.get("height")
        return cls(width,height)

    def info(self):
        print(f"{self.width}x{self.height} | Площадь {self.area()} | Периметр {self.perimetr()}")

    def area(self):
        area = self.width * self.height
        return area

    def perimetr(self):
        perimetr = (self.width + self.height) * 2
        return perimetr

s1 = Share.square(5)
s1.info()

s2 = Share.from_string("10x30")
s2.info()
s3 = Share.from_dict({"width": 10, "height": 20})
s3.info()



