import json



def show_menu():
    print("+--------------------------------------+")
    print("!         МЕНЮ ДОСТУПНЫХ ОПЕРАЦИЙ      !")
    print("+--------------------------------------+")
    print("!  [Список] Показать все задачи        !")
    print("!  [Добавить]  Добавить задачу         !")
    print("!  [Готово]  Отметить выполненой по id !")
    print("!  [Выход]  Выход                      !")
    print("+--------------------------------------+")


show_menu()

with open("todo.json","r",encoding="utf-8") as file:
    data = json.load(file)

# print(data)
# print(json.dumps(data,indent=1,ensure_ascii=False))

list_task = "Список"
set_done = "Готово"

done_false = "[ ]"
done_true = "[✓]"

while True:
    n = input("Введите команду: ")
    if n == list_task:
        for i in data['tasks']:
            if i.get('done') is False:
                print(f"{i['id']}. {done_false} {i['task']}")
            elif i.get('done') is True:
                print(f"{i['id']}. {done_true} {i['task']}")
    elif n == set_done:
        # Добавить если нет id
        _id = int(input("Введите id задачи: "))
        for i in data['tasks']:
            if i.get('id') == _id:
                i["done"] = True
                with open("todo.json","w",encoding="utf-8") as file:
                    json.dump(data,file,ensure_ascii=False, indent=4)

            # else:
            #     print("Такого id нет!")


