class Share:
    def __init__(self,color: str):
        self.color = color
        # self.area = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value:str):
        if isinstance(value, str):
            self._color = value
        else:
            print("Ошибка: переданное значение — не строка!")
            self._color = None  # Задаем дефолтное значение при ошибке



    def info(self):
        print(f"Цвет: {self.color}")

class Circle(Share):

    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = radius
        # self.area = 3.14 * (self.radius ** 2)

    @property
    def area(self):
        return 3.14 *(self.radius ** 2)

    def info(self):
        print(f"Цвет: {self.color}  | Площадь: {self.area}" )

class Rectangle(Share):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width = width
        self.height = height


    @property
    def area(self):
        return self.height * self.width

    def info(self):
        print(f"Цвет: {self.color} | Площадь: {self.area}")

class Triangle(Share):
    def __init__(self,color,base,height):
        super().__init__(color)
        self.base = base
        self.height = height
        # self.area =  self.base * 0.5 * self.height

    @property
    def area(self):
        return self.base * 0.5 * self.height

    def info(self):
        print(f"Цвет: {self.color} | Площадь {self.area}")

cr = Circle("Красный",12)
cr.info()
re = Rectangle("Зелёный",12,24)
re.info()

tr = Triangle("Синий", 2, 3)
tr.info()
cr.radius = 23
cr.info()