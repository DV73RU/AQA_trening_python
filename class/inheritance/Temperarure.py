class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius


    @property
    def celsius(self):
        return self._celsius


    @celsius.setter
    def celsius(self,value):
        if value < -273:
            print(f"Ошибка! Ниже абсолютного нуля!") # Передали значение атрибута экзампляра не верно
            self._celsius = 0
        else:
            self._celsius = value

    @property #Обращение к методу как атрибуту
    def fahrenheit(self):
        """Метод вернёт фарингейты"""
        far = (self._celsius * 9/5) + 32
        return far
    @property
    def kelvin(self):
        """Метод вернёт кельвины"""
        kel = (self._celsius + 273)
        return kel


t_c  = Temperature(-280)
print(t_c.fahrenheit)
print(t_c.kelvin)
