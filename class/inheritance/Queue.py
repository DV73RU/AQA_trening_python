class Queue:
    """Класс очередь"""
    def __init__(self):
        self.items = []
    def info(self):
        print(f"Очередь: {self.items}")

    def dequeue(self):
        if len(self.items) == 0:
            print("Пусто в очереди")
        else:
            print(f"{self.items.pop(0)} вышел из очереди")

    def size(self):
        print(f"Размер: {len(self.items)}")

    def peek(self):
        if len(self.items) == 0:
            print("Пусто в очереди")
        else:
            print(f"Первый {self.items[0]}")

    def enqueue(self,name:str):
        self.items.append(name)


o = Queue()

o.info()
# o.peek()
o.size()
o.dequeue()
o.peek()
o.info()
o.enqueue("Марина")
o.info()