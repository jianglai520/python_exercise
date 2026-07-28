# 最小公倍数

#暴力枚举
def func(n1:int, n2:int):
    for i in range(max(n1, n2), 10000000):
        if (i % n1 == 0) and (i % n2) == 0:           
            break
        else:
            continue

    return i

print(func(23, 24))