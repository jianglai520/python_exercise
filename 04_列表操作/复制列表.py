# coding = UTF-8

#复制列表
#1
def copy_list(a):
    new_list = a[:]
    return new_list

print(copy_list([1, 2, 3, 4]))

#2
def copy_list(a):
    new_list = list(a)
    return new_list

print(copy_list([2, 3, 4, 5]))

#3
def cpy_list(c):
    new_list = []
    new_list.extend(c)
    return new_list

print(cpy_list([3, 4]))