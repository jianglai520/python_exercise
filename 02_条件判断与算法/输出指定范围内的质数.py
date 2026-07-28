# coding = UTF-8

#输出指定范围内的质数

primes = []

lower = int(input("输出区间最小值:"))
upper = int(input("输入区间最大值:"))

for i in range(lower, upper + 1):
    if i > 1:
        for num in range(2, i):
            if (i % num) == 0:
                break
        else:          
            primes.append(i)

print(f"{lower}到{upper}的质数为:{primes}")
            


            
