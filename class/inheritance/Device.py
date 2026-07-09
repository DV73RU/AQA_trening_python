from orca.orca_state import device


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
        if not self.status:
            print(f"    Устройство {self.name} - Выключено 🔴 ")
        else:
            print(f"    Устройство {self.name} - Включено 🔵 ")

class Room:
    """Класс комнаты"""
    def __init__(self,name):
        self.name = name
        self.device = []

    def add_device(self,device):
        """Метод добавляет устройство в комнату"""
        self.device.append(device)
        print(f"В комнату {self.name} добавлено устройство {device.name}")

    def torn_on_all(self):
        """"Метод включает все устройства комнате"""
        pass

    def info(self):
        """Метод выводит информацию о комнате"""
        print(f"{self.name}")
        for dev in self.device:
            print(f"{dev.name})

lamp = Device("Лампа")
gostin = Room("Гостиная")

gostin.add_device(lamp)

gostin.info()