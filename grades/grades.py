import json
import os

samples = {
    "students": [
        {"name": "---", "grades": []},
        {"name": "---", "grades": []}
    ]
}

def clear_consol():
    os.system('cls' if os.name == 'nt' else 'clear')

path_file = "grades.json"

try:
    with open(path_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("Файл успешно открыт и прочитан")
    is_json = True
except FileNotFoundError:
    print("Файл не найден!")
    is_json = False

except json.JSONDecodeError:
    is_json = False
    print("Файл не JSON или повреждён")

if not is_json:
    js = input("Создать файл ? Да/Нет: ")
    if js == "Да":
        with open(path_file,"w", encoding="utf-8") as file:
            json.dump(samples,file,ensure_ascii=False,indent=4)
        with open(path_file,"r",encoding="utf-8") as file:
            data = json.load(file)
    else:
        print("Доствидания")
        exit()



def sow_menu():
    menu_items = {
        "Список": "Показать список учеников",
        "Добавить": "Добавить оценку ученику",
        "Найти": "Поиск по имени",
        "Выход": "Выход"

    }

    print("+--------------------------------------+")
    print("!         МЕНЮ ДОСТУПНЫХ КОМАНЛ        !")
    print("+--------------------------------------+")
    for cmd, desc in menu_items.items():
        # Форматируем строку: левая часть шириной 10 символов, правая — в остаток
        text = f" [{cmd}]  {desc}"
        print(f"! {text.ljust(36)} !")
    print("+--------------------------------------+")

def write_file(): #Функция пишет в файл
    with open(path_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

list_students = "Список"
add_grades = "Добавить"
_exit = "Выход"
found_name = "Найти"
total = "Итого"

count_stud = len(data['students'])
sow_menu()

while True:
    n = input("Команда: ")

    if n == found_name:
        in_name_ = input('Имя: ')
        found = False
        for names in data['students']:

            name = names['name']
            grades = names['grades']
            res = sum(grades)
            average = res / len(grades)
            if in_name_ in name:

                print(f"{name} | оцентка:{grades} | средний бал: {average}")
                found = True
        if not found:
            print(f"Такое имя: {in_name_} не найдено")



    elif n == _exit:
        print("Доствидания !")
        break
    elif n == list_students:
        for num, stud in enumerate(data['students'],start=1):
            name = stud['name']
            grades = stud['grades']
            res = sum(grades)
            try:
                average = res / len(grades)
            except ZeroDivisionError:
                # print("Оценок нет")
                average = "Нет оценок"

            print(f"{num}. {name + (' ' *(7-len(name)))} | оцентка:{grades} | средний бал: {average}")


    elif n == add_grades:
        int_name = input("Имя: ")
        # int_grade = int(input("Оценка: "))
        grades = []
        found = False
        for lst in data['students']:
            name = lst['name']
            grades = lst['grades']
            if int_name in name:
                found = True
                print(f"Такое {name} есть в списике, добавим {name} оценку")
                int_grade = int(input("Оценка: "))
                grades.append(int_grade)

                write_file()

        if not found:
            print(f"Нет такого имени {int_name}, создаю нвую запись")
            int_grade = int(input("Оценка: "))# Если есть такое имя добавь ему оценку, если нет создай новое имя и добавь оценку
            data['students'].append({"name":int_name,"grades":[int_grade]})

            write_file()



    else:
        print(f"НЕТ такой команды : {n}")
        # clear_consol()
        sow_menu()

