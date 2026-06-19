"""Треккер расходов"""
import json

path_file = "expenses.json"

#Шаблон json файла
samples = {
    "expenses": [
        {"category": "еда", "amount": 500, "note": "продукты"},
        {"category": "транспорт", "amount": 150, "note": "метро"}
    ]
}

def write_file():
    with open(path_file,"r",encoding="utf-8") as file:
        data = json.load(file
                         )


try:
    with open(path_file,"r",encoding="utf-8") as file:
        data = json.load(file)
    print(f"Файл: {file} - открыт и прочитан")
    is_json = True
except FileNotFoundError:
    print(f"Файл: {path_file} не найден")
    is_json = False
except json.JSONDecodeError:
    print(f"Файл поврежден или не JSON")
    is_json = False

if not is_json:
    creat_json = str(input("Создать файл? Да/Нет: "))
    if creat_json == "Да":
        with open(path_file,"w", encoding="utf-8") as file: # Создали JSON файл по шаблону
            json.dump(samples,file,ensure_ascii=False,indent=4)
            print(f"Файл: {path_file} - создан")
        with open(path_file,"r",encoding="utf-8") as file:
            data = json.load(file)
    else:
        print("Досвиданиея!")
        exit()

def sow_menu():
    menu_items = {
        "Список": "Показать все расходы",
        "Добавить": "Добавить расход",
        "Итого": "Показать сумму для каждой категории",
        "Выход": "Выход"

    }

    print("+-----------------------------------------------+")
    print("!         МЕНЮ ДОСТУПНЫХ КОМАНЛ                 !")
    print("+-----------------------------------------------+")
    for cmd, desc in menu_items.items():
        # Форматируем строку: левая часть шириной 10 символов, правая — в остаток
        text = f" [{cmd}]  {desc}"
        print(f"! {text.ljust(45)} !")
    print("+-----------------------------------------------+")

def write_file(): #Функция пишет в файл
    with open(path_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
#Команды ввода
_exit = "Выход"

sow_menu()
write_file()
# print(json.dumps(data,ensure_ascii=False,indent=4))

while True:
    n = input("Команда: ")
    if n == _exit:
        print("Досвидания!")
        break




