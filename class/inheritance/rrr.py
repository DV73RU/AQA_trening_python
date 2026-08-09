class User:
    """Класс User"""
    __slots__ = ("name","age")
    def __init__(self,name: str,age: int):
        self.name = name
        self.age = age


u = User("Иван",34)
print(u.age)

# print(u.__dict__)

print(u.__getstate__())