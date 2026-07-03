
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l1 = []
for i in range(len(m1[0])):
    new_lst = []
    for j in range(len(m1)):
        new_lst.append(m1[j][i])
    l1.append(new_lst)
    # for j in range(len(m1)):

print(l1)