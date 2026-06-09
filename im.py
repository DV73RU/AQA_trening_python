matrix = [[1,2,3],[4,4,5],[7,8,9]]
print(id(matrix))
print(id(matrix[0]))
print(id(matrix[1]))
print(id(matrix[2]))
row = matrix[1]
row[0] = 100

print(f"row - {id(row)}")