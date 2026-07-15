

class RussianBlue:
    bread = "Russian Blue"
    list_skills = []
    count = 0


    @classmethod
    def get_skills(cls):
        print(f"Список всех скилов экземпляров {cls.list_skills}")


    def __init__(self,name,age,skill):
        self.name = name
        self.age = age
        self.skill = skill
        self.list_skills.append(skill)
        RussianBlue.increment_count()

    @classmethod
    def increment_count(cls):  # Метод класса считает и вывод количество созданных экземпляров
        cls.count = cls.count + 1
        # print(f"Количество созданных котов(экземпляров): {cls.count_self}")

    @classmethod # Метод конструктор создатель экземпляра
    def set_cat_def(cls,name):
        cls.name = name
        cls.age = 4
        cls.skill = "Скилы тома конструктора"
        return cls(cls.name,cls.age,cls.skill)



    def sey_my(self):
        print(f"{self.name} говорит: Мяу - Мяу")


    def info(self):

        print(f"{self.bread} , {self.name}, {self.age} , {self.skill}")


    def set_bread(self,bread):
        self.bread = bread
        print(f"{self.name} - теперь {self.bread}")

    @classmethod
    def set_bread_class(cls,bread):
        cls.bread = bread
        print(f"теперь {cls.bread}")

    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def set_skill(self,skill):
        self.skill = skill

tom = RussianBlue("Tom",2,"Ловит мышей")
musya = RussianBlue("Муся",3,"Играет на гитаре")

# tom.info()

new_tom = RussianBlue.set_cat_def("nj")
new_tom.info()
