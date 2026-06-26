class Employee:
    """Класс сотрудники"""
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"Имя: {self.name} | Зарплата {self.salary}",end="")

    def get_bonus(self):
        bonus = 0.1
        print(f"Бонус {self.name}: {self.salary*bonus}")
        self.salary = self.salary + self.salary * bonus


class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language = language

    def code(self):
        print(f"{self.name} пишет на {self.language}")

    def info(self):
        super().info()
        print(f" | язык {self.language}")

class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size

    def get_bonus(self):
        bonus = 0.2
        print(f"Бонус {self.name} : {self.salary*bonus}")
        self.salary = self.salary+self.salary * bonus

    def info(self):
        super().info()
        print(f" | команда из {self.team_size} чел.")

class Designer(Employee):
    def __init__(self, name,salary,tool):
        super().__init__(name,salary)
        self.tool = tool

    def design(self):
        print(f"Дизайнер {self.name} работает в {self.tool}")

    def info(self):
        super().info()
        print(f" | Инструмент {self.tool}")


dev = Developer("Иван",10000,"Python")
mgr = Manager("Дмитрий",9000,10)
dgr =Designer("Артур",9800,"Figma")

dev.info()
mgr.info()
dgr.info()

dev.get_bonus()
dev.info()
mgr.get_bonus()
mgr.info()