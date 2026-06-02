from pathlib import Path

from pyparsing import lineStart

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

# data = "Anna:5\nBob:3\nTom:4\nKate:2\nMax:5"
# folder = Path("students") #Название папки
# file_name = "grades.txt"
# path = folder / file_name
#
# folder.mkdir(exist_ok=True)
# path.write_text(data)
#
#
# total = 0
# cout = 0
# text_in_file = path.read_text()
# for line in text_in_file.splitlines():
#     # print(line)
#     name, grade = line.strip().split(":")
#     grade = int(grade)
#     total = total + grade
#     cout = cout + 1
# sr = total / cout
#
# print(f"Средняя оценка:{sr}")
#
# folder = Path("students")
# name_files = "grades.txt"
# name_files_2 = "good_students.txt"
# path = folder / name_files
# path_2 = folder / name_files_2
#
# folder.mkdir(exist_ok=True)
#
#
#
# print(folder.is_dir())
#
# good_line = []
# texts = path.read_text()
#
# for line in texts.splitlines():
#     name, grade = line.split(":")
#     if int(grade) == 4:
#         print(f"{name} - Хорошё")
#         good_line.append(f"{name} - Хорошё")
#
#     elif int(grade) == 5:
#         good_line.append(f"{name} - Отлично")
#         print(f"{name} - Отлитчно")

#
# print(good_line)
#
# path_2.write_text("\n".join(good_line))


#Создаём лог файл
# data = "INFO:Start\nERROR:File not found\nINFO:Continue\nERROR:Timeout\nINFO:Finish"
data = """ERROR:File not found
ERROR:Timeout
ERROR:Timeout
ERROR:File not found
ERROR:Timeout"""

folder_name = Path("logs")
file_name = "logs.log"
file_error = "error.txt"
path = folder_name / file_name
path_error = folder_name / file_error
#Проверяем есть ли директория

if folder_name.is_dir():
    print(f"Директоря: {folder_name} существует")
else:
    print(f"Директория не сущестовует, создаю директорию: {folder_name}")
    folder_name.mkdir()


# try:
#     with open(path,"x") as file: #Создаем файл
#         pass #Пустой
#         print(f"Файл: {file_name} - создан")
# except FileExistsError:
#     print(f"Фаил: {file_name}  существует", "------------", sep="\n")

path.write_text(data) # Пишем в файл logs.log

text_log = path.read_text()
count_error = 0
count_info = 0
error_lst = []
status = {}
for line in text_log.splitlines():
    level, message = line.split(":")
    if level == "ERROR":
        count_error = count_error + 1
        if message in status:
            status[message] = status[message] + 1
        else:
            status[message] = 1

print(f"Количесто ERROR: {count_error}")
print(error_lst)
print(status)


path_error.write_text("\n".join(error_lst))
path_error.write_text()
print(f"Записали в файл /{path_error}: {count_error} ошибки")























