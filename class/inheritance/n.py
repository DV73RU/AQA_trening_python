
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m2= []

for i in  m1:
    m = [x*2 for x in i]
    m2.append(m)

print(m2)