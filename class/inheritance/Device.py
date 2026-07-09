class Device:
    """Класс устройство"""
    def __init__(self,name,status=False):
        self.name = name
        self.status = status

    def turn_on(self):
        """Метод включает устройство"""
        self.status = True

    def turn_off(self):
        """Метод выключает устройство"""
        self.status = True

    def info(self):
        """Метод выводит информацию о состоянии устройства"""
        if self.status == False:
            print(f"Устройство {self.name} - Выключено 🔴 ")
        else:
            print(f"Устройство {self.name} - Включено 🔵 ")
