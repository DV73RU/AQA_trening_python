class Temperature:
    """Класс родитель температура"""
    def __init__(self,temp_celsius): #Конструктор класса принимает атрибуты температуру в цельсиях.
        self.temp_celsius = temp_celsius


    def info(self):# Метод экземпляра
        print(f"Температура : {self.temp_celsius}°C" )


    @staticmethod # Декоратор статического метода
    def to_fahrenheit(c): #Метод статический: Конвертирует в из цельсия в фарингейты, принимает цельсии
        f = c *(9/5) + 32
        print(f"{f} F" )

    @staticmethod # Декоратор статического метода
    def to_kelvin(c):# Метод принимает целсии вернет кельфины
        k = c + 237.15
        print(f"{k} K")

    @classmethod # Декоратор метода класса
    def from_fahrenheit(cls,f): #Метод принимает фаренгейты вернёт Цельсии
        c = (f - 32) * 5/9
        return cls(c)




t = Temperature(10) #
t.info()

Temperature.to_fahrenheit(100) # Вызываем класс с методом конвертации в фаренгейты
Temperature.to_kelvin(100)


t2 = Temperature.from_fahrenheit(100)
t2.info()