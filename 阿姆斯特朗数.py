#如果n位正整数等于其各位数字的n次方之和，则称该数为阿姆斯特朗数

n = int(input("请输入一个整数:"))

str_n = str(n)
len_n = len(str_n)

n_ = 0
for i in str_n:
    n_ += int(i) ** len_n
if n_ == n:
    print(f"{n}为阿姆斯特朗数")
else:
    print(f"{n}不是阿姆斯特朗数")

 