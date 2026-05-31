#
# # with open("example.txt", "r") as f:
# #     content = f.read()
# #     print(content)
# #Подсчёт количество срок в файле
# with open("example.txt",'r') as file:
#     lines = file.readlines()
#     count = 0
#     print(lines)
#     # for i in range(len(lines)):
#     #     count += i
#     # print(count)
#     # print(lines)
#     # text = " ".join(item.strip() for item in lines)
#
#
#     text = " ".join(val.strip() for val in lines)
#     print(text)
#
#     lst = [i.replace('\n', '') for i in  lines]
#     print(lst)
#     lst = [i.replace('.',':') for  i in lst]
#     print(lst)
#
# ferst_line = "Первая строка\n"
# second_line = "Вторая строка\n"
# last_line = "Последующая строка\n"
# input_name_file = str(input("Введите назввание txt файла : "))
# name_file = input_name_file + ".txt"
#
# try:
#     with open(name_file,"x") as file:
#         file.write(ferst_line)
#         file.write(ferst_line)
#         print(f"В файл записано {ferst_line}, {second_line}")
# except FileExistsError:
#     print(f"Файл: {name_file} уже существует Выполняю запсиь '{last_line}' существующий файл!")
#     with open(name_file,"a") as file:
#         file.write(last_line)

#
with open("texts/note.txt","w") as file:
    file.write("Hello Python")

with open("texts/note.txt", "r") as file:
    for line in file:
        print(line.strip())
