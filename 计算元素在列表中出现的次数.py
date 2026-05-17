# coding = UTF-8

#计算列表中元素出现的次数

a_list = [1, 2, 3, 4, 'hate', 'egg', 'egg', 2, 4, 4, 1, 'pig']
print(a_list.count(1))
print(a_list.count(4))
print(a_list.count('egg'))

def func(lst, n):
    count = 0
    for i in lst:
        if (i == n):
            count += 1
    return count

print(func([1, 2, 3, 4, 4, 4], 4))