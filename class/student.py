class Student:
    """Класс сдудент"""
    def __init__(self,name):
        self.name = name # Атрибут имя
        self.grades = [] # Атрбут оценки

    def average(self):
        """Метод возвращяет средний бал"""
        return  sum(self.grades)/len(self.grades)

    def info(self):
        """Метод информации о студенте"""
        cred_ball = 0
        if not self.grades:
            print(f"{self.name} | оценки отсутствуют")
        else:
            print(f"{self.name} | оценки {self.grades} | средний бал: {self.average()}")

    def add_grade(self,n):
        """Метод добавления оценки"""
        self.grades.append(n)


stud1 = Student("Иван")
stud1.info()
stud1.add_grade(5)
stud1.info()
stud1.average()