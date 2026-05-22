numbers = {10, 20, 30, 40}
numbers.add(50)
numbers.remove(20)
numbers.discard(100)
print(numbers)

users = {"Anna", "Bob", "Tom", "Kate"}

if "Tom" in users:
    print("Пользователь найден")
else:
    print("Пользователь не найден")

# Люди которые есть в обеих группах
group_1 = {"Anna", "Bob", "Tom", "Max"}
group_2 = {"Tom", "Kate", "Bob", "Alex"}

res = group_1 & group_2
print(res)

python_students = {"Anna", "Bob", "Tom"}
java_students = {"Tom", "Kate", "Max"}

res = python_students | java_students
print(f"Все студенты: {res}")
print(f"Учат питон: {python_students}")
#5
shop_1 = {"milk", "bread", "apple", "cheese"}
shop_2 = {"bread", "banana", "cheese", "orange"}

res = shop_1 ^ shop_2
print(res)