
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
        self.status = False

    def info(self):
        """Метод выводит информацию о состоянии устройства"""
        if not self.status:
            print(f"    {self.name} - Выключено 🔴 ")
        else:
            print(f"    {self.name} - Включено 🔵 ")

class Room:
    """Класс комнаты"""
    def __init__(self,name):
        self.name = name
        self.devices = []

    def add_device(self,device):
        """Метод добавляет устройство в комнату"""
        self.devices.append(device)
        print(f"В комнату {self.name} добавлено устройство: {device.name}")

    def turn_on_all(self):
        """"Метод включает все устройства в комнате"""
        # for d in self.devices:
        #     d.status = True # Менем у всех девайсов статус на включено
        for d in self.devices:
            d.turn_on()

    def turn_off_all(self):
        """"Метод выключает все устройства в комнате"""
        # for d in self.devices:
        #     d.status = False # Менем у всех девайсов статус на выключено
        for d in self.devices:
            d.turn_off()

    def info(self):
        """Метод выводит информацию о комнате"""
        print(self.name)
        if not self.devices:
            print("    Нет устройств")
        for dev in self.devices:
            dev.info()



class SmartHome:
    def __init__(self,name):
        self.name = name
        self.rooms = []

    def add_rooms(self,room):
        """Метод добавляет комнату в дом"""
        self.rooms.append(room)
        print(f"В умный дом: '{self.name}' добавлена комната: '{room.name}'")

    def info(self):
        """Метод выводит информацию об Умном доме"""
        print(f"{self.name}")
        if not self.rooms:
            print(" Нет комнат")
        for ro in self.rooms:
            ro.info()


    def turn_off_all(self):
        """Метод выключает всё во всех комнатах"""
        print(f" Выключение всех устройств в доме '{self.name}'...")
        for ro in self.rooms:
            ro.turn_off_all()  # Вызываем метод выключения у каждой комнаты






lamp = Device("Лампа")
tv = Device("Телевизор")
condicioner = Device("Кондиционер")
living = Room("Гостиная")

lamp.info()

living2 = Room("Малая комната")
living2.add_device(condicioner)
home1 = SmartHome("Дом1")
home1.add_rooms(living)
home1.add_rooms(living2)

living.add_device(lamp)
living.add_device(tv)

living.info()
living2.info()

home1.info()
