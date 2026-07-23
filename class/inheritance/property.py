class Circus:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


c = Circus(10)
print(c.area())


class Circus_2:
    def __init__(self,radius: int):
        self.radius = radius

    @property
    def area(self: int):
        return 3.14 * self.radius **2

c2 = Circus_2((23))
print(c2.area)