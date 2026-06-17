import json
from datetime import datetime

def sow_menu():
    menu_items = {
        "Список": "Показать все задачи",
        "Добавить": "Добавить задачу",
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



file_path = "diary.json"

with open(file_path, "r", encoding="utf-8") as f:
    datas = json.load(f)

sow_menu()

list_entries = "Список"
add_entries = "Добавить"
_exit = "Выход"

# total_entries = len(datas["entries"])




while True:
    n = input("Команда: ")
    if n == list_entries:
        for num, entries in enumerate(datas["entries"],start=1):
            # print(entries)
            date_str = entries['date']
            date_form = "["+date_str+"]"
            # date = datetime.strftime(date_str,"%Y-%m-%d %H:%M")
            text = entries['text']
            print(f"{num}.{date_form} {text}")
    elif n == add_entries:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_entries = input("Запись: ")
        # for entries in datas['entries']:
        datas['entries'].append({'date':date_now,"text":new_entries})
        with open("diary.json","w",encoding="utf-8") as f:
            json.dump(datas,f,ensure_ascii=False,indent=4)
            print("Сохранено!")
    elif n == _exit:
        break

    else:
        print(f"Команда {n} - не найдена")






