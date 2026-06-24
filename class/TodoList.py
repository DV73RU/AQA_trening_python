class TodoList:
    """Класс Список дел"""
    def __init__(self): #инициалицация класса
        self.task = [] #Атрибут класса


    def add_task(self,text):
        """Метод класса:Добавление задачи"""
        id = len(self.task)+1 # Формируем порядковый номер id
        done = False

        tsk_dct = {"id":id,"text":text,"done":done}
        self.task.append(tsk_dct)

    def info(self):
        """Метод возвращяет"""
        status = False
        for key, val in enumerate(self.task):
            id = val["id"]
            text = val["text"]
            done = val["done"]
            status = "[✓]" if done else "[ ]"
            print(f"# {id}. {status} {text}")

    def done_task(self,id):
        """Метод устанавливает задачу выполненой"""
        for dst in self.task:
            if id == dst["id"]:
                dst["done"] = True

    def remove_task(self,_id):
        """Метод удаляет задачу"""
        self.task = [task for task in self.task if task['id'] != _id ]

my_task =TodoList()
my_task.add_task("Выучить классы Python")
my_task.add_task("Выучить наследование Python")
my_task.add_task("Обед")

# my_task.remove_task(3)
my_task.info()

my_task.remove_task(3)
my_task.info()
my_task.done_task(2)
my_task.info()



