class Stack:
    """Класс Стек"""
    def __init__(self):
        self.items = []

    def info(self):
        """Весть стек"""
        print(f"Стек: {self.items}")

    def peek(self):
        """Смотрим вершина стека (последенего в очереде) не забирая из неё"""
        if len(self.items) == 0:
            print("Пусто в стеке")
        else:
            print(f"Вершина :{self.items[-1]}")

    def size(self):
        """Длина стека"""
        print(f"Размер: {len(self.items)}")

    def pop(self):
        """Удалить с вершины стека (последнего в списке)"""
        if len(self.items) == 0:
            print("Пусто в стеке")
        else:
            print(f"{self.items.pop(-1)} убран с вершины")

    def push(self,name:str):
        """Добавить на вершину стека (последний в списке)"""
        self.items.append(name)

    def is_empty(self):
        """Проверка пустоты списка"""
        if len(self.items) == 0:
            print(f"Стек пустой")
        else:
            print("Стек с элементами")

v = Stack()
v.info()
v.is_empty()
v.push("Толя")
v.push("Коля")
v.info()

v.peek()
v.is_empty()