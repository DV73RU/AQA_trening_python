x,y,z = int(input()),int(input()),int(input())
ls = [x,y,z]
print(ls)
res = 0
for i in ls:
    if i > 0:
        res += res
print(res)