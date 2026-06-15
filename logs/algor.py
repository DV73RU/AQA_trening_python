n = [1,2,3,4,5,6,2,2,7,8,9]
lst = []
print(n)
counts = 0
# print(n.count(2)
for i, val in enumerate(n):
    if val % 2 == 0:
        counts = counts + 1
        lst.append(val)
        # print(val)
print(f"Соличество чётных: {counts}")

dst = {}
cou = 0
for key, v in enumerate(lst):
    cou = lst.count(v)
    dst.setdefault(v,cou)
for key, v in dst.items():
    print(f"{key} - {v} шт.")
# print(dst)

# print(lst)
