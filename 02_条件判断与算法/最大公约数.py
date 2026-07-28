# 最大公约数

def func(n1:int, n2:int):
    n1_list = []
    n2_list = []

    for i in range(1, n1 + 1):
        if n1 % i == 0:
            n1_list.append(i)
        else:
            continue

    for j in range(1, n2 + 1):
        if n2 % j == 0:
            n2_list.append(j)
        else:
            continue

    n1_set = set(n1_list)
    n2_set = set(n2_list)


    return max(n1_set&n2_set)

print(func(12, 18))
print(func(12, 24))
print(func(23, 69))
