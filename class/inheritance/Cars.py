    class Car:
    count = 0 # Атрибут класса - количество
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
        Car.count = Car.count + 1

    @classmethod #Метод класса
    def get_count(cls):
        print(f"Машин создано {cls.count}")

    @staticmethod #Метод статически
    def is_valid_speed(speed):
        print(0 < speed < 300)

    def info(self): #Методы экземпляра класса
        print(f"{self.name} | Скорость {self.speed}")


my_car = Car("Ауди",120)
my_car1 = Car("Мерседес",145)
my_car2 = Car("BMW",200)
my_car.info()
Car.get_count()
Car.is_valid_speed(501)
Car.is_valid_speed(-1)
Car.is_valid_speed(250)