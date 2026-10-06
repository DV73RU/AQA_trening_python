class ValueDescriptor:
    """Класс дескриптора валидации типа данных """

    def __init__(self, val_type):
        # Сохраняем тип данный
        self.val_type = val_type

    def __set_name__(self, owner, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        val = instance.__dict__.get(self._name)
        print(f"Получили для '{self._name}' значение: {val}")
        return val

    def __set__(self, instance, value):

        if not isinstance(value, self.val_type):  # Если преданный тип данных не ожидаемый
            raise TypeError(f"Значение '{self._name}' не доступный тип данных {self.val_type}")

        # if value < 0:
        #     raise  ValueError(f"Значение '{value}' для '{self.__name}' не допустимо")

        instance.__dict__[self._name] = value  # Меняем значение


class NameDescriptor(ValueDescriptor):
    """Класс дескриптор имение пользователя заперт доступа из вне"""

    def __set__(self, instance, value):
        if self._name in instance.__dict__:
            raise AttributeError(f"'{self._name}' - Не изменяемое!")

        super().__set__(instance,value) # Вызовем метод родителя


class User:
    age = ValueDescriptor(int)
    height = ValueDescriptor(int | float)
    name = NameDescriptor(str)  # Передаём нужный тип, и флаг записываемости

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


user1 = User("Мотя", 0, 156)
print(user1.__dict__)
try:
    user1.name = "Коля"


except AttributeError as error:
    print(error)
user1.age = 19
user1.height = 157

print(user1.__dict__)
