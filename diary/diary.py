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


sow_menu()

with open("diary.json")