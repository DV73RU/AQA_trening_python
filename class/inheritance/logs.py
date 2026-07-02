class Logger:
    """Класс логеер"""
    log = [] # Переменная для всех методов.
    def __init__(self,name): # Инициализация класса
        self.name = name


    def info(self,message):
        """Метод добавляет лог INFO"""
        # msg = Logger.format_message("INFO",self.name, message)
        msg = self.format_message("INFO",self.name,message)
        self.log.append(msg)

    def warning(self,message):
        """Метод добавляет в лог WARNING"""
        msg = Logger.format_message("WARNING",self.name, message)
        self.log.append(msg)


    def error(self,message):
        """Метод добавляет в лог WARNING"""
        msg = Logger.format_message("ERROR",self.name, message)
        self.log.append(msg)


    @classmethod #Метод класса
    def get_logs(cls):
        for log in cls.log: # Циклом переберем в списке значения
            print(log)


    @staticmethod # Статический метод
    def format_message(level, name,message):
        return f"[{level}] {name} | {message}"


log_app = Logger("App")
log_bd = Logger("Postgres")

log_app.info("Запуск программы")
log_app.warning("Превышен лимит")
log_app.error("Приложение не запустилось")

log_bd.info("Запись в Postgres")

Logger.get_logs()