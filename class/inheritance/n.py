class Car:
    # km = 0

    def __init__(self,color,marc,model, km = 0):
        self.color = color
        self.marc = marc
        self.km = km
        self.model = model


    def add_km(self,value):
        """Метод добавляет километраж"""
        self.km = self.km + value

    def get_km(self):
        """Метод вернёт текущее значение KM"""
        print(self.km)

mazda3 = Car("Красный","mazda","3")
mazda3.get_km()
tig = Car("Синий","VW","Tiguan",10000)

tig.get_km()

mazda3.add_km(100)
tig.add_km(232)
mazda3.get_km()
tig.get_km()