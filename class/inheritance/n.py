
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in m1:
    print(i)
print("------------")

strok = range(len(m1))
stolb = range(len(m1[0]))

for j in strok:
    l = []
    for i in m1:
        l.append(i[j])
    print(l)


# l1 = []
# for i in stolb: #Берём первый список в списке
#     new_lst = []
#     for j in range(len(m1)):
#         # print(f"{j} -> {i}")
#         new_lst.append(m1[j][i])
#     l1.append(new_lst)
#     # for j in range(len(m1)):

# print(l1)
