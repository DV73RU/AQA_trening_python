def generate_pairs(n:int)-> list:
    big_lst = []
    lst = []
    a = 0
    b = 0
    lst.append(a)
    lst.append(b)
    big_lst.append(lst)

    if n >= b >= a >= 0:
        lst.append(b)
        # lst.append(b)
    # big_lst.append(lst)

    return big_lst


print(generate_pairs(2))
