class Employee:
    """Класс сотрудники"""
    def __init__(self,name:str,base_salary:int):
        self.name = name
        self.base_salary = base_salary

    def info(self):
        print(f"{self.name} | Зарплата: {self.get_salary()}")

    def get_salary(self):
        return self.base_salary


class FullTime(Employee):
    """Класс сотрудники почасово"""
    def __init__(self,name:str,base_salary:int):
        super().__init__(name,base_salary)
        self.bonus = 0
        self.res = 0

    def get_salary(self):
        self.res = self.base_salary + self.bonus
        return self.res

    def add_bonus(self,amount:int):
        self.bonus = self.bonus + amount

class PartTime(Employee):
    def __init__(self,name,hours_worked,hours_rate):
        super().__init__(name,base_salary=0)
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate
        self.res = 0

    def get_salary(self):
        self.res = self.hours_worked * self.hours_rate
        return self.res

    def info(self):
        print(f"{self.name} | Зарплата: {self.get_salary()}")

class Freelancer(Employee):
    def __init__(self,name:str):
        super().__init__(name,base_salary=0)
        self.project = []
        self.res = 0

    def add_project(self,project_name,payment):
        self.project.append(payment)
        self.payment = payment
        self.res = 0

    def get_salary(self):
        return sum(self.project)


user1 = FullTime("Толя",200_000)
user2 = PartTime("Коля",8,10)
user1.info()
user2.info()


user3 = Freelancer("Галя")
user3.info()
user3.add_project("Сайт",25_000)
user3.info()
user3.add_project("Приложение",50_000)
user3.add_project("Парсер",10_000)
user3.info()