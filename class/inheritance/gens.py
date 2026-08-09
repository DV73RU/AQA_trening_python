from datetime import datetime as dt

class Player:
    _LVL, _HEALTH = 1, 100
    _slots_ = ["__lvl","__health","__born"]

    def __init__(self):
        self.__lvl = Player._LVL
        self.__health = Player._HEALTH
        self.__born = dt.now()


    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__born}'

    @lvl.setter
    def lvl(self,numeric):
        self.__lvl += Player.__type_test(numeric)
        if self.__lvl >= 100: self.__lvl = 100


    @classmethod
    def set_cls_field(cls,lvl=1,health = 100):
        cls._LVL = Player.__type_test(lvl)
        cls._HEALTH = Player.__type_test(health)

    @staticmethod
    def __type_test(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError("Должно быть число")
