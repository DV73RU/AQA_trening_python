class Matrix:
    def __init__(self,data):
        self.data = data

    def info(self):
        """Метод красиво выводит матрицу"""
        for ls in self.data:
            print(ls)

    def add(self,oser):
        """Метод складывает 2 матрицы"""

        # Принимает аргумент вторую матрицу
        res_matrix = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                res_matrix[i][j] = self.data[i][j] + oser[i][j]
        for i in res_matrix:
            print(i)

    def multiply_by(self,n):
        res = []
        for i in self.data:
            m1 = [x * n for x in i]
            res.append(m1)
        for i in res:
            print(i)

    def transpose(self):


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

m1.info()
m2.info()

m1.add(m2.data)

m1.multiply_by(2)
