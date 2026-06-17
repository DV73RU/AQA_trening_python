import json

def sow_menu():
    menu_items = {
        "Список": "Показать все контакты",
        "Добавить": "Добавить контакт",
        "Найти": "Найти по имени",
        "Удалить": "Удалить по id",
        "Выход": "Выход"
    }

    print("+--------------------------------------+")
    print("!         МЕНЮ ДОСТУПНЫХ ОПЕРАЦИЙ      !")
    print("+--------------------------------------+")
    for cmd, desc in menu_items.items():
        # Форматируем строку: левая часть шириной 10 символов, правая — в остаток
        text = f" [{cmd}]  {desc}"
        print(f"! {text.ljust(36)} !")
    print("+--------------------------------------+")


data = {} # ДОБАВИЛ ЕСЛИ ФАЙЛ ПУСТОЙ

file_path = "contacts.json"

try:
    with open(file_path,"r",encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError:
    print(f"Файл: {file_path} пуст или не JSON")

except FileNotFoundError:
    print(f"Файл {file_path} не найден. Создан пустой словарь.")



sow_menu()

print(json.dumps(data,ensure_ascii=False,indent=4))

count_contacts = len(data['contacts'])

#Команды
list_contacts = "Список"
add_contacts = "Добавить"
find_contacts = "Найти"
del_contacts = "Удалить"
_exit = "Выход"

while True:
    n = input("Команда: ")
    if n == list_contacts:
        for num, contact in  enumerate(data["contacts"]):
            _id = contact['id']
            name = contact['name']
            tel = contact['phone']
            print(f"{_id}. {name} - {tel}")

    elif n == add_contacts:
        # for idx in data['contacts']:
        new_num = data['contacts'][-1]['id'] + 1
        new_name = str(input("Имя: "))
        new_tel = str(input("Номер телефона: "))
        data['contacts'].append({"id":new_num,"name":new_name,"phone":new_tel})
        with open(file_path,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)

    elif n == find_contacts:
        f_n = str(input("Имя:"))
        found = False
        for idx, nam in enumerate(data['contacts']):
            name = nam["name"]
            if f_n in name:
                _id = nam['id']
                name = nam['name']
                tel = nam['phone']
                print(f"{_id}. {name} - {tel}")
                found = True
        if not found:
            print(f"Имя: '{f_n}' не найдено!") # Как работает?

    elif n == del_contacts:
        in_id = int(input("ID: "))
        data["contacts"] = [c for c in data["contacts"] if c["id"] != in_id]
        with open(file_path,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)

    elif n == _exit:
        break

    else:
        print(f"Команда {n} - не найдена")

