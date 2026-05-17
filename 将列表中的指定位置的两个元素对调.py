# 将列表中的指定位置的两个元素对调


def func(ar, i, j):
    length = len(ar)

    if 0 <= i < length and 0 <= j <length:
        temp = ar[i]
        ar[i] = ar[j]
        ar[j] = temp
    else:
        print("输入参数错误!")

    return ar

ar = [1, 2, 3, 4, 5, 6, 7, 8]
print(func(ar, 1, 2))