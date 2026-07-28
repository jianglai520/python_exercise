# coding = UTf-8

#计算n个自然数的平方和

def power_fun(n):
    a = 0
    for i in range(1, n+1):
        a += i ** 2
    return a

print(power_fun(4))