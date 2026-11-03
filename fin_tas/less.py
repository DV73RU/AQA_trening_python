from abc import ABC, abstractmethod


class BaseTest(ABC):
    def __init__(self, name):
        self.name = name
        self.status = "PASSED"

    @abstractmethod
    def run(self):
        pass


class Screenshotable(ABC):
    """Класс делает скриншоты"""

    @abstractmethod
    def take_screenshot(self):
        pass


class UiTest(BaseTest, Screenshotable):
    def run(self):
        self.status = "PASSED"  # Захардкодим статус теста
        return self.status  # Верни статус тесте

    def take_screenshot(self):
        print("Скриншот сохранён")


class MobileTest(BaseTest, Screenshotable):
    def run(self):
        self.status = "FAILED"
        return self.status

    def take_screenshot(self):
        print("Скриншот сохранён")


class ApiTest(BaseTest):
    def run(self):
        self.status = "FAILED"  # Захардкодим статус теста
        return self.status  # Верни статус  теста


class DB(BaseTest):
    def run(self):
        self.status = None
        return self.status


class BaseSender(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class TelegramSender(BaseSender):
    def __init__(self, id_chat):
        self.id_chat = id_chat

    def send(self, message: str):
        print(f"[Telegram к {self.id_chat}]: {message}")


class EmailSender(BaseSender):
    def __init__(self, email: str):
        self.email = email

    def send(self, message: str):
        print(f"[Email к {self.email}]: {message}")


class TestRunner:
    def __init__(self, tests: list[BaseTest], sender: BaseSender):  # Передаём список тестов для запуска и отправителя
        self.tests = tests
        self.sender = sender

    def notify_failed(self, test: BaseTest):
        msg = f"Прогон теста: {test.name} вернул: {test.status}"
        try:
            self.sender.send(msg)
        except RuntimeError as err:
            print(f"Не удалось отправить сообщение: {err}")

    def run(self,test:BaseTest): # Принимает экземпляр конкретного теста
        # 1. Проверка коннекта - установка статус теста в FAILED
        # 2. Если результат в недопустимых значения ("FAILED", "PASSED")
        # 3. Если статус None
        # 3. Отправка в sender если статус теста вернул FAILED
        # 4. Если наследник Screenshotable делаем скриншот
        try:
            result = test.run() #Тут мы запускаем метод run у переданного теста
        except ConnectionError as err:
            print(f"API Не доступен {err}")
            result = "FAILED"
            test.status = result

        if result not in ("FAILED", "PASSED"):  # Ели результ не в допустимых значениях
            raise ValueError(f"Пришло не допустимое значение  {result}")  # Выброси ошибку
        elif result == "FAILED":  # Если результат запуска тесте вернул FAILED
            test.status = result
            # self.notify_failed(test) # Отправляем сообщение

            if isinstance(test, Screenshotable):  # Если переданный тест наследник Screenshotable
                try:
                    test.take_screenshot()  # То делай скрин выполняя у него метод take_screenshot
                except (OSError, ValueError) as err:
                    print(f"Ошибка создание скриншота {str(err)}")

        return result

    def run_all(self):
        # 1. Запуск каждого теста через метод run TestRunner в списке
        # 2. Запись в список результатов
        res_list = []
        for test in self.tests:  # Пройдёмся по списку тестов переданного в экземпляр ранера
            try:
                result = self.run(test) # Тут нужно запустить run у экземпляра класса TestRuner (не путать run с методом у теста)
            except ValueError as err: # Перехвати ошибку не венного значения статуса
                print(f"{err}") # Выведи сообщение об перехваченной ошибки
                test.status = "FAILED"
                result = "FAILED"
                # self.notify_failed(test)
            except Exception as err:
                # ЗАЩИТА: перехватываем любые другие ошибки из test.run(),
                # чтобы один упавший тест не ломал весь цикл run_all
                print(f"Тест {test.name} упал с критической ошибкой: {err}")
                test.status = "FAILED"
                result = "FAILED"
            if result == "FAILED":
                test.status = "FAILED"
                self.notify_failed(test)

            res_list.append(result) # Добавь значение результатов в список результатов
        return res_list

    def get_statistics(self,result:list) -> dict[str,int]: #Примет список результатов теста (а где их взять?)
        # 1. Выполнить метод запуска который вернёт нам этот список
        # 2.
        """
        Метод вернёт статистику словарём
        {
        "total": 5,
        "passed": 3,
        "failed": 2
        }
        """
        dst = {"total":0,"passed":0,"failed":0}
        total = len(result) #Всего элементов в списке
        passed = result.count("PASSED")
        failed = result.count("FAILED")
        dst["total"] = total
        dst["passed"] = passed
        dst["failed"] = failed
        return dst

api = ApiTest("login")
ui = UiTest("to_card")
db = DB("del_user")

tel_send = TelegramSender("id_admins")
mail_send = EmailSender("admin@test.com")
list_tests = [api, ui, db]




run1 = TestRunner(list_tests, tel_send)
# print(run1.run(api))
# res = run1.run_all()



# print(run1.get_statistics(res))
# print(run1.run(api))
# print(run1.run(ui))
# print(run1.run(db))

print(run1.run_all())