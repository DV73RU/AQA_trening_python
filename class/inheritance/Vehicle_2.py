class Vehicle:
    """Класс транспортное средство"""
    def __init__(self,brand,speed,fuel_level = 30):
        self.brand = brand
        self.speed = speed
        self.fuel_level = fuel_level # < - Значение в баке топлива
        self.consumption = None


    def drive(self,km):
        self.fuel_level = self.fuel_level - self.consumption * km
        if self.fuel_level < 0:
            print(f"Топлива не хватит на {km} км")
            print(f"Хватит на {abs(self.fuel_level / self.consumption)} км")
        else:
            print(f"{self.brand}  Едет {km}км. топливо {self.fuel_level}")

    def info(self):
        """Метод экземпляра информация о транспортном средстве"""
        print(f"{self.brand} | {self.speed} | {self.fuel_level}")


class GasCar(Vehicle):
    def __init__(self,brand,speed,fuel_level = 30):
        super().__init__(brand,speed,fuel_level)
        self.consumption = 0.1

    def refuel(self,liters):
        """Метод дочернего экземпляра бензиновая машина"""
        self.fuel_level = self.fuel_level + liters
        print(f"{self.brand} заправлена на {liters} литров Топливо в баке: {self.fuel_level}")

class ElectricCar(Vehicle):
    max_level = 200 # Объём батареей
    def __init__(self,brand,speed, fuel_level = 50):
        super().__init__(brand,speed,fuel_level)
        self.consumption = 0.2

    def charge(self,percent):
        """Метод зарядки электро кара в процентах"""
        self.fuel_level = self.fuel_level + (self.max_level * percent/100)

    def drive(self, km):
        self.fuel_level = self.fuel_level - self.consumption * km
        if self.fuel_level < 0:
            print(f"Заряда не хватит на {km} км")
            print(f"Хватит на {abs(self.fuel_level / self.consumption)} км")
        else:
            print(f"{self.brand}  Едет {km} км. заряд {self.fuel_level} KWt")

class Bicycle(Vehicle):
    """Класс велосипед"""
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
        self.fuel_level = None

    def drive(self,km):
        print(f"{self.brand} -  едет {km}")


to = GasCar("AUDI",200)


my_tesla =ElectricCar("Tesla S",230)
my_tesla.info()
to.info()
my_tesla.drive(10)
my_tesla.charge(50)
my_tesla.info()
my_tesla.drive(10)

my_bicycle = Bicycle("Орлёнок",20)
my_bicycle.info()
my_bicycle.drive(34)