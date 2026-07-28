#比较三个数的大小

a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
c = int(input("请输入第三个数："))

if (a >= b):
    if (a >= c):
        max = a
    else:
        max = c
else:
    if ( b >= c):
        max = b
    else:
        max = c

print(f"max = {max}")
