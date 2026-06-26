class Character:
    """Родительский класс - Характер персонажа"""
    def __init__(self,name,hp,damage): # Конструктор характера персонажа.
        #Атрибуты
        self.name = name # < - Атрибут Имя
        self.hp = hp # < - Атрибут здоровье
        self.damage = damage # < - Атрибут уровень наносимого урона

    def info(self):
        """Метод информация"""
        print(f"{self.name} | hp: {self.hp} | Урон: {self.damage}")

    def attack(self,target):
        """Метод - атака"""
        if hasattr(target, 'armor'): # Если у атакуемого есть броня
            real_damage = self.damage - (self.damage * target.armor / 100)
        else:
            real_damage = self.damage
        target.hp -= real_damage
        self.target = target # Кого атакуем
        if self.name != self.target.name: # Себя нельзя атаковать
            self.target.hp = self.target.hp - self.damage # Вычитаем из HP урон
            print(f"{self.name} атакует -> {self.target.name} на {self.damage} урона. У {self.target.name} HP:{self.target.hp}")
        else:
            print("Себя нельзя атаковать")

class Warrior(Character):
    """Класс Воин"""
    def __init__(self,name,hp,damage,armor):
        super().__init__(name,hp,damage)
        self.armor = armor # Свой атрибут уровень защиты

    def info(self):
        """Метод информация"""
        print(f"{self.name} | hp: {self.hp} | Урон: {self.damage} | Защита {self.armor}%" )

    def block(self):
        """Метод блокирования удара"""
        # Как подчитсать защиту?
        # Взять значение атаки атакущего и уменьшить на броню атакуемого, но как?
        # self.hp = self.hp + (self.damage/100)# HP = Часть удара не зачитывается (50%)
        print(f"{self.name} Защищается от удара HP: {self.hp}")




class Mage(Character):
    """Класс Маг """
    def __init__(self,name,hp,damage,mana):
        super().__init__(name,hp,damage)
        self.mana = mana

    def info(self):
        """Метод информация"""
        print(f"{self.name} | hp: {self.hp} | Урон: {self.damage} | Mana: {self.mana}")

    def cast_spell(self,target):
        """Метод двойного удара"""
        self.target = target # Кого атакуем
        if self.name != self.target.name: # Себя нельзя атаковать
            self.target.hp = self.target.hp - self.damage * 2 # Вычитаем из HP урон
            print(f"{self.name} двойная атака -> {self.target.name} на {self.damage*2} урона. У {self.target.name} HP:{self.target.hp}")
        else:
            print("Себя нельзя атаковать")

class Archer(Character):
    """Класс лучник"""
    def __init__(self,name,hp,damage,arrows):
        super().__init__(name,hp,damage)
        self.arrows = arrows # Стрелы
    def shoot(self,target):
        if self.arrows > 0:
            self.target.hp = self.target.hp - self.damage
            print(f"{self.name} Стреляет - > {self.target.name} на {self.damage} урона. У {self.target.name} HP: {self.target.hp} ")
        else:
            print(f"Cтрел: {self.arrows} - атаки нет")
warrior1 = Warrior("Артур",100,50,50)
warrior2 = Warrior("Искандер",100,20,30)

mage = Mage("Мерлин",120,10,15)
arr = Archer("Кеша",80,15,0)
arr.info()
warrior1.info()
mage.info()


mage.attack(warrior1)
warrior1.block()
warrior1.info()
warrior1.attack(mage)
mage.cast_spell(warrior1)
arr.shoot(warrior1)