class Temperature:
    """Класс родитель температура"""
    def __init__(self,temp_celsius): #Конструктор класса принимает атрибуты.
        # c = 1.8
        self.temp_celsius = temp_celsius

    def fahrenheit(self): #Метод вернёт температуру в фарингейте
        return self.temp_celsius * 1.8 + 32

    def kelvin(self): #Метод вернёт температуру в Кельвинах
        pass

    def grad_nuton(self): #Метод вернёт температуру в градусах Ньютона
        pass

    # @classmethod
    # def set_


cel = Temperature(10)
print(cel.fahrenheit())