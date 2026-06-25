class Vehicle:
    """Класс транспортное средство"""
    def __init__(self,brand,speed,fuel): # <- конструктор класса ТТРАНСПОРТНОЕ СРЕДСТВО.
        self.brand = brand # Атрибуты класса
        self.speed = speed
        self.fuel = fuel

    def info(self):
        """Метод информация о транспортном средстве"""
        print(f"Бренд: {self.brand} | Скорость: {self.speed} Топливо: {self.fuel}")
    def move(self):
        """Метод ехать"""
        print(f"{self.brand} едет!")

class Car(Vehicle): # <- Класс наследника класса Транспортное средство
    """Класс Автобобиль"""
    def __init__(self,brand,speed,fuel,doors): # < - конструктор клсса со своими атрибудами.
        super().__init__(brand,speed,fuel) #<- Забираем атрибуды у родителя
        self.doors = doors # <- Свои атрибуты класса кар

    def info(self):
        """Метод информация"""
        print(f"Бренд: {self.brand} | Скорость: {self.speed} | Топливо: {self.fuel} | Дверей: {self.doors}") # Забираем метод у родителя и изменяем пож этот класс

    def move(self):
        print(f"{self.brand} едет!")

    def honk(self):
        """Метод гудок"""
        print(f"{self.brand}: Би-Бип ")



class Motorcycle(Vehicle):
    """Класс мотоцикл"""
    def __init__(self,brand,speed,fuel,has_sidecar): # <- Атрибцты класса.
        super().__init__(brand,speed,fuel) # <- Забираем у родительского класса атрибуды)
        self.has_sidecar = has_sidecar # <- Новые атрибуты класса мотоцикл (наличеи каляски)

    def info(self):
        """Метод информация о мотоциклк"""
        print(f"Бренд: {self.brand} | Скорость: {self.speed} | Топливо: {self.fuel} | Наличие каляски: {self.has_sidecar}") # Забираем метод у родителя и изменяем пож этот класс

    def wheelie(self):
        """Метод езы на заднем колесе"""
        # Если мотоцикл с каляской на заднем колесе не получиться
        print(f"{self.brand} не едет на заднем колесе" if self.has_sidecar else f"{self.brand}  едет на заднем колесе")


class Truck(Vehicle):
    """Класс грузовик"""

    def __init__(self,brand,speed,fuel,capacity):
        super().__init__(brand,speed,fuel)
        self.capacity = capacity # Грузопоьёмность

    def info(self):
        print(f"Бренд: {self.brand} | Скорость: {self.speed} | Топливо: {self.fuel} | Грузоподъёмность: {self.capacity}") # Забираем метод у родителя и изменяем пож этот класс

    def load(self):
        """Метод загружать"""
        print(f"{self.brand} загружает {self.capacity}")

car = Car("Audi A7",200,"Бензин",5)

car.info()
car.move()
car.honk()

moto_ural = Motorcycle("Урал",80,"Бензин",True)
moto_kava_ = Motorcycle("Кавасаки 100",200,"Бензин",False)
moto_ural.info()
moto_ural.wheelie()

moto_kava_.info()
moto_kava_.move()
moto_kava_.wheelie()

truk = Truck("Вольво",120,"Дизель",50000)
truk.move()
truk.info()
truk.load()