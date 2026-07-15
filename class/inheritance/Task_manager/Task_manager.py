import json


class TaskManager:
    """Класс Менеджер задач"""
    def __init__(self,file_path):
        self.file_path = file_path
        self.tasks= []

    def add_task(self,title,priority):
        """ Метод добавляет задачу"""
        new_id = len(self.tasks) + 1 # Длинна словопря + 1 получаем ID
        task = Task(new_id,title,priority ) #<- Создаём объект
        self.tasks.append(task) #< - в список добавляем объект

    def save(self):
        """Метод сохраняет в файл"""
        with open(self.file_path,"w",encoding="utf-8") as f:
            lst = []
            for task in self.tasks:
                lst.append(task.to_dict()) # <- в список добавляем вызов метода
            json.dump(lst,f, ensure_ascii=False,indent=4)

    def load(self):
        """Метод читает файл"""
        with open(self.file_path,"r",encoding="utf-8") as f:
            data = json.load(f)
        self.tasks = [Task(**tsk) for tsk in data] # <- Распаковываем в словарь и пишем в список

    def done_task(self,id):
        found = False
        for tsk in self.tasks:
            if tsk.id == id:
                tsk.done = True
                found = True
                print(f"Задача {tsk.title} - Выполнена ✅")
                self.save()
        if not found:
            print("Нет такой задачи")

    def info(self):
        """Метод выводит все задачи"""
        for task in self.tasks:
            status = "✅" if task.done else "❌"
            print(f"{status} [{task.id}] | {task.title} |  {task.priority}")

    def find_by_priority(self,priority):
        found = False
        for task in self.tasks:
            if task.priority == priority:
                status = "✅" if task.done else "❌"
                print(f"{status} [{task.id}] | {task.title} |  {task.priority}")
                found = True
        if not found:
            print(f"Нет такого {priority} статуса задач")


class Task:
    """Класс задача"""
    def __init__(self,id,title,priority,done = False):
        self.id = id
        self.title = title
        self.priority = priority
        self.done = done

    def to_dict(self):
        """Метод объект в словарь"""
        self.dst = {"id":self.id,"title":self.title,"priority":self.priority,"done":self.done}
        return self.dst


tm = TaskManager("tasks.json")
tm.add_task("Тест","Высокий")
tm.add_task("Тест2","Высокий")
tm.add_task("Тест3","Высокий")
tm.add_task("Тест3","Средний")
tm.add_task("Тест4","Низкий")
tm.save()
tm.done_task(2)

tm.info()
tm.load()

tm.find_by_priority("Высокий")
tm.find_by_priority("Т")