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
add_task = "Добавить"

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
    elif n == add_task:
        name = str(input("Задача: "))
        # print(data['tasks'][-1])
        last_task = data['tasks'][-1] # Последняя задача
        new_id = last_task.get('id') + 1 # Новый номер id задачи
        for i in data['tasks']:
            data['tasks'].append({"id":new_id,"task":name, "done":False})
            # print(data['tasks'])
        with open("todo.json", "w",encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii=False,indent=4)
        print("Добавлено")





            # else:
            #     print("Такого id нет!")


