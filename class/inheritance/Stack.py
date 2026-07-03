class Stack:
    """Класс Стек"""
    def __init__(self):
        self.items = []

    def info(self):
        """Весть стек"""
        print(f"Стек: {self.items}")

    def dequeue(self):
        if len(self.items) == 0:
            print("Пусто в очереди")
        else:
            print(f"{self.items.pop(0)} вышел из очереди")

    def size(self):
        """Длина стека"""
        print(f"Размер: {len(self.items)}")

    def peek(self):
        if len(self.items) == 0:
            print("Пусто в очереди")
        else:
            print(f"Первый {self.items[0]}")

    def push(self,name:str):
        """Добавить на вершину стека (последний в списке)"""
        self.items.append(name)

