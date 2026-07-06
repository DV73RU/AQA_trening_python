class Matrix:
    def __init__(self,data:list):
        self.data = data

    def info(self):
        """Метод красиво выводит матрицу"""
        for ls in self.data:
            print(ls)

    def add(self,oser:list):
        """Метод складывает 2 матрицы"""
        # print(f"Прибавляемы список {oser.data}")
        # print(f"Первый - {self.data}")

        #Через компрессион
        res = [[self.data[i][j] + oser.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        # print(res)

        # Через цикл
        rows = len(self.data) # Количество строк в матрице (это количестов списков в списке
        cols = len(self.data[0]) # Количество столбцов (это количество элементов в списке)
        # print(f"Количecтво строк - {rows}")
        # print(f"Количесвтво стлобцов - {cols}")
        res = [[0 for _ in range(cols)] for _ in range(rows)] # Формируекм матрицу из нулей
        for i in range(rows):
            for j in range(cols):
                res[i][j] = self.data[i][j] + oser.data[i][j]


        for i in res:
            print(i)

    def multiply_by(self,n):
        """Метод умножает элементы матрице на число"""
        res = []
        for i in self.data:
            m1 = [x * n for x in i]
            res.append(m1)
        for i in res:
            print(i)

    def transpose(self):
        """Метод транспонирует матрицу
        Строки становятся столбцами
        """
        for i in self.data:
            print(i)
        print("-----------------")

        rows = range(len(self.data)) # Количкчтво строк (количество списков в списке)
        cols = range(len(self.data[0])) # Количество столбцов (количество элементов в списке)
        for j in rows:
            new_l = []
            for i in self.data:
                new_l.append(i[j])
            print(new_l)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# m1.info()
# m2.info()
#
m1.add(m2)
#
# m1.multiply_by(2)
m2.transpose()