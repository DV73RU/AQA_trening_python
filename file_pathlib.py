from pathlib import Path

# path = Path("logs") / "actions.txt"

# print(path)

# folders = Path("logs_1")
#
# folders.mkdir(exist_ok=True)
#
# path = folders / "actions.txt"

# with open(path,"w") as file:
    # file.write("Привет питон")

# with open(path,"r") as file:
#     text = file.read()
#     print(text)

# path.write_text("login\nopen_page\nclick_button\n") #Пишем текст в файл
# # text = path.read_text()
#
#
# # for line in text.splitlines():
# #     print(line)
#
#
# with open(path,"a") as file: #Дописываем файл
#     file.write("send_form\n")
#     file.write("logout\n")
#
#
# with path.open("a") as file:
#     file.write("close\n")
#     file.write("exit\n")
#
# text = path.read_text()
# print(text)
# print(type(text))
#
# lst = []
#
# for line in text.splitlines():
#     lst.append(line)
# print(lst)
#
# if path.exists():
#     print("Файл существует")
#
# else:
#     print("Файла нет")
#
# print(path.is_file())
# print(path.is_dir())
#
# print(folders.is_dir())
#
# folder_2 = Path("data") / "users" / "info"
#
# folder_2.mkdir(parents=True,exist_ok=True)
#
# path = Path("logs") / "action.txt"
#
# path.mkdir(parents=True,exist_ok=True)
#
# for items in folders.iterdir():
#     print(items)

# folder = Path("shop") # Название папки.
# path = folder / "products.txt"
#
# text_write = "apple:50\nbanana:30\nmilk:100\nbread:40\ncheese:150"
#
# folder.mkdir(exist_ok=True) # Создаём директорию
#
# path.write_text(text_write) # Запишем значения в файл
#
# text = path.read_text() # Переменная принимает значение прочённого файла
# for line in text.splitlines(): # Циклом заберам посточные значения
#     name, price = line.strip().split(':') #Делим строки на название и цену
#     price = int(price) #Строку в число
#     if price > 50: #Условие
#         print(f"{name} - {price}")
#

data = "Anna:5\nBob:3\nTom:4\nKate:2\nMax:5"
folder = Path("students") #Название папки
file_name = "grades.txt"
path = folder / file_name

folder.mkdir(exist_ok=True)
path.write_text(data)


total = 0
cout = 0
text_in_file = path.read_text()
for line in text_in_file.splitlines():
    # print(line)
    name, grade = line.strip().split(":")
    grade = int(grade)
    total = total + grade
    cout = cout + 1
sr = total / cout

print(f"Средняя оценка:{sr}")

