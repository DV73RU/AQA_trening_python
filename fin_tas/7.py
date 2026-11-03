# from abc import ABC, abstractmethod
#
#
# class BaseReporter(ABC):
#
#     @abstractmethod
#     def generate_html(self):
#         pass
#
#     @abstractmethod
#     def send_email(self):
#         pass
#
#     @abstractmethod
#     def send_telegram(self):
#         pass
#
#
# class HtmlReporter(ABC):
#     pass
#
#
# class SendReporter(ABC):
#
#     @abstractmethod
#     def send(self):
#         pass
#
#
# class SendMail(SendReporter):
#     def __init__(self, mail: str):
#         self.mail = mail
#
#     def send(self, message: str):
#         print(f"Отправили на Email:{self.mail} - {message} ")
#
#
# class SendTelegram(SendReporter):
#     def __init__(self, id_chat):
#         self.id_chat = id_chat
#
#     def send(self, message: str):
#         print(f"Отправили в чат: {self.id_chat} - {message}")
#
#
# class ReportService:
#     def __init__(self, message: str, transport: SendReporter):
#         self.message = message
#         self.transport = transport
#
#     def send_report(self):
#         self.transport.send(self.message)
#
#
# send_mail = SendMail("admin@test.com")
# send_telegram = SendTelegram("id_234der")
#
# report_service = ReportService("'Текст отправляемого сообщения'", send_mail)
# report_service1 = ReportService("Текст в чат Телеграмм", send_telegram)
# report_service.send_report()
# report_service1.send_report()
#
#
class HtmlGenerator:
    def generate(self, results):
        return "HTML report"


class JsonGenerator:
    def generate(self, results):
        return "JSON report"


class ReportService:
    def __init__(self, generator):
        self.generator = generator

    def create_report(self,results):
        return self.generator.generate(results)

h = HtmlGenerator()
J = JsonGenerator()

rep = ReportService(h)
rep.create_report()