lst = [{'name': 'Тузик', 'age': 3}, {'name': 'Вася', 'age': 6}, {'name': 'Муся', 'age': 4}]

del_name = "Вася"

lst = [dst for dst in lst if dst["name"] != del_name]
print(lst)