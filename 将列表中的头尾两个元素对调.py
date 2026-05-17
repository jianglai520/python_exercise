# 将列表中的头尾两个元素对调

def fun(ar):
    length = len(ar)

    temp = ar[0]
    ar[0] = ar[length - 1]
    ar[length - 1] = temp

    return ar

ar = [1, 2, 3, 4, 5, 5, 6]
print(fun(ar))

#该空行就空行