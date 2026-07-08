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

my_new_car = Car("audi","a4",2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(1200)
my_new_car.read_odometer()

# my_new_car.odometer_reading = 0 # Прямое изменение атрибута класса (экземпляра)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(1000)

my_new_car.increment_odometer(20000)
my_new_car.read_odometer()

my_new_car.get_descriptive_name()


print(my_new_car.get_descriptive_name())
my_new_car.increment_odometer(-100)