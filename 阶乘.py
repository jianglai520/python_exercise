# coding = UTF-8

#计算一个数的阶乘

def func(n):
    num = 1
    for i in range(1, n +1):
        num *= i
    return num
    
print(func(4))