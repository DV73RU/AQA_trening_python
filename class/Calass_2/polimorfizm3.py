class ConsoleReporter:
    def save(self,result):
        return f"{__class__.__name__} выведен {result} в консоль"

class FileReporter:
    def save(self,result):
        return  f"{__class__.__name__} сохранён {result} в файл"


result = "TestSuit - Run..."
consol_reporter = ConsoleReporter()
file_reporter = FileReporter()

list_report = [consol_reporter,file_reporter]
for reports in list_report:
    print(reports.save(result))