# class MyContext:
#     def __enter__(self):
#         print("Вход в контекст")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Выход из контекста")
#         return self
#
# with MyContext():
#     print("Работаем внутри контекста")
import time



# file_path = "notes.txt"
# text = "Изучаю Python\nИзучаю контекстные менеджеры\nУчусь работать с файлами\n"
# try:
#     with open(file_path,"r",encoding="utf-8") as file:
#         data = file.read()
#         print(10/0)
# except ZeroDivisionError:
#     print("Деление на ноль")
#
# print(file.closed)


# class TrainingContext:
#     def __enter__(self):
#         print("Вход в контекст")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Выход из контекста")
#
#         if exc_type is ZeroDivisionError:  # Если тип ошибки деление на ноль
#             print(f"Обработана ошибка {exc_val}")
#             print(f"Тип ошибки: {exc_type}")
#             print(f"Значение: {exc_tb}")
#             return True # Подавляем ошибку
#         return False
#
#
# with TrainingContext():
#     print("Выполняется основной код")
#     10 / 0
#     print("Эта строка не выполнится") #Это строка не выполниться так как есть ошибка with прекратил работу
# print("Продолжаем работу")




# class FileManager:
#
#     def __init__(self, path: str, mode: str):
#         """Метод инициализации экземпляра"""
#         self.path = path  # Путь файл
#         self.mode = mode  # Режим (чтение, запись)
#         self.file = None
#
#     def __enter__(self):
#         """Вход в контекст"""
#         self.file = open(self.path, self.mode, encoding="utf-8")  # Открываем файл
#         return self.file  # Вернём файл
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Выход из контекста"""
#         self.file.close()
#         print(f"Файл закрыт: {self.file.closed}")
#         return False # Не подавляем ошибки
#
# try:
#     with FileManager(path_file, "w") as f:
#         f.write("Проверка закрытия файла при ошибки")
#         10 / 0
# except ZeroDivisionError as err:
#     print(f"{err}")
#
# print(f.closed)
#
# import time
#
# class Timer:
#     def __enter__(self):
#         """Вход в контекст"""
#         self.start = time.perf_counter()
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Выход из контекста"""
#         self.stop = time.perf_counter()
#         self.res = self.stop - self.start
#         # print(f"Время выполнения {self.res:.2f}")
#         # return self.res
#         return False
#
# with Timer() as timer:
#     sum(range(10_000_000))
#
# print(f"Время выполнения {timer.res}")

# file_path = "example.txt"
# encoding = "utf-8"
#
# text = "Я изучаю контекстные менеджеры"
#
# with open(file_path, "w", encoding=encoding) as file:
#     file.write(text)
#     print(file.closed)
# print(file.closed)
#
# with open(file_path, "a", encoding=encoding) as file:
#     file.write("\nФайл закрывается автоматически")
#     print(file.closed)
# print(file.closed)
# try:
#
#     with open(file_path, "r", encoding=encoding) as file:
#         data = file.read()
#         10 / 0
# except ZeroDivisionError as err:
#     print("Деление на ноль запрещёно")
# print(data)
# print(file.closed)

#
# class MyContext:
#     """Класс мой контекст"""
#
#     def say_hello(self):
#         """Метод вернет текст по вызову метода"""
#         print(f"Привет из контекстного менеджера")
#
#     def __enter__(self):
#         print("Вход в контекст")
#         return self  # Верни экземпляр
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#
#         print("-------------------")
#         print(f"Тип ошибки: {exc_type}")
#         print(f"Описание ошибки: {exc_val}")
#         print(f"Traceback: {exc_tb}")
#         print("Выход из контекста")
#
#         if exc_type is ZeroDivisionError: # Если приняли эту ошибку, подавляем её, а остальные не подавляем
#             print("Деление на ноль обработано") #
#             return True  # Подавляем ошибку
#         else:
#             return False # Не подавляем ошибки
# try:
#     with MyContext() as cont:
#         print("Начало основного кода")
#         int("Привет") # Вызываем другию не подавленную ошибку в __exit__ ошибку
#         10 / 0   # Если __exit__ вернёт True, ошибка подавится.
#             # Если вернёт False, ошибка передастся дальше.
#         print("Конец основного кода")
# except ValueError as err:
#     print(f"Ошибка обработана с наружи {err}")
#
# print("Программа продолжает работать")


# class Connection:
#     total_send_message = 0 #Счётчик успешно отправленных сообщений всех соединений
#     def __init__(self):
#         self.text = None
#         self.active = False
#         self.count_message = 0
#
#     def send_message(self,text):
#         """Метод отправки сообщения """
#         self.text = text
#         #Условие: Если коннект активный, отправим сообщение
#         #Если коннект не активный, сообщение нге отправим
#         if self.active:
#             self.count_message = self.count_message + 1  #Считаем количество успешных сообщений
#             Connection.total_send_message = Connection.total_send_message + 1 #Общее количеств сообщений
#             print(f"Сообщение № {self.total_send_message} '{self.text}' - Отправлено")
#         else:
#             print(f"Oшибка:Соединение закрыто")
#
#     def __enter__(self):
#         """Открывает соединение."""
#         self.active = True # Соединение активно
#         print(f"Соединение открыто")
#         return self # Верни экземпляр
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Закрывает соединение."""
#         self.active = False # Устанавливаем соединение в закрытое состояние
#         print(f"Соединение закрыто")
#         return False # не подавляем ошибки
#
#
# with Connection() as connect: #Открываем контекстный менеджер.
#     print(connect.active)
#     connect.send_message("Привет мир")
#     connect.send_message("Привет Python")
#     connect.send_message("Прощай QA")
# print(connect.active)
# connect.send_message("Второе сообщение")
#
# with Connection() as connect:
#     print(connect.active)
#     connect.send_message("Привет другой мир")
#
# connect1 = Connection()
# with connect1:
#     connect1.send_message("Новое сообщение")
# print(connect1.total_send_message)
# print(connect1.count_message)
# print(connect1.total_send_message)


# class FileManager:
#     def __init__(self, file_path, mode):
#         self.file_path = file_path
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(
#             self.file_path,
#             self.mode,
#             encoding="utf-8"
#         )
#         print("Файл открыт")
#         return self.file # Вернём открытый файл
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Выход из контекста"""
#         self.file.close() # Закрываем файл
#         print("Файл закрыт")
#         if exc_type is not None: # Условие: Если тип ошибки не пустой (то-есть какая-то ошибка)
#             print(f"Во время работы возникла ошибка:{exc_type.__name__}") # Выводим имя типа ошибки
#             print(f"Описание ошибки: {exc_val}")
#         else:
#             print(f"Записали в файл без ошибок") #Иначе выводим
#
#         return False #Не подавляем ошибки
#
#
# try:
#     with FileManager("message.txt", "w") as file:
#         file.write("Текст до возникновения ошибки\n")
#         print(f"Файл закрыт до ошибки: {file.closed}")
#
#         # 10 / 0
#
#         file.write("Этот текст не запишется")
#
# except ZeroDivisionError as error:
#     print(f"Ошибка обработана снаружи: {error}")

# print(f"Файл закрыт после ошибки: {file.closed}")


# class Timer:
#     def __enter__(self):
#         self.start = time.perf_counter()
#         print(f"Таймер запушен  {self.start}")
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end = time.perf_counter()
#         print(f"Таймер остановлен {self.end}")
#
#         self.exec = self.end - self.start # Вычисляем разницу запуска и остановки
#         print(f"Время выполнения {self.exec:.5f}")
#         return False # Не подавляем ошибки
#
#
# with Timer() as execution:
#     tot = sum(range(10_000_000))
#
# print(f"{execution.start}")
# print(f"{execution.end}")
# print(f"{execution.exec}")


# from contextlib import contextmanager
#
# @contextmanager
# def training():
#     print("Тренировка началась")
#
#     yield
#
#     print("Тренировка закончилась")
#
# with training():
#     print("Выполнение упражнения")


# from contextlib import contextmanager
#
#
# @contextmanager
# def training():
#     print("Тренировка началась")
#
#     try:
#         yield "Гантели" #
#     finally:
#         print("Тренировка закончилась")
#
#
#
# try:
#     with training() as equipment:
#         print(f"Используем: {equipment}")
#         10 / 0
# except ZeroDivisionError:
#     print("Ошибка обработана")


# @contextmanager
# def open_file(file_path, mode):
#     print("Открываем файл")
#     file = open(file_path, mode, encoding="utf-8")
#
#     try:
#         yield file # Открытый файл
#     except Exception as error:
#         print(f"Внутри контекстного менеджера возникла ошибка: {type(error).__name__}")
#         # raise # Тут мы пробрасываем исключение
#     finally:
#         file.close()
#         print("Файл закрыт")
#
#
#
# try:
#     with open_file("message.txt", "w") as file: # Открываем файл
#         file.write("Изучаю @contextmanager") # Пишем файл
#         10 / 0
#         print(f"Файл закрыт внутри with: {file.closed}") # Файл открыт
#
# except ZeroDivisionError: # Даже при ошибке finally закрыл файл
#     print("Ошибка")
#
# #При выходе из with файл сам зарывается




# @contextmanager
# def connection():
#     print("Соединение открыто (работаем с потоком данных)") #Вход в контекст(открываем соединение)
#
#     try:
#         yield "Сервер VPS" #1. yield передаст значение в as. 2. Остановит функцию на паузу, начнётся выполнение внутри with
#
#     #Тут исключения
#
#     except ValueError as error: #Передали не валидные данные
#         print(f"Ошибка данных: {error}")
#         # ValueError подавляем т.к нет raise
#
#     except Exception as error: #Скоуп всех исключений
#         print(f"Неизвестная ошибка: {type(error).__name__}") # Выведем тип ошибки, имя ошибки
#         raise # Пробросим исключения дальше (но программа упадёт с ошибкой) что бы внешний блок мог её поймать. Если не напишем raise, то подавим ошибку из вне (программа выполниться)
#     # Тут выход из контекста
#     finally: # Выполниься в любом исходе( есть ошибка или нет), поработали с данными или нет, закрой коннект
#         print("Соединение закрыто (автоматически закроем коннект после выхода из with)")
#
#
# try:
#     with connection() as server: # Тут работает сам контекстный менеджер server принимает значени из yield
#         print(f"Работаем с: {server}") #Работаем внутри with
#         10 / 0
# except ZeroDivisionError as err:
#     print(f"Ошибка обработана снаружи внутри with: {err}")


# @contextmanager
# def database_connection():
#     print("Подключение к базе данных открыто")
#
#     try:
#         yield "База данных"
#         # 1. Передаём строку в database после as
#         # 2. Ставим функцию на паузу
#         # 3. Выполняем блок with
#
#     except ValueError as error:
#         print(f"Ошибка данных: {error}")
#         raise # Отловили ошибку, что-то сделали (выведи принт или легировали) и передали дальше
#
#     except Exception as error:
#         print(f"Неизвестная ошибка: {type(error).__name__}")
#         raise  # Пробрасываем ошибку дальше
#
#     finally:
#         # В не зависимости от результата(были или небыли исключения - закрываем коннект)
#         print("Подключение к базе данных закрыто")
#
#
# try:
#     with database_connection() as database:  # Менеджер контекста запущен, database = Отправили
#         print(f"Работаем с: {database}")
#         result = 4 + "4"  # переменной присваиваем строковое значение инт типа(так не работает)
# except TypeError as err:
#     print(f"Ошибку поймали с наружи {err}")# Ошибку ловит внешний except, а не блок with
#
# print("Программа завершила")





# @contextmanager
# def config_manager():
#     print(f"Конфигурация загруженная")
#     try:
#         yield {"host": "localhost", "port": 8080}  # Передали словарь, ставим паузу, выполняем блок with.
#
#     except KeyError as kerr:
#         print(f"Параметр: {kerr} не найден") #Отлавливаем ошибку внутри
#         # raise -если передать то ошибка не подавиться
#
#     except Exception as error:
#         print(f"Не известная ошибка: {type(error).__name__}")  # Выполнили действие с ошибкой
#         raise  # Передадим ошибку дальше
##
#     finally:
#         print(f"Конфигурация закрыта")

# with config_manager() as config:
#     print(f"Хост: {config['host']}")
#     print(f"Пароль:{config['password']}")
#
#
# print("Программа продолжает работать")  # Продолжаем работать, так как отловили исключение KeyError

# @contextmanager
# def bank_transaction():
#     print(f"Транзакция начата")
#
#     try:
#         yield "Счёт клиента"
#
#         # Эта строка выполнится только в случае,
#         # если блок with завершился без ошибки
#         print("Транзакция подтверждена")
#
#     except ValueError as v_err:
#         print(f"Транзакция отклонена: {v_err}")
#
#     finally:
#         print("Транзакция завершена")
#
# balance = 1000
# with bank_transaction() as account:
#     print(f"Работаем со счётом: {account}")
#     amount = int(input("Введите сумму: "))
#     if amount <= 0:
#         print(f"Баланс: {balance}")
#         raise ValueError("Сумма снятия меньше нуля")
#
#     elif amount > balance:
#         print(f"Баланс: {balance}")
#         raise ValueError("Сумма снятия больше баланса")
#
#     else:
#         balance = balance - amount
#         print(f"Переводим: {amount} рублей")
#         print(f"Баланс: {balance}")
#
# print("Программа продолжает работу")


from contextlib import contextmanager

from io import UnsupportedOperation

# filename = report.txt
@contextmanager
def open_report(filename: str,mode: str): # Функция принимает имя файла и режим
    all_modes = ("a","w","r") # Сохраняем все доступные моды в кортеж
    file = None # Создали переменную файла

    if mode not in all_modes:
        raise ValueError(f"Недопустимый режим: {mode}")


    try: # Открываем файл с проверкой

        file = open(filename,mode,encoding="utf-8") # Открываем файл
        print(f"{filename} - Открыт")

        yield file #Передаём открытый файла



        print(f"Отчёт: в {file.name} добавлен текст") # Выводим если нет ошибок

    except UnsupportedOperation as no_mode_error:
        print(f"Операция не поддерживается: {no_mode_error}")

    except PermissionError as pr_err:
        print(f"Нет доступа: {pr_err}")
        #Подавим исключение
        if file is None:  # Если файл не открылся
            raise  # Передадим ошибку наружу

    except ValueError as vl_err:
        if file is None:
            raise

        print(f"Ошибка сохранения: {vl_err}")



    finally: # Всегда выполняем
        if file is not None: # если файл открыт
            file.close() # Закрываем файл
            print(f"Файл: {file.name} закрыт {file.closed}")
            print("Сохранение завершено")
        else:
            print(f"Файл не удалось закрыть")

try:
    mode = "r"
    with open_report("report.txt",mode) as file:

        if mode == "r":
            data = file.read()
            print(f"Содержимое файла:\n{data}")

            print(f"Позиция после чтения: {file.tell()}")

            file.seek(0)
            print(f"Позиция после seek(0): {file.tell()}")

            first_line = file.readline()
            print(f"Первая строка: {first_line.strip()}")


        else:
            text = input("Ведите текст: ")

            if not text.strip():
                raise ValueError(f"Нельзя записать пустой текст в файл {file.name}")

            if len(text) > 30:
                raise ValueError(f"Текст не должен превышать 30 символов")

            else:
                file.write(text + "\n")


except ValueError as mode_err:
    print(f"Не доступный режим: {mode_err}")

except FileNotFoundError as error:
    print(f"Не удалось открыть отчёт: {error}")

print("Продолжаем выполнение программы")



# try:
#     with open_report("report.txt","a") as file:
#         text = input("Ведите текст: ")
#         if not text.strip():
#             raise ValueError(f"Нельзя записать пустой текст в файл {file.name}")
#         if len(text) > 30:
#             raise ValueError(f"Текст не должен превышать 30 символов")
#
#         else:
#             file.write(text + "\n")
# except ValueError as mode_err:
#     print(f"Не доступный режим: {mode_err}")
# print("Продолжаем выполнение программы")
#
# try:
#     with open_report("report.txt", "r") as file:
#         file.write("Новый текст\n")


# except ValueError as mode_err:
#     print(f"Не доступный режим: {mode_err}")
# print("Программа продолжает работу")
