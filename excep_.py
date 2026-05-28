# try:
#     n = int(input("ВВЕДИТЕ ЧИСЛО: "))
# except ValueError:
#     print("Ввели не число")


# age = - 5
# if age < 0:
#     raise ValueError ("Возраст не может быть отрицательным")


# def safe_divide(a,b):
#     try:
#         res = a/b
#         print(res)
#     except ZeroDivisionError as z:
#         print("Деление на ноль")
#
# safe_divide(10,0)
# safe_divide(10,5)

# def input_ints():
#     try:
#         n = int(input("Введитие число:"))
#         print(f"Ввели число {n}")
#     except ValueError as e:
#         print("Вели не число", e)
#     finally:
#         print(f"Программа завершина")
#
# input_ints()


# def check_age(age):
#     if age < 18:
#         raise ValueError ("Возраст  должен быть от 18")
#     else:
#         print("Доступ разрешён")
#
# check_age(17)

def del_100():

    try:
        n = int(input("Веветдите число: "))
        res = 100 / n
        print(f"Раделили 100 на {n}, результат {res}")
    except ValueError:
        print("Ввели не число")
    except ZeroDivisionError:
        print("Делите на ноль")
    finally:
        print("Конец программы")


del_100()