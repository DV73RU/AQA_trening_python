class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self,n):
        """Метод добавляет оценку студента"""
        self.grades.append(n)

    def average(self):
        """Метод вернёт средний бал"""
        count = len(self.grades)
        summa = sum(self.grades)
        if count != 0:
            return  summa/count
        else:
            return "Нет оценок"


    def info(self):
        """Метод вернёт информацию о студенте"""
        return f"{self.name},  {self.average()}"

class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject # Название предмета

    def info(self):
        return f"{self.name}  {self.subject}"

class Classroom:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def info(self):

        print(f"Класс : {self.name} , Учитель: {self.teacher.name}, | {self.teacher.subject}")
        for student in self.students:
            print(f"  {student}")

    def best_student(self):
        best = self.students[0]
        for student in self.students:
            if student.average() > best.average():
                best = student
        print(best.info())

class School:
    def __init__(self,name):
        self.name = name
        self.classrooms = []

    def add_classroom(self,classroom):
        self.classrooms.append(classroom.name)

    def info(self):
        print(f"{self.name}")



    def best_students(self):
        pass



stud1 = Student("Толя")
stud2 = Student("Анна")
stud1.add_grade(4)
stud1.add_grade(5)
stud2.add_grade(5)
stud2.add_grade(5)


teach1 = Teacher("Иванов", "Математика")
teach2 = Teacher("Петрова","Информатика")
# print(teach1.info())
# print(teach2.info())

class1 = Classroom("10A",teach1)
class2 = Classroom("10B",teach2)
class1.info()
class2.info()
class1.add_student(stud1)
class1.add_student(stud2)

class1.best_student()

sh1 = School("Школа №68")
sh1.add_classroom(class1)
sh1.add_classroom(class2)
sh1.info()