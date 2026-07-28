# 线性查找

def func(lst, x):
    for i in range(0, len(lst) - 1):
        if lst[i] == x:
            print(f"已经找到了{x}在{lst}中的位置！")
            return i

lst = [1, 2, 3, 4, 5, 6, 7]
print(func(lst, 3))