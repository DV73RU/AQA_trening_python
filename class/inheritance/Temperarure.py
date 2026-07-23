import tempfile


class Temperature:
    def __init__(self,temperature: float):
        self._temperature = temperature


    @property # < - Геттер
    def to_kel(self):
        res = self._temperature + 273.15
        return res

    @to_kel.setter
    def to_kel(self,value):
        if value > 273:
            return f"температура не может быть 273"
        else:
            return self._temperature



t = Temperature(2)
print(t.to_kel)