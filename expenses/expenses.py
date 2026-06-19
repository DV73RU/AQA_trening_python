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
list_expenses = "Список"
add_expenses = "Добавить"
total = "Итого"
sow_menu()

# print(json.dumps(data,ensure_ascii=False,indent=4))

while True:
    n = input("Команда: ")
    if n == _exit:
        print("Досвидания!")
        break
    elif n == list_expenses:
        lst_data = data['expenses']
        for lst in lst_data:
            # print(lst)
            category = lst['category']
            amount = lst['amount']
            note = lst['note']
            print(f"{category}: {note} - {amount}")
    elif n == add_expenses:
        add_category = input("Введите категорию: ")
        add_note = input("Введите название: ")
        add_amount = int(input("Введите цену: "))
        lst_data = data['expenses']
        lst_data.append({"category":add_category,"amount":add_amount, "note":add_note})
        write_file()
        print("Добавлено")
    elif n == total:
        lst_data = data['expenses']
        res = 0
        totals = {}
        for i in lst_data:
            # res = 0
            amm = i["amount"]
            category = i["category"]
            if category not in totals:
                totals[category] = 0
            totals[category] = totals[category] + amm
            res = res + amm
        totals['Всего'] = res
        max_key_len = max(len(str(key)) for key in totals.keys())
        # min_key_len = min(len(str(key)) for key in totals.keys())
        for key, val in totals.items():

            key = f"{key}:"
            print(f"{key.ljust(max_key_len+2)} {val} руб.")

        # print(totals)



    else:
        print("Команада не найдена!")




