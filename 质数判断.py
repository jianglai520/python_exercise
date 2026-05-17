# coding = UTF-8

#质数判断

num = int(input("请输入一个数:"))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num}不是质数")
            break
    else:
        print(f"{num}是质数")
else:
    print(f"{num}不是质数")