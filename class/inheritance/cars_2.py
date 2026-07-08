class Car:
    """Класс автомобиль"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year  = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Метод выводит атрибуты описания автомобиля"""
        long_name = f"{self.year} {self.model} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Метод выводит пробег машины"""
        print(f"У этой машины {self.odometer_reading} миль пробега")

    def update_odometer(self,mileage):
        """
        Метод меняет значение одометра на передаваемый атрибут данного метода
        При попытки обратной прокрутки одометра изменения отклоняются
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете скрутить одометр")

    def increment_odometer(self,miles):
        """Метод увеличения одометра на переданное в метод приращение """
        if self.odometer_reading >= miles:
            self.odometer_reading = self.odometer_reading + miles
        else:
            print("Отрицательное приращение не доступно")


class ElectricCar(Car):
    """Класс электромобили"""
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"У этого автомобиля {self.battery_size} - kWh батарея")


class Battery:
    """Класс батарея"""
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"У этого автомобиля батарея {self.battery_size} - kWh")





my_new_car = Car("audi","a4",2019)
my_el_car = ElectricCar("tesls", "model s", 2019)

print(my_el_car.get_descriptive_name())

my_el_car.describe_battery()