import copy
# #
# a= "привет"
# b = "мир"
# a,b = b, a
# #
# data = [2024, "июнь", 5, "пятница"]
# year,month, *rest = data
#
# students = [("Аня", 90), ("Боря", 75), ("Вика", 88)]
# for name, scope in students:
#
#     if name == "Боря":
#         print(f"{name} набрал {scope} баллов")
#     else:
#         print(f"{name} набрала {scope} баллов")

lst = [1, [2, 3], 4]
print(f"lts - {lst}, id(lst) - {id(lst)}, id[1] - {id(lst[1])} ")

shallow = lst.copy()
print(f"shallow - {shallow}, id(shallow) - {id(shallow)}, id[1] - {id(lst[1])}")

shallow[1].append(99)

lst.append(100)
print(f"lts - {lst}, id(lst) - {id(lst)}, id[1] - {id(lst[1])} ")

print(f"shallow - {shallow}, id(shallow) - {id(shallow)}, id[1] - {id(lst[1])}")
lst[1].append(45)
print(f"lts - {lst}, id(lst) - {id(lst)}, id[1] - {id(lst[1])} ")

print(f"shallow - {shallow}, id(shallow) - {id(shallow)}, id[1] - {id(lst[1])}")
shallow[1].append(99)
print()
print(f"lts - {lst}, id(lst) - {id(lst)}, id[1] - {id(lst[1])} ")

print(f"shallow - {shallow}, id(shallow) - {id(shallow)}, id[1] - {id(lst[1])}")